#!/usr/bin/env python3
"""Loss-accountable Telegram candidate intake with exact approval/apply boundaries."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path
from typing import Callable
from urllib.parse import urlsplit

try:
    from . import generate_readme, validate_links, validate_schema
except ImportError:  # Direct script execution.
    import generate_readme
    import validate_links
    import validate_schema

CANONICAL_PROFILE = "kz-canonical-json/v1"
SOURCE_VERSION = "kz-intake-source/v1"
PREVIEW_VERSION = "kz-intake-preview/v1"
APPROVAL_VERSION = "kz-intake-approval/v1"
MARKER_VERSION = "kz-intake-pending/v1"
RECEIPT_VERSION = "kz-intake-receipt/v1"
CONTROLLED_PATHS = (
    "data/communities.json", "README.md", "index.md", "ru/index.md", "kk/index.md"
)
SAFE_INTEGER = 9_007_199_254_740_991
HANDLE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{4,31}$")
TOKEN_RE = re.compile(
    r"(?i)(?:https?://[^\s<>\"']+|tg:(?://)?[^\s<>\"']+|"
    r"(?:[a-z0-9_-]+\.)*(?:t\.me|telegram\.me|telegram\.dog)(?::\d+)?(?:/[^\s<>\"']*)?)"
)
ROOT_HOSTS = {"t.me", "telegram.me", "telegram.dog"}
RESERVED = {
    "addstickers", "c", "confirmphone", "contact", "iv", "joinchat", "login",
    "proxy", "s", "setlanguage", "share", "socks"
}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


class IntakeError(ValueError):
    """Fail-closed intake contract violation."""


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _duplicate_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise IntakeError(f"duplicate field: {key}")
        result[key] = value
    return result


def _integer(token: str) -> int:
    if token == "-0":
        raise IntakeError("lexical -0 is forbidden")
    value = int(token)
    if abs(value) > SAFE_INTEGER:
        raise IntakeError("unsafe integer")
    return value


def _forbidden_number(token: str) -> object:
    raise IntakeError(f"float/exponent/non-finite number is forbidden: {token}")


def validate_json_value(value: object, path: str = "$") -> None:
    if value is None or isinstance(value, bool):
        return
    if isinstance(value, int):
        if abs(value) > SAFE_INTEGER:
            raise IntakeError(f"{path}: unsafe integer")
        return
    if isinstance(value, float):
        raise IntakeError(f"{path}: floats are forbidden")
    if isinstance(value, str):
        try:
            value.encode("utf-8", errors="strict")
        except UnicodeEncodeError as error:
            raise IntakeError(f"{path}: invalid Unicode") from error
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            validate_json_value(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str) or not key.isascii() or not key:
                raise IntakeError(f"{path}: object keys must be non-empty ASCII")
            validate_json_value(item, f"{path}.{key}")
        return
    raise IntakeError(f"{path}: unsupported JSON value {type(value).__name__}")


def parse_closed_json(text: str) -> object:
    try:
        value = json.loads(
            text, object_pairs_hook=_duplicate_object, parse_int=_integer,
            parse_float=_forbidden_number, parse_constant=_forbidden_number,
        )
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise IntakeError(f"invalid JSON: {error}") from error
    validate_json_value(value)
    return value


def canonical_bytes(value: object) -> bytes:
    validate_json_value(value)
    return (json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ) + "\n").encode("utf-8", errors="strict")


def _exact(value: object, schema: object, path: str = "$") -> None:
    if isinstance(schema, dict):
        if not isinstance(value, dict) or set(value) != set(schema):
            actual = sorted(value) if isinstance(value, dict) else type(value).__name__
            raise IntakeError(f"{path}: fields differ; got {actual}")
        for key, child in schema.items():
            _exact(value[key], child, f"{path}.{key}")
    elif isinstance(schema, list):
        if not isinstance(value, list):
            raise IntakeError(f"{path}: expected array")
        for index, item in enumerate(value):
            _exact(item, schema[0], f"{path}[{index}]")
    elif isinstance(schema, tuple):
        if not any((type(value) is int if expected is int else isinstance(value, expected))
                   for expected in schema):
            raise IntakeError(f"{path}: expected {'/'.join(t.__name__ for t in schema)}")
    elif schema is None:
        if value is not None:
            raise IntakeError(f"{path}: expected null")
    elif (type(value) is not int if schema is int else not isinstance(value, schema)):
        raise IntakeError(f"{path}: expected {schema.__name__}")


OCCURRENCE_SCHEMA = {
    "occurrence_id": str, "source_id": str, "ordinal": int, "byte_start": int,
    "byte_end": int, "raw_text": str, "raw_utf8_hex": str, "url_text": str,
    "trimmed_suffix": str, "link_kind": str, "candidate_id": (str, type(None)),
}
CANDIDATE_SCHEMA = {"candidate_id": str, "handle": str, "occurrence_ids": [str]}
SOURCE_SCHEMA = {
    "schema_version": str, "source_id": str, "source_sha256": str, "source_bytes": int,
    "occurrences": [OCCURRENCE_SCHEMA], "candidates": [CANDIDATE_SCHEMA],
    "totals": {"occurrences": int, "candidates": int, "non_candidates": int},
}
TYPE_RESULT_SCHEMA = {
    "declared_type": str, "classification": str, "reason": str,
    "observed_type": (str, type(None)), "target_bound": bool,
    "visible_name": (str, type(None)), "member_count": (int, type(None)),
    "archive_candidate": bool,
}
OBSERVATION_SCHEMA = {
    "candidate_id": str, "requested_handle": str, "status": str, "reason": str,
    "canonical_handle": (str, type(None)), "observed_type": (str, type(None)),
    "visible_name": (str, type(None)), "member_count": (int, type(None)),
    "target_bound": bool, "observed_at": str, "source_classification": str,
    "body_sha256": (str, type(None)),
    "transport": {"ok": bool, "reason": str, "status_code": (int, type(None)), "attempts": int},
    "type_results": [TYPE_RESULT_SCHEMA],
}
COLLISION_SCHEMA = {
    "candidate_id": str, "status": str, "matched_handles": [str],
    "cross_input_duplicate": bool,
}
EDITORIAL_SCHEMA = {
    "candidate_id": str, "it_relevant": bool, "kazakhstan_relevant": bool,
    "purely_commercial": bool, "category_valid": bool, "locales_complete": bool,
    "evidence_refs": [str],
}
ENTRY_SCHEMA = {
    "type": str, "name": str, "handle": str, "description": str,
    "description_ru": str, "description_kk": str, "category": str,
    "last_verified": str, "member_count": (int, type(None)),
}
ACTION_SCHEMA = {
    "candidate_id": str, "action": str, "reason": str,
    "proposed_entry": (dict, type(None)),
}
PATH_SCHEMA = {"path": str, "before_sha256": str, "after_sha256": str}
PREVIEW_SCHEMA = {
    "schema_version": str, "canonical_profile": str,
    "contracts": {"source": str, "observation": str, "authority": str, "apply": str},
    "source": SOURCE_SCHEMA, "collisions": [COLLISION_SCHEMA],
    "observations": [OBSERVATION_SCHEMA], "editorial": [EDITORIAL_SCHEMA],
    "actions": [ACTION_SCHEMA], "controlled_paths": [PATH_SCHEMA],
    "totals": {
        "occurrences": int, "candidates": int, "observed": int, "add": int,
        "reject": int, "duplicate": int, "unresolved": int,
    },
}
APPROVAL_SCHEMA = {
    "schema_version": str, "canonical_profile": str, "payload_sha256": str,
    "actions_sha256": str, "approved_candidate_ids": [str], "owner_handle": str,
    "owner_evidence_ref": str, "approved_at": str,
}


def _telegram_like(token: str) -> bool:
    folded = token.casefold()
    return folded.startswith("tg:") or any(host in folded for host in ROOT_HOSTS)


def classify_token(token: str) -> tuple[str, str | None]:
    if not token or any(ord(char) < 32 for char in token) or "\\" in token:
        return "malformed", None
    if "%" in token:
        return "percent_encoded", None
    try:
        parsed = urlsplit(token)
    except ValueError:
        return "malformed", None
    if parsed.scheme.casefold() != "https":
        return "unsupported_scheme", None
    if parsed.username or parsed.password:
        return "userinfo", None
    try:
        if parsed.port is not None:
            return "port", None
    except ValueError:
        return "port", None
    host = (parsed.hostname or "").casefold()
    if host not in ROOT_HOSTS:
        if any(root in host for root in ROOT_HOSTS):
            return "spoofed_authority", None
        return "unsupported_host", None
    parts = [part for part in parsed.path.split("/") if part]
    if not parts:
        return "missing_handle", None
    first = parts[0]
    folded = first.casefold()
    if first.startswith("+") or folded == "joinchat":
        return "private_invite", None
    if first.isdigit():
        return "phone", None
    if folded in RESERVED:
        return "reserved_action", None
    if len(parts) != 1:
        return "message_path", None
    if parsed.query or parsed.fragment:
        return "query_or_fragment", None
    if parsed.path not in {f"/{first}", f"/{first}/"}:
        return "unsupported_path", None
    if not HANDLE_RE.fullmatch(first):
        return "invalid_handle", None
    return "candidate", first


def parse_source(text: str, source_id: str = "text") -> dict[str, object]:
    raw_bytes = text.encode("utf-8", errors="strict")
    occurrences: list[dict[str, object]] = []
    groups: dict[str, dict[str, object]] = {}
    for match in TOKEN_RE.finditer(text):
        raw = match.group(0)
        if not _telegram_like(raw):
            continue
        trimmed = raw.rstrip(").,;!]}>")
        suffix = raw[len(trimmed):]
        start = len(text[:match.start()].encode("utf-8"))
        end = start + len(raw.encode("utf-8"))
        kind, handle = classify_token(trimmed)
        candidate_id = f"candidate:{handle.casefold()}" if handle else None
        occurrence_id = f"occurrence:{len(occurrences) + 1:04d}"
        occurrences.append({
            "occurrence_id": occurrence_id, "source_id": source_id,
            "ordinal": len(occurrences) + 1, "byte_start": start, "byte_end": end,
            "raw_text": raw, "raw_utf8_hex": raw.encode("utf-8").hex(),
            "url_text": trimmed, "trimmed_suffix": suffix, "link_kind": kind,
            "candidate_id": candidate_id,
        })
        if candidate_id:
            group = groups.setdefault(candidate_id, {
                "candidate_id": candidate_id, "handle": handle, "occurrence_ids": []
            })
            group["occurrence_ids"].append(occurrence_id)
    candidates = sorted(groups.values(), key=lambda item: str(item["candidate_id"]))
    result: dict[str, object] = {
        "schema_version": SOURCE_VERSION, "source_id": source_id,
        "source_sha256": sha256_bytes(raw_bytes), "source_bytes": len(raw_bytes),
        "occurrences": occurrences, "candidates": candidates,
        "totals": {"occurrences": len(occurrences), "candidates": len(candidates),
                   "non_candidates": sum(row["candidate_id"] is None for row in occurrences)},
    }
    validate_source(result)
    return result


def observe_candidate(
    handle: str,
    fetcher: Callable[[str], validate_links.FetchResult] = validate_links.fetch_preview_with_retry,
    observed_at: str | None = None,
) -> dict[str, object]:
    fetched = fetcher(handle)
    transport = {
        "ok": fetched.ok, "reason": fetched.reason, "status_code": fetched.status_code,
        "attempts": fetched.attempts,
    }
    base: dict[str, object] = {
        "candidate_id": f"candidate:{handle.casefold()}", "requested_handle": handle,
        "status": "unresolved", "reason": fetched.reason, "canonical_handle": None,
        "observed_type": None, "visible_name": None, "member_count": None,
        "target_bound": False, "observed_at": observed_at or date.today().isoformat(),
        "source_classification": "public_telegram_preview", "body_sha256": None,
        "transport": transport, "type_results": [],
    }
    if not fetched.ok or fetched.body is None:
        _exact(base, OBSERVATION_SCHEMA)
        return base
    html = fetched.body.decode("utf-8", errors="ignore")
    base["body_sha256"] = sha256_bytes(fetched.body)
    results = [validate_links.classify_response(html, handle, kind) for kind in validate_links.ENTRY_TYPES]
    base["type_results"] = results
    verified = [row for row in results if row["classification"] == "verified"]
    mismatches = [
        row for row in results
        if row["classification"] == "ambiguous" and row["reason"] == "declared_type_mismatch"
        and row["target_bound"]
    ]
    if len(verified) == 1 and len(mismatches) == 2 and all(
        row["observed_type"] == verified[0]["declared_type"] for row in mismatches
    ):
        accepted = verified[0]
        base.update({
            "status": "verified", "reason": "one_verified_two_bound_mismatches",
            "canonical_handle": handle, "observed_type": accepted["observed_type"],
            "visible_name": accepted["visible_name"], "member_count": accepted["member_count"],
            "target_bound": True,
        })
    else:
        base["reason"] = "type_reconciliation_failed"
    _exact(base, OBSERVATION_SCHEMA)
    return base


def catalog_collisions(source: dict[str, object], catalog: dict[str, object]) -> list[dict[str, object]]:
    live: dict[str, list[str]] = {}
    archived: dict[str, list[str]] = {}
    for kind in validate_links.ENTRY_TYPES:
        for entry in catalog.get(kind, []):
            live.setdefault(str(entry["handle"]).casefold(), []).append(str(entry["handle"]))
    for entry in catalog.get("archive", []):
        archived.setdefault(str(entry["handle"]).casefold(), []).append(str(entry["handle"]))
    output = []
    for candidate in source["candidates"]:
        key = str(candidate["handle"]).casefold()
        matches = sorted(set(live.get(key, []) + archived.get(key, [])), key=str.casefold)
        status = "clear"
        if key in live and key in archived:
            status = "multiple"
        elif key in live:
            status = "live"
        elif key in archived:
            status = "archive"
        output.append({"candidate_id": candidate["candidate_id"], "status": status,
                       "matched_handles": matches,
                       "cross_input_duplicate": len(candidate["occurrence_ids"]) > 1})
    return output


def path_hashes(root: Path) -> dict[str, str]:
    return {path: file_sha256(root / path) for path in CONTROLLED_PATHS}


def actions_sha256(actions: list[dict[str, object]]) -> str:
    return sha256_bytes(canonical_bytes(actions))


def validate_source(source: dict[str, object]) -> None:
    _exact(source, SOURCE_SCHEMA)
    if source["schema_version"] != SOURCE_VERSION or not SHA_RE.fullmatch(source["source_sha256"]):
        raise IntakeError("unsupported or malformed source contract")
    occurrences = source["occurrences"]
    expected_groups: dict[str, list[str]] = {}
    for index, row in enumerate(occurrences, 1):
        if row["ordinal"] != index or row["occurrence_id"] != f"occurrence:{index:04d}":
            raise IntakeError("occurrence order/id differs")
        if not 0 <= row["byte_start"] < row["byte_end"] <= source["source_bytes"]:
            raise IntakeError("occurrence byte range differs")
        try:
            encoded = bytes.fromhex(row["raw_utf8_hex"])
        except ValueError as error:
            raise IntakeError("occurrence raw bytes are invalid") from error
        if encoded.decode("utf-8") != row["raw_text"] or len(encoded) != row["byte_end"] - row["byte_start"]:
            raise IntakeError("occurrence raw byte/text binding differs")
        kind, handle = classify_token(row["url_text"])
        candidate_id = f"candidate:{handle.casefold()}" if handle else None
        if (kind, candidate_id) != (row["link_kind"], row["candidate_id"]):
            raise IntakeError("occurrence disposition/reference differs")
        if candidate_id:
            expected_groups.setdefault(candidate_id, []).append(row["occurrence_id"])
    expected_candidates = [
        {"candidate_id": candidate_id, "handle": next(
            row["url_text"].rstrip("/").rsplit("/", 1)[-1] for row in occurrences
            if row["candidate_id"] == candidate_id
        ), "occurrence_ids": refs}
        for candidate_id, refs in sorted(expected_groups.items())
    ]
    actual = source["candidates"]
    if [row["candidate_id"] for row in actual] != [row["candidate_id"] for row in expected_candidates]:
        raise IntakeError("candidate order/reference differs")
    for row, expected in zip(actual, expected_candidates):
        if row["handle"].casefold() != expected["handle"].casefold() or row["occurrence_ids"] != expected["occurrence_ids"]:
            raise IntakeError("candidate grouping differs")
    totals = {"occurrences": len(occurrences), "candidates": len(actual),
              "non_candidates": sum(row["candidate_id"] is None for row in occurrences)}
    if source["totals"] != totals:
        raise IntakeError("source totals differ")


def validate_observation(row: dict[str, object]) -> None:
    _exact(row, OBSERVATION_SCHEMA)
    if row["candidate_id"] != f"candidate:{row['requested_handle'].casefold()}" or \
            row["source_classification"] != "public_telegram_preview":
        raise IntakeError("observation identity/source differs")
    try:
        date.fromisoformat(row["observed_at"])
    except ValueError as error:
        raise IntakeError("observation date is invalid") from error
    if row["body_sha256"] is not None and not SHA_RE.fullmatch(row["body_sha256"]):
        raise IntakeError("observation body digest is invalid")
    transport = row["transport"]
    if not 1 <= transport["attempts"] <= validate_links.RETRY_ATTEMPTS:
        raise IntakeError("observation transport attempts differ")
    results = row["type_results"]
    if transport["ok"]:
        if transport["reason"] != "fetched" or not isinstance(transport["status_code"], int) or \
                not 200 <= transport["status_code"] < 300 or row["body_sha256"] is None or len(results) != 3:
            raise IntakeError("successful transport/body tuple differs")
    else:
        reason = transport["reason"]
        status = transport["status_code"]
        possible_reason = (
            transport["attempts"] == validate_links.RETRY_ATTEMPTS
            and (reason == "max_retries_exceeded" or reason.startswith(("url_error:", "error:")))
        ) if status is None else (
            transport["attempts"] == 1 and status != 429 and not 200 <= status < 300
            and reason == f"http_{status}"
        )
        if row["body_sha256"] is not None or results or not possible_reason:
            raise IntakeError("failed transport exposes body/result facts")
    if results and [item["declared_type"] for item in results] != list(validate_links.ENTRY_TYPES):
        raise IntakeError("typed result order differs")
    verified = [item for item in results if item["classification"] == "verified"]
    accepted = len(verified) == 1 and all(
        item == (validate_links.result(
            "verified", "target_preview_verified", item["declared_type"],
            verified[0]["member_count"], verified[0]["visible_name"],
            verified[0]["declared_type"], True) if item is verified[0] else validate_links.result(
                "ambiguous", "declared_type_mismatch", item["declared_type"], None,
                verified[0]["visible_name"], verified[0]["declared_type"], True))
        for item in results
    ) and isinstance(verified[0]["visible_name"], str) and bool(verified[0]["visible_name"].strip()) \
        and (verified[0]["member_count"] is None or verified[0]["member_count"] >= 0)
    if results and not accepted:
        early = {
            ("failed", "telegram_error_marker"): (False, False),
            ("failed", "deleted_marker"): (False, False),
            ("ambiguous", "contact_shell_without_preview"): (False, False),
            ("non_target", "no_target_preview"): (False, False),
            ("ambiguous", "conflicting_target_identity"): (False, True),
            ("ambiguous", "conflicting_preview_identity_text"): (False, True),
            ("non_target", "preview_does_not_bind_requested_handle"): (False, True),
            ("ambiguous", "declared_type_not_established"): (True, True),
        }
        target_bound, named = early.get((results[0]["classification"], results[0]["reason"]), (None, None))
        common = {key: results[0][key] for key in TYPE_RESULT_SCHEMA if key != "declared_type"}
        valid_name = isinstance(common["visible_name"], str) and bool(common["visible_name"].strip()) \
            if named else common["visible_name"] is None
        if target_bound is None or any(
                {key: item[key] for key in TYPE_RESULT_SCHEMA if key != "declared_type"} != common
                for item in results) or common["target_bound"] != target_bound or \
                common["observed_type"] is not None or common["member_count"] is not None or \
                common["archive_candidate"] or not valid_name:
            raise IntakeError("typed classifier tuple is impossible")
    if row["status"] == "verified":
        if not accepted or row["reason"] != "one_verified_two_bound_mismatches" or \
                row["canonical_handle"] != row["requested_handle"] or not row["target_bound"] or \
                any(row[field] != verified[0][field] for field in
                    ("observed_type", "visible_name", "member_count")):
            raise IntakeError("verified observation tuple differs")
    elif accepted or row["status"] != "unresolved" or any(row[field] is not None for field in
                                               ("canonical_handle", "observed_type", "visible_name", "member_count")) \
            or row["target_bound"] or row["reason"] != (
                "type_reconciliation_failed" if transport["ok"] else transport["reason"]):
        raise IntakeError("unresolved observation exposes downstream facts")


def validate_preview(preview: dict[str, object]) -> None:
    _exact(preview, PREVIEW_SCHEMA)
    if preview["schema_version"] != PREVIEW_VERSION or preview["canonical_profile"] != CANONICAL_PROFILE:
        raise IntakeError("unsupported preview contract")
    validate_source(preview["source"])
    ids = [row["candidate_id"] for row in preview["source"]["candidates"]]
    if len(ids) != len(set(ids)):
        raise IntakeError("duplicate candidate IDs")
    for field in ("collisions", "observations", "editorial", "actions"):
        rows = preview[field]
        if [row["candidate_id"] for row in rows] != ids:
            raise IntakeError(f"{field} must have one ordered row per candidate")
    for candidate, observation in zip(preview["source"]["candidates"], preview["observations"]):
        if observation["requested_handle"] != candidate["handle"]:
            raise IntakeError("observation/source identity differs")
        validate_observation(observation)
    if [row["path"] for row in preview["controlled_paths"]] != list(CONTROLLED_PATHS):
        raise IntakeError("controlled path inventory/order differs")
    for row in preview["controlled_paths"]:
        if not SHA_RE.fullmatch(row["before_sha256"]) or not SHA_RE.fullmatch(row["after_sha256"]):
            raise IntakeError("invalid controlled-path digest")
    observations = {row["candidate_id"]: row for row in preview["observations"]}
    collisions = {row["candidate_id"]: row for row in preview["collisions"]}
    editorial = {row["candidate_id"]: row for row in preview["editorial"]}
    if any(not ref.strip() for row in preview["editorial"] for ref in row["evidence_refs"]):
        raise IntakeError("editorial evidence references must be non-blank")
    allowed = {"add", "reject", "duplicate", "unresolved"}
    for action in preview["actions"]:
        if action["action"] not in allowed or not action["reason"].strip():
            raise IntakeError("invalid action")
        entry = action["proposed_entry"]
        if action["action"] == "add":
            _exact(entry, ENTRY_SCHEMA, "$.actions.proposed_entry")
            gate = editorial[action["candidate_id"]]
            if observations[action["candidate_id"]]["status"] != "verified" or \
                    collisions[action["candidate_id"]]["status"] != "clear" or not (
                        gate["it_relevant"] and gate["kazakhstan_relevant"]
                        and not gate["purely_commercial"] and gate["category_valid"]
                        and gate["locales_complete"] and gate["evidence_refs"]):
                raise IntakeError("add action does not pass every gate")
            observation = observations[action["candidate_id"]]
            if any(entry[field] != observation[observed] for field, observed in (
                    ("type", "observed_type"), ("name", "visible_name"),
                    ("handle", "canonical_handle"), ("last_verified", "observed_at"),
                    ("member_count", "member_count"))):
                raise IntakeError("proposed entry differs from observation")
        elif entry is not None:
            raise IntakeError("only add actions may carry proposed entries")
    counts = {name: sum(row["action"] == name for row in preview["actions"])
              for name in allowed}
    expected = {
        "occurrences": preview["source"]["totals"]["occurrences"], "candidates": len(ids),
        "observed": len(preview["observations"]), **counts,
    }
    if preview["totals"] != expected:
        raise IntakeError("preview totals differ")


def build_preview(
    source: dict[str, object], collisions: list[dict[str, object]],
    observations: list[dict[str, object]], editorial: list[dict[str, object]],
    actions: list[dict[str, object]], root: Path, stage_root: Path,
) -> dict[str, object]:
    before = path_hashes(root)
    after = validate_action_stage(root, stage_root, actions)
    ids = [row["candidate_id"] for row in source["candidates"]]
    order = {candidate_id: index for index, candidate_id in enumerate(ids)}
    sort_rows = lambda rows: sorted(rows, key=lambda row: order[row["candidate_id"]])
    actions = sort_rows(actions)
    preview: dict[str, object] = {
        "schema_version": PREVIEW_VERSION, "canonical_profile": CANONICAL_PROFILE,
        "contracts": {"source": SOURCE_VERSION, "observation": "fetch-once-classifier/v1",
                      "authority": APPROVAL_VERSION, "apply": "controlled-path-bax/v1"},
        "source": source, "collisions": sort_rows(collisions),
        "observations": sort_rows(observations), "editorial": sort_rows(editorial),
        "actions": actions,
        "controlled_paths": [{"path": path, "before_sha256": before[path],
                              "after_sha256": after[path]} for path in CONTROLLED_PATHS],
        "totals": {"occurrences": source["totals"]["occurrences"], "candidates": len(ids),
                   "observed": len(observations),
                   **{name: sum(row["action"] == name for row in actions)
                      for name in ("add", "reject", "duplicate", "unresolved")}},
    }
    validate_preview(preview)
    return preview


def preview_sha256(preview: dict[str, object]) -> str:
    validate_preview(preview)
    return sha256_bytes(canonical_bytes(preview))


def render_preview(preview: dict[str, object]) -> str:
    validate_preview(preview)
    lines = [
        "# KZ Add Preview", "", f"Payload SHA-256: `{preview_sha256(preview)}`", "",
        "| Candidate | Observation | Editorial | Action | Reason |", "|---|---|---|---|---|",
    ]
    observed = {row["candidate_id"]: row for row in preview["observations"]}
    editorial = {row["candidate_id"]: row for row in preview["editorial"]}
    for action in preview["actions"]:
        gate = editorial[action["candidate_id"]]
        gate_text = "/".join(("IT" if gate["it_relevant"] else "non-IT",
                              "KZ" if gate["kazakhstan_relevant"] else "non-KZ",
                              "commercial" if gate["purely_commercial"] else "non-commercial",
                              "locales" if gate["locales_complete"] else "locales-missing"))
        lines.append(f"| `{action['candidate_id']}` | {observed[action['candidate_id']]['status']} | "
                     f"{gate_text} | {action['action']} | {action['reason']} |")
    lines.extend(("", "## Exact significant payload", "", "```json",
                  canonical_bytes(preview).decode("utf-8").rstrip("\n"), "```", ""))
    return "\n".join(lines)


def validate_approval(
    preview: dict[str, object], approval: dict[str, object], current_owner_refs: set[str]
) -> None:
    _exact(approval, APPROVAL_SCHEMA)
    expected_ids = sorted(row["candidate_id"] for row in preview["actions"] if row["action"] == "add")
    if approval["schema_version"] != APPROVAL_VERSION or approval["canonical_profile"] != CANONICAL_PROFILE:
        raise IntakeError("unsupported approval contract")
    if approval["payload_sha256"] != preview_sha256(preview):
        raise IntakeError("approval payload differs")
    if approval["actions_sha256"] != actions_sha256(preview["actions"]):
        raise IntakeError("approval action projection differs")
    if approval["approved_candidate_ids"] != expected_ids:
        raise IntakeError("approval must bind the exact add set")
    if not approval["owner_handle"].strip() or approval["owner_evidence_ref"] not in current_owner_refs:
        raise IntakeError("current durable owner evidence is absent")


def validate_staged_project(stage_root: Path) -> list[str]:
    commands = ((sys.executable, "scripts/validate_schema.py"),
                (sys.executable, "scripts/generate_readme.py", "--check"))
    results = []
    for command in commands:
        completed = subprocess.run(command, cwd=stage_root, text=True, capture_output=True)
        if completed.returncode:
            raise IntakeError(f"staged validation failed: {' '.join(command)}\n{completed.stdout}{completed.stderr}")
        results.append(" ".join(command[1:]))
    return results


def expected_action_stage(root: Path, actions: list[dict[str, object]]) -> dict[str, bytes]:
    """Derive exact project bytes for baseline plus only the proposed add rows."""
    baseline_body = (root / CONTROLLED_PATHS[0]).read_bytes()
    add_actions = [action for action in actions if action["action"] == "add"]
    if not add_actions:
        return {path: (root / path).read_bytes() for path in CONTROLLED_PATHS}
    baseline = parse_closed_json(baseline_body.decode("utf-8"))
    if not isinstance(baseline, dict):
        raise IntakeError("catalog must be an object")
    expected = copy.deepcopy(baseline)
    for action in add_actions:
        proposed = dict(action["proposed_entry"])
        entry_type = proposed.pop("type")
        if entry_type not in validate_links.ENTRY_TYPES or not isinstance(expected.get(entry_type), list):
            raise IntakeError("proposed catalog type differs")
        expected[entry_type].append(proposed)
    review = expected.get("localization_review")
    if not isinstance(review, dict):
        raise IntakeError("localization review binding is absent")
    review["changed_key_count"] = len(validate_schema.review_payload_keys(expected))
    review["payload_sha256"] = validate_schema.review_payload_sha256(expected)
    expected_data = (json.dumps(expected, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if baseline_body != (json.dumps(baseline, ensure_ascii=False, indent=2) + "\n").encode("utf-8"):
        raise IntakeError("baseline catalog serialization differs from project format")
    generated = generate_readme.generated_outputs(expected)
    return {CONTROLLED_PATHS[0]: expected_data, **{
        path: generated[generate_readme.PROJECT_ROOT / path].encode("utf-8")
        for path in CONTROLLED_PATHS[1:]
    }}


def validate_action_stage(root: Path, stage_root: Path,
                          actions: list[dict[str, object]]) -> dict[str, str]:
    """Prove all staged bytes are the exact mechanically derived action result."""
    expected = expected_action_stage(root, actions)
    for path, body in expected.items():
        if (stage_root / path).read_bytes() != body:
            raise IntakeError(f"staged bytes are not the exact action result: {path}")
    return path_hashes(stage_root)


def recheck_catalog_gates(root: Path, preview: dict[str, object]) -> None:
    catalog = json.loads((root / "data/communities.json").read_text(encoding="utf-8"))
    occupied = {
        str(entry.get("handle", "")).casefold()
        for kind in (*validate_links.ENTRY_TYPES, "archive")
        for entry in catalog.get(kind, [])
    }
    categories = set(catalog.get("categories", {}))
    observations = {row["candidate_id"]: row for row in preview["observations"]}
    for action in preview["actions"]:
        if action["action"] != "add":
            continue
        observation = observations[action["candidate_id"]]
        entry = action["proposed_entry"]
        if observation["observed_at"] != date.today().isoformat():
            raise IntakeError("add observation is not fresh for apply day")
        if entry["handle"].casefold() in occupied:
            raise IntakeError("add handle now collides with live/archive catalog")
        if entry["handle"].casefold() != observation["requested_handle"].casefold() or \
                entry["handle"].casefold() != observation["canonical_handle"].casefold():
            raise IntakeError("proposed identity differs from bound observation")
        if entry["type"] != observation["observed_type"] or entry["name"] != observation["visible_name"]:
            raise IntakeError("proposed type/name differs from observation")
        if entry["last_verified"] != observation["observed_at"] or \
                entry["member_count"] != observation["member_count"]:
            raise IntakeError("proposed date/count differs from observation")
        if entry["type"] not in validate_links.ENTRY_TYPES or entry["category"] not in categories:
            raise IntakeError("proposed type/category is invalid")
        if any(not str(entry[field]).strip() for field in ("description", "description_ru", "description_kk")):
            raise IntakeError("proposed locales are incomplete")


def _atomic_write(path: Path, body: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.kz-intake.tmp")
    temporary.write_bytes(body)
    os.replace(temporary, path)


def _marker(preview: dict[str, object], approval: dict[str, object]) -> dict[str, object]:
    payload = preview_sha256(preview)
    authority = sha256_bytes(canonical_bytes(approval))
    return {"schema_version": MARKER_VERSION, "canonical_profile": CANONICAL_PROFILE,
            "payload_sha256": payload, "approval_sha256": authority,
            "execution_id": sha256_bytes(f"{payload}:{authority}".encode("ascii"))}


def apply_preview(
    root: Path, stage_root: Path, preview: dict[str, object], approval: dict[str, object],
    current_owner_refs: set[str], pending_path: Path,
    preflight: Callable[[Path], list[str]] = validate_staged_project,
    fail_after: int | None = None,
) -> dict[str, object]:
    validate_approval(preview, approval, current_owner_refs)
    expected = {row["path"]: row for row in preview["controlled_paths"]}
    staged = {path: (stage_root / path).read_bytes() for path in CONTROLLED_PATHS}
    if any(sha256_bytes(staged[path]) != expected[path]["after_sha256"] for path in CONTROLLED_PATHS):
        raise IntakeError("staged bytes differ from preview")
    state = []
    for path in CONTROLLED_PATHS:
        current = file_sha256(root / path)
        before = expected[path]["before_sha256"]
        after = expected[path]["after_sha256"]
        if before == after:
            state.append("N" if current == before else "X")
        else:
            state.append("B" if current == before else "A" if current == after else "X")
    changing_state = {item for item in state if item != "N"}
    marker = _marker(preview, approval)
    existing_marker = None
    if pending_path.exists():
        existing_marker = parse_closed_json(pending_path.read_text(encoding="utf-8"))
        if existing_marker != marker:
            raise IntakeError("pending marker differs")
    if "X" in state or ({"B", "A"} <= changing_state and existing_marker is None):
        raise IntakeError("unknown or unmarked mixed controlled-path state")
    if "B" in changing_state or not changing_state:
        if "B" in changing_state and state[0] != "B":
            raise IntakeError("recovery lacks the bound baseline catalog")
        if validate_action_stage(root, stage_root, preview["actions"]) != {
                path: expected[path]["after_sha256"] for path in CONTROLLED_PATHS}:
            raise IntakeError("derived staged hashes differ from preview")
        recheck_catalog_gates(root, preview)
    validations = preflight(stage_root)
    applied_ids = [row["candidate_id"] for row in preview["actions"] if row["action"] == "add"]
    if "B" not in changing_state:
        outcome = "already_applied_exact"
    else:
        if existing_marker is None:
            _atomic_write(pending_path, canonical_bytes(marker))
        writes = 0
        for path in (*CONTROLLED_PATHS[1:], CONTROLLED_PATHS[0]):
            path_state = state[CONTROLLED_PATHS.index(path)]
            if path_state == "B":
                _atomic_write(root / path, staged[path])
                writes += 1
                if fail_after == writes:
                    raise RuntimeError("injected apply interruption")
        outcome = "recovered_exact" if "A" in changing_state else "applied_exact"
    final = path_hashes(root)
    if any(final[path] != expected[path]["after_sha256"] for path in CONTROLLED_PATHS):
        raise IntakeError("final controlled paths differ")
    if pending_path.exists():
        pending_path.unlink()
    return {
        "schema_version": RECEIPT_VERSION, "canonical_profile": CANONICAL_PROFILE,
        "payload_sha256": preview_sha256(preview),
        "approval_sha256": sha256_bytes(canonical_bytes(approval)),
        "execution_id": marker["execution_id"], "before_state": state,
        "final_sha256": final, "validations": validations,
        "applied_candidate_ids": applied_ids, "outcome": outcome,
    }


def _load(path: Path) -> dict[str, object]:
    value = parse_closed_json(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise IntakeError(f"{path}: expected object")
    return value


def _write(path: Path | None, value: object) -> None:
    body = canonical_bytes(value)
    if path:
        _atomic_write(path, body)
    else:
        sys.stdout.buffer.write(body)


def _source(args: argparse.Namespace) -> tuple[str, str]:
    if args.text is not None:
        return args.text, "text"
    path = args.file
    try:
        return path.read_text(encoding="utf-8", errors="strict"), f"file:{path.name}"
    except (OSError, UnicodeError) as error:
        raise IntakeError(f"cannot read UTF-8 source: {error}") from error


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Safe Telegram candidate intake")
    commands = root.add_subparsers(dest="command", required=True)
    for name in ("parse", "probe"):
        command = commands.add_parser(name)
        source = command.add_mutually_exclusive_group(required=True)
        source.add_argument("--text")
        source.add_argument("--file", type=Path)
        command.add_argument("--output", type=Path)
    preview = commands.add_parser("preview")
    preview.add_argument("--bundle", type=Path, required=True)
    preview.add_argument("--root", type=Path, required=True)
    preview.add_argument("--stage-root", type=Path, required=True)
    preview.add_argument("--output", type=Path, required=True)
    preview.add_argument("--render", type=Path, required=True)
    apply = commands.add_parser("apply")
    for flag in ("preview", "approval", "root", "stage-root", "pending", "receipt"):
        apply.add_argument(f"--{flag}", dest=flag.replace("-", "_"), type=Path, required=True)
    apply.add_argument("--owner-ref", required=True)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command in {"parse", "probe"}:
            text, source_id = _source(args)
            source = parse_source(text, source_id)
            if args.command == "parse":
                result = source
            else:
                observations = []
                for index, row in enumerate(source["candidates"]):
                    if index:
                        time.sleep(validate_links.BATCH_DELAY if index % validate_links.BATCH_SIZE == 0
                                   else validate_links.REQUEST_DELAY)
                    observations.append(observe_candidate(row["handle"]))
                result = {"source": source, "observations": observations}
            _write(args.output, result)
        elif args.command == "preview":
            bundle = _load(args.bundle)
            if set(bundle) != {"source", "collisions", "observations", "editorial", "actions"}:
                raise IntakeError("preview bundle fields differ")
            value = build_preview(**bundle, root=args.root, stage_root=args.stage_root)
            _write(args.output, value)
            _atomic_write(args.render, render_preview(value).encode("utf-8"))
        else:
            value = apply_preview(args.root, args.stage_root, _load(args.preview), _load(args.approval),
                                  {args.owner_ref}, args.pending)
            _write(args.receipt, value)
        return 0
    except (IntakeError, OSError) as error:
        print(f"[ERROR] {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

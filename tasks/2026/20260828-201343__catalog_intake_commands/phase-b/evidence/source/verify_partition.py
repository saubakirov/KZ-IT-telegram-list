#!/usr/bin/env python3
"""Independently verify the revealed Phase B source seal and 8/20 partition."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


SOURCE_HASHES = {
    "discovery_batch": "ffeb4b3903ae4a4eda2ee2676f31887552cc6b510ecedd65f8830e86fbef6ebb",
    "owner_note": "1fdc1286cb8c5ba1f04507c163a60b6b5171bc3c53123af1debb753b1d29a162",
}
PARTITION_SHA256 = "5b9fb0dd028ac19d02b2c413bca45e8fa3e0e05e8de9b20087bfa883fe2cb732"
SEALED_METADATA_SHA256 = "e35af73f9e11bc46309f35fcc674ce22d1bb5781699138eb339e4a6b72d69e2b"
CALIBRATION_SHA256 = "cbdf4f48f859e012445628daa5353c775192c5fd19db6b49e49b0a8cff8eb6d8"
COMMITMENT_SHA256 = "f7d4530d79e3597453ef5aa62d08295d48304cc1887a7ca1ee1495589aa0255e"


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def byte_offset(text: str, character_offset: int) -> int:
    return len(text[:character_offset].encode("utf-8"))


def discover_source_occurrences(source_id: str, body: bytes) -> list[dict[str, object]]:
    text = body.decode("utf-8", errors="strict")
    rows: list[dict[str, object]] = []
    if source_id == "owner_note":
        pattern = re.compile(
            r"https://(?:t\.me|telegram\.me|telegram\.dog)/"
            r"(?P<handle>[A-Za-z][A-Za-z0-9_]{4,31})"
        )
        matches = pattern.finditer(text)
        input_kind = "public_root_url"
    else:
        section = text.split("## 2. Отклонено — с причиной", 1)[0]
        pattern = re.compile(
            r"(?m)^\| `(?P<handle>[A-Za-z][A-Za-z0-9_]{4,31})` \|"
        )
        matches = pattern.finditer(section)
        input_kind = "bare_handle_table_cell"
    for match in matches:
        raw = match.group(0) if source_id == "owner_note" else match.group("handle")
        start_character = match.start(0) if source_id == "owner_note" else match.start("handle")
        start = byte_offset(text, start_character)
        end = start + len(raw.encode("utf-8"))
        handle = match.group("handle")
        rows.append({
            "source_id": source_id,
            "byte_start": start,
            "byte_end": end,
            "raw_span": raw,
            "handle": handle.casefold(),
            "input_kind": input_kind,
            "derived_url": f"https://t.me/{handle}",
        })
    return rows


def main() -> int:
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
    names = {"discovery_batch": "discovery-batch.md", "owner_note": "owner-note.md"}
    bodies = {source_id: (source_dir / name).read_bytes() for source_id, name in names.items()}
    actual_source_hashes = {source_id: sha256(body) for source_id, body in bodies.items()}
    if actual_source_hashes != SOURCE_HASHES:
        raise SystemExit("source hash mismatch")

    partition_path = source_dir / "full-partition.json"
    metadata_path = source_dir / "sealed-metadata.json"
    if sha256(partition_path.read_bytes()) != PARTITION_SHA256:
        raise SystemExit("partition hash mismatch")
    if sha256(metadata_path.read_bytes()) != SEALED_METADATA_SHA256:
        raise SystemExit("sealed metadata hash mismatch")
    partition = json.loads(partition_path.read_text(encoding="utf-8"))
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if metadata != {
        "schema_version": "kz-intake-sealed-material/v1",
        "source_hashes": SOURCE_HASHES,
        "partition_manifest_sha256": PARTITION_SHA256,
        "calibration_sha256": CALIBRATION_SHA256,
        "commitment_sha256": COMMITMENT_SHA256,
    }:
        raise SystemExit("sealed metadata bindings differ")

    expected_sources = [
        {
            "source_id": source_id,
            "sha256": SOURCE_HASHES[source_id],
            "bytes": len(bodies[source_id]),
            "sealed_name": names[source_id],
        }
        for source_id in ("discovery_batch", "owner_note")
    ]
    if partition.get("schema_version") != "kz-intake-partition/v1":
        raise SystemExit("partition schema differs")
    if partition.get("sources") != expected_sources:
        raise SystemExit("partition source inventory differs")

    independently_discovered = sorted(
        (
            row
            for source_id, body in bodies.items()
            for row in discover_source_occurrences(source_id, body)
        ),
        key=lambda row: (str(row["source_id"]), int(row["byte_start"])),
    )
    manifest_occurrences: list[dict[str, object]] = []
    seen_case_keys: set[str] = set()
    seen_handles: set[str] = set()
    overlap_handles: list[str] = []
    recomputed_scores: list[tuple[str, str]] = []

    for case in partition["cases"]:
        handle = str(case["handle"]).casefold()
        if case["case_key"] in seen_case_keys or handle in seen_handles:
            raise SystemExit("duplicate case key or handle")
        seen_case_keys.add(case["case_key"])
        seen_handles.add(handle)
        occurrence_keys: list[str] = []
        for occurrence in case["occurrences"]:
            source_id = occurrence["source_id"]
            body = bodies[source_id]
            start, end = occurrence["byte_start"], occurrence["byte_end"]
            raw_bytes = body[start:end]
            raw_span = raw_bytes.decode("utf-8", errors="strict")
            if occurrence["source_sha256"] != SOURCE_HASHES[source_id]:
                raise SystemExit("occurrence source binding differs")
            if raw_span != occurrence["raw_span"] or sha256(raw_bytes) != occurrence["raw_span_sha256"]:
                raise SystemExit("occurrence byte slice differs")
            if occurrence["handle"].casefold() != handle:
                raise SystemExit("occurrence handle differs")
            if occurrence["derived_url"].casefold() != f"https://t.me/{handle}":
                raise SystemExit("derived URL differs")
            manifest_occurrences.append({
                "source_id": source_id,
                "byte_start": start,
                "byte_end": end,
                "raw_span": raw_span,
                "handle": handle,
                "input_kind": occurrence["input_kind"],
                "derived_url": occurrence["derived_url"],
            })
            material = (
                f"{occurrence['source_sha256']}:{start}:{end}:"
                f"{occurrence['raw_span_sha256']}"
            ).encode("ascii")
            occurrence_keys.append(sha256(material))
        if len(case["occurrences"]) > 1:
            overlap_handles.append(handle)
        case_material = ":".join(sorted(occurrence_keys)).encode("ascii")
        case_key = sha256(b"kz-intake-case-v1\0" + case_material)
        score = sha256(b"kz-intake-split-v1\0" + case_key.encode("ascii"))
        if case_key != case["case_key"] or score != case["score"]:
            raise SystemExit("case key or score differs")
        recomputed_scores.append((score, handle))

    manifest_projection = sorted(
        manifest_occurrences,
        key=lambda row: (str(row["source_id"]), int(row["byte_start"])),
    )
    if manifest_projection != independently_discovered:
        raise SystemExit("manifest occurrence coverage differs from independent source scan")
    calibration_handles = [
        case["handle"].casefold() for case in partition["cases"]
        if case["partition"] == "calibration"
    ]
    holdout_handles = [
        case["handle"].casefold() for case in partition["cases"]
        if case["partition"] == "holdout"
    ]
    eight_lowest = {handle for _, handle in sorted(recomputed_scores)[:8]}
    if set(calibration_handles) != eight_lowest:
        raise SystemExit("calibration is not the eight-lowest score set")
    totals = {
        "occurrences": len(manifest_occurrences),
        "unique_cases": len(partition["cases"]),
        "overlap_cases": len(overlap_handles),
        "calibration": len(calibration_handles),
        "holdout": len(holdout_handles),
    }
    if totals != partition["totals"] or totals != {
        "occurrences": 29,
        "unique_cases": 28,
        "overlap_cases": 1,
        "calibration": 8,
        "holdout": 20,
    }:
        raise SystemExit("partition totals differ")
    if overlap_handles != ["aws_kz"]:
        raise SystemExit("overlap identity differs")
    aws_case = next(case for case in partition["cases"] if case["handle"].casefold() == "aws_kz")
    if {row["source_id"] for row in aws_case["occurrences"]} != {"discovery_batch", "owner_note"}:
        raise SystemExit("aws_kz source overlap differs")

    result = {
        "schema_version": "kz-intake-partition-audit/v1",
        "result": "verified",
        "source_sha256": actual_source_hashes,
        "source_bytes": {source_id: len(body) for source_id, body in bodies.items()},
        "partition_sha256": PARTITION_SHA256,
        "sealed_metadata_sha256": SEALED_METADATA_SHA256,
        "calibration_sha256": CALIBRATION_SHA256,
        "commitment_sha256": COMMITMENT_SHA256,
        "totals": totals,
        "overlap_handle": "aws_kz",
        "calibration_handles": calibration_handles,
        "holdout_handles": holdout_handles,
        "checks": {
            "source_hashes_and_sizes": True,
            "source_occurrences_independently_scanned": True,
            "source_byte_slices_and_raw_hashes": True,
            "case_keys_and_scores_recomputed": True,
            "eight_lowest_scores_are_calibration": True,
            "partition_is_disjoint_and_complete": True,
        },
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

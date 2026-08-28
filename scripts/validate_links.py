#!/usr/bin/env python3
"""Validate Telegram targets, update observed facts, and archive proven deaths.

Network validation is deliberately separate from schema validation and README
generation. Callers can request a JSON summary instead of scraping console text.

Usage:
    python scripts/validate_links.py
    python scripts/validate_links.py --update --summary-json path/to/summary.json
    python scripts/validate_links.py --archive HANDLE --reason TEXT \
        --evidence-ref REFERENCE --owner-approved
"""

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

DATA_FILE = Path(__file__).parent.parent / "data" / "communities.json"
ENTRY_TYPES = ("groups", "channels", "bots")
SUMMARY_SCHEMA_VERSION = 1

# Existing rate limiting and retry values are contract-protected.
BATCH_SIZE = 3
BATCH_DELAY = 1.5
REQUEST_DELAY = 0.3
RETRY_ATTEMPTS = 3
RETRY_BACKOFF = 2.0
TIMEOUT = 15

COUNT_PATTERN = re.compile(
    r"(?<!\d)(\d[\d\s,\u00a0]*)\s*(members?|subscribers?)\b",
    re.IGNORECASE,
)
HANDLE_IN_TEXT_PATTERN = re.compile(r"@([a-zA-Z][a-zA-Z0-9_]{4,31})")
CONTACT_TITLE_PATTERN = re.compile(r"Telegram:\s*Contact\s*@([a-zA-Z][a-zA-Z0-9_]{4,31})", re.IGNORECASE)


@dataclass(frozen=True)
class FetchResult:
    """One immutable transport result, deliberately free of identity interpretation."""

    ok: bool
    reason: str
    body: bytes | None
    status_code: int | None
    attempts: int


class TelegramPreviewParser(HTMLParser):
    """Extract only target-preview fields relevant to classification."""

    FIELD_CLASSES = {
        "tgme_page_title": "title",
        "tgme_page_extra": "extra",
        "tgme_page_description": "description",
        "tgme_action_button_new": "action",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: dict[str, list[str]] = {
            "title": [],
            "extra": [],
            "description": [],
            "action": [],
        }
        self.authoritative_identity_urls: list[str] = []
        self._active_field: str | None = None
        self._active_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}
        if self._active_field is not None:
            self._active_depth += 1

        classes = set(attributes.get("class", "").split())
        if self._active_field is None:
            for class_name, field in self.FIELD_CLASSES.items():
                if class_name in classes:
                    self._active_field = field
                    self._active_depth = 1
                    break

        # Target identity comes only from preview-owned canonical/OG metadata and
        # the primary Telegram action. Links inside descriptions are content,
        # not evidence that the page represents their destination.
        if (
            tag == "a"
            and "tgme_action_button_new" in classes
            and "href" in attributes
        ):
            self.authoritative_identity_urls.append(attributes["href"])
        if tag == "link" and "canonical" in attributes.get("rel", "").casefold():
            self.authoritative_identity_urls.append(attributes.get("href", ""))
        if tag == "meta" and attributes.get("property", "").casefold() == "og:url":
            self.authoritative_identity_urls.append(attributes.get("content", ""))

    def handle_endtag(self, tag: str) -> None:
        if self._active_field is None:
            return
        self._active_depth -= 1
        if self._active_depth == 0:
            self._active_field = None

    def handle_data(self, data: str) -> None:
        if self._active_field is not None and data.strip():
            self.parts[self._active_field].append(data.strip())

    def text(self, field: str) -> str:
        """Return normalized text for one extracted preview field."""
        return " ".join(self.parts[field]).strip()


def parse_member_count(preview_extra: str) -> int | None:
    """Parse a count only from target-specific preview-extra text."""
    match = COUNT_PATTERN.search(preview_extra)
    if not match:
        return None
    count_text = re.sub(r"[\s,\u00a0]", "", match.group(1))
    try:
        return int(count_text)
    except ValueError:
        return None


def handle_from_url(value: str) -> str | None:
    """Extract a Telegram public handle from an HTTP or tg:// URL."""
    if not value:
        return None
    parsed = urlparse(value)
    if parsed.scheme.casefold() == "tg":
        domain = parse_qs(parsed.query).get("domain", [])
        return domain[0] if domain else None
    if parsed.netloc.casefold() in {"t.me", "telegram.me", "www.t.me", "www.telegram.me"}:
        path_parts = [part for part in parsed.path.split("/") if part]
        return path_parts[0] if path_parts else None
    return None


def observed_preview_type(extra: str, action: str) -> str | None:
    """Infer the peer type only from target-preview-specific evidence."""
    extra_folded = extra.casefold()
    action_folded = action.casefold()
    if re.search(r"\bmembers?\b", extra_folded):
        return "groups"
    if re.search(r"\bsubscribers?\b", extra_folded):
        return "channels"
    if any(marker in action_folded for marker in ("send message", "start bot", "open bot")):
        return "bots"
    if any(marker in action_folded for marker in ("join group", "view group")):
        return "groups"
    if any(marker in action_folded for marker in ("join channel", "view channel")):
        return "channels"
    return None


def result(
    classification: str,
    reason: str,
    entry_type: str,
    member_count: int | None = None,
    visible_name: str | None = None,
    observed_type: str | None = None,
    target_bound: bool = False,
) -> dict[str, object]:
    """Create one stable classifier result."""
    return {
        "classification": classification,
        "reason": reason,
        "declared_type": entry_type,
        "observed_type": observed_type,
        "target_bound": target_bound,
        "visible_name": visible_name,
        "member_count": member_count,
        "archive_candidate": False,
    }


def classify_response(html: str, handle: str, entry_type: str) -> dict[str, object]:
    """Classify one Telegram HTML response without inferring missing facts."""
    if entry_type not in ENTRY_TYPES:
        raise ValueError(f"Unsupported entry type: {entry_type}")

    if "tgme_page_error" in html:
        return result("failed", "telegram_error_marker", entry_type)
    if "This group or channel no longer exists" in html:
        return result("failed", "deleted_marker", entry_type)

    parser = TelegramPreviewParser()
    parser.feed(html)
    title = parser.text("title")
    extra = parser.text("extra")
    action = parser.text("action")
    requested = handle.casefold()

    authoritative_handles = {
        observed.casefold()
        for observed in (
            handle_from_url(value) for value in parser.authoritative_identity_urls
        )
        if observed
    }
    preview_text_handles = {
        match.casefold() for match in HANDLE_IN_TEXT_PATTERN.findall(extra)
    }
    has_preview = bool(title and (extra or parser.text("description") or action))

    if not has_preview:
        contact_handles = {
            match.casefold() for match in CONTACT_TITLE_PATTERN.findall(html)
        }
        if requested in contact_handles:
            return result(
                "ambiguous",
                "contact_shell_without_preview",
                entry_type,
                target_bound=False,
            )
        return result("non_target", "no_target_preview", entry_type)

    if len(authoritative_handles) > 1:
        return result(
            "ambiguous",
            "conflicting_target_identity",
            entry_type,
            visible_name=title,
        )

    if authoritative_handles:
        target_bound = authoritative_handles == {requested}
    else:
        if len(preview_text_handles) > 1:
            return result(
                "ambiguous",
                "conflicting_preview_identity_text",
                entry_type,
                visible_name=title,
            )
        target_bound = preview_text_handles == {requested}

    if not target_bound:
        return result(
            "non_target",
            "preview_does_not_bind_requested_handle",
            entry_type,
            visible_name=title,
        )

    preview_type = observed_preview_type(extra, action)
    if preview_type is None:
        return result(
            "ambiguous",
            "declared_type_not_established",
            entry_type,
            visible_name=title,
            target_bound=True,
        )
    if preview_type != entry_type:
        return result(
            "ambiguous",
            "declared_type_mismatch",
            entry_type,
            visible_name=title,
            observed_type=preview_type,
            target_bound=True,
        )

    return result(
        "verified",
        "target_preview_verified",
        entry_type,
        member_count=parse_member_count(extra),
        visible_name=title,
        observed_type=preview_type,
        target_bound=True,
    )


def fetch_preview_with_retry(handle: str) -> FetchResult:
    """Fetch one Telegram preview without interpreting identity or peer type."""
    url = f"https://t.me/{handle}"
    for attempt in range(RETRY_ATTEMPTS):
        try:
            request = Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Accept-Language": "en-US,en;q=0.9",
                },
            )
            with urlopen(request, timeout=TIMEOUT) as response:
                body = response.read()
                status = getattr(response, "status", None)
            return FetchResult(True, "fetched", body, status, attempt + 1)
        except HTTPError as error:
            if error.code == 429:
                wait = RETRY_BACKOFF ** (attempt + 1)
                print(f"[WARNING] Rate limited; waiting {wait}s before retry")
                time.sleep(wait)
                continue
            return FetchResult(False, f"http_{error.code}", None, error.code, attempt + 1)
        except URLError as error:
            if attempt < RETRY_ATTEMPTS - 1:
                wait = RETRY_BACKOFF ** attempt
                time.sleep(wait)
                continue
            return FetchResult(False, f"url_error:{error.reason}", None, None, attempt + 1)
        except Exception as error:
            if attempt < RETRY_ATTEMPTS - 1:
                wait = RETRY_BACKOFF ** attempt
                time.sleep(wait)
                continue
            return FetchResult(False, f"error:{error}", None, None, attempt + 1)

    return FetchResult(False, "max_retries_exceeded", None, None, RETRY_ATTEMPTS)


def check_link_with_retry(handle: str, entry_type: str) -> dict[str, object]:
    """Fetch and classify one Telegram target with the existing retry semantics."""
    fetched = fetch_preview_with_retry(handle)
    if not fetched.ok or fetched.body is None:
        return result("failed", fetched.reason, entry_type)
    html = fetched.body.decode("utf-8", errors="ignore")
    return classify_response(html, handle, entry_type)


def load_data(path: Path = DATA_FILE) -> dict:
    """Load a catalog from disk."""
    with path.open("r", encoding="utf-8") as source:
        return json.load(source)


def save_data(data: dict, path: Path = DATA_FILE) -> None:
    """Persist a catalog as UTF-8 JSON with a trailing newline."""
    with path.open("w", encoding="utf-8", newline="\n") as destination:
        json.dump(data, destination, ensure_ascii=False, indent=2)
        destination.write("\n")


def collect_live_entries(data: dict) -> list[tuple[str, dict]]:
    """Return all live entries with their declared type."""
    return [
        (entry_type, entry)
        for entry_type in ENTRY_TYPES
        for entry in data.get(entry_type, [])
    ]


def enrich_result(
    entry_type: str,
    entry: dict,
    observation: dict[str, object],
) -> dict[str, object]:
    """Combine catalog state with one classifier observation."""
    old_count = entry.get("member_count")
    observed_count = observation.get("member_count")
    classification = observation["classification"]
    if classification != "verified" or observed_count is None:
        count_outcome = "unavailable"
        delta = None
    elif old_count is None:
        count_outcome = "first_count"
        delta = None
    else:
        delta = observed_count - old_count
        if delta > 0:
            count_outcome = "grew"
        elif delta < 0:
            count_outcome = "shrank"
        else:
            count_outcome = "unchanged"

    return {
        "type": entry_type,
        "name": entry["name"],
        "handle": entry["handle"],
        "classification": classification,
        "reason": observation["reason"],
        "declared_type": observation["declared_type"],
        "observed_type": observation["observed_type"],
        "target_bound": observation["target_bound"],
        "visible_name": observation["visible_name"],
        "old_count": old_count,
        "observed_count": observed_count,
        "count_outcome": count_outcome,
        "delta": delta,
        "archive_candidate": False,
    }


def build_summary(records: list[dict[str, object]], run_date: str) -> dict[str, object]:
    """Build the stable machine-readable summary consumed by project tooling."""
    classifications = ("verified", "ambiguous", "non_target", "failed")
    outcomes = ("grew", "shrank", "unchanged", "first_count")
    totals = {name: 0 for name in (*classifications, *outcomes)}
    totals["total"] = len(records)
    totals["member_delta"] = 0

    for record in records:
        classification = str(record["classification"])
        if classification in classifications:
            totals[classification] += 1
        count_outcome = str(record["count_outcome"])
        if count_outcome in outcomes:
            totals[count_outcome] += 1
        delta = record.get("delta")
        if isinstance(delta, int):
            totals["member_delta"] += delta

    return {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "run_date": run_date,
        "totals": totals,
        "entries": records,
    }


def apply_updates(
    data: dict,
    records: list[dict[str, object]],
    run_date: str,
) -> dict[str, int]:
    """Persist only positively observed dates and numeric counts in memory."""
    live_index = {
        entry["handle"].casefold(): entry
        for _, entry in collect_live_entries(data)
    }
    dates_updated = 0
    counts_updated = 0

    for record in records:
        if record["classification"] != "verified":
            continue
        entry = live_index.get(str(record["handle"]).casefold())
        if entry is None:
            raise ValueError(f"Summary handle is not live: {record['handle']}")
        entry["last_verified"] = run_date
        dates_updated += 1
        observed_count = record.get("observed_count")
        if isinstance(observed_count, int):
            if entry.get("member_count") != observed_count:
                counts_updated += 1
            entry["member_count"] = observed_count

    data.setdefault("meta", {})["last_updated"] = run_date
    return {"dates_updated": dates_updated, "counts_updated": counts_updated}


def archive_entry(
    data: dict,
    handle: str,
    reason: str,
    died_on: str,
    evidence_reference: str,
    owner_approved: bool,
) -> dict:
    """Move one owner-approved, independently proven death into the archive."""
    if not owner_approved:
        raise ValueError("Explicit owner approval is required for archive mutation")
    if not reason.strip():
        raise ValueError("An evidence-based archive reason is required")
    if not evidence_reference.strip():
        raise ValueError("An independent evidence reference is required")
    try:
        datetime.strptime(died_on, "%Y-%m-%d")
    except ValueError as error:
        raise ValueError("died_on must be a valid YYYY-MM-DD date") from error

    normalized = handle.casefold()
    archive = data.setdefault("archive", [])
    if any(str(entry.get("handle", "")).casefold() == normalized for entry in archive):
        raise ValueError(f"@{handle} is already archived")

    match: tuple[str, int, dict] | None = None
    for entry_type in ENTRY_TYPES:
        for index, entry in enumerate(data.get(entry_type, [])):
            if str(entry.get("handle", "")).casefold() == normalized:
                if match is not None:
                    raise ValueError(f"@{handle} is duplicated in the live catalog")
                match = (entry_type, index, entry)
    if match is None:
        raise ValueError(f"Live handle not found: @{handle}")

    entry_type, index, entry = match
    archived = dict(entry)
    archived.update({"type": entry_type, "died_on": died_on, "reason": reason.strip()})
    data[entry_type].pop(index)
    archive.append(archived)
    data.setdefault("meta", {})["last_updated"] = died_on
    return archived


def format_count(count: object) -> str:
    """Format an observed count for the human console."""
    if not isinstance(count, int):
        return "no-count"
    if count >= 1000:
        return f"{count / 1000:.1f}k"
    return str(count)


def write_summary(summary: dict[str, object], path: Path) -> None:
    """Write one machine-readable summary document."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as destination:
        json.dump(summary, destination, ensure_ascii=False, indent=2)
        destination.write("\n")


def run_archive_mode(args: argparse.Namespace, data: dict, run_date: str) -> int:
    """Perform the explicit offline archive operation."""
    missing = [
        flag
        for flag, value in (
            ("--reason", args.reason),
            ("--evidence-ref", args.evidence_ref),
        )
        if not value
    ]
    if missing or not args.owner_approved:
        if not args.owner_approved:
            missing.append("--owner-approved")
        print(f"[ERROR] Archive mutation requires: {', '.join(missing)}")
        return 1

    try:
        archived = archive_entry(
            data,
            args.archive,
            args.reason,
            run_date,
            args.evidence_ref,
            args.owner_approved,
        )
    except ValueError as error:
        print(f"[ERROR] {error}")
        return 1

    save_data(data)
    print(f"[OK] Archived [{archived['type']}] {archived['name']} (@{archived['handle']})")
    print(f"[INFO] Evidence reference: {args.evidence_ref}")
    return 0


def parse_args() -> argparse.Namespace:
    """Parse command-line options."""
    parser = argparse.ArgumentParser(description="Validate Telegram links safely")
    parser.add_argument("--update", action="store_true", help="Persist verified observations")
    parser.add_argument("--summary-json", type=Path, help="Write the machine summary to this path")
    parser.add_argument("--handle", help="Validate one exact live handle instead of the full catalog")
    parser.add_argument("--archive", metavar="HANDLE", help="Archive one owner-approved proven death")
    parser.add_argument("--reason", help="Evidence-based archive reason")
    parser.add_argument("--evidence-ref", help="Independent evidence artifact reference")
    parser.add_argument("--owner-approved", action="store_true", help="Confirm per-entry owner approval")
    args = parser.parse_args()
    if args.archive and (args.update or args.handle):
        parser.error("--archive cannot be combined with --update or --handle")
    if not args.archive and (args.reason or args.evidence_ref or args.owner_approved):
        parser.error("archive evidence and approval options require --archive")
    return args


def main() -> int:
    """Run archive mode or the network validator."""
    args = parse_args()
    if not DATA_FILE.exists():
        print(f"[ERROR] Data file not found: {DATA_FILE}")
        return 1

    try:
        data = load_data()
    except (OSError, json.JSONDecodeError) as error:
        print(f"[ERROR] Could not load {DATA_FILE}: {error}")
        return 1

    run_date = date.today().isoformat()
    if args.archive:
        return run_archive_mode(args, data, run_date)

    live_entries = collect_live_entries(data)
    if args.handle:
        selected = [
            item
            for item in live_entries
            if item[1]["handle"].casefold() == args.handle.casefold()
        ]
        if len(selected) != 1:
            print(f"[ERROR] Exact live handle not found or not unique: @{args.handle}")
            return 1
        live_entries = selected
    print(f"[INFO] Validating {len(live_entries)} Telegram links")
    print(f"[INFO] Rate limit: {BATCH_SIZE} requests per {BATCH_DELAY}s")
    records: list[dict[str, object]] = []

    for offset in range(0, len(live_entries), BATCH_SIZE):
        batch = live_entries[offset:offset + BATCH_SIZE]
        for entry_type, entry in batch:
            observation = check_link_with_retry(entry["handle"], entry_type)
            record = enrich_result(entry_type, entry, observation)
            records.append(record)
            classification = str(record["classification"])
            tag = "OK" if classification == "verified" else "FAIL" if classification == "failed" else "WARNING"
            print(
                f"[{tag}] [{entry_type}] {entry['name']} (@{entry['handle']}): "
                f"{classification}; {record['reason']}; "
                f"count={format_count(record['observed_count'])}"
            )
            time.sleep(REQUEST_DELAY)
        if offset + BATCH_SIZE < len(live_entries):
            time.sleep(BATCH_DELAY)

    summary = build_summary(records, run_date)
    if args.update:
        updates = apply_updates(data, records, run_date)
        save_data(data)
        print(
            f"[INFO] Persisted dates={updates['dates_updated']}; "
            f"counts={updates['counts_updated']}; meta.last_updated={run_date}"
        )

    if args.summary_json:
        write_summary(summary, args.summary_json)
        print(f"[OK] Machine summary: {args.summary_json}")
    else:
        print(f"[SUMMARY_JSON] {json.dumps(summary, ensure_ascii=False, separators=(',', ':'))}")

    totals = summary["totals"]
    print(
        "[INFO] Summary: "
        f"verified={totals['verified']}; ambiguous={totals['ambiguous']}; "
        f"non_target={totals['non_target']}; failed={totals['failed']}"
    )
    unresolved = totals["ambiguous"] + totals["non_target"] + totals["failed"]
    if unresolved:
        print("[WARNING] Unresolved results require evidence review and owner triage")
        return 1
    print("[SUCCESS] Every target was positively verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())

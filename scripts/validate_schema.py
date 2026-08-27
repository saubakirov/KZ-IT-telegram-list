#!/usr/bin/env python3
"""Validate the structured community catalog without using the network.

The validator enforces live-entry, Project North Star, and archive integrity
rules. Freshness is reported as an operational signal; valid old dates do not
make the schema invalid.

Usage:
    python scripts/validate_schema.py
"""

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "communities.json"
ENTRY_TYPES = ("groups", "channels", "bots")
FRESHNESS_DAYS = 90

REQUIRED_FIELDS = {
    "groups": ("name", "handle", "description", "category", "last_verified"),
    "channels": ("name", "handle", "description", "last_verified"),
    "bots": ("name", "handle", "description", "last_verified"),
}

HANDLE_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]{4,31}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_data(path: Path = DATA_FILE) -> dict:
    """Load a JSON catalog from *path*."""
    with path.open("r", encoding="utf-8") as source:
        return json.load(source)


def is_non_empty_string(value: object) -> bool:
    """Return whether *value* is a string containing non-whitespace text."""
    return isinstance(value, str) and bool(value.strip())


def parse_iso_date(
    value: object,
    prefix: str,
    field: str,
    errors: list[str],
) -> date | None:
    """Validate a strict ISO calendar date and append any error."""
    if not isinstance(value, str) or not DATE_PATTERN.fullmatch(value):
        errors.append(f"{prefix}: invalid {field} format '{value}' (expected YYYY-MM-DD)")
        return None

    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        errors.append(f"{prefix}: invalid {field} value '{value}'")
        return None


def validate_north_star(data: dict) -> list[str]:
    """Validate the structured Project North Star block."""
    errors: list[str] = []
    north_star = data.get("north_star")

    if not isinstance(north_star, dict):
        return ["[north_star]: missing or not an object"]

    if not is_non_empty_string(north_star.get("purpose")):
        errors.append("[north_star]: 'purpose' must be a non-empty string")

    non_goals = north_star.get("non_goals")
    if not isinstance(non_goals, list) or not non_goals:
        errors.append("[north_star]: 'non_goals' must be a non-empty list")
    elif any(not is_non_empty_string(item) for item in non_goals):
        errors.append("[north_star]: every 'non_goals' item must be a non-empty string")

    return errors


def validate_entry(
    entry: object,
    entry_type: str,
    index: int,
    allowed_categories: set[str],
    seen_live_handles: set[str],
    live_dates: list[date],
) -> list[str]:
    """Validate one live catalog entry."""
    errors: list[str] = []
    if not isinstance(entry, dict):
        return [f"[{entry_type}][{index}]: entry must be an object"]

    prefix = f"[{entry_type}][{index}] {entry.get('name', 'UNNAMED')}"
    for field in REQUIRED_FIELDS[entry_type]:
        if field not in entry or not is_non_empty_string(entry.get(field)):
            errors.append(f"{prefix}: missing required field '{field}'")

    handle = entry.get("handle")
    if isinstance(handle, str) and handle:
        normalized_handle = handle.casefold()
        if not HANDLE_PATTERN.fullmatch(handle):
            errors.append(f"{prefix}: invalid handle format '@{handle}'")
        if normalized_handle in seen_live_handles:
            errors.append(f"{prefix}: duplicate live handle '@{handle}'")
        seen_live_handles.add(normalized_handle)

    if entry_type == "groups":
        category = entry.get("category")
        if is_non_empty_string(category) and category not in allowed_categories:
            errors.append(
                f"{prefix}: unknown category '{category}' "
                f"(allowed: {sorted(allowed_categories)})"
            )

    if "last_verified" in entry:
        parsed_date = parse_iso_date(
            entry.get("last_verified"), prefix, "last_verified", errors
        )
        if parsed_date is not None:
            live_dates.append(parsed_date)

    member_count = entry.get("member_count")
    if member_count is not None and (
        not isinstance(member_count, int)
        or isinstance(member_count, bool)
        or member_count < 0
    ):
        errors.append(f"{prefix}: member_count must be a non-negative integer when present")

    return errors


def validate_archive(
    archive: object,
    allowed_categories: set[str],
    live_handles: set[str],
) -> list[str]:
    """Validate archived entries and live/archive handle separation."""
    errors: list[str] = []
    if not isinstance(archive, list):
        return ["[archive]: must be an array"]

    seen_archive_handles: set[str] = set()
    for index, entry in enumerate(archive):
        if not isinstance(entry, dict):
            errors.append(f"[archive][{index}]: entry must be an object")
            continue

        prefix = f"[archive][{index}] {entry.get('name', 'UNNAMED')}"
        entry_type = entry.get("type")
        if entry_type not in ENTRY_TYPES:
            errors.append(
                f"{prefix}: 'type' must be one of {list(ENTRY_TYPES)}"
            )
            required_fields: tuple[str, ...] = ()
        else:
            required_fields = REQUIRED_FIELDS[entry_type]

        for field in (*required_fields, "type", "died_on", "reason"):
            if field not in entry or not is_non_empty_string(entry.get(field)):
                errors.append(f"{prefix}: missing required field '{field}'")

        handle = entry.get("handle")
        if isinstance(handle, str) and handle:
            normalized_handle = handle.casefold()
            if not HANDLE_PATTERN.fullmatch(handle):
                errors.append(f"{prefix}: invalid handle format '@{handle}'")
            if normalized_handle in live_handles:
                errors.append(f"{prefix}: handle '@{handle}' also exists in the live catalog")
            if normalized_handle in seen_archive_handles:
                errors.append(f"{prefix}: duplicate archive handle '@{handle}'")
            seen_archive_handles.add(normalized_handle)

        if entry_type == "groups":
            category = entry.get("category")
            if is_non_empty_string(category) and category not in allowed_categories:
                errors.append(f"{prefix}: unknown category '{category}'")

        if "last_verified" in entry:
            parse_iso_date(entry.get("last_verified"), prefix, "last_verified", errors)
        if "died_on" in entry:
            parse_iso_date(entry.get("died_on"), prefix, "died_on", errors)

        if "reason" in entry and not is_non_empty_string(entry.get("reason")):
            errors.append(f"{prefix}: 'reason' must be a non-empty evidence-based string")

        member_count = entry.get("member_count")
        if member_count is not None and (
            not isinstance(member_count, int)
            or isinstance(member_count, bool)
            or member_count < 0
        ):
            errors.append(f"{prefix}: member_count must be a non-negative integer when present")

    return errors


def validate_data(
    data: object,
    today: date | None = None,
) -> tuple[list[str], dict[str, object]]:
    """Validate a parsed catalog and return errors plus freshness information."""
    if not isinstance(data, dict):
        return ["[catalog]: top-level JSON value must be an object"], {
            "oldest_live": None,
            "stale_count": 0,
            "threshold_days": FRESHNESS_DAYS,
        }

    errors = validate_north_star(data)
    categories = data.get("categories")
    if not isinstance(categories, dict) or not categories:
        errors.append("[categories]: must be a non-empty object")
        allowed_categories: set[str] = set()
    else:
        allowed_categories = set(categories)
        for key, display_name in categories.items():
            if not is_non_empty_string(key) or not is_non_empty_string(display_name):
                errors.append("[categories]: keys and display names must be non-empty strings")

    live_handles: set[str] = set()
    live_dates: list[date] = []
    for entry_type in ENTRY_TYPES:
        entries = data.get(entry_type)
        if not isinstance(entries, list):
            errors.append(f"[{entry_type}]: must be an array")
            continue
        for index, entry in enumerate(entries):
            errors.extend(
                validate_entry(
                    entry,
                    entry_type,
                    index,
                    allowed_categories,
                    live_handles,
                    live_dates,
                )
            )

    errors.extend(
        validate_archive(data.get("archive"), allowed_categories, live_handles)
    )

    reference_date = today or date.today()
    oldest_live = min(live_dates) if live_dates else None
    stale_count = sum(
        1
        for verified_date in live_dates
        if (reference_date - verified_date).days > FRESHNESS_DAYS
    )
    freshness = {
        "oldest_live": oldest_live.isoformat() if oldest_live else None,
        "stale_count": stale_count,
        "threshold_days": FRESHNESS_DAYS,
    }
    return errors, freshness


def main() -> int:
    """Run schema validation for the production catalog."""
    if not DATA_FILE.exists():
        print(f"[ERROR] Data file not found: {DATA_FILE}")
        return 1

    try:
        data = load_data()
    except (OSError, json.JSONDecodeError) as error:
        print(f"[ERROR] Could not load {DATA_FILE}: {error}")
        return 1

    for entry_type in ENTRY_TYPES:
        entries = data.get(entry_type)
        count = len(entries) if isinstance(entries, list) else 0
        print(f"[INFO] Validating {count} {entry_type}...")

    errors, freshness = validate_data(data)
    oldest = freshness["oldest_live"] or "unavailable"
    print(
        "[INFO] Freshness: "
        f"oldest_live={oldest}; "
        f"older_than_{freshness['threshold_days']}_days={freshness['stale_count']}"
    )
    if freshness["stale_count"]:
        print("[WARNING] Catalog freshness is stale; age alone is not a schema error")

    categories = data.get("categories")
    archive = data.get("archive")
    print(f"[INFO] Categories: {len(categories) if isinstance(categories, dict) else 0}")
    print(f"[INFO] Archive entries: {len(archive) if isinstance(archive, list) else 0}")
    print(f"[INFO] Errors: {len(errors)}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    print("[SUCCESS] Schema is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

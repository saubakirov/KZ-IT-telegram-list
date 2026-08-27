#!/usr/bin/env python3
"""Validate the structured community catalog without using the network.

The validator enforces live-entry, Project North Star, and archive integrity
rules. Freshness is reported as an operational signal; valid old dates do not
make the schema invalid.

Usage:
    python scripts/validate_schema.py
"""

import hashlib
import json
import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "communities.json"
ENTRY_TYPES = ("groups", "channels", "bots")
LOCALES = ("en", "ru", "kk")
INTENT_IDS = ("ai", "startups", "jobs", "events", "engineering")
FRESHNESS_DAYS = 90

UI_KEYS = (
    "nav.languages",
    "nav.types",
    "nav.intents",
    "stats.groups",
    "stats.channels",
    "stats.bots",
    "stats.categories",
    "stats.verified",
    "section.contents",
    "section.purpose",
    "section.groups",
    "section.channels",
    "section.bots",
    "section.archive",
    "section.contributing",
    "section.data",
    "section.license",
    "north_star.non_goals_intro",
    "bots.intro",
    "archive.summary",
    "archive.column.type",
    "archive.column.community",
    "archive.column.description",
    "archive.column.member_count",
    "archive.column.last_verified",
    "archive.column.died_on",
    "archive.column.reason",
    "type.group",
    "type.channel",
    "type.bot",
    "contributing.prompt",
    "data.download_label",
    "generated.notice",
    "license.waiver",
    "intent.ai",
    "intent.startups",
    "intent.jobs",
    "intent.events",
    "intent.engineering",
)

README_UI_KEYS = (
    "section.project_workflow",
    "workflow.intro",
    "workflow.portfolio.label",
    "workflow.portfolio.description",
    "workflow.knowledge.label",
    "workflow.knowledge.description",
    "workflow.agents.label",
    "workflow.agents.description",
)

EXPECTED_INTENTS = {
    "ai": {
        "categories": ["ai"],
        "exceptional_handles": ["ml_jobs_kz", "dsmlkz_news"],
    },
    "startups": {
        "categories": ["startups"],
        "exceptional_handles": ["thetechkzchat", "thetechkz", "saubakirov"],
    },
    "jobs": {"categories": ["jobs"], "exceptional_handles": []},
    "events": {"categories": ["events"], "exceptional_handles": []},
    "engineering": {
        "categories": [
            "ai",
            "blockchain",
            "data-analytics",
            "devops-sysadmin",
            "gamedev",
            "hardware",
            "mobile",
            "programming-languages",
            "qa-testing",
            "security",
            "web-development",
        ],
        "exceptional_handles": [
            "devkz",
            "illuminatinc",
            "teamleads_kz",
            "datanomika",
            "DevSkills",
            "nu_acm_w",
            "sysadm_in_up",
            "saubakirov",
            "cleverskz",
            "Get_Telegram_ID_bot",
        ],
    },
}

PLACEHOLDER_PATTERN = re.compile(
    r"(?:^|\b)(?:todo|tbd|placeholder|translation pending)(?:\b|$)",
    re.IGNORECASE,
)

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


def localized_key(base: str, locale: str) -> str:
    """Return the source key for *base* in *locale* without language fallback."""
    return base if locale == "en" else f"{base}_{locale}"


def localized_value(container: dict, base: str, locale: str) -> object:
    """Read one explicit localized value; absence never falls back to English."""
    return container.get(localized_key(base, locale))


def normalized_text(value: str) -> str:
    """Normalize a reviewed string to Unicode NFC."""
    return unicodedata.normalize("NFC", value)


def all_live_entries(data: dict) -> list[tuple[str, dict]]:
    """Return every live entry paired with its source type."""
    return [
        (entry_type, entry)
        for entry_type in ENTRY_TYPES
        for entry in data.get(entry_type, [])
        if isinstance(entry, dict)
    ]


def category_names(data: dict, locale: str) -> object:
    """Return explicit category labels for *locale* without fallback."""
    if locale == "en":
        return data.get("categories")
    labels = data.get("category_labels")
    return labels.get(locale) if isinstance(labels, dict) else None


def build_locale_payload(data: dict, locale: str) -> dict[str, str]:
    """Build the exact reviewed 131-key payload for one locale."""
    payload: dict[str, str] = {}

    meta = data.get("meta", {})
    north_star = data.get("north_star", {})
    payload["meta.title"] = normalized_text(localized_value(meta, "title", locale))
    payload["meta.description"] = normalized_text(
        localized_value(meta, "description", locale)
    )
    payload["north_star.purpose"] = normalized_text(
        localized_value(north_star, "purpose", locale)
    )
    non_goals = localized_value(north_star, "non_goals", locale)
    for index, value in enumerate(non_goals):
        payload[f"north_star.non_goals.{index}"] = normalized_text(value)

    labels = category_names(data, locale)
    for category in data.get("categories", {}):
        payload[f"categories.{category}"] = normalized_text(labels[category])

    for entry_type, entry in all_live_entries(data):
        handle = entry["handle"]
        value = localized_value(entry, "description", locale)
        payload[f"{entry_type}.{handle}.description"] = normalized_text(value)

    for entry in data.get("archive", []):
        handle = entry["handle"]
        payload[f"archive.{handle}.description"] = normalized_text(
            localized_value(entry, "description", locale)
        )
        payload[f"archive.{handle}.reason"] = normalized_text(
            localized_value(entry, "reason", locale)
        )

    ui = data.get("ui", {}).get(locale, {})
    for key in UI_KEYS:
        payload[f"ui.{key}"] = normalized_text(ui[key])
    if locale == "en":
        readme_ui = data.get("readme_ui", {})
        for key in README_UI_KEYS:
            payload[f"readme_ui.{key}"] = normalized_text(readme_ui[key])
    return payload


def build_review_payload(data: dict) -> dict[str, dict[str, str]]:
    """Build the complete EN/RU/KK canonical review payload."""
    return {locale: build_locale_payload(data, locale) for locale in LOCALES}


def canonical_review_bytes(data: dict) -> bytes:
    """Serialize the review payload as NFC, sorted, compact UTF-8 JSON."""
    serialized = json.dumps(
        build_review_payload(data),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return serialized.encode("utf-8")


def review_payload_sha256(data: dict) -> str:
    """Return the SHA-256 digest of the canonical review payload."""
    return hashlib.sha256(canonical_review_bytes(data)).hexdigest()


def review_payload_keys(data: dict) -> list[str]:
    """Return the exact sorted changed-key universe for an initial review."""
    payload = build_review_payload(data)
    return sorted(
        f"{locale}.{key}"
        for locale, values in payload.items()
        for key in values
    )


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


def validate_localizations(data: dict) -> list[str]:
    """Validate exact locale coverage, UI inventory, and payload shape."""
    errors: list[str] = []
    if data.get("locales") != list(LOCALES):
        errors.append(f"[locales]: must be exactly {list(LOCALES)} in this order")

    meta = data.get("meta")
    north_star = data.get("north_star")
    if not isinstance(meta, dict) or not isinstance(north_star, dict):
        return errors + ["[localization]: meta and north_star must be objects"]

    def require_text(container: dict, base: str, locale: str, prefix: str) -> None:
        key = localized_key(base, locale)
        value = container.get(key)
        if not is_non_empty_string(value):
            errors.append(f"{prefix}: '{key}' must be a non-empty explicit value")
        elif PLACEHOLDER_PATTERN.search(value):
            errors.append(f"{prefix}: '{key}' contains placeholder text")

    for locale in LOCALES:
        require_text(meta, "title", locale, "[meta]")
        require_text(meta, "description", locale, "[meta]")
        require_text(north_star, "purpose", locale, "[north_star]")

        non_goals_key = localized_key("non_goals", locale)
        non_goals = north_star.get(non_goals_key)
        if not isinstance(non_goals, list) or len(non_goals) != 4:
            errors.append(
                f"[north_star]: '{non_goals_key}' must contain exactly four values"
            )
        else:
            for index, value in enumerate(non_goals):
                if not is_non_empty_string(value):
                    errors.append(
                        f"[north_star]: '{non_goals_key}[{index}]' must be non-empty"
                    )
                elif PLACEHOLDER_PATTERN.search(value):
                    errors.append(
                        f"[north_star]: '{non_goals_key}[{index}]' contains placeholder text"
                    )

    categories = data.get("categories")
    category_labels = data.get("category_labels")
    category_keys = set(categories) if isinstance(categories, dict) else set()
    if not isinstance(category_labels, dict) or set(category_labels) != {"ru", "kk"}:
        errors.append("[category_labels]: locale keys must be exactly ['ru', 'kk']")
    else:
        for locale in ("ru", "kk"):
            labels = category_labels.get(locale)
            if not isinstance(labels, dict) or set(labels) != category_keys:
                errors.append(
                    f"[category_labels.{locale}]: keys must exactly match categories"
                )
                continue
            for category, value in labels.items():
                if not is_non_empty_string(value) or PLACEHOLDER_PATTERN.search(value):
                    errors.append(
                        f"[category_labels.{locale}]: '{category}' must be explicit and non-placeholder"
                    )

    ui = data.get("ui")
    if not isinstance(ui, dict) or list(ui) != list(LOCALES):
        errors.append(f"[ui]: locale keys must be exactly {list(LOCALES)} in order")
    else:
        expected_ui = set(UI_KEYS)
        for locale in LOCALES:
            values = ui.get(locale)
            if not isinstance(values, dict) or set(values) != expected_ui:
                missing = sorted(expected_ui - set(values or {}))
                extra = sorted(set(values or {}) - expected_ui)
                errors.append(
                    f"[ui.{locale}]: keys differ; missing={missing}; extra={extra}"
                )
                continue
            for key, value in values.items():
                if not is_non_empty_string(value) or PLACEHOLDER_PATTERN.search(value):
                    errors.append(
                        f"[ui.{locale}]: '{key}' must be explicit and non-placeholder"
                    )

    readme_ui = data.get("readme_ui")
    if not isinstance(readme_ui, dict) or set(readme_ui) != set(README_UI_KEYS):
        errors.append("[readme_ui]: keys must match the eight-key README appendix registry")
    else:
        for key, value in readme_ui.items():
            if not is_non_empty_string(value) or PLACEHOLDER_PATTERN.search(value):
                errors.append(f"[readme_ui]: '{key}' must be explicit and non-placeholder")

    localized_entries = all_live_entries(data) + [
        ("archive", entry)
        for entry in data.get("archive", [])
        if isinstance(entry, dict)
    ]
    for entry_type, entry in localized_entries:
        prefix = f"[{entry_type}] @{entry.get('handle', 'UNKNOWN')}"
        for locale in LOCALES:
            require_text(entry, "description", locale, prefix)
        if entry_type == "archive":
            for locale in LOCALES:
                require_text(entry, "reason", locale, prefix)

    if not errors:
        payload = build_review_payload(data)
        common_keys = {
            key for key in payload["en"] if not key.startswith("readme_ui.")
        }
        for locale in LOCALES:
            expected_count = 139 if locale == "en" else 131
            if len(payload[locale]) != expected_count:
                errors.append(
                    f"[localization.{locale}]: expected {expected_count} reviewed keys, got {len(payload[locale])}"
                )
            locale_common = {
                key for key in payload[locale] if not key.startswith("readme_ui.")
            }
            if locale_common != common_keys:
                errors.append(
                    f"[localization.{locale}]: semantic keys differ from English"
                )
    return errors


def validate_intents(data: dict, allowed_categories: set[str]) -> list[str]:
    """Validate the researched category-plus-exception intent contract."""
    errors: list[str] = []
    intents = data.get("intents")
    if not isinstance(intents, dict) or list(intents) != list(INTENT_IDS):
        return [f"[intents]: IDs and order must be exactly {list(INTENT_IDS)}"]

    live_entries = all_live_entries(data)
    by_handle = {entry["handle"].casefold(): entry for _, entry in live_entries}
    for intent_id in INTENT_IDS:
        definition = intents.get(intent_id)
        expected = EXPECTED_INTENTS[intent_id]
        if definition != expected:
            errors.append(
                f"[intents.{intent_id}]: definition differs from the reviewed RES-2 baseline"
            )
            continue

        categories = definition["categories"]
        exceptional_handles = definition["exceptional_handles"]
        if len(categories) != len(set(categories)):
            errors.append(f"[intents.{intent_id}]: duplicate category reference")
        if any(category not in allowed_categories for category in categories):
            errors.append(f"[intents.{intent_id}]: unknown category reference")

        folded_handles = [handle.casefold() for handle in exceptional_handles]
        if len(folded_handles) != len(set(folded_handles)):
            errors.append(f"[intents.{intent_id}]: duplicate exceptional handle")
        for handle, folded in zip(exceptional_handles, folded_handles):
            entry = by_handle.get(folded)
            if entry is None:
                errors.append(
                    f"[intents.{intent_id}]: unknown live handle '@{handle}'"
                )
            elif entry.get("category") in categories:
                errors.append(
                    f"[intents.{intent_id}]: redundant exceptional handle '@{handle}'"
                )
    return errors


def validate_review_binding(data: dict) -> list[str]:
    """Validate the exact candidate digest and initial changed-key record."""
    review = data.get("localization_review")
    if not isinstance(review, dict):
        return ["[localization_review]: missing or not an object"]

    errors: list[str] = []
    expected_literals = {
        "status": "CANDIDATE",
        "acceptance_authority": "TFW REVIEW",
        "canonicalization": "NFC + sorted-key compact UTF-8 JSON",
        "changed_keys": "ALL",
    }
    for key, expected in expected_literals.items():
        if review.get(key) != expected:
            errors.append(
                f"[localization_review]: '{key}' must be exactly '{expected}'"
            )
    if review.get("prior_approved_ref") is not None:
        errors.append("[localization_review]: initial prior_approved_ref must be null")
    if review.get("prior_approved_digest") is not None:
        errors.append("[localization_review]: initial prior_approved_digest must be null")

    exact_keys = review_payload_keys(data)
    if review.get("changed_key_count") != len(exact_keys):
        errors.append(
            f"[localization_review]: changed_key_count must be {len(exact_keys)}"
        )
    expected_digest = review_payload_sha256(data)
    if review.get("payload_sha256") != expected_digest:
        errors.append(
            "[localization_review]: payload_sha256 is stale; "
            f"expected {expected_digest}"
        )
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

    category = entry.get("category")
    if category is not None and (
        not is_non_empty_string(category) or category not in allowed_categories
    ):
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

        category = entry.get("category")
        if category is not None and (
            not is_non_empty_string(category) or category not in allowed_categories
        ):
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
    localization_errors = validate_localizations(data)
    errors.extend(localization_errors)
    errors.extend(validate_intents(data, allowed_categories))
    if not localization_errors:
        errors.extend(validate_review_binding(data))

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
    if not validate_localizations(data):
        print(
            "[INFO] Locale payload: "
            "keys=en:139,ru:131,kk:131; "
            f"sha256={review_payload_sha256(data)}"
        )
    print(f"[INFO] Errors: {len(errors)}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    print("[SUCCESS] Schema is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

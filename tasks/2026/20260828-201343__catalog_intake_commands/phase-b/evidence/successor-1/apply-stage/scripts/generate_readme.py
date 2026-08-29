#!/usr/bin/env python3
"""Generate or verify every public Markdown projection from the catalog.

Usage:
    python scripts/generate_readme.py
    python scripts/generate_readme.py --check
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

try:
    from .validate_schema import (
        ENTRY_TYPES,
        INTENT_IDS,
        LOCALES,
        load_data,
        review_payload_sha256,
        validate_data,
    )
except ImportError:  # Direct script execution.
    from validate_schema import (  # type: ignore
        ENTRY_TYPES,
        INTENT_IDS,
        LOCALES,
        load_data,
        review_payload_sha256,
        validate_data,
    )

PROJECT_ROOT = Path(__file__).parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "communities.json"
README_FILE = PROJECT_ROOT / "README.md"
OUTPUT_PATHS = {
    "readme": README_FILE,
    "en": PROJECT_ROOT / "index.md",
    "ru": PROJECT_ROOT / "ru" / "index.md",
    "kk": PROJECT_ROOT / "kk" / "index.md",
}
PUBLIC_BASE_URL = "https://saubakirov.github.io/KZ-IT-telegram-list"
OG_LOCALES = {"en": "en_US", "ru": "ru_RU", "kk": "kk_KZ"}


@dataclass(frozen=True)
class Projection:
    """One generated public Markdown projection."""

    key: str
    locale: str
    permalink: str | None
    language_links: tuple[tuple[str, str], ...]
    data_path: str
    contributing_path: str
    include_workflow: bool = False


PROJECTIONS = (
    Projection(
        key="readme",
        locale="en",
        permalink=None,
        language_links=(("EN", "README.md"), ("RU", "ru/index.md"), ("KK", "kk/index.md")),
        data_path="data/communities.json",
        contributing_path="CONTRIBUTING.md",
        include_workflow=True,
    ),
    Projection(
        key="en",
        locale="en",
        permalink="/",
        language_links=(("EN", "./"), ("RU", "ru/"), ("KK", "kk/")),
        data_path="data/communities.json",
        contributing_path="CONTRIBUTING.md",
    ),
    Projection(
        key="ru",
        locale="ru",
        permalink="/ru/",
        language_links=(("EN", "../"), ("RU", "./"), ("KK", "../kk/")),
        data_path="../data/communities.json",
        contributing_path="../CONTRIBUTING.md",
    ),
    Projection(
        key="kk",
        locale="kk",
        permalink="/kk/",
        language_links=(("EN", "../"), ("RU", "../ru/"), ("KK", "./")),
        data_path="../data/communities.json",
        contributing_path="../CONTRIBUTING.md",
    ),
)


def load_communities(path: Path = DATA_FILE) -> dict:
    """Load community data from a UTF-8 JSON file."""
    return load_data(path)


def normalize_newlines(value: str) -> str:
    """Normalize platform line endings for non-mutating currency checks."""
    return value.replace("\r\n", "\n").replace("\r", "\n")


def localized_key(base: str, locale: str) -> str:
    """Return the explicit source key for one locale."""
    return base if locale == "en" else f"{base}_{locale}"


def localized_value(container: dict, base: str, locale: str) -> str:
    """Read one localized value without fallback."""
    value = container[localized_key(base, locale)]
    if not isinstance(value, str):
        raise ValueError(f"{localized_key(base, locale)} must be a string")
    return value


def yaml_string(value: str) -> str:
    """Encode one UTF-8 string as a JSON-compatible YAML scalar."""
    return json.dumps(value, ensure_ascii=False)


def generate_front_matter(data: dict, projection: Projection) -> str:
    """Generate Jekyll route fields without placing them in the visible body."""
    if projection.permalink is None:
        return ""
    meta = data["meta"]
    alternate_locales = [
        value for locale, value in OG_LOCALES.items() if locale != projection.locale
    ]
    lines = [
            "---",
            "layout: default",
            f"permalink: {projection.permalink}",
            f"lang: {projection.locale}",
            f"title: {yaml_string(localized_value(meta, 'title', projection.locale))}",
            f"description: {yaml_string(localized_value(meta, 'description', projection.locale))}",
            f"canonical_url: {yaml_string(PUBLIC_BASE_URL + projection.permalink)}",
            f"last_modified: {meta['last_updated']}",
            f"og_locale: {OG_LOCALES[projection.locale]}",
            "og_locale_alternates:",
    ]
    lines.extend(f"  - {value}" for value in alternate_locales)
    lines.extend(
        [
            "sitemap: true",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def category_names(data: dict, locale: str) -> dict[str, str]:
    """Return explicit category labels for *locale*."""
    return data["categories"] if locale == "en" else data["category_labels"][locale]


def markdown_text(value: object) -> str:
    """Escape text so punctuation remains literal across Markdown renderers."""
    text = str(value).replace("\\", "\\\\")
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for character in ("`", "*", "_", "[", "]", "|"):
        text = text.replace(character, f"\\{character}")
    return text.replace("\r", " ").replace("\n", " ")


def table_cell(value: object) -> str:
    """Escape one Markdown table cell without changing visible text."""
    return markdown_text(value)


def stable_handle_id(handle: str) -> str:
    """Return the locale-invariant destination for a catalog record."""
    return f"entry-{handle.casefold()}"


def type_id(entry_type: str) -> str:
    """Return the stable destination for one live entry type."""
    return f"type-{entry_type}"


def category_id(entry_type: str, category: str) -> str:
    """Return the stable destination for one non-empty type/category pair."""
    return f"type-{entry_type}-category-{category}"


def intent_id(intent: str) -> str:
    """Return the stable destination for one intent map row."""
    return f"intent-{intent}"


def format_member_count(count: int | None) -> str:
    """Format an optional member count exactly, never as an estimate."""
    return f"`{count:,}`" if count is not None else ""


def sorted_entries(entries: list[dict]) -> list[dict]:
    """Order entries by exact count descending, then invariant name."""
    return sorted(
        entries,
        key=lambda entry: (
            -(entry.get("member_count") or 0),
            entry["name"].casefold(),
        ),
    )


def format_entry(entry: dict, locale: str, ui: dict[str, str]) -> str:
    """Render one complete live record with a stable explicit destination."""
    parts = [
        f"[{markdown_text(entry['name'])}](https://t.me/{entry['handle']})",
        f"`@{entry['handle']}`",
    ]
    count = format_member_count(entry.get("member_count"))
    if count:
        parts.append(count)
    parts.append(f"{ui['stats.verified']} `{entry['last_verified']}`")
    identity = " · ".join(parts)
    description = markdown_text(localized_value(entry, "description", locale))
    return f'- <a id="{stable_handle_id(entry["handle"])}"></a>{identity} — {description}'


def entries_by_category(entries: list[dict]) -> tuple[list[dict], dict[str, list[dict]]]:
    """Split uncategorized entries from category-backed entries."""
    uncategorized: list[dict] = []
    categorized: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        category = entry.get("category")
        if category is None:
            uncategorized.append(entry)
        else:
            categorized[category].append(entry)
    return uncategorized, categorized


def generate_type_section(
    data: dict,
    entry_type: str,
    locale: str,
    ui: dict[str, str],
) -> str:
    """Generate one type-first live catalog section."""
    heading = ui[f"section.{entry_type}"]
    lines = [f'## <a id="{type_id(entry_type)}"></a>{markdown_text(heading)}', ""]
    entries = data[entry_type]
    uncategorized, categorized = entries_by_category(entries)
    lines.extend(format_entry(entry, locale, ui) for entry in sorted_entries(uncategorized))
    if uncategorized:
        lines.append("")

    labels = category_names(data, locale)
    for category in data["categories"]:
        category_entries = categorized.get(category, [])
        if not category_entries:
            continue
        lines.extend(
            [
                f'### <a id="{category_id(entry_type, category)}"></a>'
                f"{markdown_text(heading)} · {markdown_text(labels[category])}",
                "",
            ]
        )
        lines.extend(
            format_entry(entry, locale, ui)
            for entry in sorted_entries(category_entries)
        )
        lines.append("")
    return "\n".join(lines)


def live_entry_lookup(data: dict) -> dict[str, tuple[str, dict]]:
    """Map case-folded handles to their type and record."""
    return {
        entry["handle"].casefold(): (entry_type, entry)
        for entry_type in ENTRY_TYPES
        for entry in data[entry_type]
    }


def intent_links(data: dict, intent: str, locale: str, ui: dict[str, str]) -> list[str]:
    """Link one intent to non-empty category and exceptional entry destinations."""
    definition = data["intents"][intent]
    labels = category_names(data, locale)
    links: list[str] = []
    for entry_type in ENTRY_TYPES:
        entries = data[entry_type]
        for category in definition["categories"]:
            if any(entry.get("category") == category for entry in entries):
                label = f"{ui[f'type.{entry_type[:-1]}']}: {labels[category]}"
                links.append(
                    f"[{markdown_text(label)}](#{category_id(entry_type, category)})"
                )

    by_handle = live_entry_lookup(data)
    for handle in definition["exceptional_handles"]:
        entry = by_handle[handle.casefold()][1]
        links.append(
            f"[{markdown_text(entry['name'])}](#{stable_handle_id(entry['handle'])})"
        )
    return links


def generate_navigation(data: dict, projection: Projection, ui: dict[str, str]) -> str:
    """Generate one-action language, type, and five-intent navigation."""
    language_links = " · ".join(
        f"[{label}]({target})" for label, target in projection.language_links
    )
    type_links = " · ".join(
        f"[{markdown_text(ui[f'section.{entry_type}'])}](#{type_id(entry_type)})"
        for entry_type in ENTRY_TYPES
    )
    intent_nav = " · ".join(
        f"[{markdown_text(ui[f'intent.{intent}'])}](#{intent_id(intent)})"
        for intent in INTENT_IDS
    )
    lines = [
        f"**{markdown_text(ui['nav.languages'])}:** {language_links}",
        "",
        f"**{markdown_text(ui['nav.types'])}:** {type_links}",
        "",
        f"**{markdown_text(ui['nav.intents'])}:** {intent_nav}",
        "",
    ]
    for intent in INTENT_IDS:
        links = intent_links(data, intent, projection.locale, ui)
        lines.append(
            f'- <a id="{intent_id(intent)}"></a>'
            f"**{markdown_text(ui[f'intent.{intent}'])}:** " + " · ".join(links)
        )
    lines.append("")
    return "\n".join(lines)


def archive_count(value: object) -> str:
    """Format an archive count as a last-known exact value."""
    return f"{value:,}" if isinstance(value, int) and not isinstance(value, bool) else "—"


def generate_archive_section(data: dict, locale: str, ui: dict[str, str]) -> str:
    """Generate a portable archive table whose links remain interactive."""
    archive = data["archive"]
    if not archive:
        return ""
    headings = (
        ui["archive.column.type"],
        ui["archive.column.community"],
        ui["archive.column.description"],
        ui["archive.column.member_count"],
        ui["archive.column.last_verified"],
        ui["archive.column.died_on"],
        ui["archive.column.reason"],
    )
    lines = [
        f"## {markdown_text(ui['section.archive'])}",
        "",
        f"{markdown_text(ui['archive.summary'])}: **{len(archive)}**",
        "",
        "| " + " | ".join(table_cell(value) for value in headings) + " |",
        "|---|---|---|---:|---|---|---|",
    ]
    labels = category_names(data, locale)
    for entry in sorted_entries(archive):
        entry_type = entry["type"][:-1]
        type_label = ui[f"type.{entry_type}"]
        if entry.get("category"):
            type_label = f"{type_label} · {labels[entry['category']]}"
        community = (
            f'<a id="{stable_handle_id(entry["handle"])}"></a>'
            f"[{markdown_text(entry['name'])}](https://t.me/{entry['handle']}) "
            f"`@{entry['handle']}`"
        )
        cells = (
            table_cell(type_label),
            community,
            table_cell(localized_value(entry, "description", locale)),
            table_cell(archive_count(entry.get("member_count"))),
            table_cell(entry["last_verified"]),
            table_cell(entry["died_on"]),
            table_cell(localized_value(entry, "reason", locale)),
        )
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return "\n".join(lines)


def oldest_live_verification(*entry_sets: list[dict]) -> str:
    """Return the conservative freshness date across all live entries."""
    dates = [entry["last_verified"] for entries in entry_sets for entry in entries]
    return min(dates)


def generate_purpose(data: dict, locale: str, ui: dict[str, str]) -> str:
    """Generate the localized North Star after the catalog."""
    north_star = data["north_star"]
    lines = [
        f"## {markdown_text(ui['section.purpose'])}",
        "",
        markdown_text(localized_value(north_star, "purpose", locale)),
        "",
        f"**{markdown_text(ui['north_star.non_goals_intro'])}**",
        "",
    ]
    lines.extend(
        f"- {markdown_text(value)}"
        for value in north_star[localized_key("non_goals", locale)]
    )
    lines.append("")
    return "\n".join(lines)


def generate_supporting_sections(
    data: dict,
    projection: Projection,
    ui: dict[str, str],
) -> str:
    """Generate data, contribution, optional workflow, provenance, and license sections."""
    lines = [
        f"## {markdown_text(ui['section.data'])}",
        "",
        f"[{markdown_text(ui['data.download_label'])}]({projection.data_path})",
        "",
        f"## {markdown_text(ui['section.contributing'])}",
        "",
        f"{markdown_text(ui['contributing.prompt'])} "
        f"[{markdown_text('CONTRIBUTING.md')}]({projection.contributing_path})",
        "",
    ]
    if projection.include_workflow:
        workflow = data["readme_ui"]
        lines.extend(
            [
                f"## {markdown_text(workflow['section.project_workflow'])}",
                "",
                markdown_text(workflow["workflow.intro"]),
                "",
                f"- **[{markdown_text(workflow['workflow.portfolio.label'])}](tasks/00-INDEX.md):** "
                f"{markdown_text(workflow['workflow.portfolio.description'])}",
                f"- **[{markdown_text(workflow['workflow.knowledge.label'])}](KNOWLEDGE.md):** "
                f"{markdown_text(workflow['workflow.knowledge.description'])}",
                f"- **[{markdown_text(workflow['workflow.agents.label'])}](AGENTS.md):** "
                f"{markdown_text(workflow['workflow.agents.description'])}",
                "",
            ]
        )
    lines.extend(
        [
            f"> {markdown_text(ui['generated.notice'])}",
            "",
            f"## {markdown_text(ui['section.license'])}",
            "",
            "[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)",
            "",
            markdown_text(ui["license.waiver"]),
            "",
        ]
    )
    return "\n".join(lines)


def render_projection(data: dict, projection: Projection) -> str:
    """Render one complete locale projection."""
    locale = projection.locale
    ui = data["ui"][locale]
    groups = data["groups"]
    channels = data["channels"]
    bots = data["bots"]
    verification_date = oldest_live_verification(groups, channels, bots)
    meta = data["meta"]
    stats = (
        f"**{len(groups)}** {markdown_text(ui['stats.groups'])} · "
        f"**{len(channels)}** {markdown_text(ui['stats.channels'])} · "
        f"**{len(bots)}** {markdown_text(ui['stats.bots'])} · "
        f"**{len(data['categories'])}** {markdown_text(ui['stats.categories'])} · "
        f"{markdown_text(ui['stats.verified'])} **{verification_date}**"
    )
    lines = [
        generate_front_matter(data, projection).rstrip("\n"),
        f"# {markdown_text(localized_value(meta, 'title', locale))}",
        "",
        f"> {markdown_text(localized_value(meta, 'description', locale))}.",
        "",
        stats,
        "",
        generate_navigation(data, projection, ui).rstrip(),
        "",
    ]
    lines.extend(
        generate_type_section(data, entry_type, locale, ui).rstrip()
        for entry_type in ENTRY_TYPES
    )
    lines.extend(
        [
            generate_archive_section(data, locale, ui).rstrip(),
            generate_purpose(data, locale, ui).rstrip(),
            generate_supporting_sections(data, projection, ui).rstrip(),
            "",
        ]
    )
    return "\n\n".join(part for part in lines if part != "")


def generate_readme(data: dict) -> str:
    """Render the English GitHub README projection."""
    return render_projection(data, PROJECTIONS[0])


def generated_outputs(data: dict) -> dict[Path, str]:
    """Return all four generated paths and contents."""
    return {
        OUTPUT_PATHS[projection.key]: render_projection(data, projection)
        for projection in PROJECTIONS
    }


def presentation_errors(content: str, data: dict, projection: Projection) -> list[str]:
    """Return deterministic semantic errors in one generated Markdown body."""
    errors: list[str] = []
    ids = re.findall(r'<a id="([^"]+)"></a>', content)
    id_counts = {destination: ids.count(destination) for destination in set(ids)}
    duplicate_ids = sorted(key for key, count in id_counts.items() if count != 1)
    if duplicate_ids:
        errors.append(f"duplicate destinations: {duplicate_ids}")

    fragments = re.findall(r"\]\(#([^)]+)\)", content)
    unresolved = sorted(fragment for fragment in fragments if id_counts.get(fragment) != 1)
    if unresolved:
        errors.append(f"unresolved fragments: {unresolved}")

    h1_count = len(re.findall(r"(?m)^#\s+", content))
    if h1_count != 1:
        errors.append(f"expected one h1, found {h1_count}")

    first_target = content.find("https://t.me/")
    purpose = content.find(f"## {markdown_text(data['ui'][projection.locale]['section.purpose'])}")
    if first_target < 0 or purpose < 0 or first_target > purpose:
        errors.append("a complete live entry must precede Purpose")

    ui = data["ui"][projection.locale]
    language_line = next(
        (
            line
            for line in content.splitlines()
            if line.startswith(f"**{markdown_text(ui['nav.languages'])}:**")
        ),
        "",
    )
    if not language_line or any(
        f"[{label}]({target})" not in language_line
        for label, target in projection.language_links
    ):
        errors.append("language routes are incomplete or not in one action")

    all_records = [
        (entry_type, entry)
        for entry_type in ENTRY_TYPES
        for entry in data[entry_type]
    ] + [("archive", entry) for entry in data["archive"]]
    lines = content.splitlines()
    for entry_type, entry in all_records:
        url = f"https://t.me/{entry['handle']}"
        matching_lines = [line for line in lines if f"]({url})" in line]
        if len(matching_lines) != 1:
            errors.append(f"@{entry['handle']}: expected one Telegram target, found {len(matching_lines)}")
            continue
        line = matching_lines[0]
        expected_link = f"[{markdown_text(entry['name'])}]({url})"
        if expected_link not in line:
            errors.append(f"@{entry['handle']}: visible name/target pair changed")
        if f"`@{entry['handle']}`" not in line:
            errors.append(f"@{entry['handle']}: invariant handle is missing")
        description = markdown_text(
            localized_value(entry, "description", projection.locale)
        )
        if description not in line:
            errors.append(f"@{entry['handle']}: localized description is missing")
        if id_counts.get(stable_handle_id(entry["handle"])) != 1:
            errors.append(f"@{entry['handle']}: stable destination is missing")
        if entry_type == "archive":
            for value in (
                entry["last_verified"],
                entry["died_on"],
                localized_value(entry, "reason", projection.locale),
            ):
                if markdown_text(value) not in line:
                    errors.append(f"@{entry['handle']}: archive fact is missing")
        else:
            if entry["last_verified"] not in line:
                errors.append(f"@{entry['handle']}: verification date is missing")
        count = entry.get("member_count")
        if count is not None and f"{count:,}" not in line:
            errors.append(f"@{entry['handle']}: exact member count is missing")

    for entry_type in ENTRY_TYPES:
        if id_counts.get(type_id(entry_type)) != 1:
            errors.append(f"missing type destination: {entry_type}")
    for intent in INTENT_IDS:
        if id_counts.get(intent_id(intent)) != 1:
            errors.append(f"missing intent destination: {intent}")
    return errors


def validate_generated_outputs(data: dict, outputs: dict[Path, str]) -> list[str]:
    """Validate all generated bodies before checking or writing them."""
    errors: list[str] = []
    for projection in PROJECTIONS:
        path = OUTPUT_PATHS[projection.key]
        for error in presentation_errors(outputs[path], data, projection):
            errors.append(f"{path.relative_to(PROJECT_ROOT)}: {error}")
    return errors


def read_current(path: Path) -> str:
    """Read a generated candidate as UTF-8 without mutating it."""
    with path.open("r", encoding="utf-8", newline="") as source:
        return source.read()


def is_current(generated: str, path: Path = README_FILE) -> bool:
    """Compare generated/current content after explicit newline normalization."""
    return path.exists() and normalize_newlines(generated) == normalize_newlines(
        read_current(path)
    )


def check_outputs(outputs: dict[Path, str]) -> list[Path]:
    """Return every missing or stale output without mutating the worktree."""
    return [path for path, content in outputs.items() if not is_current(content, path)]


def write_outputs(outputs: dict[Path, str]) -> None:
    """Write all generated files through adjacent temporary files."""
    temporary_paths: list[tuple[Path, Path]] = []
    try:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_name(f".{path.name}.tmp")
            with temporary.open("w", encoding="utf-8", newline="\n") as destination:
                destination.write(content)
            temporary_paths.append((temporary, path))
        for temporary, path in temporary_paths:
            temporary.replace(path)
    finally:
        for temporary, _ in temporary_paths:
            if temporary.exists():
                temporary.unlink()


def parse_args() -> argparse.Namespace:
    """Parse generator/check options."""
    parser = argparse.ArgumentParser(description="Generate or verify catalog projections")
    parser.add_argument("--check", action="store_true", help="Check currency without writing")
    parser.add_argument("--data", type=Path, default=DATA_FILE, help="Catalog JSON path")
    return parser.parse_args()


def main() -> int:
    """Generate every projection or run the non-mutating currency gate."""
    args = parse_args()
    try:
        data = load_communities(args.data)
    except (OSError, json.JSONDecodeError) as error:
        print(f"[ERROR] Could not load catalog data: {error}")
        return 1

    errors, _ = validate_data(data)
    if errors:
        print(f"[ERROR] Refusing to generate from invalid data ({len(errors)} errors)")
        for error in errors:
            print(f"[ERROR] {error}")
        return 1

    try:
        outputs = generated_outputs(data)
    except (KeyError, TypeError, ValueError) as error:
        print(f"[ERROR] Could not generate catalog projections: {error}")
        return 1

    presentation_failures = validate_generated_outputs(data, outputs)
    if presentation_failures:
        print(
            f"[ERROR] Refusing invalid generated projections "
            f"({len(presentation_failures)} errors)"
        )
        for error in presentation_failures:
            print(f"[ERROR] {error}")
        return 1

    stale = check_outputs(outputs)
    if args.check:
        if stale:
            for path in stale:
                print(f"[ERROR] Generated output is missing or stale: {path}")
            return 1
        print(f"[SUCCESS] All {len(outputs)} catalog projections are generator-current")
        print(f"[INFO] Locale payload sha256={review_payload_sha256(data)}")
        return 0

    try:
        write_outputs(outputs)
    except OSError as error:
        print(f"[ERROR] Could not write generated projections: {error}")
        return 1

    for path in outputs:
        print(f"[OK] Generated {path.relative_to(PROJECT_ROOT)}")
    print(
        f"[INFO] Live entries: groups={len(data['groups'])}; "
        f"channels={len(data['channels'])}; bots={len(data['bots'])}; "
        f"categories={len(data['categories'])}; "
        f"oldest_verified={oldest_live_verification(data['groups'], data['channels'], data['bots'])}"
    )
    print(f"[INFO] Locale payload sha256={review_payload_sha256(data)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

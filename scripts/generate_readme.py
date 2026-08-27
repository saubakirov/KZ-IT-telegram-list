#!/usr/bin/env python3
"""Generate or verify README.md from the structured community catalog.

Usage:
    python scripts/generate_readme.py
    python scripts/generate_readme.py --check
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "communities.json"
README_FILE = PROJECT_ROOT / "README.md"


def load_communities(path: Path = DATA_FILE) -> dict:
    """Load community data from a UTF-8 JSON file."""
    with path.open("r", encoding="utf-8") as source:
        return json.load(source)


def normalize_newlines(value: str) -> str:
    """Normalize platform line endings for the non-mutating currency check."""
    return value.replace("\r\n", "\n").replace("\r", "\n")


def github_slug(heading: str) -> str:
    """Return the GitHub-compatible slug needed by current category headings."""
    slug = re.sub(r"[^\w\s-]", "", heading.casefold())
    return re.sub(r"\s", "-", slug)


def ordered_categories(groups: list[dict], category_names: dict[str, str]) -> list[str]:
    """Return used category keys ordered by their display names."""
    used = {group.get("category", "general") for group in groups}
    return sorted(
        (key for key in used if key in category_names),
        key=lambda key: (category_names[key].casefold(), key.casefold()),
    )


def generate_toc(
    categories_used: list[str],
    category_names: dict[str, str],
    has_archive: bool,
) -> str:
    """Generate the table of contents."""
    lines = ["## Contents", "", "- [Groups](#groups)"]
    for category in categories_used:
        display_name = category_names[category]
        lines.append(f"  - [{display_name}](#{github_slug(display_name)})")

    lines.extend(["- [Channels](#channels)", "- [Bots](#bots)"])
    if has_archive:
        lines.append("- [Archive](#archive)")
    lines.extend(
        [
            "- [Contributing](#contributing)",
            "- [Project Workflow](#project-workflow)",
            "",
        ]
    )
    return "\n".join(lines)


def format_member_count(count: int | None) -> str:
    """Format an optional live member count."""
    if count is None:
        return ""
    if count >= 1000:
        return f" `{count / 1000:.1f}k`"
    return f" `{count}`"


def format_entry(entry: dict) -> str:
    """Format one live community entry."""
    count = format_member_count(entry.get("member_count"))
    return f"- [{entry['name']}](https://t.me/{entry['handle']}){count} - {entry['description']}"


def generate_groups_section(
    groups: list[dict],
    category_names: dict[str, str],
    categories_used: list[str],
) -> str:
    """Generate groups organized by display-name-ordered category."""
    lines = ["## Groups", ""]
    by_category: dict[str, list[dict]] = defaultdict(list)
    for group in groups:
        by_category[group.get("category", "general")].append(group)

    for category in categories_used:
        lines.extend([f"### {category_names[category]}", ""])
        entries = sorted(
            by_category[category],
            key=lambda entry: (
                -(entry.get("member_count") or 0),
                entry["name"].casefold(),
            ),
        )
        lines.extend(format_entry(entry) for entry in entries)
        lines.append("")
    return "\n".join(lines)


def generate_channels_section(channels: list[dict]) -> str:
    """Generate the live channels section."""
    lines = ["## Channels", ""]
    entries = sorted(
        channels,
        key=lambda entry: (
            -(entry.get("member_count") or 0),
            entry["name"].casefold(),
        ),
    )
    lines.extend(format_entry(entry) for entry in entries)
    lines.append("")
    return "\n".join(lines)


def generate_bots_section(bots: list[dict]) -> str:
    """Generate the live bots section."""
    lines = ["## Bots", "", "Bots created by Kazakhstan developers:", ""]
    entries = sorted(
        bots,
        key=lambda entry: (
            -(entry.get("member_count") or 0),
            entry["name"].casefold(),
        ),
    )
    lines.extend(format_entry(entry) for entry in entries)
    lines.append("")
    return "\n".join(lines)


def table_cell(value: object) -> str:
    """Escape one Markdown table cell."""
    return str(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def archive_count(value: object) -> str:
    """Format an archive count as a last-known exact value."""
    return str(value) if isinstance(value, int) else "—"


def generate_archive_section(archive: list[dict]) -> str:
    """Generate the collapsed archive table."""
    type_labels = {"groups": "Group", "channels": "Channel", "bots": "Bot"}
    lines = [
        "## Archive",
        "",
        "<details>",
        f"<summary>Archived communities ({len(archive)})</summary>",
        "",
        "| Type | Community | Description | Last known members | Last verified | Died on | Reason |",
        "|------|-----------|-------------|--------------------|---------------|---------|--------|",
    ]
    entries = sorted(
        archive,
        key=lambda entry: (
            str(entry.get("type", "")).casefold(),
            str(entry.get("name", "")).casefold(),
        ),
    )
    for entry in entries:
        community = f"[{entry['name']}](https://t.me/{entry['handle']})"
        cells = (
            type_labels.get(entry.get("type"), str(entry.get("type", ""))),
            community,
            entry["description"],
            archive_count(entry.get("member_count")),
            entry["last_verified"],
            entry["died_on"],
            entry["reason"],
        )
        lines.append("| " + " | ".join(table_cell(cell) for cell in cells) + " |")
    lines.extend(["", "</details>", ""])
    return "\n".join(lines)


def oldest_live_verification(*entry_sets: list[dict]) -> str:
    """Return the conservative freshness date across all live entries."""
    dates = [entry["last_verified"] for entries in entry_sets for entry in entries]
    return min(dates)


def generate_readme(data: dict) -> str:
    """Render the complete README from parsed catalog data."""
    groups = data.get("groups", [])
    channels = data.get("channels", [])
    bots = data.get("bots", [])
    archive = data.get("archive", [])
    category_names = data.get("categories", {})
    north_star = data.get("north_star", {})
    categories_used = ordered_categories(groups, category_names)
    verification_date = oldest_live_verification(groups, channels, bots)

    lines = [
        "# Awesome Kazakhstan IT Telegram",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Kazakhstan](https://img.shields.io/badge/🇰🇿-Kazakhstan-00AFCA)",
        "",
        "> A curated list of IT-related Telegram groups, channels, and bots for the Kazakhstan tech community.",
        "",
        "🇰🇿 Focused on Kazakhstan's IT ecosystem — from programming languages and DevOps to startups and job postings.",
        "",
        f"**{len(groups)}** groups · **{len(channels)}** channels · **{len(bots)}** bots · "
        f"**{len(category_names)}** categories · verified **{verification_date}**",
        "",
        "## Purpose",
        "",
        north_star["purpose"],
        "",
        "**This list is not:**",
        "",
    ]
    lines.extend(f"- {non_goal}" for non_goal in north_star["non_goals"])
    lines.append("")
    lines.append(generate_toc(categories_used, category_names, bool(archive)))
    lines.append(generate_groups_section(groups, category_names, categories_used))
    lines.append(generate_channels_section(channels))
    lines.append(generate_bots_section(bots))
    if archive:
        lines.append(generate_archive_section(archive))

    lines.extend(
        [
            "## Contributing",
            "",
            "Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.",
            "",
            "## Project Workflow",
            "",
            "This project is maintained with [Trace-First Workflow](https://github.com/saubakirov/trace-first-starter) — "
            "decisions and their reasoning are kept as durable traces, not lost in chat history.",
            "",
            "- **[Task Board](tasks/README.md)** — current and completed work",
            "- **[KNOWLEDGE.md](KNOWLEDGE.md)** — architecture decisions and project principles",
            "- **[AGENTS.md](AGENTS.md)** — how AI agents work in this repository",
            "",
            "> ⚠️ **This README is generated.** Edit [`data/communities.json`](data/communities.json) "
            "and run `python scripts/generate_readme.py` — direct edits here are overwritten.",
            "",
            "## License",
            "",
            "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)",
            "",
            "To the extent possible under law, the authors have waived all copyright and related rights to this work.",
            "",
        ]
    )
    return "\n".join(lines)


def read_current(path: Path) -> str:
    """Read a README candidate as UTF-8 without mutating it."""
    with path.open("r", encoding="utf-8", newline="") as source:
        return source.read()


def is_current(generated: str, path: Path = README_FILE) -> bool:
    """Compare generated/current content after explicit newline normalization."""
    if not path.exists():
        return False
    return normalize_newlines(generated) == normalize_newlines(read_current(path))


def write_readme(content: str, path: Path = README_FILE) -> None:
    """Write generated README content with stable LF newlines."""
    with path.open("w", encoding="utf-8", newline="\n") as destination:
        destination.write(content)


def parse_args() -> argparse.Namespace:
    """Parse generator/check options."""
    parser = argparse.ArgumentParser(description="Generate or verify README.md")
    parser.add_argument("--check", action="store_true", help="Check currency without writing")
    parser.add_argument("--data", type=Path, default=DATA_FILE, help="Catalog JSON path")
    parser.add_argument("--readme", type=Path, default=README_FILE, help="README path")
    return parser.parse_args()


def main() -> int:
    """Generate README or run the non-mutating currency gate."""
    args = parse_args()
    try:
        data = load_communities(args.data)
        content = generate_readme(data)
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as error:
        print(f"[ERROR] Could not generate README content: {error}")
        return 1

    if args.check:
        if is_current(content, args.readme):
            print(f"[SUCCESS] README is generator-current: {args.readme}")
            return 0
        print(f"[ERROR] README differs from generator output: {args.readme}")
        return 1

    try:
        write_readme(content, args.readme)
    except OSError as error:
        print(f"[ERROR] Could not write {args.readme}: {error}")
        return 1

    groups = data.get("groups", [])
    channels = data.get("channels", [])
    bots = data.get("bots", [])
    print(f"[OK] Generated {args.readme}")
    print(
        f"[INFO] Live entries: groups={len(groups)}; channels={len(channels)}; "
        f"bots={len(bots)}; categories={len(data.get('categories', {}))}; "
        f"oldest_verified={oldest_live_verification(groups, channels, bots)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

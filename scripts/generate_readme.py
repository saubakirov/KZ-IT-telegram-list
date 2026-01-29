#!/usr/bin/env python3
"""
Generate README.md from communities.json

Usage:
    python scripts/generate_readme.py

Generates a properly formatted Awesome List README.
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

DATA_FILE = Path(__file__).parent.parent / "data" / "communities.json"
README_FILE = Path(__file__).parent.parent / "README.md"


def load_communities() -> dict:
    """Load communities from JSON file."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_toc(categories_used: list[str], category_names: dict) -> str:
    """Generate table of contents."""
    lines = ["## Contents", ""]
    
    lines.append("- [Groups](#groups)")
    for cat in sorted(categories_used):
        if cat in category_names:
            anchor = category_names[cat].lower().replace(" ", "-").replace("&", "")
            lines.append(f"  - [{category_names[cat]}](#{anchor})")
    
    lines.append("- [Channels](#channels)")
    lines.append("- [Bots](#bots)")
    lines.append("- [Contributing](#contributing)")
    lines.append("")
    return "\n".join(lines)


def generate_groups_section(groups: list, category_names: dict) -> str:
    """Generate groups section organized by category."""
    lines = ["## Groups", ""]
    
    # Group by category
    by_category = defaultdict(list)
    for g in groups:
        by_category[g.get("category", "general")].append(g)
    
    # Sort categories
    for cat in sorted(by_category.keys()):
        cat_name = category_names.get(cat, cat.title())
        lines.append(f"### {cat_name}")
        lines.append("")
        
        # Sort entries alphabetically
        for entry in sorted(by_category[cat], key=lambda x: x["name"].lower()):
            lines.append(f"- [{entry['name']}](https://t.me/{entry['handle']}) - {entry['description']}")
        
        lines.append("")
    
    return "\n".join(lines)


def generate_channels_section(channels: list) -> str:
    """Generate channels section."""
    lines = ["## Channels", ""]
    
    for entry in sorted(channels, key=lambda x: x["name"].lower()):
        lines.append(f"- [{entry['name']}](https://t.me/{entry['handle']}) - {entry['description']}")
    
    lines.append("")
    return "\n".join(lines)


def generate_bots_section(bots: list) -> str:
    """Generate bots section."""
    lines = ["## Bots", "", "Bots created by Kazakhstan developers:", ""]
    
    for entry in sorted(bots, key=lambda x: x["name"].lower()):
        lines.append(f"- [{entry['name']}](https://t.me/{entry['handle']}) - {entry['description']}")
    
    lines.append("")
    return "\n".join(lines)


def generate_readme(data: dict) -> str:
    """Generate complete README content."""
    meta = data.get("meta", {})
    groups = data.get("groups", [])
    channels = data.get("channels", [])
    bots = data.get("bots", [])
    category_names = data.get("categories", {})
    
    # Collect used categories
    categories_used = set(g.get("category", "general") for g in groups)
    
    lines = []
    
    # Header
    lines.append("# Awesome Kazakhstan IT Telegram")
    lines.append("")
    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append("> A curated list of IT-related Telegram groups, channels, and bots for the Kazakhstan tech community.")
    lines.append("")
    lines.append("🇰🇿 Focused on Kazakhstan's IT ecosystem — from programming languages and DevOps to startups and job postings.")
    lines.append("")
    
    # Stats
    lines.append(f"**{len(groups)}** groups · **{len(channels)}** channels · **{len(bots)}** bots")
    lines.append("")
    
    # TOC
    lines.append(generate_toc(list(categories_used), category_names))
    
    # Sections
    lines.append(generate_groups_section(groups, category_names))
    lines.append(generate_channels_section(channels))
    lines.append(generate_bots_section(bots))
    
    # Contributing
    lines.append("## Contributing")
    lines.append("")
    lines.append("Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)")
    lines.append("")
    lines.append("To the extent possible under law, the authors have waived all copyright and related rights to this work.")
    lines.append("")
    
    return "\n".join(lines)


def main():
    if not DATA_FILE.exists():
        print(f"[ERROR] Data file not found: {DATA_FILE}")
        return
    
    data = load_communities()
    readme_content = generate_readme(data)
    
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"[OK] Generated {README_FILE}")
    print(f"   Groups: {len(data.get('groups', []))}")
    print(f"   Channels: {len(data.get('channels', []))}")
    print(f"   Bots: {len(data.get('bots', []))}")


if __name__ == "__main__":
    main()

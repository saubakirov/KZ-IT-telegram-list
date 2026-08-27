#!/usr/bin/env python3
"""Validate deterministic contracts in a built Jekyll catalog site."""

import argparse
import html
import hashlib
import json
import struct
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

try:
    from .generate_readme import ENTRY_TYPES, INTENT_IDS, category_id, load_communities, stable_handle_id
except ImportError:  # Direct script execution.
    from generate_readme import ENTRY_TYPES, INTENT_IDS, category_id, load_communities, stable_handle_id  # type: ignore

PROJECT_ROOT = Path(__file__).parent.parent
ROUTES = {
    "en": Path("index.html"),
    "ru": Path("ru/index.html"),
    "kk": Path("kk/index.html"),
}
PUBLIC_BASE_URL = "https://saubakirov.github.io/KZ-IT-telegram-list"
CANONICALS = {
    "en": f"{PUBLIC_BASE_URL}/",
    "ru": f"{PUBLIC_BASE_URL}/ru/",
    "kk": f"{PUBLIC_BASE_URL}/kk/",
}
ALTERNATES = {
    "en": CANONICALS["en"],
    "ru": CANONICALS["ru"],
    "kk": CANONICALS["kk"],
    "x-default": CANONICALS["en"],
}
OG_LOCALES = {"en": "en_US", "ru": "ru_RU", "kk": "kk_KZ"}
SOCIAL_IMAGE_URL = f"{PUBLIC_BASE_URL}/assets/social-preview.png"


class RouteParser(HTMLParser):
    """Collect the semantic route facts needed by the site contract."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_langs: list[str | None] = []
        self.ids: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.link_tags: list[dict[str, str | None]] = []
        self.meta_tags: list[dict[str, str | None]] = []
        self.titles: list[str] = []
        self.json_ld: list[str] = []
        self._title_parts: list[str] | None = None
        self._json_ld_parts: list[str] | None = None
        self.h1_texts: list[str] = []
        self._h1_parts: list[str] | None = None
        self._anchor_href: str | None = None
        self._anchor_parts: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.html_langs.append(values.get("lang"))
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if tag == "h1":
            self._h1_parts = []
        if tag == "title":
            self._title_parts = []
        if tag == "link":
            self.link_tags.append(values)
        if tag == "meta":
            self.meta_tags.append(values)
        if tag == "script" and values.get("type") == "application/ld+json":
            self._json_ld_parts = []
        if tag == "a" and values.get("href") is not None:
            self._anchor_href = values["href"]
            self._anchor_parts = []

    def handle_data(self, data: str) -> None:
        if self._h1_parts is not None:
            self._h1_parts.append(data)
        if self._title_parts is not None:
            self._title_parts.append(data)
        if self._json_ld_parts is not None:
            self._json_ld_parts.append(data)
        if self._anchor_parts is not None:
            self._anchor_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self._h1_parts is not None:
            self.h1_texts.append("".join(self._h1_parts).strip())
            self._h1_parts = None
        if tag == "title" and self._title_parts is not None:
            self.titles.append("".join(self._title_parts).strip())
            self._title_parts = None
        if tag == "script" and self._json_ld_parts is not None:
            self.json_ld.append("".join(self._json_ld_parts).strip())
            self._json_ld_parts = None
        if tag == "a" and self._anchor_parts is not None and self._anchor_href is not None:
            self.links.append(("".join(self._anchor_parts).strip(), self._anchor_href))
            self._anchor_href = None
            self._anchor_parts = None


def localized(container: dict, base: str, locale: str) -> str:
    key = base if locale == "en" else f"{base}_{locale}"
    return container[key]


def expected_route_facts(data: dict) -> tuple[set[str], Counter[tuple[str, str]]]:
    entries = [
        entry
        for section in (*ENTRY_TYPES, "archive")
        for entry in data[section]
    ]
    ids = {stable_handle_id(entry["handle"]) for entry in entries}
    ids.update(f"type-{entry_type}" for entry_type in ENTRY_TYPES)
    ids.update(
        category_id(entry_type, entry["category"])
        for entry_type in ENTRY_TYPES
        for entry in data[entry_type]
        if entry.get("category")
    )
    ids.update(f"intent-{intent}" for intent in INTENT_IDS)
    telegram = Counter(
        (entry["name"], f"https://t.me/{entry['handle']}") for entry in entries
    )
    return ids, telegram


def meta_values(parser: RouteParser, attribute: str, key: str) -> list[str | None]:
    return [
        tag.get("content")
        for tag in parser.meta_tags
        if tag.get(attribute) == key
    ]


def expected_dataset(data: dict, locale: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": localized(data["meta"], "title", locale),
        "description": localized(data["meta"], "description", locale),
        "url": CANONICALS[locale],
        "inLanguage": locale,
        "dateModified": data["meta"]["last_updated"],
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "isAccessibleForFree": True,
        "spatialCoverage": {"@type": "Place", "name": "Kazakhstan"},
        "sameAs": data["meta"]["source_repo"],
        "distribution": {
            "@type": "DataDownload",
            "contentUrl": f"{PUBLIC_BASE_URL}/data/communities.json",
            "encodingFormat": "application/json",
        },
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_social_asset(site: Path, errors: list[str]) -> dict[str, object]:
    source = PROJECT_ROOT / "assets" / "social-preview.svg"
    png = PROJECT_ROOT / "assets" / "social-preview.png"
    built_png = site / "assets" / "social-preview.png"
    facts: dict[str, object] = {}
    if not source.is_file() or not png.is_file():
        errors.append("social preview source or PNG is missing")
        return facts
    root = ElementTree.parse(source).getroot()
    if root.get("width") != "1280" or root.get("height") != "640":
        errors.append("social preview SVG is not 1280x640")
    visible_text = [
        "".join(node.itertext())
        for node in root.iter()
        if node.tag.endswith("text")
    ]
    if visible_text != ["Awesome Kazakhstan", "IT Telegram", "EN · RU · KK"]:
        errors.append(f"social preview visible text is {visible_text!r}")
    content = png.read_bytes()
    if len(content) >= 24 and content.startswith(b"\x89PNG\r\n\x1a\n"):
        width, height = struct.unpack(">II", content[16:24])
    else:
        width, height = 0, 0
        errors.append("social preview output is not a valid PNG")
    if (width, height) != (1280, 640):
        errors.append(f"social preview PNG dimensions are {width}x{height}")
    if len(content) >= 1_000_000:
        errors.append(f"social preview PNG is {len(content)} bytes")
    if not built_png.is_file() or built_png.read_bytes() != content:
        errors.append("built social preview PNG differs from repository bytes")
    facts.update(
        {
            "svg_sha256": sha256(source),
            "png_sha256": sha256(png),
            "png_width": width,
            "png_height": height,
            "png_bytes": len(content),
            "visible_text": visible_text,
        }
    )
    return facts


def validate_sitemap(site: Path, errors: list[str]) -> list[str]:
    path = site / "sitemap.xml"
    if not path.is_file():
        errors.append("sitemap.xml is missing from the supported Jekyll build")
        return []
    try:
        root = ElementTree.parse(path).getroot()
        urls = [
            (node.text or "").strip()
            for node in root.iter()
            if node.tag.endswith("loc")
        ]
    except ElementTree.ParseError as error:
        errors.append(f"sitemap.xml is invalid XML: {error}")
        return []
    expected = [CANONICALS["en"], CANONICALS["ru"], CANONICALS["kk"]]
    if set(urls) != set(expected) or len(urls) != len(expected):
        errors.append(f"sitemap URL set is {urls!r}")
    if any(not url.startswith("https://") for url in urls):
        errors.append("sitemap contains a non-HTTPS URL")
    if not (PROJECT_ROOT / "sitemap.xml").is_file():
        errors.append("repository-owned sitemap.xml source is missing")
    for source_name in ("robots.txt", "llms.txt"):
        if (PROJECT_ROOT / source_name).exists():
            errors.append(f"unapproved source discovery file exists: {source_name}")
        if (site / source_name).exists():
            errors.append(f"unapproved discovery file was emitted: {source_name}")
    return urls


def validate_site(site: Path) -> tuple[list[str], dict[str, object]]:
    data = load_communities()
    expected_ids, expected_telegram = expected_route_facts(data)
    errors: list[str] = []
    summary: dict[str, object] = {"routes": {}}
    route_id_sets: dict[str, set[str]] = {}
    for locale, relative in ROUTES.items():
        path = site / relative
        if not path.is_file():
            errors.append(f"{locale}: missing built route {relative.as_posix()}")
            continue
        parser = RouteParser()
        parser.feed(path.read_text(encoding="utf-8"))
        if parser.html_langs != [locale]:
            errors.append(f"{locale}: html lang values are {parser.html_langs!r}")
        expected_h1 = localized(data["meta"], "title", locale)
        if parser.h1_texts != [expected_h1]:
            errors.append(f"{locale}: h1 values are {parser.h1_texts!r}")
        if parser.titles != [expected_h1]:
            errors.append(f"{locale}: title values are {parser.titles!r}")
        descriptions = [
            tag.get("content") for tag in parser.meta_tags if tag.get("name") == "description"
        ]
        expected_description = localized(data["meta"], "description", locale)
        if descriptions != [expected_description]:
            errors.append(f"{locale}: descriptions are {descriptions!r}")
        canonicals = [
            tag.get("href") for tag in parser.link_tags if tag.get("rel") == "canonical"
        ]
        if canonicals != [CANONICALS[locale]]:
            errors.append(f"{locale}: canonicals are {canonicals!r}")
        alternates = {
            tag.get("hreflang"): tag.get("href")
            for tag in parser.link_tags
            if tag.get("rel") == "alternate"
        }
        if alternates != ALTERNATES or len(alternates) != len(
            [tag for tag in parser.link_tags if tag.get("rel") == "alternate"]
        ):
            errors.append(f"{locale}: alternates are {alternates!r}")
        og_expected = {
            "og:type": ["website"],
            "og:site_name": [data["meta"]["title"]],
            "og:title": [expected_h1],
            "og:description": [expected_description],
            "og:url": [CANONICALS[locale]],
            "og:locale": [OG_LOCALES[locale]],
            "og:image": [SOCIAL_IMAGE_URL],
            "og:image:width": ["1280"],
            "og:image:height": ["640"],
            "og:image:alt": [expected_h1],
        }
        for key, expected in og_expected.items():
            actual = meta_values(parser, "property", key)
            if actual != expected:
                errors.append(f"{locale}: {key} values are {actual!r}")
        expected_og_alternates = [
            value for language, value in OG_LOCALES.items() if language != locale
        ]
        actual_og_alternates = meta_values(parser, "property", "og:locale:alternate")
        if actual_og_alternates != expected_og_alternates:
            errors.append(f"{locale}: og locale alternates are {actual_og_alternates!r}")
        twitter_expected = {
            "twitter:card": ["summary_large_image"],
            "twitter:title": [expected_h1],
            "twitter:description": [expected_description],
            "twitter:image": [SOCIAL_IMAGE_URL],
            "twitter:image:alt": [expected_h1],
        }
        for key, expected in twitter_expected.items():
            actual = meta_values(parser, "name", key)
            if actual != expected:
                errors.append(f"{locale}: {key} values are {actual!r}")
        if len(parser.json_ld) != 1:
            errors.append(f"{locale}: JSON-LD block count is {len(parser.json_ld)}")
            dataset: dict = {}
        else:
            try:
                dataset = json.loads(parser.json_ld[0])
            except json.JSONDecodeError as error:
                errors.append(f"{locale}: invalid JSON-LD: {error}")
                dataset = {}
        if dataset != expected_dataset(data, locale):
            errors.append(f"{locale}: Dataset differs from source contract")
        duplicates = sorted(key for key, count in Counter(parser.ids).items() if count != 1)
        if duplicates:
            errors.append(f"{locale}: duplicate ids {duplicates!r}")
        route_id_sets[locale] = set(parser.ids) & expected_ids
        missing_ids = sorted(expected_ids - set(parser.ids))
        if missing_ids:
            errors.append(f"{locale}: missing source-derived ids {missing_ids!r}")
        telegram = Counter(
            (html.unescape(label), href)
            for label, href in parser.links
            if href.startswith("https://t.me/")
        )
        if telegram != expected_telegram:
            errors.append(f"{locale}: Telegram name/target pairs differ from source")
        fragments = Counter(
            href[1:] for _, href in parser.links if href.startswith("#")
        )
        unresolved = sorted(fragment for fragment in fragments if fragment not in route_id_sets[locale])
        if unresolved:
            errors.append(f"{locale}: unresolved fragments {unresolved!r}")
        summary["routes"][locale] = {
            "lang": parser.html_langs[0] if parser.html_langs else None,
            "title": parser.titles[0] if parser.titles else None,
            "description": descriptions[0] if descriptions else None,
            "canonical": canonicals[0] if canonicals else None,
            "alternates": alternates,
            "open_graph": {
                key: meta_values(parser, "property", key) for key in (*og_expected, "og:locale:alternate")
            },
            "twitter": {
                key: meta_values(parser, "name", key) for key in twitter_expected
            },
            "dataset": dataset,
            "h1": parser.h1_texts,
            "telegram_pair_count": sum(expected_telegram.values()),
            "stable_fragment_count": len(route_id_sets[locale]),
        }
    if route_id_sets and len({frozenset(values) for values in route_id_sets.values()}) != 1:
        errors.append("route destination sets are not locale-parallel")
    summary["sitemap_urls"] = validate_sitemap(site, errors)
    summary["social_preview"] = validate_social_asset(site, errors)
    return errors, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True, help="Built Jekyll site directory")
    parser.add_argument("--summary", type=Path, help="Write the parsed metadata summary as UTF-8 JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors, summary = validate_site(args.site.resolve())
    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print("[SUCCESS] Built EN/RU/KK route structure is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

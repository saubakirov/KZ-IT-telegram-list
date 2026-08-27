#!/usr/bin/env python3
"""Regression coverage for multilingual catalog validation and generation."""

import copy
import re
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

try:
    from .generate_readme import (
        OUTPUT_PATHS,
        PROJECTIONS,
        check_outputs,
        generated_outputs,
        markdown_text,
        presentation_errors,
        render_projection,
        stable_handle_id,
        validate_generated_outputs,
    )
    from .validate_schema import (
        INTENT_IDS,
        build_review_payload,
        load_data,
        localized_value,
        review_payload_keys,
        review_payload_sha256,
        validate_data,
    )
except ImportError:  # Direct script execution.
    from generate_readme import (  # type: ignore
        OUTPUT_PATHS,
        PROJECTIONS,
        check_outputs,
        generated_outputs,
        markdown_text,
        presentation_errors,
        render_projection,
        stable_handle_id,
        validate_generated_outputs,
    )
    from validate_schema import (  # type: ignore
        INTENT_IDS,
        build_review_payload,
        load_data,
        localized_value,
        review_payload_keys,
        review_payload_sha256,
        validate_data,
    )

PROJECT_ROOT = Path(__file__).parent.parent


class CatalogGenerationTests(unittest.TestCase):
    """Verify production and representative failure modes."""

    def setUp(self) -> None:
        self.data = load_data()
        self.outputs = generated_outputs(self.data)

    def validation_errors(self, data: dict) -> list[str]:
        """Return schema errors for a copied fixture."""
        errors, _ = validate_data(data, today=date(2026, 8, 27))
        return errors

    def assert_invalid(self, data: dict, fragment: str) -> None:
        """Assert that a fixture fails with a meaningful error fragment."""
        errors = self.validation_errors(data)
        self.assertTrue(errors, "fixture unexpectedly passed validation")
        self.assertTrue(
            any(fragment in error for error in errors),
            f"expected {fragment!r} in {errors}",
        )

    def test_production_schema_and_review_binding(self) -> None:
        errors, freshness = validate_data(self.data, today=date(2026, 8, 27))
        self.assertEqual([], errors)
        self.assertEqual(0, freshness["stale_count"])
        payload = build_review_payload(self.data)
        self.assertEqual({"en": 139, "ru": 131, "kk": 131}, {key: len(value) for key, value in payload.items()})
        self.assertEqual(401, len(review_payload_keys(self.data)))
        self.assertEqual(
            self.data["localization_review"]["payload_sha256"],
            review_payload_sha256(self.data),
        )

    def test_all_outputs_are_current_and_semantically_valid(self) -> None:
        self.assertEqual([], check_outputs(self.outputs))
        self.assertEqual([], validate_generated_outputs(self.data, self.outputs))
        self.assertEqual(set(OUTPUT_PATHS.values()), set(self.outputs))

    def test_check_mode_is_non_mutating(self) -> None:
        before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in self.outputs}
        result = subprocess.run(
            [sys.executable, str(PROJECT_ROOT / "scripts" / "generate_readme.py"), "--check"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        after = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in self.outputs}
        self.assertEqual(before, after)

    def test_projection_structure_and_exact_target_sets(self) -> None:
        expected_handles = {
            entry["handle"].casefold()
            for section in ("groups", "channels", "bots", "archive")
            for entry in self.data[section]
        }
        for projection in PROJECTIONS:
            with self.subTest(projection=projection.key):
                content = self.outputs[OUTPUT_PATHS[projection.key]]
                self.assertEqual(1, len(re.findall(r"(?m)^#\s+", content)))
                self.assertEqual(expected_handles, set(re.findall(r'<a id="entry-([^"]+)"></a>', content)))
                for section in ("groups", "channels", "bots", "archive"):
                    for entry in self.data[section]:
                        target = f"](https://t.me/{entry['handle']})"
                        self.assertEqual(1, content.count(target), entry["handle"])

    def test_intent_membership_matches_reviewed_snapshot(self) -> None:
        entries = [
            entry
            for section in ("groups", "channels", "bots")
            for entry in self.data[section]
        ]
        counts: dict[str, int] = {}
        union: set[str] = set()
        for intent in INTENT_IDS:
            definition = self.data["intents"][intent]
            selected = {
                entry["handle"].casefold()
                for entry in entries
                if entry.get("category") in definition["categories"]
                or entry["handle"].casefold()
                in {handle.casefold() for handle in definition["exceptional_handles"]}
            }
            counts[intent] = len(selected)
            union.update(selected)
        self.assertEqual(
            {"ai": 3, "startups": 3, "jobs": 6, "events": 1, "engineering": 46},
            counts,
        )
        self.assertEqual(55, len(union))

    def test_special_character_fixture_is_portable(self) -> None:
        raw = r"Pipe | [brackets] *emphasis* _underscore_ `backtick` \\ <angle> & ampersand"
        escaped = markdown_text(raw)
        for token in (r"\|", r"\[", r"\]", r"\*", r"\_", r"\`", r"\\", "&lt;", "&gt;", "&amp;"):
            self.assertIn(token, escaped)

        fixture = copy.deepcopy(self.data)
        fixture["groups"].append(
            {
                "name": raw,
                "handle": "fixture_special",
                "description": raw,
                "description_ru": raw,
                "description_kk": raw,
                "category": "ai",
                "last_verified": "2026-08-27",
                "member_count": 42,
            }
        )
        content = render_projection(fixture, PROJECTIONS[0])
        expected_link = f"[{escaped}](https://t.me/fixture_special)"
        self.assertIn(expected_link, content)
        self.assertIn(f'<a id="{stable_handle_id("fixture_special")}"></a>', content)

    def test_missing_blank_placeholder_and_unknown_locale_fail(self) -> None:
        fixtures: list[tuple[str, dict, str]] = []

        missing = copy.deepcopy(self.data)
        del missing["groups"][0]["description_kk"]
        fixtures.append(("missing", missing, "description_kk"))

        blank = copy.deepcopy(self.data)
        blank["ui"]["ru"]["section.groups"] = "  "
        fixtures.append(("blank", blank, "section.groups"))

        placeholder = copy.deepcopy(self.data)
        placeholder["meta"]["title_kk"] = "TODO translation"
        fixtures.append(("placeholder", placeholder, "placeholder"))

        unknown = copy.deepcopy(self.data)
        unknown["locales"].append("kz")
        fixtures.append(("unknown", unknown, "must be exactly"))

        for name, fixture, fragment in fixtures:
            with self.subTest(name=name):
                self.assert_invalid(fixture, fragment)

        self.assertIsNone(localized_value(missing["groups"][0], "description", "kk"))

    def test_invalid_category_and_intent_references_fail(self) -> None:
        invalid_category = copy.deepcopy(self.data)
        invalid_category["channels"][0]["category"] = "unknown-category"
        self.assert_invalid(invalid_category, "unknown category")

        missing_intent_reference = copy.deepcopy(self.data)
        missing_intent_reference["intents"]["ai"]["exceptional_handles"][0] = "missing_handle"
        self.assert_invalid(missing_intent_reference, "RES-2 baseline")

        redundant_exception = copy.deepcopy(self.data)
        redundant_exception["intents"]["ai"]["exceptional_handles"].append("cursor_kz")
        self.assert_invalid(redundant_exception, "RES-2 baseline")

    def test_stale_digest_and_duplicate_destination_fail(self) -> None:
        stale = copy.deepcopy(self.data)
        stale["ui"]["kk"]["section.groups"] += "!"
        self.assert_invalid(stale, "payload_sha256 is stale")

        duplicate = copy.deepcopy(self.data)
        duplicate["channels"][0]["handle"] = duplicate["groups"][0]["handle"].upper()
        self.assert_invalid(duplicate, "duplicate live handle")

    def test_broken_fragment_lost_anchor_and_duplicate_id_are_detected(self) -> None:
        projection = PROJECTIONS[0]
        content = self.outputs[OUTPUT_PATHS[projection.key]]

        broken = content.replace("](#type-groups)", "](#missing-fragment)", 1)
        self.assertTrue(any("unresolved fragments" in error for error in presentation_errors(broken, self.data, projection)))

        lost = content.replace("](https://t.me/cursor_kz)", "](https://example.invalid/cursor_kz)", 1)
        self.assertTrue(any("cursor_kz" in error for error in presentation_errors(lost, self.data, projection)))

        duplicate = content + '\n<a id="type-groups"></a>\n'
        self.assertTrue(any("duplicate destinations" in error for error in presentation_errors(duplicate, self.data, projection)))

    def test_existing_date_member_archive_and_north_star_rules_remain(self) -> None:
        stale = copy.deepcopy(self.data)
        stale["groups"][0]["last_verified"] = "2026-01-01"
        stale["localization_review"]["payload_sha256"] = review_payload_sha256(stale)
        errors, freshness = validate_data(stale, today=date(2026, 8, 27))
        self.assertEqual([], errors)
        self.assertGreater(freshness["stale_count"], 0)

        invalid_date = copy.deepcopy(self.data)
        invalid_date["groups"][0]["last_verified"] = "2026-02-30"
        self.assert_invalid(invalid_date, "invalid last_verified value")

        invalid_count = copy.deepcopy(self.data)
        invalid_count["groups"][0]["member_count"] = True
        self.assert_invalid(invalid_count, "member_count")

        missing_north_star = copy.deepcopy(self.data)
        missing_north_star["north_star"]["purpose"] = ""
        self.assert_invalid(missing_north_star, "purpose")

        self.assertEqual(2, len(self.data["archive"]))

    def test_canonical_digest_ignores_object_insertion_order(self) -> None:
        reordered = copy.deepcopy(self.data)
        reordered["ui"]["en"] = dict(reversed(list(reordered["ui"]["en"].items())))
        reordered["category_labels"]["ru"] = dict(
            reversed(list(reordered["category_labels"]["ru"].items()))
        )
        self.assertEqual(review_payload_sha256(self.data), review_payload_sha256(reordered))


if __name__ == "__main__":
    unittest.main(verbosity=2)

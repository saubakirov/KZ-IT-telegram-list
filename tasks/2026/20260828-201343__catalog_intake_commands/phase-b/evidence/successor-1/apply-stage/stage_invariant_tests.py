#!/usr/bin/env python3
"""Run Phase A regressions that are invariant under an approved catalog-data successor."""

from __future__ import annotations

import json
import sys
import unittest


MODULES = (
    "scripts.test_catalog_generation",
    "scripts.test_kz_intake",
    "scripts.test_kz_commands",
)
BASELINE_SNAPSHOT_ONLY = {
    "scripts.test_catalog_generation.CatalogGenerationTests.test_intent_membership_matches_reviewed_snapshot",
    "scripts.test_catalog_generation.CatalogGenerationTests.test_phase_a_body_digest_readme_and_test_contract_are_preserved",
    "scripts.test_catalog_generation.CatalogGenerationTests.test_production_schema_and_review_binding",
    "scripts.test_kz_intake.ActionStageBindingTests.test_exact_add_is_bound_and_apply_accepts_only_its_generated_stage",
}


def iter_cases(suite: unittest.TestSuite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from iter_cases(item)
        else:
            yield item


def main() -> int:
    loaded = unittest.defaultTestLoader.loadTestsFromNames(MODULES)
    cases = list(iter_cases(loaded))
    selected = [case for case in cases if case.id() not in BASELINE_SNAPSHOT_ONLY]
    excluded = sorted(case.id() for case in cases if case.id() in BASELINE_SNAPSHOT_ONLY)
    if set(excluded) != BASELINE_SNAPSHOT_ONLY:
        raise SystemExit(f"baseline snapshot test inventory drift: {excluded}")
    print(json.dumps({
        "schema_version": "kz-intake-stage-invariant-suite/v1",
        "loaded": len(cases),
        "selected": len(selected),
        "excluded_baseline_snapshot_only": excluded,
    }, sort_keys=True))
    result = unittest.TextTestRunner(verbosity=1).run(unittest.TestSuite(selected))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

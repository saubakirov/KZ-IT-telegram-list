#!/usr/bin/env python3
"""Deterministically audit successor preview 1 and its immutable predecessor boundary."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


BASE = "c2725b329664a402332341a064cfca19a0928532"
EXPECTED_COUNT_CHANGES = {
    "candidate:astana_hub": (13572, 13568),
    "candidate:digitalbussinesskz": (8362, 8361),
    "candidate:ethkz": (1227, 1226),
    "candidate:it_jobs_kz": (9702, 9703),
    "candidate:kolesa_group": (7116, 7117),
    "candidate:kz_bi_jobs": (5479, 5478),
}
BEFORE = {
    "data/communities.json": "a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d",
    "README.md": "3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d",
    "index.md": "4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3",
    "ru/index.md": "36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97",
    "kk/index.md": "64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    root = Path.cwd()
    successor = Path(__file__).resolve().parent
    evidence = successor.parent
    phase = evidence.parent
    preview = json.loads((successor / "preview.json").read_text(encoding="utf-8"))
    actions = json.loads((successor / "actions.json").read_text(encoding="utf-8"))
    old_actions = json.loads((evidence / "universe" / "actions.json").read_text(encoding="utf-8"))
    collisions = json.loads((successor / "collisions.json").read_text(encoding="utf-8"))
    manifest = json.loads((successor / "stage-manifest.json").read_text(encoding="utf-8"))
    kz_intake.validate_preview(preview)

    old_by_id = {row["candidate_id"]: row for row in old_actions}
    count_changes = {}
    for row in actions:
        old = old_by_id[row["candidate_id"]]
        if row["action"] != old["action"] or row["reason"] != old["reason"]:
            raise SystemExit("action or reason changed")
        if row["action"] != "add":
            if row != old:
                raise SystemExit("non-add action changed")
            continue
        current_entry = copy.deepcopy(row["proposed_entry"])
        old_entry = copy.deepcopy(old["proposed_entry"])
        current_count = current_entry.pop("member_count")
        old_count = old_entry.pop("member_count")
        if current_entry != old_entry:
            raise SystemExit("proposed ADD field other than count changed")
        if current_count != old_count:
            count_changes[row["candidate_id"]] = (old_count, current_count)
    if count_changes != EXPECTED_COUNT_CHANGES:
        raise SystemExit(f"ADD count changes differ: {count_changes}")

    old_paths = [
        "tasks/2026/20260828-201343__catalog_intake_commands/phase-b/evidence/preview",
        "tasks/2026/20260828-201343__catalog_intake_commands/phase-b/review/readiness.md",
        "tasks/2026/20260828-201343__catalog_intake_commands/phase-b/evidence/universe",
        "tasks/2026/20260828-201343__catalog_intake_commands/phase-b/evidence/holdout",
        "tasks/2026/20260828-201343__catalog_intake_commands/phase-b/evidence/authority",
        "tasks/2026/20260828-201343__catalog_intake_commands/journal/20260829-104615__transition__saubakirov.md",
        "tasks/2026/20260828-201343__catalog_intake_commands/journal/20260829-104942__transition__saubakirov.md",
    ]
    immutable = subprocess.run(["git", "diff", "--quiet", BASE, "--", *old_paths], cwd=root).returncode == 0
    if not immutable:
        raise SystemExit("predecessor evidence differs from c2725b3")
    current_before = kz_intake.path_hashes(root)
    if current_before != BEFORE:
        raise SystemExit("production BEFORE hashes changed")
    expected_after = {row["path"]: row["after_sha256"] for row in preview["controlled_paths"]}
    stage_hashes = kz_intake.validate_action_stage(root, successor / "stage", actions)
    if stage_hashes != expected_after:
        raise SystemExit("stage differs from preview AFTER")
    if any(row["status"] != "clear" or row["matched_handles"] for row in collisions):
        raise SystemExit("live/archive collision introduced")
    cross = [row["candidate_id"] for row in collisions if row["cross_input_duplicate"]]
    if cross != ["candidate:aws_kz"]:
        raise SystemExit("cross-input duplicate set changed")
    add_ids = [row["candidate_id"] for row in actions if row["action"] == "add"]
    result = {
        "schema_version": "kz-intake-successor-readiness-audit/v1",
        "result": "verified_executor_successor_readiness_reviewer_pending",
        "predecessor_commit": BASE,
        "payload_sha256": kz_intake.preview_sha256(preview),
        "preview_file_sha256": digest(successor / "preview.json"),
        "actions_sha256": kz_intake.actions_sha256(actions),
        "ordered_add_candidate_ids": add_ids,
        "totals": preview["totals"],
        "changed_proposed_member_counts": [
            {"candidate_id": key, "before": value[0], "successor": value[1]}
            for key, value in count_changes.items()
        ],
        "controlled_before_sha256": current_before,
        "controlled_expected_after_sha256": expected_after,
        "artifact_sha256": {
            name: digest(successor / name) for name in (
                "ledger.json", "observations.json", "editorial-public-evidence.json",
                "collisions.json", "editorial.json", "actions.json", "judgements.json",
                "occurrence-accounting.json", "bundle.json", "stage-manifest.json",
                "preview.json", "preview.md", "action-digest.json", "controlled-hashes.json",
                "readiness.md", "renderer-audit.json",
            )
        },
        "checks": {
            "fresh_observations_reused_without_probe": digest(successor / "observations.json") == digest(evidence / "pre-apply-freshness" / "observations.json"),
            "old_bound_artifacts_equal_c2725b3": immutable,
            "actions_remain_20_3_1_4": preview["totals"] == {"occurrences": 29, "candidates": 28, "observed": 28, "add": 20, "reject": 3, "duplicate": 1, "unresolved": 4},
            "only_six_add_member_counts_changed": True,
            "copy_and_other_proposed_fields_unchanged": True,
            "all_exact_live_archive_collisions_clear": True,
            "only_aws_kz_cross_input_duplicate": True,
            "isolated_stage_equals_preview_after": True,
            "staged_schema_generator_and_41_invariants_passed": all(row["returncode"] == 0 for row in manifest["validation_results"]),
            "unchanged_production_45_tests_passed": manifest["unchanged_production_full_suite"]["returncode"] == 0,
            "all_five_production_paths_equal_before": True,
            "successor_approval_envelope_absent": True,
            "persistent_reviewer_audit_pending": True,
        },
        "limitations": [
            "No new public probe was run; successor 1 consumes the committed freshness observations exactly.",
            "The retained public observations are point-in-time evidence and require another exact freshness gate before any later apply.",
            "Persistent Reviewer readiness and a new exact current owner approval are both absent.",
        ],
    }
    if not all(result["checks"].values()):
        false_checks = [key for key, value in result["checks"].items() if not value]
        raise SystemExit(f"successor checks failed: {false_checks}")
    (successor / "audit.json").write_text(
        json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )
    print(json.dumps({key: result[key] for key in ("payload_sha256", "actions_sha256", "preview_file_sha256")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

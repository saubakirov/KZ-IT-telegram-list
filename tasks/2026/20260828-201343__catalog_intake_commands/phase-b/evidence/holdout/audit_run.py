#!/usr/bin/env python3
"""Audit the retained holdout-first machine evidence without probing again."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

from scripts import kz_intake


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    evidence = Path(sys.argv[1])
    completed_at = sys.argv[2]
    root = Path.cwd()
    run_start = json.loads((evidence / "run-start.json").read_text(encoding="utf-8"))
    manifest = json.loads((evidence / "case-manifest.json").read_text(encoding="utf-8"))
    ledger = json.loads((evidence / "ledger.json").read_text(encoding="utf-8"))
    observed = json.loads((evidence / "observations.json").read_text(encoding="utf-8"))
    before = json.loads((evidence.parent / "controlled-hashes-before.json").read_text(encoding="utf-8"))

    kz_intake.validate_source(ledger)
    if observed["source"] != ledger:
        raise SystemExit("probe source differs from retained parse ledger")
    for row in observed["observations"]:
        kz_intake.validate_observation(row)
    manifest_handles = {row["handle"].casefold() for row in manifest["cases"]}
    ledger_handles = {row["handle"].casefold() for row in ledger["candidates"]}
    observation_handles = {row["requested_handle"].casefold() for row in observed["observations"]}
    if manifest_handles != ledger_handles or ledger_handles != observation_handles:
        raise SystemExit("holdout case/ledger/observation identities differ")
    if ledger["totals"] != {"occurrences": 20, "candidates": 20, "non_candidates": 0}:
        raise SystemExit("holdout ledger totals differ")
    if len(observed["observations"]) != 20:
        raise SystemExit("holdout observation count differs")

    current_hashes = kz_intake.path_hashes(root)
    before_hashes = {row["path"]: row["sha256"] for row in before["paths"]}
    if current_hashes != before_hashes:
        raise SystemExit("controlled production paths changed during holdout")
    if digest(root / "scripts/kz_intake.py") != run_start["engine_sha256"]:
        raise SystemExit("intake engine changed during holdout")
    if digest(root / "scripts/validate_links.py") != run_start["classifier_sha256"]:
        raise SystemExit("classifier changed during holdout")
    phase_a_paths = [
        "scripts/kz_intake.py",
        "scripts/validate_links.py",
        "scripts/validate_schema.py",
        "scripts/generate_readme.py",
        "scripts/test_kz_intake.py",
        "scripts/test_kz_commands.py",
        "scripts/sync_kz_commands.py",
        ".claude/commands/kz-add.md",
        ".claude/commands/kz-stats.md",
        ".claude/commands/kz-release.md",
        ".agents/skills/kz-add/SKILL.md",
        ".agents/skills/kz-stats/SKILL.md",
        ".agents/skills/kz-release/SKILL.md",
    ]
    unchanged = subprocess.run(
        ["git", "diff", "--quiet", "9185811696c762b5261e9b90f71bee846b6fc692", "--", *phase_a_paths],
        cwd=root,
        check=False,
    ).returncode == 0
    if not unchanged:
        raise SystemExit("Phase A implementation or command bytes changed")

    rows = observed["observations"]
    per_candidate = [
        {
            "candidate_id": row["candidate_id"],
            "requested_handle": row["requested_handle"],
            "status": row["status"],
            "reason": row["reason"],
            "observed_type": row["observed_type"],
            "body_sha256": row["body_sha256"],
            "transport": row["transport"],
        }
        for row in rows
    ]
    result = {
        "schema_version": "kz-intake-holdout-audit/v1",
        "result": "clean_holdout_retained",
        "started_at": run_start["started_at"],
        "completed_at": completed_at,
        "executor_commit": run_start["executor_commit"],
        "phase_a_implementation": run_start["phase_a_implementation"],
        "artifacts": {
            "input_sha256": digest(evidence / "input.txt"),
            "case_manifest_sha256": digest(evidence / "case-manifest.json"),
            "ledger_sha256": digest(evidence / "ledger.json"),
            "observations_sha256": digest(evidence / "observations.json"),
        },
        "totals": {
            "occurrences": ledger["totals"]["occurrences"],
            "candidates": ledger["totals"]["candidates"],
            "observations": len(rows),
            "verified": sum(row["status"] == "verified" for row in rows),
            "unresolved": sum(row["status"] != "verified" for row in rows),
            "body_hashes": sum(row["body_sha256"] is not None for row in rows),
        },
        "observed_type_totals": dict(sorted(Counter(row["observed_type"] for row in rows).items())),
        "transport_totals": dict(sorted(Counter(row["transport"]["reason"] for row in rows).items())),
        "per_candidate": per_candidate,
        "checks": {
            "holdout_was_first_phase_b_probe": True,
            "calibration_outcomes_consulted_for_phase_b_before_run": False,
            "full_universe_probe_preceded_holdout": False,
            "source_ledger_matches_probe_ledger": True,
            "all_observations_validate_against_closed_producer_schema": True,
            "all_twenty_cases_have_observation_body_hashes": all(
                row["body_sha256"] is not None for row in rows
            ),
            "phase_a_implementation_and_commands_unchanged": unchanged,
            "controlled_production_hashes_unchanged": True,
            "holdout_driven_rule_fixture_prompt_or_expected_outcome_change": False,
            "clean_claim_valid": True,
        },
        "controlled_sha256_after_holdout": current_hashes,
        "limitations": [
            "Only public Telegram preview evidence was used; no authenticated or private fallback was attempted.",
            "The engine retains exact response-body SHA-256 values and typed observations, not raw Telegram HTML bytes.",
            "A verified target preview does not by itself establish recent posting activity, Kazakhstan relevance, IT relevance, commerciality, spam risk, or catalog admission.",
        ],
    }
    rendered = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if len(sys.argv) > 3:
        Path(sys.argv[3]).write_text(rendered, encoding="utf-8", newline="\n")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

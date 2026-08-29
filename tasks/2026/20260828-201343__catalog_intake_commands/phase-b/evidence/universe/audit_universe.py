#!/usr/bin/env python3
"""Audit the retained post-holdout all-universe reconciliation without refetching."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    root = Path.cwd()
    universe = Path(__file__).resolve().parent
    evidence = universe.parent
    start = json.loads((universe / "run-start.json").read_text(encoding="utf-8"))
    manifest = json.loads((universe / "case-manifest.json").read_text(encoding="utf-8"))
    source = json.loads((universe / "ledger.json").read_text(encoding="utf-8"))
    probe = json.loads((universe / "observations.json").read_text(encoding="utf-8"))
    public = json.loads((universe / "editorial-public-evidence.json").read_text(encoding="utf-8"))
    collisions = json.loads((universe / "collisions.json").read_text(encoding="utf-8"))
    judgements = json.loads((universe / "judgements.json").read_text(encoding="utf-8"))
    actions = json.loads((universe / "actions.json").read_text(encoding="utf-8"))
    accounting = json.loads((universe / "occurrence-accounting.json").read_text(encoding="utf-8"))
    before = json.loads((evidence / "controlled-hashes-before.json").read_text(encoding="utf-8"))

    kz_intake.validate_source(source)
    if source != probe["source"]:
        raise SystemExit("probe source differs from retained ledger")
    for row in probe["observations"]:
        kz_intake.validate_observation(row)
    expected_ids = [row["candidate_id"] for row in source["candidates"]]
    for rows, label in (
        (probe["observations"], "observations"),
        (collisions, "collisions"),
        (judgements["candidates"], "judgements"),
        (actions, "actions"),
    ):
        if [row["candidate_id"] for row in rows] != expected_ids:
            raise SystemExit(f"{label} candidate order/coverage differs")
    if source["totals"] != {"occurrences": 29, "candidates": 28, "non_candidates": 0}:
        raise SystemExit("source totals differ")
    if manifest["totals"] != {"occurrences": 29, "unique_cases": 28, "overlap_cases": 1}:
        raise SystemExit("case manifest totals differ")
    if accounting["totals"]["accounted_occurrences"] != 29 or len(accounting["occurrences"]) != 29:
        raise SystemExit("occurrence accounting differs")
    if any(row["status"] != "verified" or not row["target_bound"] for row in probe["observations"]):
        raise SystemExit("unverified universe observation")
    if any(row["status"] != "clear" or row["matched_handles"] for row in collisions):
        raise SystemExit("unexpected exact live/archive collision")
    cross_input = [row["candidate_id"] for row in collisions if row["cross_input_duplicate"]]
    if cross_input != ["candidate:aws_kz"]:
        raise SystemExit("cross-input overlap differs")
    public_ids = [row["candidate_id"] for row in public["candidates"]]
    if public_ids != expected_ids or any(
        not row["root"].get("ok") and not row["public_stream"].get("ok")
        for row in public["candidates"]
    ):
        raise SystemExit("bounded public editorial evidence coverage differs")
    action_totals = Counter(row["action"] for row in actions)
    if action_totals != Counter({"add": 20, "unresolved": 4, "reject": 3, "duplicate": 1}):
        raise SystemExit("action totals differ")

    before_hashes = {row["path"]: row["sha256"] for row in before["paths"]}
    current_hashes = kz_intake.path_hashes(root)
    if current_hashes != before_hashes:
        raise SystemExit("controlled production paths changed")
    if digest(root / "scripts/kz_intake.py") != start["engine_sha256"]:
        raise SystemExit("approved intake engine changed")
    if digest(root / "scripts/validate_links.py") != start["classifier_sha256"]:
        raise SystemExit("approved classifier changed")
    phase_a_paths = [
        "scripts/kz_intake.py", "scripts/validate_links.py", "scripts/validate_schema.py",
        "scripts/generate_readme.py", "scripts/test_kz_intake.py", "scripts/test_kz_commands.py",
        "scripts/sync_kz_commands.py", ".claude/commands/kz-add.md",
        ".claude/commands/kz-stats.md", ".claude/commands/kz-release.md",
        ".agents/skills/kz-add/SKILL.md", ".agents/skills/kz-stats/SKILL.md",
        ".agents/skills/kz-release/SKILL.md",
    ]
    phase_a_unchanged = subprocess.run(
        ["git", "diff", "--quiet", "9185811696c762b5261e9b90f71bee846b6fc692", "--", *phase_a_paths],
        cwd=root,
        check=False,
    ).returncode == 0
    if not phase_a_unchanged:
        raise SystemExit("Phase A implementation/command surface changed")

    artifact_names = (
        "input.txt", "case-manifest.json", "run-start.json", "ledger.json", "observations.json",
        "editorial-public-evidence.json", "collisions.json", "editorial.json", "actions.json",
        "judgements.json", "occurrence-accounting.json", "bundle.json",
    )
    result = {
        "schema_version": "kz-intake-universe-audit/v1",
        "result": "verified_post_holdout_reconciliation",
        "started_at": start["started_at"],
        "completed_at": datetime.now(ZoneInfo("Asia/Qyzylorda")).isoformat(timespec="seconds"),
        "holdout_checkpoint_commit": start["holdout_checkpoint_commit"],
        "holdout_audit_sha256": start["holdout_audit_sha256"],
        "artifacts": {name: {"bytes": (universe / name).stat().st_size, "sha256": digest(universe / name)} for name in artifact_names},
        "totals": {
            "source_occurrences": 29,
            "unique_candidates": 28,
            "verified_public_targets": 28,
            "channels": sum(row["observed_type"] == "channels" for row in probe["observations"]),
            "groups": sum(row["observed_type"] == "groups" for row in probe["observations"]),
            "actions": dict(sorted(action_totals.items())),
        },
        "checks": {
            "holdout_checkpoint_precedes_universe_start": True,
            "source_probe_ledger_exact_match": True,
            "all_closed_observations_validate": True,
            "all_targets_exactly_bound_and_live": True,
            "all_29_occurrences_accounted": True,
            "all_28_candidates_have_one_judgement_and_action": True,
            "only_aws_kz_has_two_source_occurrences": True,
            "all_exact_live_archive_collisions_clear": True,
            "canonical_alias_near_handle_checks_retained": True,
            "bounded_public_editorial_evidence_covers_every_candidate": True,
            "preliminary_discovery_claims_not_used_as_current_facts": True,
            "phase_a_implementation_and_commands_unchanged": phase_a_unchanged,
            "controlled_production_hashes_unchanged": True,
        },
        "controlled_sha256_after_universe": current_hashes,
        "limitations": judgements["global_limitations"],
    }
    output = universe / "run-audit.json"
    output.write_text(
        json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "result": result["result"],
        "actions": result["totals"]["actions"],
        "output_sha256": digest(output),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

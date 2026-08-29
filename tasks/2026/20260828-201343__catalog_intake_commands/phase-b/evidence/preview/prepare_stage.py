#!/usr/bin/env python3
"""Build and verify an isolated exact expected-action stage without touching production."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], cwd: Path) -> dict[str, object]:
    completed = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    result = {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }
    if completed.returncode:
        raise SystemExit(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def run_expected_snapshot_failures(command: list[str], cwd: Path) -> dict[str, object]:
    completed = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    result = {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "classification": "baseline_snapshot_expectations_only",
    }
    expected_names = (
        "test_intent_membership_matches_reviewed_snapshot",
        "test_phase_a_body_digest_readme_and_test_contract_are_preserved",
        "test_production_schema_and_review_binding",
        "test_exact_add_is_bound_and_apply_accepts_only_its_generated_stage",
    )
    combined = completed.stdout + completed.stderr
    if completed.returncode != 1 or "FAILED (failures=4)" not in combined or "ERROR:" in combined:
        raise SystemExit("staged full-suite result was not the four expected snapshot-only failures")
    if any(name not in combined for name in expected_names):
        raise SystemExit("staged full-suite failure inventory differs")
    return result


def write_expected(stage_root: Path, expected: dict[str, bytes]) -> None:
    for relative, body in expected.items():
        target = stage_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)


def copy_validation_surface(root: Path, stage_root: Path) -> dict[str, str]:
    copied: dict[str, str] = {}
    for source in sorted((root / "scripts").glob("*.py")):
        relative = source.relative_to(root)
        target = stage_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        copied[relative.as_posix()] = digest(source)
    command_paths = [
        Path(".claude/commands/kz-add.md"),
        Path(".claude/commands/kz-stats.md"),
        Path(".claude/commands/kz-release.md"),
        Path(".agents/skills/kz-add/SKILL.md"),
        Path(".agents/skills/kz-stats/SKILL.md"),
        Path(".agents/skills/kz-release/SKILL.md"),
    ]
    for relative in command_paths:
        source = root / relative
        target = stage_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        copied[relative.as_posix()] = digest(source)
    return copied


def main() -> int:
    root = Path.cwd().resolve()
    preview_dir = Path(__file__).resolve().parent
    phase_b = preview_dir.parent.parent
    universe = phase_b / "evidence" / "universe"
    actions = json.loads((universe / "actions.json").read_text(encoding="utf-8"))
    expected = kz_intake.expected_action_stage(root, actions)
    retained_stage = preview_dir / "stage"
    write_expected(retained_stage, expected)
    expected_hashes = kz_intake.validate_action_stage(root, retained_stage, actions)

    temp_base = Path(tempfile.gettempdir()).resolve()
    temp_stage = Path(tempfile.mkdtemp(prefix="kz-intake-phase-b-stage-")).resolve()
    if temp_stage.parent != temp_base or not temp_stage.name.startswith("kz-intake-phase-b-stage-"):
        raise SystemExit("unsafe temporary stage path")
    cleaned = False
    try:
        write_expected(temp_stage, expected)
        copied = copy_validation_surface(root, temp_stage)
        runner_source = preview_dir / "stage_invariant_tests.py"
        runner_target = temp_stage / "stage_invariant_tests.py"
        shutil.copyfile(runner_source, runner_target)
        copied["stage_invariant_tests.py"] = digest(runner_source)
        full_suite_command = [
            sys.executable, "-m", "unittest", "scripts.test_catalog_generation",
            "scripts.test_kz_intake", "scripts.test_kz_commands", "-q",
        ]
        snapshot_probe = run_expected_snapshot_failures(full_suite_command, temp_stage)
        validation_commands = [
            [sys.executable, "scripts/validate_schema.py"],
            [sys.executable, "scripts/generate_readme.py", "--check"],
            [sys.executable, "stage_invariant_tests.py"],
            [sys.executable, "scripts/sync_kz_commands.py", "--check"],
            [sys.executable, "-m", "py_compile", "scripts/kz_intake.py", "scripts/validate_links.py", "scripts/validate_schema.py", "scripts/generate_readme.py"],
        ]
        results = [run(command, temp_stage) for command in validation_commands]
        validator_contract = kz_intake.validate_staged_project(temp_stage)
        if kz_intake.path_hashes(temp_stage) != expected_hashes:
            raise SystemExit("temporary and retained stage hashes differ")
    finally:
        shutil.rmtree(temp_stage)
        cleaned = not temp_stage.exists()
    production_full_suite = run(full_suite_command, root)

    manifest = {
        "schema_version": "kz-intake-isolated-stage/v1",
        "prepared_at": datetime.now(ZoneInfo("Asia/Qyzylorda")).isoformat(timespec="seconds"),
        "production_root_mutated": False,
        "actions_sha256": kz_intake.actions_sha256(actions),
        "retained_stage": "phase-b/evidence/preview/stage",
        "temporary_validation_stage": {
            "isolated_outside_repository": True,
            "removed_after_validation": cleaned,
            "path_redacted": True,
        },
        "controlled_paths": [
            {
                "path": relative,
                "bytes": len(expected[relative]),
                "sha256": expected_hashes[relative],
            }
            for relative in kz_intake.CONTROLLED_PATHS
        ],
        "validation_surface_sha256": copied,
        "validation_contract_commands": validator_contract,
        "full_suite_stage_snapshot_probe": snapshot_probe,
        "unchanged_production_full_suite": production_full_suite,
        "validation_results": results,
        "checks": {
            "retained_bytes_equal_expected_action_stage": True,
            "temporary_bytes_equal_retained_stage": True,
            "schema_validation_passed": True,
            "generator_currency_passed": True,
            "catalog_intake_command_regressions_passed": True,
            "four_baseline_snapshot_only_tests_classified_not_modified": True,
            "command_adapter_sync_passed": True,
            "python_compile_passed": True,
            "production_controlled_paths_written": False,
        },
    }
    manifest_path = preview_dir / "stage-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "actions_sha256": manifest["actions_sha256"],
        "expected_hashes": expected_hashes,
        "manifest_sha256": digest(manifest_path),
        "temporary_stage_cleaned": cleaned,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

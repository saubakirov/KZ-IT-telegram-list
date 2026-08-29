#!/usr/bin/env python3
"""Materialize the reviewed controlled stage plus its recorded validation surface."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    root = Path.cwd()
    successor = Path(__file__).resolve().parent
    retained = successor / "stage"
    target = successor / "apply-stage"
    target.mkdir(parents=True, exist_ok=True)
    for relative in kz_intake.CONTROLLED_PATHS:
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(retained / relative, destination)
    manifest = json.loads((successor / "stage-manifest.json").read_text(encoding="utf-8"))
    for relative, expected_sha in manifest["validation_surface_sha256"].items():
        source = successor / "stage_invariant_tests.py" if relative == "stage_invariant_tests.py" else root / relative
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        if digest(destination) != expected_sha:
            raise SystemExit(f"validation surface differs: {relative}")
    if kz_intake.path_hashes(target) != {
        row["path"]: row["after_sha256"]
        for row in json.loads((successor / "preview.json").read_text(encoding="utf-8"))["controlled_paths"]
    }:
        raise SystemExit("apply-stage controlled bytes differ")
    results = []
    for command in ([sys.executable, "scripts/validate_schema.py"],
                    [sys.executable, "scripts/generate_readme.py", "--check"],
                    [sys.executable, "scripts/sync_kz_commands.py", "--check"]):
        completed = subprocess.run(command, cwd=target, text=True, capture_output=True)
        results.append({"command": command, "returncode": completed.returncode,
                        "stdout": completed.stdout, "stderr": completed.stderr})
        if completed.returncode:
            raise SystemExit(completed.stdout + completed.stderr)
    record = {
        "schema_version": "kz-intake-apply-stage/v1",
        "result": "exact_reviewed_controlled_bytes_with_recorded_validation_surface",
        "controlled_sha256": kz_intake.path_hashes(target),
        "validation_surface_sha256": manifest["validation_surface_sha256"],
        "validations": results,
    }
    (successor / "apply-stage-manifest.json").write_text(
        json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )
    print(json.dumps({"controlled_sha256": record["controlled_sha256"], "result": record["result"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

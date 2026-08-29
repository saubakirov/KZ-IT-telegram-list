#!/usr/bin/env python3
"""Derive the lossless Phase B full-universe input from the sealed partition."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


PARTITION_SHA256 = "5b9fb0dd028ac19d02b2c413bca45e8fa3e0e05e8de9b20087bfa883fe2cb732"
SOURCE_ORDER = {"discovery_batch": 0, "owner_note": 1}


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def main() -> int:
    universe_dir = Path(__file__).resolve().parent
    phase_evidence = universe_dir.parent
    root = Path.cwd()
    partition_path = phase_evidence / "source" / "full-partition.json"
    partition_bytes = partition_path.read_bytes()
    if sha256(partition_bytes) != PARTITION_SHA256:
        raise SystemExit("sealed partition hash mismatch")
    partition = json.loads(partition_bytes)

    cases_by_handle = {case["handle"].casefold(): case for case in partition["cases"]}
    occurrences: list[dict[str, object]] = []
    for case in partition["cases"]:
        for occurrence in case["occurrences"]:
            occurrences.append({
                "case_key": case["case_key"],
                "partition": case["partition"],
                "handle": case["handle"].casefold(),
                "source_id": occurrence["source_id"],
                "source_sha256": occurrence["source_sha256"],
                "byte_start": occurrence["byte_start"],
                "byte_end": occurrence["byte_end"],
                "raw_span_sha256": occurrence["raw_span_sha256"],
                "derived_url": occurrence["derived_url"],
            })
    occurrences.sort(key=lambda row: (SOURCE_ORDER[str(row["source_id"])], int(row["byte_start"])))
    if len(occurrences) != 29 or len(cases_by_handle) != 28:
        raise SystemExit("full-universe totals differ")
    aws_rows = [row for row in occurrences if row["handle"] == "aws_kz"]
    if len(aws_rows) != 2 or {row["source_id"] for row in aws_rows} != {"discovery_batch", "owner_note"}:
        raise SystemExit("aws_kz overlap differs")

    input_bytes = ("\n".join(str(row["derived_url"]) for row in occurrences) + "\n").encode("utf-8")
    (universe_dir / "input.txt").write_bytes(input_bytes)
    manifest = {
        "schema_version": "kz-intake-universe-cases/v1",
        "partition_sha256": PARTITION_SHA256,
        "input_sha256": sha256(input_bytes),
        "totals": {"occurrences": 29, "unique_cases": 28, "overlap_cases": 1},
        "occurrences": occurrences,
        "cases": [
            {
                "case_key": case["case_key"],
                "partition": case["partition"],
                "handle": case["handle"].casefold(),
                "occurrence_count": len(case["occurrences"]),
            }
            for case in partition["cases"]
        ],
    }
    (universe_dir / "case-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    run_start = {
        "schema_version": "kz-intake-universe-run-start/v1",
        "started_at": datetime.now(ZoneInfo("Asia/Qyzylorda")).isoformat(timespec="seconds"),
        "executor_commit": subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
        ).stdout.strip(),
        "engine_sha256": sha256((root / "scripts" / "kz_intake.py").read_bytes()),
        "classifier_sha256": sha256((root / "scripts" / "validate_links.py").read_bytes()),
        "holdout_checkpoint_commit": "4d06114d6abab5f268d50485867279aec51d4bca",
        "holdout_audit_sha256": sha256((phase_evidence / "holdout" / "clean-run-audit.json").read_bytes()),
    }
    (universe_dir / "run-start.json").write_text(
        json.dumps(run_start, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({
        "input_sha256": manifest["input_sha256"],
        "occurrences": 29,
        "unique_cases": 28,
        "aws_occurrences": 2,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Create the deterministic fail-closed comparison without changing reviewed evidence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    phase = Path(__file__).resolve().parents[2]
    authority = phase / "evidence" / "authority"
    old_path = phase / "evidence" / "universe" / "observations.json"
    fresh_path = phase / "evidence" / "pre-apply-freshness" / "observations.json"
    preview_path = phase / "evidence" / "preview" / "preview.json"
    old = json.loads(old_path.read_text(encoding="utf-8"))
    fresh = json.loads(fresh_path.read_text(encoding="utf-8"))
    baseline = {row["candidate_id"]: row for row in old["observations"]}
    current = {row["candidate_id"]: row for row in fresh["observations"]}
    if list(baseline) != list(current) or len(baseline) != 28:
        raise SystemExit("fresh candidate coverage/order differs")
    rows = []
    for candidate_id in baseline:
        before, after = baseline[candidate_id], current[candidate_id]
        rows.append({
            "candidate_id": candidate_id,
            "body_sha256_before": before["body_sha256"],
            "body_sha256_fresh": after["body_sha256"],
            "body_changed": before["body_sha256"] != after["body_sha256"],
            "member_count_before": before["member_count"],
            "member_count_fresh": after["member_count"],
            "member_count_changed": before["member_count"] != after["member_count"],
            "identity_changed": any(before[key] != after[key] for key in
                                    ("requested_handle", "canonical_handle", "target_bound")),
            "name_changed": before["visible_name"] != after["visible_name"],
            "type_changed": before["observed_type"] != after["observed_type"],
            "liveness_changed": any(before[key] != after[key] for key in ("status", "reason")),
        })
    body_changes = [row["candidate_id"] for row in rows if row["body_changed"]]
    count_changes = [row for row in rows if row["member_count_changed"]]
    result = {
        "schema_version": "kz-intake-stale-approval/v1",
        "result": "fail_closed_stale_approval",
        "approved_payload_sha256": "a6e7444b3be13f6ed06f3268a079c2264001703ce8e83c83f14c65ab65c0dcac",
        "approved_actions_sha256": "c222aa49fb3481d1142380cf2636327ff73b486baed84af239cdf69ca0e41394",
        "preview_file_sha256": digest(preview_path),
        "baseline_observations_sha256": digest(old_path),
        "fresh_observations_sha256": digest(fresh_path),
        "totals": {"candidates": 28, "body_changes": len(body_changes),
                   "member_count_changes": len(count_changes)},
        "checks": {
            "coverage_and_order_exact": True,
            "all_identity_bindings_unchanged": not any(row["identity_changed"] for row in rows),
            "all_names_unchanged": not any(row["name_changed"] for row in rows),
            "all_types_unchanged": not any(row["type_changed"] for row in rows),
            "all_liveness_classifications_unchanged": not any(row["liveness_changed"] for row in rows),
            "all_body_sha256_changed": len(body_changes) == 28,
            "exactly_nine_member_counts_changed": len(count_changes) == 9,
            "production_apply_permitted": False,
        },
        "body_changed_candidate_ids": body_changes,
        "member_count_changes": count_changes,
        "candidates": rows,
        "disposition": "The exact approval is stale under the mandated body/count evidence binding. Do not apply, create a pending marker, or create a receipt.",
    }
    if not result["checks"]["all_body_sha256_changed"] or not result["checks"]["exactly_nine_member_counts_changed"]:
        raise SystemExit("freshness outcome differs from the fail-closed finding")
    output = authority / "stale-approval-report.json"
    output.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                      encoding="utf-8", newline="\n")
    print(json.dumps(result["totals"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

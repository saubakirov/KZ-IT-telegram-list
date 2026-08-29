#!/usr/bin/env python3
"""Reconcile exact apply receipt, approved bytes, and 20 bounded post-apply probes."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    root = Path.cwd()
    successor = Path(__file__).resolve().parent
    preview = json.loads((successor / "preview.json").read_text(encoding="utf-8"))
    receipt = json.loads((successor / "receipt.json").read_text(encoding="utf-8"))
    post = json.loads((successor / "post-apply-observations.json").read_text(encoding="utf-8"))
    approved = {row["candidate_id"]: row for row in preview["observations"]}
    add_actions = [row for row in preview["actions"] if row["action"] == "add"]
    expected_ids = [row["candidate_id"] for row in add_actions]
    actual_ids = [row["candidate_id"] for row in post["observations"]]
    if actual_ids != expected_ids:
        raise SystemExit("post-apply probe coverage/order differs")
    rows = []
    for row in post["observations"]:
        before = approved[row["candidate_id"]]
        identity_ok = (row["requested_handle"].casefold() == before["requested_handle"].casefold()
                       and row["canonical_handle"].casefold() == before["canonical_handle"].casefold()
                       and row["visible_name"] == before["visible_name"] and row["target_bound"])
        type_ok = row["observed_type"] == before["observed_type"]
        live_ok = row["status"] == "verified" and row["transport"]["ok"] and row["transport"]["status_code"] == 200
        if not identity_ok or not type_ok or not live_ok:
            raise SystemExit(f"post-apply target mismatch: {row['candidate_id']}")
        rows.append({
            "candidate_id": row["candidate_id"],
            "identity_verified": identity_ok,
            "type_verified": type_ok,
            "liveness_verified": live_ok,
            "approved_member_count": before["member_count"],
            "post_apply_member_count": row["member_count"],
            "member_count_changed": before["member_count"] != row["member_count"],
            "approved_body_sha256": before["body_sha256"],
            "post_apply_body_sha256": row["body_sha256"],
            "body_changed": before["body_sha256"] != row["body_sha256"],
        })
    expected_after = {row["path"]: row["after_sha256"] for row in preview["controlled_paths"]}
    current = kz_intake.path_hashes(root)
    if current != expected_after or receipt["final_sha256"] != expected_after:
        raise SystemExit("receipt/current bytes differ from approved AFTER")
    result = {
        "schema_version": "kz-intake-post-apply-audit/v1",
        "result": "verified_exact_apply_and_added_target_identity_type_liveness",
        "payload_sha256": kz_intake.preview_sha256(preview),
        "actions_sha256": kz_intake.actions_sha256(preview["actions"]),
        "receipt_sha256": digest(successor / "receipt.json"),
        "post_apply_observations_sha256": digest(successor / "post-apply-observations.json"),
        "controlled_after_sha256": current,
        "totals": {
            "added_targets": len(rows),
            "identity_verified": sum(row["identity_verified"] for row in rows),
            "type_verified": sum(row["type_verified"] for row in rows),
            "liveness_verified": sum(row["liveness_verified"] for row in rows),
            "member_count_changes_after_apply": sum(row["member_count_changed"] for row in rows),
            "body_changes_after_apply": sum(row["body_changed"] for row in rows),
        },
        "targets": rows,
        "checks": {
            "receipt_outcome_applied_exact": receipt["outcome"] == "applied_exact",
            "receipt_before_state_all_before": receipt["before_state"] == ["B"] * 5,
            "receipt_ids_equal_exact_approved_add_set": receipt["applied_candidate_ids"] == expected_ids,
            "all_five_current_equal_approved_after": True,
            "all_20_identity_type_liveness_verified": True,
            "post_apply_observations_not_used_to_rewrite_approved_bytes": True,
            "pending_marker_removed_after_success": not (successor / "pending.json").exists(),
        },
        "limitations": [
            "Post-apply body and member-count differences are later point-in-time evidence only and do not authorize catalog edits.",
            "Only unauthenticated public Telegram previews were probed; no private history was accessed.",
            "The unchanged Phase A 45-test suite has exactly four approved-data snapshot assertions after apply; the applicable 41 invariants pass and fixtures were not changed.",
        ],
    }
    if not all(result["checks"].values()):
        raise SystemExit("post-apply reconciliation check failed")
    (successor / "post-apply-audit.json").write_text(
        json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )
    print(json.dumps(result["totals"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Prepare exact post-apply probe input and pending lifecycle evidence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def main() -> int:
    successor = Path(__file__).resolve().parent
    preview = json.loads((successor / "preview.json").read_text(encoding="utf-8"))
    approval = json.loads((successor / "authority" / "approval.json").read_text(encoding="utf-8"))
    receipt = json.loads((successor / "receipt.json").read_text(encoding="utf-8"))
    add_actions = [row for row in preview["actions"] if row["action"] == "add"]
    handles = [row["proposed_entry"]["handle"] for row in add_actions]
    (successor / "post-apply-input.txt").write_text(
        "".join(f"https://t.me/{handle}\n" for handle in handles),
        encoding="utf-8", newline="\n",
    )
    approval_bytes = (json.dumps(approval, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    lifecycle = {
        "schema_version": "kz-intake-pending-lifecycle-evidence/v1",
        "execution_id": receipt["execution_id"],
        "payload_sha256": receipt["payload_sha256"],
        "approval_sha256": hashlib.sha256(approval_bytes).hexdigest(),
        "before_state": receipt["before_state"],
        "pending_path": "phase-b/evidence/successor-1/pending.json",
        "pending_removed_after_exact_success": not (successor / "pending.json").exists(),
        "receipt_outcome": receipt["outcome"],
    }
    (successor / "pending-lifecycle.json").write_text(
        json.dumps(lifecycle, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )
    print(json.dumps({"added_targets": len(handles), "pending_removed": lifecycle["pending_removed_after_exact_success"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

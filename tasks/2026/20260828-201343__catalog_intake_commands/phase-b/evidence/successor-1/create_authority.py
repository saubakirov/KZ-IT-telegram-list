#!/usr/bin/env python3
"""Materialize the exact successor owner chain and closed approval envelope."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


OWNER_REF = "codex-thread:01a04247-11fc-7fd1-b3e6-7277403d11d1/assistant-turn:01a04c2c-0aeb-72f0-994f-e03736548f50/assistant-message:msg_03f2f59749ac47b6016a9279e4d3a887d084558cb9b84b3690/owner-turn:01a04c48-40be-7ca2-9dbd-6917b158f601/owner-message:msg_01a04c48-4162-72f2-8e28-a9747a5efb0c"
STATEMENT_SHA256 = "585999ac7c31a05557a7f5bd2ce98809c37e05fcf011a7131e001082d7f553b4"


def main() -> int:
    successor = Path(__file__).resolve().parent
    authority = successor / "authority"
    authority.mkdir(parents=True, exist_ok=True)
    digest_record = json.loads((successor / "action-digest.json").read_text(encoding="utf-8"))
    preview = json.loads((successor / "preview.json").read_text(encoding="utf-8"))
    statement = digest_record["exact_owner_statement_template"]
    if hashlib.sha256(statement.encode("utf-8")).hexdigest() != STATEMENT_SHA256:
        raise SystemExit("committed exact statement bytes differ")
    response = "да"
    record = {
        "schema_version": "kz-intake-owner-affirmation-evidence/v1",
        "thread_id": "01a04247-11fc-7fd1-b3e6-7277403d11d1",
        "assistant_statement": {
            "turn_id": "01a04c2c-0aeb-72f0-994f-e03736548f50",
            "message_id": "msg_03f2f59749ac47b6016a9279e4d3a887d084558cb9b84b3690",
            "timestamp_utc": "2026-08-29T06:19:23.821Z",
            "timestamp_local": "2026-08-29T11:19:23.821+05:00",
            "rollout_ordinal": 10575,
            "body": statement,
            "body_sha256": STATEMENT_SHA256,
        },
        "owner_response": {
            "turn_id": "01a04c48-40be-7ca2-9dbd-6917b158f601",
            "message_id": "msg_01a04c48-4162-72f2-8e28-a9747a5efb0c",
            "timestamp_utc": "2026-08-29T06:49:58.882Z",
            "timestamp_local": "2026-08-29T11:49:58.882+05:00",
            "rollout_ordinal": 10581,
            "body": response,
            "body_utf8_hex": response.encode("utf-8").hex(),
            "body_sha256": hashlib.sha256(response.encode("utf-8")).hexdigest(),
        },
        "adjacency": {
            "directly_adjacent_owner_affirmation": True,
            "asserted_by": "Main Coordinator",
            "interpretation": "The owner's exact response да affirms the immediately preceding unchanged statement by reference.",
        },
        "owner_evidence_ref": OWNER_REF,
    }
    approval = {
        "schema_version": kz_intake.APPROVAL_VERSION,
        "canonical_profile": kz_intake.CANONICAL_PROFILE,
        "payload_sha256": kz_intake.preview_sha256(preview),
        "actions_sha256": kz_intake.actions_sha256(preview["actions"]),
        "approved_candidate_ids": [row["candidate_id"] for row in preview["actions"] if row["action"] == "add"],
        "owner_handle": "saubakirov",
        "owner_evidence_ref": OWNER_REF,
        "approved_at": "2026-08-29T06:49:58.882Z",
    }
    kz_intake.validate_approval(preview, approval, {OWNER_REF})
    (authority / "owner-affirmation.json").write_bytes(kz_intake.canonical_bytes(record))
    (authority / "approval.json").write_bytes(kz_intake.canonical_bytes(approval))
    print(json.dumps({
        "owner_evidence_ref": OWNER_REF,
        "statement_sha256": STATEMENT_SHA256,
        "response_sha256": record["owner_response"]["body_sha256"],
        "approval_sha256": hashlib.sha256(kz_intake.canonical_bytes(approval)).hexdigest(),
    }, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

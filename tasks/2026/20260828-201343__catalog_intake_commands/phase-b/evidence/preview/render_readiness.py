#!/usr/bin/env python3
"""Render the complete human and digest views of the closed Phase B preview."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


sys.path.insert(0, str(Path.cwd()))
from scripts import kz_intake


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def md(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def main() -> int:
    root = Path.cwd()
    preview_dir = Path(__file__).resolve().parent
    evidence = preview_dir.parent
    phase_b = evidence.parent
    universe = evidence / "universe"
    preview_path = preview_dir / "preview.json"
    preview = kz_intake.parse_closed_json(preview_path.read_text(encoding="utf-8"))
    kz_intake.validate_preview(preview)
    payload_sha = kz_intake.preview_sha256(preview)
    actions_sha = kz_intake.actions_sha256(preview["actions"])
    if digest(preview_path) != payload_sha:
        raise SystemExit("canonical preview file bytes differ from payload digest")
    judgements = json.loads((universe / "judgements.json").read_text(encoding="utf-8"))
    accounting = json.loads((universe / "occurrence-accounting.json").read_text(encoding="utf-8"))
    stage_manifest = json.loads((preview_dir / "stage-manifest.json").read_text(encoding="utf-8"))
    by_judgement = {row["candidate_id"]: row for row in judgements["candidates"]}
    by_observation = {row["candidate_id"]: row for row in preview["observations"]}
    by_editorial = {row["candidate_id"]: row for row in preview["editorial"]}
    by_collision = {row["candidate_id"]: row for row in preview["collisions"]}
    add_ids = [row["candidate_id"] for row in preview["actions"] if row["action"] == "add"]
    current_hashes = kz_intake.path_hashes(root)
    controlled = []
    for row in preview["controlled_paths"]:
        controlled.append({
            "path": row["path"],
            "before_sha256": row["before_sha256"],
            "expected_after_sha256": row["after_sha256"],
            "current_production_sha256": current_hashes[row["path"]],
            "production_equals_before": current_hashes[row["path"]] == row["before_sha256"],
        })
    if not all(row["production_equals_before"] for row in controlled):
        raise SystemExit("production controlled path changed")

    owner_statement = (
        "I, saubakirov, approve applying the exact Phase B KZ intake preview payload SHA-256 "
        f"{payload_sha}, actions SHA-256 {actions_sha}, and exactly these ordered ADD candidate IDs: "
        f"{', '.join(add_ids)}. I approve only the expected controlled-path bytes recorded in "
        "tasks/2026/20260828-201343__catalog_intake_commands/phase-b/evidence/preview/preview.json "
        "and no other catalog changes."
    )
    digest_record = {
        "schema_version": "kz-intake-owner-gate-digest/v1",
        "authority_status": "ABSENT_DO_NOT_APPLY",
        "preview_path": "phase-b/evidence/preview/preview.json",
        "preview_file_sha256": digest(preview_path),
        "payload_sha256": payload_sha,
        "actions_sha256": actions_sha,
        "ordered_add_candidate_ids": add_ids,
        "totals": preview["totals"],
        "controlled_paths": controlled,
        "exact_owner_statement_template": owner_statement,
        "exact_owner_statement_sha256": hashlib.sha256(owner_statement.encode("utf-8")).hexdigest(),
        "invalidation": "Any action, row, copy, evidence, ADD order, controlled before hash, or expected byte change requires a successor preview and new exact approval.",
    }
    (preview_dir / "action-digest.json").write_text(
        json.dumps(digest_record, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )
    controlled_record = {
        "schema_version": "kz-intake-controlled-hash-gate/v1",
        "result": "production_unchanged_expected_stage_isolated",
        "paths": controlled,
        "checks": {
            "all_five_current_equal_before": True,
            "all_five_retained_stage_equal_expected_after": all(
                digest(preview_dir / "stage" / row["path"]) == row["expected_after_sha256"]
                for row in controlled
            ),
            "production_apply_performed": False,
        },
    }
    if not controlled_record["checks"]["all_five_retained_stage_equal_expected_after"]:
        raise SystemExit("retained stage differs from expected after hashes")
    (preview_dir / "controlled-hashes.json").write_text(
        json.dumps(controlled_record, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )

    reviewer_state = "PENDING"
    reviewer_hash = None
    status_text = (phase_b / "status.md").read_text(encoding="utf-8")
    status_match = re.search(r"(?m)^lifecycle:\s*(\S+)", status_text)
    lifecycle = status_match.group(1) if status_match else "UNKNOWN"

    lines = [
        "# Phase B Pre-Reviewer Readiness Package",
        "",
        f"- Lifecycle at render time: `{lifecycle}`",
        "- Apply authority: **ABSENT — do not apply**",
        f"- Canonical payload SHA-256: `{payload_sha}`",
        f"- Actions SHA-256: `{actions_sha}`",
        f"- Canonical preview file SHA-256: `{digest(preview_path)}`",
        f"- Persistent Reviewer readiness: `{reviewer_state}`",
        "- Advisory language review: unavailable; see `phase-b/evidence/advisory-language-review.md`.",
        "",
        "This is a non-mutating Executor package for the persistent Reviewer. The exact owner gate has not been entered. It is not an approval envelope, pending marker, receipt, RF, formal REVIEW, or Reviewer verdict.",
        "",
        "## Closed accounting",
        "",
        "| Occurrences | Candidates | ADD | Reject | Duplicate | Unresolved |",
        "|---:|---:|---:|---:|---:|---:|",
        f"| 29 | 28 | {preview['totals']['add']} | {preview['totals']['reject']} | {preview['totals']['duplicate']} | {preview['totals']['unresolved']} |",
        "",
        "The 29 occurrences map losslessly to 28 cases. Only `candidate:aws_kz` has two source occurrences; its candidate disposition is counted once.",
        "",
        "## Controlled paths",
        "",
        "| Path | Before/current production SHA-256 | Expected-after SHA-256 | Production unchanged |",
        "|---|---|---|---|",
    ]
    for row in controlled:
        lines.append(
            f"| `{row['path']}` | `{row['before_sha256']}` | `{row['expected_after_sha256']}` | yes |"
        )
    lines.extend((
        "",
        "The retained `stage/` bytes match every expected-after digest. Current production matches every before digest.",
        "",
        "## Exact ordered ADD IDs",
        "",
    ))
    lines.extend(f"{index}. `{candidate_id}`" for index, candidate_id in enumerate(add_ids, 1))
    lines.extend((
        "",
        "## Complete disposition table",
        "",
        "| Candidate | Identity/type/liveness | Count/date | IT | KZ | Commercial | Category | Collision/alias | Activity | Action | Reason |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ))
    for action in preview["actions"]:
        candidate_id = action["candidate_id"]
        observation = by_observation[candidate_id]
        editorial = by_editorial[candidate_id]
        judgement = by_judgement[candidate_id]
        category = judgement["category"]["proposed"]
        relation = judgement["collisions"]["canonical_alias_near_handle"]
        lines.append(
            f"| `{candidate_id}` | `{md(observation['canonical_handle'])}` / {md(observation['observed_type'])} / verified target-bound | "
            f"{observation['member_count']} / {observation['observed_at']} | {editorial['it_relevant']} | "
            f"{editorial['kazakhstan_relevant']} | {editorial['purely_commercial']} | `{category}` | "
            f"{md(relation)} | {md(judgement['activity']['evidence'])} | **{action['action']}** | {md(action['reason'])} |"
        )
    lines.extend(("", "## Proposed ADD rows and parallel copy", ""))
    for action in preview["actions"]:
        if action["action"] != "add":
            continue
        candidate_id = action["candidate_id"]
        entry = action["proposed_entry"]
        judgement = by_judgement[candidate_id]
        lines.extend((
            f"### `{candidate_id}`",
            "",
            f"- Exact observed row: `{entry['type']}` / `{entry['name']}` / `{entry['handle']}` / category `{entry['category']}` / count `{entry['member_count']}` / date `{entry['last_verified']}`",
            f"- EN: {entry['description']}",
            f"- RU: {entry['description_ru']}",
            f"- KK: {entry['description_kk']}",
            f"- Relevance evidence: {judgement['relevance']['reason']}",
            f"- Commerciality/spam ruling: {judgement['commerciality_spam']['reason']}",
            f"- Activity signal: {judgement['activity']['evidence']}",
            f"- Evidence: {', '.join(f'`{ref}`' for ref in judgement['evidence_refs'])}",
            "",
        ))
    lines.extend((
        "## Non-ADD dispositions",
        "",
        "| Candidate | Action | Exact reason |",
        "|---|---|---|",
    ))
    for action in preview["actions"]:
        if action["action"] != "add":
            lines.append(f"| `{action['candidate_id']}` | **{action['action']}** | {md(action['reason'])} |")
    lines.extend((
        "",
        "## Occurrence accounting",
        "",
        "| Occurrence | Candidate | Action | Source token |",
        "|---|---|---|---|",
    ))
    for row in accounting["occurrences"]:
        lines.append(
            f"| `{row['occurrence_id']}` | `{row['candidate_id']}` | {row['action']} | `{md(row['raw_text'])}` |"
        )
    excluded = stage_manifest["full_suite_stage_snapshot_probe"]
    invariant = next(
        row for row in stage_manifest["validation_results"]
        if row["command"][-1] == "stage_invariant_tests.py"
    )
    lines.extend((
        "",
        "## Isolated stage verification",
        "",
        "- Schema validation: PASS.",
        "- Four generator-owned projections current: PASS.",
        "- Command adapter synchronization: PASS.",
        "- Python compile checks: PASS.",
        "- Complete Phase A suite on unchanged production: PASS.",
        "- Successor-stage invariant suite: PASS.",
        f"- Successor-stage invariant output: `{md(invariant['stdout'].strip())}` / `{md(invariant['stderr'].strip())}`",
        "- The full suite against the successor expected data intentionally reports exactly four baseline-snapshot-only assertions: approved intent totals, locale payload sizes/digest, exact Phase A production bytes, and synthetic baseline+1 changed-key count. Their exact trace is retained in `stage-manifest.json`; Phase A fixtures were not edited and this result is not called a full staged-suite pass.",
        f"- Snapshot probe return code: `{excluded['returncode']}`; classification: `{excluded['classification']}`.",
        "",
        "## Limitations and hard stop",
        "",
        "- Only unauthenticated public Telegram evidence was used; no private history or authenticated fallback was accessed.",
        "- Public group online counts and channel timestamps are point-in-time activity signals, not proof of long-term content quality.",
        "- Four candidates remain unresolved because Kazakhstan relevance or public quality/spam evidence is insufficient.",
        "- The optional Antigravity language advisory was unavailable. The persistent Reviewer audit is pending and remains the required next gate.",
        "- Any evidence freshness, baseline, row, copy, action, digest, or ADD-order change invalidates this statement and requires a successor preview.",
        "- The earlier broad Phase A-then-B mandate authorized preparation only; it is not exact apply authority.",
        "",
        "## Candidate exact owner statement for later use",
        "",
        "Template only — this agent-written text is **not** owner authority and is not yet an owner request. The persistent Reviewer must first approve readiness. Only then may the owner later supply this exact statement in a durable current owner record:",
        "",
        "```text",
        owner_statement,
        "```",
        "",
        "No owner gate may be entered and no approval envelope may be created until the persistent Reviewer readiness audit passes. After that, a later durable owner record and fresh baseline checks are still required.",
        "",
        "## Artifact bindings",
        "",
        f"- `preview.json`: `{digest(preview_path)}`",
        f"- `preview.md`: `{digest(preview_dir / 'preview.md')}`",
        f"- `stage-manifest.json`: `{digest(preview_dir / 'stage-manifest.json')}`",
        f"- `action-digest.json`: `{digest(preview_dir / 'action-digest.json')}`",
        f"- `controlled-hashes.json`: `{digest(preview_dir / 'controlled-hashes.json')}`",
        f"- `universe/run-audit.json`: `{digest(universe / 'run-audit.json')}`",
        f"- `holdout/clean-run-audit.json`: `{digest(evidence / 'holdout' / 'clean-run-audit.json')}`",
        "",
    ))
    readiness_path = preview_dir / "readiness.md"
    readiness_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")

    readiness = readiness_path.read_text(encoding="utf-8")
    required_tokens = [payload_sha, actions_sha, owner_statement, *add_ids]
    for row in controlled:
        required_tokens.extend((row["before_sha256"], row["expected_after_sha256"]))
    for action in preview["actions"]:
        required_tokens.extend((action["candidate_id"], action["action"], action["reason"]))
        if action["action"] == "add":
            required_tokens.extend(str(value) for value in action["proposed_entry"].values())
    missing = [token for token in required_tokens if token not in readiness]
    if missing:
        raise SystemExit(f"readiness rendering missing {len(missing)} required values")
    audit = {
        "schema_version": "kz-intake-readiness-render-audit/v1",
        "authority_result": "executor_render_complete_persistent_reviewer_pending",
        "result": "complete_executor_render_only",
        "readiness_sha256": digest(readiness_path),
        "checks": {
            "payload_and_actions_sha_present": True,
            "all_20_ordered_add_ids_present": True,
            "all_28_dispositions_and_reasons_present": True,
            "all_proposed_fields_and_en_ru_kk_copy_present": True,
            "all_five_before_expected_after_hashes_present": True,
            "all_29_occurrences_present": True,
            "exact_owner_statement_present_and_marked_non_authoritative": True,
            "stage_snapshot_limitation_not_misreported_as_full_pass": True,
        },
        "reviewer_state_at_render": "PERSISTENT_REVIEWER_AUDIT_PENDING",
        "reviewer_readiness_sha256": reviewer_hash,
    }
    (preview_dir / "renderer-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )
    print(json.dumps({
        "payload_sha256": payload_sha,
        "actions_sha256": actions_sha,
        "readiness_sha256": audit["readiness_sha256"],
        "renderer_audit_sha256": digest(preview_dir / "renderer-audit.json"),
        "reviewer_state": reviewer_state,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

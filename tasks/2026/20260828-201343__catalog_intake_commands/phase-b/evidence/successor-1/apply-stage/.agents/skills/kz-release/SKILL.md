---
name: kz-release
description: Prepare a dated verified catalog snapshot and stop before tag or push
---

# KZ Release — Dated Verified Catalog Snapshot

> **Mode:** CL

## Authority

This is a CL release operation. Run only when the owner literally invokes `/kz-release`.
Receive `$ARGUMENTS` literally. Approval of planning, intake, a sweep, review, or a commit is not
approval to create a tag or push.

Read `AGENTS.md`, `RELEASE.md`, root `CHANGELOG.md`, and the active approved TFW task. A release is
a dated verified snapshot tagged `data-YYYY-MM-DD`; it is not a semantic version and never changes
framework version/history files.

## Inputs

- Complete retained catalog-wide sweep evidence for the proposed date.
- Final evidence-backed disposition for every ambiguous/failed result; any unresolved entry blocks release.
- Independent death evidence and per-entry owner approval for each archive.
- Active task authority for changelog and local release-commit preparation.

## Operation

## Ordered Operation

1. **Establish the proposed snapshot.** Derive the date from completed sweep evidence. Inspect
   local `refs/tags/data-YYYY-MM-DD`; refuse a conflicting existing tag and never move, overwrite,
   or force it. Reconcile every live handle exactly once.
2. Run `python scripts/validate_schema.py` and `python scripts/generate_readme.py --check`; require
   success. A stale or hand-edited projection returns to the reviewed data/generator workflow,
   not an inline fix.
3. **Prepare the root changelog.** Confirm root `CHANGELOG.md` is the catalog changelog and framework history is untouched. Move
   only evidenced additions, repairs, archives, and count refreshes from Unreleased to the dated
   snapshot section.
4. **Prepare a truthful, path-scoped snapshot commit.** Inspect the exact diff and reject unrelated
   paths or inferred facts. Stage reviewed paths explicitly. Commit locally with the actual lowercase executing product
   in truthful `[agent/task/release/executor]` attribution and verify subject, dates, paths,
   evidence, schema/currency results, and proposed tag.
5. **Hard stop before external release state.** Present the exact local commit/diff, evidence,
   changelog, and proposed tag. Request explicit
   current approval to create that exact tag and push that exact commit/tag now.
   Prior approvals do not satisfy this gate.
6. **Only after explicit current approval**, recheck unchanged HEAD, worktree, evidence, and tag.
   Create the annotated `data-YYYY-MM-DD` tag without force. Push only the approved branch commit and tag. Record
   actual outcomes, never intent.

## Outputs

- Evidence-complete dated changelog section and truthful path-scoped local snapshot commit.
- Proposed `data-YYYY-MM-DD` tag shown to the owner before external state changes.
- After separate exact approval only: actual annotated tag/push outcome.

## Failure Conditions

- Schema/currency fails, sweep evidence is partial/stale/unresolved, or any fact lacks evidence.
- A death lacks independent evidence/owner triage, a tag conflicts, or unrelated work would enter.
- Current approval is missing, stale, or refers to different commit/evidence/tag state.
- A semantic/framework version changes or any force operation is proposed.

## Hard Stop

Stop after the local commit and ask for explicit current approval before tag or push. Without that
exact approval, create no tag and perform no push. Without an affirmative owner response in this
release conversation, the operation remains stopped.

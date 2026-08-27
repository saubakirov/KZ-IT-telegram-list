---
description: Prepare a dated verified catalog snapshot and stop before tag or push
---

# KZ Release — Dated Verified Catalog Snapshot

> **Mode:** CL (Chat Loop)
> **Authority:** Run only when the owner explicitly invokes `/kz-release`. Approval of a plan,
> TS, sweep, or commit is not approval to tag or push.

Read [AGENTS.md](../../AGENTS.md), [RELEASE.md](../../RELEASE.md),
[CHANGELOG.md](../../CHANGELOG.md), and the active approved TFW task before changing release
state. A project release is a dated verified snapshot tagged `data-YYYY-MM-DD`; it is not a
semantic version and does not modify `.tfw/VERSION` or `.tfw/CHANGELOG.md`.

## Preconditions

- A catalog-wide `/kz-stats` run has retained evidence for every live entry on the proposed
  snapshot date.
- Every ambiguous/failed result has a final evidence-backed disposition; any unresolved entry
  blocks release.
- Every archived entry has independent death evidence and per-entry owner approval.
- The active task authorizes changelog and release-commit preparation. This command never treats
  Phase C tooling approval as Phase D/release approval.

## Operation

1. **Establish the proposed snapshot**
   - Derive `YYYY-MM-DD` from the completed sweep evidence, never from a hand-maintained literal.
   - Inspect `refs/tags/data-YYYY-MM-DD` locally. Refuse a conflicting existing tag and stop; do
     not move, overwrite, or force a tag.
   - Confirm the evidence set covers every current live handle exactly once after approved
     repairs/archives and contains no unresolved disposition.

2. **Run release gates in order**
   - Run `python scripts/validate_schema.py`; require exit zero.
   - Run `python scripts/generate_readme.py --check`; require exit zero. A stale or hand-edited
     README stops the release. Do not repair it inside this command; return to `/kz-stats` or the
     reviewed data/generator workflow that owns the mismatch.
   - Verify the root `CHANGELOG.md` is the catalog changelog and `.tfw/CHANGELOG.md` remains
     untouched.

3. **Prepare the root changelog**
   - Move the reviewed catalog items from `[Unreleased]` into a dated snapshot section.
   - Record entries added, repaired, archived, and counts refreshed from the retained evidence.
     Do not claim changes absent from that evidence.
   - Leave framework history and version files unchanged.

4. **Prepare a truthful, path-scoped snapshot commit**
   - Review the exact diff and reject unrelated dirty paths, inferred facts, or incomplete task
     traces. Never use broad staging.
   - Stage only reviewed release paths explicitly.
   - Use `.tfw/conventions.md` §4 attribution with the actual lowercase executing product, the
     active TFW task ID, scope `release`, and role `executor`, for example:
     `[codex/TFW-4/release/executor] record verified snapshot data-YYYY-MM-DD`.
   - Commit locally. Confirm the subject, current author/commit dates, exact path list, evidence
     references, schema result, README currency result, and proposed tag.

5. **Hard stop before external release state**
   - Stop after the local commit. Present the commit hash/diff, evidence, changelog, and proposed
     `data-YYYY-MM-DD` tag to the owner.
   - Ask for explicit approval to create that exact tag and push that exact commit/tag now.
   - Without an affirmative owner response in the current release conversation, do not create a
     tag and do not push. Prior approvals do not satisfy this gate.

6. **Only after explicit current approval**
   - Recheck that HEAD, working tree, evidence set, and proposed tag are unchanged from what the
     owner approved.
   - Create the annotated `data-YYYY-MM-DD` tag without force.
   - Push only the approved branch commit and tag to the configured remote.
   - Record the actual local/remote outcome; never claim success from intent or an unrun command.

## Refusal Conditions

- README differs from generator output or schema validation fails.
- Sweep evidence is partial, missing, stale for the proposed date, or contains unresolved state.
- A count/date/archive fact lacks observed evidence, or a dead-entry decision lacks owner triage.
- The proposed tag already conflicts with repository history.
- The commit would contain unrelated dirty work or lacks truthful acting-product attribution.
- Explicit owner approval before tag/push is missing, stale, or refers to different state.

---
name: kz-stats
description: Verify Kazakhstan Telegram catalog statistics with evidence and owner triage
---

# KZ Stats — Verified Catalog Sweep

> **Mode:** CL

## Authority

This is a CL live-network operation. Run only when the owner literally invokes `/kz-stats`.
Receive `$ARGUMENTS` literally. Never infer liveness, identity, counts, continuity, or death from
recollection, a plan, one failed request, or approval without evidence.

Read `AGENTS.md`, `RELEASE.md`, and the active approved TFW task. `data/communities.json` is source;
all Markdown catalog projections are generated.

## Inputs

- Current validated catalog and an active task evidence directory.
- Explicit owner invocation for the live sweep.
- Optional literal narrowing arguments only when the owner supplied them; never silently reduce a
  requested catalog-wide universe.

## Ordered Operation

1. Run `python scripts/validate_schema.py`; stop on error. Create temporary machine-summary and
   durable task-evidence paths without credentials, cookies, or authenticated session material.
2. Run `python scripts/validate_links.py --update --summary-json <temporary-summary>`. A non-zero
   unresolved exit feeds owner triage; a missing/malformed summary or execution error stops.
3. Retain the raw summary and validate `schema_version`, `run_date`, totals, and entries. Render
   grew, shrank, unchanged, first-count, signed delta, and every ambiguous/non-target/failed row
   from JSON fields, never reconstructed console text.
4. Retry each unresolved handle once with
   `python scripts/validate_links.py --handle <handle> --update --summary-json <retry-summary>`.
   Retain each result. A repeated failure, contact shell, mismatch, or no count is not death proof.
5. Use browser evidence only as a bounded fallback. Bind the requested handle, visible name, declared type,
   and observed count/no-count. A generic Telegram landing/contact shell is not evidence. Reuse one temporary Chrome tab sequentially,
   and Close the temporary tab when evidence ends; record cleanup. Retain no authenticated secret.
   Owner approval alone is not death evidence.
6. Assign one owner triage disposition:
   - **Verify current target** — target-specific identity/type evidence may write observed date/count;
   - **Repair live link** — continuity evidence plus exact owner approval, then recheck replacement;
   - **Archive proven death** — independent same-community death evidence plus exact owner approval,
     using `python scripts/validate_links.py --archive <handle> --reason <reason> --evidence-ref <ref> --owner-approved`;
   - **Unresolved** — write no date/count/archive fact and record the blocker.
7. Run schema validation, `python scripts/generate_readme.py`, and
   `python scripts/generate_readme.py --check`. Confirm every live entry has retained evidence.
8. Report count/date changes, repairs, archives, unresolved rows, evidence, schema, and currency.

## Outputs

- Raw machine summaries, retries/fallback evidence, deltas, and one disposition per live entry.
- Only observed date/counts and separately approved/evidenced repairs or archives.
- Current generated catalog projections after passing schema and currency gates.

## Failure Conditions

- A fact lacks target-specific evidence; ambiguity/failure automatically archives an entry.
- Raw evidence is absent, a fallback tab remains open, or an unresolved row disappears.
- Generated output is hand-edited, validation fails, or unrelated work is staged.
- Owner triage, independent archive evidence, or exact repair approval is missing.

## Hard Stop

Do not create a release commit, changelog snapshot, tag, or push. Release is a separate literal
`/kz-release` operation with a new current owner gate.

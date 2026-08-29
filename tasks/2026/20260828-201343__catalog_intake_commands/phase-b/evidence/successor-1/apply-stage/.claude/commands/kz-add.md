---
name: kz-add
description: Preview and apply evidence-backed Telegram candidates with exact owner approval
---

# KZ Add — Verified Candidate Intake

## Authority

This is a CL operation. Run it only when the owner literally invokes `/kz-add` with arguments.
Receive the complete literal argument string as `$ARGUMENTS`; never replace it with remembered or
discovered candidates. Parsing, probing, and preview are non-mutating. Catalog mutation requires a
current durable owner record approving the exact payload/action set. A plan, TS, ONB, prior batch,
or agent-written owner name is not approval.

Read `AGENTS.md`, the active approved TFW task, and `data/communities.json`. Do not open unrelated
candidate sources. Never infer identity, type, count, date, category, relevance, commerciality, or
localized copy.

## Inputs

Accept exactly one source mode from `$ARGUMENTS`:

- `--text <UTF-8 text>` for one URL or pasted URL/Markdown/text content;
- `--file <UTF-8 path>` for one supplied file.

Only fixed HTTPS root peer URLs on `t.me`, `telegram.me`, or `telegram.dog` can become candidates.
Every Telegram-like occurrence, including reserved actions, invites, message links, malformed or
duplicate forms, remains in the occurrence ledger with an explicit disposition.

## Ordered Operation

1. Confirm explicit invocation, active task authority, a clean understood worktree, and a durable
   task evidence location. Hash `data/communities.json`, `README.md`, `index.md`, `ru/index.md`, and
   `kk/index.md` before work.
2. Run `python scripts/validate_schema.py`. Parse with
   `python scripts/kz_intake.py parse --text <text> --output <ledger.json>` or the exact `--file`
   form. Stop if UTF-8/source accounting fails. If every occurrence is non-candidate (including a
   reserved-action smoke sentinel), report the dispositions and stop without network or apply.
3. Run the matching `python scripts/kz_intake.py probe ... --output <observations.json>` form.
   Retain the machine output. One fetch is reconciled through the unchanged groups/channels/bots
   classifier; any inconsistent identity/type tuple remains unresolved and contributes no fact.
4. Check case-insensitive collisions across live entries, archive, canonical identity, aliases,
   and this input. Record mechanical facts separately from evidence-cited IT relevance,
   Kazakhstan relevance, commerciality, category, and explicit EN/RU/KK copy review.
5. Assign every candidate exactly one proposed action: add, reject, duplicate, or unresolved. Only
   an observed, target-bound, collision-free, eligible, locale-complete row may be proposed to add.
   Build all five expected generated outputs in an isolated staged project; run schema validation
   and `python scripts/generate_readme.py --check` there.
6. Create the closed proposal bundle, then run
   `python scripts/kz_intake.py preview --bundle <bundle.json> --root <repo> --stage-root <stage> --output <preview.json> --render <preview.md>`.
   Present the digest, complete table, exact ADD set, non-add reasons, evidence paths, and current
   controlled-path hashes. Stop and request approval of that exact payload/action projection.
7. After an explicit current owner response, retain it durably and create a separate
   `kz-intake-approval/v1` envelope binding the payload digest, action digest, exact add IDs, owner,
   evidence reference, and time. Any edit, re-observation, stale date, baseline change, or subset
   choice requires a successor preview and new approval.
8. Recheck current authority, target freshness, collision/eligibility, staged schema/currency, and
   controlled-path B/A/X state. Apply only with
   `python scripts/kz_intake.py apply --preview <preview.json> --approval <approval.json> --root <repo> --stage-root <stage> --pending <pending.json> --receipt <receipt.json> --owner-ref <exact-ref>`.
   All-before may write staged bytes; all-after is an exact no-op; only a matching durable pending
   marker permits mixed-state recovery. Unknown or unmarked mixed state stops.
9. Re-run schema validation, generator currency, relevant tests, and exact probes for added rows.
   Hash all five controlled paths again and retain the separate receipt and final dispositions.

## Outputs

- Lossless occurrence and grouped-candidate ledgers; immutable observation evidence.
- Human preview plus canonical payload digest; separate owner envelope, pending marker, and receipt.
- One explicit disposition per occurrence/candidate and exact before/after controlled-path hashes.
- Only exact owner-approved rows that still pass every gate in source JSON and generated outputs.

## Failure Conditions

- Any occurrence disappears, an invalid URL is salvaged, or bare handles are admitted as URLs.
- A foreign/ambiguous/private/dead/wrong-type target exposes an approved fact.
- Editorial positives, translations, counts, dates, names, or authority are guessed.
- Preview, owner action, staged bytes, controlled hashes, or applied bytes can diverge.
- A partial/unapproved set writes, schema/currency fails, or unrelated work is staged.

## Hard Stop

Never mutate before exact current owner approval. Never archive, release, tag, push, or contact an
external service as a side effect. On uncertainty, preserve evidence and dispositions, report the
specific blocker, and stop.

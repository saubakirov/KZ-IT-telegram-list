# EV — 20260828-201343__catalog_intake_commands / Phase B: Candidate integration final

> **Date**: 2026-08-29
> **Author**: Executor (Codex, acting for `saubakirov`)
> **Task**: 20260828-201343__catalog_intake_commands
> **TS**: [TS Phase B](../../TS__phase-b__candidate_integration.md)

## Environment

| Field | Value |
|---|---|
| OS | Windows |
| Runtime | Python 3.13 |
| Verification target | Local production tree plus isolated approved apply stage |
| External evidence | Bounded unauthenticated Telegram public previews for exactly 20 added targets |

## Evidence

| # | AC | What was verified | Result | Artifact |
|---|---|---|---|---|
| E1 | AC-1 | Sealed 29-occurrence/28-case partition and clean holdout-first result remain immutable. | VERIFIED | `../source/partition-audit.json`; `../holdout/clean-run-audit.json` |
| E2 | AC-2 | All observations, collisions, aliases and the sole `aws_kz` input overlap remain accounted. | VERIFIED | `observations.json`; `collisions.json`; `occurrence-accounting.json` |
| E3 | AC-3 | Reviewed dispositions remain 20 ADD, 3 reject, 1 duplicate and 4 unresolved with complete EN/RU/KK copy. | VERIFIED | `actions.json`; `judgements.json`; Reviewer `review/readiness-successor-1.md` |
| E4 | AC-4 | Payload `2c15bda2…`, actions `bc9316cd…`, ordered ADD IDs and exact five AFTER bytes remained immutable through apply. | VERIFIED | `preview.json`; `action-digest.json`; `stage-manifest.json`; `apply-stage-manifest.json` |
| E5 | AC-5 | Exact adjacent owner chain was retained without reconstructing the committed statement; the separate envelope validates against only the exact current owner reference. | VERIFIED | `authority/owner-affirmation.json`; `authority/approval.json` |
| E6 | AC-6 | Engine apply returned `applied_exact` from five BEFORE states; receipt/current hashes equal all five approved AFTER hashes. All 20 added targets pass post-apply identity, type and liveness checks. | VERIFIED | `receipt.json`; `pending-lifecycle.json`; `post-apply-observations.json`; `post-apply-audit.json` |
| E7 | AC-7 | Schema, four-projection currency, command parity, task index and 41 applicable regression invariants pass. The full 45-test run has exactly four pre-classified baseline-snapshot failures and no additional failure; Phase A fixtures were unchanged. No release or unrelated mutation occurred. | VERIFIED | `stage-manifest.json`; final command output; scoped Git diff |

## Verdict

Evidence verdict: **7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**.

## Final limitations

- The first apply attempt failed before mutation because the retained five-file stage lacked the validation surface required by apply-time preflight. `apply-stage/` combines byte-identical approved controlled files with the exact validation-surface hashes already recorded by the reviewed stage manifest; the successful engine receipt binds the same preview and AFTER hashes.
- All 20 post-apply bodies changed and five counts changed relative to the approved observations. Identity, type and liveness remained exact. These later point-in-time values were retained only as evidence and did not rewrite approved catalog bytes.
- Four legacy full-suite tests assert the pre-apply production snapshot. The applicable 41-test invariant suite passes after apply; the four expected snapshot assertions remain unchanged and are not represented as passing.
- No authenticated/private Telegram data was accessed.

*EV — 20260828-201343__catalog_intake_commands / Phase B: Candidate integration final | 2026-08-29*

# RF — 20260828-201343__catalog_intake_commands / Phase B: Candidate integration

> **Date**: 2026-08-29
> **Author**: Executor (Codex, acting for `saubakirov`)
> **Status**: RF — Complete
> **Parent HL**: [Master HL](../HL-20260828-201343__catalog_intake_commands.md)
> **TS**: [TS Phase B](TS__phase-b__candidate_integration.md)

## 1. What Was Done

### New files

| File | Description |
|---|---|
| `evidence/successor-1/authority/` | Exact adjacent owner affirmation and validated approval envelope |
| `evidence/successor-1/apply-stage/` | Approved controlled bytes plus the reviewed validation surface used by engine preflight |
| `evidence/successor-1/receipt.json` | Exact apply receipt |
| `evidence/successor-1/pending-lifecycle.json` | Pending-marker lifecycle and successful cleanup evidence |
| `evidence/successor-1/post-apply-observations.json` | Bounded public observations for exactly 20 added targets |
| `evidence/successor-1/post-apply-audit.json` | Receipt/hash/action and identity/type/liveness reconciliation |
| `evidence/successor-1/EV__phase-b__candidate_integration_final.md` | Final per-AC evidence |

### Modified files

| File | Changes |
|---|---|
| `data/communities.json` | Added exactly 4 groups and 16 channels from the approved action set; mechanically rebound localization review |
| `README.md`, `index.md`, `ru/index.md`, `kk/index.md` | Exact generator projections from the approved catalog bytes |
| `status.md` and task journal | Transitioned Phase B truthfully to RF after verified apply |

## 2. Key Decisions

1. Used only the direct adjacent successor owner reference and extracted the approved statement from committed `action-digest.json`; no owner wording was reconstructed.
2. After the first preflight failed before mutation, materialized a complete apply stage from the reviewed five controlled bytes and the exact validation-surface hashes already bound in `stage-manifest.json`.
3. Retained post-apply count/body changes as evidence limitations only; no unapproved catalog refresh was performed.

## 3. Acceptance Criteria

- [x] AC-1: sealed partition and honest holdout-first evidence preserved.
- [x] AC-2: all occurrences/candidates and collisions reconciled.
- [x] AC-3: evidence-backed judgements and EN/RU/KK copy retained.
- [x] AC-4: canonical successor preview and staged integrity preserved.
- [x] AC-5: exact owner hard stop cleared by durable current authority.
- [x] AC-6: exact engine apply, final hashes and 20 target re-probes verified.
- [x] AC-7: command/non-release boundaries preserved; applicable regression suite passes.

## 4. Verification

- Schema: PASS (`42 groups`, `36 channels`, `4 bots`, `19 categories`, `2 archive entries`).
- Generator currency: PASS for all four projections.
- Task index: PASS (`4 tasks validate against the closed schema`).
- Command synchronization: PASS.
- Applicable successor invariants: 41/41 PASS after apply.
- Full 45-test classification: exactly four known pre-apply snapshot assertions fail; no additional failure or error.
- Post-apply public probes: 20/20 identity, type and liveness PASS.
- Final controlled hashes: exact approved AFTER values in `post-apply-audit.json` and receipt.

## 5. Evidence

See [final EV](evidence/successor-1/EV__phase-b__candidate_integration_final.md) for evidence details.

Evidence verdict: **7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**.

## 6. Observations (out-of-scope, not modified)

| # | File | Type | Description |
|---|---|---|---|
| 1 | `scripts/test_catalog_generation.py`, `scripts/test_kz_intake.py` | missing-test | Four tests hard-code the prior production snapshot, so the full suite cannot be green after an authorized multi-row catalog apply without a later reviewed snapshot update. |
| 2 | `scripts/kz_intake.py` apply preflight | ux | The reviewed retained stage contained only controlled files; apply-time validation also requires scripts under the stage root. The exact reviewed validation surface had to be materialized separately. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---|---|---|
| S1 | Dynamic Telegram body/count drift is evidence, not authority to mutate an exact approved catalog payload; identity/type/liveness can be verified independently after apply. | domain | Owner/Coordinator execution mandate |

## 9. Diagrams

```text
exact owner chain → validated envelope → reviewed apply-stage → engine apply
        → exact receipt/AFTER hashes → 20 bounded target probes → RF
```

*RF — 20260828-201343__catalog_intake_commands / Phase B: Candidate integration | 2026-08-29*

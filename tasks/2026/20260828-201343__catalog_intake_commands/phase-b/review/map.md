# Review Map — Phase B Candidate Integration

## Inputs

- RF: `../RF__phase-b__candidate_integration.md`
- TS: `../TS__phase-b__candidate_integration.md`
- Phase HL: `../HL__phase-b__candidate_integration.md`
- Master HL contract baseline: `../../HL-20260828-201343__catalog_intake_commands.md` at `1e8cecc7bb996cdc98a8e1c0602316100dbf4cc9`
- Implementation commit: `f62f06f64557b36a8b5d9be713c7267c98ef7712`
- Reviewed readiness ancestor: `268c1fcce723d999e2872a7cbefd3487b0cbb809`

## Understanding

Phase B must turn the sealed 29 submitted occurrences (28 distinct candidates) into a fully evidenced disposition set, obtain exact owner authority for the proposed 20 additions, and apply only those approved staged bytes. The implementation must preserve accuracy over coverage, keep all dynamic post-approval observations evidentiary, regenerate the five controlled catalog projections exactly, and avoid release or other external side effects.

## Acceptance-criteria claim map

| AC | RF claim | Primary evidence named by RF | Planned independent check |
|---|---|---|---|
| AC-1 | The source was sealed before discovery, the holdout was completed first, and the 29/28 universe was derived without omission. | `evidence/source/*`, `evidence/holdout/*`, `evidence/universe/*`, final EV E1 | Re-run source/holdout validators and recompute occurrence/candidate accounting and hashes. |
| AC-2 | All 28 candidates have target-bound observations, collision findings, and one closed disposition; totals are 20 ADD, 3 reject, 1 duplicate, 4 unresolved. | `evidence/observations/*`, `evidence/collisions/*`, successor actions, final EV E2 | Recompute totals; inspect every candidate, observation, collision, and non-add reason. |
| AC-3 | Editorial judgments and all EN/RU/KK copy are supported, equivalent, neutral, natural, and non-promotional. | successor preview/actions, EV E3, prior bounded Reviewer readiness audit | Recheck all 20 proposed rows and all non-add judgments against evidence and the frozen inclusion contract. |
| AC-4 | Canonical preview/action digests, ordered ADD IDs, isolated stage bytes, and five BEFORE/AFTER hashes are exact, with no premature production mutation. | `evidence/successor-1/preview.md`, `actions.json`, manifests, staged files, EV E4 | Rehash canonical artifacts, validate schema/generation in an isolated copy, and compare staged/current bytes. |
| AC-5 | A fresh exact owner affirmation binds the unchanged statement, successor digests, ordered IDs, hashes, and only the allowed owner evidence reference. | `evidence/successor-1/authority/*`, prior readiness audit, EV E5 | Verify message bytes, SHA, adjacency metadata, timestamps/ordinals, approval schema, and stale-envelope exclusion. |
| AC-6 | The exact approved bytes were applied from BEFORE state B, a complete `applied_exact` receipt was emitted, the pending marker was removed, and 20/20 targets were reprobed without rewriting later drift. | apply-stage, receipt, pending lifecycle, post observations/audit, EV E6 | Validate receipt and state transitions, recompute catalog delta, compare current bytes to approved stage, and audit all post-apply targets/drift. |
| AC-7 | Schema, generator currency, task index, command parity, and 41 applicable invariants pass; the only full-suite failures are four stale snapshot assertions; no command/release boundary was crossed. | validation logs, final EV E7, RF observations | Re-run checks independently, classify every full-suite failure, diff command/skill/script surfaces, and inspect repository-visible side effects. |

## Declared deviations and review attention

- The first apply preflight exposed that the retained five-file successor stage omitted the validation scripts required by the engine. The Executor created a task-controlled, manifest-bound apply-stage containing the same five reviewed controlled files plus the required validation surface. Verification must determine whether that addition is exact, scoped, and non-production.
- The full regression suite is reported to have four failures caused solely by hard-coded pre-apply catalog snapshots. Verification must distinguish stale assertions from functional regressions and determine whether the condition is revision-blocking or technical debt under the frozen Phase B scope.
- This is the first formal post-apply review. The earlier `readiness-successor-1.md` is supporting pre-approval evidence only and did not close AC-6 or issue a formal verdict.

## Map self-check

- [x] Every TS acceptance criterion has a mapped RF claim.
- [x] Every mapped claim names evidence and an independent verification path.
- [x] The frozen Master HL baseline and implementation commit are explicit.
- [x] Deviations declared by the RF are visible without judgment.
- [x] No implementation or Executor-owned artifact was modified.

**Stage complete:** YES

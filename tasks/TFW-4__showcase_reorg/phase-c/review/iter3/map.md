# Map — TFW-4 / Phase C: Post-doc Reproducibility Audit
> **Mindset:** Experienced newcomer. Understand the evidence boundary before judging it.
> **RF:** [RF Phase C](../../RF__phase-c__pipeline_tooling.md)
> **TS:** [TS Phase C](../../TS__phase-c__pipeline_tooling.md)
> **Prior review:** [Phase C REVIEW](../../REVIEW__phase-c__pipeline_tooling.md) (Iteration 2 `APPROVE`)

## Understanding

This audit tests whether the Phase C evidence remains reproducible after the authorized
post-review `/tfw-docs` update to `KNOWLEDGE.md` §§1–3. The production schema and generated
README remain valid, and the classifier regressions still pass, but the documented direct harness
invocation now fails when its memory matrix compares the mutable whole `KNOWLEDGE.md` predecessor
against an ONB-era byte hash.

The audit changes no implementation or Phase D draft. It classifies the evidence defect, records
an additive review iteration, and routes a narrow evidence revision back to the Executor while
preserving both the original `REVISE` and the repeat `APPROVE` histories.

## TS ↔ RF Alignment

| TS requirement | RF / EV claim | Aligned? |
|----------------|---------------|----------|
| AC-1–AC-5 deterministic local behavior | Schema, README currency, classifier, command, and CI matrices pass | ✅ Reproduced through AC-5 |
| AC-6 keyed project-memory verification | Harness removes D13–D14 and requires an ONB-era hash for the rest of `KNOWLEDGE.md` | ❌ The check is whole-document byte coupling, not a durable keyed decision baseline |
| AC-7 reproducible bounded evidence | RF says the complete harness passes; EV says to run it directly from repository root | ❌ Current checkout exits 1, and clean snapshot `a141f7c` also exits 1 |
| Phase D boundary | Phase D drafts remain approval-pending and prohibit execution | ✅ Read-only boundary preserved |

## Deviations from TS

The authorized post-review documentation update is not a Phase C implementation deviation. The
defect is that `evidence/offline_harness.py` treats unrelated, later documentation growth as a
failure of the Phase C decision baseline, while the EV publishes an unqualified current-checkout
command. The expected digest `5190da19…` identifies ONB-era working-tree bytes but no checked-in
snapshot or exact reconstruction command preserves those bytes.

## Audit Focus

1. Reproduce the direct EV command in the current post-doc checkout.
2. Test the strongest available snapshot interpretation at lifecycle commit `a141f7c`.
3. Separate production correctness from evidence reproducibility.
4. Define a narrow handoff that makes the memory gate semantic, durable, and negative-testable
   without changing `KNOWLEDGE.md`, production implementation, or Phase D drafts.

## Checkpoint

**Self-check:**
- [x] Read RF §§1–5, EV, and the full harness?
- [x] Read TS acceptance criteria and matched the disputed claims to AC-6/AC-7?
- [x] Read the frozen Master HL baseline and Project North Star?
- [x] Read ONB, prior REVIEW/stages, post-doc `KNOWLEDGE.md` diff, and Phase D draft boundary?

Stage complete: YES


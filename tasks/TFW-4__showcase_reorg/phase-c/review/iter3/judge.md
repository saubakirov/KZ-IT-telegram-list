# Judge — TFW-4 / Phase C: Post-doc Reproducibility Audit
> **Mindset:** Judge. Rule on the evidence interface without rewriting implementation.
> **Verify findings:** [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify V13–V14: AC-6/AC-7 evidence cannot be replayed by the EV's direct command or by clean snapshot `a141f7c`; the production AC-1–AC-5 gates still pass. |
| 2 | Two clauses, both answered. **(a) Purpose Check** and **(b) Design soundness** | ✅ | **(a) Aligned:** baseline §1 promises a “repeatable, dated, evidenced operation”; preserving reproducible evidence avoids the concrete harm of a showcase whose green trace cannot be rerun. **(b) Production design remains sound:** schema/classifier/generator/authority boundaries pass; the defect is confined to evidence provenance and memory-gate design. |
| 3 | Tech debt documented | ✅ | RF §6 is present. This finding is narrow, in-scope rework and must not be deferred to TECH_DEBT. |
| 4 | Style & standards | ❌ | Verify V12–V14: a whole-document byte hash of mutable project memory plus an unqualified invocation violates TFW's reproducible-trace standard. |
| 5 | Observations collected | ✅ | RF §6 remains complete; the new issue is a review finding, not an executor observation or deferred item. |
| 6 | RF completeness (§7–9) | ✅ | RF §§7–9 remain present and adequate; no new human-only fact or diagram change is required. |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | EV E1–E7 and the harness exist; the defect is not a missing artifact. |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | Verify Commands 3–6 and E6/E7: the green full-harness claim cannot be reproduced from current checkout or a durable named snapshot. |
| 9 | Backward compatibility | ❌ | The documented consumer is a later reviewer running the EV command after normal `/tfw-docs`; authorized documentation growth now breaks that interface. |
| 10 | Safety | ✅ | Audit and required revision are local/offline; no secrets, destructive repository action, network, browser, project command, release, tag, or push occurred. |

## Purpose Check — row 2 clause (a)

**Aligned:** Frozen baseline §1 promises that the catalog operation is “repeatable, dated,
evidenced”; repairing the evidence invocation serves that clause and prevents the material harm
of presenting TFW as reproducible while its own recorded replay exits 1.

- **Excess and adjacency:** No. The required change is limited to the Phase C evidence harness,
  EV/RF provenance, and lifecycle routing; Phase D and production behavior remain untouched.
- **Deferral confession:** No. The finding belongs to Phase C evidence and is routed back to the
  Phase C Executor rather than deferred.
- **Materiality:** Yes. A non-replayable green evidence artifact directly weakens the repository's
  showcase purpose even though production behavior remains correct.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF / evidence claim | Contradiction? |
|---|----------------|---------------------|----------------|
| 1 | P1 — data is product; README is output | Production schema/generator still pass | No. |
| 2 | P2 — accuracy over coverage | Identity and non-mutation regressions pass | No. |
| 3 | D13 — freshness reported, not enforced | Schema exits 0 on valid staleness | No. |
| 4 | D14 — `kz-*` remains distinct from `tfw-*` | Static command/adapter matrix passes | No. |
| 5 | Post-doc §§1–3 additions | Harness requires unrelated predecessor bytes to remain fixed | Yes at the evidence-interface level: authorized documentation evolution is incorrectly treated as an AC-6 failure. The knowledge content itself is not wrong. |

## Required Revision Criteria

1. Replace the mutable whole-`KNOWLEDGE.md` byte assertion in
   `phase-c/evidence/offline_harness.py` with a durable, provenance-resolved keyed decision check.
2. The direct current-checkout harness command must exit 0 with the present post-doc
   `KNOWLEDGE.md`, while still failing if any D1–D12 row is removed, duplicated, or changed in
   meaning; if D13/D14 is missing/duplicated; or if D15 appears before Phase D.
3. Documentation changes outside the keyed decision rows, including the authorized current
   §§1–3 additions, must not fail the Phase C memory matrix.
4. `EV__phase-c__pipeline_tooling.md` must state an exact passing invocation and durable
   provenance. `RF__phase-c__pipeline_tooling.md` must report the new independent replay without
   erasing the original REVISE or Iteration 2 APPROVE history.
5. Re-run schema, README `--check`, the complete harness, and the identity regressions; all must
   exit 0. Preserve the post-doc KNOWLEDGE content and leave production implementation, Phase D
   drafts, TECH_DEBT, network/browser/release/tag/push state unchanged.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Purpose was judged against the frozen baseline and Project North Star?
- [x] Purpose and production design soundness were answered separately?
- [x] Evidence presence and sufficiency were answered separately?
- [x] Verify findings are cited directly?
- [x] RF §§7–9 and KNOWLEDGE contradictions were reviewed?
- [x] No Fact Candidate requires challenge?

Stage complete: YES


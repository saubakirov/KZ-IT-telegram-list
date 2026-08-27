# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify V1–V8 establishes AC1–AC5 only. RF §3 and EV E6–E8 leave AC6–AC8 DEFERRED; no local release commit, exact publication approval, tag, push, final memory closure, or frozen Master DoD 24–25 completion exists. TS AC8 lines 373–381 therefore does not permit a completion RF or task closure. |
| 2 | Two clauses, both answered. **(a) Purpose Check. (b) Design soundness.** | ❌ | **(a) ✅ Aligned:** frozen Master §1 promises to turn “these communities are alive and these numbers are real” into a “repeatable, dated, evidenced operation,” and Project North Star `README.md § Purpose` requires every live entry to be verified by a dated network check; the G1/G2 result directly serves those clauses, avoiding the material harm of publishing dead targets or invented/stale counts. It adds no adjacent product scope and does not confess a different home for the data work. **(b) ❌ Unsound trace design:** Verify V3/V8 shows that the checkpoint is encoded as `RF`, even though Master P1/P2/P8 require an honest, repeatable trace and v2 structurally defines `RF` as execution complete. Prose saying “not complete” cannot safely override the lifecycle consumed by the index/review pipeline. |
| 3 | Tech debt documented | ✅ | RF §6 is present and says “No observations.” The 100% audit found no genuine implementation debt in data, generator output, evidence, scripts, or archive handling. The premature RF is an immediate acceptance blocker, not deferrable tech debt. |
| 4 | Style & standards | ❌ | Data/README/evidence naming and formats conform, and all deterministic checks pass. The RF/lifecycle violates the v2 closed lifecycle standard: `.tfw/conventions.md:468` defines RF as execution complete, while the artifact itself reports AC6–AC8 deferred (`RF:44–56`). |
| 5 | Observations collected | ✅ | RF §6 is present; “No observations” is supported for implementation scope. No filler item should be promoted. The reviewer discrepancy is recorded in Verify and must be remediated before acceptance rather than entered as debt. |
| 6 | RF completeness (§7–9) | ✅ | RF §7 contains one specific, sourced owner-death Fact Candidate; §8 and §9 are present and truthfully state no strategic insights/diagrams. The Fact Candidate is supported by TS §6, RES3, the owner decision, and exact archive bindings. Section completeness does not cure the RF timing defect. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | Verify Evidence Verification E1–E8 resolves every EV row and external path: 5 VERIFIED artifacts and 3 explicitly blocked-by-authority DEFERRED rows, with no missing file/reference. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ❌ | The green signals fully establish the bounded G1/G2 checkpoint: exact 63+1 universe, four retries, two target-bound repairs, two archives, schema/generated output, and invariance. They do **not** establish execution completion: the same EV deliberately proves no G3 local release, G4 publication, or AC8 closure. Thus evidence is sufficient for the checkpoint facts but insufficient for the structural `RF` state that v2 consumers interpret as execution complete. |
| 9 | Backward compatibility | ❌ | Catalog consumers remain compatible: schema passes and README is generator-current. The downstream TFW lifecycle consumer is not: `tasks/00-INDEX.md` faithfully projects `phase-d/status.md` as RF, and APPROVE would route that state to KNW/DONE even though the frozen Phase D release contract is still open. This changes the meaning relied on by review/resume/docs workflows. |
| 10 | Safety | ✅ | All inspected evidence is free of credentials, cookies, session tokens, and unrelated browser state; fallback evidence is bounded. No destructive Git operation, release commit, tag, push, force, remote mutation, or unauthorized live rerun occurred. Exact external snapshot roots and rollback boundaries remain intact. |

Rows 7 and 8 differ materially: all evidence exists and has valid statuses (row 7), but it proves only the G1/G2 checkpoint and cannot prove the execution-complete lifecycle implied by `RF` (row 8).

## Purpose Check — row 2 clause (a)

**Aligned — ✅:** frozen Master §1 requires the catalog promise, “these communities are alive and these numbers are real,” to become a “repeatable, dated, evidenced operation,” while Project North Star `README.md § Purpose` requires every live entry to be “verified by a dated network check, never by recollection”; the verified G1/G2 result serves both clauses and prevents the material harm of publishing dead communities or fabricated/stale facts.

- **Excess and adjacency:** No for the implemented catalog result. Only observed fields, two exact repairs, two exact archives, evidence, and generated output changed.
- **Deferral confession:** No for the G1/G2 product work; yes for the separate RF packaging defect, which is judged under design/DoD/evidence/lifecycle rows rather than misclassified as a product-purpose failure.
- **Materiality:** The catalog accuracy harm is material and was correctly addressed. The lifecycle harm is also material, but it is correctable within the same task and does not make the G1/G2 work itself unfit for purpose.

The frozen Master and Project North Star are coherent: both require dated evidence and honest publication boundaries. There is no contract defect and no ground for REJECT.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | P1 — data is product; README is output | Data modified; README regenerated | No — schema/generator and keyed comparison pass |
| 2 | P2 — accuracy over coverage | No inferred count, identity, continuity, or death | No — raw evidence and owner bindings establish every final disposition |
| 3 | P3 — validation precedes generation | Schema/generator/currency passed | No — rerun independently |
| 4 | P4 — external state is CL territory | G1/G2 use explicit owner gates; G3/G4 absent | No — authority boundary was respected |
| 5 | D11/D12 — data-owned North Star and archive | Generated Purpose and exact archive rows | No — structures remain data-owned and schema-valid |
| 6 | D15 — task-local `status.md` is live-state authority | Phase status is `RF`; index projects it | No textual contradiction, but this makes the incorrect execution-complete lifecycle materially authoritative rather than cosmetic |

The RF Fact Candidate is credible and well sourced, but it remains a candidate until a later approved `/tfw-knowledge` pass; the current REVISE verdict does not promote it.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every ⚪ N/A carries a stated reason — no row skipped as a bare ✅? No N/A rows used.
- [x] Row 2(a) answered against the frozen Master baseline and Project North Star, with a quoted clause and named harm?
- [x] Rows 7 and 8 answered separately, with different reasoning?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7–9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or “None”?
- [x] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES

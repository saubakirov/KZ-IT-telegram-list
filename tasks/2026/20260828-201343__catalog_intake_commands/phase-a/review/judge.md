# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify establishes AC-1/5/6/7 and most regression/build/scope portions of AC-8. F2 violates AC-2's producer-possible tuple requirement; F1a violates AC-3/AC-4 exact action/no-op binding; F1b makes the required real schema preflight reject an exact ADD. |
| 2 | Two clauses, both answered. **(a) Purpose Check** — is this what we set out to do? **(b) Design soundness** | ❌ | **(a) ✅ Aligned:** the Project North Star says, “A catalog whose value is accuracy,” and the master HL exact-owner boundary protects against the concrete harm of a false or unauthorized catalog row; the work directly serves that clause. **(b) ❌ Unsound:** zero-add approval can rewrite source bytes, exact ADD cannot interoperate with required schema validation, and impossible transport provenance passes, contrary to master-HL P1/P3/P5 and TS P1/P3. |
| 3 | Tech debt documented | ✅ | RF §6's stale historical-harness assertion is genuine and already recorded as Low/Open TD-19. F1a/F1b/F2 are in-scope acceptance findings, not deferred debt. |
| 4 | Style & standards | ❌ | Naming, standard-library use, scope, command parity, and path neutrality hold. Exact authority/no-manual-repair standards do not: zero-add is not byte-exact, exact add needs a synthetic preflight substitution, and transport records are not producer-closed. |
| 5 | Observations collected | ✅ | RF §6's single observation reproduces: the historical full harness has a stale fixed date while its reusable matrices pass. It survives the quality filter and remains TD-19. |
| 6 | RF completeness (§7–9) | ✅ | RF §7 correctly reports no human-only Fact Candidates; §8 records relevant execution insights; §9 contains a useful intake/apply state-flow diagram. |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | All eight EV rows resolve to tests/source or retained repository artifacts; runtime, calibration, partition, build, production-hash, and scope artifacts exist. |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | The 42 tests, exact build, parity, partition, and hash gates are real but do not prove E2/E3/E4: exact counterexamples F1a/F1b/F2 survive, and the exact-add test explicitly replaces real preflight. |
| 9 | Backward compatibility | ❌ | Existing classifier bodies, command behavior, and production projections remain exact. However, the new exact ADD stage is rejected by the existing `validate_schema.py` locale-review contract, so the new producer does not interoperate with its required existing downstream validator. |
| 10 | Safety | ❌ | No secret, credential, live holdout, production write, pull, deployment, release, tag, push, or external mutation occurred during review. The future mutation boundary remains unsafe because zero approved IDs can still rewrite source bytes; fabricated impossible transport provenance is also accepted as a valid unresolved record. |

Rows 7 and 8 differ deliberately: every named evidence artifact exists, while the positive suite
does not cover and cannot outweigh three independently executable counterexamples.

## Purpose Check — row 2 clause (a)

Reference set used: master HL contract baseline at refreeze commit
`1e8cecc7bb996cdc98a8e1c0602316100dbf4cc9` and the Project North Star in `README.md` § Purpose.
The frozen master-HL sections remain unchanged from that baseline.

- **Excess and adjacency:** No. Implementation/evidence stay within Phase A intake, command parity,
  calibration, fixture apply, and verification boundaries.
- **Deferral confession:** No. Production candidate application remains outside Phase A and did
  not occur.
- **Materiality:** Yes. A false or unauthorized catalog row or non-exact source rewrite directly
  harms the catalog's stated accuracy value.

Outcome: **Aligned**. Checklist row 2 fails only its separate design-soundness clause; there is no
purpose failure or contract defect.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|----------------|----------|----------------|
| 1 | D1 — JSON source of truth / generated projections | Production catalog/projections remain unchanged; future intake writes source only. | No trace contradiction; hashes hold. F1a is an implementation violation because zero action can still rewrite source bytes. |
| 2 | D2 — offline deterministic work separated from live checks | Offline suites and eight bounded calibration probes are recorded separately. | No. |
| 3 | D4 — categories live in data | Intake consults the current category map. | No. |
| 4 | D14 — `kz-*` project operations | All three commands use the project namespace. | No. |
| 5 | D18 — target-bound evidence and exact-universe reconciliation | RF claims producer-closed serialized observations. | No knowledge-file contradiction, but F2 is an implementation violation of the cited evidence rule. |
| 6 | D19 — explicit EN/RU/KK without fallback | Exact ADD includes explicit locale fields and claims real schema validation. | No knowledge-file contradiction, but F1b exposes failed integration with the existing locale-review binding. |

No RF Fact Candidate requires challenge. The RF correctly reports none, and F1a/F1b/F2 are
repository-discoverable implementation facts rather than human-only knowledge.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every ⚪ N/A carries a reason? No N/A rows used.
- [x] Row 2(a) answered against the contract baseline and Project North Star with a quoted clause and named harm?
- [x] Rows 7 and 8 answered separately with different reasoning?
- [x] Referenced `verify.md` findings in DoD assessment?
- [x] Checked RF §7–9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced?
- [x] RF Fact Candidates reviewed?

Stage complete: YES

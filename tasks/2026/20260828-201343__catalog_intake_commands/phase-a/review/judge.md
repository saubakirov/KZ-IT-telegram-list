# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify establishes AC-1 and AC-3–AC-8, including every previous review closure. AC-2 still fails because F2a accepts failed HTTP 2xx records that the producer cannot emit. |
| 2 | Two clauses, both answered. **(a) Purpose Check** — is this what we set out to do? **(b) Design soundness** | ❌ | **(a) ✅ Aligned:** the Project North Star says, “A catalog whose value is accuracy,” and a producer-closed evidence record protects that concrete value. **(b) ❌ Unsound:** `validate_observation` accepts forged failed-2xx provenance contrary to master-HL P1/P3 and TS AC-2/P3. |
| 3 | Tech debt documented | ✅ | RF §6's stale historical-harness assertion reproduces and is already Low/Open TD-19. F2a is an in-scope acceptance finding, not deferred debt. |
| 4 | Style & standards | ❌ | Scope, naming, standard-library use, command parity, byte-exact action derivation, and structural locale validation hold. The closed evidence/provenance standard does not hold because failed 2xx tuples validate. |
| 5 | Observations collected | ✅ | RF §6's single observation is truthful: the full historical harness has a stale date assertion while its reusable matrices pass. TD-19 remains accurate. |
| 6 | RF completeness (§7–9) | ✅ | RF §7 correctly reports no human-only Fact Candidates; §8 records relevant execution insights; §9 contains a useful intake/apply flow diagram. |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | All eight EV rows resolve to code/tests or retained calibration, partition, runtime, build, production-hash, and scope artifacts. |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | Forty-four tests and all deterministic gates are genuine, but the suite omits failed `http_2xx`; direct counterexamples falsify E2 and aggregate E8. |
| 9 | Backward compatibility | ✅ | Six classifier authority bodies, predecessor link/command behavior, command/runtime bytes, production data/projections, schema baseline, and generator output remain exact. F2a is a new-input validation defect rather than a regression of the predecessor behavior. |
| 10 | Safety | ❌ | No holdout reveal, production write, networked build, external mutation, release, tag, push, or deployment occurred. The future evidence boundary remains unsafe because a fabricated failed 2xx transport can be accepted as producer-authentic. |

Rows 7 and 8 differ deliberately: every named evidence artifact exists, while the positive suite
does not exercise and cannot outweigh the directly reproduced failed-2xx counterexamples.

## Purpose Check — row 2 clause (a)

Reference set used: master HL contract baseline at refreeze commit
`1e8cecc7bb996cdc98a8e1c0602316100dbf4cc9` and the Project North Star in `README.md` § Purpose.
The frozen master-HL claims remain unchanged from that baseline.

- **Excess and adjacency:** No. Implementation and evidence stay within Phase A parsing,
  observation, owner approval, isolated fixture apply, command parity, calibration, and verification.
- **Deferral confession:** No. Production candidate application and the sealed holdout remain
  outside Phase A and were not touched.
- **Materiality:** Yes. Treating a producer-impossible transport record as valid provenance can
  admit fabricated evidence into the owner decision boundary, directly harming catalog accuracy.

Outcome: **Aligned**. Checklist row 2 fails only its independent design-soundness clause; this is
an implementation/test defect within the frozen contract, not a purpose or contract defect.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|----------------|----------|----------------|
| 1 | D1 — JSON source of truth / generated projections | Zero/one/many ADD action stages are byte-exact and generator-derived. | No — direct exploit reproduction confirms the action/stage contract and controlled production hashes remain exact. |
| 2 | D2 — offline deterministic work separated from live checks | Offline suites and eight bounded calibration probes are recorded separately. | No. |
| 3 | D4 — categories live in data | Intake consults the current category map. | No. |
| 4 | D14 — `kz-*` project operations | All three commands use the project namespace. | No. |
| 5 | D18 — target-bound exact-universe evidence | RF claims serialized observations accept only exact producer families. | No knowledge-file contradiction, but F2a is an implementation violation of the cited evidence rule. |
| 6 | D19 — explicit EN/RU/KK without fallback | ADD stages mechanically rebind locale review under the real schema. | No — direct 0/1/2 probes and baseline output reproduce. |

No RF Fact Candidate requires challenge. The RF correctly reports none, and F2a is an
independently discoverable repository fact rather than human-only knowledge.

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

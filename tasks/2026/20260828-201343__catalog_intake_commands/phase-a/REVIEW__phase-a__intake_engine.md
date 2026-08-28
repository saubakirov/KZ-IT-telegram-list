# REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-29
> **Author**: saubakirov (Reviewer, via Codex)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase A](RF__phase-a__intake_engine.md)
> **TS**: [TS Phase A](TS__phase-a__intake_engine.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

The final revision is integrated at RF base
`45878d9459e263ed7821dcc84bc400ed0603fb3c`, with implementation
`731b3d6a3350bb3fe41115a4ae9213aaa86bbc6f`. It changes only the three approved implementation
files after Coordinator base `067528d…`, adds structural locale-cardinality validation, and claims
complete closure of all previous action-stage and producer-tuple findings while preserving parser,
classifier, command/runtime, seal, production-hash, scope, and no-mutation boundaries.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | All 24 RF-claimed paths plus two public seal-support artifacts | ✅ 100% audited | [Verification log](review/verify.md#verification-log) |
| 2 | Complete prior D1–D6 closure set | ✅ remains closed | Literal authority, recursive closure, neutral state, complete runtime records, public sealed binding, and exact-SHA build reproduce. |
| 3 | Original F1 unrelated valid stage exploit | ✅ closed | A real schema/generator-valid unrelated delta is rejected before preview/marker/write. |
| 4 | Last zero-ADD semantic reserialization exploit | ✅ closed | Real preflight passes, exact-action validation rejects the changed catalog bytes, and root bytes remain unchanged. |
| 5 | Real zero/one/many ADD stage and apply contract | ✅ closed | Mechanical digest/key-count rebinding, exact JSON/LF, real schema/generator preflight, exact IDs, catalog-last failure, and recovery reproduce. |
| 6 | Prior F2 classifier/facts and retry-attempt tuple exploits | ✅ closed | Target-unbound/arbitrary verified facts, early retry-terminal errors, nonterminal HTTP errors, and every `http_429` tuple are rejected. |
| 7 | Full regression/schema/generator/index/compile/predecessor matrices | ✅ | 44 tests and every approved offline deterministic gate pass. |
| 8 | Data-derived locale invariant and truthful baseline | ✅ | Structural formula grows with real rows, digest binding stays independent, baseline is `139/131/131`, 0 errors. |
| 9 | Classifier/command/runtime hashes, scope, production hashes, public seal | ✅ | Exact authority bodies and pairs; 13 paths, 8 new/5 modified, 2,369 lines; controlled bytes and public bindings unchanged; holdout identities unopened. |
| 10 | Exact-SHA official-image site build | ✅ | Fresh network-disabled build at `731b3d6a…` exits 0; output and retained summary hashes match. |
| 11 | Failed HTTP 2xx producer tuples | ❌ F2a | `ok=false, reason=http_200/http_204/http_299, status_code=2xx, attempts=1` all validate although the producer's 2xx path is fetched success. |
| 12 | Master-HL §7.2 / ONB §7 citations and TD-19 | ✅ | 15/15 citations resolve or are expected-absent and match meaning/application; TD-19 remains accurate and Open. |

Raw verification log: [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-2 fails on F2a; AC-1 and AC-3–AC-8 pass. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ❌ | Purpose aligns with the accuracy North Star; design is unsound because producer-impossible failed-2xx provenance validates. |
| 3 | Tech debt documented | ✅ | Historical harness issue is already Low/Open TD-19; F2a is not deferred debt. |
| 4 | Style & standards | ❌ | Scope, parity, action exactness, and schema structure hold; exact evidence closure does not. |
| 5 | Observations collected | ✅ | RF observation reproduces and remains correctly triaged as TD-19. |
| 6 | RF completeness (§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and diagram sections are present and appropriate. |
| 7 | Evidence completeness — does it exist? | ✅ | All eight EV items and all named repository artifacts exist. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Green tests/build/hashes omit F2a; E2 and aggregate E8 are overclaimed. |
| 9 | Backward compatibility | ✅ | Classifiers, predecessor behavior, commands, schema baseline, generator, and production projections remain exact. |
| 10 | Safety | ❌ | Review caused no external mutation, but fabricated failed-2xx provenance can enter the future owner-evidence boundary. |

## 4. Verdict

**🔄 REVISE**

The revision closes all previously returned counterexamples. D1–D6 remain closed; semantic-only
zero ADD is rejected with bytes unchanged; real zero/one/many ADD mechanically rebinds locale
review, preserves exact JSON/LF, passes the real schema/generator gate, and recovers safely; the
earlier classifier/facts and retry-attempt tuple exploits are rejected. All 44 tests, predecessor
matrices, parity, compile, schema, generator, index, exact scope, classifier/runtime/production
hashes, public seal, and fresh exact-SHA offline site build independently reproduce.

Phase A is nevertheless not ready for holdout evaluation or Phase B. The serialized observation
validator still accepts failed HTTP records with 2xx statuses, while the preserved producer's 2xx
family is successful `fetched`. This is one bounded implementation/test finding inside the frozen
TS; no HL/TS amendment is required. Non-blocking nits: none.

### Item to fix

1. **F2a — exclude 2xx from failed HTTP tuples.** Make the non-429 terminal HTTP branch accept
   only statuses outside 200–299 at attempt 1, while retaining fetched 2xx at attempts 1–3,
   URL/general and `max_retries_exceeded` only at attempt 3, and no `http_429`. Add direct
   `http_200`, `http_204`, and `http_299` rejection tests plus the complete valid producer matrix.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF Phase A §6 | Low | `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py:279` | Historical full harness hardcodes the former oldest-live date and fails before reusable matrices can complete. | Already tracked as TD-19 (Open); owning task updates the assertion. |

F2a is a current acceptance finding, not deferred debt. `TECH_DEBT.md` already contains TD-19, so
this review adds no duplicate.

## 6. Traces Updated

- [x] Phase A `status.md` — lifecycle returned from `RF` to `ONB`, with a clock-derived transition event in the task journal.
- [x] HL status — unchanged because the phase did not complete.
- [x] Phase A `status.md` — `updated` reflects this review; no counter was incremented.
- [x] Other project files — checked for stale information; TD-19 remains correctly Open and no duplicate was added.
- [x] tfw-docs: N/A — REVISE verdict; no post-approval documentation workflow starts.
- [x] tfw-knowledge: N/A — approval was not reached, so knowledge capture does not start.

## 7. Fact Candidates

No fact candidates. The human instruction supplied review authority and sealed-boundary limits,
not new human-only domain facts; F2a is independently discoverable from repository code.

---

*REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-29*

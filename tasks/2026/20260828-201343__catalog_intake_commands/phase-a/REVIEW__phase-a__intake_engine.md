# REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-28
> **Author**: saubakirov (Reviewer, via Codex)
> **Verdict**: 🔄 REVISE
> **RF**: [RF Phase A](RF__phase-a__intake_engine.md)
> **TS**: [TS Phase A](TS__phase-a__intake_engine.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

The Executor revised only the intake runtime/tests after the prior review. The new code derives a
stage from proposed ADD rows, rederives it during apply, writes the catalog last, and validates
serialized observations against enumerated classifier/transport families while preserving the
already-reviewed parser, classifier bodies, command copies, evidence, and no-mutation boundary.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | All 23 RF-claimed paths plus two public seal-support artifacts | ✅ 100% audited | [Verification log](review/verify.md#verification-log) |
| 2 | Previous D1–D6 closures | ✅ remain closed | Literal authority, recursive closure, neutral state, complete runtime records, sealed allocation, and exact-SHA build all reproduce. |
| 3 | Original F1 reject-only unrelated valid stage exploit | ✅ closed | Real valid unrelated delta is rejected before preview. |
| 4 | Original F2 target-unbound/arbitrary verified and failed-transport-with-facts exploits | ✅ closed | Every original mutation is rejected in preview/apply. |
| 5 | Full regression/schema/generator/index/compile/predecessor matrices | ✅ | 42 tests and every approved offline deterministic gate pass. |
| 6 | Classifier semantic preservation and actual result families | ✅ | Six authority bodies are exact to base; all nine actual classifier families and valid transports pass. |
| 7 | Command completeness/parity/path neutrality and runtime binding | ✅ | Exact pairs and hashes reproduce; Claude limitation and Codex explicit paths are stated without overclaim. |
| 8 | Scope/LOC, calibration continuity, partition receipt, controlled hashes | ✅ | 12 paths, 8 new/4 modified, 2,230 lines; exact public/sealed bindings; all production blobs unchanged. |
| 9 | Exact-SHA official-image site build | ✅ | Fresh offline digest-pinned build at `20c19505…` exits 0; summary/output bindings match. |
| 10 | Zero-add exact no-op | ❌ F1a | A semantically identical catalog reserialization with unchanged projections passes real preflight and is applied with zero IDs, rewriting source bytes. |
| 11 | One exact ADD with real preflight | ❌ F1b | Action-stage derivation passes, but the existing schema rejects the added locale-review keys; the green unit test substitutes a synthetic preflight. |
| 12 | Exact failed-transport producer tuples | ❌ F2 | Retry-terminal reasons at early attempts and `http_429` are accepted although the preserved producer cannot emit them. |
| 13 | Master-HL §7.2 / ONB §7 citations and TD-19 | ✅ | 15/15 citations resolve or are expected-absent and match meaning/application; TD-19 remains accurate and Open. |

Raw verification log: [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-2 fails on F2; AC-3/AC-4 fail on F1a/F1b. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ❌ | Purpose aligns with the accuracy North Star; design is unsound because zero-add can write, exact add cannot pass required schema, and impossible transport provenance validates. |
| 3 | Tech debt documented | ✅ | Historical harness issue is already Low/Open TD-19; current findings are not deferred debt. |
| 4 | Style & standards | ❌ | Scope/naming/parity hold, but exact authority, producer closure, and no-manual-repair standards fail. |
| 5 | Observations collected | ✅ | RF observation reproduces and remains correctly triaged as TD-19. |
| 6 | RF completeness (§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and diagram sections are present and appropriate. |
| 7 | Evidence completeness — does it exist? | ✅ | All eight EV items and all named repository artifacts exist. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Green tests/build/hashes are genuine but omit F1a/F1b/F2; E2/E3/E4/E8 are overclaimed. |
| 9 | Backward compatibility | ❌ | Existing classifiers/commands/projections remain exact, but the new ADD producer is incompatible with its required existing schema validator. |
| 10 | Safety | ❌ | No review mutation escaped temporary copies, but a zero-ID approval can still rewrite catalog source bytes. |

## 4. Verdict

**🔄 REVISE**

The revision closes the exact counterexamples returned in the previous review, and the surrounding
evidence is strong: D1–D6 remain closed; all 42 tests, predecessor matrices, command parity/runtime
records, classifier preservation, sealed allocation, exact scope, exact-SHA offline site build,
and controlled production hashes independently reproduce.

Phase A is nevertheless not ready for holdout evaluation or Phase B. The zero-add boundary is not
byte-exact, the one-add path cannot pass the real schema it is required to run, and failed transport
records are not fully constrained to tuples the producer can emit. These are implementation/test
findings within the frozen TS; no HL/TS amendment is required. Non-blocking nits: none.

### Items to fix

1. **F1a — make zero-add a byte-exact no-op.** Require all five staged controlled bytes, including
   `data/communities.json`, to equal the baseline when no ADD action exists; prove preview/apply
   reject a semantically identical reserialization before marker/write.
2. **F1b — make exact ADD pass the real existing schema/generator contract.** Integrate the
   deterministic locale-review binding changes required by a new localized row into the exact
   derived stage without permitting unrelated editorial changes. Replace the synthetic exact-add
   preflight callback with real `validate_staged_project`, and test 0/1/N ADD plus catalog-last
   failure/recovery through the real gate.
3. **F2 — close transport tuples against `fetch_preview_with_retry`.** Bind each failure reason and
   status to its possible attempt count: retry-terminal errors only at the terminal attempt,
   `max_retries_exceeded` only after all attempts, and no `http_429` result. Keep the direct tests
   that every exact real producer family passes.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF Phase A §6 | Low | `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py:279` | Historical full harness hardcodes the former oldest-live date and fails before reusable matrices can complete. | Already tracked as TD-19 (Open); owning task updates the snapshot assertion. |

F1a/F1b/F2 are current acceptance findings, not deferred debt. `TECH_DEBT.md` already contains
TD-19, so this review adds no duplicate.

## 6. Traces Updated

- [x] Phase A `status.md` — lifecycle returned from `RF` to `ONB`, with a clock-derived transition event in the task journal.
- [x] HL status — unchanged because the phase did not complete.
- [x] Phase A `status.md` — `updated` reflects this review; no counter was incremented.
- [x] Other project files — checked for stale information; TD-19 remains correctly Open and no duplicate was added.
- [x] tfw-docs: N/A — REVISE verdict; no post-approval documentation workflow starts.
- [x] tfw-knowledge: N/A — approval was not reached, so knowledge capture does not start.

## 7. Fact Candidates

No fact candidates. The human messages supplied review/sealed-audit authority and evaluation
boundaries, not new human-only domain facts; F1a/F1b/F2 are independently discoverable repository
facts.

---

*REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

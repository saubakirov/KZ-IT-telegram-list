# REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-29
> **Author**: saubakirov (Reviewer, via Codex)
> **Verdict**: ✅ APPROVE
> **RF**: [RF Phase A](RF__phase-a__intake_engine.md)
> **TS**: [TS Phase A](TS__phase-a__intake_engine.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

The Executor completed the bounded F2a correction at implementation
`9185811696c762b5261e9b90f71bee846b6fc692`, changing only `scripts/kz_intake.py` and
`scripts/test_kz_intake.py` after the prior reviewed implementation. The four authorized commits
were integrated without conflict or manual edit onto the prior Reviewer base, producing RF base
`24f9e2de000b8c07d061388ffb878ca72192fff6`, whose tree is byte-identical to Executor tip
`1be9412c03962cd159b528a66603c4dd00af2b30`.

The correction excludes every failed HTTP 2xx observation while preserving fetched 2xx at attempts
1–3, outside-2xx non-429 terminal HTTP at attempt 1, retry-terminal failures at attempt 3, and no
`http_429`. All prior parser, classifier, action-stage, apply, locale, command/runtime, seal,
scope/hash, build, and no-mutation contracts remain unchanged.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | Exact four-commit integration and final implementation binding | ✅ | Stable patch IDs match; integrated tree equals Executor tip; all 13 implementation paths equal `91858116…`. |
| 2 | Failed/fetched 2xx and terminal/retry producer matrix | ✅ | Independent harness rejects 100/100 failed 2xx, accepts 300/300 fetched 2xx, and preserves every attempt/reason/status constraint. |
| 3 | Complete prior D1–D6 closures | ✅ | Trailing authority, recursive schema, neutral states, complete runtime records, public seal, and fresh exact-SHA build reproduce. |
| 4 | Original F1/F2 and last three REVISE exploits | ✅ | Unrelated valid delta, semantic zero ADD, real 0/1/N ADD, locale rebinding, classifier/facts, retry tuples, failure/recovery all reproduce as closed. |
| 5 | Real zero/one/many ADD stage and apply contract | ✅ | Exact JSON/LF, independent object equality, mechanical digest/key count, real schema/generator preflight, exact IDs, catalog-last failure, and recovery pass. |
| 6 | Full deterministic regression gates | ✅ | 45 tests, schema, generator, parity, index, compile, `git diff --check`, and predecessor matrices pass. |
| 7 | Classifier, command/runtime, evidence, and production hashes | ✅ | Six authority bodies and all declared SHA-256 bindings remain exact at required revisions/current tree. |
| 8 | Scope and loop boundary | ✅ | Exactly 13 paths, 8 new/5 modified, 2,406 lines ≤2,500; only intake runtime/test changed for F2a. |
| 9 | Calibration and public sealed boundary | ✅ | Exact public commitment/input/observation/receipt hashes, `29/28/1/8/20`, 8/8 retained observations; holdout identities unopened. |
| 10 | Fresh final exact-SHA official-image site build | ✅ | Network-disabled build at `91858116…` exits 0; EN/RU/KK/sitemap and retained summary hashes match exactly. |
| 11 | Master-HL §7.2 / ONB §7 citations and TD-19 | ✅ | 15/15 citations resolve or are expected-absent and match meaning/application; TD-19 remains accurate and Open. |

Raw verification log: [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | Verify V1–V10 establishes AC-1–AC-8 completely. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | The accuracy North Star is served; closed evidence, exact authority, sealed evaluation, and generated output satisfy master-HL P1–P7. |
| 3 | Tech debt documented | ✅ | Historical harness issue remains Low/Open TD-19; no new deferred debt. |
| 4 | Style & standards | ✅ | Closed schemas, exact serialization, naming, parity, role/scope, and no-manual-repair standards hold. |
| 5 | Observations collected | ✅ | RF observation is actionable and already tracked; reusable matrices pass. |
| 6 | RF completeness (§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and diagram sections are complete and truthful. |
| 7 | Evidence completeness — does it exist? | ✅ | All eight EV items and all named artifacts exist. |
| 8 | Evidence sufficiency — does it establish the claim? | ✅ | Independent adversarial probes, direct exploits, Git/hash checks, and generated outputs prove rather than merely assert the claims. |
| 9 | Backward compatibility | ✅ | Classifiers, predecessor behavior, commands, schema baseline, generator, and production projections remain exact. |
| 10 | Safety | ✅ | Holdout remained sealed and no production/external mutation, networked build, release, tag, push, or deployment occurred. |

## 4. Verdict

**✅ APPROVE**

Phase A satisfies the frozen Master HL, revised Phase A TS, all eight acceptance criteria, evidence
requirements, safety boundaries, and the Project North Star. The bounded F2a correction closes the
last producer-impossible family: failed `http_200` through `http_299` now reject, while every valid
success/terminal/retry family remains exact.

Approval rests on independent execution rather than focused-test trust. All prior D1–D6/F1/F2
counterexamples, semantic zero ADD, real zero/one/many ADD, structural locale validation, neutral
state/recovery, classifier/predecessor behavior, command/runtime records, scope, public seal,
controlled hashes, and a fresh final exact-SHA offline site build reproduce. Phase A may proceed
to the required knowledge/documentation gate; this review does not start Phase B.

Non-blocking trace note: revised ONB/RF/EV headers carry 2026-08-29 while their decorative footer
lines retain the original 2026-08-28 task date. Artifact identities, implementation/evidence
bindings, and lifecycle authority are unambiguous; no contract or evidence claim is affected.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF Phase A §6 | Low | `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py:279` | Historical full harness hardcodes the former oldest-live date and fails before reusable matrices can complete. | Already tracked as TD-19 (Open); owning task updates the assertion. |

No new technical debt was found. `TECH_DEBT.md` already contains TD-19, so this review adds no
duplicate.

## 6. Traces Updated

- [x] Phase A `status.md` — lifecycle advanced from `RF` to `KNW`, with a clock-derived transition event in the task journal.
- [x] HL status — unchanged under the Reviewer role lock; the approved phase contract remains authoritative.
- [x] Phase A `status.md` — `updated` reflects this review; no counter was incremented.
- [x] Other project files — checked for stale information; TD-19 remains correctly Open and no duplicate was added.
- [x] tfw-docs: Applied — `KNOWLEDGE.md` §§1–2 now index the approved intake architecture, operational contract, D21, and key artifact; `TECH_DEBT.md` remains unchanged because TD-19 already covers the only observation.
- [x] tfw-knowledge: N/A — the Phase A RF, REVIEW, RES traces, and owner context contain no new human-only Fact Candidates to consolidate.

## 7. Fact Candidates

No fact candidates. The human instruction supplied review authority, exact correction commits, and
sealed-boundary limits, not new human-only domain knowledge; all reviewed facts are independently
discoverable from repository code and evidence.

---

*REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-29*

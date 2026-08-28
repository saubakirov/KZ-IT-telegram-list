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

The Executor delivered a loss-accountable candidate intake engine, a fetch-once seam around the
preserved classifier, closed preview/approval/receipt records, a fixture-only exact-state apply
boundary, and complete synchronized Claude/Codex copies of all three `kz-*` commands. The revised
RF additionally binds complete runtime records, a non-revealing partition receipt, controlled
production hashes, exact scope, regressions, and an exact-SHA official-image build without
applying a production candidate.

The revision directly addresses the six findings from the first formal review and changes only
intake code/tests after the accepted command smokes.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | All 23 RF-claimed paths plus two public seal-support artifacts | ✅ 100% audited | [verify.md § Verification Log](review/verify.md#verification-log) |
| 2 | Previous D1–D3 code counterexamples | ✅ closed | Literal trailing-dot rejection, strict integers/evidence/transport, and neutral-path first apply/rerun all reproduce. |
| 3 | Previous D4 runtime-evidence finding | ✅ closed with stated limit | Claude supplies complete behavior records plus static path/hash binding but no absolute-path echo; Codex explicitly reports loaded absolute paths/hashes. |
| 4 | Previous D5 partition-evidence finding | ✅ closed | Authorized read-only primary audit reproduces exact source/manifest/receipt hashes, content-derived allocation, 29/28/1/8/20 counts, eight-lowest split, and exact disclosed calibration equality without disclosure. |
| 5 | Previous D6 built-site finding | ✅ closed | Independent digest-pinned official-image build at revised SHA exits 0; metadata summary and four output hashes exactly match the retained log. |
| 6 | Focused/full regression, schema, generator, index, compile, parity, formatting, predecessor matrices | ✅ | 36 tests and every permitted deterministic/offline gate pass. |
| 7 | Classifier semantic preservation | ✅ | Six protected authority bodies are byte-exact to the approved base; predecessor link matrices pass. |
| 8 | Command standalone completeness/parity/path neutrality and authority stops | ✅ | Exact three-command pairs and sync/predecessor checks pass; stats/release stops remain intact. |
| 9 | Scope, LOC, controlled production hashes | ✅ | Exactly 12 implementation paths, 8 new/4 modified, 1,957 changed lines; all five controlled blobs match at every checkpoint. |
| 10 | Exact approved action set versus staged bytes | ❌ F1 | A reject-only preview with zero approved/applied IDs passes real preflight and applies an unrelated valid staged catalog delta. |
| 11 | Closed verified observation tuple | ❌ F2 | A target-unbound, arbitrary-reason typed result marked `verified` passes preview validation and add apply. |
| 12 | All master-HL §7.2 and ONB §7 knowledge citations | ✅ | 15 unique citations / 30 applications resolve and match; 0 irrelevant or hallucinated. |

Raw verification log: see [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-2/AC-3 fail on F2; AC-3/AC-4 fail on F1. AC-1/5/6/7 and the build/scope/regression parts of AC-8 hold. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ❌ | Purpose aligns with the North Star and master HL exact-owner boundary; design is unsound because staged bytes and verified typed evidence can escape the approved semantics. |
| 3 | Tech debt documented | ✅ | RF §6's genuine historical-harness issue is already Low/Open TD-19; no duplicate added. |
| 4 | Style & standards | ❌ | Scope/naming/parity hold, but significant-field closure and exact authority/apply standards fail at F1/F2. |
| 5 | Observations collected | ✅ | RF observation reproduces and remains accurately triaged as TD-19. |
| 6 | RF completeness (§7-9 present) | ✅ | Fact Candidates, Strategic Insights, and a useful state-flow diagram are present and appropriate. |
| 7 | Evidence completeness — does it exist? | ✅ | All eight EV rows and named repository artifacts exist. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Evidence establishes D1–D6 closure and major green gates, but the positive suite omits and execution accepts F1/F2. |
| 9 | Backward compatibility | ✅ | Classifier bodies, predecessor matrices, controlled projections, and existing authority semantics are preserved. |
| 10 | Safety | ❌ | No external/production mutation occurred, but the future production boundary can apply unrelated staged catalog bytes or target-unbound verified evidence. |

## 4. Verdict

**🔄 REVISE**

The revision successfully closes all six findings from the first formal review. Exact scope,
controlled hashes, classifier preservation, command completeness/parity, runtime records,
calibration partition, regressions, official-image build, and zero external mutation are now
independently established.

Phase A is still not ready for holdout evaluation or Phase B. The apply boundary validates staged
byte hashes and generator currency but does not prove that the staged catalog delta implements
exactly the approved `add` rows; a zero-add reject preview can therefore apply unrelated valid
catalog bytes. Independently, the observation consumer accepts a `verified` typed result that the
preserved classifier could never emit, allowing target-unbound evidence into an approved add.
Both are repairable within the frozen TS and must return to the Executor; no HL/TS change is
required.

### Items to fix

1. Bind staged controlled content semantically to the preview action projection. Before the first
   write, prove that the stage differs from the baseline by exactly the proposed/approved add rows
   and their generator-derived projections, with no unrelated modification, removal, reorder, or
   non-add delta. Add a real-preflight test where a zero-add/reject preview binds unrelated valid
   staged bytes and must stop before marker/write.
2. Validate each typed classifier result as an exact possible output tuple, including verified
   reason, declared/observed type relation, `target_bound: true`, fact fields, and successful-body
   transport binding. Add negative preview/apply tests for target-unbound, arbitrary-reason, and
   transport/body-inconsistent verified tuples.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF Phase A §6 | Low | `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py:279` | Historical full harness hardcodes the former oldest-live date and fails before reusable matrices can complete. | Already tracked as TD-19 (Open); owning task updates the snapshot assertion. |

F1 and F2 are current acceptance findings, not deferred debt. `TECH_DEBT.md` already contains
TD-19, so this review does not append a duplicate.

## 6. Traces Updated

- [x] Phase A `status.md` — lifecycle returned from `RF` to `ONB`, with a clock-derived transition event in the task journal.
- [x] HL status — unchanged because the phase did not complete.
- [x] Phase A `status.md` — `updated` reflects this re-review; no counter was incremented.
- [x] Other project files — checked for stale information; TD-19 remains correctly Open and no duplicate was added.
- [x] tfw-docs: N/A — REVISE verdict; no post-approval documentation workflow starts.
- [x] tfw-knowledge: N/A — approval was not reached, so knowledge capture does not start.

## 7. Fact Candidates

No fact candidates. The human messages supplied review authority and sealed-audit boundaries, not
new human-only domain facts; F1/F2 are independently discoverable implementation facts.

---

*REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

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

The Executor added a loss-accountable Telegram candidate intake engine, a minimal immutable seam
around the existing classifier, fixture-only preview/authority/apply behavior, and synchronized
complete Claude/Codex copies of all three `kz-*` commands. The RF binds calibration, production
hash, site, runtime-smoke, scope, and regression evidence without applying a production candidate.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | All 21 RF-claimed paths (12 implementation, 9 evidence) | ⚠️ 100% audited after first discrepancy | [verify.md § Verification Log](review/verify.md#verification-log) |
| 2 | Core deterministic suite, compile, schema, projections, task index, command parity, formatting | ✅ | 31 tests and every listed offline gate passed. |
| 3 | Classifier semantic preservation and predecessor behavior | ✅ | Six authority bodies are byte-exact to the sealed base; both predecessor matrices pass. |
| 4 | Closed source grammar | ❌ | A trailing-dot authority is normalized and accepted as a candidate (D1). |
| 5 | Closed observation/preview schema and evidence gate | ❌ | Boolean integers, blank evidence references, and verified/failed-transport inconsistency are accepted (D2). |
| 6 | Exact-state apply/idempotent rerun | ❌ | Equal before/after controlled-path hashes create an unmarked mixed state on exact rerun (D3). |
| 7 | Command inventory, static completeness, byte parity, path neutrality, authority stops | ✅ | Exact three-command pairs and sync/predecessor checks pass. |
| 8 | Sealed calibration boundary | ⚠️ partial | Precommit timing, eight disclosed/observed cases, and permitted leakage scan hold; exact manifest membership cannot be reproduced from the permitted public evidence (D5). |
| 9 | Fresh Claude/Codex runtime evidence | ❌ | The repository contains coordinator transcriptions, not the required redacted complete transcripts or per-invocation local-load proof (D4). |
| 10 | Scope, LOC, controlled production hashes | ✅ | Exactly 12 paths, 8 new/4 modified, 1,885 changed lines; all five controlled blobs match at every checkpoint. |
| 11 | Built-site evidence | ⚠️ limited | Summary is byte-identical to the prior approved primary artifact; review policy rejected the attempted fresh container build before start, so no fresh rebuild is claimed (D6). |
| 12 | All master-HL §7.2 and ONB §7 knowledge citations | ✅ | 15 unique citations / 30 applications resolved and matched; 0 irrelevant or hallucinated. |

Raw verification log: see [review/verify.md](review/verify.md).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-1, AC-3, AC-4, and AC-7 fail; AC-6 is only partially reproducible. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ❌ | Purpose is aligned with the North Star and master HL §1, but D1–D3 make the implementation design unsound against P1/P3/P5/P6. |
| 3 | Tech debt documented | ✅ | RF §6 contains a genuine historical-harness issue; promoted as TD-19. |
| 4 | Style & standards | ❌ | Closed grammar/schema and usable-without-repair standards fail at D1/D2. |
| 5 | Observations collected | ✅ | RF observation reproduced and passed the debt quality filter. |
| 6 | RF completeness (§7-9 present) | ✅ | Fact Candidates, Strategic Insights, and a useful state-flow diagram are present and appropriate. |
| 7 | Evidence completeness — does it exist? | ✅ | All eight EV rows and their named repository artifacts exist with valid statuses. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Positive tests miss D1–D3; public seal artifacts do not prove manifest membership; runtime summaries do not prove D4. |
| 9 | Backward compatibility | ✅ | Classifier bodies, predecessor matrices, projections, and existing command authority semantics are preserved. |
| 10 | Safety | ❌ | No mutation occurred, but blank evidence and transport inconsistency weaken future production admission; exact rerun recovery is unreliable. |

## 4. Verdict

**🔄 REVISE**

The work is fit for the approved product purpose and most of its static architecture, scope, parity,
classifier preservation, and no-mutation claims are independently verified. It is not ready for
holdout evaluation or Phase B because closed input/schema safeguards and exact apply idempotency
have reproducible defects, while the fresh-runtime and partition-manifest claims are not established
by reviewer-contained evidence. These are repairable within the existing TS; they do not require an
HL or TS rewrite.

### Items to fix

1. Reject trailing-dot and every other non-literal authority without normalizing it into one of the
   three permitted Telegram root hosts; add the missing adversarial grammar vector.
2. Make integer validation exclude JSON booleans, require every add evidence reference to be a
   non-blank usable reference, and bind verified observations to a consistent successful transport
   tuple; add negative tests for each case.
3. Make apply state classification unambiguous when a controlled path has equal before/after hashes,
   and prove first apply plus exact rerun/no-op for both partially and wholly unchanged staged output.
4. Replace coordinator summaries with repository-contained redacted complete fresh Claude and
   Codex transcripts (or equally direct raw harness records) that prove the exact local copy loaded,
   literal routing/result, zero mutation, and accepted-versus-excluded attempts.
5. Add a reviewer-verifiable, non-holdout-revealing inclusion proof for the disclosed eight-case
   calibration so AC-6's exact manifest audit does not require access to sealed material.
6. Provide a safely reproducible fresh built-site run/log at the revised exact implementation SHA;
   preserve the deterministic summary binding.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF Phase A §6 | Low | `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py:279` | Historical full harness hardcodes the former oldest-live date and now fails before its reusable matrices can complete. | → TD-19 backlog; owning task must update the snapshot assertion. |

## 6. Traces Updated

- [x] Phase A `status.md` — lifecycle returned from `RF` to `ONB`, with a clock-derived transition event in the task journal.
- [x] HL status — unchanged because the phase did not complete.
- [x] Phase A `status.md` — `updated` reflects this review; no counter was incremented.
- [x] Other project files — checked for stale information; `TECH_DEBT.md` now records TD-19.
- [x] tfw-docs: N/A — REVISE verdict; only the workflow-required Reviewer debt promotion was made.
- [x] tfw-knowledge: N/A — approval was not reached, so knowledge capture does not start.

## 7. Fact Candidates

No fact candidates. The human messages supplied review authority and boundaries, not new
human-only domain facts; all findings above are independently discoverable from repository files
or deterministic execution.

---

*REVIEW — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

# REVIEW — TFW-4 / Phase C: Pipeline & Tooling

> **Date**: 2026-08-27
> **Author**: Reviewer (Codex)
> **Verdict**: ✅ APPROVE — Iteration 4 repeat review
> **RF**: [RF Phase C](RF__phase-c__pipeline_tooling.md)
> **TS**: [TS Phase C](TS__phase-c__pipeline_tooling.md)
> **Current stage files**: `review/iter4/map.md`, `review/iter4/verify.md`,
> `review/iter4/judge.md`
> **Prior stage files**: `review/iter3/{map,verify,judge}.md`,
> `review/iter2/{map,verify,judge}.md`, and `review/{map,verify,judge}.md`
> This file retains every prior verdict and adds the binding Iteration 4 repeat-review ruling.

## Review History

| Iteration | Date | Input | Verdict | Stage files |
|-----------|------|-------|---------|-------------|
| 1 | 2026-08-27 | Original implementation/evidence at `172e6ac` / `c7180b9` | 🔄 REVISE | `review/{map,verify,judge}.md` |
| 2 | 2026-08-27 | Revised implementation/evidence at `165541c6` / `a141f7c2` | ✅ APPROVE | `review/iter2/{map,verify,judge}.md` |
| 3 | 2026-08-27 | Authorized post-doc checkout after `/tfw-docs`; direct and clean-snapshot evidence replay | 🔄 REVISE | `review/iter3/{map,verify,judge}.md` |
| 4 | 2026-08-27 | Keyed evidence fix `a1c8673`; revised EV/RF lifecycle `556ed83`; current and clean-detached replay | ✅ APPROVE | `review/iter4/{map,verify,judge}.md` |

---

> **History boundary:** Sections 1–7 below preserve the Iteration 2 `APPROVE` synthesis as it
> stood before `/tfw-docs`. Section 8 preserves the binding-at-the-time Iteration 3 `REVISE`.
> Section 9 is the additive, current, binding verdict; it closes that finding without erasing the
> original `REVISE`, repeat `APPROVE`, or post-doc `REVISE` history.

## 1. Map

Phase C retains the intended ten-path offline implementation: structured schema/archive/freshness
rules, evidence-safe Telegram classification and temporary mutation helpers, complete generated
README presentation/currency, two future CL `kz-*` operations, offline CI, and bounded D13–D14 /
TD-3–TD-6 memory updates. The revision narrows target identity to canonical/OG/primary-action
signals, rejects authoritative conflicts, treats description anchors as content, and adds exact
decoy/conflict non-mutation evidence. Production Telegram facts, Phase D, browser use, remote CI,
project-command invocation, release, tag, and push remain outside the result.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | AC-1 schema behavior, TS negatives, added wrong-type/date fixtures, and stale diagnostics | ✅ | Production exits 0; all invalid fixtures reject and valid staleness remains non-fatal (iter2 Verify V2/E1) |
| 2 | AC-2 exact prior decoy, authoritative conflicts, legitimate/fallback previews, C3/C4/C5, summary/update/archive semantics | ✅ | Decoy is `non_target`/false-bound/null-count with 0/0 updates and unchanged target; full affected matrix passes (V3/E2) |
| 3 | AC-3 renderer, README currency/archive behavior, and semantic preservation | ✅ | `--check`, isolated archive/stale/CRLF, 63/63 live entries, order/anchors and exact Purpose/stats pass (V4/V8/E3) |
| 4 | AC-4 `kz-*` documents, authority gates, local references, and protected adapters | ✅ | Static ordered gates pass; all references resolve and 12 `/tfw-*` hashes retain aggregate `288fde38…` (V5–V6/E4) |
| 5 | AC-5 CI YAML and exact local equivalents | ✅ | YAML/static scan and local schema/currency commands pass; remote run remains honestly `DEFERRED` under the no-push boundary (V7/E5) |
| 6 | AC-6 KNOWLEDGE/TECH_DEBT transitions | ✅ | D13–D14 once, D15 absent, only TD-3/TD-6 resolved; TD-5/TD-10/TD-11 stay open (V9–V10/E6) |
| 7 | AC-7 exact scopes, production/protected state, original review history, attribution, refs, tags, and external boundary | ✅ | Exact 10/4/2/3 commit sets, 134 protected, revision-start 4-file Reviewer aggregate plus byte-stable first-stage traces, baseline/HL/TS match, zero tags and no external result artifact (V1/V11–V16/E7) |

Raw repeat-verification log: see `review/iter2/verify.md`. All 14/14 RF-claimed files were
rechecked, with independent identity and history audits beyond the revised harness. Repeat review
used no network, Telegram, browser, project command, Phase D, release, tag, or push.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | Iter2 Verify V1–V16 establishes AC-1 through AC-7 and all 14/14 RF-claimed files |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | Baseline accuracy promise and North Star dated-observation clause are served; authoritative-only/conflict-safe binding closes the material foreign-peer harm without Phase D excess |
| 3 | Tech debt documented | ✅ | RF §6 preserves TD-5/TD-10/TD-11; the prior in-scope defect is fixed, not deferred |
| 4 | Style & standards | ✅ | Exact scope, truthful attribution, standard-library/ASCII conventions, generated README, and protected adapters hold |
| 5 | Observations collected | ✅ | RF §6 is present and no genuine new review observation requires debt promotion |
| 6 | RF completeness (§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and Diagrams are present and adequate |
| 7 | Evidence completeness — does it exist? | ✅ | EV E1–E7 and revised harness exist; primary history remains at `c7180b9`; status vocabulary is TS-compliant |
| 8 | Evidence sufficiency — does it establish the claim? | ✅ | The exact old counterexample, conflict/fallback branches, all mutation gates, and full AC regression independently reproduce |
| 9 | Backward compatibility | ✅ | CLI/rate constants, data/README consumers, framework adapters, contracts, and first-review traces are preserved |
| 10 | Safety | ✅ | No secrets, destructive restore, production external action, release, tag, or push; remote CI remains unclaimed |

## 4. Verdict

**✅ APPROVE**

The repeat review independently verifies all seven ACs and closes the only original in-scope
finding. Commit `165541c6` prevents arbitrary description anchors from binding a requested target,
rejects conflicting authoritative identities, and preserves a bounded fallback when no
authoritative URL exists. Commit `a141f7c2` records the revised evidence/RF without changing the
original Reviewer-owned traces. Every Judge row now holds; Phase C is ready for post-review
documentation capture, not Phase D execution.

### Revision closure

| Prior finding | Resolution | Independent result | Status |
|---------------|------------|--------------------|--------|
| High — unrelated description anchor could bind `requested_group` on an `other_group` preview and persist foreign date/count | Authoritative-only identity plus explicit conflict handling in `165541c6`; exact regression in the evidence harness | `non_target`, `target_bound=false`, `member_count=null`; date/count updates `0/0`; requested fields unchanged | ✅ Closed |

### Preserved Iteration 1 finding and disposition

The first formal verdict remains **🔄 REVISE** in Review History and in the unchanged first-stage
traces. Its original finding is preserved here: pre-revision `scripts/validate_links.py:81–82,196,
398–404` collected every page anchor as identity evidence. A page whose canonical/primary action
belonged to `other_group`, but whose description alone linked `t.me/requested_group`, was classified
`verified` for `requested_group` with count `500`; `apply_updates()` persisted date `2026-08-27`
and count `500` to the wrong entry. Severity was **High**, failing AC-2/AC-7 and the catalog's
no-inferred-fact boundary. Iteration 1 correctly routed to `/tfw-handoff tfw-4`; it is historical
evidence and is not erased by the current approval.

There is no remaining in-scope finding and no frozen-contract amendment. Post-review
documentation is now captured, so Phase C is complete while Master TFW-4 remains open and Phase D
remains unstarted. The exact next workflow is `/tfw-plan tfw-4`.

## 5. Tech Debt Collected

No new item collected. TD-5, TD-10, and TD-11 remain open and unchanged. The former High classifier
issue is a closed Phase C acceptance finding with direct implementation/regression evidence, not
debt to defer.

## 6. Traces Updated

- [x] Task Board — Phase C marked complete; the open TFW-4 master task now points to Phase D planning only
- [x] HL status — N/A; Reviewer role lock forbids HL edits and no amendment is required
- [x] `project_config.yaml` — N/A; no task ID or configuration change belongs to this review
- [x] Other project files — Master TFW-4 remains open; Phase D unstarted; TD-5/TD-10/TD-11 unchanged
- [x] tfw-docs: Applied — updated `KNOWLEDGE.md` §§1–3; preserved D13–D14 without duplication; TD-5, TD-10, and TD-11 remain unchanged
- [x] tfw-knowledge: N/A — no Fact Candidates in either RES iteration, the revised RF, or the REVIEW; the EV is evidence-only and TFW-4 remains below the configured hard interval

## 7. Fact Candidates

No fact candidates. The revision, resolved finding, and all review observations are directly
discoverable repository facts or reviewer analysis, not human-only strategic/domain knowledge.

## 8. Post-doc Reproducibility Audit Addendum

### 8.1 Map

The authorized post-review `/tfw-docs` update expanded `KNOWLEDGE.md` §§1–3 without changing
D1–D14 meaning. Production schema validation and README currency still pass, and the Phase C
offline harness still passes AC-1 through AC-5 plus all identity regressions. It then aborts in
`run_memory_matrix()` because it hashes every remaining byte of `KNOWLEDGE.md` after removing
D13–D14 and compares that mutable document to an ONB-era digest.

This is an evidence/provenance defect, not a reopened classifier or production-data defect. Phase
D drafts remain unapproved, read-only, and unchanged.

### 8.2 Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | Current production gates | ✅ | `validate_schema.py` exit 0; `generate_readme.py --check` exit 0 (Iter3 Verify V1–V4/V8) |
| 2 | Current-checkout EV invocation | ❌ | Harness exit 1 after AC-1–AC-5 at `AssertionError: D1-D12 and predecessor knowledge must match ONB` (V13–V14) |
| 3 | Snapshot-bound interpretation | ❌ | Clean local clone detached at `a141f7c` fails at the same assertion; snapshot minus D13/D14 hashes to `02bef456…`, not `5190da19…` (V13) |
| 4 | Expected-hash provenance | ❌ | Full digest occurs only as a harness literal; no checked-in byte snapshot or exact reconstruction invocation resolves it (V12–V14) |
| 5 | Post-doc KNOWLEDGE change | ✅ authorized | Diff is confined to `/tfw-docs` additions in §§1–3; D1–D14 remain semantically valid and D15 absent (V9) |
| 6 | Full 14-file RF claim set and external boundary | ✅ except finding | 14/14 checked; no network/browser/project-command/Phase D/release/tag/push action (Iter3 Verify) |

Raw audit log: `review/iter3/verify.md`.

### 8.3 Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-6/AC-7 evidence replay fails from both documented current checkout and named lifecycle snapshot |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | Baseline promises a “repeatable, dated, evidenced operation”; production design remains sound, and the narrow revision serves that purpose |
| 3 | Tech debt documented | ✅ | Finding is immediate Phase C rework, not deferred debt |
| 4 | Style & standards | ❌ | Mutable whole-document bytes plus unqualified invocation are not durable trace provenance |
| 5 | Observations collected | ✅ | RF §6 remains present; the new item is a review finding |
| 6 | RF completeness (§7–9 present) | ✅ | Required sections remain complete |
| 7 | Evidence completeness — does it exist? | ✅ | EV E1–E7 and harness exist |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Full replay cannot reproduce the recorded green result |
| 9 | Backward compatibility | ❌ | Normal authorized `/tfw-docs` evolution breaks the published harness consumer |
| 10 | Safety | ✅ | Audit remained local/offline and non-destructive to repository state |

### 8.4 Verdict

**🔄 REVISE — P2 reproducibility finding**

The Iteration 2 `APPROVE` remains valid history for the implementation and identity-binding fix,
but it is no longer the current Phase C verdict. The EV publishes a direct current-checkout
command, yet both that checkout and clean snapshot `a141f7c` exit 1. Because the expected
`5190da19…` predecessor bytes are not preserved through resolvable provenance, this cannot be
accepted as snapshot-bound evidence by adding a qualifier after the fact.

#### Required narrow revision

1. **`tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py`** — replace the
   whole-`KNOWLEDGE.md` predecessor-byte assertion with a durable, provenance-resolved keyed
   decision check.
2. The current-checkout harness command must exit 0 with the authorized post-doc
   `KNOWLEDGE.md`, while negative fixtures must fail for a removed/duplicated/meaning-changed
   D1–D12 row, missing/duplicated D13 or D14, or premature D15.
3. Documentation outside the keyed decision rows, including current §§1–3 additions, must not
   affect the memory matrix.
4. **`evidence/EV__phase-c__pipeline_tooling.md`** — record the exact passing invocation and
   durable provenance. **`RF__phase-c__pipeline_tooling.md`** — record the replay and preserve
   all three review iterations.
5. Require exit 0 from schema, README `--check`, the complete harness, and all identity
   regressions. Preserve current post-doc KNOWLEDGE content; do not change production
   implementation, Phase D drafts, or TECH_DEBT, and perform no network/browser/project-command/
   release/tag/push action.

Exact next workflow: **`/tfw-handoff tfw-4`**.

### 8.5 Tech Debt Collected

No new debt. The finding is a bounded Phase C evidence correction with an immediate handoff, not
a deferred problem. TD-5, TD-10, and TD-11 retain their existing dispositions.

### 8.6 Traces Updated

- [x] Task Board — Phase C returned to `REVISE`; Phase D remains draft and unapproved
- [x] Prior REVIEW history — original `REVISE` and Iteration 2 `APPROVE` preserved
- [x] Phase D drafts — unchanged
- [x] TECH_DEBT — unchanged; no deferred debt created
- [x] tfw-docs: Applied — historical marker preserved; no second docs run is warranted before revision
- [x] tfw-knowledge: N/A — historical marker preserved; no Fact Candidate exists

### 8.7 Fact Candidates

No fact candidates. The failure and its provenance are directly reproducible repository facts,
not human-only domain knowledge.

## 9. Iteration 4 Repeat Review Addendum

### 9.1 Map

Iteration 4 reviews the narrow reproducibility repair in `a1c8673` and the revised EV/RF/Task
Board lifecycle in `556ed83`. The repair retains the ten-path Phase C implementation and the
Iteration 2 identity fix, but replaces the Iteration 3 mutable whole-document digest with a
content-addressed keyed oracle: D1–D12 come from onboarding predecessor `4bc1bb1`, D13–D14 from
its direct implementation child `172e6ac`, and clean lifecycle debt from `a141f7c`.

No production implementation, frozen contract, previous REVIEW trace, Phase D draft, framework
adapter, external state, or release artifact belongs to the repair. Iterations 1–3 remain complete
historical verdicts; this section is the current binding ruling.

### 9.2 Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | Current checkout direct gates | ✅ | Schema exit 0; README `--check` exit 0; complete harness exit 0 (Iter4 Verify V2) |
| 2 | Clean detached exact revision | ✅ | Local no-hardlink clone detached at `556ed83` (parent `a1c8673`) passed the same three commands and remained empty under status/index/worktree checks (V3) |
| 3 | Git provenance and keyed decision oracle | ✅ | Exact subjects/parents; D1–D12 semantic equality; D13/D14 exactly once; D15 absent; remove/duplicate/meaning-change/new-decision negatives reject (V1/V4) |
| 4 | Keyed debt lifecycle | ✅ | TD-3/TD-6 resolve at implementation provenance; TD-5/TD-10/TD-11 remain open Medium; change/remove negatives reject (V5) |
| 5 | Identity and AC-1…AC-6 regression | ✅ | Exact decoy/conflict non-mutation, C3/C4/C5, schema, renderer, commands, CI, decision, and debt matrices pass (V2/V6–V9) |
| 6 | AC-7 commits, paths, protected state, and history | ✅ | Exact path sets `1/10/4/2/3/1/3`; 14/14 RF files; protected `160 / ce33b08d…`; adapters `12 / 288fde38…`; prior REVIEW aggregate retained (V1/V10/V12) |
| 7 | Frozen/draft/external boundaries | ✅ | Master baseline and Phase C HL/TS exact; Phase D draft aggregate exact; zero tags and no network/browser/project-command/release/tag/push action (V11/V12) |

Raw repeat-verification log: `review/iter4/verify.md`. All 14/14 RF-claimed files were checked,
exceeding the configured 6-file minimum. The temporary clean checkout was sent to the Windows
Recycle Bin after evidence capture and is recoverable; its former path no longer exists.

### 9.3 Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | Iter4 Verify V1–V12 establishes AC-1 through AC-7 and all 14/14 RF files |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | Durable keyed provenance serves the frozen “repeatable, dated, evidenced operation” and accuracy clauses without claiming or entering the Phase D live sweep |
| 3 | Tech debt documented | ✅ | RF §6 preserves TD-5/TD-10/TD-11; the P2 finding is fixed, not deferred |
| 4 | Style & standards | ✅ | Role/path locks, content language, exact attribution, generated README, namespace separation, and truthful evidence statuses hold |
| 5 | Observations collected | ✅ | RF §6 is present; no real new issue requires TECH_DEBT |
| 6 | RF completeness (§§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and Diagrams are present and adequate |
| 7 | Evidence completeness — does it exist? | ✅ | EV E1–E7, exact invocation, Git objects, and revised harness exist; remote CI alone is explicitly `DEFERRED` |
| 8 | Evidence sufficiency — does it establish the claim? | ✅ | Current plus byte-clean detached replay and independent positive/negative oracles prove the green result |
| 9 | Backward compatibility | ✅ | Keyed consumers tolerate unrelated docs growth while scripts/data/README/adapters/review history/Phase D drafts remain intact |
| 10 | Safety | ✅ | Local/offline checks only; temporary clone recycled; no secret, destructive restore, external, release, tag, or push action |

### 9.4 Verdict

**✅ APPROVE**

The Iteration 3 P2 reproducibility finding is closed. Commit `a1c8673` removes the mutable
whole-document oracle and anchors every required semantic expectation to resolvable Git objects;
commit `556ed83` records the revised evidence lifecycle. Both the authorized current post-doc
checkout and a byte-clean detached lifecycle revision run the documented command with exit 0.
Independent mutation fixtures prove the oracle still rejects removed, duplicated, or changed
meaning rather than merely weakening the prior assertion.

The original Iteration 1 `REVISE`, Iteration 2 `APPROVE`, and Iteration 3 binding-at-the-time
`REVISE` remain visible in Review History and their unchanged stage traces. Iteration 4 supersedes
only the current verdict. Phase C now advances to post-review documentation capture; this approval
does not approve or start Phase D.

#### Revision closure

| Prior finding | Required resolution | Independent result | Status |
|---------------|---------------------|--------------------|--------|
| Iteration 3 P2 — direct and snapshot replay failed because a mutable whole-document digest had no resolvable predecessor bytes | Durable keyed decision/debt provenance, strict negatives, exact current invocation, current and clean replay, preserved docs/Phase D/debt | All required positive and negative checks pass in current checkout and clean detached `556ed83`; protected/history boundaries hold | ✅ Closed |

There is no remaining in-scope finding and no frozen-contract amendment. Exact next workflow:
**`/tfw-docs tfw-4 phase-c`**.

### 9.5 Tech Debt Collected

No new debt. The P2 item was immediate bounded evidence rework and is now closed. TD-5, TD-10,
and TD-11 retain their existing open Medium dispositions; `TECH_DEBT.md` is unchanged by review.

### 9.6 Traces Updated

- [x] Task Board — Phase C moved from RF to `KNW`; Iteration 4 `APPROVE` recorded
- [x] HL status — N/A; Reviewer role lock forbids HL edits and no amendment is required
- [x] `project_config.yaml` — N/A; no task ID/configuration change belongs to this review
- [x] Prior REVIEW history — Iterations 1–3 and every earlier finding preserved
- [x] Phase D drafts — unchanged and unapproved
- [x] TECH_DEBT — unchanged; no deferred review debt created
- [x] tfw-docs: Applied — binding Iteration 4 result captured; existing Phase C updates in `KNOWLEDGE.md` §§1–3 remain sufficient, with D13–D14 preserved exactly once and no duplicate durable content added
- [x] tfw-knowledge: N/A — both RES iterations, the revised RF, and all REVIEW iterations contain no Fact Candidates; `4 - 0 = 4` is also below the configured hard interval of 5

### 9.7 Fact Candidates

No fact candidates. The fix, provenance, replay, and review results are directly discoverable
repository facts rather than human-only domain knowledge.

---

*REVIEW — TFW-4 / Phase C: Pipeline & Tooling | 2026-08-27*

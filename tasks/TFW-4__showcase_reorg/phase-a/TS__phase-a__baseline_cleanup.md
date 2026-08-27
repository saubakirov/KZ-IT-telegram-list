# TS — TFW-4 / Phase A: Baseline & Cleanup

> **Date**: 2026-08-26
> **Author**: Coordinator (Codex)
> **Status**: ✅ APPROVED — owner pre-authorization for Phases A–C, 2026-08-26
> **Approval Boundary**: Valid because this TS is strictly derived from frozen Master HL
> baseline `8485c29`. It does not authorize Phase D, tags, release, or push.
> **Parent Phase HL**: [Phase A HL](HL__phase-a__baseline_cleanup.md)
> **Parent Master HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Mode**: AG — local filesystem and git only; no network and no push

---

## 1. Objective

Complete the narrowed Phase A contract by removing the dead `.agent/` adapter copy, resolving
TD-7, and making the Task Board describe the preserved TFW-01/TFW-02 folders accurately. The
result establishes a clean boundary for Phase B without replaying the TFW-3 commit work already
satisfied by `0fe6c67` and removed from this phase by Master HL §12 A1.

## 2. Scope

### In Scope

- Delete `.agent/rules/conventions.md`, `.agent/rules/glossary.md`, and the resulting empty
  `.agent/` directory.
- Change only TD-7 in `TECH_DEBT.md` from open duplication to a truthful resolved record.
- Preserve the existing TFW-4 row and iteration-2 research link in `tasks/README.md`, keep its
  workflow status current, and sharpen the TFW-01/TFW-02 note as specified by the Phase HL.
- Verify that surviving `STEPS.md` and `TASK.md` references are historical references allowed by
  amended Master HL DoD 3, not live instructions.
- Produce the mandatory Phase A ONB, evidence, and RF trace through `/tfw-handoff`.

### Out of Scope

- Recommitting or rewriting the TFW-3 result; Phase A deliverables 2–3 were removed by A1 after
  commit `0fe6c67` satisfied them.
- Any modification to `AGENTS.md`, `.agents/**`, `research/**`, the Master HL, `.tfw/**`,
  `.claude/commands/**`, `CLAUDE.md`, `KNOWLEDGE.md`, `data/**`, `scripts/**`, `README.md`,
  `CONTRIBUTING.md`, release files, or GitHub workflows.
- Renaming, restructuring, deleting, or rewriting the legacy `TFW-01` / `TFW-02` task folders.
- Phase B documentation consolidation, Phase C pipeline/tooling, and Phase D network sweep,
  archive triage, release, tag, or push.
- Any Telegram or other network access.

## 3. Principles Check

| # | Principle (from Master HL §7) | Enforced by | Gate |
|---|--------------------------------|-------------|------|
| P1 | The trace before the improvement | AC-4 | Only the four Phase A implementation paths change; no Phase B–D work appears |
| P2 | Honest history over tidy history | AC-4 | Commit metadata is current and its subject describes only the observed Phase A delta |
| P3 | One copy of every rule | AC-1 | `.agent/` is absent while canonical `.tfw/conventions.md` and `.tfw/glossary.md` remain |
| P4 | Derived facts are never written by hand | AC-4 | No count, date, category list, or generated README content changes in this phase |
| P5 | Non-goals are load-bearing | N/A | Phase B creates the North Star; Phase A does not author or render it |
| P6 | The network is the only authority on liveness | N/A | Phase A performs no network check and writes no catalog fact |
| P7 | Absence of evidence is not death | N/A | Phase A neither triages nor modifies communities |
| P8 | The tool serves the operation | N/A | Project commands are Phase C deliverables; Phase A does not modify adapters or commands |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.agent/rules/conventions.md` | DELETE | Remove obsolete duplicate; exact singular path |
| `.agent/rules/glossary.md` | DELETE | Remove obsolete duplicate; exact singular path |
| `TECH_DEBT.md` | MODIFY | Resolve TD-7 only |
| `tasks/README.md` | MODIFY | Preserve existing TFW-4 research hunk; update phase status and legacy proto-artifact note |

**Implementation budget:** 0 new files, 2 modifications, 2 deletions, 4 total paths, and an
estimated delta below 200 LOC. Limits: 30 files, 15 new files, 3000 LOC, 30 modified files.
The complete Phase A lifecycle is expected to contain at most 9 trace files
(HL, TS, ONB, RF, EV, three review-stage files, REVIEW), so the full phase also remains below
the new-file and total-file limits. No override is authorized or required.

## 5. Acceptance Criteria

### AC-1: Remove only the dead singular adapter

The obsolete `.agent/` directory is gone, the framework copies remain canonical, and the live
plural `.agents/` Codex adapter is byte-for-byte unchanged from the executor's onboarding
snapshot.

- [ ] `.agent/` does not exist.
- [ ] `.tfw/conventions.md` and `.tfw/glossary.md` still exist and are unmodified.
- [ ] Every pre-existing file under `.agents/**` still exists with unchanged content.

Gate: Literal-path existence checks plus before/after path-and-hash comparison for `.agents/**`;
`git diff --name-status` shows only the two singular `.agent/rules/*` deletions for this AC.

Evidence: N/A — this is local repository state fully established by deterministic filesystem,
hash, and git checks.

### AC-2: Resolve TD-7 truthfully

The debt register records that the duplicate `.agent/rules/` copies were removed and TD-7 is
resolved, without changing the status or substance of any unrelated debt item.

- [ ] TD-7 reads `✅ RESOLVED` and identifies removal of the duplicate adapter as the resolution.
- [ ] No other TD row changes except unavoidable table formatting local to TD-7.

Gate: Compare the `TECH_DEBT.md` diff against the pre-execution version and query the TD-7 row.

Evidence: N/A — the acceptance result is the versioned document diff itself.

### AC-3: Preserve and clarify the Task Board trace

The TFW-4 board row remains present with the completed iteration-2 RES link and a status matching
the workflow stage. The TFW-01/TFW-02 note makes clear that they are preserved pre-framework
proto-artifacts which borrowed the vocabulary but lack the contract, freeze, Definition of
Failure, and review lifecycle. No allowed historical mention of `STEPS.md` or `TASK.md` is erased.

- [ ] The existing TFW-4 row and iteration-2 RES link survive the edit.
- [ ] The legacy note carries the explicit proto-artifact distinction from the Phase HL.
- [ ] Repository search finds no surviving `STEPS.md` or `TASK.md` reference used as a live
  instruction; historical references in `tasks/**`, `KNOWLEDGE.md`, `TECH_DEBT.md`,
  `tasks/README.md`, and `.tfw/**` remain permitted.

Gate: Inspect the narrow `tasks/README.md` diff and classify every repository-search match using
the allow-list in Master HL DoD 3.

Evidence: N/A — the board and reference classification are directly reviewable repository text.

### AC-4: Keep the phase bounded and the history honest  [depends: AC-1]

Apart from mandatory Phase A trace artifacts, the completed change set contains only the four
paths in §4. It contains no Phase B–D work, does not overwrite pre-existing owner/user changes,
and records the phase with current, truthful git metadata.

- [ ] `AGENTS.md`, `.agents/**`, `research/**`, the Master HL, `.tfw/**`, and every other
  out-of-scope path match their onboarding state.
- [ ] No network, tag, release, or push action occurred.
- [ ] The local execution commit follows the inherited attribution grammar and does not backdate
  or claim work excluded by A1.

Gate: Compare the final path set and protected-path hashes with ONB, inspect `git status`, and
inspect the local commit subject/date. Do not use a whole-tree restore to obtain a clean diff.

Evidence: N/A — local git metadata and the protected-path comparison are the authoritative checks;
record their output in the EV file.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-a__baseline_cleanup.md` | Structured environment header, per-AC evidence statuses, protected-path comparison references, and verdict (required) |

All four ACs use `N/A` for external/live evidence because Phase A changes only local repository
state. The EV file is still mandatory and must record the deterministic gate results; `N/A` does
not mean the gates may be skipped.

## 6. Technical Guidance

- The frozen authority is Master HL baseline `8485c29`; Phase A derivation is in
  `HL__phase-a__baseline_cleanup.md`.
- Master HL §12 A1 removed the already-completed TFW-3 commit deliverables. Do not manufacture a
  replacement commit for `0fe6c67` or narrate it as Phase A work.
- `.agent/` and `.agents/` differ by one character and have opposite dispositions. Resolve and
  compare literal paths; the plural tree is protected by Master HL DoF 14 and A3.
- `tasks/README.md` already has a pre-existing user change that replaces the pending RES marker
  with the iteration-2 RES link. Preserve that hunk while applying the Phase A note/status edit.
- `AGENTS.md`, `.agents/**`, `research/iterations.yaml`, and both research iteration directories
  contain owner/user work outside this TS. They must not be staged, rewritten, cleaned, or moved.
- Amended Master HL DoD 3 permits historical `STEPS.md` / `TASK.md` references in `tasks/**`,
  `KNOWLEDGE.md`, `TECH_DEBT.md`, `tasks/README.md`, and `.tfw/**`. The forbidden state is a live
  instruction, not the literal text.
- The established execution commit scope slug is `baseline-cleanup`; commit attribution remains
  subject to the inherited Quality Contract below.

### Inherited Quality Contract (verbatim from Master HL §7.1)

- No placeholders. No `TODO`, no stub, no "implement later". `.tfw/README.md` § Completeness
  Over Speed.
- No hardcoded derived value in any file — counts, dates, category lists.
- `README.md` is never hand-edited. Change the generator or the data.
- No file under `.tfw/` is touched except `project_config.yaml` and `knowledge_state.yaml`.
- No `/tfw-*` adapter file in `.claude/commands/` is modified.
- Every commit follows `conventions.md` §4: `[agent/task/scope/role] summary`, with
  `agent` = `claude-code`, `task` = the task ID, `role` = the acting TFW role.
- `git push` only on explicit owner approval given at that moment.
- Python: standard library only. The project's sole declared dependency is `requests`
  (`project_config.yaml` → `stack.dependencies`), and no current script uses it — do not add
  one. Type hints and docstrings in the existing style; ASCII-tagged output (`[OK]`, `[FAIL]`,
  `[INFO]`) to stay readable in a Windows console.
- Scripts exit non-zero on error, zero on success. `/kz-release` and CI depend on it.

## 7. Definition of Failure

- ❌ `.agents/` (plural) or any file under it is deleted, modified, moved, or omitted from the
  protected-path comparison.
- ❌ Any `.tfw/**`, `.claude/commands/tfw-*`, `AGENTS.md`, research artifact, Master HL,
  catalog data, script, generated README, or Phase B–D file is modified.
- ❌ TFW-01 or TFW-02 is renamed, restructured, deleted, or rewritten.
- ❌ A pre-existing `tasks/README.md` hunk, especially the iteration-2 RES link, is lost.
- ❌ Historical trace references are deleted merely because they contain `STEPS.md` or `TASK.md`.
- ❌ A commit is backdated, uses nonconforming attribution, or claims TFW-3 work already excluded
  by A1.
- ❌ Any network request, community mutation, tag, release, or push occurs.
- ❌ A placeholder, hardcoded derived value, or unrelated cleanup enters the phase.

Any failure must be corrected before RF. If `.agents/**` is affected, restore it from the exact
onboarding snapshot, stop, and report; do not continue on the assumption that adapter recovery is
complete.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Singular/plural adapter confusion | Literal-path checks and before/after `.agents/**` hashes in AC-1 |
| Overwriting an overlapping user diff in `tasks/README.md` | Preserve the existing hunk; accept only the narrow Phase A diff in AC-3 |
| Over-broad reference cleanup destroys trace context | Classify matches under amended DoD 3 instead of deleting by string match |
| Phase creep into documentation or tooling | AC-4 enforces the four-path implementation set and protected paths |
| Local commit entangles untracked research or adapters | Inspect the commit path list; never stage all dirty files |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `TECH_DEBT.md` | Phase D | Phase A changes TD-7 only; preserve every other row for later resolution work |
| `tasks/README.md` | Phase lifecycle and Phase D | Preserve the Phase A proto-artifact note and update only workflow status/links later |

---

*TS — TFW-4 / Phase A: Baseline & Cleanup | 2026-08-26*

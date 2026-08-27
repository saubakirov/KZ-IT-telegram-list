# RF — TFW-4 / Phase A: Baseline & Cleanup

> **Date**: 2026-08-26
> **Author**: Executor (Codex)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Phase HL**: [Phase A HL](HL__phase-a__baseline_cleanup.md)
> **TS**: [TS Phase A](TS__phase-a__baseline_cleanup.md)

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `ONB__phase-a__baseline_cleanup.md` | Executor understanding, protected-worktree snapshot, questions, risks, and knowledge-citation verification created before implementation |
| `evidence/EV__phase-a__baseline_cleanup.md` | Mandatory per-AC environment, deterministic gate output, and evidence verdict |
| `RF__phase-a__baseline_cleanup.md` | Phase A result trace |

### Modified Files

| File | Changes |
|------|---------|
| `TECH_DEBT.md` | Moved TD-7 from the open table to a truthful `✅ RESOLVED` record linked to this RF; no other TD identifier changed |
| `tasks/README.md` | Preserved the iteration-2 RES and approved Phase A TS links, advanced TFW-4 to `🟢 RF`, added Phase A trace links, and clarified the preserved TFW-01/TFW-02 proto-artifact status |

### Deleted Files

| File | Reason |
|------|--------|
| `.agent/rules/conventions.md` | Obsolete singular-adapter duplicate; `.tfw/conventions.md` is canonical |
| `.agent/rules/glossary.md` | Obsolete singular-adapter duplicate; `.tfw/glossary.md` is canonical |

### Local Commits

| Commit | Scope |
|--------|-------|
| `2250456` | ONB only — `[claude-code/TFW-4/baseline-cleanup/executor] record phase a onboarding` |
| `f8d6be2` | Exactly the four implementation paths — `[claude-code/TFW-4/baseline-cleanup/executor] remove obsolete singular adapter` |

No push, tag, release, or network action was performed.

## 2. Key Decisions

1. Delete the two approved files by exact literal singular path, then remove the empty
   `.agent/rules/` and `.agent/` directories non-recursively. This avoids any ambiguous glob near
   the protected `.agents/` plural path.
2. Move TD-7 into the existing Resolved table rather than leave a resolved item under Open Items.
   The record includes `✅ RESOLVED`, the concrete duplicate-removal outcome, the date, and this RF.
3. Edit `tasks/README.md` from its dirty working-copy state. This preserves the pre-existing
   iteration-2 RES and Phase A TS links while applying the phase-owned status and legacy-note
   changes.
4. Use separate path-scoped commits for ONB and implementation. No broad staging command was
   used, so unrelated owner/user changes and research files remained outside both commits.

### Deviations

- No implementation-scope or acceptance-criteria deviation occurred.
- The approved Master HL and TS require commit `agent=claude-code`, while the executor is Codex
  and the general convention derives `agent` from the acting product. The more specific frozen
  task contract was followed without changing Git author/committer metadata; the inconsistency is
  reported in §6.
- The offline schema validator was run as a supplemental smoke check. It did not modify data or
  generated output and did not expand Phase A scope.

## 3. Acceptance Criteria

- [x] **AC-1 — Remove only the dead singular adapter.** `.agent/` is absent;
  `.tfw/conventions.md` and `.tfw/glossary.md` exist with zero diff; all 11 `.agents/**` files
  retain the onboarding manifest hash
  `b9013c985044bea7f309901662dfa79f78c2c87473aaa7842b68af27fb276d6b`.
- [x] **AC-2 — Resolve TD-7 truthfully.** TD-7 is the only changed `TD-N` record and now states
  `✅ RESOLVED` with the duplicate-adapter removal as its resolution.
- [x] **AC-3 — Preserve and clarify the Task Board trace.** The TFW-4 row retains the completed
  iteration-2 RES and approved Phase A TS links, records the current RF stage, and the legacy note
  now identifies TFW-01/TFW-02 as preserved pre-framework proto-artifacts. All 12 surviving
  `STEPS.md` / `TASK.md` reference files are within the amended DoD 3 allow-list and contain
  historical/migration context rather than a live instruction.
- [x] **AC-4 — Keep the phase bounded and history honest.** The 116-file protected-workspace
  manifest is unchanged from ONB; implementation commit `f8d6be2` contains only the four §4
  paths, has current 2026-08-26 metadata, follows the approved prefix, and has no pointing tag.
  No Phase B–D work, network, release, tag, push, or whole-tree restore occurred.

## 4. Verification

- Frozen baseline: PASS — baseline `8485c29`, `HEAD` at onboarding, and the working Master HL all
  resolve to blob `194667238926ac096957a82123a24ba575a7dbda`.
- AC-1 literal path/hash gate: PASS — singular absent, plural manifest unchanged, canonical
  `.tfw/` files unchanged.
- AC-2 debt-row comparison: PASS — `changed_td_ids=TD-7`.
- AC-3 board/reference gate: PASS — required links and note present;
  `legacy_reference_outside_allowlist_count=0` after semantic inspection of all 12 matching files.
- AC-4 protected scope gate: PASS — protected manifest remained
  `2ca61142d7914f0fbf7ccd8e554861f670139af5cc9184a235408984acdfcac3`; commit path list is exactly
  two deletions and two modifications.
- Lint (`python scripts/validate_schema.py`): PASS — 40 groups, 18 channels, 5 bots, 18
  categories, 0 errors, exit 0.
- Tests (`python scripts/validate_links.py`): N/A — the approved TS prohibits network access and
  defines no test command for Phase A; the network-bound validator was not run.
- Verify (`python scripts/validate_schema.py && python scripts/generate_readme.py`): N/A — the TS
  defines deterministic per-AC gates and prohibits an out-of-scope generated README change; the
  schema half was run separately and passed.
- Build/compile gate: N/A — the approved Phase A TS specifies no build or compile command for this
  documentation-and-deletion phase.
- Added-placeholder scan on the implementation commit: PASS — 0 matches.

## 5. Evidence

See [EV file](evidence/EV__phase-a__baseline_cleanup.md) for evidence details.

Evidence verdict: 0/4 VERIFIED, 0 DEFERRED, 0 BLOCKED, 4 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/conventions.md`; Master HL; Phase A TS | 221; 678; 177 | naming | The general commit rule derives `agent` from the acting product, but the frozen TFW-4 contract hardcodes `claude-code`. This Codex execution followed the specific approved contract; a future Coordinator should reconcile the convention/contract mismatch without editing it under the Executor role. |
| 2 | `tasks/README.md` | 25 | style | The board links to user/Coordinator-owned Phase A TS and iteration-2 RES artifacts that remain untracked at RF time. They were deliberately excluded from implementation commits per the delegation; the Coordinator should preserve them in a separate trace-owned commit before task closure. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW-4 / Phase A: Baseline & Cleanup | 2026-08-26*

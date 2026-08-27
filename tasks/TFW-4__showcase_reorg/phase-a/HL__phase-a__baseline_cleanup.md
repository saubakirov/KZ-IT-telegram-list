# Phase HL — TFW-4 / Phase A: Baseline & Cleanup

> **Date**: 2026-08-26
> **Author**: Coordinator (Codex)
> **Status**: 🟡 TS_DRAFT — derivation complete; Phase A TS pre-authorized
> **Contract**: DERIVATION-ONLY — inherits frozen Master HL baseline `8485c29`
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Authority**: Owner pre-authorization covers Phases A–C only when each TS is strictly
> derived from the frozen Master HL. It does not cover Phase D, tags, release, or push.

> This Phase HL adds execution context only. It does not define an independent vision,
> acceptance contract, failure contract, or principles; Master HL §§1, 5, 6, and 7 remain the
> sole authority, per `conventions.md` §3 rules 20–21.

---

## 2. Phase Context

Phase A originally included committing the TFW-3 installation and explaining that late commit.
Commit `0fe6c67` already delivered both outcomes before research began. Master HL §12 A1 therefore
applied a `RESTRICT`: Phase A now contains only deliverables 1, 4, and 5 from Master HL §4.

| Item | Current state | Governing source |
|------|---------------|------------------|
| `.agent/rules/conventions.md` | Tracked duplicate; 78 lines | Master HL §2, Phase A deliverable 1, DoD 1 |
| `.agent/rules/glossary.md` | Tracked duplicate; 76 lines | Master HL §2, Phase A deliverable 1, DoD 1 |
| `.agents/skills/tfw-*/SKILL.md` | Live Codex adapter; 11 untracked files that must survive unchanged | Master HL §12 A3, DoF 14 |
| `TECH_DEBT.md` TD-7 | 🔴 OPEN | Master HL Phase A deliverable 4, DoD 1 |
| `tasks/README.md` | TFW-4 row exists and points to research iteration 2; the legacy note still describes TFW-01/02 only as predating TFW | Master HL Phase A deliverables 4–5, §11 S5, §12 A4 |
| `STEPS.md`, `TASK.md` | Absent; remaining references are historical trace/context references | Master HL DoD 3 as amended by A2 |

The checkout is intentionally dirty with owner/user work in `AGENTS.md`, `tasks/README.md`,
`research/**`, and `.agents/**`. The Phase A executor may make a narrow edit to
`tasks/README.md`; every pre-existing hunk and every other listed path must be preserved.

## 3. Derived Phase Outcome

The phase outcome is a smaller, truthful repository surface:

```text
BEFORE                                      AFTER PHASE A
.agent/rules/conventions.md   duplicate     .agent/                  absent
.agent/rules/glossary.md      duplicate     .tfw/                    canonical
.agents/                      live          .agents/                  unchanged
TECH_DEBT TD-7                OPEN          TECH_DEBT TD-7            RESOLVED
legacy board note             ambiguous     legacy board note         explicit proto-artifact label
```

Derived deliverables:

1. Remove `.agent/` (singular) and only that dead adapter directory.
2. Mark TD-7 resolved without altering unrelated debt entries.
3. Keep the TFW-4 Task Board row current and sharpen the TFW-01/TFW-02 note: they are preserved
   pre-framework proto-artifacts that borrowed the vocabulary but lack the contract, freeze,
   Definition of Failure, and review lifecycle.
4. Confirm that surviving `STEPS.md` / `TASK.md` mentions are historical, never live instructions.

The phase does not repeat the already-satisfied commit work removed by A1. It does not perform
any Phase B documentation consolidation, Phase C tooling, or Phase D network/release work.

## 4. Scope, Sequence, and Files

| Path | Phase action | Boundary |
|------|--------------|----------|
| `.agent/rules/conventions.md` | DELETE | Exact singular path only |
| `.agent/rules/glossary.md` | DELETE | Exact singular path only |
| `TECH_DEBT.md` | MODIFY | TD-7 row only, except formatting needed for that row |
| `tasks/README.md` | MODIFY | Preserve existing TFW-4/research changes; update current status and legacy note only |

Sequence:

1. Capture the pre-existing state of protected dirty paths, especially `.agents/**` and the
   existing `tasks/README.md` diff.
2. Remove only `.agent/` and update the two trace registries.
3. Verify the narrowed Phase A outcome, historical-reference rule, protected-path integrity,
   and commit attribution before RF.

### Scope Budget

| Measure | Estimate | Limit | Result |
|---------|----------|-------|--------|
| Implementation files | 4 total | 30 | Within budget |
| New implementation files | 0 | 15 | Within budget |
| Modified implementation files | 2 | 30 | Within budget |
| Deleted implementation files | 2 (154 lines) | included in total | Within budget |
| Estimated implementation delta | <200 LOC | 3000 LOC | Within budget |
| Full lifecycle trace files | 9 maximum across HL/TS/ONB/RF/EV/review stages | 15 new files | Within budget |

No budget override or additional split is required.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Frozen Master HL including approved A5 | ✅ baseline `8485c29` |
| TFW-3 installation commit | ✅ `0fe6c67` |
| A1 restriction removing already-completed Phase A deliverables 2–3 | ✅ applied |
| A2 historical-reference rule | ✅ approved and applied |
| A3 protection of `.agents/` (plural) | ✅ applied |
| Owner pre-authorization for a strictly derived Phase A TS | ✅; excludes Phase D, tag, release, push |
| Network, Telegram, or owner CL presence | N/A for Phase A |

## 9. Phase Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| `.agents/` is mistaken for `.agent/` | Medium | High — live Codex adapter is lost | Resolve exact literal paths; compare `.agents/**` with the pre-execution snapshot |
| Existing user changes in `tasks/README.md` are overwritten | Medium | High — research trace/status is lost | Preserve the current hunk and make only the derived note/status edit |
| Historical mentions are removed to satisfy an obsolete DoD reading | Medium | Medium — trace discipline is violated | Apply amended DoD 3: reject only live-instruction references |
| Phase B–D work leaks into the cleanup | Medium | Medium — sequencing and reviewability break | Enforce the four-path implementation scope and Master HL P1 |
| A commit is backdated or narrates work not performed in this phase | Low | High — honesty contract fails | Use actual commit metadata and describe only the Phase A delta |

---

*Phase HL — TFW-4 / Phase A: Baseline & Cleanup | 2026-08-26*

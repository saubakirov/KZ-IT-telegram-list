---
description: TFW Resume — locate task, build status matrix, decide next phase
---

# TFW Resume — Phase Status Bootstrap

> **Role:** Coordinator (new or returning)
> **Output:** Phase status matrix + recommendation for next phase
> **When to use:** Starting a new session for a multi-phase task, or returning after a break

> **🔒 ROLE LOCK: COORDINATOR**
> This workflow runs in Coordinator mode ONLY.
> Permitted actions: read artifacts, build status matrix, write Phase HL + TS.
> Forbidden actions: execution, writing ONB, writing RF, writing code.

> Context loading: verify conventions.md §10 core context is loaded before proceeding.

## Phase 1: Locate Task

1. User specifies task folder path (e.g. `tasks/PROJ-3__admin_ui/`)
2. List the task folder contents — identify Master HL, Master TS, and all phase artifacts
3. Read **Master HL** — extract:
   - Vision (section 1) — one-liner
   - Phase list (section 4) — all planned phases with priorities
   - Design principles (section 7) — non-negotiable rules
   - Strategic Insights (section 11) — check for gaps from previous session

4. Read **Master TS** (if exists) — extract:
   - Phase definitions and scope budgets
   - Quality contract (anti-patterns, style rules)
   - Verification plan

## Phase 2: Build Status Matrix

5. Scan folder for `HL__Phase*`, `TS__Phase*`, `ONB__Phase*`, `RF__Phase*`, `REVIEW__Phase*` files
6. Build matrix and present:

```markdown
## Phase Status Matrix

| Phase | Description | HL | TS | ONB | RF | REVIEW | Status |
|-------|-------------|----|----|-----|----|----|--------|
| A | Backend: API endpoints | ✅ | ✅ | ✅ | ✅ | ✅ APPROVED | ✅ Done |
| B | Frontend: components | ❌ | ❌ | ❌ | ❌ | ❌ | ⬜ Next |
| C | Integration tests | ❌ | ❌ | ❌ | ❌ | ❌ | ⬜ TODO |
```

7. If the last completed phase has a REVIEW file — read it, extract:
   - Verdict (APPROVED / REVISE / REJECT)
   - Key lessons or issues found
   - Tech debt items collected
8. If a REVISE verdict exists for any phase — flag it as needing re-execution
9. Read `TECH_DEBT.md` — extract accumulated items across phases

## Phase 3: Report & Decide

10. Present structured status report to user:

```markdown
## Resume Report — {PREFIX}-{N}

**Task**: [title from Master HL]
**Progress**: X of Y phases complete

### Completed
- Phase A: [one-line summary] ✅ [REVIEW verdict]
- Phase B: [one-line summary] ✅ [REVIEW verdict]

### Lessons from Last Phase
- [extracted from REVIEW]

### Tech Debt Accumulated
- [summary from TECH_DEBT.md]

### Next Phase
**Phase C**: [description from Master HL]
- Scope: [N files, brief]
- Dependencies: [any blockers from previous phases]
```

11. Ask user: **"Start planning Phase C?"** or **"Which phase to work on?"**

## After User Confirms

12. Use [plan workflow](plan.md) Phase 4 flow (large task path) to write HL+TS for the chosen phase
13. Present HL+TS for user approval
14. After approval → use [handoff workflow](handoff.md) to delegate to executor agent
15. After RF → use [review workflow](review.md) (`/tfw-review`) for review

## Anti-patterns

- Skip reading Master HL/TS and jump straight to writing phase TS
- Read all RF files in full (only read REVIEW summaries — RF is for executors)
- Start planning without showing the status matrix first
- Assume phase order is fixed — user may want to skip or reorder
- Ignore TECH_DEBT.md items from previous phases
- Ignore accumulated tech debt when planning next phase scope

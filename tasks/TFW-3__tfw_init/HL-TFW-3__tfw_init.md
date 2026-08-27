# HL — TFW-3: Initialize TFW 1.3.0

> **Date**: 2026-08-26
> **Author**: Claude Opus 5 (Coordinator) for saubakirov
> **Status**: ✅ DONE
> **Contract**: 🔒 FROZEN — approved by saubakirov 2026-08-26
> **Frozen**: §1 · §3 · §4 · §5 · §6 · §7 — locked on owner approval
> **Free**: §2 · §7.2 · §8 · §9 · §10 · §11 — research updates these directly
> **Append-only**: §12 Amendment Log — the only channel for changing a frozen section
> **Baseline**: this file at the init commit

> **Project North Star**: `README.md § Awesome Kazakhstan IT Telegram` · `AGENTS.md § AI Role & Mission`

---

## 1. Vision 🔒 FROZEN

KZ-IT-telegram-list runs on Trace-First Workflow 1.3.0. Every future change to the catalog —
adding a community, purging dead links, restructuring categories — leaves a trace that the next
session or contributor can read: what was decided, on what evidence, and what was rejected.

**Impact:** The project stops depending on a chat session's memory. A new maintainer (human or
agent) reads `AGENTS.md` → `KNOWLEDGE.md` → the Task Board and can act correctly without asking
anyone what the rules are.

> "I should be able to hand this repo to someone else and have them not break the README."

## 2. Current State (As-Is) 🟢 FREE

The project carries an **ad-hoc pre-1.0 TFW layout**, installed by hand before the framework was
versioned. What exists:

| Artifact | State |
|----------|-------|
| `.tfw/` | **Absent** — no framework files, no version marker, no config |
| `STEPS.md` | Freeform progress log, 14 entries, last touched 2026-01-30 |
| `TASK.md` | "Active Task: None" + completed list + a 3-item backlog (TFW-03/04/05) |
| `tasks/TFW-01_*`, `tasks/TFW-02_*` | 4 files total: HL/TS for TFW-01, HL/RF for TFW-02 |
| `.agent/rules/` | `agents.md` (duplicate of root `AGENTS.md`), `conventions.md`, `glossary.md` |
| `AGENTS.md` | Hand-written; claims "23 channels" while the data holds 18 |
| Lifecycle | None — no statuses, no roles, no review, no knowledge gate |

Consequences: no Task Board, no RES/ONB/REVIEW stages, no `KNOWLEDGE.md`, no `TECH_DEBT.md`, no
upgrade path, and two competing status systems (`STEPS.md` and `TASK.md`) that already disagree
on what "done" means.

## 3. Target State (To-Be) 🔒 FROZEN

TFW 1.3.0 installed from the `v1.3.0` tag of `saubakirov/trace-first-starter`, configured for this
project, with the Claude Code adapter attached and legacy artifacts migrated and removed.

| Aspect | As-Is | To-Be |
|--------|-------|-------|
| Framework | none | `.tfw/` at 1.3.0, pinned in `project_config.yaml` |
| Status tracking | `STEPS.md` + `TASK.md` (conflicting) | Task Board in `tasks/README.md` |
| Lifecycle | none | `HL_DRAFT → RES → TS_DRAFT → ONB → RF → REV → KNW → DONE` |
| Commands | none | 12 `/tfw-*` slash commands |
| Knowledge | none | `KNOWLEDGE.md` + `TECH_DEBT.md` + `knowledge_state.yaml` |
| Upgrade path | none | `/tfw-update` against pinned upstream |

### 3.1 Result Visualization

The repo root after init:

```
KZ-IT-telegram-list/
├── .tfw/                     ← 60 files, VERSION = 1.3.0
│   ├── VERSION  CHANGELOG.md  README.md
│   ├── conventions.md  glossary.md  quickstart.md
│   ├── project_config.yaml   ← task_prefix: TFW, initial_seq: 3, version: 1.3.0
│   ├── knowledge_state.yaml  ← last_consolidation_seq: 0  (clean, from template)
│   └── templates/  workflows/  adapters/
├── .claude/commands/         ← tfw-plan.md, tfw-handoff.md, … 12 commands
├── CLAUDE.md                 ← adapter, filled with real project values
├── AGENTS.md                 ← rewritten: roles, generation contract, corrected counts
├── KNOWLEDGE.md              ← P1-P4 principles, D1-D7 decisions, architecture map
├── TECH_DEBT.md              ← tracked debt items
├── tasks/
│   ├── README.md             ← Task Board  ◄── linked from generated README.md
│   ├── TFW-01_…/  TFW-02_…/  ← legacy traces, preserved untouched
│   └── TFW-3__tfw_init/      ← HL · RES · RF   (this task)
├── data/  scripts/  README.md   ← untouched product
└── (deleted: STEPS.md, TASK.md, .agent/rules/agents.md)
```

The Task Board a maintainer opens:

| ID | Task | Status | HL | RES | TS | RF |
|----|------|--------|----|-----|----|----|
| TFW-01 | Awesome List restructure | ✅ DONE | ✅ | — | ✅ | — |
| TFW-02 | Enhanced validation & cleanup | ✅ DONE | ✅ | — | — | ✅ |
| TFW-3 | Initialize TFW 1.3.0 | ✅ DONE | ✅ | ✅ | — | ✅ |

## 4. Scope 🔒 FROZEN

**In scope:** installing `.tfw/` from tag v1.3.0; filling `project_config.yaml`; resetting
`knowledge_state.yaml` from template; the Claude Code adapter (`CLAUDE.md` + `.claude/commands/`);
rewriting `AGENTS.md`; creating `KNOWLEDGE.md`, `TECH_DEBT.md`, `tasks/README.md`,
`.user_preferences.md`; `.gitignore` entries; migrating and deleting `STEPS.md` / `TASK.md`; one
change to `scripts/generate_readme.py` making the Task Board reachable from `README.md`.

**Out of scope:** any change to `data/communities.json`; any change to catalog content; the
Antigravity, Cursor and Codex adapters; renaming legacy `TFW-01`/`TFW-02` folders; acting on the
legacy backlog items TFW-03/04/05.

## 5. Deliverables 🔒 FROZEN

1. `.tfw/` at version 1.3.0, sourced from the tag, config filled for this project
2. Working `/tfw-*` slash commands for Claude Code
3. `AGENTS.md`, `KNOWLEDGE.md`, `TECH_DEBT.md` reflecting the real project
4. Task Board at `tasks/README.md`, durable against README regeneration
5. Legacy `STEPS.md` / `TASK.md` content migrated, files removed
6. This task's trace: HL, RES, RF

## 6. Success Criteria 🔒 FROZEN

- `.tfw/VERSION` reads `1.3.0` and `tfw.version` in `project_config.yaml` matches it
- `initial_seq: 3` — the next task is TFW-4; legacy TFW-01/TFW-02 untouched
- All 12 `.claude/commands/tfw-*.md` present
- `knowledge_state.yaml` has `last_consolidation_seq: 0` (from template, not upstream's history)
- `python scripts/validate_schema.py` passes; `generate_readme.py` reproduces `README.md` with
  **zero diff to catalog content** and the Task Board link present
- No `STEPS.md`, no `TASK.md`, and no board content living in generated `README.md`

## 7. Principles 🔒 FROZEN

1. **Product data is untouchable** — init changes process files only. `data/communities.json` and
   the catalog body of `README.md` end byte-identical to how they started.
2. **Version comes from the tag** — files are extracted from `v1.3.0`, not from the upstream
   working tree, which sits ahead of the tag on unreleased commits.
3. **State is never inherited** — `knowledge_state.yaml` comes from `.tfw/templates/`, never from
   upstream, or this project inherits the starter's consolidation history.
4. **Traces are preserved, not tidied** — legacy TFW-01/TFW-02 folders stay exactly as they are,
   including their non-conforming zero-padded IDs.
5. **Nothing durable goes in a generated file** — `README.md` is output; anything that must
   survive belongs in a source file or in the generator.

### 7.2 Knowledge Citations 🟢 FREE

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| 1 | `.tfw/workflows/init.md` | Phase 0 full-init vs adapter-repair detection | `.tfw/` absent → full init is the correct branch |
| 2 | `.tfw/workflows/init.md` § Anti-patterns | "copies `knowledge_state.yaml` directly from upstream" | Drove Principle 3 |
| 3 | `.tfw/conventions.md` §4 | Artifact naming `HL-{PREFIX}-{N}__{title}.md` | Names every file in this task folder |
| 4 | `.tfw/conventions.md` §5 | Task Board row must link the task folder | Board format in `tasks/README.md` |

## 8. Dependencies 🟢 FREE

| Dependency | Status |
|------------|--------|
| Local clone of `trace-first-starter` with tag `v1.3.0` at `D:/projects/research/steps-framework` | ✅ |
| Owner decisions: prefix, adapter, content language, legacy handling | ✅ 2026-08-26 |
| Python 3.10+ available to run the validators | ✅ |

## 9. Risks 🟢 FREE

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Task Board written into `README.md` is destroyed by `generate_readme.py` | High | High | Board lives in `tasks/README.md`; generator emits the link (D7) |
| `knowledge_state.yaml` copied from upstream carries the starter's consolidation history, breaking the knowledge gate | High | Medium | Copy from `.tfw/templates/` after extraction (Principle 3) |
| Extracting from the upstream working tree instead of the tag installs an unreleased version | Medium | Medium | `git archive v1.3.0` — tag-pinned (Principle 2) |
| Rewriting `AGENTS.md` loses project-specific rules | Medium | Medium | Old content read in full and folded into the new file before replacing |
| Regenerating `README.md` alters catalog content | Low | High | Byte-compare the catalog region before and after |

## 10. RESEARCH Case 🟢 FREE

### Blind Spots

- Whether `README.md` is safe to append to, or whether it is a build artifact
- Whether the existing `.agent/rules/` files are TFW-generated (replaceable) or project-authored
  (must be preserved)
- Whether the legacy `TFW-01`/`TFW-02` IDs collide with a fresh `initial_seq: 1`
- Whether the counts stated in the docs match the data

### Hypotheses

| # | Hypothesis | Status |
|---|-----------|--------|
| H1 | `README.md` is generated and cannot hold durable content | ✅ confirmed |
| H2 | `.agent/rules/` is project-authored, not TFW-generated | ✅ confirmed (with one exception) |
| H3 | Legacy task IDs collide with a default `initial_seq: 1` | ✅ confirmed |
| H4 | Documented community counts match `data/communities.json` | ❌ refuted |

### Risks of Not Researching

A Task Board appended to `README.md` would look correct and vanish on the next data update — the
failure would surface weeks later as "the board disappeared", with no trace of why.

### Proposed RESEARCH Focus

1. **Gather**: how `README.md` is produced and what owns each of its regions
2. **Extract**: which existing files are project state and which are framework artifacts
3. **Challenge**: does any documented fact contradict the data?

### Why Not Just...?

- Why not run `/tfw-update`? — Update is defined as a diff between a recorded version and a target
  version. With no `.tfw/` and no `tfw.version`, there is no baseline to diff. Init is the correct
  entry point; see RES § Decision D-1.
- Why not copy the upstream working tree? — It sits ahead of `v1.3.0` on unreleased commits.
- Why not start a fresh prefix at `initial_seq: 1`? — `TFW-1` would collide with the legacy
  `TFW-01` folder in every board link.

## 11. Strategic Insights 🟢 FREE

1. **The upgrade wasn't an upgrade.** The request was "do tfw-update", but update requires a
   recorded version to diff against. The pre-1.0 layout here was a *convention imitation*, not an
   installation — which is why it drifted (23 vs 18 channels) with nothing to catch it.
2. **Generated files are a trap for process tooling.** The init workflow says "create Task Board in
   README.md". That instruction assumes a hand-maintained README. Any framework that writes into a
   project's README needs to establish who owns that file first.
3. **Two status files means zero status.** `STEPS.md` and `TASK.md` both claimed to track state and
   had diverged. A single board is not tidier — it is the only version that can be *detectably*
   wrong.

## 12. Amendment Log

| # | Date | Target § | Proposal | Evidence | Verdict |
|---|------|----------|----------|----------|---------|
| A1 | 2026-08-26 | §4 Scope | Add one change to `scripts/generate_readme.py` emitting a Task Board link | H1 confirmed: `generate_readme.py` writes `README.md` end-to-end, so §6's "Task Board reachable from README" is unreachable without a generator change | ✅ APPROVED — owner selected "Migrate, then remove", which requires the board to remain findable |

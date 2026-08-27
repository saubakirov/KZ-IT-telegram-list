# RES — TFW-3: Initialize TFW 1.3.0

> **Date**: 2026-08-26
> **Author**: Claude Opus 5 (Researcher)
> **Status**: ✅ Complete
> **Parent HL**: [HL-TFW-3](HL-TFW-3__tfw_init.md)
> **Mode**: Pipeline (within TFW-3)
> **Iterations**: 1 (single pass — all four hypotheses closed on direct file evidence, no
> open threads carried forward)

---

## Research Context

Before installing TFW 1.3.0 we needed to know what the project already is: what the existing
"TFW-looking" files actually are, which files are safe to overwrite, whether `README.md` can hold
durable content, and whether the documentation's claims about the catalog are true. The install
plan depends on all four answers.

## Briefing

**Question:** What is the real current state of KZ-IT-telegram-list, and which install path —
`tfw-update` or `tfw-init` — is applicable?

**Scope:** the project's own files plus the `v1.3.0` tag of the upstream starter.
**Excluded:** the catalog data itself (out of scope per HL §4).

## Gather — What Was Read

| Source | What it gave |
|--------|--------------|
| `d:/projects/KZ-IT-telegram-list` file tree | No `.tfw/`; `STEPS.md`, `TASK.md`, `.agent/rules/` present |
| `scripts/generate_readme.py` | Full generation logic, `main()` write mode |
| `data/communities.json` | Real counts via `json.load` |
| `AGENTS.md`, `.agent/rules/*` | Existing conventions, glossary, agent brief |
| `tasks/TFW-01_*`, `tasks/TFW-02_*` | Legacy trace shape and ID format |
| Upstream `git tag -l`, `git ls-tree v1.3.0` | Tag exists; 60 files under `.tfw/`; 12 `.claude/commands/` |
| Upstream `.tfw/workflows/update.md` @ v1.3.0 | Update's prerequisites |
| Upstream `.tfw/workflows/init.md` @ v1.3.0 | Init phases and anti-patterns |
| Upstream `.tfw/templates/project_config.yaml` | Field-by-field PROJECT vs FRAMEWORK ownership |

## Extract — Findings

### F1 — `README.md` is a build artifact, not a document

`scripts/generate_readme.py` `main()` opens `README.md` with mode `"w"` and writes the return
value of `generate_readme(data)`, which composes the entire file from scratch: header, badges,
stats line, TOC, Groups, Channels, Bots, Contributing, License. There is no read of the existing
file, no marker block, no preserved region.

**Consequence:** any content added to `README.md` by hand — including a Task Board — is destroyed
by the next `python scripts/generate_readme.py`. Content that must persist has to be emitted by
the generator.

### F2 — `tfw-update` has no baseline in this project

`.tfw/workflows/update.md` § Prerequisites, step 1: *"Read project's `.tfw/project_config.yaml` →
`tfw.version` (current) and `tfw.upstream` (source URL)"*. Step 1 of the workflow body then compares
current against target and stops if equal.

Neither `.tfw/` nor `project_config.yaml` exists here, so there is no `tfw.version` to read and
nothing to diff. Update is structurally inapplicable.

`.tfw/workflows/init.md` Phase 0 defines the branch directly: **full init** when `.tfw/` is newly
copied and the project has no configured Task Board or TFW task traces; **adapter attach/repair**
when `.tfw/` exists with a board and traces. This project has task folders but no `.tfw/` and no
board — the framework was never installed, only imitated.

### F3 — The existing layout is a pre-1.0 imitation, not an installation

`AGENTS.md` states *"Based on https://github.com/saubakirov/trace-first-starter"*. The project
borrowed vocabulary (HL, TS, RF, CL/AG modes, the Summary line) without the framework:

| TFW 1.3.0 element | Present here |
|---|---|
| `.tfw/` framework files | ❌ |
| Version marker / config | ❌ |
| Lifecycle statuses | ❌ (STEPS.md uses freeform `Stage=Planning/Implementation/Testing`) |
| Roles + role locks | ❌ (only Human/AI split) |
| RES, ONB, REVIEW stages | ❌ (only HL, TS, RF) |
| Task Board | ❌ |
| KNOWLEDGE.md / TECH_DEBT.md | ❌ |
| Knowledge gate | ❌ |

### F4 — Two status systems, already diverged

`STEPS.md` (append-only log, 14 entries) and `TASK.md` (active task + completed + backlog) both
claim to track state. Neither references the other. `STEPS.md` ends TFW-02 with
`Status/Problem=... Final: 40 groups, 18 channels, 5 bots`; `TASK.md` records the same. But
`AGENTS.md` — the file an agent reads first — says **"23 channels"**.

### F5 — Documented counts contradict the data (H4 refuted)

```
python -c "import json; d=json.load(open('data/communities.json',encoding='utf-8')); ..."
→ groups 40  channels 18  bots 5  categories 18
```

| Source | Groups | Channels | Bots |
|--------|--------|----------|------|
| `data/communities.json` (truth) | 40 | **18** | 5 |
| `README.md` (generated) | 40 | **18** | 5 |
| `STEPS.md` / `TASK.md` | 40 | **18** | 5 |
| `AGENTS.md` | 40 | **23** ❌ | 5 |

The generated README is correct because it derives its stats from the data. The hand-written
`AGENTS.md` is wrong and nothing checks it. This is F1's lesson inverted: hand-maintained copies
of derived facts drift silently.

### F6 — `.agent/rules/` is project-authored, with one duplicate (H2 confirmed, qualified)

| File | Verdict |
|------|---------|
| `conventions.md` | Project-authored — project structure, JSON entry format, inclusion criteria, categories. **Preserve.** |
| `glossary.md` | Project-authored — Telegram terms, KZ-specific terms (TSARKA, 1C), category slugs. **Preserve.** |
| `agents.md` | Duplicate of root `AGENTS.md`. Two copies of the agent brief that must be edited in lockstep — F5's failure mode waiting to repeat. **Remove.** |

Neither surviving file matches the upstream Antigravity adapter's rules. They are project content
that happens to live under `.agent/`.

### F7 — Legacy IDs collide with a default `initial_seq` (H3 confirmed)

Existing folders are `tasks/TFW-01_awesome_list_restructure/` and
`tasks/TFW-02_enhanced_validation/`. `.tfw/conventions.md` §4 specifies unpadded
`tasks/{PREFIX}-{N}__{title}/`. With `initial_seq: 1` and prefix `TFW`, the first new task is
`TFW-1` — a distinct folder from `TFW-01` but an ambiguous board label, and `TFW-1`/`TFW-01` read
as the same task to a human scanning the list.

The legacy artifact filenames also deviate: `HL__TFW-01__…` (double underscore) versus the
convention's `HL-{PREFIX}-{N}__…` (single hyphen).

### F8 — `project_config.yaml` ownership is explicit

The template annotates every field `← PROJECT: set during init` or `← FRAMEWORK: updated by
tfw-update`. PROJECT: `project.*`, `task_prefix`, `initial_seq`, `content_language`, `build.*`.
FRAMEWORK: `version`, `upstream`, `templates`, `workflows`, `statuses`, `scope_budgets`,
`research`, `review`, `knowledge`. This is the contract the *next* `/tfw-update` will honour, so
project values must go in PROJECT fields only.

### F9 — Upstream working tree is ahead of the tag

`git log -1 v1.3.0` → `9289a3e` (2026-08-18, "release v1.3.0"). Upstream `HEAD` carries later
unreleased commits (TFW-55, TFW-60, TFW-61 work). Copying the working tree would install an
unreleased state; `git archive v1.3.0` pins the requested version.

### F10 — `knowledge_state.yaml` must come from the template

`.tfw/workflows/init.md` § Anti-patterns names this explicitly: *"Agent copies
`knowledge_state.yaml` directly from upstream instead of from template (inherits upstream's
consolidation history — breaks knowledge gate)."* Extracting `.tfw/` wholesale from the tag brings
upstream's populated `knowledge_state.yaml` and its own `project_config.yaml` along with it — both
must be overwritten from `.tfw/templates/` after extraction.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | `README.md` is generated and cannot hold durable content | open | ✅ confirmed | F1 — `main()` opens `"w"`, composes whole file |
| H2 | `.agent/rules/` is project-authored, not TFW-generated | open | ✅ confirmed (qualified) | F6 — 2 of 3 preserve; `agents.md` is a duplicate |
| H3 | Legacy task IDs collide with a default `initial_seq: 1` | open | ✅ confirmed | F7 — `TFW-1` vs `TFW-01` |
| H4 | Documented community counts match the data | open | ❌ **refuted** | F5 — `AGENTS.md` says 23 channels; data has 18 |

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D-1 | Run **full init**, not `tfw-update` | F2 — update requires a recorded `tfw.version` to diff; none exists. Init Phase 0's full-init branch matches this project exactly |
| D-2 | Extract from `git archive v1.3.0`, not the working tree | F9 — the tree is ahead of the tag on unreleased commits |
| D-3 | Overwrite `project_config.yaml` and `knowledge_state.yaml` from `.tfw/templates/` after extraction | F10 — otherwise the project inherits upstream's config and consolidation history |
| D-4 | Task Board in `tasks/README.md`; generator emits a link to it | F1 — a board in `README.md` cannot survive regeneration |
| D-5 | `initial_seq: 3`, prefix `TFW` | F7 + owner ruling — avoids the `TFW-1`/`TFW-01` collision while preserving legacy traces unrenamed |
| D-6 | Preserve `.agent/rules/conventions.md` and `glossary.md`; delete `.agent/rules/agents.md` | F6 — the first two are project knowledge, the third is a drift-prone duplicate |
| D-7 | Correct the channel count in the new `AGENTS.md` and stop restating derived counts | F5 — hand-copied derived facts drift |
| D-8 | Record the ID-format inconsistency as tech debt rather than renaming legacy folders | HL §7 Principle 4 — renaming rewrites history; the inconsistency is real and belongs on the ledger |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Keep prefix `TFW` or switch to a project-specific one? | ✅ closed | Owner: keep `TFW` (2026-08-26) |
| Q2 | Which adapters to install? | ✅ closed | Owner: Claude Code only |
| Q3 | Artifact content language? | ✅ closed | Owner: English (`content_language: en`) |
| Q4 | Fate of `STEPS.md` / `TASK.md`? | ✅ closed | Owner: migrate, then remove |
| Q5 | Are the legacy backlog items TFW-03/04/05 still wanted? | 🟡 open | Carried to `TECH_DEBT.md` — not decided during init |
| Q6 | Are the 2026-01-30 `last_verified` dates still valid? | 🟡 open | Requires a network run of `validate_links.py`; out of scope here |

## HL Update Recommendations

### Refinements (free sections — coordinator applies directly)

| # | Target § | Refinement |
|---|----------|------------|
| R1 | §2 Current State | Populate the As-Is table from F3/F4/F6 — the layout is an imitation, not an install |
| R2 | §9 Risks | Add the `knowledge_state.yaml` inheritance risk (F10) and the tag-vs-tree risk (F9) |
| R3 | §10 Hypotheses | Record H1-H3 confirmed, H4 refuted |
| R4 | §11 Strategic Insights | Record the "generated files are a trap for process tooling" insight (F1) |

### Amendment Proposals (frozen sections — owner verdict required)

| # | Target § | Proposal | Evidence | Cost | Alternative considered |
|---|----------|----------|----------|------|------------------------|
| A1 | §4 Scope | Permit one change to `scripts/generate_readme.py` to emit a Task Board link | F1 — §6 requires the board reachable from `README.md`; the generator owns that file entirely | ~6 lines in one function | Leave the board unlinked and rely on maintainers finding `tasks/README.md` — rejected: an unfindable board is an unused board |

> Filed as HL §12 row A1. Verdict: ✅ APPROVED by owner.

## Iteration Status

- **Gaps closed:** all four hypotheses resolved on direct file evidence
- **Open threads:** Q5 (legacy backlog relevance), Q6 (link freshness) — both deferred to
  `TECH_DEBT.md`, neither blocks the install
- **Recommendation:** ✅ **SUFFICIENT** — proceed to execution

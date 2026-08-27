# RF — TFW-3: Initialize TFW 1.3.0

> **Date**: 2026-08-26
> **Author**: Claude Opus 5 (Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-3](HL-TFW-3__tfw_init.md)
> **RES**: [RES TFW-3](RES__TFW-3__tfw_init.md)
> **TS**: none — init workflow (`.tfw/workflows/init.md`) served as the specification

---

## 1. What Was Done

Installed Trace-First Workflow 1.3.0 from the `v1.3.0` tag of
`saubakirov/trace-first-starter`, configured it for this project, attached the Claude Code
adapter, and migrated the pre-1.0 ad-hoc layout onto it.

### New Files

| File | Description |
|------|-------------|
| `.tfw/` (60 files) | Framework at 1.3.0 — `VERSION`, `CHANGELOG.md`, `README.md`, `conventions.md`, `glossary.md`, `quickstart.md`, `compilable_contract.md`, `templates/`, `workflows/`, `adapters/` |
| `.tfw/project_config.yaml` | From `.tfw/templates/`, filled: prefix `TFW`, `initial_seq: 3`, `version: 1.3.0`, `content_language: en`, `build.*`, `stack.*` |
| `.tfw/knowledge_state.yaml` | From `.tfw/templates/` — clean state, `last_consolidation_seq: 0` |
| `.claude/commands/tfw-*.md` (12) | Slash-command adapters: `plan`, `research`, `handoff`, `review`, `resume`, `docs`, `knowledge`, `task`, `config`, `release`, `init`, `update` |
| `CLAUDE.md` | Claude Code adapter from `.tfw/adapters/claude-code/CLAUDE.md.template`, filled with real project values + the generation contract |
| `KNOWLEDGE.md` | Knowledge index: 4 principles, 7 architecture decisions (D1-D7), component map, data flow, legacy table |
| `TECH_DEBT.md` | 8 tracked items (TD-1…TD-8) + 3 resolved by this task |
| `tasks/README.md` | Task Board + lifecycle diagram + migrated backlog |
| `tasks/TFW-3__tfw_init/HL-TFW-3__tfw_init.md` | This task's HL, contract frozen, amendment A1 logged and approved |
| `tasks/TFW-3__tfw_init/RES__TFW-3__tfw_init.md` | Research: findings F1-F10, decisions D-1…D-8, hypotheses H1-H4 |
| `tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md` | This file |
| `.user_preferences.md` | Personal preferences file (gitignored) |

### Modified Files

| File | Changes |
|------|---------|
| `AGENTS.md` | Rewritten for TFW 1.3.0: role/mission, TFW role table with locks, repository map, generation contract, change procedure, execution modes. **Corrected the channel count 23 → 18.** Project-specific rules from the old version preserved (inclusion criteria, JSON format, quality standards) |
| `scripts/generate_readme.py` | Added a `## Project Workflow` section and its TOC entry — links to the Task Board, KNOWLEDGE.md, AGENTS.md, plus a "this file is generated" warning. ~18 lines across two functions. Amendment A1 |
| `README.md` | Regenerated. Gained the TOC entry and the Project Workflow section; **catalog content byte-identical** |
| `.gitignore` | Added `.tfw/.upstream/`, `.user_preferences.md`, `*.local.md`, `__pycache__/`, `*.pyc`, `.pytest_cache/` |

### Deleted Files

| File | Rationale |
|------|-----------|
| `STEPS.md` | Freeform progress log superseded by task traces + Task Board. 14 entries migrated: TFW-01/TFW-02 rows on the board, decisions into `KNOWLEDGE.md` D1-D5 |
| `TASK.md` | Active-task + backlog file superseded by the Task Board. Backlog (TFW-03/04/05) migrated to `tasks/README.md` § Backlog and `TECH_DEBT.md` TD-3/TD-4/TD-8 |
| `.agent/rules/agents.md` | Byte-duplicate of root `AGENTS.md` — a drift-prone second copy (RES F6) |

### Deliberately Untouched

`data/communities.json`, the catalog body of `README.md`, `CONTRIBUTING.md`, `LICENSE`,
`.agent/rules/conventions.md`, `.agent/rules/glossary.md`, `tasks/TFW-01_*`, `tasks/TFW-02_*`.

## 2. Key Decisions

1. **Full init, not `tfw-update`** (RES D-1). The request named `tfw-update`, but
   `.tfw/workflows/update.md` requires `.tfw/project_config.yaml` → `tfw.version` as its diff
   baseline. Neither the file nor the directory existed. `.tfw/workflows/init.md` Phase 0 defines
   exactly this case as full init. The pre-existing "TFW-looking" files were vocabulary borrowed
   from the starter, not an installation. `/tfw-update` is now the correct command for the *next*
   upgrade, and works because `tfw.version: "1.3.0"` and `tfw.upstream` are recorded.
2. **Tag-pinned extraction** (RES D-2). `git archive v1.3.0 | tar -x` rather than copying the
   upstream working tree, which sits ahead of the tag on unreleased TFW-55/60/61 commits.
3. **`project_config.yaml` and `knowledge_state.yaml` re-copied from `.tfw/templates/` after
   extraction** (RES D-3). Extracting `.tfw/` wholesale from the tag brings the starter's *own*
   config and its populated consolidation history. `init.md` § Anti-patterns names inheriting
   that history as a way to break the knowledge gate.
4. **Task Board in `tasks/README.md`, not `README.md`** (RES D-4, amendment A1). `README.md` is
   fully overwritten by `generate_readme.py`; a board placed there would vanish on the next data
   update. The generator now emits a link to the board, so the board is reachable from README and
   survives regeneration. This departs from `init.md` Phase 2 step 4, which assumes a
   hand-maintained README.
5. **`initial_seq: 3` with prefix `TFW`** (RES D-5, owner ruling). Preserves legacy TFW-01/TFW-02
   without renaming, while avoiding the `TFW-1`/`TFW-01` ambiguity a default seq would create.
6. **Corrected the channel count and stopped restating derived facts** (RES D-7). `AGENTS.md`
   said 23 channels; the data holds 18. The new `AGENTS.md` states the counts once and marks them
   as derived from the data file.
7. **Legacy ID inconsistency recorded as accepted debt, not fixed** (RES D-8). Renaming trace
   folders for cosmetic consistency rewrites history — HL §7 Principle 4.

## 3. Acceptance Criteria

Against HL §6:

- [x] `.tfw/VERSION` reads `1.3.0` and `tfw.version` in `project_config.yaml` matches
- [x] `initial_seq: 3`; legacy TFW-01/TFW-02 folders untouched
- [x] All 12 `.claude/commands/tfw-*.md` present
- [x] `knowledge_state.yaml` has `last_consolidation_seq: 0`
- [x] `validate_schema.py` passes; `generate_readme.py` reproduces `README.md` with zero diff to
      catalog content and the Task Board link present
- [x] No `STEPS.md`, no `TASK.md`, no board content in generated `README.md`

Against `init.md` Phase 5 checklist:

- [x] `.tfw/` exists with all core files
- [x] `project_config.yaml` has correct project values
- [x] Tool adapter in place and configured (Claude Code)
- [x] Slash commands copied
- [x] Root files exist: `README.md` (links the Task Board), `AGENTS.md`
- [x] `tasks/` exists with TFW-3
- [x] `KNOWLEDGE.md` created
- [x] TFW-3 has a RES file from RESEARCH
- [x] `tfw.version` matches `.tfw/VERSION`
- [x] Codex commands — N/A, adapter not selected

## 4. Verification

| Check | Command | Result |
|-------|---------|--------|
| Lint | `python scripts/validate_schema.py` | ✅ 40 groups, 18 channels, 5 bots, 18 categories, **0 errors** |
| Verify | `python scripts/generate_readme.py` | ✅ Regenerated; 40/18/5 |
| Regression | `diff README.before.md README.md` | ✅ Only the 2 intended additions (TOC entry + Project Workflow section); **0 changes to catalog content** |
| Version | `cat .tfw/VERSION` vs `grep version .tfw/project_config.yaml` | ✅ `1.3.0` == `"1.3.0"` |
| Framework files | `find .tfw -type f \| wc -l` | ✅ 60 |
| Commands | `ls .claude/commands/` | ✅ 12 |
| Knowledge state | `grep last_consolidation_seq .tfw/knowledge_state.yaml` | ✅ `0` |
| Data untouched | `git status data/` | ✅ no changes |

**Not run:** `python scripts/validate_links.py` (`build.test`). It performs live network requests
against Telegram and is CL-mode work; running it unsupervised would produce unreviewed liveness
verdicts. The staleness it would reveal is recorded as TD-2.

## 5. Evidence

No EV file — every acceptance criterion is verifiable by a single command reproduced in §4 above,
with its output. Evidence verdict: **8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A** (Codex adapter).

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `data/communities.json` | `meta.last_updated` | data-integrity | Reads `2026-01-30`; no script reads or writes it. Drifts silently on every data edit → TD-6 |
| 2 | `scripts/` | — | missing-test | No tests. `generate_readme.py` output correctness is eyeballed → TD-5 |
| 3 | `data/communities.json` | all entries | data-freshness | Every `last_verified` is `2026-01-30` → TD-2 |
| 4 | `.agent/rules/conventions.md`, `glossary.md` | — | duplication | Overlap with `AGENTS.md` and `.tfw/glossary.md`; project terms now in two places → TD-7 |
| 5 | `scripts/validate_links.py` | — | ux | No `--dry-run`; `--update` writes counts back to JSON in the same pass that checks liveness, so a throttled run can persist wrong counts |
| 6 | repo root | — | tooling | No CI; nothing validates a PR before merge → TD-3 |

## 7. Fact Candidates

> Not verified facts. Promoted only by `/tfw-knowledge` consolidation.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | Owner keeps the `TFW` prefix across the framework boundary — legacy traces are preserved rather than renormalized | Owner ruling, 2026-08-26 | High |
| 2 | process | Claude Code is the only AI tool in use for this project; Antigravity was used earlier (`.agent/rules/` residue) but is not current | Owner ruling, 2026-08-26 | High |
| 3 | domain | Conversation language is Russian; written artifacts are English. The split is deliberate — the audience is KZ/RU, the repo is public open source | Owner ruling + repo contents | High |
| 4 | domain | The list's credibility rests on verification, not size. TFW-02 chose to delete 12 dead communities rather than keep the count high | `RF TFW-02`, `STEPS.md` (retired) | Medium |

## 8. Strategic Insights

1. **"Update" and "init" are not interchangeable, and the difference is diagnostic.** Discovering
   that update had no baseline is what surfaced the real state of the project: the borrowed
   vocabulary, the drifted counts, the two competing status files. Had `.tfw/` merely been copied
   in without checking, all three would have survived the install intact.
2. **The framework's own instructions collided with this project's architecture.** `init.md` says
   to put the Task Board in `README.md`. Here that is precisely wrong. The collision is worth
   reporting upstream — a framework installing into arbitrary projects cannot assume the README is
   hand-maintained.
3. **Everything corrected in this task was a hand-maintained copy of a derived fact.** The channel
   count, the duplicated `agents.md`, the two status files, `meta.last_updated`. The project's own
   founding decision (D1: generate the README from data) is the fix it had not finished applying
   to its own process files.

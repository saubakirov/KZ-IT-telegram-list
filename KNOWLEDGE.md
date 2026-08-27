# KNOWLEDGE.md — Project Knowledge Index

> Central index of project architecture, decisions, and evolution.
> **Principle**: Index, don't duplicate — link to RF/HL files, don't copy their contents.
> Maintained via `/tfw-docs` after each REVIEW; facts consolidated via `/tfw-knowledge`.

---

## 0. Philosophy & Principles

| # | Principle | Source |
|---|-----------|--------|
| P1 | **Data is the product; README is output.** `data/communities.json` is the single source of truth. `README.md` is a build artifact, regenerated in full and never hand-edited. | [RF TFW-01](tasks/TFW-01_awesome_list_restructure/) |
| P2 | **Accuracy over coverage.** A dead link or an invented member count damages the list more than a missing entry. Unverifiable data is omitted, not estimated. | [RF TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| P3 | **Validation precedes generation.** Schema check → link check → regenerate. The order is load-bearing: generating from invalid data publishes the error. | [RF TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| P4 | **External state is Chat-Loop territory.** Link liveness and member counts come from the network, not from the model. The agent proposes; the human validates. | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |

---

## 1. Architecture Map

### Components

| Component | Description | Key Files |
|-----------|-------------|-----------|
| Data store | Single JSON document holding `meta`, `groups`, `channels`, `bots`, `categories` | `data/communities.json` |
| Schema validator | Checks structure, required fields, category membership | `scripts/validate_schema.py` |
| Link validator | Network check of `t.me/{handle}` liveness; scrapes member counts; `--update` writes counts back to JSON | `scripts/validate_links.py` |
| README generator | Renders the full Awesome List from JSON; sorts groups by category then member count | `scripts/generate_readme.py` |
| TFW framework | Workflows, templates, conventions driving all task work | `.tfw/` |
| Claude Code adapter | Slash commands `/tfw-*` bound to canonical workflows | `CLAUDE.md`, `.claude/commands/` |

### Data flow

```
data/communities.json ──► validate_schema.py ──► validate_links.py ──► generate_readme.py ──► README.md
       (edit here)            (structure)          (liveness/counts)        (render)          (artifact)
```

### Architecture Decisions

| # | Decision | Rationale | Source |
|---|----------|-----------|--------|
| D1 | JSON source of truth + generated README, rather than editing the Markdown list directly | Makes the list queryable and validatable; eliminates the drift between what is listed and what is true | [TFW-01](tasks/TFW-01_awesome_list_restructure/TS__TFW-01__awesome_list_restructure.md) |
| D2 | Three separate scripts (schema / links / generate) instead of one pipeline script | Schema validation is offline and instant; link validation is slow and network-bound. Separating them lets local edits be checked without network access | [TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| D3 | Rate limiting in `validate_links.py` | Telegram throttles rapid scraping; unthrottled runs produce false "dead link" verdicts | [TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| D4 | Categories live in the data file (`categories` map), not in code | Adding a category is a data change, not a code change; the validator reads the same map it enforces | `data/communities.json` |
| D5 | CC0 license | Maximally permissive for a community catalog; matches Awesome List norms | `LICENSE` |
| D6 | Adopt TFW 1.3.0 with prefix `TFW`, `initial_seq: 3` | Legacy traces TFW-01/TFW-02 predate the framework install; keeping the prefix preserves them without renaming history | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| D7 | Task Board lives in `tasks/README.md`, linked from generated `README.md` | `README.md` is fully overwritten by the generator — a board placed there would be destroyed. The generator emits a link instead | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| D8 | Preserve the late TFW-3 trace honestly, with current authorship dates and no reconstructed history | A late, explicit trace is verifiable; backdating would make the repository's methodology showcase false | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) |
| D9 | `AGENTS.md` is the canonical project contract; `CLAUDE.md` is a thin Claude Code adapter | A pointer is a mechanism for agreement; duplicated rules rely on habit and reproduce the drift removed in Phase A | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |
| D10 | A project release is a dated verified snapshot tagged `data-YYYY-MM-DD`, not a semantic version | Catalog readers need to know when the data was true; the catalog has no API compatibility surface | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |
| D11 | The Project North Star lives in `data/communities.json` and is rendered later as `README.md § Purpose` | The README is generated, while structured product data can be schema-enforced and rendered without a second hand-maintained copy | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |
| D12 | Dead communities are archived with `died_on` and `reason`, never deleted | The record of a community's death is catalog data; retaining it avoids repeating the historical loss tracked by TD-4 | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |

---

## 2. Key Artifacts

| Task | Title | Key Artifact | Why Important |
|------|-------|-------------|---------------|
| TFW-01 | Awesome List restructure | [TS TFW-01](tasks/TFW-01_awesome_list_restructure/TS__TFW-01__awesome_list_restructure.md) | Establishes the JSON-as-source-of-truth architecture the whole project rests on |
| TFW-02 | Enhanced validation & cleanup | [RF TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) | Establishes the validation discipline; records the first data purge (12 dead communities removed) |
| TFW-3 | TFW 1.3.0 initialization | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | Records the framework install, adapter choice, and legacy migration |
| TFW-4 Phase A | Baseline & cleanup | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) | Records the bounded removal of the obsolete singular adapter and establishes the preserved trace baseline for later TFW-4 phases |

---

## 3. Legacy & Deprecation

| Item | Status | When | Replacement | Source |
|------|--------|------|-------------|--------|
| `STEPS.md` — freeform progress log | Removed | 2026-08-26 | Task traces in `tasks/` + Task Board in `tasks/README.md` | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| `TASK.md` — current-task + backlog file | Removed | 2026-08-26 | Task Board in `tasks/README.md` | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| `.agent/rules/agents.md` — duplicate of root AGENTS.md | Removed | 2026-08-26 | Root `AGENTS.md` | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| Remaining singular `.agent/` adapter copies (`conventions.md`, `glossary.md`) | Removed | 2026-08-26 | Canonical `.tfw/` documents; Codex entry points in root `AGENTS.md` and `.agents/skills/` | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) |
| Ad-hoc pre-1.0 TFW layout (HL/TS/RF only, no lifecycle) | Superseded | 2026-08-26 | TFW 1.3.0 lifecycle `HL_DRAFT → RES → TS_DRAFT → ONB → RF → REV → KNW → DONE` | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| Task ID zero-padding (`TFW-01`) | Frozen | 2026-08-26 | Unpadded `TFW-3` onward per `.tfw/conventions.md` §4 | [TECH_DEBT.md](TECH_DEBT.md) |

---

## 4. Project Facts

> Index of verified project knowledge. Details in `knowledge/` topic files.
> Updated by `/tfw-knowledge` consolidation.

| Category | Count | Topic File |
|----------|-------|------------|

_No consolidation run yet — `last_consolidation_seq: 0`. First consolidation due after TFW-8 (`tfw.knowledge.interval: 5`)._

---

> **Maintenance**: This file is updated via the `tfw-docs` workflow after each REVIEW.
> See `.tfw/workflows/docs.md` for the update process.

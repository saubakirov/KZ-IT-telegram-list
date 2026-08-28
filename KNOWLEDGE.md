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
| Data store | Single JSON document holding the structured Project North Star, live catalog, metadata, categories, and evidence-backed archive records | `data/communities.json` |
| Schema validator | Enforces North Star, live-entry, archive, collision, and strict-date contracts; reports valid staleness without making age fatal | `scripts/validate_schema.py` |
| Link validator | Classifies Telegram responses against authoritative target identity and declared type; emits machine-readable results and exposes separate evidence-safe update/archive paths | `scripts/validate_links.py` |
| Catalog generator | Sole writer for the GitHub mirror and EN/RU/KK catalog projections; renders locale-complete UI, intent navigation, derived stats, categories, entries, and conditional archive output; provides normalized non-mutating `--check` | `scripts/generate_readme.py`, `README.md`, `index.md`, `ru/index.md`, `kk/index.md` |
| Published discovery surface | Repository-owned Jekyll layout/head logic, responsive CSS, Liquid sitemap, and reviewed preview asset publish the generated EN/RU/KK catalog with self-canonical and reciprocal hreflang, Dataset, Open Graph, and Twitter metadata | `_layouts/default.html`, `_config.yml`, `sitemap.xml`, `assets/css/catalog.css`, `assets/social-preview.svg`, `assets/social-preview.png` |
| Agent contract | Count-free canonical project rules and project-operation authority boundaries | `AGENTS.md` |
| TFW framework | Workflows, templates, conventions driving all task work | `.tfw/` |
| Task state carrier | Each task's own `status.md` is the only authority for its lifecycle, owner and outcome; a phase carries one per phase directory. Coordination events are immutable files in `journal/` | `tasks/{task}/status.md`, `tasks/{task}/journal/` |
| Portfolio view | Derived, non-authoritative index rebuilt from every task's state; also the schema validation gate (`--validate`) | `tasks/00-INDEX.md`, `docs/scripts/gen_index.py` |
| Participants | One declared profile per participant. Attribution, never authentication | `team/` |
| Claude Code adapter | Thin pointer to `AGENTS.md` plus Claude-Code-specific context loading and slash-command routing | `CLAUDE.md`, `.claude/commands/` |
| Project operations | CL contracts for catalog verification/owner triage and dated-snapshot preparation with a hard stop before tag or push | `.claude/commands/kz-stats.md`, `.claude/commands/kz-release.md` |
| CI validation | Runs schema validation and non-mutating README currency checks on pull requests and pushes to `master`; never depends on Telegram | `.github/workflows/validate.yml` |
| Release policy and catalog history | Defines dated verified snapshots and records catalog changes separately from framework releases | `RELEASE.md`, `CHANGELOG.md` |

### Data flow

```
data/communities.json
  ├──► validate_schema.py (structure + locale)
  ├──► validate_links.py (liveness/counts; evidence-safe source updates)
  └──► generate_readme.py (one renderer)
          ├──► README.md
          ├──► index.md
          ├──► ru/index.md
          └──► kk/index.md

index.md + ru/index.md + kk/index.md
  └──► Jekyll layout/head + CSS + Liquid sitemap
          └──► GitHub Pages EN/RU/KK discovery surface
```

### Operational Contracts

| Contract | Durable rule | Source |
|----------|--------------|--------|
| Telegram identity binding | When canonical, Open Graph, or primary-action identity signals exist, they must consistently bind the requested handle; conflicting authority is ambiguous. Only when no authoritative URL exists may a target-preview handle fallback bind, and declared type must still match. Description anchors are content, not identity; counts come only from the bound target preview; ambiguous, generic, or failed inputs cannot mutate catalog facts | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) · [REVIEW TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/REVIEW__phase-c__pipeline_tooling.md) |
| Generator currency | `generate_readme.py` is the only writer for `README.md`, `index.md`, `ru/index.md`, and `kk/index.md`. Its normalized UTF-8/newline `--check` is non-mutating and is the shared local, CI, and release-preparation currency gate | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) · [RF catalog discoverability Phase A](tasks/2026/20260827-132641__catalog_discoverability/phase-a/RF__phase-a__multilingual_catalog.md) |
| Offline CI | CI runs schema validation and generator currency checks only; it does not call Telegram, mutate data/README, archive entries, or perform release actions | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) |
| Project-command authority | `/kz-stats` preserves four-way owner/evidence triage; `/kz-release` validates completeness and stops before tag/push for explicit owner approval. Command definitions are not evidence that either operation ran | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) |
| Multilingual projection integrity | Every EN/RU/KK value and intent destination is explicit in the source; missing, blank, placeholder, or unknown values fail validation. One renderer writes all four projections, and a digest binds language review to exact locale bytes; any locale-content change invalidates that verdict | [REVIEW catalog discoverability Phase A](tasks/2026/20260827-132641__catalog_discoverability/phase-a/REVIEW__phase-a__multilingual_catalog.md) |
| Published discovery integrity | The public surface is the supported GitHub Pages/Jekyll build of the generated EN/RU/KK projections. Each route has one self-canonical and reciprocal `en`/`ru`/`kk`/`x-default` hreflang set; the repository-owned Liquid sitemap contains those three canonicals; Dataset and social metadata stay consistent with visible content and the reviewed preview PNG; project `robots.txt` and `llms.txt` are not emitted | [REVIEW catalog discoverability Phase B](tasks/2026/20260827-132641__catalog_discoverability/phase-b/REVIEW__phase-b__published_discovery.md) |

### Architecture Decisions

| # | Decision | Rationale | Source |
|---|----------|-----------|--------|
| D1 | JSON source of truth + generated README, rather than editing the Markdown list directly | Makes the list queryable and validatable; eliminates the drift between what is listed and what is true | [TFW-01](tasks/TFW-01_awesome_list_restructure/TS__TFW-01__awesome_list_restructure.md) |
| D2 | Three separate scripts (schema / links / generate) instead of one pipeline script | Schema validation is offline and instant; link validation is slow and network-bound. Separating them lets local edits be checked without network access | [TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| D3 | Rate limiting in `validate_links.py` | Telegram throttles rapid scraping; unthrottled runs produce false "dead link" verdicts | [TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| D4 | Categories live in the data file (`categories` map), not in code | Adding a category is a data change, not a code change; the validator reads the same map it enforces | `data/communities.json` |
| D5 | CC0 license | Maximally permissive for a community catalog; matches Awesome List norms | `LICENSE` |
| D6 | Adopt TFW 1.3.0 with prefix `TFW`, `initial_seq: 3` — **partly superseded by D17** | Legacy traces TFW-01/TFW-02 predate the framework install; keeping the prefix preserves them without renaming history. `initial_seq` was retired at TFW 2.0.0: identifiers are clock-derived and read no counter | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| D7 | Task Board lives in `tasks/README.md`, linked from generated `README.md` — **superseded by D15** | `README.md` is fully overwritten by the generator — a board placed there would be destroyed. The generator emits a link instead. The board itself was retired at TFW 2.0.0; the reasoning about generated-README fragility still holds and is why D15 keeps the file | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| D8 | Preserve the late TFW-3 trace honestly, with current authorship dates and no reconstructed history | A late, explicit trace is verifiable; backdating would make the repository's methodology showcase false | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) |
| D9 | `AGENTS.md` is the canonical project contract; `CLAUDE.md` is a thin Claude Code adapter | A pointer is a mechanism for agreement; duplicated rules rely on habit and reproduce the drift removed in Phase A | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |
| D10 | A project release is a dated verified snapshot tagged `data-YYYY-MM-DD`, not a semantic version | Catalog readers need to know when the data was true; the catalog has no API compatibility surface | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |
| D11 | The Project North Star lives in `data/communities.json` and is rendered later as `README.md § Purpose` | The README is generated, while structured product data can be schema-enforced and rendered without a second hand-maintained copy | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |
| D12 | Dead communities are archived with `died_on` and `reason`, never deleted | The record of a community's death is catalog data; retaining it avoids repeating the historical loss tracked by TD-4 | [HL TFW-4](tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) |
| D13 | Catalog freshness is reported, not enforced, by schema validation | A valid old verification date is an operational signal for a live sweep; making age fatal would block unrelated contributions. Malformed or impossible dates remain schema errors | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) |
| D14 | Project operations use the `kz-*` namespace while framework operations remain `tfw-*` | The namespace boundary keeps project-owned commands distinct from adapter content managed by `/tfw-update` | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) |
| D15 | Task state lives in each task's own `status.md`; `tasks/README.md` is kept permanently as a hand-maintained route and as the home for the backlog and legacy-trace notes | A shared table serialized every lifecycle transition through one file. The route file survives because generated `README.md` cannot hold hand-maintained content (D7's reasoning) and the derived index must not — it is rebuilt and would discard it | [.tfw/CHANGELOG.md](.tfw/CHANGELOG.md) 2.0.0 |
| D16 | TFW framework tooling lives in `docs/scripts/`, separate from project `scripts/` | `.tfw/conventions.md` and `.tfw/workflows/init.md` reference that literal path, and `gen_index.py` resolves the project root as `parents[2]` of its own file. Keeping the path leaves `.tfw/` byte-identical to upstream, so future `/tfw-update` runs stay trivial diffs | [docs/scripts/README.md](docs/scripts/README.md) |
| D17 | One task container (`task_containers: [tasks]`), and the pre-2.0.0 corpus is not renamed | The corpus already lives in `tasks/`, so no second container is needed. Renaming legacy ids into the clock grammar was declined: a trace needing a translation table has lost the property the framework exists to provide. Cost recorded as TD-12 | [.tfw/project_config.yaml](.tfw/project_config.yaml) |
| D18 | A catalog release is an evidence-complete dated snapshot: the immutable full-sweep evidence may be supplemented by exact handle rechecks, while type repairs and death archives require target-bound or owner-bound evidence before publication | The first release showed that a single HTTP shape is not enough: target identity, peer type, historical continuity, explicit archive authority, and a final exact-universe reconciliation prevent ambiguous Telegram responses from becoming catalog facts | [RF TFW-4 Phase D](tasks/TFW-4__showcase_reorg/phase-d/RF__phase-d__live_sweep_release.md) |
| D19 | Store locale/UI/intent content explicitly in `data/communities.json` and generate the GitHub mirror plus EN/RU/KK projections through one renderer with no fallback | Explicit completeness and one generation path prevent translation drift, preserve locale-invariant community facts, and allow advisory and formal language review to bind to one exact digest | [REVIEW catalog discoverability Phase A](tasks/2026/20260827-132641__catalog_discoverability/phase-a/REVIEW__phase-a__multilingual_catalog.md) |
| D20 | Publish the generated multilingual catalog through repository-owned Jekyll layout/head/CSS and a Liquid sitemap, using supported GitHub Pages capability and no project robots/llms surface | One static build keeps visible content, canonical/hreflang, Dataset, social metadata, navigation, sitemap, and preview bytes mutually verifiable without a runtime application or unsupported plugin | [REVIEW catalog discoverability Phase B](tasks/2026/20260827-132641__catalog_discoverability/phase-b/REVIEW__phase-b__published_discovery.md) |

---

## 2. Key Artifacts

| Task | Title | Key Artifact | Why Important |
|------|-------|-------------|---------------|
| TFW-01 | Awesome List restructure | [TS TFW-01](tasks/TFW-01_awesome_list_restructure/TS__TFW-01__awesome_list_restructure.md) | Establishes the JSON-as-source-of-truth architecture the whole project rests on |
| TFW-02 | Enhanced validation & cleanup | [RF TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) | Establishes the validation discipline; records the first data purge (12 dead communities removed) |
| TFW-3 | TFW 1.3.0 initialization | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | Records the framework install, adapter choice, and legacy migration |
| TFW-4 Phase A | Baseline & cleanup | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) | Records the bounded removal of the obsolete singular adapter and establishes the preserved trace baseline for later TFW-4 phases |
| TFW-4 Phase B | Contract & docs | [RF TFW-4 Phase B](tasks/TFW-4__showcase_reorg/phase-b/RF__phase-b__contract_docs.md) | Establishes the canonical agent contract, structured North Star, contributor policy, and dated-snapshot release vocabulary consumed by later phases |
| TFW-4 Phase C | Pipeline & tooling | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) | Establishes the evidence-safe Telegram classifier, generated presentation/currency contract, offline CI, and bounded project operations that Phase D may later execute |
| TFW-4 Phase D | Live sweep & first release | [RF TFW-4 Phase D](tasks/TFW-4__showcase_reorg/phase-d/RF__phase-d__live_sweep_release.md) | Records the verified 2026-08-27 catalog snapshot, exact repair/archive evidence, release commit, annotated tag, publication, and final task closure |
| Catalog discoverability Phase A | One-source multilingual catalog | [REVIEW Phase A](tasks/2026/20260827-132641__catalog_discoverability/phase-a/REVIEW__phase-a__multilingual_catalog.md) | Approves the digest-bound EN/RU/KK source, one-renderer/four-projection contract, intent navigation, and deterministic regression suite |
| Catalog discoverability Phase B | Published discovery surface | [REVIEW Phase B](tasks/2026/20260827-132641__catalog_discoverability/phase-b/REVIEW__phase-b__published_discovery.md) | Approves the deployed GitHub Pages/Jekyll routes, canonical/hreflang and Dataset/social metadata, Liquid sitemap, responsive navigation, repository preview, and exact public evidence |

---

## 3. Legacy & Deprecation

| Item | Status | When | Replacement | Source |
|------|--------|------|-------------|--------|
| Task Board table in `tasks/README.md` | Removed | 2026-08-27 | Each task's own `status.md` (authority) + derived `tasks/00-INDEX.md` (view). Captured verbatim as `tasks/BOARD-SNAPSHOT.md`; the file itself remains as a route, per D15 | [.tfw/CHANGELOG.md](.tfw/CHANGELOG.md) 2.0.0 |
| `tfw.initial_seq` sequence counter | Removed | 2026-08-27 | Clock-derived `YYYYMMDD-HHMMSS__slug` identifiers; legacy `TFW-N` still resolves | [.tfw/project_config.yaml](.tfw/project_config.yaml) |
| `STEPS.md` — freeform progress log | Removed | 2026-08-26 | Task traces in `tasks/` + Task Board in `tasks/README.md`  (board later retired at 2.0.0 — see D15) | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| `TASK.md` — current-task + backlog file | Removed | 2026-08-26 | Task Board in `tasks/README.md`  (board later retired at 2.0.0 — see D15) | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| `.agent/rules/agents.md` — duplicate of root AGENTS.md | Removed | 2026-08-26 | Root `AGENTS.md` | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| Remaining singular `.agent/` adapter copies (`conventions.md`, `glossary.md`) | Removed | 2026-08-26 | Canonical `.tfw/` documents; Codex entry points in root `AGENTS.md` and `.agents/skills/` | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) |
| Duplicated project rules in `CLAUDE.md` | Superseded | 2026-08-27 | Thin Claude Code adapter pointing to canonical `AGENTS.md` | [RF TFW-4 Phase B](tasks/TFW-4__showcase_reorg/phase-b/RF__phase-b__contract_docs.md) |
| Copied contributor reference tables, divergent validation procedure, `origin main`, and archive `TODO` | Removed | 2026-08-27 | Canonical source pointers, `master`, North Star inclusion gates, and evidence-based archive policy | [RF TFW-4 Phase B](tasks/TFW-4__showcase_reorg/phase-b/RF__phase-b__contract_docs.md) |
| HTTP-200/negative-marker liveness and page-wide member-count parsing | Superseded | 2026-08-27 | Authoritative handle/type binding, conflict-safe ambiguity, and target-preview-only counts | [REVIEW TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/REVIEW__phase-c__pipeline_tooling.md) |
| Write-mode regeneration as the only README currency check | Superseded | 2026-08-27 | Normalized non-mutating `generate_readme.py --check`, shared by local validation, CI, and release preparation | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) |
| Ad-hoc pre-1.0 TFW layout (HL/TS/RF only, no lifecycle) | Superseded | 2026-08-26 | TFW 1.3.0 lifecycle `HL_DRAFT → RES → TS_DRAFT → ONB → RF → REV → KNW → DONE` | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| Task ID zero-padding (`TFW-01`) | Frozen | 2026-08-26 | Unpadded `TFW-3` onward per `.tfw/conventions.md` §4 | [TECH_DEBT.md](TECH_DEBT.md) |

---

## 4. Project Facts

> Index of verified project knowledge. Details in `knowledge/` topic files.
> Updated by `/tfw-knowledge` consolidation.

| Category | Count | Topic File |
|----------|-------|------------|
| Domain | 2 | [knowledge/domain.md](knowledge/domain.md) |

---

> **Maintenance**: This file is updated via the `tfw-docs` workflow after each REVIEW.
> See `.tfw/workflows/docs.md` for the update process.

# TECH_DEBT.md — Known Debt & Deferred Work

> Tracked shortcuts, deferred decisions, and known inconsistencies.
> Updated via `/tfw-docs` after each REVIEW. An item leaves this file only when it is
> resolved (with a link to the RF that resolved it) or consciously accepted.

| Status | Meaning |
|--------|---------|
| 🔴 OPEN | Unresolved, no plan |
| 🟡 PLANNED | Has a task or backlog entry |
| 🟢 ACCEPTED | Deliberately not fixing; rationale recorded |
| ✅ RESOLVED | Fixed; RF linked |

---

## Open Items

| # | Item | Type | Severity | Status | Source |
|---|------|------|----------|--------|--------|
| TD-1 | Legacy tasks `TFW-01` / `TFW-02` use zero-padded IDs and `HL__`/`TS__` filenames, deviating from `.tfw/conventions.md` §4 (`TFW-3`, `HL-TFW-3__…`) | convention | Low | 🟢 ACCEPTED | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| TD-8 | Legacy backlog items (CI, `README.ru.md`, archive section) were carried from the retired `TASK.md` without re-confirming they are still wanted | scope | Low | 🟡 PLANNED | [RES TFW-3 Q5](tasks/TFW-3__tfw_init/RES__TFW-3__tfw_init.md) |
| TD-9 | TFW-4's frozen Quality Contract hardcodes commit `agent=claude-code`, while `.tfw/conventions.md` §4 derives `agent` from the acting product. A non-Claude executor must violate one source or emit misleading trace attribution | trace-attribution | Medium | 🟡 PLANNED | [REVIEW TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/REVIEW__phase-a__baseline_cleanup.md) |
| TD-11 | Claude Code adapter sources route `/tfw-research` to nonexistent `.tfw/workflows/research.md`; the live adapter is correct, but a reinstall or sync can reintroduce the broken path | adapter-routing | Medium | 🔴 OPEN | [REVIEW TFW-4 Phase B](tasks/TFW-4__showcase_reorg/phase-b/REVIEW__phase-b__contract_docs.md) |
| TD-12 | `tasks/TFW-01_awesome_list_restructure/` and `TFW-02_enhanced_validation/` are invisible to `docs/scripts/gen_index.py`: its `TASK_DIR` pattern requires a `__` separator and these use a single `_`. `tasks/00-INDEX.md` therefore files both under **Backlog — “ideas, not work in progress”**, which is false: both have real directories with completed HL/TS/RF traces. No trace is lost (both are terminal and captured verbatim in `BOARD-SNAPSHOT.md`), but a generated artifact asserts something untrue | index-accuracy | Medium | 🔴 OPEN | [TFW 2.0.0 migration](tasks/TFW-4__showcase_reorg/journal/) |
| TD-13 | The installed framework is `2.0.0-dirty`, an upstream **pre-release** cut so the update path could be exercised before `2.0.0` is claimed. Upstream ships it with TD-182 open (the Assisted edition still changes status by moving a folder, contradicting the release) and TFW-60 at `PHASES` with Phases B and C unwritten. `consolidation` is a reserved journal `kind` that is not valid yet | framework-version | Medium | 🟡 PLANNED | [.tfw/CHANGELOG.md](.tfw/CHANGELOG.md) |
| TD-14 | `docs/scripts/migrate_board.py` carries a local delta from upstream: `--board` and `--board-heading` were added because upstream hardcodes root `README.md` under `## Task Board`, while this project's board was `tasks/README.md` under `## Board`. The change is additive and upstream defaults are unchanged, but `/tfw-update` will overwrite it unless re-applied — or unless upstream accepts the options | framework-fork | Low | 🟡 PLANNED | [docs/scripts/README.md](docs/scripts/README.md) |
| TD-15 | `build.verify` runs only the catalog gates (`validate_schema.py` + `generate_readme.py`). It does not run `python docs/scripts/gen_index.py --validate`, the gate that checks every task's `status.md` and journal against the closed schema, so a malformed task state file passes the project's own verify | missing-gate | Medium | 🔴 OPEN | [.tfw/project_config.yaml](.tfw/project_config.yaml) |
| TD-16 | `team/README.md` is a tracked file in the upstream starter but lives **outside** `.tfw/`, so `/tfw-update` Step 3 and Step 6 never mention it and no template exists for it. An updating project silently gains a `team/` directory with no explanation of what it is. Copied by hand here; a future update will not refresh it | upstream-packaging | Low | 🟡 PLANNED | [team/README.md](team/README.md) |
| TD-17 | `tfw.task_containers` is a **new required decision** at 2.0.0 — it sets where new tasks are created and whether an old corpus path keeps resolving — but `update.md` names it only in the “preserve” list. Nothing in the update path presents it as a choice, so the value gets picked silently. Relocating or renaming the container is possible and was never surfaced | upstream-workflow | Medium | 🟡 PLANNED | [.tfw/project_config.yaml](.tfw/project_config.yaml) |
| TD-18 | TFW 2.0.0 is a major breaking release that retires a required artifact and moves live state, yet it ships no migration guide. `update.md` changed by exactly **one line** between 1.3.0 and 2.0.0, and the CHANGELOG's Migration section documents the upstream repository's own migration rather than a general procedure. The order of operations, the decisions to make, and the tooling's location all had to be reconstructed during the update | upstream-workflow | **High** | 🟡 PLANNED | [.tfw/CHANGELOG.md](.tfw/CHANGELOG.md) |

---

## Detail

### TD-1 — Legacy task ID format (ACCEPTED)

> **Consequence added at TFW 2.0.0 (see TD-12).** The deviation is no longer cosmetic: the
> single-underscore names are unreadable to `docs/scripts/gen_index.py`, so both tasks are
> absent from the derived portfolio index and are misreported there as backlog ideas. Renaming
> them would fix it and was declined — 2.0.0 guarantees that nothing existing is renamed, and
> TD-1 exists to keep these filenames as historical traces.


`tasks/TFW-01_awesome_list_restructure/` and `tasks/TFW-02_enhanced_validation/` predate the
framework install. Renaming them would rewrite trace history for cosmetic consistency —
HL-TFW-3 §7 Principle 4 forbids it. `initial_seq: 3` sidesteps the `TFW-1`/`TFW-01` collision.
Accepted permanently; new tasks follow the convention.

### TD-6 — `meta.last_updated` pipeline ownership (RESOLVED)

`validate_links.py --update` now writes the run date to `meta.last_updated` when it persists
observed link results. Explicit archive mutation also writes the evidence date. Phase C delivered
the ownership mechanism without running a production sweep or changing the existing production
value; Phase D remains responsible for the first observed refresh.

---

## Resolved

| # | Item | Resolved by | Date |
|---|------|-------------|------|
| TD-2 | ✅ RESOLVED — all 62 surviving live communities have positive evidence and `last_verified: 2026-08-27`; counts were persisted only when observed, with exact supplemental rechecks for repaired entries | [RF TFW-4 Phase D](tasks/TFW-4__showcase_reorg/phase-d/RF__phase-d__live_sweep_release.md) | 2026-08-27 |
| TD-4 | ✅ RESOLVED — dead-community handling now preserves complete source records in `archive` with `type`, evidence date, and owner-approved reason; the first two records were archived rather than deleted | [RF TFW-4 Phase D](tasks/TFW-4__showcase_reorg/phase-d/RF__phase-d__live_sweep_release.md) | 2026-08-27 |
| TD-10 | ✅ RESOLVED — TFW 2.0.0 retired the Task Board entirely. The managed `AGENTS.md` block and all 11 Codex `SKILL.md` copies now name the selected task's `status.md` as the state carrier; no adapter names any board. The only remaining mention is the `BOARD-SNAPSHOT.md` history row | [TFW 2.0.0 update](.tfw/CHANGELOG.md) | 2026-08-27 |
| TD-3 | ✅ RESOLVED — added offline CI for schema validation and the generator's non-mutating README-currency gate on pull requests and pushes to `master`; no remote run is claimed in Phase C | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) | 2026-08-27 |
| TD-6 | ✅ RESOLVED — `validate_links.py` owns `meta.last_updated` whenever an observed update or explicit evidence-backed archive is persisted; production remains unchanged until Phase D | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) | 2026-08-27 |
| TD-7 | ✅ RESOLVED — removed the obsolete `.agent/` adapter and its duplicate `conventions.md` / `glossary.md` copies; `.tfw/` remains canonical | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) | 2026-08-26 |
| TD-5 | ✅ RESOLVED — added twelve deterministic generation, drift, locale, intent, digest, invariant, and projection-regression tests for `generate_readme.py` and its four outputs | [REVIEW catalog discoverability Phase A](tasks/2026/20260827-132641__catalog_discoverability/phase-a/REVIEW__phase-a__multilingual_catalog.md) | 2026-08-27 |
| — | `AGENTS.md` claimed 23 channels; `data/communities.json` holds 18. Hand-maintained copy of a derived fact, unchecked by any script | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |
| — | Two competing status systems (`STEPS.md` and `TASK.md`), already diverged | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |
| — | `.agent/rules/agents.md` duplicated root `AGENTS.md` — two copies requiring lockstep edits | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |

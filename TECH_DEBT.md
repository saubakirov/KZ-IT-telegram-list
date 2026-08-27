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
| TD-2 | Every `last_verified` in `data/communities.json` reads `2026-01-30`. Link liveness and member counts are ~7 months stale | data-freshness | **High** | 🟡 PLANNED | [RES TFW-3 Q6](tasks/TFW-3__tfw_init/RES__TFW-3__tfw_init.md) |
| TD-4 | TFW-02 deleted 12 dead communities with no archive. The list of what was removed, and why, exists only in a commit diff | trace-loss | Medium | 🟡 PLANNED | [RF TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| TD-5 | `scripts/` has no tests. `generate_readme.py` correctness is verified only by eyeballing the output | missing-test | Medium | 🔴 OPEN | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| TD-8 | Legacy backlog items (CI, `README.ru.md`, archive section) were carried from the retired `TASK.md` without re-confirming they are still wanted | scope | Low | 🟡 PLANNED | [RES TFW-3 Q5](tasks/TFW-3__tfw_init/RES__TFW-3__tfw_init.md) |

---

## Detail

### TD-1 — Legacy task ID format (ACCEPTED)

`tasks/TFW-01_awesome_list_restructure/` and `tasks/TFW-02_enhanced_validation/` predate the
framework install. Renaming them would rewrite trace history for cosmetic consistency —
HL-TFW-3 §7 Principle 4 forbids it. `initial_seq: 3` sidesteps the `TFW-1`/`TFW-01` collision.
Accepted permanently; new tasks follow the convention.

### TD-2 — Stale verification dates (highest-value open item)

All 63 entries carry `last_verified: 2026-01-30`. A curated list whose central promise is
accuracy has not been verified in roughly seven months. Some communities have likely died,
merged, or changed handles, and every member count is stale.

**Resolution:** `python scripts/validate_links.py --update`, in CL mode — the run touches the
network and its verdicts need human review before dead entries are removed. Consider TD-4's
archive question at the same time, so this sweep does not repeat TFW-02's silent deletion.

### TD-6 — `meta.last_updated` pipeline ownership (RESOLVED)

`validate_links.py --update` now writes the run date to `meta.last_updated` when it persists
observed link results. Explicit archive mutation also writes the evidence date. Phase C delivered
the ownership mechanism without running a production sweep or changing the existing production
value; Phase D remains responsible for the first observed refresh.

---

## Resolved

| # | Item | Resolved by | Date |
|---|------|-------------|------|
| TD-3 | ✅ RESOLVED — added offline CI for schema validation and the generator's non-mutating README-currency gate on pull requests and pushes to `master`; no remote run is claimed in Phase C | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) | 2026-08-27 |
| TD-6 | ✅ RESOLVED — `validate_links.py` owns `meta.last_updated` whenever an observed update or explicit evidence-backed archive is persisted; production remains unchanged until Phase D | [RF TFW-4 Phase C](tasks/TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) | 2026-08-27 |
| TD-7 | ✅ RESOLVED — removed the obsolete `.agent/` adapter and its duplicate `conventions.md` / `glossary.md` copies; `.tfw/` remains canonical | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) | 2026-08-26 |
| — | `AGENTS.md` claimed 23 channels; `data/communities.json` holds 18. Hand-maintained copy of a derived fact, unchecked by any script | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |
| — | Two competing status systems (`STEPS.md` and `TASK.md`), already diverged | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |
| — | `.agent/rules/agents.md` duplicated root `AGENTS.md` — two copies requiring lockstep edits | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |

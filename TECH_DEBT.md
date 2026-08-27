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
| TD-3 | No CI. Nothing runs `validate_schema.py` on a PR — an invalid contribution reaches `master` before anyone notices | tooling | Medium | 🟡 PLANNED | [Task Board backlog](tasks/README.md) |
| TD-4 | TFW-02 deleted 12 dead communities with no archive. The list of what was removed, and why, exists only in a commit diff | trace-loss | Medium | 🟡 PLANNED | [RF TFW-02](tasks/TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) |
| TD-5 | `scripts/` has no tests. `generate_readme.py` correctness is verified only by eyeballing the output | missing-test | Medium | 🔴 OPEN | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
| TD-6 | `data/communities.json` `meta.last_updated` is `2026-01-30` and is not touched by any script — it drifts from reality on every data edit | data-integrity | Low | 🔴 OPEN | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) |
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

### TD-6 — `meta.last_updated` drifts

`generate_readme.py` never reads `meta.last_updated` and no script writes it, so it records
when someone last remembered to edit it by hand. Either wire it into the validation or
generation step, or drop the field — a fact that nothing maintains is worse than an absent one.
This is the same failure that produced the "23 channels" error corrected during TFW-3.

---

## Resolved

| # | Item | Resolved by | Date |
|---|------|-------------|------|
| TD-7 | ✅ RESOLVED — removed the obsolete `.agent/` adapter and its duplicate `conventions.md` / `glossary.md` copies; `.tfw/` remains canonical | [RF TFW-4 Phase A](tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) | 2026-08-26 |
| — | `AGENTS.md` claimed 23 channels; `data/communities.json` holds 18. Hand-maintained copy of a derived fact, unchecked by any script | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |
| — | Two competing status systems (`STEPS.md` and `TASK.md`), already diverged | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |
| — | `.agent/rules/agents.md` duplicated root `AGENTS.md` — two copies requiring lockstep edits | [RF TFW-3](tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | 2026-08-26 |

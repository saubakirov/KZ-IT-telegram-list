# Task Board — KZ-IT-telegram-list

> **Methodology:** [Trace-First Workflow](https://github.com/saubakirov/trace-first-starter) v1.3.0
> **Prefix:** `TFW` · **Next task:** TFW-5 · **Conventions:** [`.tfw/conventions.md`](../.tfw/conventions.md)
>
> This board is the single source of truth for project work status. It lives here, not in
> `README.md`, because `README.md` is regenerated in full by `scripts/generate_readme.py` and
> would discard it.

## Lifecycle

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
                                                                    │
                                                          🔄 REVISE ─┴─ ❌ REJECT
```

## Board

| ID | Task | Status | HL | RES | TS | ONB | RF | REV |
|----|------|--------|----|-----|----|-----|----|-----|
| [TFW-01](TFW-01_awesome_list_restructure/) | Awesome List restructure — JSON source of truth + generator | ✅ DONE | [✅](TFW-01_awesome_list_restructure/HL__TFW-01__awesome_list_restructure.md) | — | [✅](TFW-01_awesome_list_restructure/TS__TFW-01__awesome_list_restructure.md) | — | — | — |
| [TFW-02](TFW-02_enhanced_validation/) | Enhanced validation & community cleanup | ✅ DONE | [✅](TFW-02_enhanced_validation/HL__TFW-02__enhanced_validation.md) | — | — | — | [✅](TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) | — |
| [TFW-3](TFW-3__tfw_init/) | Initialize TFW 1.3.0 — framework install, Claude Code adapter, legacy migration | ✅ DONE | [✅](TFW-3__tfw_init/HL-TFW-3__tfw_init.md) | [✅](TFW-3__tfw_init/RES__TFW-3__tfw_init.md) | — | — | [✅](TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | — |
| [TFW-4](TFW-4__showcase_reorg/) | Showcase reorganization — commit the trace, consolidate the contract, automate the promise | 🟢 RF | [🔒](TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) | [✅](TFW-4__showcase_reorg/research/iter2/RES.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/TS__phase-a__baseline_cleanup.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/ONB__phase-a__baseline_cleanup.md) | — | — |

> **TFW-01 and TFW-02 are preserved pre-framework proto-artifacts.** They borrowed the TFW
> vocabulary before `.tfw/` and the methodology lifecycle existed, so they do not contain the
> contract freeze, Definition of Failure, or review lifecycle required by current TFW. Their
> zero-padded IDs and `HL__` filenames remain unchanged as historical traces — see
> [TECH_DEBT.md](../TECH_DEBT.md) TD-1. Tasks from TFW-3 onward follow the convention.

## Backlog

Carried over from the retired `TASK.md`. Not yet planned — each needs `/tfw-plan` before it
becomes a task with an ID.

| Candidate | Description | Priority | Note |
|-----------|-------------|----------|------|
| CI validation | GitHub Actions running `validate_schema.py` on PRs | Low | Would catch bad contributions before merge |
| `README.ru.md` | Russian translation of the list | Low | `description_ru` already exists in the data |
| Archive section | Keep dead communities visible as an archive instead of deleting | Low | TFW-02 deleted 12 outright; no record of what they were |
| Link freshness sweep | Re-run `validate_links.py --update`; all `last_verified` dates read 2026-01-30 | Medium | See TECH_DEBT.md TD-2 |

## How to start work

| Intent | Command |
|--------|---------|
| New task | `/tfw-plan <what you want to do>` |
| Continue interrupted work | `/tfw-resume` |
| Execute an approved TS | `/tfw-handoff` |
| Review completed work | `/tfw-review` |
| Upgrade the framework | `/tfw-update` |

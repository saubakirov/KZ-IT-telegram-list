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
| [TFW-4](TFW-4__showcase_reorg/) | Showcase reorganization — commit the trace, consolidate the contract, automate the promise | 🟢 RF — Phase C Iteration 3 evidence revision complete; re-review required; Phase D unapproved | [🔒 Master](TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/HL__phase-b__contract_docs.md) · [✅ Phase C](TFW-4__showcase_reorg/phase-c/HL__phase-c__pipeline_tooling.md) · [🟡 Phase D draft](TFW-4__showcase_reorg/phase-d/HL__phase-d__live_sweep_release.md) | [✅](TFW-4__showcase_reorg/research/iter2/RES.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/TS__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/TS__phase-b__contract_docs.md) · [✅ Phase C](TFW-4__showcase_reorg/phase-c/TS__phase-c__pipeline_tooling.md) · [🟡 Phase D draft](TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/ONB__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/ONB__phase-b__contract_docs.md) · [✅ Phase C](TFW-4__showcase_reorg/phase-c/ONB__phase-c__pipeline_tooling.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/RF__phase-b__contract_docs.md) · [🟢 Phase C Iteration 3 RF](TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/REVIEW__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/REVIEW__phase-b__contract_docs.md) · [🔄 Phase C addendum](TFW-4__showcase_reorg/phase-c/REVIEW__phase-c__pipeline_tooling.md) |

> **TFW-4 phase handoff:** Phases A–B are complete. Phase C preserves the original `🔄 REVISE`,
> Iteration 2 `✅ APPROVE`, and binding post-doc Iteration 3 `🔄 REVISE` in REVIEW history.
> Executor revision `a1c8673` replaces the non-reproducible ONB-era `KNOWLEDGE.md` byte hash with
> content-addressed keyed decision/debt provenance and strict negative fixtures. The direct
> current post-doc command and a clean detached `a1c8673` snapshot both pass schema, README
> `--check`, and the complete harness with exit 0. Phase C is now `🟢 RF`; exact next workflow:
> `/tfw-review tfw-4`.
> `tfw-docs: Applied` (`KNOWLEDGE.md` §§1–3) and `tfw-knowledge: N/A` (no Fact Candidates;
> the hard interval is not due). D13–D14 remain single indexed decisions. TD-5, TD-10, and TD-11
> remain unchanged. Master TFW-4 stays open; Phase D drafts remain unapproved and unchanged, with
> no live sweep implied or authorized. Remote GitHub Actions evidence remains `DEFERRED`; no
> Telegram, browser, project-command, release, tag, or push result exists. Phase D planning
> drafts are linked below; no execution approval is recorded.

> **TFW-4 Phase D approval gate:** Derivation-only
> [Phase HL](TFW-4__showcase_reorg/phase-d/HL__phase-d__live_sweep_release.md) and
> [TS](TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md) are DRAFT; no owner
> approval is recorded. Until approval there may be no network/Telegram/browser action,
> `kz-*` execution, live/update/archive validator run, catalog/README/release mutation,
> version change, release commit, tag, or push. After approval, the exact next workflow is
> `/tfw-handoff tfw-4`. Handoff is not publication approval: the prepared local snapshot
> must stop again for a separate owner decision on the exact commit, tag, branch, and remote.

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

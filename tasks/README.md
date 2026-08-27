# Tasks — KZ-IT-telegram-list

> **Methodology:** [Trace-First Workflow](https://github.com/saubakirov/trace-first-starter) v2.0.0-dirty
> **Identifiers:** clock-derived `YYYYMMDD-HHMMSS__slug` — no counter, nothing to reserve.
> Legacy `TFW-N` ids still resolve. · **Conventions:** [`.tfw/conventions.md`](../.tfw/conventions.md)
>
> This file is the route into task state, not the state itself. Live state lives in each
> task's own `status.md`; the derived portfolio view is [`00-INDEX.md`](00-INDEX.md). It
> lives here, not in `README.md`, because `README.md` is regenerated in full by
> `scripts/generate_readme.py` and would discard it.
>
> **Lifecycle vocabulary:** [`.tfw/glossary.md`](../.tfw/glossary.md) § Status Flow and
> [`.tfw/conventions.md`](../.tfw/conventions.md) §5. TFW 2.0.0 moved the legend there;
> this file deliberately keeps no second copy.
> **Commands:** [`../AGENTS.md`](../AGENTS.md) and [`../CLAUDE.md`](../CLAUDE.md).

## Where task state lives

Task state is **not** in this file. Each task carries its own `status.md`, which is the
only authority for that task's lifecycle, owner and outcome; a task with phases carries one
per phase directory. A transition is one write, inside one task directory, so two tasks
advance without their authors meeting in a shared file.

| Looking for | Read |
|-------------|------|
| The portfolio view — every task, its lifecycle and owner | [`00-INDEX.md`](00-INDEX.md) — derived, non-authoritative, rebuilt by `python docs/scripts/gen_index.py` |
| One task's live state | that task's `status.md` |
| Why a task reached its current state | that task's `journal/` — one immutable file per event |
| The retired board, captured verbatim | [`BOARD-SNAPSHOT.md`](BOARD-SNAPSHOT.md) — history, never edited |
| Who a handle refers to | [`../team/`](../team/) |

When the index disagrees with a task, **the task is right**: any workflow acting on a task
re-reads that task's `status.md` first.

### The board this file used to carry

The Task Board table was removed at TFW 2.0.0, which retired it as a required artifact.
Every row it held is preserved verbatim in [`BOARD-SNAPSHOT.md`](BOARD-SNAPSHOT.md), and
the accounting that proved nothing was lost is reproducible with
`python docs/scripts/migrate_board.py --board tasks/README.md --board-heading "## Board"
--board-rev <commit-before-removal>`.

The board's TFW-4 rollup notes are not reproduced here. A task-level summary of phase state
is a second fact that has to agree with the phases, which is the synchronization problem the
per-task carrier exists to remove. Their content lives where it belongs: in
[Phase D HL](TFW-4__showcase_reorg/phase-d/HL__phase-d__live_sweep_release.md) and
[Phase D TS](TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md), which
carry each gate record more fully than the board did.

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


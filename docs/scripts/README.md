# TFW framework tooling

These files are **framework tooling imported from the TFW upstream**, not project scripts.
Project scripts (the catalog pipeline) live in [`../../scripts/`](../../scripts/).

| File | What it does |
|------|--------------|
| `gen_index.py` | Rebuilds the derived portfolio view `tasks/00-INDEX.md` from each task's own `status.md`. Also the validation gate: `--validate`. |
| `migrate_board.py` | One-time: accounts for the retired Task Board and writes `status.md` per live task. |

## Why `docs/scripts/` in a project with no `docs/` site

`.tfw/conventions.md` §"derived index" and `.tfw/workflows/init.md` reference these by the
literal path `docs/scripts/`. Keeping that path means `.tfw/` stays byte-identical to
upstream and future `/tfw-update` runs remain trivial diffs. `gen_index.py` also resolves
its project root as `parents[2]` of its own file, which only holds at this depth.

`gen_docs.py` and `test_integration.py` were deliberately **not** imported: they build the
upstream repository's own MkDocs site, which this project does not have.

## Local adaptation

`migrate_board.py` upstream hardcodes the board at root `README.md` under `## Task Board`.
This project's board was `tasks/README.md` under `## Board`, because
`scripts/generate_readme.py` regenerates the root README in full and would discard it.
Two options were added — `--board` and `--board-heading` — defaulting to the upstream
values, so the change is additive and upstream behavior is unchanged.

## Requires

PyYAML.

# Board snapshot — the root Task Board at TFW 2.0.0


Every data row of the root `README.md` Task Board, captured verbatim on the day
the board was removed. This is history: it is never edited, never re-sorted and
never brought up to date. Live state lives in each task's own `status.md`, and the
browsable view is rebuilt at
[`tasks/00-INDEX.md`](../tasks/00-INDEX.md).

Backlog rows are here too. Six of them are ideas that never had a task directory —
a snapshot of only finished work would have deleted the project's backlog. An idea
is picked up by creating a real task, not by resurrecting a row.

| | |
|---|---|
| Rows captured | 4 |
| With a task directory | 2 |
| Board-only, no directory | 2 |
| In a shape no strict row parser matches | 0 |

## Rows

| ID | Task | Status | Class |
|---|---|---|---|
| `TFW-01` | Awesome List restructure — JSON source of truth + generator | ✅ DONE | board-only, backlog |
| `TFW-02` | Enhanced validation & community cleanup | ✅ DONE | board-only, backlog |
| `TFW-3` | Initialize TFW 1.3.0 — framework install, Claude Code adapter, legacy migration | ✅ DONE | matched |
| `TFW-4` | Showcase reorganization — commit the trace, consolidate the contract, automate the promise | 🟠 READY — G2 approved; datanomika success retained; kzquake UTF-8 resume planned; archives and G3–G4 pending | matched |

## Verbatim source

The rows exactly as the board carried them, links, strike-through and schema drift
included. This block is what makes the table above checkable.

```text
| [TFW-01](TFW-01_awesome_list_restructure/) | Awesome List restructure — JSON source of truth + generator | ✅ DONE | [✅](TFW-01_awesome_list_restructure/HL__TFW-01__awesome_list_restructure.md) | — | [✅](TFW-01_awesome_list_restructure/TS__TFW-01__awesome_list_restructure.md) | — | — | — |
| [TFW-02](TFW-02_enhanced_validation/) | Enhanced validation & community cleanup | ✅ DONE | [✅](TFW-02_enhanced_validation/HL__TFW-02__enhanced_validation.md) | — | — | — | [✅](TFW-02_enhanced_validation/RF__TFW-02__enhanced_validation.md) | — |
| [TFW-3](TFW-3__tfw_init/) | Initialize TFW 1.3.0 — framework install, Claude Code adapter, legacy migration | ✅ DONE | [✅](TFW-3__tfw_init/HL-TFW-3__tfw_init.md) | [✅](TFW-3__tfw_init/RES__TFW-3__tfw_init.md) | — | — | [✅](TFW-3__tfw_init/RF__TFW-3__tfw_init.md) | — |
| [TFW-4](TFW-4__showcase_reorg/) | Showcase reorganization — commit the trace, consolidate the contract, automate the promise | 🟠 READY — G2 approved; `datanomika` success retained; `kzquake` UTF-8 resume planned; archives and G3–G4 pending | [🔒 Master](TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/HL__phase-b__contract_docs.md) · [✅ Phase C](TFW-4__showcase_reorg/phase-c/HL__phase-c__pipeline_tooling.md) · [🟠 Phase D G2 PARTIAL/READY](TFW-4__showcase_reorg/phase-d/HL__phase-d__live_sweep_release.md) | [✅ Iteration 2](TFW-4__showcase_reorg/research/iter2/RES.md) · [✅ G2 Iteration 3](TFW-4__showcase_reorg/research/iter3/RES.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/TS__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/TS__phase-b__contract_docs.md) · [✅ Phase C](TFW-4__showcase_reorg/phase-c/TS__phase-c__pipeline_tooling.md) · [🟠 Phase D G2 PARTIAL/READY](TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/ONB__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/ONB__phase-b__contract_docs.md) · [✅ Phase C](TFW-4__showcase_reorg/phase-c/ONB__phase-c__pipeline_tooling.md) · [✅ Phase D ONB](TFW-4__showcase_reorg/phase-d/ONB__phase-d__live_sweep_release.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/RF__phase-b__contract_docs.md) · [🟢 Phase C Iteration 3 RF](TFW-4__showcase_reorg/phase-c/RF__phase-c__pipeline_tooling.md) | [✅ Phase A](TFW-4__showcase_reorg/phase-a/REVIEW__phase-a__baseline_cleanup.md) · [✅ Phase B](TFW-4__showcase_reorg/phase-b/REVIEW__phase-b__contract_docs.md) · [✅ Phase C Iteration 4](TFW-4__showcase_reorg/phase-c/REVIEW__phase-c__pipeline_tooling.md) |
```

---

*Captured once by `docs/scripts/migrate_board.py`. Historical — do not update.*

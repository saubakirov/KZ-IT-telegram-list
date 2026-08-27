# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__baseline_cleanup.md)
> TS: [TS Phase A](../TS__phase-a__baseline_cleanup.md)

## Understanding

The executor removed the obsolete singular `.agent/` adapter, moved TD-7 from the open debt
table to the resolved table, and updated the TFW-4 Task Board row plus the legacy TFW-01/TFW-02
note. The work was split into an ONB-only commit and a four-path implementation commit so the
pre-existing dirty `AGENTS.md`, `.agents/**`, research, Phase HL, and Phase TS work stayed outside
the implementation path set. The RF also records deterministic local evidence, an offline schema
smoke check, and no network, push, tag, or release action.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — remove `.agent/` singular while preserving canonical `.tfw/` files and byte-identical `.agents/**` plural | RF §3 reports `.agent/` absent, canonical files unchanged, and the 11-file plural manifest unchanged at `b9013c…d6b` | ✅ |
| AC-2 — resolve only TD-7 and preserve unrelated debt items | RF §3 reports `changed_td_ids=TD-7` and a resolved record naming the duplicate-adapter removal | ✅ |
| AC-3 — preserve the TFW-4 research/TS trace, clarify the proto-artifact note, and retain allowed historical references | RF §3 reports the iteration-2 RES and approved Phase A TS links retained, status advanced to RF, and 12 reference files classified within the amended DoD 3 allow-list | ✅ |
| AC-4 — keep implementation to four paths, preserve protected dirty work, and use truthful current commit metadata | RF §3 reports an unchanged 116-file protected manifest and commit `f8d6be2` with exactly two deletions plus two modifications, current dates, no tag, and no network/release/push | ✅ |

## Deviations from TS

- The executor ran `python scripts/validate_schema.py` as an additional offline smoke check. The
  RF declares that this was read-only with respect to Phase A implementation output.
- The commits use the task-specific `[claude-code/TFW-4/baseline-cleanup/executor]` prefix even
  though the acting product was Codex. RF §2 explains that the frozen Master HL and approved TS
  explicitly fixed `agent=claude-code`, while the general convention normally derives the token
  from the acting product.
- No acceptance criterion or implementation-scope deviation is declared in RF §2.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

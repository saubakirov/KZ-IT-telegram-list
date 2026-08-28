# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__intake_engine.md)
> TS: [TS Phase A](../TS__phase-a__intake_engine.md)

## Understanding

The Executor added a loss-accountable Telegram candidate intake engine, a minimal immutable
fetch/retry seam around the existing classifier, and deterministic tests for parsing,
observation, canonical preview/approval, and crash-aware apply behavior. It also installed three
complete byte-identical Claude/Codex `kz-*` command pairs with an explicit Claude-to-Codex sync
gate, then recorded calibration, runtime-smoke, controlled-hash, build, and regression evidence
without applying a production candidate.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — lossless closed candidate source grammar | RF §3 claims every Telegram-like occurrence is accounted for before grouping and only the closed HTTPS root grammar produces candidates. | ✅ |
| AC-2 — non-mutating arbitrary-candidate observation | RF §3 claims fetch-once three-type reconciliation through unchanged classifier calls, with fail-closed unresolved outcomes. | ✅ |
| AC-3 — closed preview and separate current authority | RF §3 claims closed canonical payloads, complete rendering, exact action binding, and separate durable owner authority. | ✅ |
| AC-4 — strict idempotent crash-aware apply | RF §3 claims revalidation, exact-state idempotency, marker-bound recovery, separate receipt, and fixture-only writes. | ✅ |
| AC-5 — complete synchronized command inventory | RF §3 claims exact three-command inventory, byte parity, completeness, path neutrality, and preserved stats/release authority stops. | ✅ |
| AC-6 — sealed evaluation boundary | RF §3 claims only the eight disclosed calibration cases entered execution and no holdout/source material entered implementation or evidence. | ✅ |
| AC-7 — fresh Claude and Codex literal behavior | RF §3 claims exact-SHA fresh Claude and non-forked Codex smokes for sentinel routing, triage, release stops, and no mutation. | ✅ |
| AC-8 — scope and predecessor preservation | RF §3 claims all declared gates pass, production bytes remain unchanged, implementation is exactly 12 paths and 1,885 changed lines, and no external mutation occurred. | ✅ |

## Deviations from TS

- The configured generic full-catalog live `python scripts/validate_links.py` command was not run;
  the RF says the Phase A TS/Coordinator boundary instead used the approved predecessor offline
  matrices plus exactly eight calibration probes.
- The historical Phase C harness `main()` was not run because of its recorded stale fixed-date
  assertion; the RF says its TS-relevant `run_link_matrix` and `run_command_matrix` functions were
  called directly.
- Three pre-acceptance Claude harness attempts are retained as excluded deviations: one lost the
  empty tools argument before model execution, one launch was policy-rejected before start, and
  one quoting probe returned an unexecuted tool-call proposal. The RF offers later invocations as
  the accepted evidence.
- The Phase HL allowed up to 13 implementation paths, while the approved TS fixed the tighter
  budget at exactly 12; the Executor followed the TS boundary.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

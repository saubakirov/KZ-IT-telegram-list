# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__intake_engine.md)
> TS: [TS Phase A](../TS__phase-a__intake_engine.md)

## Understanding

The Executor completed the single bounded F2a correction at implementation SHA
`9185811696c762b5261e9b90f71bee846b6fc692`. Relative to the previously reviewed implementation
`731b3d6a3350bb3fe41115a4ae9213aaa86bbc6f`, it changes only `scripts/kz_intake.py` and
`scripts/test_kz_intake.py`: failed HTTP observations now exclude the entire 200–299 interval,
while exhaustive tests preserve fetched 2xx at attempts 1–3 and the existing terminal/retry tuple
families.

The four authorized Executor commits were integrated without conflict or manual edit onto the
prior Reviewer commit, producing RF base `24f9e2de000b8c07d061388ffb878ca72192fff6`; its tree is
byte-identical to the Executor tip `1be9412c03962cd159b528a66603c4dd00af2b30`. The RF carries
forward the previously reviewed parser, exact action/stage/apply boundary, structural locale
invariant, unchanged classifier and command bodies, calibration/public seal evidence, runtime
smokes, controlled hashes, and exact-SHA offline build evidence.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — lossless closed candidate source grammar | RF §3 retains occurrence-first accounting, fixed literal HTTPS authorities, trailing-dot rejection, and explicit non-candidate dispositions. | ✅ |
| AC-2 — non-mutating arbitrary-candidate observation | RF §3 claims one fetch, three unchanged classifier calls, all failed 2xx rejected, fetched 2xx attempts 1–3, outside-2xx non-429 HTTP attempt 1, retry-terminal failures attempt 3, and no `http_429`. | ✅ |
| AC-3 — closed preview and separate current authority | RF §3 retains recursive closure, exact action/stage derivation, complete rendering, and a separate current-owner envelope. | ✅ |
| AC-4 — strict idempotent crash-aware apply | RF §3 retains byte-exact zero ADD, mechanically rebound 1/N ADD, real schema/generator preflight, neutral B/A/X semantics, catalog-last recovery, and a bound receipt. | ✅ |
| AC-5 — complete synchronized command inventory | RF §3 retains exactly three standalone byte-identical command pairs with path neutrality, parity enforcement, and authority stops. | ✅ |
| AC-6 — sealed evaluation boundary | RF §3 claims only eight disclosed calibration cases entered Phase A and preserves the non-revealing full-partition receipt. | ✅ |
| AC-7 — fresh Claude and Codex literal behavior | RF §3 retains complete accepted runtime records at unchanged-command SHA `f8fd5022…`, with Claude's stated limitation and Codex's explicit loaded paths. | ✅ |
| AC-8 — regression, build, scope, and no mutation | RF §3 claims 45 tests, predecessor matrices, classifier preservation, exact 13-path/2,406-line scope, final exact-SHA build, controlled hashes, and zero external mutation. | ✅ |

## Deviations from TS

- The generic configured full-catalog live validator was not run; the approved Phase A boundary
  uses predecessor offline matrices plus the retained eight disclosed calibration probes.
- The historical Phase C harness's full `main()` was not run because its fixed oldest-live
  assertion is stale; its TS-relevant link and command matrices were invoked directly.
- Accepted Claude/Codex runtime smokes remain at
  `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`; the bounded correction changes only intake
  validation/tests, leaving `AGENTS.md` and all six command files byte-identical.
- One focused Executor unittest invocation named a nonexistent class and failed before executing a
  test; the corrected method, full 45-test suite, and all other gates subsequently passed.
- The Executor's supported exact-SHA build supersedes a prior policy-rejected Reviewer attempt;
  this re-review also independently completed a fresh exact-SHA, network-disabled build.
- Production apply, holdout execution or identity inspection, a full-catalog live sweep,
  browser/authenticated fallback, release, tag, push, and deployment remain outside Phase A and
  were not performed.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

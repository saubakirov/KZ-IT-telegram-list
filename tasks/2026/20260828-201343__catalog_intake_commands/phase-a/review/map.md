# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__intake_engine.md)
> TS: [TS Phase A](../TS__phase-a__intake_engine.md)

## Understanding

The Executor completed the narrow Phase A replan at implementation SHA
`731b3d6a3350bb3fe41115a4ae9213aaa86bbc6f` and integrated its RF/evidence at
`45878d9459e263ed7821dcc84bc400ed0603fb3c`. Relative to the approved revision base, the
implementation changes only `scripts/kz_intake.py`, `scripts/test_kz_intake.py`, and
`scripts/validate_schema.py`: zero-ADD stages are claimed byte-exact, exact ADD stages mechanically
rebind locale-review metadata under the real schema/generator preflight, and serialized transport
observations are claimed closed to the retry producer's exact tuples.

The RF carries forward the previously reviewed lossless parser, unchanged classifier authority,
closed preview/approval/marker/receipt records, complete synchronized Claude/Codex commands,
calibration and sealed-partition evidence, exact runtime smokes, controlled production hashes, and
offline site-build evidence. It claims all earlier D1–D6 and F1/F2 counterexamples remain closed,
with no production candidate, holdout reveal, release, tag, push, deployment, or external mutation.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — lossless closed candidate source grammar | RF §3 claims occurrence-first accounting, fixed literal HTTPS authorities, trailing-dot rejection, and explicit non-candidate dispositions. | ✅ |
| AC-2 — non-mutating arbitrary-candidate observation | RF §3 claims one fetch, three unchanged classifier calls, exact classifier families, and only producer-possible transport tuples. | ✅ |
| AC-3 — closed preview and separate current authority | RF §3 claims recursive closure, exact action/stage derivation, complete rendering, and a separate current-owner envelope. | ✅ |
| AC-4 — strict idempotent crash-aware apply | RF §3 claims byte-exact zero ADD, mechanically rebound 1/N ADD, real schema/generator preflight, neutral B/A/X semantics, catalog-last recovery, and a bound receipt. | ✅ |
| AC-5 — complete synchronized command inventory | RF §3 claims exactly three standalone byte-identical command pairs with path neutrality, parity enforcement, and preserved authority stops. | ✅ |
| AC-6 — sealed evaluation boundary | RF §3 claims only eight disclosed calibration cases entered Phase A and cites a non-revealing full-partition receipt without exposing the holdout. | ✅ |
| AC-7 — fresh Claude and Codex literal behavior | RF §3 claims complete accepted runtime records at unchanged-command SHA `f8fd5022…`, with Claude's stated limitation and Codex's explicit loaded paths. | ✅ |
| AC-8 — regression, build, scope, and no mutation | RF §3 claims 44 tests, predecessor matrices, classifier preservation, exact 13-path/2,369-line scope, final exact-SHA build, controlled hashes, and zero external mutation. | ✅ |

## Deviations from TS

- The generic configured full-catalog live validator was not run; the approved Phase A boundary
  uses predecessor offline matrices plus the retained eight disclosed calibration probes.
- The historical Phase C harness's full `main()` was not run because its fixed oldest-live
  assertion is stale; its TS-relevant link and command matrices were invoked directly.
- Accepted Claude/Codex runtime smokes remain at
  `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`; the final revision changes only intake code/tests and
  schema validation, leaving `AGENTS.md` and all six command files byte-identical.
- Claude proves project-setting behavior plus independently bound local bytes but did not echo an
  absolute loaded path; the Codex report explicitly names absolute loaded paths and hashes.
- Production apply, holdout execution or identity inspection, a full-catalog live sweep,
  browser/authenticated fallback, release, tag, push, and deployment remain outside Phase A and
  are reported as not performed.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

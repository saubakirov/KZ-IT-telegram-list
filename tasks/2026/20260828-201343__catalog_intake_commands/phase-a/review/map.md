# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__intake_engine.md)
> TS: [TS Phase A](../TS__phase-a__intake_engine.md)

## Understanding

The Executor revised the candidate-intake authority boundary after the prior review. The revision
derives a staged catalog from the baseline plus proposed ADD rows, requires four generator-exact
projections, rederives that state during apply, writes the catalog last for recoverability, and
validates serialized observations against enumerated classifier and transport families.

The revision changes only `scripts/kz_intake.py` and `scripts/test_kz_intake.py` after the accepted
command-runtime smokes. The RF otherwise carries forward the already-reviewed lossless source
parser, preserved classifier seam, closed preview/approval/marker/receipt objects, synchronized
Claude/Codex commands, calibration artifacts, production hashes, and exact-SHA site-build record.

## TS ↔ RF Alignment

This table maps requirements to RF claims only. Whether the claims hold is deferred to Verify.

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — lossless closed candidate source grammar | RF §3 claims occurrence-first accounting, fixed literal HTTPS authorities, and explicit non-candidate dispositions. | ✅ |
| AC-2 — non-mutating arbitrary-candidate observation | RF §3 claims one fetch, three unchanged classifier calls, and acceptance of only exact producer-possible transport/classifier tuples. | ✅ |
| AC-3 — closed preview and separate current authority | RF §3 claims recursively closed records, exact action/stage derivation, complete rendering, and a separate durable owner envelope. | ✅ |
| AC-4 — strict idempotent crash-aware apply | RF §3 claims apply-time semantic rederivation, real schema/currency preflight, neutral B/A/X state, catalog-last recovery, exact no-op, and receipt binding. | ✅ |
| AC-5 — complete synchronized command inventory | RF §3 claims exactly three standalone byte-identical command pairs with path neutrality and preserved authority stops. | ✅ |
| AC-6 — sealed evaluation boundary | RF §3 claims only the eight disclosed calibration cases entered execution and cites the non-revealing full-partition receipt. | ✅ |
| AC-7 — fresh Claude and Codex literal behavior | RF §3 claims complete accepted records, with Claude's behavior/static binding limitation distinguished from Codex's explicit loaded-path report. | ✅ |
| AC-8 — regression, build, scope, and no mutation | RF §3 claims 42 tests, predecessor matrices, classifier preservation, exact 12-path/2,230-line scope, official-image build, controlled hashes, and zero mutation. | ✅ |

## Deviations from TS

- The configured generic full-catalog live validator was not run. The approved phase boundary uses
  predecessor offline matrices plus exactly eight disclosed calibration probes.
- The historical Phase C harness's complete `main()` remains inapplicable because its fixed
  oldest-live assertion is stale; its TS-relevant link and command matrices were invoked directly.
- Accepted Claude/Codex smokes remain at `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a` because only
  intake code/tests changed later. Claude proves behavior plus static local path/hash binding but
  did not echo its loaded absolute path; Codex explicitly reports loaded absolute paths/hashes.
- The exact-SHA build log binds revised implementation `20c19505d5e156c3f0fe563877a03f387322aca2`.
- Production apply, holdout execution, full-catalog live sweep, browser/authenticated fallback,
  release, tag, push, and deployment remain outside Phase A and were not performed.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

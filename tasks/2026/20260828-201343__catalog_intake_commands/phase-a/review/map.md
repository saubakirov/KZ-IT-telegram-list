# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__intake_engine.md)
> TS: [TS Phase A](../TS__phase-a__intake_engine.md)

## Understanding

The Executor added a loss-accountable Telegram candidate intake engine, a fetch-once seam around
the existing classifier, closed preview/approval/receipt records, and a fixture-only exact-state
apply boundary. It also installed complete synchronized Claude/Codex copies of `kz-add`,
`kz-stats`, and `kz-release`, then bound calibration, runtime, scope, production-hash, regression,
and built-site evidence without applying a production candidate.

The revision changes only `scripts/kz_intake.py` and `scripts/test_kz_intake.py` after the accepted
runtime smokes. It addresses the six findings from the first formal review: literal trailing-dot
authority rejection, recursive integer/evidence/transport validation, neutral controlled paths,
complete runtime records, a non-revealing partition receipt, and an exact-revision Jekyll log.

## TS ↔ RF Alignment

This table maps requirements to RF claims only. Whether the claims hold is deferred to Verify.

| TS requirement | RF claim | Addressed? |
|----------------|----------|------------|
| AC-1 — lossless closed candidate source grammar | RF §3 claims occurrence-first accounting, literal fixed HTTPS authorities, and explicit trailing-dot rejection. | ✅ |
| AC-2 — non-mutating arbitrary-candidate observation | RF §3 claims fetch-once three-type reconciliation through unchanged classifier calls and fail-closed handling of every non-exact tuple. | ✅ |
| AC-3 — closed preview and separate current authority | RF §3 claims recursive closed schemas, complete rendering, exact action binding, and a separate durable owner envelope. | ✅ |
| AC-4 — strict idempotent crash-aware apply | RF §3 claims staged validation, neutral-aware B/A/X state, exact no-op/recovery behavior, and a separate receipt. | ✅ |
| AC-5 — complete synchronized command inventory | RF §3 claims exactly three complete byte-identical command pairs with path neutrality and preserved stats/release authority stops. | ✅ |
| AC-6 — sealed evaluation boundary | RF §3 claims only the eight disclosed calibration cases entered execution and cites a non-revealing receipt for exact full-partition membership. | ✅ |
| AC-7 — fresh Claude and Codex literal behavior | RF §3 claims complete fresh accepted records, with Claude's local-load proof expressly limited and Codex reporting absolute loaded paths/hashes. | ✅ |
| AC-8 — regression, build, scope, and no mutation | RF §3 claims all deterministic gates, official-image build, exact 12-path/1,957-line scope, controlled hashes, and zero external/production mutation. | ✅ |

## Deviations from TS

- The configured generic full-catalog live validator was not run. The approved Phase A boundary
  replaces it with predecessor offline matrices and exactly eight disclosed calibration probes.
- The historical Phase C harness's full `main()` was not used because its fixed oldest-date
  assertion is stale. Its TS-relevant link and command matrices were invoked directly.
- Three pre-acceptance Claude harness deviations are retained and excluded. The accepted Claude
  records establish project-setting use and local-body-matching behavior plus static path/hash
  parity, but Claude did not echo an absolute loaded path. Codex separately reports absolute
  loaded paths and hashes.
- Runtime smokes remain bound to `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`; the revised
  implementation SHA changes only intake code/tests and leaves all command bodies byte-identical.
- The allocation receipt is Coordinator-owned. Under the review's explicit post-freeze authority,
  the Reviewer may reproduce it from sealed material without disclosing or using holdout content.
- Production apply, full-catalog live sweep, browser/authenticated fallback, release, tag, push,
  and deployment remain outside Phase A and were not performed.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

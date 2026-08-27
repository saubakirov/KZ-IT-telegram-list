# Map — TFW-4 / Phase C: Pipeline & Tooling (Repeat Review)
> **Mindset:** Experienced newcomer. Understand before judging.
> **RF:** [RF Phase C](../../RF__phase-c__pipeline_tooling.md)
> **TS:** [TS Phase C](../../TS__phase-c__pipeline_tooling.md)
> **Prior review:** [Phase C REVIEW](../../REVIEW__phase-c__pipeline_tooling.md) (`REVISE`)

## Understanding

The revision retains the original ten-path offline Phase C implementation and closes the first
review's target-binding finding in a two-path implementation/evidence commit. Commit `165541c`
limits authoritative page identity to canonical, OG, and primary Telegram action signals,
rejects conflicting authoritative identities, and treats description anchors as content rather
than peer binding; commit `a141f7c` records the revised EV/RF and re-review handoff without
changing the original Reviewer-owned REVIEW or stage traces. Production Telegram facts, remote
CI, Phase D, browser use, project-command invocation, release, tag, and push remain outside the
result.

## TS ↔ RF Alignment

| TS requirement | Revised RF claim | Aligned? |
|----------------|------------------|----------|
| AC-1 — enforce North Star/archive/date contract while adding only `archive: []` | RF §§1, 3–4 retain the production-schema and isolated negative/stale matrix claims | ✅ Claimed |
| AC-2 — evidence-safe identity/type classification, updates, summaries, and explicit archive input | RF §§1–4 now claim authoritative-only target binding, exact decoy non-mutation, conflict rejection, and the full C3/C4/C5/update/archive matrix | ✅ Claimed |
| AC-3 — generated Purpose/stats/order/anchors/archive and non-mutating README currency | RF §§1, 3–4 retain generator, `--check`, isolated archive/stale variants, and 63-entry semantic preservation claims | ✅ Claimed |
| AC-4 — complete bounded `kz-*` definitions with protected framework adapters and no invocation | RF §§1–4 retain static command/reference/authority-gate claims and the unchanged 12-file `/tfw-*` manifest | ✅ Claimed |
| AC-5 — offline CI and exact local equivalents; remote run classified honestly | RF §§2, 4–5 and EV E5 keep the real GitHub Actions run `DEFERRED` because the TS forbids push | ✅ Claimed |
| AC-6 — D13–D14 once; only TD-3/TD-6 resolved | RF §§1, 3–4 retain the keyed memory/debt transition claims and preserve TD-5/TD-10/TD-11 | ✅ Claimed |
| AC-7 — exact bounded scope, preserved traces/protected state, truthful attribution, and no external/release action | RF §§1, 3–4 add the exact two-path revision and four-file Reviewer-trace manifest to the original ten-path/protected/history boundary | ✅ Claimed |

## Deviations from TS

No revised product path is outside the approved Phase C implementation/evidence boundary.
`scripts/validate_links.py` is one of the ten approved implementation paths, and the bounded
`evidence/offline_harness.py` revision is a mandatory Phase C evidence attachment rather than a
general TD-5 test-suite repair. The original `REVISE`, REVIEW synthesis, and first-iteration
`review/{map,verify,judge}.md` remain historical Reviewer-owned traces.

## Repeat-Review Focus

1. Replay the exact original decoy and prove both classification and persisted data remain
   non-mutating.
2. Challenge authoritative conflicts, legitimate target previews, and the no-authoritative
   fallback before accepting the revised binding design.
3. Re-run all offline AC-1 through AC-7 gates, all 14 RF-claimed files, exact scope, protected
   manifests, original Reviewer-trace preservation, attribution/history, tags, and absence of
   external-state artifacts.
4. Keep the remote Actions result `DEFERRED`; perform no network, browser, `kz-*`, Phase D,
   release, tag, or push action.

## Checkpoint

**Self-check:**
- [x] Read revised RF §§1–5 and revised EV completely?
- [x] Read approved TS DoD and matched every AC to revised RF §3?
- [x] Read Master HL §7 Principles and frozen baseline `d31e60d`?
- [x] Read ONB, both revision commits, the prior REVIEW, and all first-iteration stage files?

Stage complete: YES

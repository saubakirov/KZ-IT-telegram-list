# RF — TFW-4 / Phase C: Pipeline & Tooling

> **Date**: 2026-08-27
> **Author**: Executor (Codex)
> **Status**: 🟢 RF — Iteration 3 Revision Complete; re-review required
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Phase HL**: [Phase C HL](HL__phase-c__pipeline_tooling.md)
> **TS**: [TS Phase C](TS__phase-c__pipeline_tooling.md)
> **Revision source**: [Phase C REVIEW](REVIEW__phase-c__pipeline_tooling.md) (`🔄 REVISE`)

---

## 1. What Was Done

### Revision History

| Iteration | Result | Trace |
|-----------|--------|-------|
| Original execution | Ten-path implementation plus initial EV/RF; later REVIEW found the identity-decoy gap | Implementation `172e6ac`; primary EV/RF `c7180b9`; [formal REVIEW](REVIEW__phase-c__pipeline_tooling.md) |
| Review revision | Restricted arbitrary anchors from identity binding, rejected authoritative conflicts, and added exact non-mutation regression evidence | Revision implementation `165541c`; revised EV/RF and Task Board in the subsequent lifecycle commit |
| Post-doc evidence revision | Replaced the non-reproducible ONB-era whole-document hash with committed keyed decision/debt provenance and strict negative fixtures; replayed both the current post-doc checkout and a clean fixed revision | Evidence implementation `a1c8673`; current binding verdict remains Iteration 3 `REVISE` until fresh review |

The original EV/RF versions remain addressable at commit
`c7180b92e14013d51c231a851b17fb1c833366bf`; this file preserves the original `REVISE`, the
Iteration 2 `APPROVE`, and the binding Iteration 3 `REVISE` without deleting prior history.

### New Files

| File | Description |
|------|-------------|
| `.claude/commands/kz-stats.md` | Complete future CL catalog-validation, evidence, delta and owner-triage operation; it was defined but not invoked |
| `.claude/commands/kz-release.md` | Complete dated-snapshot preparation operation with freshness/evidence gates and a hard stop before tag or push; it was defined but not invoked |
| `.github/workflows/validate.yml` | Read-only pull-request and `master` push validation using schema and non-mutating README-currency gates |
| `tasks/TFW-4__showcase_reorg/phase-c/ONB__phase-c__pipeline_tooling.md` | Executor onboarding, boundary confirmation and ONB snapshots |
| `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` | Bounded socket-free Phase C evidence harness, extended by Iteration 2 identity regressions and Iteration 3 content-addressed keyed decision/debt provenance; not a replacement for TD-5's general test suite |
| `tasks/TFW-4__showcase_reorg/phase-c/evidence/EV__phase-c__pipeline_tooling.md` | Per-AC evidence, all three review iterations, inline synthetic classifier shapes, current/clean-revision replay and external-evidence boundary |

### Modified Files

| File | Changes |
|------|---------|
| `data/communities.json` | Added only the approved empty top-level `archive` array; all six existing top-level values are semantically unchanged |
| `scripts/validate_schema.py` | Enforces North Star/live/archive contracts, collisions and strict dates; reports dynamic non-fatal freshness using ASCII-tagged output |
| `scripts/validate_links.py` | Adds target/type-bound classifications, machine-readable summaries, evidence-safe update ownership and explicit owner/evidence-gated archive moves; review revision limits identity to canonical/OG/primary-action signals and rejects conflicts while preserving throttle/backoff constants |
| `scripts/generate_readme.py` | Renders Purpose, dynamic stats, display-name category order and conditional archive presentation; adds normalized non-mutating `--check` |
| `README.md` | Regenerated exclusively through the generator; presentation changed without changing any live entry fact |
| `KNOWLEDGE.md` | Added D13 and D14 only for Phase C |
| `TECH_DEBT.md` | Resolved TD-3 and TD-6 only; Phase D and unrelated debt remain open |
| `tasks/README.md` | Records the Phase C executor lifecycle and RF handoff |

## 2. Key Decisions

1. Freshness is reported but not schema-enforced. Valid old dates remain operational signals;
   malformed or impossible dates are fatal.
2. A target may be verified without a count only when the preview binds both requested handle and
   declared type. Canonical/OG and primary-action handles are authoritative; arbitrary description
   links cannot bind a target, and conflicting authoritative handles are ambiguous. Counts are
   parsed only from the target preview region; ambiguous, generic and failed responses create no
   catalog fact.
3. Observed updates and archive moves are separate pure mutation paths. Archive requires an exact
   handle, non-empty reason, evidence reference and explicit owner approval; classification never
   auto-archives.
4. README currency is proven by normalized comparison in a non-mutating check mode. Production
   README content continues to have one source: the generator plus structured data.
5. Project operations use `kz-*`; framework operations remain `tfw-*`. The new project adapters
   describe future CL authority and browser fallback but Phase C does not invoke either command.
6. Remote CI evidence is deferred rather than inferred: the workflow and exact local equivalents
   exist, but no push is authorized in this phase.
7. AC-6 uses normalized keyed semantics from content-addressed Git predecessors, not mutable
   document bytes. D1–D12 resolve from `4bc1bb1`, D13–D14 from direct child `172e6ac`, and the
   clean lifecycle debt state from `a141f7c`; unrelated post-doc prose cannot invalidate them.

## 3. Acceptance Criteria

- [x] AC-1 — the structured North Star/archive/date contract is enforced offline and production data gains only `archive: []`.
- [x] AC-2 — link classification, updates, summaries and explicit archive input are target-evidence-safe under the offline fixture matrix.
- [x] AC-3 — the promised README presentation and normalized non-mutating currency contract are generated and regression-checked.
- [x] AC-4 — complete bounded `kz-stats` and `kz-release` CL operations exist without any framework-adapter or external action.
- [x] AC-5 — read-only offline CI validation is defined and its exact local equivalents pass; the remote run is explicitly deferred.
- [x] AC-6 — D1–D14 meanings and only the TD-3/TD-6 resolution transitions are verified from committed keyed provenance; D15 is absent and strict negative fixtures reject semantic/cardinality drift.
- [x] AC-7 — exact scope, protected state, attribution and offline/no-release boundaries are confirmed; Phase D remains next.

## 4. Verification

- Lint (`python scripts/validate_schema.py`): PASS, exit 0; 40 groups, 18 channels, 5 bots,
  18 categories, empty archive, 0 errors; 63 stale live dates were reported non-fatally.
- Tests (`python scripts/validate_links.py`): NOT RUN by design because the configured command
  opens the production network path, which the approved Phase C TS forbids. The required
  socket-free imported classifier/update/archive matrix passed via
  `python -B tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py`.
- Verify (`python scripts/validate_schema.py && python scripts/generate_readme.py`): PASS for the
  approved generation step; the stricter postcondition `python scripts/generate_readme.py --check`
  also passed without rewriting README.
- Python compilation: PASS for the three production scripts and offline harness without retaining
  `__pycache__` evidence artifacts.
- CI definition: PASS locally; YAML parsed with an already available parser and both exact workflow
  commands exited 0. Remote GitHub Actions run remains DEFERRED because it requires a forbidden push.
- Regression harness: PASS for AC-1 through AC-6 matrices, including sanitized synthetic C3/C4/C5,
  count/type mismatch/failure, identity decoy, authoritative conflict, update/archive, conditional
  archive README and stale check behavior. The exact REVIEW counterexample now returns
  `non_target`, count `null`, zero date/count updates and unchanged requested-entry fields. The
  AC-6 matrix also rejects removed/duplicated/meaning-changed predecessor decisions,
  missing/duplicated Phase C decisions, premature D15, and invalid TD-5/TD-6 transitions.
- Scope/integrity: PASS; implementation commit `172e6ac18c7e604d553c38522650562d416dfb51`
  contains exactly ten TS implementation paths with 1327 insertions and 407 deletions.
- Revision scope/integrity: PASS; commit `165541c6cf4668bf60c891fa8df2f249884cc946`
  contains only `scripts/validate_links.py` and the approved Phase C offline evidence harness.
- Iteration 3 scope/integrity: PASS; commit `a1c8673acca273b08b241ba242d848c78369c310`
  contains only the approved Phase C offline evidence harness.
- Current + fixed-revision replay: PASS; schema, README `--check`, and the complete harness exit 0
  in the post-doc checkout and in a clean detached local clone at `a1c8673`; the clone remains clean.
- Protected restart manifest: PASS; 160 current post-doc files outside Task Board/RF/EV/harness
  retain aggregate `ce33b08d4ca36ad2aeb94e95966152a642d6e276327628ec9315090b6152c368`.
- Framework adapter manifest: PASS; 12 `/tfw-*` files retain aggregate
  `288fde38245a27073e9b703af05c2f936a31418f3206aff42b475eb39be933ce`.
- Formal REVIEW traces: PASS; the original `REVISE`, Iteration 2 `APPROVE`, and binding Iteration 3
  `REVISE` plus all three stage-file sets remain unchanged by this Executor revision.
- `git diff --check`: PASS. Tags remain absent. No network, browser, project command, release,
  release commit, tag, push, destructive restore or broad staging occurred.

During the original execution, a first read-only protected-hash diagnostic used newer .NET APIs
unavailable in the installed Windows PowerShell runtime and exited with method errors. It made no
file, process, network or repository-state change; the PowerShell-5-compatible rerun succeeded.

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [Phase C EV](evidence/EV__phase-c__pipeline_tooling.md) for environment, per-AC results,
sanitized synthetic fixtures, command output and bounded-state comparisons.

Evidence verdict: 0/7 VERIFIED, 1 DEFERRED, 0 BLOCKED, 6 N/A

## 6. Observations (out-of-scope, not modified)

No new observations. Existing TD-5, TD-10 and TD-11 remain open and unchanged; Phase C's bounded
evidence harness intentionally does not present itself as the missing general script test suite.

## 7. Fact Candidates

No fact candidates. Execution produced deterministic repository observations, not new
human-supplied domain facts.

## 8. Strategic Insights (Execution)

No strategic insights. The user supplied workflow authority and status directives, not new domain
knowledge requiring synthesis.

## 9. Diagrams

```text
data/communities.json
        │
        ├── validate_schema.py ──┐
        │                        ├── offline CI: schema + README --check
        ├── generate_readme.py ──┘
        │           │
        │           └── README.md (generated only)
        │
        └── validate_links.py (future authorized CL observation/update)
                    ▲
                    │
              /kz-stats ── owner evidence triage
                    │
                    └── /kz-release ── hard stop ── owner approval ── tag/push

Phase C boundary: everything left of external observation; no live/browser/release action.
Phase D next: authorized Telegram verification and evidence collection.
```

---

*RF — TFW-4 / Phase C: Pipeline & Tooling | 2026-08-27*

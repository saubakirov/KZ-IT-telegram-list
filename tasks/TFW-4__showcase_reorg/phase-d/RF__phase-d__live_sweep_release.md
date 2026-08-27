# RF — TFW-4 / Phase D: Live Sweep & First Release

> **Date**: 2026-08-27
> **Author**: saubakirov (via Codex)
> **Status**: 🟠 RF — G2 checkpoint complete; G3–G4 deferred
> **Parent HL**: [Phase D HL](HL__phase-d__live_sweep_release.md)
> **TS**: [TS Phase D](TS__phase-d__live_sweep_release.md)
> **Completion boundary**: This is not a Phase D completion claim. No `/kz-release`, local release commit, tag, push, or publication was authorized.

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `evidence/g2_recheck_summaries.json` | Reversible byte-preserving aggregate for the retained `datanomika` and fresh `kzquake` raw rechecks |
| `evidence/EV__phase-d__live_sweep_release.md` | Per-AC evidence index, commands, snapshots, hashes, coverage, and deferred authority gates |
| `RF__phase-d__live_sweep_release.md` | Truthful non-completion G2 execution checkpoint |

### Modified Files

| File | Changes |
|------|---------|
| `data/communities.json` | Retained the successful `datanomika` repair; completed the exact verified `kzquake` repair; moved the two independently evidenced, owner-approved dead communities into archive |
| `README.md` | Regenerated end to end by the committed v2 generator from the final G2 data |

The authoritative Phase D lifecycle was already `RF` at resume. Its status, four journal events,
and current generated portfolio index were validated and left unchanged by this execution turn.

## 2. Key Decisions

1. Preserved the successful `datanomika` checkpoint and its exact external raw bytes instead of
   rerunning it.
2. Used the reconciled PS5-safe fixed-root/GUID snapshot guards and exactly one fresh
   `python -X utf8` invocation for `kzquake`. Only machine-observed count/date and metadata were
   accepted after the unchanged target-bound channel predicate passed.
3. Constructed and verified the durable G2 aggregate before either archive, as required by TS §6;
   the immutable G1 and `cursor_kz` evidence files stayed byte-exact.
4. Applied the two archive decisions sequentially only after the local-date gate passed. Each
   command had an independent external candidate snapshot and exact owner-approved reason and
   evidence reference. `mobile_dev_kz` was not treated as a repair.
5. Stopped before G3/G4. AC-6 through AC-8 remain deferred where they depend on `/kz-release`,
   publication approval, or final project-memory closure.

## 3. Acceptance Criteria

- [x] AC-1 — approved protected execution baseline and v2 task-state guard verified.
- [x] AC-2 — immutable G1 summary plus the exact `cursor_kz` supplement cover the pre-G2 manifest.
- [x] AC-3 — every G1 unresolved row has one retained exact retry and bounded fallback evidence.
- [x] AC-4 — both exact repairs and both exact archives have evidence-backed owner dispositions and passed their candidate predicates.
- [x] AC-5 — final schema, evidence coverage, generator write/currency, protected hashes, and diff gates passed.
- [ ] AC-6 — DEFERRED: `/kz-release` was not invoked; no changelog snapshot or local release commit exists.
- [ ] AC-7 — DEFERRED: no exact publication approval exists; no tag or push occurred.
- [ ] AC-8 — DEFERRED: protected v2 state passed, but completion memory/debt transitions and task closure wait on AC-6/AC-7 and the frozen Master DoD.

## 4. Verification

- Lint (`python scripts/validate_schema.py`): PASS, exit `0`.
- Tests (`python scripts/validate_links.py`): the generic catalog-wide command was not rerun because
  TS permits no extra live sweep at this checkpoint. The retained G1 suite plus the sole approved
  `kzquake` UTF-8 retry and both exact archive commands all satisfy the phase-specific test gates.
- Verify (`python scripts/validate_schema.py` plus generator write): PASS, exit `0` for each command.
- Currency (`python scripts/generate_readme.py --check`): PASS, exit `0`.
- G2 aggregate base64/strict-UTF-8/byte/hash/source/deep-equality verifier: PASS.
- Manifest, retry, final-live evidence, four-disposition, date, protected-hash, and unchanged-record reconciliation: PASS.
- Diff whitespace (`git diff --check -- data/communities.json README.md`): PASS.
- v2 state (`python docs/scripts/gen_index.py --validate`): PASS.
- Derived index (`python docs/scripts/gen_index.py --check`): PASS.

One initial read-only Python aggregate-checker command hit Windows native-argument quoting before
it could open the aggregate. It mutated nothing. The strict PowerShell verifier passed the same
required predicates immediately afterward.

## 5. Evidence

See [EV file](evidence/EV__phase-d__live_sweep_release.md) for evidence details.

Evidence verdict: 5/8 VERIFIED, 3 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | domain | The owner directly checked Telegram and reported that the historical `mobile_developers_kz` and `kzqacommunity` communities no longer exist; RES3 supplies the historical-record binding used by the exact archive decisions | Phase D TS §6 owner death evidence binding; source task `01a03eef-e770-7271-82e3-727586c7d274` | High |

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW-4 / Phase D: Live Sweep & First Release | 2026-08-27*

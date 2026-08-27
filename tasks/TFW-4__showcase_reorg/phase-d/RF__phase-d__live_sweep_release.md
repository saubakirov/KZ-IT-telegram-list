# RF — TFW-4 / Phase D: Live Sweep & First Release

> **Date**: 2026-08-27
> **Author**: saubakirov (via Codex)
> **Status**: ✅ RF — Phase D complete; verified snapshot published
> **Parent HL**: [Phase D HL](HL__phase-d__live_sweep_release.md)
> **TS**: [TS Phase D](TS__phase-d__live_sweep_release.md)
> **Completion boundary**: The verified snapshot was committed as `ee2e4f8f69b7bfc66b905801f950d8e832caa02f`, tagged `data-2026-08-27`, and published under the owner's explicit compact-history and push instruction.

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
| `CHANGELOG.md` | Added the evidence-bound `data-2026-08-27` catalog snapshot entry |

The release history was compacted into one commit per TFW-4 phase. The Phase D snapshot commit is
the annotated release target; the task-closing trace is intentionally a later commit so the tag
continues to identify the exact catalog snapshot.

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
5. Completed G3/G4 under the owner's direct instruction: prepared the dated changelog, created the
   reviewed Phase D snapshot commit, created the annotated tag, and pushed `master` plus the tag
   with an exact force-with-lease correction after detecting Git newline normalization in one raw
   evidence blob. Project memory and lifecycle closure were then completed in the task-closing commit.

## 3. Acceptance Criteria

- [x] AC-1 — approved protected execution baseline and v2 task-state guard verified.
- [x] AC-2 — immutable G1 summary plus the exact `cursor_kz` supplement cover the pre-G2 manifest.
- [x] AC-3 — every G1 unresolved row has one retained exact retry and bounded fallback evidence.
- [x] AC-4 — both exact repairs and both exact archives have evidence-backed owner dispositions and passed their candidate predicates.
- [x] AC-5 — final schema, evidence coverage, generator write/currency, protected hashes, and diff gates passed.
- [x] AC-6 — the evidence-bound root changelog and local Phase D snapshot commit were created.
- [x] AC-7 — owner-authorized annotated tag `data-2026-08-27` and `origin/master` publication succeeded; the only rewritten refs used exact `--force-with-lease` expectations to preserve the approved raw evidence bytes.
- [x] AC-8 — final review, knowledge/debt transitions, authoritative task states, journals, and derived index are complete.

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
- Publication (`git ls-remote origin refs/heads/master refs/tags/data-2026-08-27`): PASS;
  the remote branch and peeled annotated tag identify the reviewed snapshot commit.

One initial read-only Python aggregate-checker command hit Windows native-argument quoting before
it could open the aggregate. It mutated nothing. The strict PowerShell verifier passed the same
required predicates immediately afterward.

## 5. Evidence

See [EV file](evidence/EV__phase-d__live_sweep_release.md) for evidence details.

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | domain | The owner directly checked Telegram and reported that the historical `mobile_developers_kz` and `kzqacommunity` communities no longer exist; RES3 supplies the historical-record binding used by the exact archive decisions | Phase D TS §6 owner death evidence binding; source task `01a03eef-e770-7271-82e3-727586c7d274` | High |

> fact-candidates: processed 2026-08-27

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW-4 / Phase D: Live Sweep & First Release | 2026-08-27*

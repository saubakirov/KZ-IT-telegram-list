# Phase HL — TFW-4 / Phase C: Pipeline & Tooling

> **Date**: 2026-08-27
> **Author**: Coordinator (Codex)
> **Status**: 🟡 TS_DRAFT — derivation approved; Phase C TS approved
> **Contract**: DERIVATION-ONLY — inherits frozen Master HL baseline `d31e60d`
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Authority**: The owner's standing authorization permits this strictly derived local Phase C
> plan and approval. This phase does not authorize Phase D, a live sweep, browser use, release,
> tag, or push.
> **Project North Star**: `README.md § Purpose`, sourced from `data/communities.json#north_star`;
> Phase C establishes the generated README locus without changing the approved text.

> This Phase HL adds execution context only. It does not define an independent vision,
> acceptance contract, failure contract, or principles; Master HL §§1, 5, 6, and 7 remain the
> sole authority, per `conventions.md` §3 rules 20–21.

---

## 2. Phase Context

### Knowledge Gate

`current_seq - last_consolidation_seq = 4 - 0 = 4`, below the configured hard interval of 5.
Knowledge consolidation is not due and does not block Phase C.

### Pre-TS Gate

Phase C depends on the completed Phase B result, not on the earlier Phase B plan.

| Gate input | Actual result | Bearing on Phase C |
|------------|---------------|--------------------|
| [Phase B RF](../phase-b/RF__phase-b__contract_docs.md) | All five Phase B ACs complete after the bounded revision; no scope or implementation deviation | `north_star`, the canonical agent contract, release policy, root changelog, and D8–D12 are real predecessor inputs |
| [Phase B repeat REVIEW](../phase-b/REVIEW__phase-b__contract_docs.md) | `✅ APPROVE`; every Judge row passes | Phase B is an accepted predecessor and Phase C may start planning |
| Phase B docs state | `tfw-docs: Applied`; `tfw-knowledge: N/A`; `KNOWLEDGE.md` indexes D8–D12 once | Phase C appends only D13–D14 and does not repeat Phase B documentation |
| Task Board | TFW-4 remains open with “Phase C next” | The master task advances to Phase C TS approval, not task completion |
| Phase B debt | TD-10 and TD-11 remain open Medium adapter debt | Both are explicitly outside Phase C; no adapter-source or framework repair is permitted |
| Master amendments | A5 and A6 are approved in baseline `d31e60d` | C4 contact shells remain ambiguous; attribution uses the actual executing product |

Phase A was consulted only for the inherited attribution history: its RF/REVIEW exposed the
actor-token conflict that A6 resolved. No Phase A deliverable or file enters Phase C scope.

### Current Tooling Facts

| Path | Current fact | Phase C derivation |
|------|--------------|--------------------|
| `data/communities.json` | Contains the exact approved `north_star`; has no `archive` key; all live verification dates still share the pre-sweep value | Add only an empty archive container; do not alter any live catalog fact |
| `scripts/validate_schema.py` | Validates live entries and categories only; ignores `north_star`, archive integrity, and freshness reporting | Add the frozen schema and reporting gates |
| `scripts/validate_links.py` | Treats marker-free HTTP 200 as alive, parses page-wide member-like prose, and refreshes dates only when a count parses | Implement A5-safe classification, independent date/count updates, explicit archive handling, and a machine-readable summary |
| `scripts/generate_readme.py` | Sorts categories by key, emits count-only stats, ignores `north_star`/archive, and imports unused `datetime` | Render the approved presentation and provide an offline currency check |
| `.claude/commands/` | Contains only framework `tfw-*` adapters | Add project-owned `kz-stats` and `kz-release` files without modifying any `tfw-*` file |
| `.github/workflows/` | Absent | Add the approved offline validation workflow |
| `README.md` | Generated artifact; Phase B left it byte-identical | Regenerate through the generator only; presentation diff must not change a live entry fact |

## 3. Derived Phase Outcome

Phase C turns the Phase B contract into an offline-verifiable pipeline and project operation
surface while leaving every live Telegram fact for Phase D:

```text
BEFORE                                      AFTER PHASE C
north_star stored but not enforced          schema-required and rendered as README Purpose
no archive container or integrity rules     empty archive + validated archive contract
HTTP 200 means “alive”                      target preview / ambiguous / failure separated
count parser scans generic page prose       count parsed only inside target preview evidence
date update depends on a numeric count       verified target gets a date; count stays optional
README categories sort by key               TOC/body sort by display name with valid anchors
README has no freshness/category signal      derived categories + oldest live verification date
no project operation adapters               /kz-stats + /kz-release are defined in CL mode
no pull-request validation                  offline schema + README-currency CI gate
manual README write                         generator write + non-mutating --check path
```

Derived deliverables:

1. Extend `data/communities.json` only with an empty `archive` array and make
   `validate_schema.py` enforce the approved North Star/archive contract while reporting stale
   live-entry dates without failing merely for age.
2. Make `validate_links.py` classify target-specific previews, ambiguous contact shells,
   generic pages, and explicit failures safely; update verified dates independently of count
   parsing; maintain `meta.last_updated`; support explicit evidence-backed archiving; and emit a
   machine-readable run summary.
3. Make `generate_readme.py` render Purpose, derived category/freshness statistics,
   display-name category ordering, correct current anchors, and conditional collapsed archive;
   add a normalized, non-mutating README currency check and regenerate `README.md` only through
   the script.
4. Create `.claude/commands/kz-stats.md` and `.claude/commands/kz-release.md` as project commands.
   They preserve owner triage and stop-before-tag/push authority gates and do not modify any
   framework command.
5. Create `.github/workflows/validate.yml` for offline schema and README-currency validation on
   pull requests and pushes to `master`.
6. Record D13–D14 and resolve only the tooling debt actually delivered by Phase C (TD-3 and
   TD-6). TD-5, TD-10, and TD-11 remain open and unchanged in disposition.

The browser fallback is specified for later CL evidence collection: only a visible,
target-specific Telegram preview can supplement an inconclusive scripted response; a generic
contact shell cannot. One temporary tab is reused sequentially and closed when the batch or
evidence collection ends. Phase C itself opens no browser and makes no Telegram request.

## 4. Scope, Sequence, and Files

| Path | Phase action | Boundary |
|------|--------------|----------|
| `data/communities.json` | MODIFY | Add only an empty top-level `archive` array; preserve every existing value |
| `scripts/validate_schema.py` | MODIFY | North Star/archive validation and non-fatal freshness report |
| `scripts/validate_links.py` | MODIFY | Safe classifier, update/archive semantics, and machine-readable summary |
| `scripts/generate_readme.py` | MODIFY | Generated presentation plus normalized `--check` behavior |
| `.claude/commands/kz-stats.md` | CREATE | CL statistics/sweep adapter with owner triage and future browser-evidence fallback |
| `.claude/commands/kz-release.md` | CREATE | CL release preparation adapter with hard stop before tag/push |
| `.github/workflows/validate.yml` | CREATE | Offline schema and README-currency validation |
| `README.md` | MODIFY (GENERATED) | Regenerated output only; presentation-only catalog diff |
| `KNOWLEDGE.md` | MODIFY | Append D13–D14 only |
| `TECH_DEBT.md` | MODIFY | Resolve TD-3 and TD-6 only; preserve TD-5/TD-10/TD-11 |

Sequence constraints derived from the cascade:

1. Snapshot the current dirty/protected paths and semantic catalog state before overlapping
   edits; do not reconstruct from `HEAD` or broadly stage the working tree.
2. Establish the archive/schema and classifier contracts before relying on them in commands or
   generated presentation.
3. Regenerate `README.md` through the finished generator, then use its non-mutating check in the
   command adapter and CI.
4. Verify every Phase C outcome offline. Do not invoke either project command, run the network
   validator against Telegram, open a browser, or perform release actions.

### Scope Budget

| Measure | Estimate | Limit | Result |
|---------|----------|-------|--------|
| Implementation files | 10 total | 30 | Within budget |
| New implementation files | 3 | 15 | Within budget |
| Modified implementation files | 7 | 30 | Within budget |
| Estimated implementation delta | <2000 LOC | 3000 LOC | Within budget |
| Full phase trace + implementation new files | 12 maximum | 15 | Within budget |
| Full phase trace + implementation paths | 19 maximum | 30 | Within budget |

No budget override, additional phase, or delegated scope extension is required.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Frozen Master HL including approved A5/A6 | ✅ baseline `d31e60d` |
| Phase B RF | ✅ complete after bounded revision |
| Phase B repeat REVIEW | ✅ `APPROVE` |
| Phase B docs and board state | ✅ applied; Phase C is next |
| `north_star` structured data | ✅ present with the approved text |
| Project release policy | ✅ `RELEASE.md` exists; it is an input, not release authorization |
| Research H1/H4 | ✅ public preview/count boundary and current emitted anchors are sufficiently resolved for offline implementation |
| Owner authorization for strictly derived local Phase C planning/execution | ✅; excludes this phase from live state, browser, release, tag, and push actions |
| Telegram/network/browser availability | N/A for Phase C; future Phase D CL evidence only |
| GitHub Actions remote run | ⬜ unavailable until a later authorized push; local equivalent is mandatory in Phase C evidence |

## 9. Phase Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| A marker-free contact shell is dated as a verified community | Observed predecessor defect | High — the catalog asserts an unobserved fact | A5 classifier states plus inline C3/C4/C5 offline evidence; ambiguous never dates or auto-archives |
| Generic Telegram prose yields a false member count | Observed predecessor defect | High — fabricated catalog data | Count extraction is scoped to target-specific preview content and C5 must return no count |
| The archive operation converts a broken link into a death claim | Medium | High — living community is misclassified | Explicit per-handle owner/evidence triage; repair/death/unresolved branches; no automatic archive |
| README freshness wording overstates a partial run | Medium | High — public accuracy claim is misleading | Render the oldest live `last_verified` date, not a hand-maintained or optimistic literal |
| README currency behaves differently on Windows and CI | Medium | Medium | Compare UTF-8 generated/current content in memory with normalized line endings |
| Command files imply they were executed or authorize a release | Medium | High | Static adapter verification only; Phase C does not invoke them; release command contains a hard stop |
| CI accidentally runs the Telegram validator | Low | High — flaky external-state gate | Workflow permits only schema and generator currency checks; scan for network validator invocations |
| Phase C repairs TD-10/TD-11 while touching adjacent adapter paths | Medium | Medium — scope and ownership violation | Protect `.agents/**` and `.tfw/**`; leave both debt rows open and unchanged |
| Generated README diff changes a live catalog fact | Medium | High — presentation/data boundary collapses | Compare all live-entry semantic fields before/after and reject any entry name, handle, description, count, or date change |

---

*Phase HL — TFW-4 / Phase C: Pipeline & Tooling | 2026-08-27*

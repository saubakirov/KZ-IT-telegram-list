# Verify — TFW-4 / Phase C: Post-doc Reproducibility Audit
> **Mindset:** Auditor. A command labelled reproducible must run from the provenance it names.
> **Min verify ratio:** 0.42
> **RF files claimed:** 14
> **Files required by ratio:** ⌈14 × 0.42⌉ = 6
> **Files actually re-verified:** 14/14; the discrepancy triggered 100% coverage

## Verification Log

### V1: `data/communities.json`
- **RF claim:** Phase C added only `archive: []` and preserved all live facts.
- **Actual:** Production schema still exits 0; the harness parses the same production data and
  passes its full AC-1 matrix before reaching the later memory failure.
- **Match:** ✅

### V2: `scripts/validate_schema.py`
- **RF claim:** North Star/archive/date integrity is fatal while valid staleness is non-fatal.
- **Actual:** Direct execution exits 0 with 63 stale dates reported and zero errors; all isolated
  AC-1 negatives pass in the harness.
- **Match:** ✅

### V3: `scripts/validate_links.py`
- **RF claim:** Authoritative target binding, identity-decoy/conflict rejection, update/archive
  guards, and summary behavior pass offline.
- **Actual:** The direct harness reaches and passes C3/C4/C5, identity decoy, authoritative
  conflict, non-mutation, summary/update/archive, and AC-2 final markers.
- **Match:** ✅

### V4: `scripts/generate_readme.py`
- **RF claim:** Renderer and non-mutating currency behavior pass.
- **Actual:** Direct `--check` exits 0; the harness passes the AC-3 renderer/currency matrix.
- **Match:** ✅

### V5: `.claude/commands/kz-stats.md`
- **RF claim:** The future CL operation contains evidence, retry, four-way triage, browser cleanup,
  and owner/archive gates.
- **Actual:** The unchanged static command matrix passes before the memory failure.
- **Match:** ✅

### V6: `.claude/commands/kz-release.md`
- **RF claim:** The future release operation validates completeness and stops before tag/push.
- **Actual:** The unchanged static command matrix passes; the command was not invoked.
- **Match:** ✅

### V7: `.github/workflows/validate.yml`
- **RF claim:** CI contains only offline schema and README-currency checks.
- **Actual:** YAML parsing and the forbidden-operation scan pass; exact local commands exit 0.
- **Match:** ✅ locally; remote run remains `DEFERRED`

### V8: `README.md`
- **RF claim:** The generated artifact is current and preserves live facts.
- **Actual:** `python -B scripts/generate_readme.py --check` exits 0.
- **Match:** ✅

### V9: `KNOWLEDGE.md`
- **RF claim:** D1–D12 retain predecessor meaning, D13–D14 occur once, and D15 is absent.
- **Actual:** All keyed decisions satisfy those semantic conditions. Authorized `/tfw-docs`
  additions to §§1–3 change unrelated architecture, operational-contract, artifact, and legacy
  text. Removing only D13–D14 from the current file yields SHA-256 `dfc8641a…`, not the harness
  constant `5190da19…`.
- **Match:** ✅ semantically; ❌ under the harness's whole-document byte check

### V10: `TECH_DEBT.md`
- **RF claim:** Only TD-3/TD-6 are resolved by Phase C; deferred debt retains its disposition.
- **Actual:** The keyed debt portion of `run_memory_matrix()` is not reached because the earlier
  knowledge hash aborts. Direct inspection confirms the documented Phase C dispositions; this
  reproducibility finding is immediate rework, not deferred debt.
- **Match:** ✅ content; ⚠️ not reached by the published full-harness result

### V11: `tasks/README.md`
- **RF claim:** The board preserves Phase C history and Phase D authority boundaries.
- **Actual:** Before this audit it recorded Phase C complete and Phase D draft approval pending.
  The post-doc finding requires a new additive `REVISE` routing while leaving Phase D drafts
  unapproved and unchanged.
- **Match:** ❌ stale relative to the new verdict; Reviewer trace update required

### V12: `ONB__phase-c__pipeline_tooling.md`
- **RF claim:** It supplies reproducible predecessor snapshots.
- **Actual:** ONB records only the abbreviated initial `KNOWLEDGE.md` hash and describes dirty
  predecessor state. The full expected digest appears only as a literal in the harness; no
  checked-in byte snapshot or exact reconstruction command resolves it.
- **Match:** ⚠️ sufficient for the original working session, insufficient as durable provenance

### V13: `evidence/offline_harness.py`
- **RF claim:** Direct execution reproduces AC-1 through AC-6 and exits 0.
- **Actual:** Current checkout exits 1 at `run_memory_matrix()` after AC-1–AC-5 pass. A clean local
  clone detached at lifecycle snapshot `a141f7c` also exits 1 at the same assertion. In that
  snapshot, removing D13–D14 yields durable predecessor hash `02bef456…`, still not `5190da19…`.
- **Match:** ❌

### V14: `evidence/EV__phase-c__pipeline_tooling.md`
- **RF claim:** “Run from the repository root” is the reproducible harness invocation.
- **Actual:** The unqualified command fails in the current checkout. The EV names no commit,
  worktree overlay, newline convention, predecessor snapshot, or reconstruction step that makes
  the expected hash resolvable.
- **Match:** ❌

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -B scripts/validate_schema.py` | PASS, exit 0 |
| 2 | `python -B scripts/generate_readme.py --check` | PASS, exit 0 |
| 3 | `python -B tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` | FAIL, exit 1 after AC-1–AC-5; `AssertionError: D1-D12 and predecessor knowledge must match ONB` |
| 4 | Clean local clone, detached `a141f7c`, same harness command | FAIL, exit 1 at the same assertion |
| 5 | Post-doc `git diff -- KNOWLEDGE.md` plus keyed/hash audit | Authorized §§1–3 additions identified; current minus D13/D14 = `dfc8641a…`; `a141f7c` minus D13/D14 = `02bef456…`; neither equals `5190da19…` |
| 6 | Repository search for the full expected digest | The full digest resolves only to `offline_harness.py`; no content snapshot or reproducible invocation resolves it |

No network, Telegram, browser, project command, Phase D, release, tag, or push action ran. The
temporary clean clone contained no unique data and was removed after the audit.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “Full offline replay … AC-1…AC-6 harness … pass” | RF §4 | Direct current-checkout harness | ❌ — exits 1 in AC-6 memory matrix |
| C2 | “Run from the repository root” reproduces the harness | EV Reproducible Harness | Current checkout and clean `a141f7c` snapshot | ❌ — both exit 1; no qualifier repairs provenance |
| C3 | Production schema/README and identity regressions remain green | RF §4 / EV E1–E3 | Direct commands and pre-failure harness output | ✅ — functional Phase C behavior remains intact |

All artifact links used by this addendum resolve. The frozen baseline is recoverable at
`d31e60d`; the Phase C lifecycle snapshot is recoverable at `a141f7c`; neither resolves the
ONB-era expected predecessor bytes. The existing 41/41 Master/ONB knowledge citations remain
present; no citation hallucination is introduced by the post-doc change.

## Discrepancies Found

### P2 — Published Phase C harness is not reproducible from either documented current-checkout or durable snapshot provenance

`offline_harness.py:627–647` removes D13–D14 and hashes every remaining byte of mutable
`KNOWLEDGE.md` against `5190da19…`. `EV__phase-c__pipeline_tooling.md:182–188` publishes a direct
repository-root command with no snapshot qualifier. Authorized post-doc updates therefore break
the advertised command, and the strongest natural snapshot (`a141f7c`) also fails because the
expected ONB-era bytes are not preserved by a resolvable artifact. This is a reproducibility
defect in Phase C evidence, not a production schema/classifier/generator defect.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV E1 / schema matrix | ✅ | ✅ — reproduces before the later memory failure |
| E2 | EV E2 / classifier/update/archive matrix | ✅ | ✅ — identity and mutation regressions reproduce |
| E3 | EV E3 / generator and README matrix | ✅ | ✅ — direct currency and renderer gates reproduce |
| E4 | EV E4 / command and adapter matrix | ✅ | ✅ — static matrix reproduces; no invocation claimed |
| E5 | EV E5 / CI definition | ✅ | ✅ locally; remote run remains honestly `DEFERRED` |
| E6 | EV E6 / decision and debt matrix | ✅ | ❌ — direct harness aborts before the claimed matrix completes |
| E7 | EV E7 / bounded state and history | ✅ | ⚠️ production/history claims remain supported, but the advertised full replay is not |

Evidence presence is 7/7. Evidence sufficiency is 5/7 full, 1/7 partial, and 1/7 failed for the
post-doc reproducibility claim.

## Knowledge Citations Verified

| # | Artifact | Citation set | Link resolves? | Item exists? |
|---|----------|--------------|----------------|--------------|
| 1 | Master HL §7.2 #1–20 | North Star, TFW principles, KNOWLEDGE P/D rows, conventions | ✅ | ✅ |
| 2 | ONB §7 #1–21 | Master citation set plus Phase B predecessor | ✅ | ✅ |

Total citation rows: 41; verified: 41; hallucinations: 0.

## Checkpoint

**Self-check:**
- [x] Rechecked all 14/14 RF-claimed paths after the discrepancy?
- [x] Ran production gates and both current/snapshot harness reproductions?
- [x] Spot-checked the three load-bearing claims against direct output and Git provenance?
- [x] Verified every AC's relevant evidence boundary and isolated the AC-6/AC-7 defect?
- [x] Checked current KNOWLEDGE/TECH_DEBT and the post-doc diff?
- [x] Verified knowledge citations and all seven evidence rows?

Stage complete: YES


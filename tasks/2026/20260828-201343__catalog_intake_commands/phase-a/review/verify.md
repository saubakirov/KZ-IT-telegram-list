# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 24 (13 implementation paths and 11 RF-created evidence paths)
> Files to verify: ⌈24 × 0.42⌉ = 11; all 24 claimed paths and the two supporting public commitment/input artifacts were audited.

## Verification Log

### V1: correction integration and exact implementation binding

- **RF claim:** Final implementation is
  `9185811696c762b5261e9b90f71bee846b6fc692`, and the bounded F2a loop changes only
  `scripts/kz_intake.py` and `scripts/test_kz_intake.py`.
- **Actual:** The four authorized Executor commits applied cleanly in their declared order onto
  Reviewer base `e91d2aaff22b3d9d9e9137e7a15d15da85fc3aa2`, producing integrated RF base
  `24f9e2de000b8c07d061388ffb878ca72192fff6`. Stable patch IDs match each supplied commit exactly,
  and the integrated tree is byte-identical to Executor tip
  `1be9412c03962cd159b528a66603c4dd00af2b30`. All 13 current implementation paths are byte-identical
  to final implementation `91858116…`; its delta from prior implementation `731b3d6a…` is exactly
  38 insertions and one deletion across only the two named files.
- **Match:** ✅

### V2: `scripts/kz_intake.py` — F2a and exact producer tuple audit

- **RF claim:** Failed HTTP observations reject every 2xx status; fetched 2xx remains valid only as
  `ok=true, reason=fetched` at attempts 1–3; all other terminal/retry families remain exact.
- **Actual:** A standalone producer/consumer harness constructed observations through
  `observe_candidate` and then called production `validate_observation`, independent of the unit
  test assertions. Results:

  ```text
  FAILED_2XX_REJECTED=100/100
  FETCHED_2XX_ACCEPTED=300/300
  OUTSIDE_ATTEMPT1_ACCEPTED=11/11
  OUTSIDE_ATTEMPTS_2_3_REJECTED=22/22
  RETRY_TERMINAL_ACCEPTED=3/3
  RETRY_EARLY_REJECTED=6/6
  HTTP_429_REJECTED=3/3
  WRONG_SUCCESS_REJECTED=5/5
  ```

  The exhaustive sets cover failed status 200 through 299 and fetched status 200 through 299 at
  each attempt 1, 2, and 3. Outside-2xx boundaries include 100/199/300/301/399/400/404/428/430/
  500/599. URL/general errors and `max_retries_exceeded` accept only attempt 3; `http_429` accepts
  no attempt. Success rejects outside-2xx status, wrong reason, and attempt 0/4.
- **Match:** ✅ — F2a is closed without narrowing any valid producer family.

### V3: direct D1–D3 and F1/F2 action/authority reproduction

- **RF claim:** Every earlier formal-review exploit remains closed under the real project gates.
- **Actual:** A separate temporary-project harness exercised production functions directly:
  - D1: `https://t.me./valid_name` remains `spoofed_authority` with no candidate;
  - D2: Boolean integer, blank evidence, arbitrary verified reason, and target-unbound verified
    result mutations all reject;
  - D3: neutral-state first apply reproduced `[B,N,B,B,B] -> applied_exact`, exact rerun
    `[A,N,A,A,A] -> already_applied_exact`, and marked recovery
    `[B,N,A,B,B] -> recovered_exact`, with the neutral path unchanged;
  - original F1: an unrelated schema/generator-valid catalog/projection delta rejects before
    preview/marker/write;
  - original F2: target-unbound/arbitrary classifier facts and impossible failed-transport facts
    reject; the exact retry families are covered in V2;
  - semantic-only zero-ADD JSON reserialization passes the real schema/generator preflight but is
    rejected as not the exact action result; root bytes stay unchanged and no marker appears;
  - exact zero ADD returns `already_applied_exact` with zero IDs and byte-identical controlled
    paths;
  - exact one/two ADD stages equal an independently constructed baseline-plus-row object plus only
    the two mechanical locale-review bindings, retain UTF-8 `indent=2` JSON, exactly one LF and no
    CR, and pass the real schema/generator preflight;
  - one ADD produces counts `en:140,ru:132,kk:132`, `changed_key_count=404`, matching digest, and
    `applied_exact` for one ID;
  - two ADDs produce `en:141,ru:133,kk:133`, `changed_key_count=407`, matching digest; injected
    projection-first failure leaves the catalog baseline intact and retry returns
    `recovered_exact` for both IDs.

  Production controlled hashes before and after the complete harness were identical.
- **Match:** ✅ — D1–D3 and all prior F1/F2/action-stage findings remain closed.

### V4: `scripts/validate_schema.py`

- **RF claim:** Locale cardinality is independently data-derived, digest binding remains exact,
  and baseline output remains truthful.
- **Actual:** `expected_locale_payload_counts` derives counts from current categories, live and
  archive entries, locale non-goals, and fixed UI registries rather than the generated payload or
  old `139/131/131` constants. Direct 0/1/2-row projects reproduced structural counts exactly and
  retained independent canonical payload digest/key checks. Current validation reports
  `en:139,ru:131,kk:131`, digest `51db402d…`, and zero errors.
- **Match:** ✅

### V5: classifier/predecessor preservation

- **RF claim:** The fetch seam leaves all six classifier authority bodies and predecessor behavior
  unchanged.
- **Actual:** AST source segments for `TelegramPreviewParser`, `parse_member_count`,
  `handle_from_url`, `observed_preview_type`, `result`, and `classify_response` are byte-for-byte
  equal between base `be830d3766ca4de12ff18198a680253ed133894f` and final implementation
  `9185811696c762b5261e9b90f71bee846b6fc692`. Direct Phase C `run_link_matrix` and
  `run_command_matrix` pass retry, identity decoy/conflict, summary/update/archive, type mismatch,
  failure, stats, and release behavior.
- **Match:** ✅ — D1/D2 classifier and predecessor closures remain exact.

### V6: command inventory and fresh runtime evidence

| Pair / file | Bytes | SHA-256 / result |
|---|---:|---|
| `AGENTS.md` | 8,768 | `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612` |
| `kz-add` pair | 5,331 each | `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414` |
| `kz-stats` pair | 3,761 each | `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe` |
| `kz-release` pair | 3,532 each | `2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc` |
| Claude smoke | 13,602 | `55871364d401e6afd55138b0f015dbdd7cca47100d8c4700c0fae64d58ee8f89` |
| Codex smoke | 4,896 | `9e67f40e970c098a602e5d44318f9eac1048946d88be23850d46142cbb8e85bc` |

All seven routing/runtime bytes match smoke SHA `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`, final
implementation, integrated RF base, and the current tree. Static parity, completeness, path
neutrality, and sync direction pass. The three accepted Claude records each have exit 0, one turn,
zero tool/server/web steps, equal before/after state, and explicit no-network/no-write/no-external-
mutation effects; three excluded attempts remain marked unacceptable. The Codex artifact retains
the explicit absolute loaded paths/hashes and complete sentinel/stats/release results. Claude's
no-absolute-path-echo limitation remains accurately bounded rather than overclaimed.
- **Match:** ✅ — D4 and AC-5/AC-7 remain closed; no model rerun was required because command bytes
  did not change.

### V7: public seal and retained calibration

- **RF claim:** Public artifacts bind `29/28/1/8/20`, eight disclosed calibration observations,
  and full partition `5b9fb0dd…` without exposing the holdout.
- **Actual:** Exact artifact hashes reproduce: commitment `f7d4530d…`, calibration input
  `cbdf4f48…`, observations `507938e3…`, and allocation receipt `6febc879…`. The commitment,
  calibration, and receipt bind the same partition digest. Public receipt booleans and totals are
  exact; all eight retained observations and their lossless source validate under the corrected
  consumer without a network rerun. No holdout identity, URL, raw text, case key, score, source
  path, or expected outcome was opened or inspected.
- **Match:** ✅ within the permitted non-revealing public boundary — D5 and AC-6 remain closed.

### V8: exact scope and controlled production hashes

- **RF claim:** Final implementation scope is 13 paths, 8 new/5 modified, 2,406
  insertion-plus-deletion lines; only two implementation paths changed in F2a; production bytes
  remain unchanged.
- **Actual:** Explicit allowlist diff from `be830d3766ca4de12ff18198a680253ed133894f` to
  `9185811696c762b5261e9b90f71bee846b6fc692` reproduces exactly `13 / 8 / 5 / 2406`, below the
  2,500 ceiling. Diff from `731b3d6a…` to `91858116…` names only `scripts/kz_intake.py` and
  `scripts/test_kz_intake.py`. All five production hashes are identical at base, smoke, prior
  implementation, final implementation, integrated RF base, and current tree:

  | Path | SHA-256 |
  |---|---|
  | `data/communities.json` | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` |
  | `README.md` | `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d` |
  | `index.md` | `4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3` |
  | `ru/index.md` | `36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97` |
  | `kk/index.md` | `64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7` |

- **Match:** ✅

### V9: fresh final exact-SHA offline site build

- **RF claim:** Final implementation SHA builds under the digest-pinned official image with no
  network or external mutation and matches retained output bindings.
- **Actual:** A fresh Git archive of `9185811696c762b5261e9b90f71bee846b6fc692` built with the
  already-local official image at digest
  `sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041`, read-only source,
  isolated writable output, and container network disabled. Build and site validation exited 0.
  Output hashes reproduced exactly: EN `64597def…`, RU `fef3499e…`, KK `2d4465e7…`, sitemap
  `79dcb9bb…`; the 11,097-byte generated summary matched retained SHA-256 `bbf30af0…`
  byte-for-byte. The temporary archive/output were automatically removed.
- **Match:** ✅ — D6 remains closed; no image pull, deployment, production write, release, tag,
  push, or external-service mutation occurred.

### V10: full regression and evidence inventory

- **RF claim:** All 45 tests and every deterministic gate pass; all eleven evidence paths support
  eight verified EV rows.
- **Actual:** The complete 45-test generation/intake/command suite passes, as do command parity,
  schema, generator currency, index validation, six-module compile, predecessor matrices, and
  `git diff --check`. All eleven RF-created evidence paths exist. Their hashes, internal bindings,
  final implementation SHA, scope totals, runtime statements, controlled hashes, and build outputs
  match the primary code/Git/generated results above.
- **Match:** ✅

## Commands Executed

| # | Command / audit | Result |
|---|-----------------|--------|
| 1 | Four exact `git cherry-pick` integrations plus tree/stable-patch-ID comparison | PASS — declared order, no conflict/manual edit, integrated tree exact to Executor tip. |
| 2 | Standalone exhaustive failed/fetched HTTP producer matrix | PASS — 100 failed 2xx rejected, 300 fetched 2xx accepted, all terminal/retry constraints exact. |
| 3 | Standalone real-project zero/unrelated/one/two ADD and recovery harness | PASS — exact bytes, real schema/generator, mechanical locale binding, root unchanged. |
| 4 | Standalone neutral-state first/rerun/recovery harness | PASS — `[B,N,B,B,B]`, `[A,N,A,A,A]`, `[B,N,A,B,B]` outcomes exact. |
| 5 | `python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands -v` | PASS — 45 tests. |
| 6 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, locale `139/131/131`, 0 errors. |
| 7 | `python scripts/generate_readme.py --check` | PASS — all four projections current. |
| 8 | `python scripts/sync_kz_commands.py --check` | PASS — exact three-command inventory/parity. |
| 9 | `python docs/scripts/gen_index.py --validate` | PASS — four tasks validate. |
| 10 | Six-module `python -m py_compile` | PASS. |
| 11 | Direct Phase C `run_link_matrix` and `run_command_matrix` | PASS — classifier/retry/identity/update/archive and command behavior. |
| 12 | Classifier source, implementation scope, loop-path, runtime, production, evidence hash audits | PASS — all exact. |
| 13 | Public commitment/calibration/receipt audit and retained observation validation | PASS — exact public bindings/totals, 8/8 observations; holdout unopened. |
| 14 | Fresh digest-pinned official-image build from exact final Git archive, network disabled | PASS — build 0, validation 0, output/summary hashes exact. |
| 15 | `git diff --check`, status, and staging audit | PASS before Reviewer trace writes. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | failed/fetched HTTP families are exactly producer-closed | RF §§1–4 / EV E2 | producer code, consumer predicate, exhaustive standalone matrix, 45-test suite | ✅ |
| C2 | exact zero/one/many action-to-stage/apply behavior | RF §§2–4 / EV E3–E4 | temporary project bytes, independent object derivation, real schema/generator, failure/recovery | ✅ |
| C3 | locale invariant is structurally data-derived | RF §§1–4 / EV E4 | schema source, baseline/1/2-row structural counts and canonical digest | ✅ |
| C4 | classifier and command/runtime behavior is preserved | RF §§2–4 / EV E5/E7 | exact source segments, Git/runtime hashes, predecessor matrices, complete smoke artifacts | ✅ with the stated Claude path-echo limit. |
| C5 | scope, build, and production immutability | RF §4 / EV E8 | Git objects/diffs, exact-SHA offline build, working-tree hashes | ✅ — `13/8/5/2406`, only two F2a paths, controlled bytes exact. |
| C6 | sealed allocation/calibration boundary | RF §4 / EV E6 | public commitment/input/observations/receipt only | ✅ within authority; holdout identities were not inspected. |

All RF/EV, master-HL §7.2, and ONB §7 references resolve. Data and evidence claims were checked
against code, Git objects, public primary artifacts, independently derived temporary states, or
independently generated outputs rather than accepted from the RF summary.

## Discrepancies Found

No material discrepancy. Every contract, TS, evidence, safety, scope, and purpose-relevant claim
holds. Non-blocking trace note: the revised ONB/RF/EV headers say 2026-08-29 while their decorative
footer lines retain the task's original 2026-08-28 date; identities, revisions, evidence bindings,
and lifecycle authority remain unambiguous.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|-----------------|----------------|
| E1 | AC-1 grammar evidence | ✅ | ✅ — direct D1/source probe and full tests reproduce. |
| E2 | AC-2 producer/classifier/calibration evidence | ✅ | ✅ — exhaustive independent tuple matrix and retained observations pass. |
| E3 | AC-3 preview/authority evidence | ✅ | ✅ — recursive closure and exact zero/one/many stage exploits reproduce. |
| E4 | AC-4 apply/hash evidence | ✅ | ✅ — real preflight, neutral paths, catalog-last recovery, exact reruns, and production immutability reproduce. |
| E5 | AC-5 command parity evidence | ✅ | ✅ — inventory, completeness, parity, neutrality, and authority stops reproduce. |
| E6 | AC-6 partition/calibration evidence | ✅ | ✅ — public bindings and totals hold without holdout inspection. |
| E7 | AC-7 Claude/Codex smoke evidence | ✅ | ✅ with recorded limit — complete Claude behavior/static binding and explicit Codex paths. |
| E8 | AC-8 aggregate evidence | ✅ | ✅ — 45 tests, all gates, exact scope/hashes, and fresh final-SHA build reproduce. |

Evidence totals: 8 items, 8 exist, 8 match.

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------|
| 1 | HL §7.2 / ONB §7 | PV0-1 — `README.md` § Purpose | ✅ | ✅ | ✅ — accuracy, inclusion gates, non-goals | ✅ |
| 2 | HL §7.2 / ONB §7 | PV1-1 — `.tfw/README.md` NS2 | ✅ | ✅ | ✅ — purpose, human authority, proportional assurance | ✅ |
| 3 | HL §7.2 / ONB §7 | PV1-2 — `.tfw/README.md` Methodology values | ✅ | ✅ | ✅ — Structural Enforcement and Portability | ✅ |
| 4 | HL §7.2 / ONB §7 | PV2-1 — `knowledge/philosophy.md` absent | N/A as cited | ✅ absent | ✅ — citation records absence | ✅ |
| 5 | HL §7.2 / ONB §7 | PV3-1 — `KNOWLEDGE.md` D1 | ✅ | ✅ | ✅ — JSON source and generated projections | ✅ |
| 6 | HL §7.2 / ONB §7 | PV3-2 — `KNOWLEDGE.md` D2 | ✅ | ✅ | ✅ — offline/live separation | ✅ |
| 7 | HL §7.2 / ONB §7 | PV3-3 — `KNOWLEDGE.md` D4 | ✅ | ✅ | ✅ — categories live in data | ✅ |
| 8 | HL §7.2 / ONB §7 | PV3-4 — `KNOWLEDGE.md` D14 | ✅ | ✅ | ✅ — `kz-*` / `tfw-*` namespaces | ✅ |
| 9 | HL §7.2 / ONB §7 | PV3-5 — `KNOWLEDGE.md` D18 | ✅ | ✅ | ✅ — target-bound exact-universe evidence | ✅ |
| 10 | HL §7.2 / ONB §7 | PV3-6 — `KNOWLEDGE.md` D19 | ✅ | ✅ | ✅ — explicit EN/RU/KK, no fallback | ✅ |
| 11 | HL §7.2 / ONB §7 | PV4-1 — conventions §3 Evidence | ✅ | ✅ | ✅ — evidence differs from verification | ✅ |
| 12 | HL §7.2 / ONB §7 | PV4-2 — conventions §9 | ✅ | ✅ | ✅ — normal thin-adapter rule and approved A1 exception | ✅ |
| 13 | HL §7.2 / ONB §7 | PV4-3 — conventions §11 | ✅ | ✅ | ✅ — no placeholders/manual repair | ✅ |
| 14 | HL §7.2 / ONB §7 | PV4-4 — conventions §14 | ✅ | ✅ | ✅ — no bonus scope/invented evidence | ✅ |
| 15 | HL §7.2 / ONB §7 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | ✅ | ✅ — historical dead entries remain archived | ✅ |

Citation totals: 15, resolved/expected-absent 15, semantically verified 15, irrelevant 0,
hallucinated 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈24 × 0.42⌉ files and recorded findings? All 24 plus two supporting public artifacts.
- [x] Ran at least 1 build/test command? Full tests and a fresh final exact-SHA build both ran.
- [x] Claim & Source Checks filled with primary-source verification?
- [x] Each RF §3 acceptance check verified against actual files?
- [x] KNOWLEDGE.md checked — contradictions documented in Judge?
- [x] All HL §7.2 and ONB §7 citations verified?
  - Total: 15, resolved/expected-absent: 15, semantically verified: 15, irrelevant: 0, hallucinated: 0.
- [x] Evidence artifacts from RF §5 verified?
  - Total: 8, exist: 8, match: 8.

Stage complete: YES

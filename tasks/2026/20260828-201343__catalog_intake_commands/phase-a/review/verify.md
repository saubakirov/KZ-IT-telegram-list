# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 23 (12 implementation paths and 11 RF-created evidence paths)
> Files to verify: ⌈23 × 0.42⌉ = 10; discrepancies were found, so all 23 claimed paths and two supporting public seal artifacts were audited.

## Verification Log

### V1: `scripts/kz_intake.py`

- **RF claim:** The revision derives staged bytes from exactly the fixed ADD rows, enforces an exact
  zero-add no-op, rederives before every write/recovery, writes the catalog last, and accepts only
  producer-possible observation tuples.
- **Actual:** The original F1/F2 counterexamples are closed: an unrelated schema-valid edit in a
  reject-only stage is rejected; target-unbound/arbitrary-reason verified classifier tuples and
  failed transports carrying facts are rejected. Extra/add/edit/delete/reorder/wrong-type/
  changed-proposal/stale-projection and owner-subset cases also stop. Catalog-last failure injection
  left all four projections at A while the catalog remained at B, retained a matching marker, and
  recovered to exact A. All nine actual classifier-output families and valid transport families
  pass the revised validator.

  Three material gaps remain:

  **F1a — zero-add is semantic, not byte-exact.** `validate_action_stage` compares the parsed
  catalog semantically but checks exact baseline bytes only for the four projections. In an
  isolated exact-SHA project, the stage used the identical catalog object serialized with different
  valid JSON bytes and left every projection unchanged. Real schema and generator checks passed;
  a reject-only preview with an empty approval set was accepted, and apply returned
  `applied_exact`, zero applied IDs, while rewriting only `data/communities.json`.

  ```text
  BUILD_ACCEPTED=True
  REAL_STAGE_SCHEMA_CURRENCY=PASS
  APPROVED/APPLIED_IDS=[]
  OUTCOME=applied_exact
  CHANGED_PATHS=[data/communities.json]
  ```

  This falsifies the RF's “exact zero-add no-op” claim and the TS AC-3/AC-4 exact
  action-to-expected-state boundary; owner action, expected state, and applied bytes diverge under
  TS Definition of Failure §7.

  **F1b — the exact ADD path cannot pass the real project preflight.** Baseline plus exactly the
  proposed synthetic row and all four generator-derived projections passes
  `validate_action_stage`. The real `validate_staged_project` then rejects the stage because a new
  localized row increases the fixed reviewed locale-key counts. Updating other top-level review
  binding data cannot fit the current action-stage rule, which requires the stage object to equal
  baseline plus only the proposed row. The green exact-add unit test replaces real preflight with
  `lambda _stage: ["synthetic"]`, so it does not establish RF E3/E4's real-schema claim.

  ```text
  ACTION_STAGE_BINDING=PASS
  REAL_PREFLIGHT=REJECT
  VALIDATE_SCHEMA_ERRORS=3
  ERROR_FAMILY=fixed reviewed locale-key counts changed by the new row
  ```

  This makes the isolated add boundary unusable with the real schema required by TS AC-4.

  **F2 — transport attempt/reason closure is incomplete.** Failed transport validation checks a
  reason/status shape and an attempts range, but not the producer's retry semantics. It accepts
  `max_retries_exceeded` at attempt 1, `url_error:*` at attempt 1, `error:*` at attempt 2, and
  `http_429` at attempts 1 or 3. The preserved producer emits terminal URL/general errors only at
  attempt 3, emits `max_retries_exceeded` only at attempt 3 after 429 retries, and never emits
  `http_429`. Each impossible tuple passed a complete unresolved preview with no downstream facts.
  Exact actual classifier families, non-429 HTTP failure, terminal retry failures, and verified
  success all passed, so this finding is limited to the remaining impossible producer tuples.
- **Match:** ❌ — original F1/F2 examples close, but F1a/F1b still fail AC-3/AC-4 and F2 still
  fails AC-2's “unexpected tuples are unresolved” requirement.

### V2: `scripts/validate_links.py`

- **RF claim:** Adds only the immutable fetch seam while preserving the six classifier authority
  bodies and predecessor behavior.
- **Actual:** Independent AST source-span comparison at base
  `be830d3766ca4de12ff18198a680253ed133894f` and implementation
  `20c19505d5e156c3f0fe563877a03f387322aca2` is exact for
  `TelegramPreviewParser`, `parse_member_count`, `handle_from_url`, `observed_preview_type`,
  `result`, and `classify_response`. Direct predecessor link/command matrices pass retry,
  identity-decoy/conflict, summary/update/archive, and command behavior. F2 is in the new consumer,
  not a classifier regression.
- **Match:** ✅

### V3: six runtime command copies

| Pair | Bytes each | SHA-256 | Actual |
|---|---:|---|---|
| `kz-add` | 5,331 | `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414` | Byte-identical, standalone intake/approval/apply contract, root-neutral paths. Its failure rules prohibit the F1a/F1b behavior. |
| `kz-stats` | 3,761 | `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe` | Byte-identical complete owner-triage command; repair/archive authority preserved. |
| `kz-release` | 3,532 | `2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc` | Byte-identical complete local-release command; exact pre-tag/pre-push owner stop preserved. |

- **Match:** ✅ for inventory, parity, completeness, path neutrality, and authority boundaries.

### V4: `scripts/sync_kz_commands.py`, `scripts/test_kz_intake.py`, and `scripts/test_kz_commands.py`

- **RF claim:** Enforce exact command inventory/parity and every revised intake authority branch.
- **Actual:** Command inventory, metadata, standalone markers, path-neutrality checks, drift/missing/
  extra/thin detection, and Claude-to-Codex sync all pass. All 42 tests pass. Coverage is
  insufficient for the three findings:
  1. the zero-add test uses byte-identical baseline catalog bytes and does not vary harmless JSON
     serialization;
  2. the exact-add test supplies a synthetic preflight callback instead of the real schema/
     generator preflight;
  3. the impossible-tuple test checks reason/status/fact mismatches but not reason-attempt tuples
     forbidden by `fetch_preview_with_retry`.
- **Match:** ⚠️ partial — the suite is green but does not establish the full RF claim.

### V5: `AGENTS.md`

- **RF claim:** Registers all three project commands and distinguishes availability from execution.
- **Actual:** Exact inventory, execution boundaries, and the availability-versus-live-execution
  warning are present. The file remains 8,768 bytes /
  `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612`.
- **Match:** ✅

### V6: all eleven RF-created evidence paths

| Path / group | Actual |
|---|---|
| `calibration-observations.json` | 17,093 bytes / `507938e38a5b655a9373d46bd41edb37be9f0cbd9508522878a504e0ba84c061`; eight disclosed observations and their source ledger all pass the current validator without a network rerun. |
| Four `production-hashes-*.json` checkpoints | All resolve and match independent Git-blob and working-tree hashes for the five controlled paths. |
| `site-metadata-summary.json` | 11,097 bytes / `bbf30af0cdf5fbc26d547a80e97d9199035841e47b370cd2b0dc238a527f0552`; independently regenerated byte-for-byte. |
| `claude-runtime-smoke.jsonl` | 13,602 bytes / `55871364d401e6afd55138b0f015dbdd7cca47100d8c4700c0fae64d58ee8f89`; complete accepted behavior records and excluded harness deviations. It proves project-setting use plus behavior/static path/hash binding, not an absolute loaded-path echo. |
| `codex-runtime-smoke.md` | 4,896 bytes / `9e67f40e970c098a602e5d44318f9eac1048946d88be23850d46142cbb8e85bc`; complete fresh non-forked report with explicit absolute loaded paths/hashes and unchanged controlled state. |
| `partition-audit.json` | 1,780 bytes / `6febc8793a7b763d5212cfaff4e96d7c12b9f9525427fb88e0ffdb65c3c2fbff`; authorized sealed reproduction passes in V8. |
| `jekyll-build-revision.txt` | Complete digest-pinned exact-SHA build record; independently reproduced offline in V9. |
| `EV__phase-a__intake_engine.md` | E1–E8 use valid statuses and all artifacts exist, but E2/E3/E4 overstate producer closure, real-schema exact-add behavior, and exact zero-add no-op. E8 therefore overstates aggregate acceptance. |

- **Match:** ⚠️ partial — artifacts and bindings exist, but the EV's all-verified conclusion does
  not survive F1a/F1b/F2.

### V7: exact scope and commit binding

- **RF claim:** Exactly 12 implementation paths, 8 new/4 modified, and 2,230 insertion-plus-
  deletion lines; only intake code/tests changed after command smokes.
- **Actual:** The explicit 12-path implementation allowlist at base
  `be830d3766ca4de12ff18198a680253ed133894f` reproduces 8 new, 4 modified, and exactly 2,230
  changed lines. Diffing accepted smoke SHA `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a` to revised
  implementation changes only `scripts/kz_intake.py` and `scripts/test_kz_intake.py`. RF base
  `2864b216e1f0c85a6d6f11cf7762f60a4d2d8249` adds only evidence/traces after implementation.
- **Match:** ✅

### V8: authorized sealed partition audit

- **RF claim:** The public receipt binds exact source snapshots and full partition, proves 29
  occurrences / 28 cases / one overlap / eight calibration / 20 holdout, assigns the eight lowest
  content-derived scores to calibration, and exactly matches the disclosed calibration projection.
- **Actual:** Read-only aggregate reproduction under the explicit post-freeze Reviewer authority
  established:
  - exact source bindings: 13,648 bytes /
    `ffeb4b3903ae4a4eda2ee2676f31887552cc6b510ecedd65f8830e86fbef6ebb` and 169 bytes /
    `1fdc1286cb8c5ba1f04507c163a60b6b5171bc3c53123af1debb753b1d29a162`;
  - exact full-manifest SHA-256
    `5b9fb0dd028ac19d02b2c413bca45e8fa3e0e05e8de9b20087bfa883fe2cb732`;
  - every occurrence key, case key, and split score reproduces from the declared domain-separated
    content formulas; required keys and scores are unique;
  - exact aggregate `29/28/1/8/20`, exact eight-lowest calibration allocation, and exact disclosed
    calibration case/occurrence equality;
  - public commitment, disclosed input, and sealed metadata bindings hold;
  - public receipt semantics and SHA-256
    `6febc8793a7b763d5212cfaff4e96d7c12b9f9525427fb88e0ffdb65c3c2fbff` reproduce;
  - a scoped strong-token scan across all 12 implementation paths and Phase A evidence found zero
    non-calibration disclosures.

  No holdout identity, URL, raw text, case key, score, or path was copied, listed, retained in a
  repository artifact, sent to the Executor, or used to change rules.
- **Match:** ✅ — D5 remains closed.

### V9: exact-SHA official-image build and controlled production hashes

- **RF claim:** Revised implementation SHA builds with the recorded digest-pinned official image,
  and production bytes remain unchanged.
- **Actual:** A fresh Git archive of `20c19505d5e156c3f0fe563877a03f387322aca2` built with the
  already-local official image at digest
  `sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041`, source read-only,
  isolated writable output, and container network disabled. Build and metadata validation exited
  0; the retained summary was byte-identical and all four built output hashes matched the log.
  Temporary output was automatically removed. Git blobs at base, smoke, revised implementation,
  RF base, and the current working tree are identical for all five controlled production paths.
- **Match:** ✅ — D6 remains closed; no pull, deployment, production write, release, tag, push, or
  external mutation occurred.

## Commands Executed

| # | Command / audit | Result |
|---|-----------------|--------|
| 1 | `python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands -v` | PASS — 42 tests. |
| 2 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, 0 errors. |
| 3 | `python scripts/generate_readme.py --check` | PASS — all four projections current. |
| 4 | `python scripts/sync_kz_commands.py --check` | PASS — exact three-command inventory/parity. |
| 5 | `python docs/scripts/gen_index.py --validate` | PASS — four tasks validate. |
| 6 | `python -m py_compile` for five changed/new modules | PASS. |
| 7 | Direct Phase C `run_link_matrix` and `run_command_matrix` | PASS — retry, identity, summary/update/archive, stats/release behavior. |
| 8 | Six classifier authority-body source hashes | PASS — exact to approved base. |
| 9 | 12-path/8-new/4-modified/2,230-line allowlist audit | PASS. |
| 10 | Command pair bytes/hashes and standalone-body inspection | PASS. |
| 11 | Five controlled Git-blob hashes at four revisions plus working tree | PASS — byte-identical. |
| 12 | Current-validator audit of retained calibration source/observations | PASS — 8/8 accepted, no network rerun. |
| 13 | Authorized sealed partition recomputation and scoped leakage scan | PASS — exact bindings/allocation/receipt, zero leakage paths. |
| 14 | Digest-pinned official-image build from exact revised Git archive with network disabled | PASS — build 0, validation 0, output/summary bindings exact. |
| 15 | Original reject-only unrelated valid stage exploit | PASS closure — rejected before preview. |
| 16 | Extra/edit/delete/reorder/wrong-type/changed-proposal/stale-projection matrix | PASS closure — all rejected. |
| 17 | Catalog-last failure injection and marked recovery | PASS — catalog retained at B until final write; exact recovery. |
| 18 | Re-formatted semantic zero-add stage with real preflight | FAIL contract — accepted and rewrote catalog bytes with zero applied IDs (F1a). |
| 19 | One exact ADD stage with real preflight | FAIL contract — action-stage derivation passes, real schema rejects (F1b). |
| 20 | Impossible failure reason/attempt transport tuples | FAIL contract — all tested impossible tuples accepted (F2). |
| 21 | Exact actual classifier-output and valid transport families | PASS — every real family accepted. |
| 22 | `git diff --check`, status, and staged-state audit | PASS before reviewer trace writes. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “only exact producer-possible transport/body/identity/type/result tuples” | RF §3 / E2 | `validate_observation`, preserved retry producer, direct tuple matrix | ❌ — impossible reason/attempt tuples pass (F2). |
| C2 | zero-add exact no-op and exact ADD with real schema/generator | RF §§2–4 / E3/E4 | `validate_action_stage`, `validate_staged_project`, isolated real project probes | ❌ — F1a rewrites zero-add catalog bytes; F1b cannot pass real schema. |
| C3 | exact calibration/full-partition allocation | RF §4 / E6 | authorized sealed primary inputs, public commitment/input/receipt | ✅ — formulas, hashes, counts, allocation, and disclosed equality reproduce without disclosure. |
| C4 | fresh runtime behavior and local binding | RF §4 / E7 | complete Claude/Codex artifacts plus static Git bytes | ✅ with stated limit — Claude has behavior/static binding but no loaded-path echo; Codex explicitly reports loaded paths/hashes. |
| C5 | exact scope, build, and production immutability | RF §4 / E8 | Git objects/diffs, exact-SHA offline official-image build, current hashes | ✅ — 12 paths/2,230 lines, build outputs, and controlled hashes reproduce. |

All RF/EV, master-HL §7.2, and ONB §7 references resolve. Data and build claims were checked
against primary sealed inputs, Git objects, or independently generated outputs rather than copied
from the RF summary.

## Discrepancies Found

1. **F1a — zero-add bytes are not an exact no-op.** A semantically identical reserialization of
   the catalog is accepted and applied with zero approved/applied IDs.
2. **F1b — exact ADD is incompatible with real schema preflight.** Baseline plus exactly one
   localized row passes action-stage derivation but fails the fixed locale-review key contract; the
   green test replaces real preflight.
3. **F2 — failed transport tuples are not producer-closed.** Retry-terminal reasons at early
   attempts and `http_429` are accepted even though the preserved producer cannot emit them.

Previous formal D1–D6 closures remain independently established. The original F1 unrelated-delta
and F2 target-bound/facts counterexamples also close; the findings above are uncovered branches of
the same authority requirements, not regressions in those exact closure tests.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|-----------------|----------------|
| E1 | AC-1 grammar evidence | ✅ | ✅ — focused/full tests and direct source validation reproduce. |
| E2 | AC-2 classifier/calibration evidence | ✅ | ❌ — classifier preservation/calibration hold, but F2 admits impossible transport tuples. |
| E3 | AC-3 preview/authority evidence | ✅ | ❌ — F1a violates exact zero-add action/state binding; F2 leaves a significant tuple family open. |
| E4 | AC-4 apply/hash evidence | ✅ | ❌ — safe replacement order holds, but F1a is not a no-op and F1b cannot pass real preflight. |
| E5 | AC-5 command parity evidence | ✅ | ✅ — exact inventory, completeness, parity, neutrality, and authority stops reproduce. |
| E6 | AC-6 partition/calibration evidence | ✅ | ✅ — authorized primary audit fully reproduces the non-revealing receipt. |
| E7 | AC-7 Claude/Codex smoke evidence | ✅ | ✅ with recorded limitation — complete behavior/static Claude binding and explicit Codex loaded paths. |
| E8 | AC-8 regression/build/scope evidence | ✅ | ❌ overall — 42 tests/build/scope/hashes pass, but the suite does not establish AC-2/3/4 due F1a/F1b/F2. |

Evidence totals: 8 items, 8 exist, 4 fully match, 4 are insufficient or overclaimed.

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 / ONB §7 | PV0-1 — `README.md` § Purpose | ✅ | ✅ | ✅ — accuracy, inclusion gates, and non-goals | ✅ — strict candidate admission |
| 2 | HL §7.2 / ONB §7 | PV1-1 — `.tfw/README.md` NS2 | ✅ | ✅ | ✅ — purpose, human authority, proportional assurance | ✅ — owner/evidence gates |
| 3 | HL §7.2 / ONB §7 | PV1-2 — `.tfw/README.md` Methodology values | ✅ | ✅ | ✅ — Structural Enforcement and Portability | ✅ — closed/parity gates |
| 4 | HL §7.2 / ONB §7 | PV2-1 — `knowledge/philosophy.md` absent | N/A as cited | ✅ absent | ✅ — citation explicitly records absence | ✅ — correctly N/A |
| 5 | HL §7.2 / ONB §7 | PV3-1 — `KNOWLEDGE.md` D1 | ✅ | ✅ | ✅ — JSON source, generated projections | ✅ |
| 6 | HL §7.2 / ONB §7 | PV3-2 — `KNOWLEDGE.md` D2 | ✅ | ✅ | ✅ — offline/live separation | ✅ |
| 7 | HL §7.2 / ONB §7 | PV3-3 — `KNOWLEDGE.md` D4 | ✅ | ✅ | ✅ — categories live in data | ✅ |
| 8 | HL §7.2 / ONB §7 | PV3-4 — `KNOWLEDGE.md` D14 | ✅ | ✅ | ✅ — `kz-*` versus `tfw-*` namespaces | ✅ |
| 9 | HL §7.2 / ONB §7 | PV3-5 — `KNOWLEDGE.md` D18 | ✅ | ✅ | ✅ — target-bound exact-universe evidence | ✅ — F2 is an implementation violation, not a bad citation |
| 10 | HL §7.2 / ONB §7 | PV3-6 — `KNOWLEDGE.md` D19 | ✅ | ✅ | ✅ — explicit EN/RU/KK, no fallback | ✅ — F1b exposes an unmet integration requirement |
| 11 | HL §7.2 / ONB §7 | PV4-1 — conventions §3 Evidence | ✅ | ✅ | ✅ — evidence differs from verification | ✅ |
| 12 | HL §7.2 / ONB §7 | PV4-2 — conventions §9 | ✅ | ✅ | ✅ — normal thin-adapter rule | ✅ — approved A1 exception is explicit |
| 13 | HL §7.2 / ONB §7 | PV4-3 — conventions §11 | ✅ | ✅ | ✅ — no placeholders/manual repair | ✅ |
| 14 | HL §7.2 / ONB §7 | PV4-4 — conventions §14 | ✅ | ✅ | ✅ — no bonus scope/invented evidence | ✅ |
| 15 | HL §7.2 / ONB §7 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | ✅ | ✅ — historical dead entries remain archived | ✅ — archive collision gate |

Citation totals: 15, resolved/expected-absent 15, semantically verified 15, irrelevant 0,
hallucinated 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈23 × 0.42⌉ files and recorded findings? All 23 plus two supporting artifacts.
- [x] Ran at least 1 build/test command? Full tests and exact-SHA build both ran.
- [x] Claim & Source Checks filled with primary-source verification?
- [x] Each RF §3 acceptance check verified against actual files?
- [x] KNOWLEDGE.md checked — contradictions documented in Judge?
- [x] All HL §7.2 and ONB §7 citations verified?
  - Total: 15, resolved/expected-absent: 15, semantically verified: 15, irrelevant: 0, hallucinated: 0.
- [x] Evidence artifacts from RF §5 verified?
  - Total: 8, exist: 8, fully match: 4, insufficient/overclaimed: 4.

Stage complete: YES

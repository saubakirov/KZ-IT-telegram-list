# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 24 (13 implementation paths and 11 RF-created evidence paths)
> Files to verify: ⌈24 × 0.42⌉ = 11; all 24 claimed paths and the two supporting public commitment/input artifacts were audited.

## Verification Log

### V1: `scripts/kz_intake.py` — direct authority and exploit audit

- **RF claim:** All prior D1–D6 and F1/F2 findings close. In particular, zero-ADD is byte-exact,
  exact 1/N ADD mechanically rebinds locale review and passes the real project preflight, and
  serialized observations accept only tuples the preserved fetch producer can emit.
- **Actual:** The action/stage findings close under direct temporary-project exploits, not merely
  the green suite:
  - semantic-only zero-ADD JSON reserialization passed the real schema/generator preflight but was
    rejected as `staged bytes are not the exact action result: data/communities.json`; all root
    controlled bytes remained unchanged and no pending marker appeared;
  - an unrelated schema/generator-valid reject-only catalog/projection edit was likewise rejected;
  - real zero ADD returned `already_applied_exact` with zero IDs and byte-identical controlled
    paths;
  - real one and two ADD stages equalled baseline plus exactly the proposed row(s) and the two
    mechanical `localization_review` bindings, used exact UTF-8 `indent=2` JSON with one LF and no
    CR, matched independently recomputed payload digests/key counts, passed the real
    `validate_schema.validate_data` and schema/generator preflight, and applied exactly the approved
    IDs;
  - the one-ADD counts were `en:140,ru:132,kk:132` with `changed_key_count=404`; the two-ADD counts
    were `en:141,ru:133,kk:133` with `changed_key_count=407`;
  - injected two-ADD failure before the catalog replacement left the catalog at B and exact
    projections/marker recoverable; retry returned `recovered_exact` with both IDs;
  - an isolated neutral-path state harness reproduced first apply `[B,N,B,B,B] -> applied_exact`
    and exact rerun `[A,N,A,A,A] -> already_applied_exact`.

  Recursive schema checks reject Boolean integers, blank evidence, verified rows over failed
  transport, target-unbound or arbitrary-reason verified classifier tuples, and success records
  missing status/body. Exact fetched 2xx attempts 1–3, non-429 HTTP terminal attempt 1,
  URL/general terminal attempt 3, and `max_retries_exceeded` attempt 3 pass. Non-429 HTTP attempts
  2/3, retry-terminal attempts 1/2, and every `http_429` result fail.

  One material producer-closure gap remains:

  **F2a — failed HTTP records still accept 2xx statuses.** The failed-status branch requires only
  `attempts == 1`, `status != 429`, and `reason == "http_<status>"`; it does not exclude 200–299.
  Direct observations created from failed fetch results at status 200, 204, and 299 were all
  accepted:

  ```text
  200 ACCEPTED
  204 ACCEPTED
  299 ACCEPTED
  ```

  The preserved producer returns its normal response path as `ok=True, reason="fetched"`; its
  `HTTPError` branch is the failed HTTP family. Therefore failed `http_2xx` records are not
  producer-possible and contradict TS AC-2 and RF/EV E2's exact tuple claim. Outside-2xx terminal
  HTTP records at attempt 1 continue to validate, so this finding is bounded to the missing 2xx
  exclusion.
- **Match:** ❌ — D1–D6 and the previous F1/F2 examples close, but F2a leaves AC-2's exact
  producer-tuple boundary open.

### V2: `scripts/validate_schema.py`

- **RF claim:** Locale-cardinality validation is independently data-derived, remains bound to the
  canonical review digest, and reports the truthful current baseline.
- **Actual:** `expected_locale_payload_counts` derives cardinalities from the three common fields,
  current categories, current live entries, twice the current archive size, the registered UI
  keys, locale-specific non-goal lengths, and EN-only README UI keys. It does not contain the old
  `139/131/131` acceptance constant. Direct 0/1/2-row projections increase the expected counts by
  exactly 0/1/2 per locale; canonical digest and changed-key checks remain independently computed
  from the payload. The real baseline reports
  `keys=en:139,ru:131,kk:131; sha256=51db402d…` and zero errors.
- **Match:** ✅ — genuine structural invariant, truthful output, and unchanged digest binding.

### V3: `scripts/validate_links.py`

- **RF claim:** Adds only the immutable fetch/retry seam while preserving the classifier authority
  bodies and predecessor behavior.
- **Actual:** Direct source-segment comparison between approved base
  `be830d3766ca4de12ff18198a680253ed133894f` and final implementation
  `731b3d6a3350bb3fe41115a4ae9213aaa86bbc6f` is exact for `TelegramPreviewParser`,
  `parse_member_count`, `handle_from_url`, `observed_preview_type`, `result`, and
  `classify_response`. The predecessor link matrix passes retry, identity decoy/conflict,
  summary/update/archive, type mismatch, and failure behavior. F2a is in the new serialized-record
  consumer, not a classifier regression.
- **Match:** ✅

### V4: command inventory and runtime records

| Pair / file | Bytes | SHA-256 / result |
|---|---:|---|
| `kz-add` pair | 5,331 each | `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414`; byte-identical and complete. |
| `kz-stats` pair | 3,761 each | `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe`; byte-identical, triage authority preserved. |
| `kz-release` pair | 3,532 each | `2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc`; byte-identical, pre-tag/pre-push stop preserved. |
| `AGENTS.md` | 8,768 | `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612`; exact three-command inventory and execution warning. |
| Claude smoke | 13,602 | `55871364d401e6afd55138b0f015dbdd7cca47100d8c4700c0fae64d58ee8f89`; three accepted, exit 0, no tools/network/writes/mutation. |
| Codex smoke | 4,896 | `9e67f40e970c098a602e5d44318f9eac1048946d88be23850d46142cbb8e85bc`; complete report with explicit loaded paths/hashes. |

All seven routing/runtime bytes match smoke SHA `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`, final
implementation, integrated RF base, and the current tree. Static parity, standalone completeness,
path neutrality, sync direction, and the predecessor command matrix pass. Claude's recorded limit
(behavior plus static local binding, no echoed absolute loaded path) remains stated accurately.

- **Match:** ✅

### V5: tests and enforcement coverage

- **RF claim:** Forty-four tests include all formal-review exploits and exact producer tuple
  families.
- **Actual:** All 44 tests pass, including semantic zero-ADD rejection, real 0/1/N preflight,
  mechanical locale rebinding, recovery, previous impossible retry tuples, exact classifier
  families, command parity, and generation/schema regressions. The suite does not include failed
  `http_2xx` tuples, so its green result does not establish the complete producer-possible claim.
- **Match:** ⚠️ partial — regression coverage is substantial, but F2a is an uncovered mandatory
  rejection family.

### V6: all eleven RF-created evidence paths

| Path / group | Actual |
|---|---|
| `calibration-observations.json` | 17,093 bytes / `507938e38a5b655a9373d46bd41edb37be9f0cbd9508522878a504e0ba84c061`; all eight disclosed observations pass the current validator without network rerun. |
| Four `production-hashes-*.json` files | All resolve and match Git blobs/current bytes for the five controlled production paths. |
| `site-metadata-summary.json` | 11,097 bytes / `bbf30af0cdf5fbc26d547a80e97d9199035841e47b370cd2b0dc238a527f0552`; independently regenerated byte-for-byte. |
| `claude-runtime-smoke.jsonl` / `codex-runtime-smoke.md` | Complete accepted records with the exact limitations and path/hash bindings summarized in V4. |
| `partition-audit.json` | 1,780 bytes / `6febc8793a7b763d5212cfaff4e96d7c12b9f9525427fb88e0ffdb65c3c2fbff`; public allocation receipt remains bound. |
| `jekyll-build-revision.txt` | Complete digest-pinned final-implementation build record; independently reproduced in V9. |
| `EV__phase-a__intake_engine.md` | All rows and references exist, but E2 and aggregate E8 overstate transport producer closure because F2a survives. |

- **Match:** ⚠️ partial — artifacts and bindings exist; the all-verified conclusion does not
  survive F2a.

### V7: exact scope and commit binding

- **RF claim:** Exactly 13 implementation paths, 8 new/5 modified, 2,369 insertion-plus-deletion
  lines; only three approved implementation files changed after Coordinator base `067528d…`.
- **Actual:** The explicit implementation allowlist from
  `be830d3766ca4de12ff18198a680253ed133894f` to
  `731b3d6a3350bb3fe41115a4ae9213aaa86bbc6f` reproduces exactly 13 paths, 8 new, 5 modified, and
  2,369 changed lines. Relative to
  `067528dba201e93d3a8d4efcb525d9bdfcb753d0`, the only implementation paths changed are
  `scripts/kz_intake.py`, `scripts/test_kz_intake.py`, and `scripts/validate_schema.py`; the other
  differences are the expected task handoff/lifecycle traces. Integrated RF base is exactly
  `45878d9459e263ed7821dcc84bc400ed0603fb3c` before Reviewer writes.
- **Match:** ✅

### V8: public sealed-boundary audit

- **RF claim:** Public artifacts bind 29 occurrences / 28 cases / one overlap / eight calibration /
  20 holdout without disclosing the sealed holdout.
- **Actual:** Public hashes remain exact: input commitment `f7d4530d…`, calibration input
  `cbdf4f48…`, calibration observations `507938e3…`, and partition receipt `6febc879…`.
  The public receipt records the exact `29/28/1/8/20` totals and the eight disclosed observations
  validate. Per the explicit review boundary, no sealed holdout identity, URL, case key, score,
  raw text, or path was opened or inspected.
- **Match:** ✅ within the permitted non-revealing public evidence boundary; the seal is preserved.

### V9: exact-SHA site build and controlled production hashes

- **RF claim:** Final implementation SHA builds in the digest-pinned official image and controlled
  production bytes remain unchanged.
- **Actual:** A fresh Git archive of `731b3d6a3350bb3fe41115a4ae9213aaa86bbc6f` built with the
  already-local image digest
  `sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041`, read-only source,
  isolated writable output, and container network disabled. Build and site-metadata validation
  exited 0. Built hashes reproduced exactly: EN `64597def…`, RU `fef3499e…`, KK `2d4465e7…`,
  sitemap `79dcb9bb…`; summary `bbf30af0…` was byte-identical. Git blobs at base, smoke, final
  implementation, integrated RF base, and current tree are identical for the five controlled
  production paths (`data/communities.json`, EN/RU/KK projections, `README.md`). Temporary build
  output was removed automatically.
- **Match:** ✅ — D6 remains closed; no pull, deploy, production write, release, tag, push, or
  external mutation occurred.

## Commands Executed

| # | Command / audit | Result |
|---|-----------------|--------|
| 1 | `python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands -v` | PASS — 44 tests. |
| 2 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, locale counts `139/131/131`, 0 errors. |
| 3 | `python scripts/generate_readme.py --check` | PASS — all four projections current. |
| 4 | `python scripts/sync_kz_commands.py --check` | PASS — exact three-command inventory/parity. |
| 5 | `python docs/scripts/gen_index.py --validate` | PASS — four tasks validate. |
| 6 | `python -m py_compile` for all six changed/new Python runtime/test/schema modules | PASS. |
| 7 | Direct Phase C `run_link_matrix` and `run_command_matrix` | PASS — retry, identity, summary/update/archive, stats/release behavior. |
| 8 | Literal trailing-dot, recursive schema, classifier-family, and transport-family probes | PASS closures for D1/D2 and prior F2 tuples. |
| 9 | Real semantic zero-ADD and unrelated-valid-delta exploits | PASS closure — both rejected before marker/write, root bytes unchanged. |
| 10 | Real 0/1/2 ADD preflight, byte/digest/count checks, failure injection, and recovery | PASS closure — exact stage and outcomes. |
| 11 | Neutral-path first-apply/rerun state harness | PASS closure — equal path stays neutral. |
| 12 | Failed `http_200`, `http_204`, and `http_299` observations | **FAIL contract (F2a)** — all accepted. |
| 13 | Classifier source equality, command/runtime hashes, controlled production hashes | PASS — exact at all required revisions/current tree. |
| 14 | 13-path/8-new/5-modified/2,369-line allowlist audit and three-file revision audit | PASS. |
| 15 | Public seal/hash/count audit without opening holdout identities | PASS — bindings/totals preserved. |
| 16 | Digest-pinned official-image build from exact final Git archive, network disabled | PASS — build 0, metadata 0, retained output/summary hashes exact. |
| 17 | `git diff --check` and initial worktree/staging audit | PASS before Reviewer trace writes. |

## Claim & Source Checks

| # | Claim / citation checked | Traces to | Holds? |
|---|--------------------------|-----------|--------|
| C1 | only producer-possible transport tuples | `fetch_preview_with_retry`, `validate_observation`, direct tuple matrix | ❌ — failed `http_2xx` attempt-1 tuples validate (F2a). |
| C2 | exact zero/one/many action-to-stage/apply behavior | stage builder, real schema/generator, temporary-project byte/digest/state probes | ✅ — prior F1/F1a/F1b closures reproduce. |
| C3 | data-derived locale invariant and digest binding | `expected_locale_payload_counts`, canonical payload functions, baseline/1/2-row probes | ✅. |
| C4 | preserved classifier and command/runtime behavior | source spans, hashes, parity tests, predecessor matrices, smoke artifacts | ✅ with the RF-stated Claude path-echo limitation. |
| C5 | scope, build, and controlled immutability | Git objects/diffs, exact-SHA offline build, current hashes | ✅ — exact 13 paths/2,369 lines and unchanged production bytes. |
| C6 | public sealed allocation boundary | commitment/input/observation/receipt artifacts only | ✅ within authority; holdout identities were not inspected. |

All RF/EV, master-HL §7.2, and ONB §7 references resolve. Claims were checked against code,
Git objects, independently derived temporary states, or independently generated outputs rather
than accepted from the RF summary.

## Discrepancies Found

1. **F2a — failed HTTP 2xx tuples are accepted.** The consumer admits
   `ok=false, reason=http_<2xx>, status_code=<2xx>, attempts=1`, although the producer's 2xx family
   is `ok=true, reason=fetched`. Add the missing outside-2xx condition and direct rejection tests
   while retaining every valid producer tuple test.

All prior D1–D6 closures, the original F1 unrelated-stage exploit, the prior F2 classifier/facts
exploits, and the three last REVISE exploits otherwise reproduce as closed. No other material or
non-blocking finding was found.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|-----------------|----------------|
| E1 | AC-1 grammar evidence | ✅ | ✅ — D1 and source/accounting tests reproduce. |
| E2 | AC-2 producer/classifier/calibration evidence | ✅ | ❌ — F2a admits failed 2xx tuples the producer cannot emit. |
| E3 | AC-3 preview/authority evidence | ✅ | ✅ — recursive closure and exact zero/one/many stages reproduce. |
| E4 | AC-4 apply/hash evidence | ✅ | ✅ — real preflight, neutral paths, catalog-last recovery, and exact reruns reproduce. |
| E5 | AC-5 command parity evidence | ✅ | ✅ — exact inventory, completeness, parity, neutrality, and authority stops reproduce. |
| E6 | AC-6 partition/calibration evidence | ✅ | ✅ — public bindings and totals hold without holdout inspection. |
| E7 | AC-7 Claude/Codex smoke evidence | ✅ | ✅ with recorded limit — complete Claude behavior/static binding and explicit Codex paths. |
| E8 | AC-8 aggregate evidence | ✅ | ❌ overall — tests/build/scope/hashes pass, but the suite misses F2a and cannot establish full acceptance. |

Evidence totals: 8 items, 8 exist, 6 fully match, 2 are insufficient or overclaimed.

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
| 9 | HL §7.2 / ONB §7 | PV3-5 — `KNOWLEDGE.md` D18 | ✅ | ✅ | ✅ — target-bound exact-universe evidence | ✅ — F2a violates the application, not the citation. |
| 10 | HL §7.2 / ONB §7 | PV3-6 — `KNOWLEDGE.md` D19 | ✅ | ✅ | ✅ — explicit EN/RU/KK, no fallback | ✅ |
| 11 | HL §7.2 / ONB §7 | PV4-1 — conventions §3 Evidence | ✅ | ✅ | ✅ — evidence differs from verification | ✅ |
| 12 | HL §7.2 / ONB §7 | PV4-2 — conventions §9 | ✅ | ✅ | ✅ — normal thin-adapter rule | ✅ |
| 13 | HL §7.2 / ONB §7 | PV4-3 — conventions §11 | ✅ | ✅ | ✅ — no placeholders/manual repair | ✅ |
| 14 | HL §7.2 / ONB §7 | PV4-4 — conventions §14 | ✅ | ✅ | ✅ — no bonus scope/invented evidence | ✅ |
| 15 | HL §7.2 / ONB §7 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | ✅ | ✅ — historical dead entries remain archived | ✅ |

Citation totals: 15, resolved/expected-absent 15, semantically verified 15, irrelevant 0,
hallucinated 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈24 × 0.42⌉ files and recorded findings? All 24 plus two supporting public artifacts.
- [x] Ran at least 1 build/test command? Full tests and exact-SHA build both ran.
- [x] Claim & Source Checks filled with primary-source verification?
- [x] Each RF §3 acceptance check verified against actual files?
- [x] KNOWLEDGE.md checked — contradictions documented in Judge?
- [x] All HL §7.2 and ONB §7 citations verified?
  - Total: 15, resolved/expected-absent: 15, semantically verified: 15, irrelevant: 0, hallucinated: 0.
- [x] Evidence artifacts from RF §5 verified?
  - Total: 8, exist: 8, fully match: 6, insufficient/overclaimed: 2.

Stage complete: YES

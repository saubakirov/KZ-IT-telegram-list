# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 23 (12 implementation paths and 11 RF-created evidence paths)
> Files to verify: ⌈23 × 0.42⌉ = 10; discrepancies were found, so all 23 claimed paths and two supporting public seal artifacts were audited.

## Verification Log

### V1: `scripts/kz_intake.py`
- **RF claim:** Implements the literal source grammar, exact observation tuple, recursively closed
  preview/authority schemas, and neutral-aware exact-state apply.
- **Actual:** The three code defects from the first review are closed:
  1. `https://t.me./valid_name` is now `spoofed_authority`, not a candidate.
  2. Exact integer schemas reject Python/JSON booleans, blank/whitespace editorial references are
     rejected, and `status: verified` rejects `transport.ok: false`.
  3. Equal before/after paths are neutral; partial-neutral and wholly unchanged first apply/rerun,
     marked recovery, and unknown-state cases behave as claimed.

  Two other contract failures remain:

  **F1 — staged bytes are not derived from the approved action set.** Lines 643–667 bind staged
  bytes only to preview after-hashes, recheck add rows against the current catalog, and run schema/
  generator preflight. They never prove that the staged catalog delta consists exactly of the
  preview's proposed `add` rows or that reject/duplicate/unresolved rows cause no catalog delta.
  An isolated exact-SHA project probe changed an unrelated existing description in the stage,
  regenerated valid projections, and built a preview containing one `reject` action and zero
  approved add IDs. Real schema and generator preflight passed; `apply_preview` returned
  `applied_exact`, changed three controlled paths including `data/communities.json`, and made the
  final controlled hashes equal the unrelated stage. The receipt still reported zero applied IDs.
  This violates TS AC-3/AC-4, master-HL Definition of Finished item 6, and TS Definition of Failure
  (owner action, expected post-state, and applied bytes can diverge).

  ```text
  PREFLIGHT_VALIDATIONS=['scripts/validate_schema.py', 'scripts/generate_readme.py --check']
  APPROVED_ADD_COUNT=0
  RECEIPT_APPLIED_COUNT=0
  OUTCOME=applied_exact
  CONTROLLED_PATHS_CHANGED=3
  CATALOG_UNRELATED_CHANGE_APPLIED=True
  FINAL_EQUALS_STAGE=True
  ```

  **F2 — serialized classifier tuples are not validated against classifier semantics.** Lines
  439–447 count any row whose `classification` equals `verified`; they do not require the verified
  row's `target_bound: true` or exact verified reason. A preview whose verified typed result was
  changed to `target_bound: false` and an arbitrary non-classifier reason passed
  `validate_preview`; after recomputing its synthetic approval, add apply returned
  `applied_exact` with one applied ID. A transport marked `ok: true` with no status/body binding is
  also accepted. `classify_response` itself can emit `verified` only with reason
  `target_preview_verified` and `target_bound: true`, so these are impossible producer tuples that
  AC-2 says must remain unresolved, not approved downstream facts.

  ```text
  VERIFIED_RESULT_TARGET_BOUND_FALSE=ACCEPTED
  VERIFIED_RESULT_REASON_ARBITRARY=ACCEPTED
  TRANSPORT_OK_WITHOUT_STATUS_OR_BODY=ACCEPTED
  TAMPERED_PREVIEW=ACCEPTED
  TAMPERED_APPLY_OUTCOME=applied_exact
  TAMPERED_APPLIED_COUNT=1
  ```
- **Match:** ❌ — the previous D1–D3 counterexamples close, but F1 and F2 independently falsify
  AC-2, AC-3, and AC-4.

### V2: `scripts/validate_links.py`
- **RF claim:** Adds only an immutable fetch/retry seam while preserving the six classifier
  authority bodies and predecessor behavior.
- **Actual:** Independent AST/source-span hashing at base
  `be830d3766ca4de12ff18198a680253ed133894f` and revised implementation
  `3b06f143102bb90b3bd47f994607371bb3f0df45` produced exact equality for all six bodies:

  | Body | SHA-256 |
  |---|---|
  | `TelegramPreviewParser` | `0e9ef29cc7e9baec5ad2e22dbd4891c5feb118537b123fd51984241803d9ea4b` |
  | `parse_member_count` | `061de7a95db251575c47a1814360492a29e8ff4c5d372734209a57730c310199` |
  | `handle_from_url` | `2ede21c62417f59372fcc4ad924003c218770c15639eb3d228ecbe85cb9530a4` |
  | `observed_preview_type` | `91c684c0bc1280d134023951c49bf37ac4afc1ac1e806266296964d56e1948c3` |
  | `result` | `4215525160b26b326ad4628622d80d7bc71aa6841ce9350c78c2779313a0c0a7` |
  | `classify_response` | `5950b026dc66568a9ec3f455c4113e9ec272d35b430c88ae0e58658b01f990a7` |

  Direct predecessor link matrices also passed retry, target identity/decoy/conflict, summary,
  update, and archive behavior. F2 is in the new consumer validator, not a change to classifier
  semantics.
- **Match:** ✅

### V3: six runtime command copies

| Path | Actual |
|---|---|
| `.claude/commands/kz-add.md` | Complete standalone preview/approval/apply contract; root-neutral repository paths. Its failure rules explicitly forbid divergence and unrelated staged work. |
| `.agents/skills/kz-add/SKILL.md` | Exact byte copy of Claude `kz-add`; valid skill metadata. |
| `.claude/commands/kz-stats.md` | Complete owner-triage command; repair/archive authority preserved. |
| `.agents/skills/kz-stats/SKILL.md` | Exact byte copy of Claude `kz-stats`; valid skill metadata. |
| `.claude/commands/kz-release.md` | Complete local release preparation; exact-current approval stop before tag/push preserved. |
| `.agents/skills/kz-release/SKILL.md` | Exact byte copy of Claude `kz-release`; valid skill metadata. |

Pair hashes reproduce the runtime records: `kz-add` is 5,331 bytes /
`783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414`, `kz-stats` is
3,761 bytes / `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe`, and
`kz-release` is 3,532 bytes /
`2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc`.

- **Match:** ✅ for inventory, byte parity, standalone completeness, path neutrality, and preserved
  authority stops. Runtime proof is assessed separately under V6/E7.

### V4: `scripts/sync_kz_commands.py`, `scripts/test_kz_intake.py`, and `scripts/test_kz_commands.py`
- **RF claim:** Enforce exact command inventory/parity and the full intake grammar/schema/
  authority/idempotency/recovery contract.
- **Actual:** Exact command inventory, parity, completeness markers, forbidden-reference checks,
  drift, and sync direction all pass. The focused D1–D3 tests and full 36-test suite pass. The
  intake tests do not include the F1 zero-approved-add/unrelated-stage delta or F2 impossible
  verified typed-result tuple, so the green suite does not establish every AC-2/3/4 branch.
- **Match:** ⚠️ partial

### V5: `AGENTS.md`
- **RF claim:** Registers the three project commands and distinguishes availability from execution.
- **Actual:** The exact `/kz-add`, `/kz-stats`, `/kz-release` inventory, execution boundaries, and
  availability-versus-live-execution warning are present. The file is 8,768 bytes /
  `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612` at the smoke and revised
  SHAs.
- **Match:** ✅

### V6: all eleven RF-created evidence paths

| Path | Actual |
|---|---|
| `evidence/calibration-observations.json` | Eight disclosed calibration observations and their source ledger; SHA-256 `507938e38a5b655a9373d46bd41edb37be9f0cbd9508522878a504e0ba84c061`; unchanged and accepted by the revised validator. |
| Four `evidence/production-hashes-*.json` checkpoints | All resolve and match independent Git-blob hashes for the five controlled paths. |
| `evidence/site-metadata-summary.json` | 11,097 bytes / `bbf30af0cdf5fbc26d547a80e97d9199035841e47b370cd2b0dc238a527f0552`; independently regenerated byte-for-byte. |
| `evidence/claude-runtime-smoke.jsonl` | 13,602 bytes / `55871364d401e6afd55138b0f015dbdd7cca47100d8c4700c0fae64d58ee8f89`; self-contained accepted records for all three literal invocations, complete result texts, controlled hashes, and separately excluded deviations. It proves project-setting use plus behavior matching the statically bound local body; it does not claim an absolute loaded-path echo. |
| `evidence/codex-runtime-smoke.md` | 4,896 bytes / `9e67f40e970c098a602e5d44318f9eac1048946d88be23850d46142cbb8e85bc`; complete fresh non-forked report with exact input, task identity, literal routing results, absolute loaded paths/hashes, and before/after controlled hashes. |
| `evidence/partition-audit.json` | 1,780 bytes / `6febc8793a7b763d5212cfaff4e96d7c12b9f9525427fb88e0ffdb65c3c2fbff`; reproduced under the authorized sealed audit in V8. |
| `evidence/jekyll-build-revision.txt` | Complete exact-SHA official-image command/output/validation record; independently reproduced in V9. |
| `evidence/EV__phase-a__intake_engine.md` | Contains E1–E8 with valid status vocabulary, but E2/E3/E4 overstate the untested F1/F2 branches and E8 therefore overstates aggregate acceptance. |

- **Match:** ⚠️ partial — every file and recorded hash exists; runtime, partition, build, and
  production-hash bindings hold, but the EV's all-verified conclusion does not survive F1/F2.

### V7: exact scope and commit binding
- **RF claim:** Exactly 12 implementation paths, 8 new/4 modified, 1,957 insertion-plus-deletion
  lines, and revised SHA changes only intake code/tests after runtime smoke.
- **Actual:** Parent-to-revised-implementation Git diff reproduces exactly 12 paths, 8 new/4
  modified, and 1,957 changed lines. Diffing accepted smoke SHA `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`
  to revised SHA changes only `scripts/kz_intake.py` and `scripts/test_kz_intake.py`; `AGENTS.md` and
  all six runtime copies are byte-identical. Base `4c79b16c62b7b448aef1e3cac6b0a1c0ebb2b8b9`
  adds only RF/evidence/traces after implementation `3b06f143102bb90b3bd47f994607371bb3f0df45`.
- **Match:** ✅

### V8: authorized sealed partition audit
- **RF claim:** The public receipt binds the exact full partition and proves 29 occurrences / 28
  cases / one overlap / eight calibration / 20 holdout, eight-lowest allocation, and exact
  disclosed calibration equality without disclosure.
- **Actual:** Read-only aggregate reproduction under the special Reviewer authority established:
  - the two committed source bindings are exact: 13,648 bytes /
    `ffeb4b3952bf43426b2dd86b51e8abe204734a08fab5dd1d53b2b50edd9c2a4d` and 169 bytes /
    `1fdc1286d778d9edfb81864ded71f8a1803226721ebba0cfd9c6be5dc5b35f8f`;
  - the full manifest is 38,703 bytes /
    `5b9fb0dd028ac19d02b2c413bca45e8fa3e0e05e8de9b20087bfa883fe2cb732`;
  - every occurrence key is derived from source hash/range/raw-span hash, every case key is derived
    from its sorted occurrence keys, and every split score is derived from its case key using the
    declared domain-separated formulas; all keys and scores are unique where required;
  - the exact aggregate is 29 occurrences / 28 cases / one overlap / eight calibration / 20
    holdout, and the calibration partition is exactly the eight lowest scores;
  - disclosed calibration cases and occurrences equal the manifest's calibration projection
    exactly, in order and set;
  - public commitment, calibration input, and sealed metadata bindings all hold;
  - the public receipt semantics reproduce byte-for-byte at SHA-256
    `6febc8793a7b763d5212cfaff4e96d7c12b9f9525427fb88e0ffdb65c3c2fbff`;
  - a scoped strong-token leakage scan across implementation, commands, and Phase A evidence
    found zero non-calibration disclosures.

  No holdout identity, URL, raw text, case key, score, or path was copied, listed, retained in a
  repository artifact, sent to the Executor, or used to change rules.
- **Match:** ✅ — previous D5 closed.

### V9: exact-SHA official-image build and controlled production hashes
- **RF claim:** The revised SHA builds with the recorded digest-pinned official image and all
  controlled production bytes remain unchanged.
- **Actual:** From a Git archive of exact implementation SHA
  `3b06f143102bb90b3bd47f994607371bb3f0df45`, the already-local image
  `ghcr.io/actions/jekyll-build-pages@sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041`
  ran with the source mounted read-only and an isolated writable output mount. Build exit was 0;
  metadata validation exit was 0. Independent outputs exactly match the checked-in log:

  | Output | Bytes | SHA-256 |
  |---|---:|---|
  | `index.html` | 33,669 | `64597def18f8777f92739d131649299c1639af1923f7cccde34b86d7ea61de21` |
  | `ru/index.html` | 40,530 | `fef3499ecf2d5678a52fea4d1a93d51ce5d168d883652087bb02d776c144ec0f` |
  | `kk/index.html` | 41,343 | `2d4465e7dc55856683247bf036f113380b452db1053424d82935dff81d4fba49` |
  | `sitemap.xml` | 338 | `79dcb9bbd3dda14054fe33695f89f6f62cdeea08881a427ec059d5e2d1665767` |

  The regenerated summary is byte-identical to the retained artifact. Git blobs at seal,
  implementation, smoke, revised implementation, and RF base are identical for all five
  controlled production paths:

  | Path | Bytes | SHA-256 |
  |---|---:|---|
  | `data/communities.json` | 45,260 | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` |
  | `README.md` | 16,627 | `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d` |
  | `index.md` | 16,536 | `4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3` |
  | `ru/index.md` | 22,412 | `36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97` |
  | `kk/index.md` | 23,004 | `64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7` |

- **Match:** ✅ — previous D6 closed; no deployment, pull, push, tag, release, production write, or
  external-service mutation occurred.

## Commands Executed

| # | Command / audit | Result |
|---|-----------------|--------|
| 1 | Five focused D1–D3 revision tests | PASS — trailing-dot, exact integer/evidence/transport, neutral first apply/rerun, and wholly unchanged/unknown cases. |
| 2 | `python -m unittest -v scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands` | PASS — 36 tests. |
| 3 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, 0 errors. |
| 4 | `python scripts/generate_readme.py --check` | PASS — all four projections current. |
| 5 | `python docs/scripts/gen_index.py --validate` | PASS — four tasks validate. |
| 6 | `python -m py_compile` for five changed/new Python modules | PASS. |
| 7 | `python scripts/sync_kz_commands.py --check` | PASS — exact three-command inventory and parity. |
| 8 | `git diff --check` | PASS. |
| 9 | Direct Phase C `run_link_matrix` and `run_command_matrix` | PASS — retry, decoy/conflict, summary/update/archive, stats/release. |
| 10 | Six classifier authority-body hashes | PASS — exact to `be830d3766ca4de12ff18198a680253ed133894f`. |
| 11 | 12-path/8-new/4-modified/1,957-line Git audit | PASS. |
| 12 | Five controlled Git-blob hashes at five checkpoints | PASS — byte-identical. |
| 13 | Authorized sealed content-derived partition reproduction | PASS — exact source/manifest/receipt bindings and 29/28/1/8/20 allocation. |
| 14 | Digest-pinned official-image build from exact revised Git archive | PASS — exit 0. |
| 15 | `python scripts/test_site_metadata.py` against independent build | PASS; retained summary byte-identical. |
| 16 | Reject-only preview + unrelated valid staged delta + real preflight | FAIL contract — zero approved/applied IDs, yet catalog/projections changed and outcome was `applied_exact` (F1). |
| 17 | Impossible verified typed-result tuple in preview/apply | FAIL contract — target-unbound/arbitrary-reason verified result was accepted and applied (F2). |

The full historical harness `main()` remains inapplicable because line 279 hardcodes
`oldest_live == 2026-01-30` while the current oldest live date is `2026-08-27`. Its reusable
matrices pass, and the already-open TD-19 accurately records the owning-task repair.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “fail closed on every non-exact tuple” | RF §3 / E2 | `validate_observation`, immutable classifier output semantics, adversarial preview/apply | ❌ — an impossible target-unbound/arbitrary-reason verified tuple is approved and applied (F2). |
| C2 | Preview/action/expected-after/applied bytes remain exact | RF §§2–3 / E3/E4 | `build_preview`, `validate_approval`, `apply_preview`, real-preflight temporary project | ❌ — a zero-add reject preview applies an unrelated valid staged catalog delta (F1). |
| C3 | Exact calibration/full-partition allocation | RF §4 / E6 | authorized sealed primary inputs, public commitment/input/receipt | ✅ — formulas, hashes, counts, eight-lowest split, and exact disclosed calibration equality reproduce without disclosure. |
| C4 | Fresh runtime behavior and local binding | RF §4 / E7 | complete Claude/Codex artifacts plus static Git bytes | ✅ with stated limit — Codex explicitly reports loaded absolute paths/hashes; Claude supplies complete behavior records and static path/hash binding but no absolute-path echo. |
| C5 | Production bytes and exact scope | RF §4 / E8 | Git objects/diffs at exact commits | ✅ — 12 paths, 1,957 lines, classifier bodies, and all controlled hashes reproduce. |

All RF/EV, master-HL §7.2, and ONB §7 references resolve. Data and build claims were checked
against primary sealed inputs, Git objects, or independently generated outputs rather than copied
from the RF summary.

## Discrepancies Found

1. **F1 — AC-3/AC-4 exact action-to-stage binding is absent.** A preview with no add action and an
   empty approved set can bind and apply an unrelated schema-valid catalog/projection delta. The
   after-hash binding proves byte identity only, not that those bytes implement exactly the
   approved action projection.
2. **F2 — AC-2/AC-3 observation validation accepts impossible verified classifier tuples.** The
   consumer validator does not require the verified result's target binding and exact classifier
   reason; a tampered tuple can provide approved downstream facts and pass add apply.

Previous formal findings D1–D6 were each independently reproduced against their revised closure
and are closed. F1/F2 are new branches found by full contract audit, not failures of those exact
revision tests.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | AC-1 synthetic grammar evidence | ✅ | ✅ — focused and full tests plus direct authority classification reproduce. |
| E2 | AC-2 classifier/calibration evidence | ✅ | ❌ — fetch/classifier preservation holds, but F2 admits an impossible verified tuple. |
| E3 | AC-3 canonical preview/authority evidence | ✅ | ❌ — F1 permits action/stage divergence and F2 permits a significant typed-result tamper. |
| E4 | AC-4 apply/hash evidence | ✅ | ❌ — neutral idempotency closes D3, but F1 violates exact approved-set apply. |
| E5 | AC-5 command parity evidence | ✅ | ✅ — exact inventory, completeness, parity, neutrality, and authority stops reproduce. |
| E6 | AC-6 partition/calibration evidence | ✅ | ✅ — authorized primary audit fully reproduces the non-revealing receipt. |
| E7 | AC-7 Claude/Codex smoke evidence | ✅ | ✅ with explicit limit — Claude is behavioral+static binding; Codex explicitly reports loaded paths. |
| E8 | AC-8 aggregate verification evidence | ✅ | ⚠️ partial — build, scope, regressions, hashes, and no mutation hold; aggregate acceptance does not because AC-2/3/4 fail. |

Evidence totals: 8 referenced items, 8 present, 4 fully matched, 1 partially matched, 3 mismatched.

## Knowledge Citations Verified

Each row covers both the master HL §7.2 citation and its mirrored ONB §7 application (30 artifact
applications total). The cited files are unchanged from the first formal review and were reopened
or hash/diff-confirmed in this review.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL/ONB #1 | PV0-1 — `README.md` § Purpose | ✅ | ✅ | ✅ — accuracy, live/verified IT-KZ admission, dated checks and non-goals are present. | ✅ — directly governs candidate admission. |
| 2 | HL/ONB #2 | PV1-1 — `.tfw/README.md` NS2 | ✅ | ✅ | ✅ — purpose, questions, human authority, and proportionate assurance match. | ✅ — directly supports owner authority and evidence gates. |
| 3 | HL/ONB #3 | PV1-2 — `.tfw/README.md` Methodology values | ✅ | ✅ | ✅ — Structural Enforcement and Portability are named values. | ✅ — directly supports versioned parity/schema gates. |
| 4 | HL/ONB #4 | PV2-1 — `knowledge/philosophy.md` absent | ✅ | ✅ — the claimed absence was confirmed. | ✅ — N/A is represented truthfully. | ✅ — no additional priority-2 rule was available. |
| 5 | HL/ONB #5 | PV3-1 — `KNOWLEDGE.md` D1 | ✅ | ✅ | ✅ — JSON is source; README is generated. | ✅ — production mutation boundary follows it. |
| 6 | HL/ONB #6 | PV3-2 — `KNOWLEDGE.md` D2 | ✅ | ✅ | ✅ — offline generation/schema and network validation are separated. | ✅ — supports deterministic tests plus bounded CL probes. |
| 7 | HL/ONB #7 | PV3-3 — `KNOWLEDGE.md` D4 | ✅ | ✅ | ✅ — categories live in the catalog, not code. | ✅ — intake reads the current category map. |
| 8 | HL/ONB #8 | PV3-4 — `KNOWLEDGE.md` D14 | ✅ | ✅ | ✅ — project operations use `kz-*`, framework operations `tfw-*`. | ✅ — command placement follows the namespace boundary. |
| 9 | HL/ONB #9 | PV3-5 — `KNOWLEDGE.md` D18 | ✅ | ✅ | ✅ — evidence must be target-bound and the universe exactly reconciled. | ✅ — directly supports occurrence/candidate and observation binding. |
| 10 | HL/ONB #10 | PV3-6 — `KNOWLEDGE.md` D19 | ✅ | ✅ | ✅ — EN/RU/KK are explicit with no fallback. | ✅ — directly supports locale-complete add gates. |
| 11 | HL/ONB #11 | PV4-1 — `.tfw/conventions.md` §3 Evidence | ✅ | ✅ | ✅ — real-environment evidence is distinct from verification. | ✅ — calibration/runtime evidence belongs in EV. |
| 12 | HL/ONB #12 | PV4-2 — `.tfw/conventions.md` §9 | ✅ | ✅ | ✅ — tool adapters normally use a tool-agnostic core. | ✅ — the approved complete-copy exception is explicitly identified. |
| 13 | HL/ONB #13 | PV4-3 — `.tfw/conventions.md` §11 | ✅ | ✅ | ✅ — placeholders and manually repaired results are forbidden. | ✅ — applies to closed payloads and command completeness. |
| 14 | HL/ONB #14 | PV4-4 — `.tfw/conventions.md` §14 | ✅ | ✅ | ✅ — bonus scope, invented evidence, and provider-bound truth are forbidden. | ✅ — directly supports scope and evidence boundaries. |
| 15 | HL/ONB #15 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | ✅ | ✅ — dead communities are archived rather than deleted. | ✅ — archive collisions must be explicit. |

Total unique citations: 15; resolved: 15; semantically verified: 15; irrelevant: 0;
hallucinated: 0. One citation intentionally and correctly records an absent priority-2 file.

`KNOWLEDGE.md` D1, D2, D4, D14, D18, and D19 were checked for contradiction. None contradicts
the intended implementation direction; D18 makes F2 a material contract finding rather than a
knowledge contradiction.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈23 × 0.42⌉ files and recorded findings? All 23 RF-claimed paths plus two supporting public seal artifacts were audited.
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — key claims spot-checked, every citation traced, data claims checked against primary sources?
- [x] Each RF §3 (AC) checkmark verified against actual files?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 15 unique / 30 applications, resolved: 15 unique / 30 applications, semantically verified: 15 unique / 30 applications, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 8, present: 8, fully matched: 4, partial: 1, mismatched: 3

Stage complete: YES

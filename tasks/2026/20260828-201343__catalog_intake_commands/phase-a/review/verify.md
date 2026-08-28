# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 21 (12 implementation paths and 9 RF-created evidence paths)
> Files to verify: ⌈21 × 0.42⌉ = 9; a discrepancy was found, so verification escalated to all 21 claimed paths.

## Verification Log

### V1: `scripts/kz_intake.py`
- **RF claim:** Implements the closed root-URL grammar, fetch-once observation, exact closed
  preview/authority contracts, and exact-state idempotent apply.
- **Actual:** The main structure is present and the positive suite passes, but independent
  adversarial calls exposed three contract failures:
  1. `classify_token("https://t.me./valid_name")` returns
     `("candidate", "valid_name")` because line 236 removes a trailing dot from the parsed host.
     The TS grammar admits only the three literal root hosts and requires malformed/spoofed
     variants to remain non-candidates.
  2. `_exact` uses Python `isinstance` at lines 128–147. Because `bool` is a subclass of `int`, a
     preview whose integer total is `true` passes. The add gate at lines 481–489 also accepts
     `evidence_refs: [""]`, and `validate_observation` at lines 424–451 accepts a `verified`
     observation whose transport says `ok: false`. These values are incompatible with the closed,
     evidence-linked observation/preview contract.
  3. Apply labels a path `B` before testing `A` at lines 642–646. When a legitimate controlled
     path has equal before/after hashes, first apply succeeds, but the exact rerun is classified as
     an unmarked `B/A` mixture and stops at lines 653–654 instead of returning the required
     all-after no-op.

  Exact adversarial observations:

  ```text
  trailing_dot_host ACCEPTED ('candidate', 'valid_name')
  bool_in_integer_field ACCEPTED None
  blank_evidence_ref ACCEPTED None
  verified_with_failed_transport ACCEPTED None
  partial_equal_first applied_exact ['B', 'B', 'B', 'B', 'B']
  partial_equal_rerun REJECTED IntakeError unknown or unmarked mixed controlled-path state
  ```
- **Match:** ❌

### V2: `scripts/validate_links.py`
- **RF claim:** Adds only a minimal immutable fetch/retry seam while preserving all six classifier
  authority bodies and predecessor behavior.
- **Actual:** Independent AST/source-span hashing at base
  `be830d3766ca4de12ff18198a680253ed133894f` and implementation
  `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a` produced equal byte hashes for
  `TelegramPreviewParser`, `parse_member_count`, `handle_from_url`,
  `observed_preview_type`, `result`, and `classify_response`. The predecessor link matrix passed,
  including retry, identity-decoy, conflict, update, and archive cases.
- **Match:** ✅

### V3: six runtime command copies

| Path | Actual |
|---|---|
| `.claude/commands/kz-add.md` | Complete command body; byte-identical to Codex copy; root-neutral repository paths and preview/apply stop present. |
| `.agents/skills/kz-add/SKILL.md` | Exact byte copy of Claude `kz-add`; valid skill metadata. |
| `.claude/commands/kz-stats.md` | Complete owner-triage command; repair/archive authority preserved. |
| `.agents/skills/kz-stats/SKILL.md` | Exact byte copy of Claude `kz-stats`; valid skill metadata. |
| `.claude/commands/kz-release.md` | Complete local release preparation command; exact-current-approval stop before tag/push preserved. |
| `.agents/skills/kz-release/SKILL.md` | Exact byte copy of Claude `kz-release`; valid skill metadata. |

Static pair hashes at the implementation SHA match the runtime-smoke records: `kz-add` is 5,331
bytes / `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414`, `kz-stats`
is 3,761 bytes / `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe`, and
`kz-release` is 3,532 bytes /
`2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc`. `AGENTS.md` is 8,768
bytes / `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612`. The sync check and
predecessor command matrix both passed.

- **Match:** ✅ for static completeness, parity, path neutrality, and preserved command semantics;
  AC-7 runtime-loading proof is assessed separately under V6/E7.

### V4: `scripts/sync_kz_commands.py`, `scripts/test_kz_intake.py`, and `scripts/test_kz_commands.py`
- **RF claim:** Enforce the exact three-command inventory/parity contract and exercise the complete
  intake grammar, closed schemas, authority, idempotency, and recovery behavior.
- **Actual:** Inventory, parity, drift, sync-direction, and the existing intake tests pass. The
  intake suite does not cover trailing-dot authorities, JSON booleans in integer fields, blank
  evidence references, verified observations with failed transport, or a controlled path whose
  before and after hashes are equal. Consequently the suite's green result does not establish the
  corresponding closed-grammar/schema/idempotency claims.
- **Match:** ⚠️ partial

### V5: `AGENTS.md`
- **RF claim:** Registers the exact three project commands and distinguishes availability from
  evidence of execution.
- **Actual:** The table contains exactly `/kz-add`, `/kz-stats`, and `/kz-release`, accurately names
  their execution boundaries, and explicitly says command availability does not prove a live
  sweep, intake apply, or release.
- **Match:** ✅

### V6: all nine RF-created evidence paths

| Path | Actual |
|---|---|
| `evidence/calibration-observations.json` | Eight observations and an exact calibration-only source ledger; all rows validate under the current implementation, but that validator has the V1 schema gap. |
| `evidence/production-hashes-pre-calibration.json` | Resolves and matches independently computed Git-blob hashes. |
| `evidence/production-hashes-post-calibration.json` | Resolves and matches; controlled production bytes remain equal. |
| `evidence/production-hashes-pre-ac7.json` | Resolves and matches; controlled production bytes remain equal. |
| `evidence/production-hashes-final.json` | Resolves and matches at RF base. |
| `evidence/site-metadata-summary.json` | Resolves and is byte-identical (11,097 bytes, SHA-256 `bbf30af0cdf5fbc26d547a80e97d9199035841e47b370cd2b0dc238a527f0552`) to the previously approved `catalog_discoverability` Phase B metadata summary. |
| `evidence/claude-runtime-smoke.jsonl` | Seven coordinator-transcribed summary records, not a redacted complete prompt/response transcript or per-invocation local-file loading trace. It does retain the three excluded harness deviations. |
| `evidence/codex-runtime-smoke.md` | A coordinator transcription that explicitly says the full final report remains in a mailbox; no complete fresh-task transcript is in the repository. |
| `evidence/EV__phase-a__intake_engine.md` | Covers E1–E8 using valid status vocabulary, but marks every item VERIFIED despite the implementation and evidence discrepancies recorded here. |

- **Match:** ⚠️ partial

### V7: exact scope and commit binding
- **RF claim:** The implementation is exactly 12 paths, 8 new/4 modified, with 1,885
  insertion-plus-deletion lines, and evidence completion did not change implementation.
- **Actual:** The parent-to-implementation diff contains exactly the twelve implementation paths
  listed in V1–V5 plus nine evidence paths. The twelve implementation paths are 8 new/4 modified,
  and their insertion-plus-deletion sum is exactly 1,885. The diff from implementation commit
  `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a` to RF base
  `624d0b6be2fbf7cdaec1e1918ee3d2c7661f0f3f` changes only RF/evidence records.
- **Match:** ✅

### V8: sealed calibration boundary
- **RF claim:** The public commitment and disclosed calibration input prove that only the committed
  eight-case calibration entered execution and no holdout/source material entered artifacts or
  context.
- **Actual:** The public commitment and calibration input are committed before implementation,
  internally agree on method, manifest digest, and counts, and the eight observed handles exactly
  equal the eight disclosed calibration handles. A scan of all permitted Phase A artifacts found
  only those eight real handles plus obvious synthetic sentinels. However, the permitted evidence
  contains no partition manifest or non-revealing inclusion proof. Repeating the manifest SHA-256
  in the public commitment and calibration input cannot independently establish that the disclosed
  eight cases belong to that manifest or that the stated 8/20 split was followed. Holdout and raw
  source material were intentionally not accessed during this review.
- **Match:** ⚠️ partial — precommit timing, disclosed-set use, and repository leakage scan hold;
  the TS-required exact manifest audit is not reproducible from reviewer-permitted evidence.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands -v` | PASS — 31 tests. |
| 2 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, 0 errors. |
| 3 | `python scripts/generate_readme.py --check` | PASS — four projections current. |
| 4 | `python docs/scripts/gen_index.py --validate` | PASS — four tasks validate. |
| 5 | `python -m py_compile` for the five changed/new Python runtime/test modules | PASS. |
| 6 | `python scripts/sync_kz_commands.py --check` | PASS — exact inventory and byte parity. |
| 7 | `git diff --check` | PASS. |
| 8 | Direct `run_link_matrix(validate_links)` and `run_command_matrix()` from the Phase C offline harness | PASS — retry, decoy/conflict, update/archive, stats/release semantics. |
| 9 | Independent AST/source-span hash comparison for six classifier authority bodies | PASS — all exact between sealed base and implementation. |
| 10 | Independent Git-blob hashes at seal, execution, implementation, and RF commits | PASS — all five controlled paths are identical at every checkpoint and match recorded evidence. |
| 11 | Adversarial `classify_token("https://t.me./valid_name")` | FAIL contract — accepted as `candidate/valid_name`. |
| 12 | Adversarial preview validation with `true` in an integer field | FAIL contract — accepted. |
| 13 | Adversarial add preview with `evidence_refs: [""]` | FAIL contract — accepted. |
| 14 | Adversarial verified observation with `transport.ok: false` | FAIL contract — accepted. |
| 15 | Temporary-project apply/rerun with one equal before/after controlled path | FAIL contract — first apply succeeds; exact rerun stops as an unmarked mixed state. |
| 16 | Fresh local Jekyll container rebuild | NOT RUN — the attempted command was rejected by the execution safety policy before start. The checked-in summary was instead hash-compared byte-for-byte with the previously approved primary artifact; no build result is claimed by this review. |

The historical harness's full `main()` was not used because its line 279 hardcodes a stale
`oldest_live == 2026-01-30` assertion while the current catalog's oldest live verification date is
`2026-08-27`. Its reusable link and command matrices were run directly and passed.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “only the closed root HTTPS grammar produces candidates” | RF §3 / E1 | `scripts/kz_intake.py` and adversarial runtime call | ❌ — a trailing-dot authority is normalized into an allowed host. |
| C2 | “all-after is a no-op” and apply is exact-state idempotent | RF §§2–3 / E4 | `scripts/kz_intake.py` and isolated temporary-project reproduction | ❌ — an unchanged controlled path makes the exact rerun an unmarked mixed state. |
| C3 | Fresh runtimes “loaded exact local runtime bytes” | RF §3 / E7 | `claude-runtime-smoke.jsonl`, `codex-runtime-smoke.md`, and static Git-blob hashes | ❌ — hashes establish repository bytes, while the two runtime files are coordinator summaries and contain no complete model exchange or per-invocation load proof. |
| C4 | Production bytes remained unchanged | RF §4 / E4/E8 | Git blobs at `be830d`, `dd49842`, `f8fd502`, and `624d0b6`; four checkpoint files | ✅ — exact hashes are equal at every point: `data/communities.json` `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d`, `README.md` `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d`, index `4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3`, RU `36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97`, KK `64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7`. |
| C5 | Implementation is 12 paths / 1,885 changed lines | RF §§1,4 | parent-to-implementation Git diff | ✅ — independently reproduced exactly. |

All artifact links in the RF, EV, master HL §7.2, and ONB §7 were resolved. Data/count claims were
checked against the repository source or Git objects rather than copied from RF summaries.

## Discrepancies Found

1. **D1 — AC-1 grammar is broader than the closed contract.** `rstrip(".")` accepts a
   trailing-dot authority such as `https://t.me./valid_name` as a production candidate.
2. **D2 — AC-3 schemas and evidence gating are not closed.** JSON booleans can satisfy integer
   fields; a blank string satisfies `evidence_refs`; and `status: verified` is not tied to a
   successful transport tuple.
3. **D3 — AC-4 exact rerun fails when any controlled path is intentionally unchanged.** Equal
   before/after hashes are classified only as before-state, creating an unmarked mixture after
   the first successful apply.
4. **D4 — AC-7's required complete fresh-runtime transcripts are absent.** Both artifacts are
   coordinator transcriptions; the Codex artifact expressly locates the full result outside the
   repository. Static hashes and summaries do not prove what each fresh runtime loaded or how its
   literal exchange completed. The three Claude harness deviations are honestly recorded and
   excluded, but their summaries do not cure the missing accepted transcripts.
5. **D5 — AC-6's exact partition-manifest audit is not independently reproducible.** The public
   files prove precommit timing, eight disclosed cases, internal hash/count agreement, and no
   visible artifact leakage; they do not provide a verifier-usable proof that those cases are the
   committed partition without exposing the holdout.
6. **D6 — The Phase A Jekyll build was not independently rerun in this review.** Execution policy
   rejected the attempted container command before start. The checked-in summary exactly matches
   the already approved metadata artifact and other deterministic gates pass, but this review does
   not claim a fresh build reproduction.

Because D1 was found during sampling, every one of the 21 RF-claimed paths was opened and audited.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | AC-1 synthetic grammar evidence | ✅ | ❌ — the positive suite passes but omits the accepted trailing-dot authority. |
| E2 | AC-2 classifier/calibration evidence | ✅ | ⚠️ partial — classifier hashes and predecessor matrices hold; observation validation does not bind verified status to successful transport. |
| E3 | AC-3 canonical preview/authority evidence | ✅ | ❌ — boolean integers and blank evidence references are accepted. |
| E4 | AC-4 apply/hash evidence | ✅ | ❌ — hashes are correct, but the all-after/idempotent claim fails for equal before/after paths. |
| E5 | AC-5 command parity evidence | ✅ | ✅ — exact inventory, byte parity, static completeness, path neutrality, and predecessor semantics reproduced. |
| E6 | AC-6 commitment/calibration evidence | ✅ | ⚠️ partial — internal bindings and permitted leakage scan hold; exact manifest membership cannot be audited from the disclosed artifacts. |
| E7 | AC-7 Claude/Codex smoke evidence | ✅ | ❌ — the named files are summaries, not the TS-required redacted complete transcripts or runtime-load proof. |
| E8 | AC-8 aggregate verification evidence | ✅ | ❌ — scope, hashes, core tests, projections, index, compile, and predecessor matrices hold, but AC-1/3/4/7 do not; the fresh site rebuild was not independently reproduced. |

Evidence totals: 8 referenced items, 8 present, 1 fully matched, 2 partially matched, 5 mismatched.

## Knowledge Citations Verified

Each row covers both the master HL §7.2 citation and its mirrored ONB §7 application (30 artifact
applications total).

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
| 9 | HL/ONB #9 | PV3-5 — `KNOWLEDGE.md` D18 | ✅ | ✅ | ✅ — evidence must be target-bound and the universe exactly reconciled. | ✅ — directly supports occurrence/candidate accounting. |
| 10 | HL/ONB #10 | PV3-6 — `KNOWLEDGE.md` D19 | ✅ | ✅ | ✅ — EN/RU/KK are explicit with no fallback. | ✅ — directly supports locale-complete add gates. |
| 11 | HL/ONB #11 | PV4-1 — `.tfw/conventions.md` §3 Evidence | ✅ | ✅ | ✅ — real-environment evidence is distinct from verification. | ✅ — calibration/runtime evidence belongs in EV. |
| 12 | HL/ONB #12 | PV4-2 — `.tfw/conventions.md` §9 | ✅ | ✅ | ✅ — tool adapters normally use a tool-agnostic core. | ✅ — the approved complete-copy exception is explicitly identified. |
| 13 | HL/ONB #13 | PV4-3 — `.tfw/conventions.md` §11 | ✅ | ✅ | ✅ — placeholders and manually repaired results are forbidden. | ✅ — applies to closed payloads and command completeness. |
| 14 | HL/ONB #14 | PV4-4 — `.tfw/conventions.md` §14 | ✅ | ✅ | ✅ — bonus scope, invented evidence, and provider-bound truth are forbidden. | ✅ — directly supports the scope and evidence boundaries. |
| 15 | HL/ONB #15 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | ✅ | ✅ — dead communities are archived rather than deleted. | ✅ — archive collisions must be explicit. |

Total unique citations: 15; resolved: 15; semantically verified: 15; irrelevant: 0;
hallucinated: 0. One citation intentionally and correctly records an absent priority-2 file.

`KNOWLEDGE.md` D1, D2, D4, D14, D18, and D19 were also checked for contradiction with the actual
changes. None contradicts the implementation direction; D18's evidence boundary makes D2/D4
material quality findings rather than knowledge contradictions.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈21 × 0.42⌉ files and recorded findings? All 21 RF-claimed paths were audited.
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — key claims spot-checked, every citation traced, data claims checked against primary repository/Git sources?
- [x] Each RF §3 (AC) checkmark verified against actual files?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 15 unique / 30 applications, resolved: 15 unique / 30 applications, semantically verified: 15 unique / 30 applications, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 8, present: 8, fully verified: 1, partial: 2, mismatched: 5

Stage complete: YES

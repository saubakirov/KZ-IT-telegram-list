# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 14
> Files to verify: ⌈14 × 0.42⌉ = 6; one discrepancy escalated verification to all 14 claimed files

## Verification Log

### V1: `data/communities.json`
- **RF claim:** Phase C adds only an empty `archive` array and preserves all pre-existing semantic values and 63 live entries.
- **Actual:** Parsed comparison with `172e6ac^:data/communities.json` returned `preexisting_semantics_equal=True`, `archive_empty=True`, 40 groups + 18 channels + 5 bots = 63 live entries, 18 categories, and oldest date `2026-01-30`. The commit diff is the single `"archive": []` addition.
- **Match:** ✅

### V2: `scripts/validate_schema.py`
- **RF claim:** Enforces North Star/archive integrity and fatal strict dates while reporting valid staleness non-fatally.
- **Actual:** Production schema exited 0 with 63 stale entries reported; the committed harness rejected all TS-listed negative fixtures. Independent additions also rejected wrong-typed purpose/non-goals/items, an impossible live date, and a wrong-typed archive.
- **Match:** ✅

### V3: `scripts/validate_links.py`
- **RF claim:** Target/type-bound classification makes non-target content unable to create a date or count.
- **Actual:** The declared C3/C4/C5/count/failure/update/archive matrix passes, but `TelegramPreviewParser.handle_starttag()` adds **every** page anchor to `identity_urls` at lines 81–82. An independently constructed preview canonically and operationally bound to `other_group`, with only an unrelated description link to `requested_group`, was classified `verified` for `requested_group` with count `500`; `apply_updates()` then persisted date `2026-08-27` and count `500` to the wrong entry.
- **Match:** ❌ — High, AC-2/AC-7 target-identity failure

### V4: `scripts/generate_readme.py`
- **RF claim:** Generates Purpose, dynamic conservative stats, display-name ordering/current anchors, conditional archive, and non-mutating normalized currency checks.
- **Actual:** Source review and independent execution confirmed each behavior; `--check` exited 0, the isolated archive/stale/CRLF cases passed, and no `datetime` import or new dependency exists.
- **Match:** ✅

### V5: `.claude/commands/kz-stats.md`
- **RF claim:** Complete future CL sweep with structured deltas, retry, target-specific browser fallback, four dispositions, owner/evidence archive gate, and no release work.
- **Actual:** All ordered gates and references are present and resolve. The document is complete, but it relies on the defective classifier's `verified` state, so the operation cannot presently guarantee that an apparently verified record is target-bound.
- **Match:** ⚠️ partial — document matches TS; its classifier dependency does not

### V6: `.claude/commands/kz-release.md`
- **RF claim:** Implements schema/currency/evidence gates, truthful commit preparation, and a hard stop before tag/push.
- **Actual:** Ordered static inspection confirms all refusal and authority gates, including current owner approval; all local references resolve. It was not invoked.
- **Match:** ✅

### V7: `.github/workflows/validate.yml`
- **RF claim:** Pull-request and `master` push workflow runs only schema and non-mutating README currency checks.
- **Actual:** YAML parsed locally; triggers, supported Python, checkout, schema, and `--check` steps are present. No link validator, browser, secrets, mutation, release, tag, or push operation appears.
- **Match:** ✅

### V8: `README.md`
- **RF claim:** Generator-current presentation-only output preserving all live facts.
- **Actual:** Full file inspection plus generator `--check` passed. Diff from the implementation parent adds Purpose/stats and reorders Engineering Management presentation only. All 63 formatted live entries resolve from unchanged JSON; no Archive row/section appears for `archive: []`.
- **Match:** ✅

### V9: `KNOWLEDGE.md`
- **RF claim:** D13 and D14 added once; predecessor decisions retain meaning; D15 absent.
- **Actual:** D1–D14 each occur once and D15 is absent. Removing only D13–D14 reproduces the ONB dirty baseline hash. Pre-existing shared-checkout Phase B documentation hunks remain unstaged and preserved.
- **Match:** ✅

### V10: `TECH_DEBT.md`
- **RF claim:** Only TD-3 and TD-6 resolve; TD-2/TD-4/TD-5/TD-10/TD-11 retain required dispositions.
- **Actual:** Keyed inspection confirms exactly those transitions. TD-5, TD-10, and TD-11 remain open; no Phase D freshness/archive claim appears.
- **Match:** ✅

### V11: `tasks/README.md`
- **RF claim:** Records Phase C RF completion and review handoff without closing TFW-4 or starting Phase D.
- **Actual:** TFW-4 reads `🟢 RF — Phase C complete; review next`, links the Phase C RF, and explicitly leaves Phase D after separate review/approval.
- **Match:** ✅

### V12: `ONB__phase-c__pipeline_tooling.md`
- **RF claim:** Records the approved offline boundary and reproducible protected/semantic snapshots.
- **Actual:** Full file inspected. Master blob `b18bb1…` matches baseline `d31e60d`; Phase HL/TS hashes match; replaying the case-insensitively ordered 134-row protected manifest returns `0fb1d8e…`, and the 12-file framework-command aggregate returns `288fde38…`.
- **Match:** ✅

### V13: `evidence/offline_harness.py`
- **RF claim:** Reproducibly proves all required offline matrices without sockets.
- **Actual:** Full source inspection confirms no network call path and the harness exits 0 for AC-1 through AC-6. Its AC-2 matrix tests C3/C4/C5 and a type mismatch, but not conflicting identity signals or an unrelated page anchor; it therefore misses V3's false-positive target binding.
- **Match:** ⚠️ partial

### V14: `evidence/EV__phase-c__pipeline_tooling.md`
- **RF claim:** All seven AC rows are covered; six are N/A real-world evidence, the forbidden-push remote CI run is DEFERRED, and deterministic local verification establishes the Phase C result.
- **Actual:** Artifact and all seven rows exist; the remote-run classification is honest and TS-compliant. E2 and derivative E7 overstate sufficiency because the classifier can still write a non-target count/date under the V3 fixture.
- **Match:** ⚠️ partial

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python scripts/validate_schema.py` | PASS, exit 0; 63 stale dates reported non-fatally, 0 errors |
| 2 | `python scripts/generate_readme.py --check` | PASS, exit 0; README generator-current |
| 3 | `python tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` | PASS, exit 0 for declared AC-1…AC-6 matrices |
| 4 | Independent in-memory schema wrong-type/impossible-date matrix (`python -B -c …`) | PASS; five additional negative cases rejected |
| 5 | Independent parent/current JSON semantic comparison (`python -c …`) | PASS; only `archive: []`, 63 live entries unchanged |
| 6 | Independent conflicting-identity classifier/update fixture (`python -B -c …`) | **FAIL acceptance:** canonical/action target `other_group` was reported `verified` for `requested_group`; date/count mutation reproduced |
| 7 | Protected and framework manifests replay | PASS; 134 / `0fb1d8e…`, 12 / `288fde38…` |
| 8 | Commit/tree/history audit (`git show`, `diff-tree`, `reflog`, refs/status) | PASS for scope/history boundary: `172e6ac` has exact 10 implementation paths; `c7180b9` has only board/RF/EV/harness; subjects/dates are truthful; no tags; branch remains 19 commits ahead of `origin/master` |
| 9 | Local Markdown-link resolver over Master/Phase C artifacts and command docs | PASS; 42/42 local Markdown targets resolve |
| 10 | `git diff --check 4bc1bb1..c7180b9` and protected-path diff | PASS; no whitespace error or protected Phase C commit path |

The configured `python scripts/validate_links.py` project test was not run because it opens the production Telegram network path forbidden by the approved Phase C TS. The independent failure is fully offline and does not invoke either `kz-*` command.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “Implementation commit … exactly the ten TS §4 paths” | RF §4 / EV AC-7 | Primary Git tree for `172e6ac18c7e604d553c38522650562d416dfb51` | ✅ — exact ten paths; 1327 insertions, 407 deletions |
| C2 | “Production data differs only by the empty archive container” and README preserves 63 live facts | RF §§1, 4 / EV E3, E7 | Parent/current parsed JSON, data diff, generated README, `--check` | ✅ — all six prior top-level values equal and 63 formatted entries retained |
| C3 | “Target-bound classifications … evidence-safe” | RF §§1–4 / EV E2 | `scripts/validate_links.py:81-82,196,398-404` plus independent conflicting-identity fixture | ❌ — unrelated page anchor is accepted as binding and wrong target data is persisted |

All 42 local Markdown links in the reviewed Master/Phase C/command artifacts resolve. Mutable catalog numbers were checked against the primary JSON; scope/attribution/tags were checked against primary Git objects and refs. No external source was contacted.

## Discrepancies Found

1. **High — `scripts/validate_links.py:81-82` / AC-2, AC-7.** Every anchor is admitted as an identity URL. A page whose canonical/operation target is another peer becomes `verified` for the requested handle if that handle merely appears in an unrelated link. The reproduced result persists a foreign verification date and member count through lines 398–404. This violates the TS target-binding contract and inherited no-inferred-fact failure boundary.
2. **Evidence consequence — EV E2/E7 and RF AC-2/AC-7.** The committed fixture matrix does not exercise contradictory/secondary-link identity and therefore does not establish the claimed classifier safety. This is the evidence impact of discrepancy 1, not a separate implementation defect.

Verification was escalated to 100% of the 14 RF-claimed files after discrepancy 1.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV E1 / `offline_harness.py` AC-1 | ✅ | ✅ — production, negative, and stale schema behavior independently reproduced |
| E2 | EV E2 / classifier-update-archive matrix | ✅ | ❌ — declared fixtures pass, but conflicting identity produces a verified wrong target and mutation |
| E3 | EV E3 / README and generator matrix | ✅ | ✅ — independently reproduced |
| E4 | EV E4 / command and adapter matrix | ✅ | ✅ — static command gates and adapter manifest verified; no invocation claimed |
| E5 | EV E5 / CI definition and local equivalents | ✅ | ✅ — local gates pass; remote run correctly `DEFERRED` because push is forbidden |
| E6 | EV E6 / decision and debt matrix | ✅ | ✅ — keyed transitions reproduced |
| E7 | EV E7 / bounded-state and all-AC claim | ✅ | ❌ — scope/history boundary holds, but “all offline gates” does not because AC-2 fails |

Evidence status vocabulary matches the TS: six `N/A`, one `DEFERRED`, zero fabricated `VERIFIED`. Presence is complete; substantive sufficiency is 5/7 because E2 and E7 do not establish their claims.

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | Master HL §7.2 #1 | Baseline North-Star fallback state | ✅ | ✅ — baseline header records no designated locus at freeze time |
| 2 | Master HL §7.2 #2–6 | `.tfw/README.md` values and principles | ✅ | ✅ — all five named principle sections exist |
| 3 | Master HL §7.2 #7–14 | `KNOWLEDGE.md` P1–P4 and D2/D3/D4/D7 | ✅ | ✅ — all eight items exist |
| 4 | Master HL §7.2 #15–20 | `conventions.md` §§2/3/4/9/14 | ✅ | ✅ — all six cited rules/sections exist |
| 5 | ONB §7 #1–20 | Applied restatement of the Master citation set | ✅ | ✅ — all source items above exist and apply as recorded |
| 6 | ONB §7 #21 | Phase B RF and repeat APPROVE REVIEW | ✅ | ✅ — RF exists; repeat REVIEW verdict is `✅ APPROVE` |

Total citations: 41, verified: 41, hallucinations: 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈14 × 0.42⌉ files and recorded findings? (14/14)
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 41, verified: 41, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 7, present: 7, substantively verified: 5, missing: 0, insufficient: 2

Stage complete: YES

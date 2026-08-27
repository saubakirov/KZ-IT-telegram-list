# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 5
> Files to verify: ⌈5 × 0.42⌉ = 3; escalated to all 5 claimed files and the complete evidence/source set after the RF-timing discrepancy was found.

## Verification Log

### V1: `evidence/g2_recheck_summaries.json`
- **RF claim:** Ordered, reversible, byte-preserving aggregate for the retained `datanomika` and fresh `kzquake` rechecks.
- **Actual:** 4669 bytes, SHA-256 `950ca60b7779e8f5f4c1e2e0cdf4804cf16f0079d08701163a90f0cd239ac489`. Record order is exactly `datanomika`, `kzquake`. For each record, decoded base64 is byte-identical to the named external raw file; byte length, SHA-256, strict UTF-8 JSON parse, stored summary deep equality, and `verified/channels/channels/target_bound=true` all pass.
- **Match:** ✅

### V2: `evidence/EV__phase-d__live_sweep_release.md`
- **RF claim:** Per-AC evidence index with 5 VERIFIED and 3 DEFERRED items, exact snapshots, hashes, coverage, and authority gates.
- **Actual:** E1–E5 resolve and independently pass. E6–E8 truthfully name absent G3/G4 authority and the open memory/closure work. All referenced repository and `E:\TEMP` artifacts exist at the stated paths and hashes.
- **Match:** ✅ for the evidence facts; the same E6–E8 records prove that Phase D execution is not complete.

### V3: `RF__phase-d__live_sweep_release.md`
- **RF claim:** A truthful non-completion G2 checkpoint, with AC1–AC5 complete and AC6–AC8 deferred.
- **Actual:** Its factual G1/G2 claims are true and its deferrals are honest. However, the artifact is still an `RF` and is paired with lifecycle `RF`. TS AC8 requires that the RF be written only after the final publication outcome is known (`TS`, lines 373–375), while the RF says G3/G4 were never authorized (`RF`, lines 5–8, 44–56). TS lines 380–381 allow recording a checkpoint but prohibit a completion RF/task closure; v2 has no partial-RF lifecycle subtype, and defines `RF` as “Execution complete, RF written” (`.tfw/conventions.md`, line 468).
- **Match:** ❌ — content honesty does not make the RF timing/lifecycle contract valid.

### V4: `data/communities.json`
- **RF claim:** Exact retained `datanomika` repair, exact `kzquake` repair, and exactly two owner-approved archives; no non-candidate drift.
- **Actual:** SHA-256 `b773a69d8f828b3732d387f797a5c41cbd37376d62be18e559b9a39d7d325de3`; schema passes. The final universe is 38 groups + 20 channels + 4 bots + 2 archives = 64 unique handles. Sequential pre-candidate snapshots prove that each of the four G2 edits changed only its named target and preserved all other records, ordering, categories, North Star content, and metadata. Both archives preserve the complete prior row and add only `type=groups`, `died_on=2026-08-27`, and the exact approved reason.
- **Match:** ✅

### V5: `README.md`
- **RF claim:** Fully regenerated from final G2 data and generator-current.
- **Actual:** SHA-256 `58266a695a3e50f0997c9b7adcbe349853942d68a7ab91a06060113fa0ee3697`; `generate_readme.py --check` passes. It contains exactly the 62 live and 2 archived unique Telegram handles, both exact archive reasons, 38/20/4/19 totals, and verification date `2026-08-27`.
- **Match:** ✅

### V6: immutable G1/cursor/retry/browser evidence
- **RF claim:** Original G1 artifacts stayed byte-exact and prove the 63+1 pre-G2 universe, four exact retries, and bounded browser fallback.
- **Actual:** Repository evidence hashes match EV: full sweep `bb99e525…` (63 entries), cursor `43605bba…` (one non-overlapping `cursor_kz`), retries `c1e4da02…` (four exact handles, once each), browser PDF `d57a6029…` (four visually inspected pages). The first three are byte-identical to their external raw/consolidated files; every retry raw file matches its recorded byte length, SHA-256, and embedded JSON. The PDF has four pages and the two source screenshots hash to `2dffc39a…` and `42c690ea…`; visual inspection confirms the two generic contact-shell results and zero-temporary-tab cleanup record.
- **Match:** ✅

### V7: protected baseline and Git boundary
- **RF claim:** Frozen Master, protected evidence, stashes, staged/unmerged state, and G3/G4 boundary are intact.
- **Actual:** Current Master bytes hash to `16fc5ddf…` and are byte-identical to baseline `d31e60d`. Phase HL/TS and all retained evidence match EV hashes. ONB's six external recovery snapshots match their recorded bytes/hashes. Current protected tracked framework, command, release, script, changelog, and Master surfaces equal HEAD; the only post-ONB generator change is the separately committed v2 migration `97dd429`. Both recorded stashes remain at `e1d755a…` and `23373bf…`; staged/unmerged sets and Git lock set are empty. `CHANGELOG.md` has no worktree diff, no `data-*` tag exists, HEAD is still `97dd429`, and no release commit/tag/push evidence exists.
- **Match:** ✅

### V8: v2 status/journal/index
- **RF claim:** Phase D status, four task-root journal events, and derived index validate.
- **Actual:** `gen_index.py --validate` and `--check` pass; 131 framework tests pass (1 skipped). All four journal filenames match their YAML times/kinds/actors, refs resolve, times are strictly increasing, and there is no phase-local journal. The index correctly projects Phase D as `RF`. The structural problem is the projected source value itself: `phase-d/status.md:6` says `RF` while AC6–AC8 and the publication outcome are open.
- **Match:** ⚠️ deterministic v2 integrity passes; lifecycle meaning does not.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, zero errors |
| 2 | `python scripts/generate_readme.py --check` | PASS — README generator-current |
| 3 | `python docs/scripts/gen_index.py --validate` | PASS — two task states validate against the closed schema |
| 4 | `python docs/scripts/gen_index.py --check` | PASS — `tasks/00-INDEX.md` current |
| 5 | `python -m pytest docs/scripts/test_gen_index.py docs/scripts/test_migrate_board.py -q` | PASS — 131 passed, 1 skipped |
| 6 | `git diff --check -- data/communities.json README.md` | PASS |
| 7 | `git diff --check` | PASS for the full tracked worktree diff |
| 8 | Independent Python evidence/coverage assertions | PASS — evidence hashes/raw identity; exact 63+1 coverage; 62 live + 2 archive final disposition; four exact retries; G2 aggregate byte/base64/deep equality; final count/date reconciliation |
| 9 | Independent Python four-snapshot keyed comparisons | PASS — only `datanomika`, then `kzquake`, then `mobile_developers_kz`, then `kzqacommunity` changed at each boundary; all non-candidate values and order invariant |
| 10 | Independent Python HEAD-to-checkpoint comparison | PASS — original 64 live handles become 62 live + exact two archives; surviving non-repair records change only observed member/date fields |
| 11 | Independent README/data keyed comparison | PASS — 64 unique rendered handles equal the 62 live + 2 archive data universe |
| 12 | Independent journal/status assertions | PASS — four immutable task-root events; exact actor/on-behalf/via/time/ref grammar; phase status/index projection consistent |
| 13 | Frozen/citation source checks via `git show d31e60d:…` and `git show 0097835:…` | PASS — all 20 Master and 21 ONB citations resolve and semantically match their artifact-time source trees |
| 14 | `git diff --exit-code HEAD -- .tfw .claude/commands RELEASE.md scripts docs/scripts CHANGELOG.md …` | PASS — no current Phase D worktree mutation on protected tracked surfaces |
| 15 | `git diff --exit-code d31e60d -- tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md` | PASS — frozen Master unchanged |
| 16 | Git state/tag/stash/lock probes | PASS — zero staged/unmerged/locks, exact two stashes, no data tag, no G3/G4 release state |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “63-entry G1 summary plus one-entry cursor supplement form the exact pre-G2 64-handle manifest” | RF §3; EV E2/§Coverage | Immutable repository JSON and byte-identical external raw files; final keyed data universe | ✅ |
| C2 | “Both target-bound repair summaries are reversibly preserved and unchanged” | RF §§1–4; EV E4/§Coverage | `g2_recheck_summaries.json` plus the two exact `E:\TEMP` raw files | ✅ |
| C3 | “No `/kz-release`, local release commit, tag, push, or publication occurred” | RF header, §2, AC6–AC8; EV E6–E8 | `CHANGELOG.md`, staged set, HEAD/log, local tags, branch/ahead state | ✅ — and therefore the final publication outcome required before RF does not exist |
| C4 | Every evidence/source citation resolves | RF §5 → EV; EV links/paths; Master HL §7.2; ONB §7 | Repository paths, external snapshots, and artifact-time Git trees | ✅ |
| C5 | Owner death facts are bound to the exact historical records | RF §7; TS §6; RES3 | Exact owner decision recorded in TS/source-task binding, RES3 continuity analysis, candidate snapshots, and final archive rows | ✅ |

## Discrepancies Found

1. **Premature RF and invalid partial-RF lifecycle.** `RF__phase-d__live_sweep_release.md:5-8,20,44-56` expressly says G3/G4 and AC6–AC8 are deferred, while `TS__phase-d__live_sweep_release.md:373-381` requires the RF only after the final publication outcome and prohibits a completion RF/task close while AC7 or frozen Master DoD remains open. `phase-d/status.md:6` nevertheless uses `RF`, which v2 defines as execution complete (`.tfw/conventions.md:468`); APPROVE would necessarily route to KNW (`.tfw/conventions.md:503-505`, `.tfw/workflows/review.md:135-146`) and create the forbidden completion path. The workflow offers only APPROVE/REVISE/REJECT, not “partial APPROVE.”

The discrepancy triggered 100% verification. No data, README, script, evidence-byte, archive, coverage, citation, or G3/G4-boundary discrepancy was found.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | ONB, `phase-d/status.md`, task journal | ✅ | ✅ protected baseline and v2 mechanics verified; lifecycle semantics separately fail as above |
| E2 | `live_sweep_summary.json`, `cursor_kz_supplement.json` | ✅ | ✅ exact immutable 63+1 coverage |
| E3 | `retry_summaries.json`, `browser_fallback.pdf` | ✅ | ✅ four exact retries and bounded fallback/cleanup evidence |
| E4 | `g2_recheck_summaries.json`, TS G2 package, four external candidate snapshots | ✅ | ✅ exact ordered repairs/archives and byte identity |
| E5 | final data/README hashes and validation outputs | ✅ | ✅ hashes, schema, generation, invariance, and coverage all pass |
| E6 | G3 local release preparation | ✅ EV row present | ✅ DEFERRED accurately — explicit `/kz-release` invocation absent |
| E7 | G4 publication | ✅ EV row present | ✅ DEFERRED accurately — exact publication approval/tag/push absent |
| E8 | completion memory/closure | ✅ EV row present | ✅ DEFERRED accurately — depends on open AC6/AC7 and Master DoD |

## Knowledge Citations Verified

Frozen Master citations were verified against the frozen `d31e60d` source tree; ONB citations were verified against its committed `0097835` source tree. This preserves artifact-time semantics across the later authorized TFW 2.0 migration. Current v2 PV0/PV1/PV3/PV4 sources were also scanned in full; PV5–PV7 have no relevant project topic files beyond the reviewed tooling documentation.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | Master HL §7.2 #1 | PV0 — no Project North Star designated at freeze | ✅ | ✅ | ✅ | ✅ Phase B was the designated gap closure |
| 2 | Master HL §7.2 #2 | PV1 — Traces Over Code | ✅ | ✅ | ✅ | ✅ grounds trace-before-improvement |
| 3 | Master HL §7.2 #3 | PV1 — Single Source of Truth | ✅ | ✅ | ✅ | ✅ grounds canonical rules/data ownership |
| 4 | Master HL §7.2 #4 | PV1 — Structural Enforcement | ✅ | ✅ | ✅ | ✅ grounds schema/CI/gates |
| 5 | Master HL §7.2 #5 | PV1 — Honesty Over Convincingness | ✅ | ✅ | ✅ | ✅ forbids invented counts/results |
| 6 | Master HL §7.2 #6 | PV1 — Completeness Over Speed | ✅ | ✅ | ✅ | ✅ forbids placeholders |
| 7 | Master HL §7.2 #7 | PV3 — KNOWLEDGE P1 | ✅ | ✅ | ✅ | ✅ data is product, README output |
| 8 | Master HL §7.2 #8 | PV3 — KNOWLEDGE P2 | ✅ | ✅ | ✅ | ✅ accuracy over coverage |
| 9 | Master HL §7.2 #9 | PV3 — KNOWLEDGE P3 | ✅ | ✅ | ✅ | ✅ validation precedes generation |
| 10 | Master HL §7.2 #10 | PV3 — KNOWLEDGE P4 | ✅ | ✅ | ✅ | ✅ external state is CL territory |
| 11 | Master HL §7.2 #11 | PV3 — KNOWLEDGE D2 | ✅ | ✅ | ✅ | ✅ preserves separate scripts |
| 12 | Master HL §7.2 #12 | PV3 — KNOWLEDGE D3 | ✅ | ✅ | ✅ | ✅ retry/throttle boundary |
| 13 | Master HL §7.2 #13 | PV3 — KNOWLEDGE D4 | ✅ | ✅ | ✅ | ✅ data-owned categories |
| 14 | Master HL §7.2 #14 | PV3 — KNOWLEDGE D7 | ✅ | ✅ | ✅ | ✅ generator constraint; later superseded by D15 only for lifecycle carrier |
| 15 | Master HL §7.2 #15 | PV4 — conventions §9 adapter pattern | ✅ | ✅ | ✅ | ✅ adapters remain protected |
| 16 | Master HL §7.2 #16 | PV4 — conventions §3 Project North Star | ✅ | ✅ | ✅ | ✅ purpose plus non-goals |
| 17 | Master HL §7.2 #17 | PV4 — conventions §3 rules 13–16 | ✅ | ✅ | ✅ | ✅ frozen baseline discipline |
| 18 | Master HL §7.2 #18 | PV4 — conventions §4 attribution | ✅ | ✅ | ✅ | ✅ commit/push authority boundary |
| 19 | Master HL §7.2 #19 | PV4 — conventions §14 executor scope | ✅ | ✅ | ✅ | ✅ prevents adjacent fixes |
| 20 | Master HL §7.2 #20 | PV4 — conventions §2 Task Board default | ✅ | ✅ | ✅ | ✅ explicitly documented historical project deviation |
| 21 | ONB §7 #1 | PV0 — frozen Master had no North Star | ✅ | ✅ | ✅ | ✅ reconciled to delivered README Purpose |
| 22 | ONB §7 #2 | PV1 — Traces Over Code | ✅ | ✅ | ✅ | ✅ ONB preserves intent/state |
| 23 | ONB §7 #3 | PV1 — Single Source of Truth | ✅ | ✅ | ✅ | ✅ data/command contracts retained |
| 24 | ONB §7 #4 | PV1 — Structural Enforcement | ✅ | ✅ | ✅ | ✅ hashes/manifests/gates replayable |
| 25 | ONB §7 #5 | PV1 — Honesty Over Convincingness | ✅ | ✅ | ✅ | ✅ failed probes/untracked state reported |
| 26 | ONB §7 #6 | PV1 — Completeness Over Speed | ✅ | ✅ | ✅ | ✅ no onboarding stubs |
| 27 | ONB §7 #7 | PV3 — KNOWLEDGE P1 | ✅ | ✅ | ✅ | ✅ source/output snapshot boundary |
| 28 | ONB §7 #8 | PV3 — KNOWLEDGE P2 | ✅ | ✅ | ✅ | ✅ no unverified facts accepted |
| 29 | ONB §7 #9 | PV3 — KNOWLEDGE P3 | ✅ | ✅ | ✅ | ✅ schema → generate → check |
| 30 | ONB §7 #10 | PV3 — KNOWLEDGE P4 | ✅ | ✅ | ✅ | ✅ G1–G4 remain CL gates |
| 31 | ONB §7 #11 | PV3 — KNOWLEDGE D2 | ✅ | ✅ | ✅ | ✅ script responsibilities unchanged |
| 32 | ONB §7 #12 | PV3 — KNOWLEDGE D3 | ✅ | ✅ | ✅ | ✅ exact retry after unresolved result |
| 33 | ONB §7 #13 | PV3 — KNOWLEDGE D4 | ✅ | ✅ | ✅ | ✅ catalog structure remains data-owned |
| 34 | ONB §7 #14 | PV3 — KNOWLEDGE D7 | ✅ | ✅ | ✅ | ✅ historically correct at ONB; v2 D15 later replaces live board state |
| 35 | ONB §7 #15 | PV4 — conventions §9 adapter pattern | ✅ | ✅ | ✅ | ✅ project commands referenced/protected |
| 36 | ONB §7 #16 | PV4 — conventions §3 Project North Star | ✅ | ✅ | ✅ | ✅ Purpose governs dispositions |
| 37 | ONB §7 #17 | PV4 — conventions §3 rules 13–16 | ✅ | ✅ | ✅ | ✅ baseline recorded before execution |
| 38 | ONB §7 #18 | PV4 — conventions §4 attribution | ✅ | ✅ | ✅ | ✅ local executor attribution boundary |
| 39 | ONB §7 #19 | PV4 — conventions §14 executor scope | ✅ | ✅ | ✅ | ✅ no adjacent implementation drift |
| 40 | ONB §7 #20 | PV4 — conventions §2 Task Board default | ✅ | ✅ | ✅ | ✅ explicit accepted historical deviation |
| 41 | ONB §7 #21 | NEW PV0 — README § Purpose | ✅ | ✅ | ✅ | ✅ dated evidence/no promotion/no estimation/data authority |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈5 × 0.42⌉ files and recorded findings? All 5 RF files plus every evidence/source artifact were checked.
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — key claims checked, every citation traced, and data claims checked against primary raw/snapshot sources?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 41, resolved: 41, semantically verified: 41, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 8, verified: 8 as truthful statuses (5 VERIFIED, 3 DEFERRED), missing: 0

Stage complete: YES

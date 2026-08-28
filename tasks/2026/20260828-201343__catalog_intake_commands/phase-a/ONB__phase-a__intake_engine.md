# ONB — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-28
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Revision authorized; no blocking questions
> **Parent HL**: [Master HL](../HL-20260828-201343__catalog_intake_commands.md)
> **Phase HL**: [Phase A HL](HL__phase-a__intake_engine.md)
> **TS**: [TS Phase A](TS__phase-a__intake_engine.md)
> **Original implementation baseline**: `be830d3766ca4de12ff18198a680253ed133894f`
> **Approved revision base**: `067528dba201e93d3a8d4efcb525d9bdfcb753d0`

---

## 1. Understanding

This revision must close exactly the formal REVIEW findings F1a, F1b, and F2 without reopening
the already-closed D1–D6 or prior F1/F2 boundaries. Zero-ADD must bind all five controlled paths
to the exact baseline bytes. Exact 1/N ADD must derive the catalog as baseline plus only approved
localized rows, mechanically rebind `localization_review.payload_sha256` and
`changed_key_count`, preserve the project's exact JSON/LF serialization, and pass the real schema
and generator preflight. Serialized transport observations must match only the attempt/status/
reason tuples emitted by `fetch_preview_with_retry`.

The current worktree is clean at the exact approved revision base. The revised TS budget is
feasible as exactly 13 implementation paths: 8 new and 5 modified relative to the original
implementation baseline, with `scripts/validate_schema.py` as the sole newly authorized path.
The implementation ceiling remains at most 2500 insertion-plus-deletion lines. Only
`scripts/kz_intake.py`, `scripts/test_kz_intake.py`, and `scripts/validate_schema.py` require new
implementation edits in this revision.

## 2. Entry Points

- `scripts/validate_links.py` — existing pure `classify_response` authority and combined
  fetch/retry/classify entry point; only the minimum immutable fetch seam may change.
- `scripts/kz_intake.py` — exact action-stage byte derivation and producer-closed observation
  validation; command bodies, classifier bodies, and runtime hashes are unaffected.
- `scripts/test_kz_intake.py` — real 0/1/N schema/generator preflight, semantic-reserialization,
  catalog-last recovery, and exact transport-family regression tests.
- `scripts/validate_schema.py` — replace fixed `139/131/131` acceptance cardinalities with an
  independently data-derived locale payload invariant and truthful dynamic reporting.
- `tasks/2026/20260828-201343__catalog_intake_commands/phase-a/REVIEW__phase-a__intake_engine.md`
  and `review/verify.md` — exact exploit definitions and retained prior closures.
- `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` — predecessor retry,
  classifier, summary, update, archive, and command matrices.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The owner explicitly approved the narrow TS revision and autonomous
continuation through implementation, evidence, RF, lifecycle updates, and local commits.

## 4. Recommendations (suggestions, not blocking)

1. Centralize exact action-stage derivation in one pure helper used by preview validation and
   tests; this prevents the test fixture from independently recreating production semantics.
2. Derive expected locale payload counts independently from source structure, then compare them
   to the generated payload. This keeps duplicate-key/count loss detectable instead of replacing
   one mutable constant with another.
3. Reuse the retained calibration and fresh-runtime evidence because the approved change does not
   affect command bodies, classifier bodies, or calibration observation bytes; revalidate those
   artifacts and hashes rather than rerunning external observations.

## 5. Risks Found (edge cases, potential issues not in TS)

1. A data-derived locale count computed from the payload itself would be tautological. The count
   must be derived from categories, live/archive entries, non-goals, and fixed UI registries.
2. A semantic catalog comparison is insufficient even when real schema and generator checks pass;
   the expected source bytes must be compared before marker creation or any controlled write.
3. ADD derivation must update only the two review-binding fields in addition to the exact proposed
   rows. Updating `meta.last_updated`, reordering entries, reformatting JSON, or changing any other
   valid field must remain rejected.
4. Tests must keep production controlled paths untouched while still exercising real preflight
   and catalog-last failure/recovery inside isolated temporary project copies.

## 6. Inconsistencies with Code (spec vs reality)

1. The original ONB recorded a 12-path / 8-new / 4-modified ceiling. The approved revision now
   authorizes the Phase HL maximum of 13 paths and adds exactly one modified path,
   `scripts/validate_schema.py`; no other implementation path is available.
2. The current exact-add green test replaces `validate_staged_project` with a synthetic callback,
   so it does not establish the approved real schema/generator gate.
3. `validate_schema.py` validates fixed locale counts and prints the same constants. Exact localized
   additions therefore fail real preflight even after the review digest and changed-key total are
   mechanically correct; both acceptance and reporting must become data-derived.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV0-1 — `README.md` § Purpose | ✅ | Applied | Admission remains stricter than URL resolution; purely commercial, non-IT, non-KZ, and unverifiable rows cannot become proposed additions. |
| 2 | PV1-1 — `.tfw/README.md` NS2 | ✅ | Applied | Exact owner authority, visible uncertainty, and evidence proportional to catalog mutation risk remain hard gates. |
| 3 | PV1-2 — `.tfw/README.md` Methodology values | ✅ | Applied | Command parity, closed schemas, inventory checks, and ordinary repository files structurally enforce portability. |
| 4 | PV2-1 — `knowledge/philosophy.md` absent | ✅ | N/A | Confirmed that the cited priority-2 file does not exist; no additional philosophy rule is available. |
| 5 | PV3-1 — `KNOWLEDGE.md` D1 | ✅ | Applied | Production writes, if later authorized in Phase B, target JSON source only; Phase A changes neither source nor projections. |
| 6 | PV3-2 — `KNOWLEDGE.md` D2 | ✅ | Applied | Deterministic parser/apply tests remain offline; the eight calibration probes are a separate CL evidence step. |
| 7 | PV3-3 — `KNOWLEDGE.md` D4 | ✅ | Applied | Category validity is read from the current catalog categories map, not duplicated in intake code. |
| 8 | PV3-4 — `KNOWLEDGE.md` D14 | ✅ | Applied | All new operations stay in the project-owned `kz-*` namespace outside `.tfw/`. |
| 9 | PV3-5 — `KNOWLEDGE.md` D18 | ✅ | Applied | Candidate facts require target binding and full occurrence/candidate reconciliation before any proposal. |
| 10 | PV3-6 — `KNOWLEDGE.md` D19 | ✅ | Applied | EN/RU/KK values are explicit fields with no fallback or placeholder path. |
| 11 | PV4-1 — `.tfw/conventions.md` §3 Evidence | ✅ | Applied | Live calibration and fresh runtime observations go to EV; unit-test output remains verification, not evidence. |
| 12 | PV4-2 — `.tfw/conventions.md` §9 | ✅ | Applied with approved exception | A1 supersedes the normal thin-adapter pattern only for complete synchronized `kz-*` copies; reproducible parity compensates for copied bytes. |
| 13 | PV4-3 — `.tfw/conventions.md` §11 | ✅ | Applied | No placeholder schema fields, incomplete command bodies, or manually repairable outputs are acceptable. |
| 14 | PV4-4 — `.tfw/conventions.md` §14 | ✅ | Applied | The 13-path revised budget, no bonus fixes, no invented evidence, and no holdout/source access are enforced. |
| 15 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | Applied | Archive collisions remain explicit and cannot silently resurrect historical handles as new entries. |

No additional Project Values item was found that changes the approved Phase A implementation.

---

*ONB — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

# ONB — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-28
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Awaiting execution authorization; no blocking questions
> **Parent HL**: [Master HL](../HL-20260828-201343__catalog_intake_commands.md)
> **Phase HL**: [Phase A HL](HL__phase-a__intake_engine.md)
> **TS**: [TS Phase A](TS__phase-a__intake_engine.md)
> **Execution baseline**: `be830d3766ca4de12ff18198a680253ed133894f`

---

## 1. Understanding

Phase A must implement the approved I2-C1R intake contract without changing any production
catalog or projection byte. The result must account losslessly for one/many/file URL input,
reuse the existing target-bound classifier through a minimal fetch-once seam, keep observation
separate from editorial and owner authority, and enforce exact preview/envelope/pending-marker/
receipt state transitions on isolated fixtures. It must also install complete byte-identical,
location-neutral Claude and Codex copies of `kz-add`, `kz-stats`, and `kz-release`, preserving the
existing stats triage and release tag/push stops. Live Phase A use is limited to the committed
eight-case calibration input; no production candidate may be applied and no holdout material may
enter implementation, tests, prompts, transcripts, or evidence.

The dedicated worktree is clean on branch `codex/20260828-catalog-intake-phase-a` at the exact
approved base. The TS budget is feasible as exactly 12 implementation paths: all eight declared
CREATE paths are absent, all four MODIFY paths exist, and no additional implementation path is
required. The TS/delegated limits of 8 new, 4 modified, 12 total, and at most 2500 changed lines
are tighter than the project defaults and therefore govern execution.

## 2. Entry Points

- `scripts/validate_links.py` — existing pure `classify_response` authority and combined
  fetch/retry/classify entry point; only the minimum immutable fetch seam may change.
- `scripts/kz_intake.py` — new bounded parser, observation reconciliation, canonical preview,
  authority validation, and fixture-only apply orchestration.
- `scripts/sync_kz_commands.py` — new Claude-source-to-Codex exact inventory/sync/check gate.
- `scripts/test_kz_intake.py` and `scripts/test_kz_commands.py` — new deterministic branch,
  tamper, recovery, completeness, and parity coverage.
- `.claude/commands/kz-stats.md` and `.claude/commands/kz-release.md` — reviewed complete command
  contracts whose location-relative links must become location-neutral without semantic drift.
- `.claude/commands/kz-add.md` and `.agents/skills/kz-*/SKILL.md` — new complete synchronized
  runtime copies.
- `AGENTS.md` — project-operation inventory; update only when all three commands are truthful.
- `tasks/2026/20260828-201343__catalog_intake_commands/phase-a/evidence/calibration-input.json`
  and `input-commitment.json` — the only disclosed real-case input and its public commitment.
- `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` — the existing offline
  classifier/summary/update/archive predecessor matrix.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved TS, exact base, calibration-only input, authority boundary,
and path budget are sufficient to begin after the required ONB approval.

## 4. Recommendations (suggestions, not blocking)

1. Treat `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` as the concrete
   “predecessor suite” named by AC-2 and record its exact invocation in EV; the repository has no
   separate current `test_validate_links.py` module.
2. Capture SHA-256 for the five controlled production paths before implementation, before and
   after calibration, and at the final evidence gate. Keep every apply/failure-injection test in
   isolated temporary project copies.
3. Commit the completed implementation before AC-7 runtime evidence, then have the parent
   coordinate the required genuinely fresh non-forked Codex task and fresh nonpersistent Claude
   session against that exact SHA. Static parity or this contextualized executor session must not
   be substituted.
4. Keep `kz-canonical-json/v1` closed to the exact preview/envelope/marker/receipt domain and the
   standard library. A generic canonical-JSON abstraction or dependency would exceed the TS.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Source offsets are UTF-8 byte offsets, not Python character offsets. Multibyte wrapper text can
   make an apparently correct character-span ledger fail exact source accounting.
2. Seven disclosed calibration occurrences originate as bare source spans while the committed
   calibration artifact also provides allowed root `derived_url` values. Calibration must consume
   those disclosed derived URLs; it must not broaden the production grammar to admit bare handles.
3. `check_link_with_retry` currently combines transport, lossy UTF-8 decoding, retry timing, and
   classification. The new seam must preserve existing output/retry behavior while ensuring the
   same fetched payload reaches all three typed classifier calls.
4. AC-3 and AC-4 have a large adversarial surface within a strict line budget: duplicate-key and
   lexical rejection, closed recursive schemas, renderer completeness, exact action projection,
   and B/A/X recovery must remain independently testable rather than compressed into opaque logic.
5. Fresh literal Codex routing is not collectable inside this inherited task context. AC-7 remains
   a real post-implementation dependency until a newly created exact-SHA task supplies the required
   transcript and state hashes.

## 6. Inconsistencies with Code (spec vs reality)

1. The Phase HL says “at most 13 implementation paths,” while the approved TS and delegated
   execution boundary require exactly 12 paths (8 new, 4 modified). Execution will follow the
   tighter downstream TS/delegated budget and will not use a thirteenth path.
2. AC-2 refers to a predecessor suite, but no current `scripts/test_validate_links.py` exists;
   the comprehensive offline regression matrix is retained as the Phase C evidence harness named
   above. This is executable and non-blocking, but EV must identify it explicitly.
3. `.tfw/project_config.yaml` still names network-wide `python scripts/validate_links.py` as the
   generic project test. Running that command would probe the full production catalog, conflicting
   with this phase's calibration-only live-input boundary. Phase A will use the TS-specific offline
   suites plus exactly eight read-only calibration probes and report the generic configured command
   as superseded by the narrower approved phase gate.

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
| 14 | PV4-4 — `.tfw/conventions.md` §14 | ✅ | Applied | The 12-path budget, no bonus fixes, no invented evidence, and no holdout/source access are enforced. |
| 15 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | Applied | Archive collisions remain explicit and cannot silently resurrect historical handles as new entries. |

No additional Project Values item was found that changes the approved Phase A implementation.

---

*ONB — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

# RF — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-28
> **Author**: Executor (Codex)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Master HL](../HL-20260828-201343__catalog_intake_commands.md)
> **Phase HL**: [Phase A HL](HL__phase-a__intake_engine.md)
> **TS**: [TS Phase A](TS__phase-a__intake_engine.md)
> **Implementation SHA**: `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`

---

## 1. What Was Done

Phase A implemented a lossless Telegram candidate intake engine without changing a production
catalog or projection byte. It added a fixed source grammar and occurrence ledger, fetch-once
three-type reconciliation through the existing classifier, closed canonical preview/approval
contracts, and an exact-state crash-aware fixture apply boundary. It also installed complete
byte-identical `kz-add`, `kz-stats`, and `kz-release` command pairs for Claude and Codex with an
explicit Claude-to-Codex parity gate.

### New Files

| File | Description |
|------|-------------|
| `scripts/kz_intake.py` | Source parsing, observation reconciliation, closed canonical preview/envelope contracts, exact-state apply orchestration, and CLI. |
| `scripts/sync_kz_commands.py` | Exact three-command inventory, completeness/parity validator, and explicit Claude-to-Codex sync. |
| `scripts/test_kz_intake.py` | Synthetic adversarial parser, classifier, canonicalization, authority, stale-state, idempotency, and recovery tests. |
| `scripts/test_kz_commands.py` | Inventory, metadata, body completeness, parity, drift, and sync-direction tests. |
| `.claude/commands/kz-add.md` | Complete location-neutral Claude `/kz-add` runtime contract. |
| `.agents/skills/kz-add/SKILL.md` | Byte-identical Codex `/kz-add` runtime contract. |
| `.agents/skills/kz-stats/SKILL.md` | Byte-identical Codex `/kz-stats` runtime contract. |
| `.agents/skills/kz-release/SKILL.md` | Byte-identical Codex `/kz-release` runtime contract. |
| `phase-a/evidence/calibration-observations.json` | Exact eight-candidate read-only calibration observations and lossless source ledger. |
| `phase-a/evidence/production-hashes-*.json` | Pre/post calibration, pre-AC-7, and final controlled-path hash checkpoints. |
| `phase-a/evidence/site-metadata-summary.json` | Parsed deterministic built-site metadata summary. |
| `phase-a/evidence/claude-runtime-smoke.jsonl` | Bound accepted fresh Claude command runs and explicitly excluded harness deviations. |
| `phase-a/evidence/codex-runtime-smoke.md` | Bound fresh non-forked Codex literal command behavior and no-mutation state. |
| `phase-a/evidence/EV__phase-a__intake_engine.md` | Per-AC verification, live calibration, runtime, hashes, scope, and mutation evidence. |

### Modified Files

| File | Changes |
|------|---------|
| `scripts/validate_links.py` | Added the minimum immutable fetch/retry seam; existing classifier authority bodies remain unchanged. |
| `.claude/commands/kz-stats.md` | Made the existing complete owner-triage command location-neutral and parity-ready without weakening repair/archive authority. |
| `.claude/commands/kz-release.md` | Made the existing complete release command location-neutral and parity-ready while preserving pre-tag/pre-push approval. |
| `AGENTS.md` | Registered the truthful three-command project inventory and distinguished availability from execution evidence. |

The implementation budget is exactly 12 paths: 8 new, 4 modified, and 1,885 total
insertion+deletion lines. Evidence and lifecycle traces are outside that implementation budget.

## 2. Key Decisions

1. Production source grammar remains fixed to root HTTPS `t.me`, `telegram.me`, and
   `telegram.dog` handle URLs. The disclosed calibration's derived URLs were consumed without
   broadening production input to bare handles or salvaging parent/prefix forms.
2. One immutable fetch result is decoded once and passed unchanged through the existing
   target-bound classifier for all three declared types. No second identity classifier was added;
   all six established classifier authority bodies remain exact to the approved base.
3. `kz-canonical-json/v1` is a small standard-library-only closed domain for the exact Phase A
   payload/envelope/marker/receipt schemas, not a general JCS implementation.
4. Preview payload, current owner approval, pending recovery marker, and receipt remain separate
   objects. Apply may replace bytes only from exact all-before state or a matching durable marked
   mixture; all-after is a no-op and every unknown/unmarked state stops.
5. Claude command files are the explicit sync source, but both runtime copies are complete
   standalone bodies. Exact byte parity and fresh runtime behavior jointly establish portability.
6. The implementation was committed cleanly before AC-7. Fresh Claude and non-forked Codex
   smokes were then coordinated at that exact SHA; this Executor's contextualized task was not
   substituted for literal Codex command evidence.
7. Phase A used only the approved predecessor offline matrices and exactly eight disclosed
   calibration probes. It did not run the generic live full-catalog validator or use browser/auth
   fallback.

## 3. Acceptance Criteria

- [x] AC-1 — Every Telegram-like occurrence is accounted for before grouping and only the closed root HTTPS grammar produces candidates.
- [x] AC-2 — Arbitrary candidates are fetched once, reconciled through all three unchanged classifier calls, and fail closed on every non-exact tuple.
- [x] AC-3 — Canonical preview bytes, complete human rendering, action projection, and separate current owner authority are closed and tamper/replay resistant.
- [x] AC-4 — Apply revalidates before writes, is exact-state idempotent, permits only marked recovery, emits a separate receipt, and never touches production in Phase A.
- [x] AC-5 — Both runtime locations contain exactly the three complete byte-identical `kz-*` commands with non-mutating parity checks and preserved authority stops.
- [x] AC-6 — Only the committed eight-case calibration and public commitment entered execution; no holdout/source material entered implementation or evidence.
- [x] AC-7 — Fresh exact-SHA Claude and non-forked Codex literal smokes prove sentinel routing, stats triage, release approval boundaries, and zero mutation.
- [x] AC-8 — Approved tests/build/validation, predecessor behavior, exact scope, final hashes, and zero external mutation all pass.

## 4. Verification

- Tests: `python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands -v` — PASS, 31 tests.
- Command parity: `python scripts/sync_kz_commands.py --check` — PASS, exact `kz-add`, `kz-stats`, `kz-release` inventory.
- Compile: `python -m py_compile ...` for all five changed/new Python runtime/test modules — PASS.
- Schema: `python scripts/validate_schema.py` — PASS, 0 errors across 38 groups, 20 channels, 4 bots, 19 categories, and 2 archive entries.
- Projection currency: `python scripts/generate_readme.py --check` — PASS, all 4 projections current.
- Index: `python docs/scripts/gen_index.py --validate` — PASS, 4 tasks validate.
- Predecessor behavior: direct `run_link_matrix` and `run_command_matrix` from the Phase C
  `offline_harness.py` — PASS, including retry, identity decoy/conflict, summary/update/archive,
  and stats/release command behavior.
- Classifier audit: six authority bodies match base
  `be830d3766ca4de12ff18198a680253ed133894f` exactly — PASS.
- Built site: official local `actions/jekyll-build-pages:v1.0.13` read-only build followed by
  `python scripts/test_site_metadata.py --site <temporary-build>` — PASS for EN/RU/KK routes.
- Calibration: one bounded probe for each of exactly eight disclosed candidates — 8 fetched,
  8 verified, 0 unresolved, 0 fallback, 0 mutation.
- AC-7 runtime: three fresh Claude sessions and one fresh non-forked Codex task at
  `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a` — PASS with exact runtime hashes and clean
  before/after state.
- Scope: implementation commit contains exactly 12 implementation paths, 8 new/4 modified,
  1,885 insertion+deletion lines — PASS.
- Formatting/state: `git diff --check`, final status/staging audit, and five controlled-path hashes
  — PASS; production hashes are unchanged at every checkpoint.

Exact deviations:

- The generic configured `python scripts/validate_links.py` full-catalog live command was not run,
  by explicit TS/Coordinator boundary. Phase A used the approved predecessor offline suites plus
  exactly eight disclosed probes.
- The historical Phase C harness's full `main()` contains an unrelated stale fixed production-date
  assertion. The ONB-approved TS-relevant `run_link_matrix` and `run_command_matrix` were called
  directly and both passed.
- Before the accepted Claude invocations, one direct PowerShell attempt lost the empty tools
  argument and exited before model execution, one ProcessStartInfo attempt was policy-rejected
  before start, and one quoting probe returned unexecuted tool-call proposal text. All had zero
  writes/network, were superseded, and are explicitly excluded from accepted evidence.

## 5. Evidence

See [EV file](evidence/EV__phase-a__intake_engine.md) for evidence details.

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` | 279 | todo | The historical full harness asserts `oldest_live == 2026-01-30` while labeling the date dynamic; the current catalog's oldest live date is `2026-08-27`. The reusable link and command matrices pass, but a future full-harness run needs its snapshot assertion updated through the owning task. |

## 7. Fact Candidates

No fact candidates. The Coordinator messages supplied execution authority and evidence bindings,
not new human-only domain facts.

## 8. Strategic Insights (Execution)

No strategic insights. The execution followed the already approved TS and ONB recommendations;
no new stakeholder domain correction or strategy was introduced during implementation.

## 9. Diagrams

```mermaid
flowchart LR
    S[Text or UTF-8 file] --> L[Lossless occurrence ledger]
    L --> C[Grouped candidates]
    C --> F[Fetch once]
    F --> T[Existing classifier × 3 declared types]
    T --> P[Closed preview payload and human rendering]
    E[Editorial evidence] --> P
    P --> A[Separate current-owner approval envelope]
    A --> G{Controlled paths state}
    G -->|all before| W[Validate staged project, mark pending, replace exact bytes]
    G -->|all after| N[No-op: already_applied_exact]
    G -->|mixed + matching marker| R[Resume exact marked recovery]
    G -->|unknown or unmarked| X[Hard stop]
    W --> Q[Separate bound receipt]
    R --> Q
```

---

*RF — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

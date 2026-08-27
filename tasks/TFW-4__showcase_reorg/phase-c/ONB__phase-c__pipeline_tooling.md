# ONB — TFW-4 / Phase C: Pipeline & Tooling

> **Date**: 2026-08-27
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Complete; no blocking questions
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Phase HL**: [Phase C HL](HL__phase-c__pipeline_tooling.md)
> **TS**: [TS Phase C](TS__phase-c__pipeline_tooling.md)
> **Frozen baseline**: `d31e60d`; baseline and working Master HL blob
> `b18bb135e486ef5d6cfaa8cc8bc13bcb1012d41d` match

---

## 1. Understanding

Phase C must deliver the local, offline pipeline and project-operation surface already approved
by the frozen TFW-4 contract. The executor will add only an empty production archive container,
make the three existing scripts enforce and render the Phase B contract, define the two future
CL `kz-*` operations, add offline CI, regenerate `README.md` through the generator, record D13–D14
and resolve only TD-3/TD-6, then produce deterministic evidence and RF. No Telegram request,
browser action, live catalog mutation, Phase D work, release, tag, push, or framework/adapter
repair is authorized.

The AC dependency chain is load-bearing: AC-1 establishes the data contract before AC-2 and
AC-3; AC-4 follows AC-2/AC-3; AC-5 follows AC-1/AC-3; AC-6 follows AC-1/AC-4/AC-5; AC-7 is the
final bounded-state gate.

### Scope budget

| Measure | Approved estimate | Configured limit | Onboarding result |
|---------|-------------------|------------------|-------------------|
| Implementation paths | 10 | 30 files per phase | Within budget |
| New implementation files | 3 | 15 new files | Within budget |
| Modified implementation files | 7 | 30 modified files | Within budget |
| Implementation delta | <2000 LOC | 3000 LOC | Within budget |

## 2. Entry Points

| Path | Onboarding fact | Intended use |
|------|-----------------|--------------|
| `data/communities.json` | Holds `meta`, approved `north_star`, 63 live entries and 18 category definitions; no `archive` key | Add only an empty `archive` array; all six pre-existing top-level values are semantic invariants |
| `scripts/validate_schema.py` | Validates live required fields/categories/dates only | Enforce North Star/archive contracts and report non-fatal freshness |
| `scripts/validate_links.py` | Binary alive/dead classifier; page-wide count regex; date update depends on count | Add target-evidence classifications, pure offline mutation helpers, guarded archive operation and JSON summary without changing throttle/backoff constants |
| `scripts/generate_readme.py` | Key-sorted categories, count-only stats, no Purpose/archive, write-only behavior | Render the approved presentation and add normalized non-mutating `--check` |
| `.claude/commands/kz-stats.md` | Absent | Create future CL sweep/evidence/triage operation; do not invoke it |
| `.claude/commands/kz-release.md` | Absent | Create future release-preparation operation with hard stop; do not invoke it |
| `.github/workflows/validate.yml` | Absent | Create offline schema plus README-currency gates only |
| `README.md` | Generator-current Phase B artifact | Regenerate only through `generate_readme.py`; presentation-only live-entry output |
| `KNOWLEDGE.md` | Dirty predecessor state already contains D8–D12 | Preserve the dirty baseline and append D13–D14 only |
| `TECH_DEBT.md` | Dirty predecessor/reviewer state contains open TD-3/TD-6 and TD-10/TD-11 | Preserve the dirty baseline; resolve TD-3/TD-6 only |
| `tasks/README.md` | Dirty Coordinator-owned Phase C approval state | Apply only current handoff lifecycle status/link edits |
| `RELEASE.md` | Read-only dated-snapshot policy | Source for `/kz-release`; never mutate or execute release actions |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. The approved TS defines the data boundary, classifier outcomes, command authority gates, exact path scope and offline evidence plan. | N/A — proceed under the explicit AG/offline handoff without waiting. |

## 4. Recommendations (suggestions, not blocking)

1. Keep classifier, update, archive and renderer behavior in importable pure functions inside the
   three approved scripts. This makes the required C3/C4/C5 and mutation matrices deterministic
   without adding the general test suite excluded as TD-5.
2. Give the machine-readable link summary an explicit schema version and write it to a caller-
   selected path. `/kz-stats` can consume structured fields without parsing console prose.
3. Make archive mutation require an exact handle, a non-empty evidence reference, a non-empty
   reason and an explicit owner-approval flag. These structural inputs cannot prove death, but
   they prevent the CLI from presenting a failed request as sufficient authority.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Telegram preview markup can bind a requested handle while still failing declared-type
   continuity. A handle match alone must not verify a group/channel/bot type mismatch.
2. A verified no-count target must refresh `last_verified` without deleting or inventing a
   `member_count`; the update helper must keep observed-count absence distinct from numeric zero.
3. The production JSON currently mixes newline forms introduced by predecessor edits. The only
   authorized semantic change is `archive: []`; evidence must compare parsed values rather than
   treating a whole-file byte rewrite as catalog drift.
4. The checkout contains Coordinator/Reviewer dirty and untracked traces. All commits and diffs
   must be path-scoped; a broad add/restore would entangle or erase work that predates this handoff.

## 6. Inconsistencies with Code (spec vs reality)

1. Master HL §7.2 citation 1 still records that no Project North Star is designated, while Phase
   B has stored the approved `north_star` block and the Phase C derivation designates the generated
   `README.md § Purpose` locus. The locus is not yet present in the current generated README;
   AC-3 intentionally closes this transitional gap, so it is not blocking.
2. Master HL Phase C context permits a one-handle smoke request, but the later approved Phase C TS
   expressly forbids every network request and browser action. This execution follows the narrower
   approved TS boundary and uses synthetic offline fixtures only.
3. `validate_links.py` currently treats every marker-free HTTP 200 as alive and scans the entire
   page for count-like prose. This is the exact A5 defect AC-2 owns, not an unplanned scope issue.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV 0 — Project North Star transition | ✅ | Applied by AC-1/AC-3 | Preserve the approved JSON strings and establish only the generated README locus. |
| 2 | PV 1 — `.tfw/README.md` Traces Over Code | ✅ | Applied to ONB, EV and RF | Implementation claims remain traceable to deterministic output. |
| 3 | PV 1 — Single Source of Truth | ✅ | Applied to AC-4 | New project commands live only in `kz-*`; no framework command is copied or changed. |
| 4 | PV 1 — Structural Enforcement | ✅ | Applied to AC-1/AC-5 | Schema exits and CI/currency gates enforce the contract structurally. |
| 5 | PV 1 — Honesty Over Convincingness | ✅ | Applied throughout | Synthetic fixtures are labelled synthetic; no live/remote/release claim is permitted. |
| 6 | PV 1 — Completeness Over Speed | ✅ | Applied throughout | Production scripts and command documents will be complete, with no deferred implementation markers. |
| 7 | `KNOWLEDGE.md` P1 — data is the product | ✅ | Applied to AC-1/AC-3 | North Star/archive live in JSON; README remains generated output. |
| 8 | `KNOWLEDGE.md` P2 — accuracy over coverage | ✅ | Applied to AC-2 | Ambiguous/non-target evidence cannot create dates, counts or archive facts. |
| 9 | `KNOWLEDGE.md` P3 — validation precedes generation | ✅ | Applied to AC-4/AC-5 | Both future release operation and CI preserve schema-before-currency ordering. |
| 10 | `KNOWLEDGE.md` P4 — external state is CL | ✅ | Applied as a Phase C prohibition | No Telegram/browser observation is performed; fallback stays documented for Phase D. |
| 11 | `KNOWLEDGE.md` D2 — three scripts | ✅ | Applied | Responsibilities remain separate; commands orchestrate rather than merge them. |
| 12 | `KNOWLEDGE.md` D3 — rate limiting | ✅ | Applied to AC-2 | `BATCH_SIZE`, request/batch delays, retry attempts, timeout and backoff stay unchanged. |
| 13 | `KNOWLEDGE.md` D4 — categories in data | ✅ | Applied to AC-1/AC-3 | Category validation, count and names derive from the JSON map. |
| 14 | `KNOWLEDGE.md` D7 — Task Board locus | ✅ | Applied | `tasks/README.md` receives lifecycle state; generated README retains only the pointer. |
| 15 | `conventions.md` §9 — Tool Adapter Pattern | ✅ | Applied to AC-4 | Project adapters use the separate namespace; managed sources/copies are protected. |
| 16 | `conventions.md` §3 — Project North Star | ✅ | Applied to AC-1/AC-3 | Purpose plus all non-goals are required and rendered, not only a purpose statement. |
| 17 | `conventions.md` §3 rules 13–16 — Contract Baseline | ✅ | Applied | Recovered `d31e60d`; baseline and working Master HL blobs match. |
| 18 | `conventions.md` §4 — Commit Attribution | ✅ | Applied | Executor commits use `[codex/TFW-4/pipeline-tooling/executor]` and remain local. |
| 19 | `conventions.md` §14 — no scope drift | ✅ | Applied | Exact implementation/lifecycle paths only; TD-5/TD-10/TD-11 stay outside changes. |
| 20 | `conventions.md` §2 Task Board default vs D7 | ✅ | N/A as known project deviation | Project D7 intentionally places the board in `tasks/README.md`; no framework edit is permitted. |
| 21 | New PV — Phase B RF and repeat REVIEW | ✅ | Applied as predecessor fact | Phase B is accepted; exact North Star, D8–D12, release policy and dirty trace state are real inputs. |

## 8. Onboarding Snapshot

### Repository state

| Item | Snapshot |
|------|----------|
| Branch / HEAD | `master` / `158f432b7e16249a0df2cc7bbed6fb07bec1d872` (`origin/master` behind local by 16 commits) |
| Tags | None |
| Remote configuration | `origin` fetch/push URL recorded locally; no remote contact performed |
| Dirty tracked files before ONB | `KNOWLEDGE.md`, `TECH_DEBT.md`, `tasks/README.md`, `research/iterations.yaml` |
| Principal untracked state | `.agents/**`, Phase A/B/research traces, approved Phase C HL/TS |
| Protected manifest | 134 files; ordered `path<TAB>sha256<LF>` aggregate `0fb1d8e57de8912b523de688d7d3aa206a7fc3fe8430b0bb122afd1780d3edd1` |
| Framework command manifest | 12 `.claude/commands/tfw-*.md` files; aggregate `288fde38245a27073e9b703af05c2f936a31418f3206aff42b475eb39be933ce` |
| Phase C HL / TS SHA-256 | `7965eb479361df6f147a8394bcd021466308ecd5a896ddabc93182a85404771b` / `f51c5170ff0760986f04f48436ec69bfbd5107affcbbeb7e802c8285c0443f1d` |

The protected-manifest predicate is every current non-`.git`, non-`__pycache__` file except the
ten implementation paths, `tasks/README.md`, and Phase C ONB/RF/evidence paths. This includes
`.tfw/**`, `.agents/**`, all framework commands, Master/Phase A/Phase B/research traces, Phase C
HL/TS, root protected documents and legacy tasks. Replaying the same ordered UTF-8/LF
serialization must produce the same count and aggregate at AC-7.

### Production semantic invariants

| JSON value | Canonical onboarding SHA-256 |
|------------|------------------------------|
| `meta` | `5af830bea579d5e8494acfafd1d0084d7acd8d1638e6372f2e848b195b66b5e3` |
| `north_star` | `c412a46adb7cdaf2f73919d562780ac721a52ac444db1504b718a6fd7fb7693f` |
| `groups` | `768d97073d7b6fdd4b71c6734132393a796b1f688aa0170951af3dba71a25033` |
| `channels` | `f6b1f7419b7c48cb043858c1bd049dbc5d93b2eaa356aabd30563736ece9d8aa` |
| `bots` | `49eb5d75f8f6c081066bdd6bb6de8d6308b5c4d9e921a51da6f588210d5c69c6` |
| `categories` | `093ce984ba6213566889b6aba7fac78b0426a0135388209444998a1f7545a644` |

Canonical hashes above use PowerShell `ConvertFrom-Json` followed by ordered
`ConvertTo-Json -Depth 100 -Compress` and UTF-8 SHA-256; the same procedure is used at AC-7.
Initial file hashes: data `ed16ac0b…a161`, README `cc730c6b…94f9`, schema
`df770176…1fa`, links `6d6e9704…ae54`, generator `e5c96f82…06e0`, current dirty KNOWLEDGE
`5190da19…d0fe`, TECH_DEBT `0aa0466d…6e`, and Task Board `67808bca…09e9`.

---

*ONB — TFW-4 / Phase C: Pipeline & Tooling | 2026-08-27*

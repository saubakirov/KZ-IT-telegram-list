# Verify — TFW-4 / Phase B: Contract & Docs (Repeat Review)
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Map:** [map.md](map.md)
> **Min verify ratio:** 0.42
> **RF implementation files claimed:** 7
> **Minimum files:** ⌈7 × 0.42⌉ = 3
> **Files verified:** 7/7 (100%, required by the repeat-review delegation)

## Verification Log

### V1: `AGENTS.md`
- **RF claim:** Complete count-free canonical contract, both future project-operation declarations,
  no live singular-adapter map row, and a byte-identical generated Codex region.
- **Actual:** Every required contract heading is present; `/kz-stats` and `/kz-release` each occur
  once; no literal catalog total or live `.agent/` map row exists. The managed range occurs once,
  is 1515 UTF-8 bytes, and has SHA-256
  `3ec08aeaf1c6fd98dfe8c3d832ce521cc6ed6aaa5ba292686c8a7023850ebf46`.
- **Match:** ✅. The protected text's `README.md` Task Board locus still contradicts project D7,
  but it is unchanged inherited adapter debt (TD-10), not a Phase B revision target.

### V2: `CLAUDE.md`
- **RF claim:** Thin Claude Code adapter with no duplicated project contract.
- **Actual:** The only level-two sections are Context Loading, Slash-Command Routing, and Execution
  Mode. The route table names 12 adapters and 11 canonical workflow files; all 23 filesystem
  targets resolve, and the `AGENTS.md` canonical pointer is the twenty-fourth named local target.
  The live research route is `research/base.md`, not the nonexistent legacy target.
- **Match:** ✅. The dormant source-template defect remains TD-11 outside Phase B.

### V3: `data/communities.json`
- **RF claim:** Only exact approved `north_star` data was added; all prior catalog semantics remain;
  no `archive` exists.
- **Actual:** Parsed comparison against the implementation parent finds one added top-level key,
  `north_star`, and no removed key. Purpose and all four non-goals match the frozen TS strings in
  exact order. `archive` is absent. `meta`, `groups`, `channels`, `bots`, and `categories` compare
  equal and reproduce ONB hashes `5af830…5e3`, `768d97…033`, `f6b1f7…8aa`, `49eb5d…9c6`, and
  `093ce9…644` respectively.
- **Match:** ✅.

### V4: `CONTRIBUTING.md`
- **RF claim:** The revision removed the copied validation sequence and left a pure pointer to the
  canonical procedure while preserving the approved contributor policy.
- **Actual:** The canonical `AGENTS.md#change-procedure` pointer and target heading both resolve.
  Literal occurrences of `scripts/validate_schema.py`, `scripts/validate_links.py`, and
  `scripts/generate_readme.py` are all zero. No copied category/required-field table remains;
  `master`, all four non-goals, evidence rules, and archive-not-delete owner triage remain.
- **Match:** ✅. Prior P2 finding resolved by `958ceb5`.

### V5: `RELEASE.md`
- **RF claim:** Complete future-facing dated-snapshot policy, no project semver, correct tag form,
  framework-version distinction, triggers/checklist, and owner gate before tag/push.
- **Actual:** Sections 1–7 contain every required policy and authority boundary. The local
  changelog citation resolves; the file records no completed release or snapshot.
- **Match:** ✅.

### V6: `CHANGELOG.md`
- **RF claim:** Root Keep-a-Changelog catalog history with concrete `[Unreleased]` Phase B entries
  and no completed snapshot.
- **Actual:** Added/Changed entries describe delivered Phase B contract work, framework history is
  separated, and the final paragraph explicitly says no dated snapshot exists.
- **Match:** ✅.

### V7: `KNOWLEDGE.md`
- **RF claim:** D8–D12 occur once, D13–D15 are absent, and D1–D7 plus two Phase A rows are preserved.
- **Actual:** Counts are D8–D12 = 1 each and D13–D15 = 0. Explicit UTF-8/LF keyed-row replay yields
  D1–D7 SHA-256 `0bb77bc1cf5bd99d40c2bc83d386ecb362586b13a987561893705b6224b0ce16`
  and Phase A SHA-256 `a1c5ec73882091dca5f3c9d8eafe47ba3e3f9386141bb23534dfe6307cc33ccb`,
  both equal to ONB. D8–D12 preserve the Master baseline meanings and their source links resolve.
- **Match:** ✅.

### V8: P3 protected-manifest replay
- **RF claim:** The retained ordered manifest makes the ONB aggregate and every protected file
  independently replayable with only reviewer-owned TD-10/TD-11 projected out.
- **Actual:** `protected_manifest.tsv` has 115 unique, single-tab rows matching
  `<normalized-path><TAB><lowercase-sha256>`. Reapplying the stated `git ls-files` source,
  normalization, PowerShell `Sort-Object -Unique`, and every listed inclusion predicate produces
  the same 115 paths in the same order: zero missing and zero extra. The artifact is UTF-8 without
  BOM and LF-only, with a conventional final LF; the documented aggregate input reserializes its
  115 rows with LF and no final LF and hashes to
  `14802fad376f4c906278b115820b2b57ef0afb361cc507559c1eba5108fa4864`.
- **Match:** ✅. Replay compares 114 files as raw bytes and projects only `TECH_DEBT.md` by removing
  exactly two complete rows, TD-10 and TD-11, in memory. Result: 0 mismatches. Prior P3 finding
  resolved by `158f432`.

### V9: commits, path scopes, attribution, and dates
- **RF claim:** Original and revision work remained path-scoped and truthfully attributed.
- **Actual:** Exact commit path counts are `ea4a694` = 1 (ONB), `836c099` = 7 (the approved
  implementation set), `ce01b17` = 2 (original EV/RF), `958ceb5` = 1 (`CONTRIBUTING.md`), and
  `158f432` = 3 (revised EV/RF plus manifest). Every subject begins
  `[codex/TFW-4/contract-docs/executor]`; author and committer timestamps are equal, monotonic from
  2026-08-26 23:23 through 2026-08-27 00:18 at `+05:00`, and the subjects claim no Phase C/D work.
  The current seven implementation paths have no worktree diff.
- **Match:** ✅.

### V10: frozen/protected state, tags, and action boundary
- **RF claim:** Master contract, generated README, protected dirty state, and empty tag set remain;
  no release/network/push action occurred.
- **Actual:** Current Master HL blob equals baseline `d31e60d`; current README blob equals the same
  baseline and SHA-256 `cc730c6b5a442174b2821a0d891fbaf723a11c7a4356e809942e8856b64894f9`.
  Manifest replay establishes protected bytes; unrelated Task Board/research/reviewer dirty traces
  remain outside executor commit scopes. `git tag --list` and `refs/tags` are empty. No release
  state or catalog/live mutation is present.
- **Match:** ✅ for reproducible repository state. A historical claim that no arbitrary network or
  push command ran is not reconstructible from Git; this repeat review used neither and found no
  resulting local tag, release, catalog, or remote-tracking artifact.

### V11: documents, links, citations, and offline verification
- **RF claim:** Documents are complete, local links resolve, schema passes, and README is
  generator-current.
- **Actual:** Required AGENTS headings all exist; the six Markdown implementation paths contain no
  `TODO`, `origin main`, `implement later`, or literal derived catalog totals. A local resolver
  checked 100 links/citations across 18 relevant implementation, board, contract, RF/EV, and
  review files plus five anchors: zero missing. Three external HTTP links were intentionally not
  fetched because the TS/review boundary prohibits network and no verdict fact depends on their
  remote content. In an isolated temporary copy, schema and generator both exited 0; README hashes
  before/after/current were all `cc730c…94f9`. The temporary copy was removed.
- **Match:** ✅.

## Commands Executed

| # | Command / check | Result |
|---|-----------------|--------|
| 1 | Managed-block UTF-8 byte extraction and SHA-256 | PASS — one marker pair, 1515 bytes, `3ec08a…bf46` |
| 2 | Parsed JSON parent/current comparison with explicit UTF-8 decoding | PASS — only exact ordered `north_star`; all prior values equal; no `archive` |
| 3 | `python -B scripts/validate_schema.py` in an isolated copy | PASS — exit 0, errors 0 |
| 4 | `python -B scripts/generate_readme.py` in the same isolated copy | PASS — exit 0; README unchanged at `cc730c…94f9` |
| 5 | Predicate reconstruction, manifest format/order/encoding audit, aggregate hash, and byte replay | PASS — 115/115 paths, `14802f…864`, two projected debt rows, 0 mismatches |
| 6 | Local Markdown path/anchor resolver | PASS — 100 local links, five anchors, zero missing |
| 7 | `git diff-tree`, `git show`, `git diff`, blob/hash, status, and tag checks | PASS — exact 1/7/2/1/3 scopes, clean implementation paths, truthful metadata, tags 0 |
| 8 | UTF-8 keyed decision-row hashing and D-number audit | PASS — protected hashes equal, D8–D12 once, D13–D15 absent |

A preliminary literal-array comparison used Windows PowerShell's implicit text decoding and
reported false North Star/row-hash results. The focused rerun used explicit UTF-8 decoding and
exact indexed strings, producing the results above; no repository file changed.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Frozen authority is `d31e60d` and D8–D12 retain their accepted meanings | Phase HL, TS, RF AC-4 | Subject-recovered baseline, current identical Master blob, and keyed `KNOWLEDGE.md` rows | ✅ |
| C2 | P2 is a pure canonical procedure pointer with zero copied validation/generation commands | RF AC-3 / EV E3 | Current `CONTRIBUTING.md`, resolved `AGENTS.md#change-procedure`, and literal command scan | ✅ |
| C3 | P3 replay is deterministic and excludes only reviewer-owned TD-10/TD-11 | RF AC-5 / EV E5 | 115-row manifest, reconstructed predicate set, exact serialization, raw-byte replay, and two-row in-memory projection | ✅ |
| C4 | Project North Star is exact and semantic-only | RF AC-2 / EV E2 | Approved TS strings, implementation parent JSON, and current parsed JSON | ✅ |
| C5 | TD-10/TD-11 identify real but out-of-scope adapter defects | RF §6 | Managed Codex source/installed skills, D7, Claude template, and existing/missing workflow targets | ✅ |

## Discrepancies Found

No in-scope discrepancies. The first review's P2 contributor and P3 evidence-reproducibility
findings are resolved.

Remaining non-blocking debt is unchanged:

1. TD-10 — the protected Codex block/source says `README.md` Task Board while D7 designates
   `tasks/README.md`; correct through adapter/config synchronization, not this review.
2. TD-11 — the Claude source template points to nonexistent `.tfw/workflows/research.md`; correct
   through framework adapter maintenance and synchronization, not Phase B.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV AC-1 inline log + ONB block snapshot | ✅ | ✅ — document roles, paths, and managed bytes reproduce; TD-10 remains disclosed debt |
| E2 | EV AC-2 inline log | ✅ | ✅ — exact semantic comparison plus independent offline schema/generator gate |
| E3 | EV AC-3 inline log | ✅ | ✅ — P2 pointer, command absence, policy completeness, links, and tags reproduce |
| E4 | EV AC-4 inline log | ✅ | ✅ — decision counts, protected hashes, meanings, and source links reproduce |
| E5 | EV AC-5 inline log + manifest + five commits | ✅ | ✅ — path scopes, predicate set, serialization, aggregate, projection, hashes, dates, and tags reproduce |

External/live evidence is correctly N/A for all five ACs. The TS requires deterministic local
verification instead, and that evidence is sufficient.

## Knowledge Citations Verified

| # | Artifact | Citation set | Link resolves? | Item exists? |
|---|----------|--------------|----------------|--------------|
| 1 | Master HL §7.2 at `d31e60d` | PV references 1–20 | ✅ 20/20 | ✅ 20/20 |
| 2 | ONB §7 | Master-HL citation confirmations 1–20 | ✅ 20/20 | ✅ 20/20 |
| 3 | Phase B implementation, traces, and Task Board | Relevant local Markdown links and anchors | ✅ 100/100 | ✅ 100/100 |

No hallucinated internal citation was found. External links were not fetched under the explicit
zero-network boundary.

## Checkpoint

**Self-check:**
- [x] Opened at least ⌈7 × 0.42⌉ files and recorded findings? — 7/7 opened
- [x] Ran at least one build/test command? — schema and generator ran offline in isolation
- [x] Claim & Source Checks filled; key claims and every internal citation traced?
- [x] Each RF §3 acceptance-criterion checkmark verified against actual files?
- [x] `KNOWLEDGE.md` checked and contradictions classified?
- [x] Knowledge Citations from Master HL §7.2 and ONB §7 verified?
  - Total citation rows: 40, verified: 40, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 5, verified: 5, missing: 0

Stage complete: YES

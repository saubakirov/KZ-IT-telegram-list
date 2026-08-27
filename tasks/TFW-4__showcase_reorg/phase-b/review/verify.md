# Verify — TFW-4 / Phase B: Contract & Docs
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Min verify ratio:** 0.42
> **RF implementation files claimed:** 7
> **Minimum files:** ⌈7 × 0.42⌉ = 3
> **Files verified:** 7/7 (100%, required by the review delegation)

## Verification Log

### V1: `AGENTS.md`
- **RF claim:** Complete count-free canonical contract, future project-operation declarations,
  no live singular-adapter row, and a byte-identical generated Codex region.
- **Actual:** All required contract sections and both `/kz-*` declarations are present; no
  literal catalog totals or live `.agent/` map row remain. The managed range occurs once, is
  1515 bytes, and has SHA-256
  `3ec08aeaf1c6fd98dfe8c3d832ce521cc6ed6aaa5ba292686c8a7023850ebf46`, equal to ONB and
  commit `836c099`.
- **Match:** ⚠️ Partial. The byte-preservation claim is true, but the protected block itself says
  `README.md` is the Task Board at line 195, contradicting project D7 and the canonical contract's
  `tasks/README.md` locus. This is inherited generated-adapter debt, not an executor edit.

### V2: `CLAUDE.md`
- **RF claim:** Thin Claude Code adapter only; canonical pointer, context loading, routing, and
  mode surface with no copied project contract.
- **Actual:** Its only level-two sections are Context Loading, Slash-Command Routing, and
  Execution Mode. All 12 adapter paths and their 11 canonical workflow paths resolve; the live
  `/tfw-research` row correctly names `.tfw/workflows/research/base.md`.
- **Match:** ✅

### V3: `data/communities.json`
- **RF claim:** Add exactly the frozen `north_star`, preserve all prior semantics, introduce no
  `archive`, and leave generated README currency intact.
- **Actual:** Parsed parent/current comparison shows one added top-level key (`north_star`), no
  removed keys, exact purpose and four ordered non-goals, no `archive`, and equality for `meta`,
  `groups`, `channels`, `bots`, and `categories`. The five ONB semantic hashes reproduce using
  the executor's PowerShell compact-JSON representation.
- **Match:** ✅

### V4: `CONTRIBUTING.md`
- **RF claim:** Canonical pointers, all four non-goals, `master`, no copied mutable tables or
  placeholders, and evidence-backed archive-not-delete policy.
- **Actual:** Those listed document checks pass; seven local links and all three local anchors
  resolve. However lines 40–43 claim to follow the sequence in `AGENTS.md` and then copy it with
  `python scripts/validate_links.py`, while `AGENTS.md` lines 75 and 84 require
  `python scripts/validate_links.py --update`.
- **Match:** ⚠️ Partial. The contributor workflow is a second, divergent copy of the canonical
  change procedure and does not fully satisfy the Phase HL canonical-pointer outcome or P3.

### V5: `RELEASE.md`
- **RF claim:** Complete future-facing dated-snapshot policy, no semver, correct tag form,
  `.tfw/VERSION` distinction, triggers/checklist, and explicit owner gate before tag/push.
- **Actual:** Sections 1–7 contain every named policy and authority gate. Its local changelog link
  resolves. It does not claim a completed release.
- **Match:** ✅

### V6: `CHANGELOG.md`
- **RF claim:** Root Keep-a-Changelog catalog history with a concrete `[Unreleased]` Phase B
  entry and no completed snapshot.
- **Actual:** `[Unreleased]`, Added, and Changed sections record the delivered contract work; the
  file distinguishes `.tfw/CHANGELOG.md` and explicitly says no dated snapshot exists.
- **Match:** ✅

### V7: `KNOWLEDGE.md`
- **RF claim:** D8–D12 exactly once, D13–D15 absent, and D1–D7 plus two Phase A rows preserved.
- **Actual:** Counts are D8–D12 = 1 each and D13–D15 = 0. UTF-8 keyed-row hashes reproduce ONB:
  D1–D7 `0bb77bc1cf5bd99d40c2bc83d386ecb362586b13a987561893705b6224b0ce16`;
  Phase A rows `a1c5ec73882091dca5f3c9d8eafe47ba3e3f9386141bb23534dfe6307cc33ccb`.
  Every new source link resolves to the Master HL or accepted Phase A RF.
- **Match:** ✅

### V8: commit and repository-state claims
- **RF claim:** `ea4a694` ONB-only; `836c099` exactly seven implementation paths;
  `ce01b17` EV/RF-only; truthful Codex attribution/current dates; zero tags; protected dirty work
  preserved; no network/release/push action.
- **Actual:** Path sets are exactly 1/7/2 and parent chain is
  `d31e60d → ea4a694 → 836c099 → ce01b17`. All subjects use
  `[codex/TFW-4/contract-docs/executor]`; author and committer timestamps are equal, monotonic,
  and dated 2026-08-26. All seven current files are byte-equal to their `836c099` blobs and have
  no worktree diff. Tags = 0. The unrelated tracked/untracked dirty categories named by ONB remain.
- **Match:** ✅ for reproducible repository state. A historical assertion that no network or push
  command ran cannot be replayed from Git, and no local `origin/master` ref exists; review did not
  access the network. No resulting tag, release state, catalog mutation, or remote-tracking update
  is present.

### V9: ONB / EV / RF evidence trace
- **RF claim:** EV records deterministic per-AC gates and a 115-file protected manifest equal to
  ONB.
- **Actual:** ONB, EV, and RF exist in the declared commits; EV covers all five ACs and its N/A
  statuses match the TS's external-evidence fields. The managed-block, JSON, README, knowledge,
  link, path-set, date, and tag claims were independently reproduced. The 115-file manifest's
  contents, exclusions, ordering, and serialization were not retained, so its aggregate hash
  cannot itself be independently recomputed; Git path sets and the surviving dirty state provide
  an independent scope audit but not a byte-for-byte baseline for untracked files.
- **Match:** ⚠️ Partial evidence reproducibility; the implementation scope outcome is otherwise
  corroborated.

## Commands Executed

| # | Command / check | Result |
|---|-----------------|--------|
| 1 | SHA-256 and byte extraction for `TFW:CODEX` range | PASS — 1515 bytes, ONB/commit hash equal |
| 2 | Parsed JSON parent/current semantic comparison | PASS — only exact `north_star` added |
| 3 | `python -B scripts/validate_schema.py` in an isolated temp copy | PASS — exit 0, zero errors |
| 4 | `python -B scripts/generate_readme.py` in an isolated temp copy | PASS — exit 0; before/after/current README SHA-256 `cc730c…94f9` |
| 5 | Local Markdown link and heading-anchor resolver | PASS — implementation 33/33; Phase B artifacts resolve; three apparent Master HL misses are illustrative links inside code fences |
| 6 | Named adapter/workflow path resolver | PASS — 24 routing/adapter targets represented; all distinct filesystem targets resolve |
| 7 | `git diff-tree`, `git show`, `git hash-object`, `git diff` for three commits and seven paths | PASS — exact 1/7/2 sets, byte-equal implementation, truthful subjects/dates |
| 8 | UTF-8 keyed-row hash and D-number audit | PASS — D1–D7 and Phase A hashes equal; D8–D12 present; D13–D15 absent |
| 9 | `git tag --list`, repository/status inspection | PASS — zero tags; no implementation path dirty; unrelated dirty state remains separate |

Two earlier attempts to isolate the schema/generator run were rejected or misdirected by local
PowerShell/safety behavior. The misdirected run executed the same offline scripts in the checkout,
but `README.md` remained byte-identical and clean; the final isolated run then passed. No network
validator was run.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Frozen Master authority is baseline `d31e60d` | Phase HL, TS, ONB | Subject-recovered freeze commit and unchanged Master HL blob | ✅ |
| C2 | Only exact `north_star` data changed | RF AC-2 / EV E2 | Parent/current parsed JSON objects and frozen TS strings | ✅ |
| C3 | D8–D12 preserve Master HL decisions and accepted Phase A knowledge | RF AC-4 / EV E4 | Master HL §3.3, Phase A RF/REVIEW, keyed KNOWLEDGE rows | ✅ |
| C4 | Canonical routes and document citations resolve | RF verification / EV AC-1, AC-3, AC-4 | 33 implementation local links, 24 routing targets, all Phase B trace links | ✅ |
| C5 | Two RF observations identify real source defects | RF §6 | Codex source/installed adapter text and Claude/Antigravity adapter templates | ✅ |

## Discrepancies Found

1. **P2 — in-scope contributor procedure divergence.** `CONTRIBUTING.md:40–43` copies the
   canonical validation sequence but omits `--update`, disagreeing with `AGENTS.md:75,84` and
   undermining Phase HL deliverable 3 plus Master HL P3. This is executor-revisable inside the
   approved seven-path scope.
2. **P2 — inherited Codex Task Board locus conflict.** `AGENTS.md:195` and the owning Codex
   adapter source/skills say `README.md`, while D7 designates `tasks/README.md`. The TS required
   exact preservation, so this is adapter/config debt and not an executor revision target.
3. **P2 — dormant Claude adapter research route.** The live `CLAUDE.md` is correct, but
   `.tfw/adapters/claude-code/CLAUDE.md.template:31` names nonexistent
   `.tfw/workflows/research.md`; related adapter READMEs repeat it. This is framework debt outside
   Phase B implementation.
4. **P3 — protected-manifest evidence is not self-reproducing.** ONB/EV retain only an aggregate
   hash and file count, not the manifest definition or contents. The seven committed paths are
   independently auditable; byte preservation of every untracked protected file is not.

Any discrepancy triggered the required 100% escalation; all seven implementation paths were
opened, diffed, and independently checked.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|------------------|----------------|
| E1 | EV AC-1 inline gate log + ONB block snapshot | ✅ | ✅ with inherited-locus debt — byte/hash and document-role checks reproduce |
| E2 | EV AC-2 inline gate log | ✅ | ✅ — exact semantic comparison, validator, and generator-currency gates reproduce |
| E3 | EV AC-3 inline gate log | ✅ | ⚠️ Partial — release/tag claims hold; contributor sequence diverges from canonical command |
| E4 | EV AC-4 inline gate log | ✅ | ✅ — knowledge counts, hashes, and source links reproduce |
| E5 | EV AC-5 inline gate log + Git commits | ✅ | ⚠️ Partial — commit/tag/path state reproduces; untracked protected-manifest hash is not self-recomputable |

External/live evidence is correctly N/A for all five ACs. Deterministic verification remains
mandatory and is audited above.

## Knowledge Citations Verified

| # | Artifact | Citation set | Link resolves? | Item exists? |
|---|----------|--------------|----------------|--------------|
| 1 | Master HL §7.2 | PV references 1–20 | ✅ 20/20 (row 1 is the explicit pre-Phase-B N/A North Star state) | ✅ 20/20 |
| 2 | ONB §7 | HL citation confirmations 1–20 | ✅ 20/20 map to Master HL rows | ✅ 20/20 |
| 3 | Phase B implementation and traces | 44 local links outside illustrative code fences | ✅ 44/44 | ✅ 44/44 |

No hallucinated internal citation was found. The external Keep a Changelog URL was not fetched
because the approved phase and review delegation prohibit network access; no verdict claim rests
on remote content.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈7 × 0.42⌉ files and recorded findings? — 7/7 opened
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled; key claims and all internal citations traced?
- [x] Each RF §3 acceptance-criterion checkmark verified against actual files?
- [x] KNOWLEDGE.md checked; preservation and D8–D12 verified?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total citation rows: 40, verified: 40, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 5, fully matched: 3, partially matched: 2, missing: 0

Stage complete: YES

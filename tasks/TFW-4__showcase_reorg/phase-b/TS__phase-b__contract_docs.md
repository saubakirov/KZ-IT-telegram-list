# TS — TFW-4 / Phase B: Contract & Docs

> **Date**: 2026-08-26
> **Author**: Coordinator (Codex)
> **Status**: ✅ APPROVED — owner pre-authorization for Phases B–C, 2026-08-26
> **Approval Boundary**: Valid because this TS is strictly derived from frozen Master HL
> baseline `d31e60d` after the Phase A RF/REVIEW Pre-TS Gate. It does not authorize Phase D,
> live sweep, release, tag, or push.
> **Parent Phase HL**: [Phase B HL](HL__phase-b__contract_docs.md)
> **Parent Master HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Mode**: AG — local filesystem and git only; no network, release, tag, or push

---

## 1. Objective

Deliver the documentation and data contract for the remaining TFW-4 work: one canonical,
count-free agent contract; one thin Claude Code adapter; a structured Project North Star;
truthful contributor and release policies; a catalog changelog; and indexed decisions D8–D12.
The result must preserve the completed Phase A trace and the live Codex adapter while providing
a bounded, reviewable input for Phase C.

## 2. Scope

### In Scope

- Make `AGENTS.md` the canonical project contract with the role/mission, generation contract,
  repository map, working process, change procedure, data and inclusion rules, TFW roles,
  human/AI split, execution modes, quality standards, and `/kz-stats` / `/kz-release` entries.
- Preserve the current generated `TFW:CODEX:START` / `TFW:CODEX:END` region in `AGENTS.md`
  byte-for-byte while editing only the surrounding human-owned contract.
- Reduce `CLAUDE.md` to Claude-Code-specific adapter content: canonical pointer, context-loading
  order, slash-command routing, execution-mode default, and an explicit no-duplication warning.
- Add only the approved top-level `north_star` block to `data/communities.json`.
- Correct and de-duplicate `CONTRIBUTING.md`, including the `master` branch, North Star inclusion
  gate, canonical-source pointers, and archive-not-delete policy.
- Create project-root `RELEASE.md` and `CHANGELOG.md` with the frozen dated-snapshot semantics.
- Append decisions D8–D12 to `KNOWLEDGE.md` without losing D1–D7 or the Phase A documentation
  already present in the dirty working copy.
- Produce Phase B ONB, structured EV, and RF traces through `/tfw-handoff`.

### Out of Scope

- Any modification to the Master HL, Phase A/research traces, `.agents/**`, `.tfw/**`,
  `.claude/commands/**`, `scripts/**`, `README.md`, `TECH_DEBT.md`, GitHub workflows, or legacy
  TFW-01/TFW-02 folders.
- Schema enforcement or README rendering of `north_star`; the `archive` array; validator,
  generator, or classifier changes; project command files; CI. These are Phase C outcomes.
- Adding, removing, re-vetting, dating, recounting, archiving, or otherwise changing any Telegram
  community, catalog metadata, category, handle, description, or count.
- Telegram or other network access, the live sweep, archive triage, changelog release finalization,
  release execution, tag creation, or push. These remain Phase D/owner-authorized actions.
- Any claim that a dated snapshot, release, tag, or push has already occurred.

## 3. Principles Check

| # | Principle (from Master HL §7) | Enforced by | Gate |
|---|--------------------------------|-------------|------|
| P1 | The trace before the improvement | AC-5 | Baseline `d31e60d` and the approved Phase A RF/REVIEW remain intact; Phase B touches only its seven implementation paths plus lifecycle traces |
| P2 | Honest history over tidy history | AC-3, AC-5 | Release/changelog text records policy and `[Unreleased]`, never a fictitious snapshot; commits use the actual product identifier from A6 |
| P3 | One copy of every rule | AC-1 | `AGENTS.md` owns project rules; `CLAUDE.md` contains adapter-only context and no repeated generation/data/change contract |
| P4 | Derived facts are never written by hand | AC-1, AC-2, AC-3 | Agent/contributor docs contain no catalog counts or category copy; the North Star is data-borne; README remains generated and unchanged |
| P5 | Non-goals are load-bearing | AC-2, AC-3 | All four approved non-goals are stored in JSON and applied as the contributor inclusion gate |
| P6 | The network is the only authority on liveness | AC-5 | Phase B performs no network check and writes no liveness, count, or verification-date fact |
| P7 | Absence of evidence is not death | AC-3, AC-5 | Contributor policy requires evidence and archive-not-delete; no catalog entry moves in this phase |
| P8 | The tool serves the operation | AC-1, AC-3 | Canonical docs name the future project commands and release contract without pretending Phase C tooling or Phase D execution already exists |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `AGENTS.md` | MODIFY | Canonical, count-free project contract around an unchanged generated Codex region |
| `CLAUDE.md` | MODIFY | Thin Claude Code adapter pointing to `AGENTS.md` |
| `data/communities.json` | MODIFY | Add only the approved `north_star` block |
| `CONTRIBUTING.md` | MODIFY | Canonical pointers, non-goals, corrected branch, and archive policy |
| `RELEASE.md` | CREATE | Dated verified snapshot strategy and gates |
| `CHANGELOG.md` | CREATE | Separate Keep-a-Changelog catalog history |
| `KNOWLEDGE.md` | MODIFY | Add D8–D12 while preserving current content |

**Budget:** 2 new implementation files, 5 modifications, 7 implementation paths, estimated
delta below 1500 LOC. With Phase HL, TS, ONB, RF, EV, three review-stage files, and REVIEW, the
phase has at most 11 new files and 16 total paths. Limits: 30 files, 15 new files, 3000 LOC,
30 modified files. No override is authorized or required.

## 5. Acceptance Criteria

### AC-1: Establish one canonical agent contract

`AGENTS.md` contains the full project contract without hardcoded catalog statistics, while
`CLAUDE.md` contains only the Claude Code adapter surface. The generated Codex region in
`AGENTS.md` survives byte-for-byte.

- [ ] `AGENTS.md` covers every Phase B deliverable named in Master HL §4 Phase B item 1 and
  contains `/kz-stats` and `/kz-release` entries, while derived counts are described only by
  their source in `data/communities.json`.
- [ ] The repository map no longer presents `.agent/` as a live project path.
- [ ] The exact bytes between and including `<!-- TFW:CODEX:START -->` and
  `<!-- TFW:CODEX:END -->` match the executor's ONB snapshot.
- [ ] `CLAUDE.md` names `AGENTS.md` as canonical, states that duplicating its project rules is a
  defect, and contains only Claude-Code-specific context loading, adapter routing, and mode data.
- [ ] `CLAUDE.md` contains no generation contract, change procedure, JSON field rules, inclusion
  criteria, repository map, or other semantic rule already owned by `AGENTS.md`.

Gate: Inspect both document structures and their semantic overlap; scan for literal derived
catalog/count/category facts; compare the managed Codex-region hash and bytes with ONB; verify all
local links and named workflow/adapter paths resolve without modifying them.

Evidence: N/A — the outcome is deterministic local document content and byte comparison; record
the checks and managed-region hash in the mandatory EV file.

### AC-2: Store the approved Project North Star without catalog drift

`data/communities.json` gains exactly one top-level `north_star` object with the frozen purpose
and four frozen non-goals below; every pre-existing value remains semantically unchanged.

Purpose:

> A catalog whose value is accuracy. Every entry is a live, verified, IT-relevant Kazakhstan
> Telegram community — verified by a dated network check, never by recollection.

Non-goals:

1. A directory of every Kazakhstan Telegram chat — IT relevance is a gate, not a hint.
2. A promotion channel — no purely commercial or paid-placement entries.
3. A hand-edited list — `README.md` is an artifact; the data is the product.
4. An estimator — an unverifiable member count is omitted, never guessed.

- [ ] `north_star.purpose` equals the approved purpose and is non-empty.
- [ ] `north_star.non_goals` contains the four approved strings in the approved order and no
  additional claim.
- [ ] `meta`, `groups`, `channels`, `bots`, and `categories` are semantically identical to the
  pre-execution state; no `archive` array is introduced in Phase B.
- [ ] The current schema validator still exits zero, and a generator run leaves `README.md`
  byte-identical and without a working-tree diff.

Gate: Parse and compare the JSON against the frozen strings; compute a semantic before/after
comparison with `north_star` excluded; run `python scripts/validate_schema.py`; run
`python scripts/generate_readme.py` and verify the pre-run and post-run `README.md` hash is equal.

Evidence: N/A — Phase B adds local contract data but does not yet render it in a live/public
environment; record the parsed comparison, validator output, and README hash in the EV file.

### AC-3: Publish truthful contributor and release policies

The contributor guide and new release artifacts express the frozen policies without duplicated
mutable data, placeholders, or a false claim that Phase D occurred.

- [ ] `CONTRIBUTING.md` uses `master`, contains no copied categories table, no copied required-field
  or validation-script reference table, no `TODO`/stub, and points to `AGENTS.md` and
  `data/communities.json` as the canonical sources.
- [ ] `CONTRIBUTING.md` applies all four North Star non-goals as an inclusion gate and states that
  a community is archived only on evidence and owner triage, never silently deleted.
- [ ] `RELEASE.md` defines a release as a dated verified catalog snapshot, explicitly rejects
  project semver, uses `data-YYYY-MM-DD`, distinguishes `.tfw/VERSION`, states triggers and a
  complete pre-release checklist, and preserves explicit owner approval before tag/push.
- [ ] Root `CHANGELOG.md` follows Keep a Changelog, contains a concrete `[Unreleased]` entry for
  Phase B's North Star/documentation contract, and distinguishes catalog history from
  `.tfw/CHANGELOG.md` without recording a completed snapshot.
- [ ] All referenced local files exist; no release, tag, push, or network action is performed.

Gate: Inspect headings and required claims; scan for `TODO`, placeholders, `origin main`, copied
category rows, and false completed-release language; resolve local links; inspect `git tag` and
the local action log to confirm Phase B did not create release state.

Evidence: N/A — these are versioned local policies, not a release execution; record document/link
checks and the no-new-tag observation in the EV file.

### AC-4: Index decisions D8–D12 without losing accepted knowledge

`KNOWLEDGE.md` gains the five Master HL decisions and preserves its existing architecture,
Phase A key-artifact row, Phase A legacy row, and D1–D7 content.

- [ ] D8 records the honest, non-backdated TFW-3 trace decision already delivered by Phase A.
- [ ] D9 records `AGENTS.md` canonical plus a thin `CLAUDE.md` adapter.
- [ ] D10 records dated verified snapshots and `data-YYYY-MM-DD`, not semver.
- [ ] D11 records `north_star` data rendered later as `README.md § Purpose`.
- [ ] D12 records archive-not-delete with `died_on` and `reason`.
- [ ] D1–D7 and the current TFW-4 Phase A additions in §§2–3 remain present and unchanged in
  meaning; no D13–D15 claim is added early.

Gate: Compare keyed Architecture Decision rows and the protected Phase A rows against the ONB
snapshot; resolve every new source link to the Master HL or accepted Phase A trace.

Evidence: N/A — the result is deterministic project knowledge text; record the keyed comparison
and link-resolution result in the EV file.

### AC-5: Keep Phase B bounded, truthful, and ready for Phase C  [depends: AC-1, AC-2, AC-3, AC-4]

The completed change set contains only the seven implementation paths in §4 plus mandatory
Phase B lifecycle traces, preserves every unrelated dirty path, and passes its offline checks.

- [ ] `.agents/**`, `.tfw/**`, `.claude/commands/**`, `scripts/**`, `README.md`, `TECH_DEBT.md`,
  Master/Phase A/research traces, and legacy task folders match their ONB state, excluding only
  Coordinator/Executor lifecycle-status edits explicitly owned by the current workflow.
- [ ] No community data, catalog metadata, category data, generated README content, schema/tooling,
  CI, live evidence, release, tag, or push change appears in the implementation diff.
- [ ] `python scripts/validate_schema.py` exits zero; `python scripts/generate_readme.py` leaves
  `README.md` unchanged; local document links and JSON parsing pass.
- [ ] Executor commits in the current Codex context use
  `[codex/TFW-4/contract-docs/executor]`; if execution instead occurs in Claude Code, they use
  `[claude-code/TFW-4/contract-docs/executor]`. Metadata is current and truthful, and the subject
  makes no claim of Phase C/D work.
- [ ] No network request, live sweep, release command, tag, push, or whole-tree restore occurs.

Gate: Compare the final path set and protected-path hashes with ONB; inspect the implementation
diff, validation/link outputs, local commit subjects/dates, tag set, and repository status. Do not
obtain a narrow diff by resetting or restoring unrelated user work.

Evidence: N/A — the phase is deliberately local and pre-operational; record deterministic gates,
protected hashes, commit metadata, and the no-new-tag observation in the EV file.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-b__contract_docs.md` | Structured environment header, per-AC gate results, protected dirty-state hashes, and evidence verdict (required) |

All five ACs use `N/A` for external/live evidence because Phase B changes local documentation and
contract data only. The EV file remains mandatory and must contain the deterministic gate output;
`N/A` does not permit skipping verification.

## 6. Technical Guidance

- Frozen authority: Master HL baseline `d31e60d`; phase derivation:
  `HL__phase-b__contract_docs.md`; factual predecessor: Phase A RF and `✅ APPROVE` REVIEW.
- The current `AGENTS.md` generated Codex region is machine-managed adapter state. Read through it,
  preserve it exactly, and make the canonical project contract around it.
- `.tfw/adapters/claude-code/CLAUDE.md.template` is reference material, not a file to copy verbatim
  and not authorization to edit `.tfw/`. The frozen D9 result is intentionally thinner.
- `RELEASE.md` may use `.tfw/templates/RELEASE.md` as structural reference, but every placeholder
  must be replaced and the project-specific dated-snapshot semantics control.
- Root `CHANGELOG.md` is catalog history; `.tfw/CHANGELOG.md` is framework history and remains
  untouched. `[Unreleased]` is a state label, not a placeholder or a completed release claim.
- `data/communities.json` is the source of truth. Phase B adds the approved `north_star`; Phase C
  adds its enforcement/rendering and the archive structure. Do not pull Phase C forward.
- The existing `KNOWLEDGE.md` dirty hunks are accepted Phase A documentation. Work from the current
  file and preserve those rows instead of reconstructing from `HEAD` or the freeze commit.
- `tasks/README.md`, research, Phase A traces, and `.agents/**` contain unrelated workflow/user
  state. Preserve them; do not stage all dirty files or use a whole-tree restore.

### Inherited Quality Contract (verbatim from Master HL §7.1 at `d31e60d`)

- No placeholders. No `TODO`, no stub, no "implement later". `.tfw/README.md` § Completeness
  Over Speed.
- No hardcoded derived value in any file — counts, dates, category lists.
- `README.md` is never hand-edited. Change the generator or the data.
- No file under `.tfw/` is touched except `project_config.yaml` and `knowledge_state.yaml`.
- No `/tfw-*` adapter file in `.claude/commands/` is modified.
- Every commit follows `conventions.md` §4: `[agent/task/scope/role] summary`, with
  `agent` = the lowercase AI product name established by the actual executing product/adapter
  context (`codex` for Codex executor commits; `claude-code` for Claude Code executor commits),
  `task` = the task ID, and `role` = the acting TFW role.
- `git push` only on explicit owner approval given at that moment.
- Python: standard library only. The project's sole declared dependency is `requests`
  (`project_config.yaml` → `stack.dependencies`), and no current script uses it — do not add
  one. Type hints and docstrings in the existing style; ASCII-tagged output (`[OK]`, `[FAIL]`,
  `[INFO]`) to stay readable in a Windows console.
- Scripts exit non-zero on error, zero on success. `/kz-release` and CI depend on it.

## 7. Definition of Failure

- ❌ The generated `TFW:CODEX` region or any file under `.agents/**` is changed, deleted, moved,
  or reconstructed rather than preserved from the ONB state.
- ❌ `AGENTS.md` and `CLAUDE.md` both state the same project rule, or `CLAUDE.md` retains the
  generation contract, change procedure, data rules, or inclusion criteria.
- ❌ A catalog count, category list, verification date, or other derived mutable fact is copied
  into documentation by hand.
- ❌ Any pre-existing `data/communities.json` value changes other than adding the exact approved
  `north_star`, or an `archive` structure appears early.
- ❌ `README.md`, a script, schema, validator, generator, project command, CI workflow, `.tfw/**`,
  or `.claude/commands/**` is modified.
- ❌ D1–D7, the Phase A knowledge rows, unrelated dirty work, or historical traces are lost,
  rewritten, staged by accident, or restored to an older tree.
- ❌ A placeholder, `TODO`, stub, `origin main`, copied mutable reference table, or false completed
  release/tag/snapshot claim remains in a Phase B deliverable.
- ❌ An AI-authored commit uses an agent token different from the actual executing product, is
  backdated, or claims Phase C/D work not performed.
- ❌ Any network request, community mutation, live sweep, archive triage, release, tag, or push
  action occurs.

Any failure must be corrected before RF. If the Codex managed region or `.agents/**` is affected,
restore it from the exact ONB snapshot, stop, and report; do not infer that an adapter-source copy
is byte-identical. Authorization does not extend to Phase D or release operations.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Canonicalization erases machine-managed or user-owned content | ONB byte/hash snapshots plus AC-1 and AC-5 protected comparisons |
| The thin adapter duplicates semantics under different wording | Review content by semantic role, not only identical strings |
| JSON formatting hides an unintended catalog change | Compare parsed pre/post objects with `north_star` excluded |
| Release policy is mistaken for release authorization | `[Unreleased]`, explicit future gates, and hard prohibition on tag/push/network actions |
| Phase B consumes Phase C work for convenience | Seven-path scope and explicit no-script/no-command/no-CI/no-README gates |
| Shared dirty files are broadly staged | Path-scoped staging and commit inspection; no `git add .` |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|------------------|-------------------|
| `AGENTS.md` | Phase C | Phase B establishes the canonical contract and command declarations; Phase C adds command files without rewriting the protected Codex region |
| `data/communities.json` | Phases C and D | Phase C adds enforcement/archive structure; Phase D alone changes live catalog facts after network evidence |
| `CHANGELOG.md` | Phase D | Phase B records `[Unreleased]` contract work; Phase D finalizes the verified snapshot only after the live sweep |
| `RELEASE.md` | Phase D | Phase B defines the gate; Phase D reads and executes it with separate owner approval |
| `KNOWLEDGE.md` | Phases C and D | Preserve D8–D12; later phases append D13–D15 rather than rewriting them |

---

*TS — TFW-4 / Phase B: Contract & Docs | 2026-08-26*

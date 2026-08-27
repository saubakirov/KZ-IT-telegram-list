# TS — TFW-4 / Phase C: Pipeline & Tooling

> **Date**: 2026-08-27
> **Author**: Coordinator (Codex)
> **Status**: ✅ APPROVED — derivation-only under owner pre-authorization, 2026-08-27
> **Approval Boundary**: Valid because this TS is strictly derived from frozen Master HL
> baseline `d31e60d` after the Phase B RF/repeat-REVIEW Pre-TS Gate. It authorizes only local,
> offline Phase C execution; it does not authorize Phase D, Telegram requests, browser use, a
> live sweep, release, tag, or push.
> **Parent Phase HL**: [Phase C HL](HL__phase-c__pipeline_tooling.md)
> **Parent Master HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Mode**: AG — local filesystem and git only; no network, browser, release, tag, or push

---

## 1. Objective

Deliver the offline-verifiable pipeline and project tooling promised by TFW-4 Phase C: enforce
the Phase B data contract, make Telegram classification evidence-safe, generate the complete
README presentation, define the two `kz-*` project operations, and add offline CI. The result
must make Phase D executable without performing any Phase D live-state or release action and
must preserve the frozen master contract, all live catalog facts, and out-of-phase adapter debt.

## 2. Scope

### In Scope

- Add an empty top-level `archive` array to `data/communities.json` while preserving all existing
  semantic values, including every live entry and the approved `north_star` text.
- Extend `scripts/validate_schema.py` to enforce the approved `north_star` and archive contracts,
  reject archive/live handle collisions, and report oldest/stale live verification dates without
  failing only because a valid date is old.
- Extend `scripts/validate_links.py` so target-specific preview evidence, ambiguous contact shells,
  generic pages, and explicit failures are distinct outcomes; counts are parsed only from target
  previews; verified dates are count-independent; updates maintain `meta.last_updated`; explicit
  approved archives preserve the record; and a machine-readable run summary exposes deltas and
  triage states.
- Extend `scripts/generate_readme.py` to render the approved Purpose, dynamic category/freshness
  statistics, display-name category ordering, current GitHub-compatible anchors, conditional
  collapsed Archive output, and a normalized non-mutating README currency check.
- Regenerate `README.md` exclusively by running `scripts/generate_readme.py`. Its Phase C diff is
  presentation-only and may not change any live entry fact.
- Create `.claude/commands/kz-stats.md` and `.claude/commands/kz-release.md` in the project-owned
  namespace, leaving every `/tfw-*` adapter untouched.
- Encode the approved future browser fallback in `/kz-stats`: a visible target-specific Telegram
  preview is admissible; a generic contact shell is not; one temporary tab is reused sequentially
  and closed after the batch or evidence collection ends.
- Create `.github/workflows/validate.yml` with offline schema and README-currency gates for pull
  requests and pushes to `master`.
- Append D13–D14 to `KNOWLEDGE.md`; resolve TD-3 and TD-6 in `TECH_DEBT.md`; preserve TD-5,
  TD-10, and TD-11 as open debt.
- Produce Phase C ONB, structured EV, RF, and later review traces through the normal TFW
  lifecycle.

### Out of Scope

- Phase D, the catalog-wide live sweep, any target-specific smoke request, member-count refresh,
  liveness/date verification of production entries, owner archive triage, or production archive
  population.
- Opening Chrome or any browser during Phase C. Browser behavior is a future CL evidence protocol
  encoded in the command adapter, not Phase C evidence collection.
- Invoking `/kz-stats` or `/kz-release`; preparing or finalizing a dated snapshot; editing a dated
  changelog section; creating a release commit; tag; push; or remote mutation.
- Adding, removing, re-vetting, renaming, re-describing, recounting, or re-dating a live Telegram
  entry. The only production-data structural change is an empty `archive` array.
- Editing `README.md` by hand. All README changes must be emitted by the generator.
- Modifying `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `RELEASE.md`, `CHANGELOG.md`, any
  `.tfw/**` file, any `.agents/**` file, or any `.claude/commands/tfw-*.md` file.
- Repairing TD-5, TD-10, or TD-11; adding a general `scripts/` test suite; changing framework or
  adapter sources; changing `/tfw-*` behavior.
- Modifying or restructuring legacy TFW-01/TFW-02 traces, Phase A/Phase B/research artifacts, or
  the frozen Master HL.
- New dependencies. The scripts remain standard-library Python under the inherited Quality
  Contract.

## 3. Principles Check

| # | Principle (from Master HL §7) | Enforced by | Gate |
|---|--------------------------------|-------------|------|
| P1 | The trace before the improvement | AC-7 | Phase B RF/APPROVE REVIEW and baseline `d31e60d` remain intact; Phase C owns only its declared implementation and lifecycle paths |
| P2 | Honest history over tidy history | AC-4, AC-7 | Command files are verified but not invoked; no live, release, tag, push, or browser result is claimed; commits use A6 attribution |
| P3 | One copy of every rule | AC-4, AC-7 | Project operations live only in new `kz-*` adapters; framework `tfw-*`, `.tfw/**`, and `.agents/**` stay unchanged |
| P4 | Derived facts are never written by hand | AC-1, AC-3, AC-5 | Schema/generator derive values from JSON; README is generator-only; CI runs the same currency contract |
| P5 | Non-goals are load-bearing | AC-1, AC-3 | The approved data-borne North Star is required and rendered exactly, with all non-goals |
| P6 | The network is the only authority on liveness | AC-2, AC-4, AC-7 | Classifier writes live facts only from positive target evidence; Phase C performs no network or browser observation |
| P7 | Absence of evidence is not death | AC-2, AC-4 | C4 is ambiguous; archive requires explicit evidence/owner triage; repair, death, and unresolved branches remain distinct |
| P8 | The tool serves the operation | AC-2, AC-4, AC-5 | Machine-readable statistics, bounded project commands, and offline CI replace the manual checklist without weakening gates |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `data/communities.json` | MODIFY | Add only an empty top-level `archive` array |
| `scripts/validate_schema.py` | MODIFY | Validate North Star/archive and report freshness |
| `scripts/validate_links.py` | MODIFY | Safe target classifier, update/archive semantics, and machine-readable summary |
| `scripts/generate_readme.py` | MODIFY | Purpose/stats/order/anchors/archive rendering and normalized currency check |
| `.claude/commands/kz-stats.md` | CREATE | CL live-statistics and evidence/triage operation for later invocation |
| `.claude/commands/kz-release.md` | CREATE | CL release-preparation operation with stop-before-tag/push gate |
| `.github/workflows/validate.yml` | CREATE | Offline PR/push validation for `master` |
| `README.md` | MODIFY (GENERATED) | Presentation-only output from `generate_readme.py` |
| `KNOWLEDGE.md` | MODIFY | Append D13–D14 only |
| `TECH_DEBT.md` | MODIFY | Resolve TD-3 and TD-6 only |

**Budget:** 3 new implementation files, 7 modifications, 10 implementation paths, estimated
implementation delta below 2000 LOC. With Phase HL, TS, ONB, RF, EV, three review-stage files,
and REVIEW, the phase has at most 12 new files and 19 total paths. Limits: 30 files, 15 new
files, 3000 LOC, 30 modified files. No override is authorized or required.

## 5. Acceptance Criteria

### AC-1: Enforce the structured data contract offline

The production data gains only an empty archive container, while the schema validator makes the
approved North Star, archive integrity, and date freshness observable and deterministic.

- [ ] `data/communities.json` has a top-level `archive` array whose Phase C production value is
  empty; `meta`, `north_star`, `groups`, `channels`, `bots`, and `categories` are semantically
  identical to the Phase C ONB snapshot.
- [ ] `north_star.purpose` must be a non-empty string and `north_star.non_goals` a non-empty list
  of non-empty strings; missing, wrong-typed, or empty values make schema validation exit non-zero.
- [ ] A non-empty archive fixture requires an entry type (`groups`, `channels`, or `bots`), the
  corresponding live-entry fields, an ISO `died_on`, and a non-empty evidence-based `reason`;
  an archive handle colliding case-insensitively with any live handle is rejected.
- [ ] Live-entry `last_verified` dates remain schema-validated. The validator reports the oldest
  live date and the number older than 90 days; valid staleness alone exits zero, while malformed
  or impossible dates remain fatal.
- [ ] Summary output uses ASCII tags and reports dynamic values from the parsed data rather than
  embedding mutable catalog counts or dates in source code.

Gate: Run `python scripts/validate_schema.py` against the unchanged live catalog plus empty
archive and require exit 0. In an isolated in-memory or temporary-data harness, require non-zero
results for missing/empty North Star, malformed archive date, empty reason, wrong entry type,
missing type-specific field, and archive/live handle collision; require zero for a valid stale
fixture while confirming the freshness warning. The harness must not replace or rewrite the
production JSON.

Evidence: N/A — this is deterministic local schema behavior. Record command output and the
isolated fixture matrix inline in `evidence/EV__phase-c__pipeline_tooling.md`.

### AC-2: Make link classification, updates, archive input, and summaries evidence-safe  [depends: AC-1]

The link tool distinguishes what Telegram actually proves. A positive target binding can refresh
a date without a numeric count; ambiguous or generic responses cannot create a live or dead fact.

- [ ] Classification separates at least: target-specific verified preview, ambiguous contact
  shell, generic/non-target page, and explicit request/deletion failure. The machine-readable
  summary preserves the classification and observed reason for each handle.
- [ ] A target-specific preview must bind the requested handle and the declared entry type before
  it is verified. A valid no-count preview remains verified with `member_count = null`; a numeric
  count is parsed only from the target-specific preview region.
- [ ] A C4 marker-free HTTP 200 contact shell is `ambiguous`: it does not refresh
  `last_verified`, does not change `member_count`, and is not an automatic archive candidate.
- [ ] A C5 generic Telegram landing page is non-target evidence: member-like site-wide prose is
  never parsed as the entry's count and no verification date is written.
- [ ] Under `--update`, only verified targets receive the observed run date; an observed numeric
  count updates independently, no-count remains absent, and a persisted update writes
  `meta.last_updated` from the run date. The production catalog is not passed to this mode in
  Phase C.
- [ ] The machine-readable run summary contains dynamically derived totals and per-entry fields
  sufficient for `/kz-stats` to show grew, shrank, unchanged, first-count, verified, ambiguous,
  and failed outcomes without scraping human-formatted console text.
- [ ] Archive mutation is explicit per handle after external evidence and owner triage: it moves
  rather than deletes the record, preserves its original fields, adds type, `died_on`, and a
  non-empty reason, and cannot auto-archive an ambiguous or merely failed request.
- [ ] Existing batch size, request delay, retry count, timeout, and backoff semantics remain
  unchanged unless an executor raises a contract conflict in ONB and stops.

Gate: Use a fully offline, isolated harness that imports the classifier/update/archive behavior
without opening a socket. Demonstrate C3 (target preview, no count → verified/date eligible), C4
(contact shell → ambiguous/no mutation), and C5 (generic page containing member-like prose →
non-target/no count/no mutation), plus a target-preview count case and explicit failure. Exercise
`--update` and explicit archive behavior only against temporary data, verify the machine-readable
summary schema and deltas, and compare production JSON semantics before/after. Inline the
sanitized synthetic response shapes and results in the EV file; do not claim they are fresh live
captures.

Evidence: N/A — A5 permits deterministic fixtures/captured shapes and Phase C is expressly
offline. Real Telegram and any browser fallback evidence belong to Phase D.

### AC-3: Generate the promised README presentation and currency contract  [depends: AC-1]

The generator turns the Phase B data contract into the public presentation and exposes a
non-mutating, cross-platform way to prove that `README.md` is current.

- [ ] `## Purpose` appears immediately after the dynamic stats line and contains the exact
  `north_star.purpose` plus every `north_star.non_goals` string without a second hand-maintained
  copy in source.
- [ ] The stats line derives group/channel/bot totals, category count, and the oldest live
  `last_verified` date from parsed data. Archive records do not inflate live counts or the live
  freshness signal.
- [ ] Group categories are ordered by display name in both TOC and body;
  `Engineering Management` precedes `Game Development`, and both precede `General`.
- [ ] Every TOC category href emitted for current used categories resolves to its generated
  heading under GitHub's slug rules. Unused categories emit neither an orphan row nor a heading.
- [ ] When archive is non-empty in an isolated fixture, the README includes an `## Archive` TOC
  row and a collapsed details section with type, last known entry data, `died_on`, and reason.
  With the production empty archive, both the row and section are absent.
- [ ] The unused `datetime` import is removed and no new dependency is added.
- [ ] A non-mutating check mode exits zero when UTF-8 generated and current content are equal
  after explicit newline normalization and non-zero when an isolated stale/hand-edited README
  differs. It does not rewrite the file it checks.
- [ ] Production `README.md` is regenerated by running the generator only. Its diff changes
  presentation but no live entry name, handle, description, count, or verification date.

Gate: Run `python scripts/generate_readme.py`, then its non-mutating currency check and require
exit 0. Parse the output to compare Purpose strings with JSON, dynamic stats with computed data,
category TOC/body order and href/heading pairs. Call the pure renderer against an isolated
non-empty archive fixture and assert the conditional collapsed section, then assert the
production empty-archive output omits it. Verify a temporary altered README makes check mode fail
without changing production data or output.

Evidence: N/A — the deliverable is deterministic generated local content. Record hashes,
render assertions, and check-mode output in the EV file.

### AC-4: Define bounded project commands without changing framework adapters  [depends: AC-2, AC-3]

The two `kz-*` command files make the later catalog operation explicit while preserving CL
authority, evidence, and release gates. Phase C creates and inspects them but never invokes them.

- [ ] `.claude/commands/kz-stats.md` is a complete CL operation that validates structure, runs
  the live updater with machine-readable output when later authorized, presents count deltas and
  every ambiguous/failed result, and requires per-entry owner triage before any archive mutation.
- [ ] `/kz-stats` exposes verify-current-target, repair-live-link, archive-proven-death, and
  unresolved branches. It never turns one failed request, a wrong/unoccupied handle, or owner
  approval without death evidence into an archive fact.
- [ ] `/kz-stats` permits a future visible Telegram preview only when it is target-specific and
  binds requested handle, visible name, declared type, and observed count or explicit no-count.
  A generic contact shell is rejected as evidence; one temporary Chrome tab is reused
  sequentially and closed after the batch or when evidence collection ends.
- [ ] `.claude/commands/kz-release.md` follows `RELEASE.md`: schema validation, non-mutating
  README-currency gate, complete-sweep/evidence and unresolved-state gates, root changelog
  preparation, a truthful attributed commit, then a hard stop for explicit owner approval before
  any `data-YYYY-MM-DD` tag or push.
- [ ] `/kz-release` refuses a generator-stale/hand-edited README, a partial or unresolved sweep,
  a conflicting existing tag, or missing owner approval; it does not treat Phase C TS approval as
  release approval.
- [ ] Both files use the `kz-*` namespace and resolve their local references. All existing
  `.claude/commands/tfw-*.md` files, `.agents/**`, and `.tfw/**` match the ONB snapshot.
- [ ] No project command is invoked in Phase C; no network, browser, changelog release section,
  release commit, tag, or push result is claimed.

Gate: Parse both command documents for complete ordered gates, CL stops, archive dispositions,
browser fallback requirements, README check, acting-product attribution, and explicit
stop-before-tag/push. Resolve referenced local paths. Compare framework adapter hashes with ONB
and inspect local action history/status to confirm neither project command nor any external
operation ran.

Evidence: N/A — Phase C verifies the local adapters, not their future live execution. If the
browser fallback is used in Phase D, that phase's EV must reference a target-specific capture and
the one-tab cleanup observation.

### AC-5: Add an offline CI validation gate  [depends: AC-1, AC-3]

GitHub validation must catch invalid data and stale generated presentation without depending on
Telegram or modifying repository content.

- [ ] `.github/workflows/validate.yml` triggers on pull requests and pushes to `master`.
- [ ] The job checks out the repository, uses a supported Python 3.10+ runtime, runs
  `python scripts/validate_schema.py`, then runs the generator's non-mutating README currency
  check.
- [ ] The workflow does not invoke `validate_links.py`, Telegram, browser automation, archive
  mutation, release commands, secrets, tags, pushes, or a write-mode generator step.
- [ ] The same two validation commands pass locally from the repository root.
- [ ] TD-3 is marked resolved only after the workflow file and local-equivalent gates exist;
  no claim is made that a remote GitHub run occurred in Phase C.

Gate: Parse the workflow and triggers; scan it for forbidden network/live/release commands; run
the exact local schema and README-check commands and require exit 0. Validate YAML structure with
an available local parser if present; absence of an optional parser is not permission to install
a dependency.

Evidence: DEFERRED — a real GitHub Actions run requires a later authorized push, which Phase C
forbids. Record that blocker and the passing exact local-equivalent output in the EV file.

### AC-6: Record only Phase C decisions and resolved debt  [depends: AC-1, AC-4, AC-5]

Project memory reflects what Phase C actually delivered without pulling Phase D or unrelated
adapter maintenance into scope.

- [ ] `KNOWLEDGE.md` adds D13 once: schema freshness is reported, not enforced; valid staleness
  exits zero and invalid dates/data exit non-zero.
- [ ] `KNOWLEDGE.md` adds D14 once: project operations use the `kz-*` namespace and framework
  operations remain `tfw-*`.
- [ ] D1–D12 and all Phase A/B index and legacy rows remain present and unchanged in meaning;
  D15 is absent because Phase D has not occurred.
- [ ] TD-3 records the delivered offline CI workflow as resolved and TD-6 records pipeline-owned
  `meta.last_updated` as resolved, without claiming that a fresh production sweep occurred.
- [ ] TD-2 and TD-4 remain unresolved for Phase D; TD-5 remains open; TD-10 and TD-11 remain open
  Medium debt with their existing scope and sources.

Gate: Compare keyed decision/debt rows and protected documentation hashes with ONB. Resolve D13–
D14 sources to the Master/Phase C trace, verify D15 is absent, and verify the only debt status
transitions are TD-3 and TD-6.

Evidence: N/A — the result is deterministic project-memory text. Record the keyed comparison in
the EV file.

### AC-7: Keep Phase C offline, bounded, and ready for Phase D  [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6]

The final Phase C change set is limited to §4 implementation paths plus mandatory Phase C
lifecycle traces, passes every offline gate, and contains no live-state or release action.

- [ ] Production data differs only by the empty `archive` container; no live entry field and no
  existing `meta`, `north_star`, or category value changes. Generated README is presentation-only.
- [ ] The ten implementation paths in §4 are the complete implementation set. Existing dirty
  user/workflow state and all out-of-scope paths match their ONB snapshots, excluding only
  lifecycle-status edits owned by the current workflow.
- [ ] `python scripts/validate_schema.py` and the generator currency check exit zero; isolated
  schema, C3/C4/C5 classifier, update/archive, README archive, stale-README, and command/CI gates
  all pass without a network-capable test path.
- [ ] `.agents/**`, `.tfw/**`, every `/tfw-*` adapter, Master/Phase A/Phase B/research traces,
  `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `RELEASE.md`, `CHANGELOG.md`, and legacy task
  folders remain unchanged from ONB.
- [ ] Executor commits in the current Codex context use
  `[codex/TFW-4/pipeline-tooling/executor]`; if a different product executes, A6 and
  `conventions.md` §4 supply that actual lowercase product token. Dates and claims remain current
  and truthful.
- [ ] No socket request, Telegram fetch, browser/tab action, project-command invocation, live
  sweep, production count/date refresh, owner archive decision, release, release commit, tag,
  push, destructive restore, or broad staging occurs.
- [ ] The RF explicitly states that Phase D remains next and that live/browser/release evidence
  has not been collected.

Gate: Compare final paths, semantic JSON, protected hashes, adapter hashes, README-derived entry
facts, commit subjects/dates, tags, remotes, and repository status with ONB. Review the EV file for
all seven AC rows, the inline offline fixture results, one DEFERRED CI-live row with its blocker,
and no fabricated external evidence. Do not obtain a narrow diff by resetting/restoring unrelated
work.

Evidence: N/A — Phase C is intentionally local/offline. The mandatory EV file records
deterministic verification and the explicit absence of external-state claims.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-c__pipeline_tooling.md` | Structured environment, per-AC results, protected-state comparisons, inline sanitized C3/C4/C5 shapes, offline harness output, CI-live blocker, and verdict (required) |

The EV file must cover every AC. It must label C3/C4/C5 inputs as synthetic/sanitized offline
fixtures, not fresh Telegram captures. AC-5's remote CI evidence is `DEFERRED` with the specific
no-push blocker; deterministic local checks remain mandatory. No screenshot, browser log, or
network response is expected or permitted in Phase C.

## 6. Technical Guidance

- Frozen authority: Master HL baseline `d31e60d`, including approved A5 and A6. Phase derivation:
  `HL__phase-c__pipeline_tooling.md`. Factual predecessor: Phase B RF plus repeat
  `✅ APPROVE` REVIEW and applied docs/board state.
- Current production data has `meta`, `north_star`, `groups`, `channels`, `bots`, and
  `categories`; `archive` is absent. Phase C adds an empty array only. Temporary fixtures must use
  an isolated path or in-memory object and must never replace production data.
- The flat archive needs an entry-type discriminator so type-specific required fields and README
  presentation remain unambiguous. This is execution context for the already-approved archive
  deliverable, not a new catalog claim.
- Research iteration 1 configurations are the classifier gate: C3 is target preview/no count, C4
  is contact shell/no preview metadata, and C5 is global landing content with unrelated
  member-like prose. Iteration 2 requires current-peer binding plus declared type/continuity for
  any authenticated fallback and preserves repair/death/unresolved branches.
- The machine-readable summary is an interface between `validate_links.py` and `/kz-stats`.
  Human console output may remain readable, but the adapter must not parse presentation text to
  recover deltas or triage states.
- A non-mutating generator check mode is the shared currency gate for local work, `/kz-release`,
  and CI. Explicit UTF-8 decoding and newline normalization prevent Windows/CI false failures.
  Technical implementation may differ if it preserves those observable semantics.
- The public freshness signal should be conservative: use the oldest live `last_verified` date.
  `meta.last_updated` records pipeline persistence, not proof that every live target passed.
- `.claude/commands/*.md` uses front matter plus complete operational instructions. The new
  project-owned namespace must not copy or modify framework adapter content.
- `RELEASE.md` is read-only input for `/kz-release`. Root `CHANGELOG.md` remains untouched because
  Phase C delivers tooling, not a dated catalog snapshot.
- TD-5 remains open: inline/import-based fixture gates in the EV are bounded A5 evidence, not a
  general scripts test-suite repair.
- Work from the current dirty checkout. Snapshot protected path hashes in ONB, use path-scoped
  staging/commits, and never use a whole-tree restore or `git add .`.

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

- ❌ Any Telegram/network request, browser opening/tab action, live validator run against the
  production catalog, `/kz-stats` or `/kz-release` invocation, release action, tag, or push occurs.
- ❌ A C4 contact shell or C5 generic page refreshes a verification date, yields a member count,
  or becomes an automatic archive candidate.
- ❌ A community is archived from one failed request, a broken/unoccupied username, ambiguity,
  or owner approval without independent evidence identifying the same historical community as
  deleted/closed.
- ❌ A production live entry, existing `meta` value, North Star string, category, count, or
  verification date changes; `archive` becomes non-empty in Phase C.
- ❌ `README.md` is hand-edited, generated from changed live facts, or reports a freshness date
  newer than the oldest live `last_verified` date.
- ❌ CI invokes the link validator, depends on Telegram/browser/secrets, mutates README/data, or
  performs a release/tag/push action.
- ❌ Any `.tfw/**`, `.agents/**`, `.claude/commands/tfw-*.md`, Master/Phase A/Phase B/research,
  legacy-task, or other out-of-scope file is modified, deleted, moved, or restored.
- ❌ TD-5, TD-10, or TD-11 is repaired, closed, rewritten in substance, or used to justify an
  adapter/framework change; D15 is recorded before Phase D.
- ❌ A placeholder, stub, copied mutable catalog value, new dependency, inferred external fact,
  or false claim of live/CI/release evidence appears.
- ❌ An AI-authored commit uses an agent token different from the actual executing product, is
  backdated, broadly stages unrelated dirty work, or claims Phase D work not performed.
- ❌ Any offline gate fails or the final implementation path set exceeds §4 without a new owner
  decision; delegated authority cannot approve a budget or scope overrun.

Correct ordinary implementation defects before RF and rerun all affected offline gates. If a
protected/out-of-scope path changes, restore only that exact path from the ONB snapshot, stop, and
report. If any external action or inferred catalog fact occurs, stop immediately and escalate;
do not continue or manufacture compensating evidence.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Classifier still equates HTTP success with target identity | AC-2 explicit states plus offline C3/C4/C5 matrix and mutation assertions |
| Archive CLI is technically capable of bypassing owner evidence | Require explicit per-handle mutation and encode the four-way CL disposition in `/kz-stats`; never run it in Phase C |
| Machine summary and command adapter drift | Treat summary fields/classifications as an AC interface and test the adapter against offline sample output |
| Freshness presentation overclaims partial verification | Render the oldest live date; keep `meta.last_updated` semantically distinct |
| README check rewrites the file or fails on CRLF | Dedicated non-mutating mode, UTF-8, normalized newlines, isolated stale-file test |
| Generated presentation hides a live-data mutation | Semantic pre/post catalog comparison plus rendered entry-fact comparison |
| CI appears complete without a remote run | AC-5 exact local equivalent plus `DEFERRED` remote evidence; no claim of remote success |
| Adjacent adapter debt tempts a bonus fix | Hash-protect `.agents/**`/`.tfw/**`, keep TD-10/TD-11 open, and reject scope expansion |
| Dirty checkout causes broad staging or trace loss | ONB manifest, path-scoped edits/commits, no broad restore or staging |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|------------------|-------------------|
| `data/communities.json` | Phase D | Phase C adds empty archive/tooling contract only; Phase D alone writes observed counts/dates, archives approved deaths, and changes `meta.last_updated` through the live operation |
| `README.md` | Phase D | Phase C presentation-only output precedes Phase D data-driven regeneration; reviewers must keep the diffs separable |
| `KNOWLEDGE.md` | Phase D | Phase C appends D13–D14; Phase D may append D15 only after the live triage behavior actually occurs |
| `TECH_DEBT.md` | Phase D | Phase C resolves TD-3/TD-6 tooling; Phase D alone can resolve TD-2/TD-4 from live evidence |

---

*TS — TFW-4 / Phase C: Pipeline & Tooling | 2026-08-27*

# TS — TFW-4 / Phase D: Live Sweep & First Release

> **Date**: 2026-08-27
> **Author**: Coordinator (Codex)
> **Status**: 🟠 READY — exact G3 68+3 pre-staging amendment approved; AC6 handoff ready;
> Phase D remains `ONB` after REVIEW `REVISE`; G4 exact-current-commit gate remains pending
> **Approval Boundary**: Owner verdict “Отлично, даю апрув на запуск D” approved this exact
> derivation-only Phase HL/TS as G0; G1 and the bounded post-merge `cursor_kz` supplement later
> completed. Owner saubakirov's direct verdict “одобряю” on 2026-08-27 in source task
> `01a03eef-e770-7271-82e3-727586c7d274` immediately answered the exact four-position OWNER G2
> WAIT and approved only the package in §6. G2 later completed and REVIEW verified all G1/G2 data
> and evidence. Owner saubakirov's next direct verdict “одобряю” on 2026-08-27 in the same source
> task immediately answered the exact G3 request: execute `/kz-release` for TFW-4, prepare local
> snapshot `data-2026-08-27`, update root `CHANGELOG.md`, create one path-scoped local release
> commit, then hard-stop before tag/push. The owner's next direct instruction on 2026-08-27 —
> “Без разницы мне, достигни цели, которую я поставил. Задачу доведи до логического конца, так
> чтобы осталось только сделать пуш.” — immediately answered the exact §6 G3 pre-staging scope
> request and approves its recommended 68-path trace checkpoint followed by the exact three-path
> AC6 release commit. This still supplies no exact-current-commit G4 tag or push authority.
> **v2 Resume State**: `phase-d/status.md` is `ONB` after immutable transition
> `20260827-092520`. Binding REVIEW `REVISE` accepted all G1/G2 facts but rejected the premature
> completion lifecycle. Existing EV, RF, REVIEW, and review stages remain historical checkpoint
> artifacts. `tasks/00-INDEX.md` is a generated projection only.
> **Parent Phase HL**: [Phase D HL](HL__phase-d__live_sweep_release.md)
> **Parent Master HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Frozen Authority**: Master HL baseline `d31e60d`; this TS is derivation-only and
> creates no amendment
> **Mode**: CL — live observation, each repair/archive decision, local release preparation, and
> final publication authority use explicit owner gates

---

## 1. Objective

Complete TFW-4 Phase D without weakening its accuracy or authority contract: verify every live
catalog entry against contemporaneous Telegram evidence, retry and triage every non-verified
result without invention, persist only observed facts, regenerate the public catalog, prepare a
truthful local dated snapshot, and stop for a separate final owner decision before any tag or
push. The phase is complete only when the frozen Master DoD is satisfied or the owner explicitly
revises the task through the proper workflow; a locally prepared commit is not publication.

## 2. Scope

### In Scope

- After approval and `/tfw-handoff` onboarding, snapshot the execution-start live catalog,
  protected dirty checkout, existing refs, and mutable Phase D paths before any write.
- After a separate explicit owner invocation of `/kz-stats`, run the catalog-wide live
  sweep, retain its raw machine summary, and show derived count/classification deltas.
- Retry every `ambiguous`, `non_target`, or `failed` result once by exact handle
  and retain the consolidated raw retry results.
- When scripted evidence remains insufficient, use a visible target-specific Telegram preview
  or authenticated peer resolution as bounded fallback evidence. Reuse one temporary Chrome tab
  sequentially for all fallback checks, close it after the batch, and confirm no temporary
  fallback tab remains.
- Assign each non-verified entry one evidence-backed disposition with the owner: verify the
  current target, repair a proven living replacement and recheck, archive independently proven
  death with exact per-entry approval, or leave unresolved.
- Update `data/communities.json` only with observed dates/counts, approved and reverified
  repairs, independently evidenced owner-approved archives, and pipeline-owned metadata.
- Validate the final catalog, regenerate `README.md` only through the generator, and require
  its non-mutating currency gate.
- After a separate explicit owner invocation of `/kz-release`, derive the snapshot date
  from the complete evidence set, prepare the root dated changelog, and create one reviewed,
  path-scoped local snapshot commit.
- Stop after local preparation. Only after a fresh owner approval naming the exact commit, tag,
  branch, and remote may the executor create the annotated dated tag and push that exact state.
- Record D15 and the evidence-backed TD-2/TD-4 transitions; maintain task-local Phase D
  `status.md` and immutable journal events, then regenerate the derived portfolio index.

### Out of Scope

- Any Phase D execution before explicit approval of this HL/TS and start through
  `/tfw-handoff tfw-4`.
- Any network, browser, authenticated-client, `/kz-*`, live validator, data, README,
  changelog, release, tag, or push action performed merely because G0 approval is recorded.
- Adding, removing, re-vetting, renaming, or redescribing communities on editorial judgement.
  A link repair is in scope only when retained evidence proves continuity with the same live
  community and the owner approves the exact repair.
- Treating one failed request, a repeated failure, ambiguity, an unoccupied/wrong username,
  absence of a count, a generic contact shell, or owner approval alone as proof of death.
- Hand-editing `README.md`, hardcoding mutable catalog counts/dates, estimating a member
  count, or inferring a verification date, type, identity, replacement, or death.
- Editing `RELEASE.md`, `AGENTS.md`, `CLAUDE.md`,
  `CONTRIBUTING.md`, scripts, project command definitions, CI, `.tfw/**`,
  `.agents/**`, or any `.claude/commands/tfw-*.md` file.
- Modifying the Master HL, its frozen baseline, any Phase A–C artifact, or any research artifact
  except the exact Coordinator-owned A5 open-to-closed reconciliation in
  `research/iterations.yaml` approved by the 2026-08-27 G3 scope verdict. No RES/stage rewrite,
  Master amendment, or retrospective cleanup is authorized.
- Fixing, rewriting, resolving, or otherwise changing TD-5, TD-10, or TD-11.
- Changing `.tfw/VERSION`, adding project semver, editing
  `.tfw/CHANGELOG.md`, creating a GitHub Release, or publishing anywhere beyond the exact
  approved branch commit and `data-YYYY-MM-DD` tag.
- Force-tagging, force-pushing, moving an existing tag, broad staging, whole-tree restore,
  history rewriting, or automatic rollback of user-owned dirty state.
- Creating ONB, implementation, evidence, RF, REVIEW, a release commit, tag, or push during this
  planning workflow.

## 3. Principles Check

| # | Principle (from Master HL §7) | Enforced by | Gate |
|---|--------------------------------|-------------|------|
| P1 | The trace before the improvement | AC-1, AC-8 | Baseline `d31e60d` and accepted predecessor traces are hash-checked; Phase D writes only its lifecycle/result paths |
| P2 | Honest history over tidy history | AC-2, AC-6, AC-7 | Raw failures and partial state remain visible; local preparation is not called a release; commit/publication results are recorded only after they occur |
| P3 | One copy of every rule | AC-1, AC-8 | Existing command/release contracts are invoked/read, not duplicated or modified; master and project rules remain protected |
| P4 | Derived facts are never written by hand | AC-2, AC-4, AC-5, AC-6 | Dates/counts/changelog claims come from retained observations; README comes only from JSON plus generator |
| P5 | Non-goals are load-bearing | AC-4, AC-8 | Editorial additions, promotion, estimation, and hand-maintained derived facts are excluded and checked |
| P6 | The network is the only authority on liveness | AC-2, AC-3, AC-4 | Every surviving live date and count has contemporaneous target-specific evidence; unresolved evidence cannot become a fact |
| P7 | Absence of evidence is not death | AC-3, AC-4 | One retry, independent death evidence, and exact owner triage precede archive; unresolved remains unchanged and blocks release |
| P8 | The tool serves the operation | AC-2, AC-5, AC-6, AC-7 | Delivered `kz-*` operations carry the sweep and preparation while preserving explicit human authority gates |

## 4. Affected Files

| File | Action after approval | Description |
|------|-----------------------|-------------|
| `data/communities.json` | MODIFY | Evidence-backed live observations, approved repairs/archives, and pipeline-owned metadata |
| `README.md` | MODIFY (GENERATED) | Generated public result from the final reviewed data |
| `CHANGELOG.md` | MODIFY | Dated catalog snapshot derived from retained evidence |
| `KNOWLEDGE.md` | MODIFY | Add D15 once after live retry/owner triage occurs |
| `TECH_DEBT.md` | MODIFY | Resolve TD-2/TD-4 only after their evidence gates |
| `tasks/TFW-4__showcase_reorg/phase-d/status.md` | MODIFY | Sole Phase D lifecycle authority; remain `ONB` after REVIEW `REVISE` while AC6 resumes |
| `tasks/TFW-4__showcase_reorg/journal/*.md` | APPEND ONLY | Immutable coordination events, including the exact G3-to-AC6 handoff |
| `tasks/00-INDEX.md` | REGENERATE | Derived projection from task-local status files; never an authority |
| `tasks/TFW-4__showcase_reorg/research/iterations.yaml` | MODIFY ONCE | Coordinator-only A5 current-control reconciliation exactly approved by the owner; iteration statuses remain complete |
| `tasks/README.md`, `tasks/BOARD-SNAPSHOT.md` | READ ONLY | v2 route and retired historical board; no live lifecycle writes |
| `tasks/TFW-4__showcase_reorg/phase-d/ONB__phase-d__live_sweep_release.md` | EXISTS — IMMUTABLE | Executor onboarding and protected-state snapshot |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/EV__phase-d__live_sweep_release.md` | EXISTS — HISTORICAL CHECKPOINT | Premature RF evidence index; preserve without claiming completion |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/live_sweep_summary.json` | EXISTS — IMMUTABLE | Untouched full catalog machine summary |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/retry_summaries.json` | EXISTS — IMMUTABLE | Consolidated exact-handle retry summaries |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/browser_fallback.pdf` | EXISTS — IMMUTABLE | One multipage target-specific fallback and cleanup bundle |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/cursor_kz_supplement.json` | EXISTS — IMMUTABLE | Untouched one-entry exact-handle validator summary for the post-G1 merged live handle |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/g2_recheck_summaries.json` | EXISTS — IMMUTABLE | Byte-preserving aggregate for both successful post-repair summaries; REVIEW verified it |
| `tasks/TFW-4__showcase_reorg/phase-d/RF__phase-d__live_sweep_release.md` | EXISTS — HISTORICAL CHECKPOINT | Premature non-completion RF retained under binding REVIEW `REVISE`; replace only after final publication outcome |
| `tasks/TFW-4__showcase_reorg/phase-d/REVIEW__phase-d__live_sweep_release.md` and `review/*.md` | EXISTS — IMMUTABLE | Binding `REVISE` accepted G1/G2 and routed execution back to `ONB` for AC6–AC8 |

`RELEASE.md`, `.claude/commands/kz-stats.md`, and
`.claude/commands/kz-release.md` are read/invocation inputs, not modification targets.
The next reviewer writes a fresh REVIEW only after the final publication outcome and revised
completion RF; the current REVIEW and stages remain immutable history.

**Budget:** 0 new implementation files, 6 modified project/result files, and at most 14 new
trace/evidence files including this HL/TS, ONB, EV, four JSON artifacts, one optional
multipage browser artifact, RF, three review-stage files, and REVIEW. At most 20 phase paths and
an authored/project-result delta below 3000 LOC. Limits: 30 files, 15 new files, 3000 LOC,
30 modified files. No override is authorized. If the evidence set cannot be bundled within these
bounds, stop for an owner scope decision.

The migration-created phase status, task-root journal, and generated portfolio index are v2
lifecycle control/projection paths. The owner's exact 2026-08-27 G3 scope verdict additionally
authorizes the enumerated 68-path trace checkpoint as a narrow process-only budget/read-only
override; it does not widen the frozen Phase D implementation or Telegram evidence scope.

## 5. Acceptance Criteria

### AC-1: Establish an approved, protected execution baseline

Phase D begins only from an explicit owner-approved draft and an executor ONB that distinguishes
user-owned dirty state, frozen/predecessor authority, and the exact live/release scope.

- [ ] The owner explicitly approves this Phase HL and TS; `/tfw-handoff tfw-4` starts a
  separate Executor turn before any Phase D action.
- [ ] ONB confirms the current Master HL blob equals `d31e60d` and the revised Phase C
  RF plus repeat `APPROVE` REVIEW are the factual predecessor.
- [ ] ONB records the exact execution-start live-handle set derived from JSON, mutable Phase D
  path hashes/byte snapshots, current dirty/untracked paths, existing `data-*` tags,
  branch/remote facts, and relevant command/release-contract hashes.
- [ ] Existing user/workflow changes are protected by path-scoped staging and exact snapshots;
  no state is reconstructed from `HEAD` and no whole-tree restore is planned.
- [ ] The owner is told that approved handoff is not `/kz-stats` invocation, per-entry
  repair/archive approval, `/kz-release` invocation, or tag/push approval.

Gate: Read-only compare the Master blob with `d31e60d`, resolve all predecessor/contract
references, enumerate execution-start live handles and protected dirty paths, hash the mutable
inputs, inspect local tags/branch/remotes, and record the results in ONB. No project script,
network, browser, or mutable action is part of this gate.

Evidence: N/A — deterministic local onboarding. Record hashes, live-handle manifest digest, and
authority checklist in ONB/EV; do not copy mutable catalog totals into narrative documentation.

### AC-2: Collect a complete catalog-wide live sweep  [depends: AC-1]

After the owner explicitly invokes `/kz-stats`, every execution-start live handle is
observed once through the delivered classifier and represented exactly once in an intact machine
summary.

- [ ] The preflight schema gate exits zero before the live run.
- [ ] The full sweep is run with update plus a temporary machine-summary path; the raw summary is
  copied unchanged to `evidence/live_sweep_summary.json` before human rendering or triage.
- [ ] The retained summary has the expected schema version, an observed run date, internally
  consistent totals, and one record for every execution-start live handle with no missing,
  duplicate, or foreign handle.
- [ ] Every `verified` record has target binding and matching declared/observed type.
  Its date may update even when no numeric count is present; a count updates only when observed.
- [ ] `ambiguous`, `non_target`, and `failed` records do not receive a
  verification date/count from that result and remain explicit triage inputs.
- [ ] A non-zero process exit caused by unresolved results does not erase or mislabel the
  already-persisted verified observations; actual JSON changes and raw evidence are reported.
- [ ] Human-readable grew/shrank/unchanged/first-count/classification totals and aggregate delta
  are derived from the retained JSON, never reconstructed from console prose.

Gate: Validate the raw JSON structure and exact handle coverage against the ONB manifest; compare
pre/post JSON per handle; reconcile summary totals; confirm only verified records received
observed updates and that every unresolved record is queued for AC-3.

Evidence: Full spec — live Telegram observation in the execution environment. Required artifact:
`evidence/live_sweep_summary.json` plus EV command/exit/output references, pre/post hashes,
and per-handle coverage result. VERIFIED requires the real retained summary; Phase C fixtures,
historical counts, or an unrun command are insufficient.

### AC-3: Resolve scripted uncertainty without weakening target identity  [depends: AC-2]

Every non-verified scripted result receives exactly one retained exact-handle retry and, only
when necessary, bounded target-specific fallback evidence. Missing evidence remains visible.

- [ ] Each unresolved handle from AC-2 is retried exactly once by exact handle; all retry
  summaries are preserved in one consolidated `evidence/retry_summaries.json` with original
  result linkage and actual exit outcome.
- [ ] A verified retry may update the observed date/count under the same target/type rules; a
  repeated failure, contact shell, type mismatch, non-target page, or no-count result is not death
  evidence.
- [ ] Browser fallback is used only where scripted classification cannot establish identity.
  Every accepted capture binds the requested handle, visible name, declared/observed type, and
  observed count or explicit no-count; a generic contact/landing shell is marked non-evidence.
- [ ] One temporary Chrome tab is reused sequentially for all fallback checks. No per-handle tab
  accumulation occurs; the tab is closed after the batch or when evidence collection stops, and
  a final check confirms zero remaining temporary fallback tabs.
- [ ] If authenticated Telegram resolution is used, evidence records requested handle, peer kind,
  and continuity with the catalogued community while excluding credentials, cookies, tokens,
  contacts, unrelated tabs, and session material.
- [ ] Every still-unresolved handle advances to AC-4 with its blocker and evidence references;
  no fact is invented to force completion.

Gate: Compare AC-2 unresolved handles with the consolidated retry set one-for-one. If browser or
authenticated fallback was used, inspect the single multipage bundle/EV fields for
target-specific binding, privacy redaction, sequential one-tab use, close action, and zero-tab
cleanup confirmation. If none was used, record `N/A` with the reason.

Evidence: Full spec — real exact-handle retry output is required for every AC-2 unresolved result.
Browser evidence is conditional: when used, one multipage
`evidence/browser_fallback.pdf` plus EV cleanup observation; when not used,
`N/A — all targets resolved by scripted evidence`. A generic shell can be retained as a
negative observation but can never be VERIFIED target evidence.

### AC-4: Apply only evidence-backed owner dispositions  [depends: AC-3]

Every non-verified entry has one explicit disposition, and the final live/archive data contains
no inferred identity, date, count, repair, or death.

- [ ] **Verify current target:** target-specific evidence binds the stored handle to the intended
  peer and declared type; write the observation date and only an actually observed count.
- [ ] **Repair live link:** evidence proves continuity to a living replacement; the owner
  approves the exact repair, the link/handle is updated, and the repaired target is rechecked
  before any date/count is written.
- [ ] **Archive proven death:** independent evidence identifies the same historical community as
  deleted/closed; the owner approves that exact entry; archive mutation uses a non-empty
  evidence-based reason and evidence reference; the complete record is moved, never deleted.
- [ ] **Unresolved:** no current binding, living replacement, or independent death evidence
  exists; the entry receives no unsupported mutation and the phase stops before release
  preparation.
- [ ] Owner approval is recorded per exact repair/archive and points to the evidence. General
  plan, sweep, or publication approval is not substituted for per-entry triage.
- [ ] After all dispositions, every remaining live entry is positively evidenced for one common
  snapshot date derived from the completed run. If work crosses a date boundary, affected
  entries are rechecked or the snapshot remains ineligible.
- [ ] `meta.last_updated`, every `last_verified`, count, repaired handle, archive
  `died_on`, and reason are consequences of retained observations/decisions only.

Gate: Join the ONB live set, AC-2/AC-3 evidence, owner-decision rows, and final live/archive JSON.
Require one valid disposition per non-verified record, exact evidence/approval for every
repair/archive, no silent deletion, no unresolved state, and a common evidence-derived snapshot
date for every surviving live entry. Any unresolved row fails the gate and blocks AC-5/AC-6.

Evidence: Full spec — EV decision table with one row per non-verified entry, evidence references,
exact owner decision, before/after JSON result, and recheck/archive command result. VERIFIED
archive status requires both independent death evidence and exact owner approval; either alone
is insufficient.

### AC-5: Validate and generate the final local catalog  [depends: AC-4]

The evidence-backed JSON is structurally valid and its public README is regenerated and current,
with no hand edit or editorial catalog change hidden inside the sweep.

- [ ] `python scripts/validate_schema.py` exits zero on the final data.
- [ ] `README.md` is written only by `python scripts/generate_readme.py` and the
  subsequent `--check` exits zero without changing it.
- [ ] The final diff is limited to observed live facts, owner-approved repair/archive facts,
  pipeline-owned metadata, and their deterministic generated presentation.
- [ ] No community is added, removed, renamed, redescribed, recategorized, or promoted by
  editorial judgement; no mutable count/date is copied into a hand-maintained document.
- [ ] The evidence set covers every final live handle exactly once for the snapshot date and
  every archive/repair decision before local release preparation becomes eligible.
- [ ] `RELEASE.md`, version files, framework changelog, scripts, command definitions,
  adapters, and predecessor artifacts remain unchanged.

Gate: Run schema validation, generator write, then generator `--check` in order. Compare
final JSON/README semantics and exact path hashes with ONB/evidence; verify full final-handle
coverage and no unresolved disposition.

Evidence: N/A — deterministic local validation/generation. Record command exits, output hashes,
path diff, generator-only README proof, and final evidence-coverage reconciliation in EV.

### AC-6: Prepare one local dated snapshot and stop  [depends: AC-5]

After the owner explicitly invokes `/kz-release`, the complete reviewed evidence becomes a
dated root changelog section and one truthful local snapshot commit, with no external release
state.

- [ ] The proposed `YYYY-MM-DD` is derived from the common completed-sweep evidence date;
  the matching local `data-YYYY-MM-DD` ref is checked and a conflict stops preparation.
- [ ] Release preconditions prove complete final-handle coverage, zero unresolved dispositions,
  exact archive approvals/evidence, schema success, and generator currency.
- [ ] Root `CHANGELOG.md` moves only evidence-backed catalog changes into the dated snapshot
  section. `.tfw/CHANGELOG.md` and `.tfw/VERSION` remain byte-unchanged; no semver or
  version bump occurs.
- [ ] The exact diff excludes unrelated dirty paths and is staged explicitly by reviewed path;
  broad staging is not used.
- [ ] The local commit uses
  `[codex/TFW-4/release/executor] record verified snapshot data-YYYY-MM-DD` in the current
  Codex context (or the actual lowercase executing product under A6), with current truthful
  dates and only reviewed Phase D/result paths.
- [ ] After commit, the executor presents the exact commit hash/diff, evidence set, changelog,
  proposed tag, branch, and remote, then stops. No tag, push, GitHub Release, or other publication
  exists at this gate.

Gate: Re-run release preconditions; inspect the tag namespace, final changelog, staged and
committed path lists, commit subject/dates, clean state of protected paths, and absence of a new
tag/remote action. A local commit with any unrelated path or unsupported claim fails the gate.

Evidence: Minimal spec — local Git result in the intended repository. EV must record the commit
hash/subject/date/path list, exact proposed tag/branch/remote, schema/currency outputs, protected
path comparison, and proof that the tag is still absent. This is local preparation evidence, not
publication evidence.

### AC-7: Publish only after a separate exact owner decision  [depends: AC-6]

External publication is a distinct final gate. It never follows automatically from TS approval,
`/kz-release` invocation, local commit success, or a general instruction to finish.

- [ ] The owner reviews the AC-6 package and explicitly approves creating the exact proposed
  annotated tag and pushing the exact commit/tag to the named branch and remote in the current
  release conversation.
- [ ] Without that affirmative current approval, no tag or push occurs; publication evidence is
  `DEFERRED`, the local commit remains unpublished, and Phase D remains open because Master
  DoD 24 is not met.
- [ ] After approval, HEAD, working tree, evidence set, branch/remote, and proposed tag are
  rechecked against the approved package; any drift invalidates approval and returns to the hard
  stop.
- [ ] The annotated `data-YYYY-MM-DD` tag is created without force and only the approved
  branch commit and tag are pushed. No other ref, release object, version, or unrelated state is
  published.
- [ ] Actual local and remote outcomes are retained. A failed/partial push is reported exactly;
  no success is inferred, and no delete/move/force/retry occurs without a new owner decision.

Gate: Before publication, compare current state with the exact owner-approved package. After an
approved attempt, inspect the local tag target and the actual push/remote result. Require the tag
to target the approved commit and the approved branch/tag outcome to be evidenced; otherwise
leave the AC incomplete.

Evidence: Full spec — VERIFIED only with the exact owner approval reference, local annotated-tag
target, and actual push/remote output for the approved branch and tag. DEFERRED with blocker
`final owner publication decision not granted` is truthful but does not satisfy Master DoD
24 or permit Phase D closure.

### AC-8: Close project memory only from achieved results  [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7]

Phase D traces and project memory describe only what actually happened, preserve all prior
history, and do not repair adjacent debt.

- [ ] `KNOWLEDGE.md` adds D15 exactly once only after the retry plus owner-triage behavior
  actually occurs; D1–D14 retain their accepted meaning.
- [ ] TD-2 becomes resolved only after every surviving live entry has contemporaneous evidence
  for the snapshot date. TD-4 becomes resolved only after the archive mechanism is exercised
  against every proven-dead result, or the RF explains with Master-consistent evidence why no
  proven-dead entry existed and does not falsely claim historical recovery.
- [ ] TD-3 and TD-6 remain resolved as delivered by Phase C. TD-5, TD-10, and TD-11 remain open,
  unchanged in wording/disposition, and unfixed.
- [ ] The Master HL stays byte-identical to `d31e60d`; research and Phase A–C artifacts,
  `.tfw/**`, `.agents/**`, framework commands, and legacy traces remain unchanged.
- [ ] `phase-d/status.md` remains the sole live-state authority, task-root journal events record
  material handoffs/transitions immutably, and the regenerated `tasks/00-INDEX.md` projects that
  state. `tasks/README.md` remains a route and `tasks/BOARD-SNAPSHOT.md` remains untouched
  history. TFW-4 is not marked complete while AC-7 or any frozen Master DoD item is open.
- [ ] RF is written only after the final publication outcome is known. It includes all mandatory
  sections, exact evidence statuses, deviations/partial external state, and no reconstructed or
  invented claim.

Gate: Keyed compare D1–D15 and debt rows against ONB/Phase C docs; verify protected hashes,
task-local status/journal authority, generated-index projection, evidence references,
commit/tag/push facts, and every Master DoD/DoF item. If
AC-7 is deferred or any Master DoD remains open, record the checkpoint and do not produce a
completion RF or close the task.

Evidence: N/A — deterministic trace/memory verification. EV and RF reference the external
evidence from AC-2/AC-3/AC-4/AC-7 rather than duplicating it.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-d__live_sweep_release.md` | Environment, authority gates, per-AC evidence table, owner decisions, rollback/cleanup observations, local-release package, publication result, and verdict (required) |
| `evidence/live_sweep_summary.json` | Untouched machine summary for the complete execution-start live set (required after approved sweep) |
| `evidence/retry_summaries.json` | Consolidated exact-handle retries with original-result linkage (required when AC-2 has unresolved records; otherwise N/A in EV) |
| `evidence/browser_fallback.pdf` | One multipage target-specific capture/cleanup bundle (required only if fallback is used; otherwise N/A in EV) |
| `evidence/cursor_kz_supplement.json` | Untouched one-entry exact-handle validator summary for the live handle merged after the original G1 manifest (required before current final-handle coverage may pass) |
| `evidence/g2_recheck_summaries.json` | One reproducible aggregate of both post-repair raw summaries. It must preserve the exact retained `datanomika` bytes and fresh successful `kzquake` bytes through per-record byte length, SHA-256, and reversible base64, while retaining unchanged decoded summary objects (required to complete G2; original G1 JSON artifacts remain byte-immutable) |

The EV file must cover all eight ACs. It must distinguish observed Telegram facts, owner
decisions, deterministic local gates, local release preparation, and external publication. No
artifact may contain credentials, cookies, session tokens, unrelated contacts/tabs, or inferred
facts. Evidence status uses only VERIFIED, DEFERRED, BLOCKED, and N/A.

## 6. Technical Guidance

- Authority chain: frozen Master HL `d31e60d` → this derivation-only Phase HL/TS →
  explicit owner approval → `/tfw-handoff tfw-4`. Handoff approval is still not explicit
  `/kz-stats` invocation, per-entry triage, `/kz-release` invocation, or final
  publication approval.
- Factual predecessor: revised Phase C RF, revision commits `165541c` /
  `a141f7c`, repeat REVIEW `APPROVE`, and applied docs state. The Master current blob
  must continue to equal its baseline.
- `/kz-stats` specifies the live operation. Its central command is
  `python scripts/validate_links.py --update --summary-json <temporary-summary-path>`.
  The tool saves verified updates before computing an unresolved exit. Therefore exit 1 with a
  valid summary can be expected partial observed state; a missing/malformed summary or execution
  error is a hard stop.
- Exact-handle retry uses
  `python scripts/validate_links.py --handle <handle> --update --summary-json <retry-path>`
  once per unresolved handle. Consolidate raw retry JSON without rewriting classifications or
  reasons.
- The browser supplement is fallback evidence, not a classifier bypass. A visible target-specific
  Telegram preview is admissible; a generic contact shell is not. Use one temporary tab for the
  entire batch, navigate it sequentially, close it, and query tabs afterward to confirm zero
  temporary fallback tabs remain. Authenticated resolution must bind peer kind and continuity.
- Browser/authenticated observations have no automatic production-write interface. Any resulting
  data edit must be limited to the exact observed field, referenced in EV, reviewed against the
  capture, and then schema/generator checked. Do not manufacture a synthetic summary row and call
  it validator output.
- Archive mutation uses
  `python scripts/validate_links.py --archive <handle> --reason <evidence-based-reason> --evidence-ref <artifact-reference> --owner-approved`
  only after independent same-community death evidence and exact owner approval.
- Final local generation order is `python scripts/validate_schema.py` →
  `python scripts/generate_readme.py` →
  `python scripts/generate_readme.py --check`. README is never edited directly.
- `/kz-release` owns local snapshot preparation: evidence completeness, tag conflict,
  schema/currency, root changelog, exact path staging, truthful local commit, then a hard stop.
  `RELEASE.md` is read-only authority. No version bump exists for this catalog.
- Publication, when separately approved, is limited to the exact `master` branch commit and
  annotated `data-YYYY-MM-DD` tag on the configured remote. Do not create a GitHub Release
  or push other refs.
- Work from the shared dirty checkout. ONB must preserve the current user-owned dirty/untracked
  state and use path-scoped snapshots/staging. Never use `git add .`, whole-tree restore,
  destructive reset, force-tag, or force-push.
- Before the first mutable action, create exact temporary byte snapshots outside the repository
  for mutable Phase D paths and record their hashes in ONB. If a pre-commit correction is needed,
  restore only the exact affected Phase D path/entry, retain the retraction evidence, regenerate,
  and rerun dependent gates. After commit/tag, never rewrite or delete state automatically.
- Preserve the three existing G1 artifacts byte-for-byte. Add only one raw `cursor_kz` summary
  and one bundled post-repair recheck JSON. If this cannot preserve reviewable evidence within the
  14-file phase bound, stop for an owner scope decision; delegation cannot approve an overrun.

### Post-G1 `cursor_kz` Coverage Supplement

Local semantic merge `c919640` added `groups|cursor_kz` after the ONB manifest and immutable
63-entry `evidence/live_sweep_summary.json` were produced. `origin/master` remains `d92039a`;
no push or tag exists. This is not a Master amendment: the operation preserves the historical
G1 record and supplies the missing final-live-set coverage required by AC-4/AC-5. It adds no
editorial entry or frozen deliverable. Existing G1 approval plus the owner's direct
“доделаывайте” authorizes this exact bounded supplement and nothing in G2–G4.

Execution record — completed on 2026-08-27. The exact command below ran once with exit `0`; the
durable raw JSON has SHA-256
`43605bbadd0900b14c3182b7b44416b440ba1d7734f4bc6fafbe9842aea79535`, contains exactly one
`verified / groups / groups / target_bound=true` row, and its union with the immutable 63-entry
summary covers the current 64-entry pre-G2 live set exactly once. Only the permitted
`cursor_kz` observed fields and metadata changed; post-supplement data SHA-256 is
`242796146b668a685a80e6c92a9a7a7f6406fad4fff33802f17316a8f89210a3`. The original G1
artifacts and both merge-recovery stashes retained their recorded hashes. The following contract
is retained as the completed operation's replay boundary and must not be rerun.

Before the command, the Executor must confirm that the durable supplement path does not exist,
that both merge-recovery stashes remain unchanged, and that the unique current
`groups|cursor_kz` record is byte/field-equivalent to the record introduced by merge `c919640`.
Create and hash a fresh external byte snapshot of current `data/communities.json`, plus a
structured copy of the exact record, its original group index, and `meta.last_updated`. The ONB
snapshot predates this entry and is not a valid rollback source for the supplement.

Run exactly once, from the repository root:

```powershell
python scripts/validate_links.py --handle cursor_kz --update --summary-json "tasks/TFW-4__showcase_reorg/phase-d/evidence/cursor_kz_supplement.json"
```

The command is eligible to pass only when all of the following hold:

- exit is `0`; the durable JSON exists, parses, has `schema_version=1`, the actual run date,
  `totals.total=1`, `totals.verified=1`, and zero `ambiguous`, `non_target`, and `failed`;
- `entries` contains exactly one record with `handle=cursor_kz`, `type=groups`,
  `classification=verified`, `declared_type=groups`, `observed_type=groups`, and
  `target_bound=true`; there is no duplicate or foreign handle;
- the only permitted data changes from the pre-supplement snapshot are
  `groups[cursor_kz].last_verified = summary.run_date`,
  `groups[cursor_kz].member_count = observed_count` only when that field is an integer, and
  `meta.last_updated = summary.run_date`; every copy, category, handle, collection, other live
  record, and archive value is unchanged;
- the exact typed-handle union of the immutable 63-entry G1 summary and
  `groups|cursor_kz` equals the pre-G2 current live catalog with no missing, duplicate,
  or foreign typed handle; the three original G1 artifacts retain their recorded hashes.

The earlier visible Telegram observation is direction only and may not supply a count or date.
If the command exits non-zero, the file is missing/malformed, any predicate differs, the diff is
wider, or exact union coverage fails, retain the actual output as failed evidence, restore only
`cursor_kz` fields and `meta.last_updated` changed by this command from the fresh snapshot,
preserve every other G1/merge/user change and both stashes, and stop. Do not retry, use browser
fallback, rewrite the original G1 JSON, enter G2, generate README, or create EV/RF/release state
without a new Coordinator/owner decision.

### G2 Exact Owner Decision Package

Iteration 3 is `SUFFICIENT`. Under `conventions.md` §3 rule 6, its two positive recommendations
fit the already-approved Phase D scope and AC-4 repair branch: they are target-specific factual
repairs with exact owner approval and post-repair recheck, not editorial additions and not changes
to Master HL §§1, 3–7. This section refines execution guidance only; it changes no scope, AC,
DoD, DoF, principle, phase, or Master baseline. G0 and G1 are evidence/authority predecessors,
not an exact G2 verdict.

Approval record — ✅ owner saubakirov, 2026-08-27. In source task
`01a03eef-e770-7271-82e3-727586c7d274`, the owner verdict “одобряю” directly answered the
immediately preceding instruction to approve G2 exactly as worded; the preceding message was the
full four-position package reproduced below. This reference chain binds the verdict to exactly
`datanomika`, atomic `kzquake`, `mobile_developers_kz`, and `kzqacommunity`, including their
field-level values, retries, date gate, evidence references, order, rollback, and stop behavior.
It supplies G2 only and supplies neither G3 `/kz-release` nor G4 tag/push authority.

#### Historical G2 fail-closed checkpoints and free UTF-8 refinement

Before final G2 completion, the Executor stopped fail-closed after these exact intermediate
results. They remain the replay/audit history and are not the current resume boundary:

| Candidate | Exact checkpoint | Retained state |
|-----------|------------------|----------------|
| `datanomika` | The approved structural repair and its exact validator retry succeeded with `classification=verified`, `declared_type=channels`, `observed_type=channels`, `target_bound=true`, `member_count=2731`, and `last_verified=2026-08-27` | Keep the successful `channels` record. Raw summary remains at `E:\TEMP\TFW-4-phase-d-g2-datanomika-93ab85a59ed141e695f1ba12572fee96\raw_summary.json`, 734 bytes, SHA-256 `39ef51989d671cd5f339b77fbe55a7b387ff7005e24276bad2d29ab27de9f939`; do not rerun |
| `kzquake` | The same approved atomic package was applied, then the sole plain-mode validator process exited 1 when Windows `cp1252` could not emit the approved Cyrillic `name` to stdout. The exception occurred before summary/update | Candidate-only byte rollback completed. No raw summary exists for that attempt. The external checkpoint root is `E:\TEMP\TFW-4-phase-d-g2-kzquake-48d78995c3094d5988a08cbc0527a327`; current whole-data SHA-256 is `628095507c7f9b435fb11d5e1b49177179846608bd3b6f930e365562173be27d` |
| PS5 snapshot setup | After lifecycle entered the recorded `RF` state, the next executor attempted `New-Item -LiteralPath` for the fresh `kzquake` resume root. Windows PowerShell 5 rejected the unsupported parameter before the root existed | No directory, copy, candidate mutation, raw summary, or validator invocation occurred. The single fresh `python -X utf8` allowance remains unused; resume from directory creation with the compatible guarded block below |
| `mobile_developers_kz`, `kzqacommunity` | No archive command ran | Both remain unchanged live rows and `archive` remains empty |

Explicit process UTF-8 is a free execution-guidance refinement under `conventions.md` §3 rule 6,
not a Master or G2 amendment. `python -X utf8` changes only the interpreter's process I/O encoding
so the already-approved Cyrillic field can pass the script's console-print boundary. It does not
change the HTTP request, target binding, classifier, update ownership, approved field values,
success predicate, rollback, candidate order, evidence budget, AC, DoD/DoF item, principle, phase,
or frozen baseline `d31e60d`. The failed process supplied neither a raw result document nor an
update and remains an indexed execution failure, not a Telegram disposition result. The existing
exact G2 approval therefore remains sufficient for one replacement invocation under the bounded
resume procedure below; it authorizes no second replacement attempt.

The directory-create compatibility correction is likewise free execution guidance under
`conventions.md` §3 rule 6. Windows PowerShell 5 exposes `New-Item -Path` but not
`New-Item -LiteralPath`. Fixed `E:\TEMP` prefixes plus regex-bound GUID-only suffixes,
pre-existence checks, `Resolve-Path`, exact-prefix/leaf checks, and empty-root checks change no
approved entry value, Telegram request, retry budget, success predicate, snapshot payload/hash,
candidate order, rollback, evidence budget, AC, DoD/DoF item, principle, phase, or Master baseline.
The same compatibility guard applies to `kzquake` and both later archive snapshots; no G2
re-approval is required.

Decision evidence:

| Reference | SHA-256 / exact bearing |
|-----------|------------------------|
| [`evidence/live_sweep_summary.json`](evidence/live_sweep_summary.json) | `bb99e525814c70a5f47510159ba162cffb617c5dc879436b50f13a26bab3ffa7`; authoritative target binding and declared/observed type results |
| [`evidence/retry_summaries.json`](evidence/retry_summaries.json) | `c1e4da020c5272d32eebd5bf1c6911700f7d3a64fbe43dfc0372b22c76105b54`; exactly one unchanged retry result per unresolved handle |
| [`evidence/browser_fallback.pdf`](evidence/browser_fallback.pdf) | `d57a60299dd7b2dfd002de544cc36cd636e70c6252da4a554c6aa8a98d0a6787`; contact shells are negative observations and the temporary-tab cleanup result is zero |
| [Iteration 3 RES](../research/iter3/RES.md) | `4d09296fe5ff9b367a467387c2218d8a381e0c19dfc3446cbeaa51a8a463a9fa`; cross-time continuity, counter-evidence, exact repair limits, and unresolved dispositions |
| Direct owner Telegram observation, source task `01a03eef-e770-7271-82e3-727586c7d274`, 2026-08-27 | Exact owner text: “сам проверил в телешрам, таких сообществ больше нет, kzqacommuninty и mobile_developers_kz”. The typo `kzqacommuninty` is normalized to the unique catalog handle `kzqacommunity`. Combined with RES3 historical binding, this is independent same-community death evidence, not archive approval |

Exact `datanomika` package — one structural repair, no copy change:

| Field | Old → new under G2 |
|-------|--------------------|
| collection | `groups` → `channels` |
| `category` | `data-analytics` → field absent (group-only field) |
| `name` | `Datanomika` → unchanged |
| `handle` | `datanomika` → unchanged |
| `description` | `Data visualization, dashboards, business intelligence` → unchanged |
| `description_ru` | `О визуализации данных, интерактивной отчетности, BI` → unchanged |
| `member_count` | current pre-repair value → no direct G2 write; replace only if the mandatory retry observes an integer |
| `last_verified` | current pre-repair value → no direct G2 write; update only from the mandatory verified retry |

Exact `kzquake` package — one atomic K-coherent repair; partial K-min approval is rejection:

| Field | Old → new under G2 |
|-------|--------------------|
| collection | `bots` → `channels` |
| `category` | absent → absent |
| `name` | `KZ Quake Bot` → `Землетрясения \| Казахстан` |
| `handle` | `kzquake` → unchanged |
| `description` | `Earthquake monitoring in Kazakhstan` → unchanged |
| `description_ru` | `Бот следит за землетрясениями в КЗ` → `Оперативные сообщения о землетрясениях на территории Казахстана` |
| `member_count` | current pre-repair value → no direct G2 write; replace only if the mandatory retry observes an integer |
| `last_verified` | current pre-repair value → no direct G2 write; update only from the mandatory verified retry |

#### G2 owner death evidence binding

The owner observation supplies the current external death fact while RES3 supplies the exact
historical-record identity. The combination satisfies AC-4's independent same-community death
evidence threshold for proposal:

| Entry | Historical binding | Current death observation | Exact evidence-safe disposition before verdict |
|-------|--------------------|---------------------------|-----------------------------------------------|
| `mobile_developers_kz` | RES3 binds the catalog row to the 2017 `Mobile Developers KZ` repository record under exact handle `mobile_developers_kz` | The owner named the exact handle after a direct Telegram check and stated the community no longer exists | Exact archive candidate; every field remains unchanged until exact G2. `mobile_dev_kz` remains an unbound alternative and is not a repair |
| `kzqacommunity` | RES3 binds the catalog row to the historical `KZ QA community` through repository history and archived exact-handle/peer evidence | The owner stated the named community no longer exists; the one-character-order typo is explicitly normalized to the unique catalog handle `kzqacommunity` | Exact archive candidate; every field remains unchanged until exact G2. No replacement or directory-derived count/date is authorized |

The observation itself did not name the archive command, exact `died_on`, exact reason,
`evidence_ref`, or rollback and therefore was not the semantic G2 verdict. G0, G1, and
“доделаывайте” also did not substitute for it; the distinct bound verdict recorded above supplies
the required exact approval.

Exact `mobile_developers_kz` package — move the complete unchanged live record into archive:

| Field | Old → new under G2 |
|-------|--------------------|
| collection | `groups` → removed from live `groups`; complete record appended to `archive` |
| `name` | `Mobile Developers KZ` → unchanged |
| `handle` | `mobile_developers_kz` → unchanged |
| `description` | `Mobile app developers community` → unchanged |
| `description_ru` | `Группа для мобильных разработчиков` → unchanged |
| `category` | `mobile` → unchanged in archived record |
| `last_verified` | `2026-01-30` → unchanged in archived record |
| `member_count` | absent → absent |
| `type` | absent → `groups` |
| `died_on` | absent → `2026-08-27` |
| `reason` | absent → `Owner verified in Telegram on 2026-08-27 that the historical Mobile Developers KZ community no longer exists.` |
| command `evidence_ref` | absent → `tasks/TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding` |

Exact `kzqacommunity` package — move the complete unchanged live record into archive:

| Field | Old → new under G2 |
|-------|--------------------|
| collection | `groups` → removed from live `groups`; complete record appended to `archive` |
| `name` | `QA Community KZ` → unchanged |
| `handle` | `kzqacommunity` → unchanged |
| `description` | `QA specialists community` → unchanged |
| `description_ru` | `Сообщество QA специалистов Казахстана` → unchanged |
| `category` | `qa-testing` → unchanged in archived record |
| `last_verified` | `2026-01-30` → unchanged in archived record |
| `member_count` | `762` → unchanged in archived record |
| `type` | absent → `groups` |
| `died_on` | absent → `2026-08-27` |
| `reason` | absent → `Owner verified in Telegram on 2026-08-27 that the historical KZ QA community no longer exists.` |
| command `evidence_ref` | absent → `tasks/TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding` |

The approved `datanomika` action has completed successfully and must not run again. Its actual raw
summary path is the external snapshot path recorded above; that result, not the earlier generic
planning-time temporary path, is part of the current candidate baseline.

Each retained repair result must be `classification=verified`, `declared_type=channels`,
`observed_type=channels`, and `target_bound=true`. A missing count is acceptable; only an
actually observed integer may replace the preserved count. Do not copy any research/directory
count.

Resume at `kzquake` only. First require current `data/communities.json` SHA-256
`628095507c7f9b435fb11d5e1b49177179846608bd3b6f930e365562173be27d`; any drift is a collision
STOP. Create a new unique external snapshot root and copy the current full data bytes into it:

```powershell
$g2KzquakeResumeGuid = [guid]::NewGuid().ToString("N")
if ($g2KzquakeResumeGuid -cnotmatch '\A[0-9a-f]{32}\z') { throw "Invalid kzquake snapshot GUID" }
$g2KzquakeResumePrefix = "E:\TEMP\TFW-4-phase-d-g2-kzquake-resume-"
$g2KzquakeResumeRoot = $g2KzquakeResumePrefix + $g2KzquakeResumeGuid
if (Test-Path -LiteralPath $g2KzquakeResumeRoot) { throw "Kzquake snapshot root already exists" }
New-Item -ItemType Directory -Path $g2KzquakeResumeRoot -ErrorAction Stop | Out-Null
$g2KzquakeResumeRoot = (Resolve-Path -LiteralPath $g2KzquakeResumeRoot -ErrorAction Stop).Path
if (-not [System.IO.Path]::IsPathRooted($g2KzquakeResumeRoot)) { throw "Kzquake snapshot root is not absolute" }
if (-not $g2KzquakeResumeRoot.StartsWith($g2KzquakeResumePrefix, [System.StringComparison]::Ordinal)) { throw "Kzquake snapshot root escaped its exact prefix" }
if ((Split-Path -Leaf $g2KzquakeResumeRoot) -cne ("TFW-4-phase-d-g2-kzquake-resume-" + $g2KzquakeResumeGuid)) { throw "Kzquake snapshot leaf mismatch" }
if (@(Get-ChildItem -LiteralPath $g2KzquakeResumeRoot -Force -ErrorAction Stop).Count -ne 0) { throw "Kzquake snapshot root is not empty" }
Copy-Item -LiteralPath "data/communities.json" -Destination (Join-Path $g2KzquakeResumeRoot "communities.json") -ErrorAction Stop
```

The root is built only from the exact fixed prefix and the locally generated, regex-bound GUID;
no wildcard, environment-derived root, or untrusted expansion is permitted. Before mutation, also
write `candidate.json` in that same root with the complete current
`kzquake` record, `collection=bots`, index `0`, current `archive`, current
`meta.last_updated=2026-08-27`, the resolved snapshot paths, data byte length, and the exact
pre-candidate SHA-256 above. Verify that the copied bytes have that same hash and that the snapshot
root contains exactly `communities.json` and `candidate.json` before mutation. If either snapshot
write is incomplete, the record/index/archive/meta differ, or a hash differs, stop before mutation.

Reapply exactly the already-approved atomic `kzquake` package and no other data change. Then run
exactly one fresh validator process, with its raw output inside the new snapshot root:

```powershell
python -X utf8 scripts/validate_links.py --handle kzquake --update --summary-json "$g2KzquakeResumeRoot\raw_summary.json"
```

No plain-mode fallback and no second fresh invocation is allowed. Success remains exactly exit
`0`, one `kzquake` result, `classification=verified`, `declared_type=channels`,
`observed_type=channels`, `target_bound=true`, no foreign handle, and a valid raw JSON document.
Only an observed integer may replace the preserved count; the validator-owned date/metadata must
be `2026-08-27`. On any process error, missing/malformed raw JSON, foreign handle, or predicate
mismatch, restore only `kzquake` and only its command-owned metadata from the fresh
`candidate.json`, verify byte-equivalent candidate state, preserve the successful `datanomika`
result and its raw bytes, record the failure, mark `kzquake` `UNRESOLVED`, and STOP before either
archive, schema/generator, EV/RF, G3, or G4.

After exact `kzquake` success and before either archive, create the single durable
`evidence/g2_recheck_summaries.json`. Its `records` array is ordered `datanomika`, `kzquake`; each
record contains the exact `handle`, resolved external source path, `raw_byte_length`, lowercase
`raw_sha256`, `raw_base64`, and the decoded `summary` object. For `datanomika`, ingest the exact
734 bytes at
`E:\TEMP\TFW-4-phase-d-g2-datanomika-93ab85a59ed141e695f1ba12572fee96\raw_summary.json`, whose
SHA-256 is `39ef51989d671cd5f339b77fbe55a7b387ff7005e24276bad2d29ab27de9f939`; do not reconstruct it
from console text or current data. For both records, base64-decode and require byte length/hash
identity, decode strictly as UTF-8, parse JSON, and require deep equality with the stored
`summary`. Preserve every decoded result field/classification unchanged and do not rewrite any
original G1 artifact. Aggregate construction or verification failure preserves both external raw
documents and any already-verified repair state but STOPs before archives and downstream gates.

The archive implementation derives `died_on` from Python's local `date.today()` and does not
accept a historical-date flag. Therefore, immediately before either archive command, require:

```powershell
python -c "from datetime import date; d=date.today().isoformat(); print(d); raise SystemExit(0 if d == '2026-08-27' else 1)"
```

If that gate is non-zero, stop and return to `/tfw-plan tfw-4`; do not write a later date and do
not backdate manually. If it is zero and exact G2 exists, create the first archive candidate's
fresh external snapshot root with the same PS5-compatible safety pattern:

```powershell
$g2MobileArchiveGuid = [guid]::NewGuid().ToString("N")
if ($g2MobileArchiveGuid -cnotmatch '\A[0-9a-f]{32}\z') { throw "Invalid mobile archive snapshot GUID" }
$g2MobileArchivePrefix = "E:\TEMP\TFW-4-phase-d-g2-archive-mobile_developers_kz-"
$g2MobileArchiveRoot = $g2MobileArchivePrefix + $g2MobileArchiveGuid
if (Test-Path -LiteralPath $g2MobileArchiveRoot) { throw "Mobile archive snapshot root already exists" }
New-Item -ItemType Directory -Path $g2MobileArchiveRoot -ErrorAction Stop | Out-Null
$g2MobileArchiveRoot = (Resolve-Path -LiteralPath $g2MobileArchiveRoot -ErrorAction Stop).Path
if (-not [System.IO.Path]::IsPathRooted($g2MobileArchiveRoot)) { throw "Mobile archive snapshot root is not absolute" }
if (-not $g2MobileArchiveRoot.StartsWith($g2MobileArchivePrefix, [System.StringComparison]::Ordinal)) { throw "Mobile archive snapshot root escaped its exact prefix" }
if ((Split-Path -Leaf $g2MobileArchiveRoot) -cne ("TFW-4-phase-d-g2-archive-mobile_developers_kz-" + $g2MobileArchiveGuid)) { throw "Mobile archive snapshot leaf mismatch" }
if (@(Get-ChildItem -LiteralPath $g2MobileArchiveRoot -Force -ErrorAction Stop).Count -ne 0) { throw "Mobile archive snapshot root is not empty" }
Copy-Item -LiteralPath "data/communities.json" -Destination (Join-Path $g2MobileArchiveRoot "communities.json") -ErrorAction Stop
```

Before the `mobile_developers_kz` mutation, write `candidate.json` in that root with the complete
current live record, its current `groups` index, the complete current `archive`, current
`meta.last_updated`, resolved snapshot paths, and the pre-candidate data byte length and SHA-256.
Require the copied `communities.json` hash to equal that recorded pre-candidate hash and the root
to contain exactly `communities.json` and `candidate.json`; otherwise stop before mutation. Then
run the already-approved command unchanged:

```powershell
python scripts/validate_links.py --archive mobile_developers_kz --reason "Owner verified in Telegram on 2026-08-27 that the historical Mobile Developers KZ community no longer exists." --evidence-ref "tasks/TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding" --owner-approved
```

Only after that candidate meets every existing postcondition, create the second archive
candidate's fresh external snapshot root:

```powershell
$g2KzqaArchiveGuid = [guid]::NewGuid().ToString("N")
if ($g2KzqaArchiveGuid -cnotmatch '\A[0-9a-f]{32}\z') { throw "Invalid KZ QA archive snapshot GUID" }
$g2KzqaArchivePrefix = "E:\TEMP\TFW-4-phase-d-g2-archive-kzqacommunity-"
$g2KzqaArchiveRoot = $g2KzqaArchivePrefix + $g2KzqaArchiveGuid
if (Test-Path -LiteralPath $g2KzqaArchiveRoot) { throw "KZ QA archive snapshot root already exists" }
New-Item -ItemType Directory -Path $g2KzqaArchiveRoot -ErrorAction Stop | Out-Null
$g2KzqaArchiveRoot = (Resolve-Path -LiteralPath $g2KzqaArchiveRoot -ErrorAction Stop).Path
if (-not [System.IO.Path]::IsPathRooted($g2KzqaArchiveRoot)) { throw "KZ QA archive snapshot root is not absolute" }
if (-not $g2KzqaArchiveRoot.StartsWith($g2KzqaArchivePrefix, [System.StringComparison]::Ordinal)) { throw "KZ QA archive snapshot root escaped its exact prefix" }
if ((Split-Path -Leaf $g2KzqaArchiveRoot) -cne ("TFW-4-phase-d-g2-archive-kzqacommunity-" + $g2KzqaArchiveGuid)) { throw "KZ QA archive snapshot leaf mismatch" }
if (@(Get-ChildItem -LiteralPath $g2KzqaArchiveRoot -Force -ErrorAction Stop).Count -ne 0) { throw "KZ QA archive snapshot root is not empty" }
Copy-Item -LiteralPath "data/communities.json" -Destination (Join-Path $g2KzqaArchiveRoot "communities.json") -ErrorAction Stop
```

Before the `kzqacommunity` mutation, write the same `candidate.json` fields for its then-current
complete live record, `groups` index, complete archive and metadata. Require byte length/hash
identity for its copied `communities.json` and exactly the same two-file root invariant; otherwise
stop before mutation. Then run the already-approved command unchanged:

```powershell
python scripts/validate_links.py --archive kzqacommunity --reason "Owner verified in Telegram on 2026-08-27 that the historical KZ QA community no longer exists." --evidence-ref "tasks/TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding" --owner-approved
```

For each archive, require exit `0`, removal of exactly the named live record, one appended archive
record preserving every original field and adding only `type=groups`, `died_on=2026-08-27`, and
the exact reason above, plus `meta.last_updated=2026-08-27`. The current implementation validates
and prints `--evidence-ref` but does not store it in catalog JSON, so EV must retain the exact
command, output, owner verdict, and this durable TS reference; no new catalog field is invented.

The approved full order was `datanomika`, `kzquake`, `mobile_developers_kz`, then
`kzqacommunity`; the historical retained checkpoint resumed at `kzquake` because `datanomika`
was complete. Execution subsequently completed under this fail-closed boundary. Before each candidate, retain its exact current record, live collection/index,
archive state, and `meta.last_updated`. If a repair mutation is partial, its command fails to
produce valid raw JSON, or any required result field differs, restore only that repair candidate
to its pre-candidate fields/collection and restore only its command's metadata change; preserve
all other G1/cursor/user changes, mark it `UNRESOLVED`, and stop. If an archive command fails or
its exact postconditions differ, remove only its partial archive result if present, restore the
complete candidate at its original live index plus only its command's metadata change from the
pre-candidate snapshot, preserve already successful earlier candidates, and stop. Never restore
the whole data file, touch either merge stash, continue to a later candidate after failure, or
enter schema/generator, EV/RF, G3, or release work on a failed candidate.

Approved exact package wording — G2 and nothing later:

> G2: одобряю четыре exact disposition: (1) `datanomika` — перенести `groups` → `channels`,
> удалить поле `category`, остальные текстовые поля и `handle` не менять; `member_count` и
> `last_verified` менять только по обязательному exact post-move retry; (2) `kzquake` — одним
> атомарным изменением перенести `bots` → `channels`, изменить `name` с `KZ Quake Bot` на
> `Землетрясения | Казахстан`, оставить `handle: kzquake` и `description: Earthquake monitoring in Kazakhstan`, изменить `description_ru` с `Бот следит за землетрясениями в КЗ` на
> `Оперативные сообщения о землетрясениях на территории Казахстана`; `member_count` и
> `last_verified` менять только по обязательному exact post-move retry. При неполном изменении
> или результате retry, отличном от `verified / channels / channels / target_bound=true`,
> восстановить только соответствующую запись по pre-candidate snapshot, оставить её
> `UNRESOLVED` и остановиться; (3) `mobile_developers_kz` — архивировать полную неизменённую
> запись с `type=groups`, `died_on=2026-08-27`, reason `Owner verified in Telegram on 2026-08-27 that the historical Mobile Developers KZ community no longer exists.` и evidence_ref
> `tasks/TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding`;
> `mobile_dev_kz` не считать repair; (4) `kzqacommunity` — архивировать полную неизменённую
> запись с `type=groups`, `died_on=2026-08-27`, reason `Owner verified in Telegram on 2026-08-27 that the historical KZ QA community no longer exists.` и тем же evidence_ref. Архивные команды
> выполнять только если Python local date равна `2026-08-27`; при другом дне остановиться без
> мутации. При любой ошибке восстановить только текущего кандидата и его metadata change по
> pre-candidate snapshot, сохранить успешные предыдущие результаты и остановиться. Это только
> G2, не G3 `/kz-release` и не G4 tag/push.

That exact semantic verdict remains in force. Execution subsequently completed every G2
disposition under those predicates: `datanomika` and `kzquake` are verified channels;
`mobile_developers_kz` and `kzqacommunity` are exact approved archive records; the durable
byte-preserving aggregate is
[`evidence/g2_recheck_summaries.json`](evidence/g2_recheck_summaries.json), SHA-256
`950ca60b7779e8f5f4c1e2e0cdf4804cf16f0079d08701163a90f0cd239ac489`. Final data contains 62
live entries plus two archives at common date `2026-08-27`, SHA-256
`b773a69d8f828b3732d387f797a5c41cbd37376d62be18e559b9a39d7d325de3`; generated `README.md`
SHA-256 is `58266a695a3e50f0997c9b7adcbe349853942d68a7ab91a06060113fa0ee3697`.

Binding REVIEW `REVISE` independently verified these G1/G2 facts and found only a lifecycle
defect: EV/RF were written before AC6–AC8 and the final publication outcome. Therefore the
existing EV, RF, REVIEW, and review stages are preserved as historical checkpoints, authoritative
status remains `ONB`, and `/tfw-handoff tfw-4` resumes at AC6 rather than rerunning G1/G2.

#### Exact G3 Approval and AC6 Handoff

Approval record — ✅ owner saubakirov, 2026-08-27. In source task
`01a03eef-e770-7271-82e3-727586c7d274`, the direct verdict “одобряю” immediately answered this
exact request:

> Одобряю G3 `/kz-release` для TFW-4: подготовить локальный snapshot `data-2026-08-27`,
> обновить корневой CHANGELOG и создать локальный path-scoped release commit. Остановиться до
> создания тега и push. Это не G4.

This activates the already-approved AC6 branch and changes no scope, AC, success predicate,
rollback rule, DoD/DoF item, principle, phase, or frozen Master baseline. The next Executor must:

1. re-read this TS, `RELEASE.md`, `.claude/commands/kz-release.md`, binding REVIEW and stages,
   current `ONB` status/journal, and the accepted final G1/G2 evidence;
2. fail closed on any checkout drift, tag conflict, incomplete evidence, schema failure, README
   currency failure, or path-scope mismatch;
3. execute `/kz-release` for AC6 only: prepare local snapshot `data-2026-08-27`, update root
   `CHANGELOG.md`, and create exactly one local release commit with explicit reviewed paths;
4. present the exact commit hash/diff, proposed tag, branch, and remote, then hard-stop.

No tag, push, GitHub Release, force/ref mutation, or other publication action is authorized.
G4 requires a fresh exact owner verdict on the prepared commit/tag/branch/remote package.

#### G3 Pre-staging Path Matrix and Approved Scope Gate

The G3 Executor passed evidence, date, schema, README-currency, tag-conflict, protected-state, and
changelog gates, then stopped before `git add`. Current state is `HEAD=97dd429`, cached paths `0`,
unmerged paths `0`, no local `data-2026-08-27` tag, no commit, and no push. The prepared root
changelog is preserved at SHA-256
`05480f03ab9c42e20159afb64ecaf91c4ca669dfa84f6aaa37c3100ead190b36`; accepted data/README bytes
remain SHA-256 `b773a69d8f828b3732d387f797a5c41cbd37376d62be18e559b9a39d7d325de3` and
`58266a695a3e50f0997c9b7adcbe349853942d68a7ab91a06060113fa0ee3697`.

The exact current dependency matrix is:

| Class | Exact current paths | Git state at stop | Reviewed authority / needed by | Allowed disposition |
|-------|---------------------|-------------------|--------------------------------|---------------------|
| AC6 result | `CHANGELOG.md`; `README.md`; `data/communities.json` | 3 modified tracked paths | G3 authorizes the evidence-bound changelog; binding Phase D REVIEW verifies data/README; these are the dated catalog result | Second commit only, exactly these three paths, after an authorized trace checkpoint |
| Phase D trace/evidence | `phase-d/{HL__phase-d__live_sweep_release.md,TS__phase-d__live_sweep_release.md,RF__phase-d__live_sweep_release.md,REVIEW__phase-d__live_sweep_release.md,status.md}`; `phase-d/evidence/{EV__phase-d__live_sweep_release.md,browser_fallback.pdf,cursor_kz_supplement.json,g2_recheck_summaries.json,live_sweep_summary.json,retry_summaries.json}`; `phase-d/review/{map.md,verify.md,judge.md}` | 13 untracked; `status.md` modified tracked; 14 total | Owner-approved HL/TS; binding REVIEW `REVISE` verifies the historical RF/EV and all G1/G2 bytes; status is live authority | First trace checkpoint only; no byte rewrite except post-verdict Coordinator-owned HL/TS/status gate binding |
| Current task journal | `journal/20260827-081045__handoff__saubakirov.md`; `20260827-082200__transition__saubakirov.md`; `20260827-083156__handoff__saubakirov.md`; `20260827-092520__transition__saubakirov.md`; `20260827-094217__handoff__saubakirov.md`; `20260827-121244__handoff__saubakirov.md` | 6 untracked | Immutable v2 lifecycle/handoff history referenced by Phase D status/EV; the sixth event binds the post-verdict handoff | First trace checkpoint only; bytes immutable after creation |
| Phase C accepted predecessor | `phase-c/{HL__phase-c__pipeline_tooling.md,TS__phase-c__pipeline_tooling.md,REVIEW__phase-c__pipeline_tooling.md}`; `phase-c/review/{map.md,verify.md,judge.md}`; `phase-c/review/iter2/{map.md,verify.md,judge.md}`; `phase-c/review/iter3/{map.md,verify.md,judge.md}`; `phase-c/review/iter4/{map.md,verify.md,judge.md}` | 15 untracked | Final Iteration 4 `APPROVE`; Phase D HL links the binding REVIEW, whose history requires all four stage sets | First trace checkpoint only; bytes immutable |
| Phase B accepted predecessor | `phase-b/{HL__phase-b__contract_docs.md,TS__phase-b__contract_docs.md,REVIEW__phase-b__contract_docs.md}`; `phase-b/review/{map.md,verify.md,judge.md}`; `phase-b/review/iter2/{map.md,verify.md,judge.md}` | 9 untracked | Final repeat `APPROVE`; required by Phase C HL and REVIEW/TS closure | First trace checkpoint only; bytes immutable |
| Phase A accepted predecessor | `phase-a/{HL__phase-a__baseline_cleanup.md,TS__phase-a__baseline_cleanup.md,RF__phase-a__baseline_cleanup.md,REVIEW__phase-a__baseline_cleanup.md}`; `phase-a/evidence/EV__phase-a__baseline_cleanup.md`; `phase-a/review/{map.md,verify.md,judge.md}` | 8 untracked | Binding `APPROVE`; completes the task's A→B→C→D trace rather than leaving the first phase outside history | First trace checkpoint only; bytes immutable |
| Research control and iterations | `research/iterations.yaml`; for each of `research/iter1`, `iter2`, and `iter3`: `{1_briefing.md,2_gather.md,3_extract.md,4_challenge.md,RES.md}` | 15 untracked stage/RES files; `iterations.yaml` modified tracked; 16 total | Iterations 1–2 are accepted Phase C inputs; Iteration 3 is an accepted Phase D G2 input. Full stage sets are required by TFW file-existence semantics | First trace checkpoint only. Before staging, Coordinator must change only `iterations.yaml` from stale current A5-open projection to the already-recorded A5 approved/closed truth; all RES/stage bytes remain immutable |
| Existing HEAD support | Master HL; task/phase ONB/status/result/evidence paths already in HEAD; `KNOWLEDGE.md`; `TECH_DEBT.md`; task route/index; framework and project command/release authorities | Tracked and unchanged | Supplies the local-link and authority targets already committed | Exclude from both commits unless a listed AC6 result path; equality to HEAD is a gate |
| External/user-owned migration state | `.agents/**` and every other dirty/untracked path outside the enumerated closure | Untracked or otherwise user-owned | Not required by any closure edge and protected by Phase D | Exclude from both commits |

The six trace/control classes now contain exactly 68 paths: Phase A 8 + Phase B 9 + Phase C 15
+ research 16 + Phase D 14 + journal 6. Their local Markdown references resolve either inside
that set or to unchanged HEAD. The AC6 release commit remains a separate exact three-path commit.

Classification:

1. A three-path result-only commit is syntactically link-closed but fails the project command's
   incomplete-task-trace refusal and P1.
2. A single 70-path expanded release commit is link-closed but violates Scope §2, the Phase D
   budget at §4, AC6's reviewed Phase D/result boundary, and Failure §7's scope-overrun rule.
3. A 68-path trace checkpoint followed by the exact three-path AC6 release commit is the only
   truthful design. It was not FREE, so the Coordinator requested an exact owner scope amendment.
   Owner saubakirov approved it on 2026-08-27 through the direct verdict recorded below.

Exact package presented to the owner, with no implied G4 authority:

> Одобряю G3 pre-staging scope amendment для TFW-4 в два локальных коммита. Первый — один
> path-scoped trace checkpoint с subject
> `[codex/TFW-4/trace/executor] checkpoint reviewed task trace before release`: включить ровно
> перечисленные в Phase D TS классы Phase A (8), Phase B (9), Phase C (15), research (16),
> Phase D (14), пять существующих task journal events и один новый post-verdict handoff event —
> всего 68 paths; не включать `data/communities.json`, `README.md` или `CHANGELOG.md`. Перед
> staging разрешаю Coordinator изменить только `research/iterations.yaml`: установить
> `open_amendments: []`, перенести A5 в `closed_amendments` со status
> `APPROVED — saubakirov, 2026-08-26` согласно frozen Master и сохранить iter1–3 `complete`; RES
> и stage files не менять. Второй — ровно один AC6 release commit с subject
> `[codex/TFW-4/release/executor] record verified snapshot data-2026-08-27` и только тремя paths:
> `CHANGELOG.md`, `README.md`, `data/communities.json`. После второго commit остановиться. Это не
> G4: tag и push запрещены.

Bound verdict — ✅ owner saubakirov, 2026-08-27. In source task
`01a03eef-e770-7271-82e3-727586c7d274`, the owner's direct response immediately after the exact
package was: “Без разницы мне, достигни цели, которую я поставил. Задачу доведи до логического
конца, так чтобы осталось только сделать пуш.” This delegates the enumerated path-matrix choice
and affirmatively selects the recommended safe two-commit design. It authorizes exactly:

1. the Coordinator-only `research/iterations.yaml` A5 reconciliation, this HL/TS/status binding,
   and one immutable post-verdict handoff event;
2. one path-scoped 68-path trace checkpoint with subject
   `[codex/TFW-4/trace/executor] checkpoint reviewed task trace before release`, excluding
   `data/communities.json`, `README.md`, and `CHANGELOG.md`;
3. after exact cached/committed allowlist validation, one AC6 release commit with subject
   `[codex/TFW-4/release/executor] record verified snapshot data-2026-08-27` and only
   `CHANGELOG.md`, `README.md`, and `data/communities.json`.

This is a Phase D TS/G3 execution-scope amendment, not a Master §12 amendment. It supplies the
extra trace commit, exact cross-phase/research inclusion, narrow budget/read-only override, and
A5 control correction that the prior G3 did not supply. No broad staging or additional path is
authorized; all G1/G2 evidence/result bytes and all RES/stage bytes remain unchanged.

The same verdict's phrase “так чтобы осталось только сделать пуш” expresses the desired local
endpoint, but it cannot satisfy AC7's exact-current-commit gate before the release commit exists.
`RELEASE.md` and `/kz-release` require the owner to review the prepared exact commit hash, diff,
evidence, tag, branch, and remote after AC6 and approve at that moment. Therefore the Executor
must hard-stop after the second commit and return: exact hash and parent, exact three-path list,
subject/dates, branch `master`, configured remote `origin`, unchanged evidence hashes, schema and
README-currency results, and absent/conflict-free `data-2026-08-27` tag. A post-commit Coordinator
decision is required before any local tag. No tag, push, ref deletion/move, force, or retry is
authorized by this handoff; push remains explicitly forbidden.

### Inherited Quality Contract (verbatim from Master HL §7.1 at `d31e60d`)

- No placeholders. No `TODO`, no stub, no “implement later”. `.tfw/README.md`
  § Completeness Over Speed.
- No hardcoded derived value in any file — counts, dates, category lists.
- `README.md` is never hand-edited. Change the generator or the data.
- No file under `.tfw/` is touched except `project_config.yaml` and
  `knowledge_state.yaml`.
- No `/tfw-*` adapter file in `.claude/commands/` is modified.
- Every commit follows `conventions.md` §4:
  `[agent/task/scope/role] summary`, with `agent` = the lowercase AI product name
  established by the actual executing product/adapter context (`codex` for Codex executor
  commits; `claude-code` for Claude Code executor commits), `task` = the task ID, and
  `role` = the acting TFW role.
- `git push` only on explicit owner approval given at that moment.
- Python: standard library only. The project's sole declared dependency is `requests`
  (`project_config.yaml` → `stack.dependencies`), and no current script uses it — do
  not add one. Type hints and docstrings in the existing style; ASCII-tagged output
  (`[OK]`, `[FAIL]`, `[INFO]`) to stay readable in a Windows console.
- Scripts exit non-zero on error, zero on success. `/kz-release` and CI depend on it.

## 7. Definition of Failure

- ❌ Any network call, Telegram request, Chrome/browser/authenticated-client action,
  `/kz-stats` or `/kz-release` execution, live/update/archive validator run, production
  data/README/changelog/release mutation, release commit, tag, or push occurs before explicit
  Phase D approval and the applicable later owner gate.
- ❌ A catalog fact is written without contemporaneous target-specific observation; a count/date,
  identity, type, continuity, replacement, reason, or death is estimated, remembered, or inferred.
- ❌ The raw full-sweep summary is absent/malformed, fails exact live-handle coverage, or is
  replaced by console prose, Phase C fixtures, a synthetic row, or reconstructed evidence.
- ❌ An unresolved result is not retried once, or a repeated failure/contact shell/non-target/type
  mismatch/no-count state is treated as proof of death.
- ❌ Browser fallback accepts a generic contact shell, opens/accumulates separate tabs per handle,
  captures secrets/unrelated user state, ends without closing the temporary tab, or lacks a final
  zero-temporary-tab confirmation.
- ❌ A repair/archive occurs without exact owner approval and the required continuity/death
  evidence; an entry is deleted rather than archived; an unresolved entry is mutated to force
  release eligibility.
- ❌ Any surviving live entry lacks positive evidence for the common snapshot date, or release
  preparation proceeds with unresolved, partial, missing, or cross-date evidence.
- ❌ `README.md` is hand-edited, schema/generator/currency gates fail, or the final diff
  contains editorial/non-evidenced catalog changes.
- ❌ A version is bumped; `RELEASE.md`, `.tfw/VERSION`,
  `.tfw/CHANGELOG.md`, scripts, command definitions, adapters, master/research/Phase A–C
  artifacts, or any other out-of-scope path is modified.
- ❌ TD-5, TD-10, or TD-11 is fixed, rewritten, closed, or used to justify adjacent changes.
- ❌ A local release commit includes unrelated dirty work, uses broad staging, misleading
  attribution/backdating, an unsupported changelog claim, or a conflicting tag.
- ❌ A tag/push/publication occurs without fresh approval of the exact commit/tag/branch/remote,
  or drifted state is published under stale approval.
- ❌ A tag is forced/moved/deleted automatically, a push is forced, a failed/partial publication
  is called successful, or any retry/rollback outside the exact TS-authorized candidate boundary
  occurs without a new owner decision. The one replacement UTF-8 `kzquake` invocation and its
  candidate-only rollback are the only reconciled exception already covered by G2.
- ❌ The file/LOC budget or declared path scope is exceeded without an explicit new owner decision;
  delegated authority is not approval for an overrun.
- ❌ TFW-4 is marked complete, D15/TD resolution is recorded, or a completion RF is written while
  any relevant Master DoD, AC-7 publication, evidence, or owner-decision gate remains open.

On any honesty, authority, evidence-loss, privacy, archive, or publication failure, stop
immediately, preserve the exact state/output, and escalate to the owner. Do not continue or create
compensating evidence. For an ordinary pre-commit data/generation defect, restore only the exact
affected Phase D path/entry from the ONB snapshot, record the retraction, and rerun every dependent
gate. After a local commit or tag, preserve history/refs and await owner direction; never reset,
amend, delete, move, or force automatically.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Full update partially persists verified records before unresolved exit 1 | Treat raw summary plus JSON diff as truth; retain both before triage and never equate process exit with transaction rollback |
| Rate limiting produces correlated false failures | Preserve delivered throttle/backoff, perform the one exact retry, detect systemic patterns, and pause without archiving |
| Browser fallback bypasses authoritative identity or leaks user session state | Target-specific required fields, one sequential temporary tab, secret exclusion, bundled capture, close plus zero-tab confirmation |
| Authenticated resolution proves a peer but not historical continuity | Require peer kind and continuity evidence; otherwise leave unresolved |
| General owner approval is reused for an exact archive | EV records separate per-entry evidence and approval; command requires evidence reference plus owner-approved flag |
| Sweep spans dates or repairs change the live handle set | Reconcile against final handles and one evidence-derived date; recheck affected entries or block snapshot |
| Dirty checkout contaminates rollback/staging/commit | ONB exact byte/hash snapshots, explicit paths, no HEAD reconstruction, no broad staging/restore |
| Root changelog overstates refreshed/archived changes | Derive every dated bullet from EV/raw summaries and exact final diff |
| Local commit is mistaken for released state | AC-6 hard stop, absent-tag proof, AC-7 separate fresh exact approval |
| Tag succeeds locally but push fails | Preserve partial state and actual output; no delete/force/retry without owner |
| Evidence volume exceeds budget | Preserve the three immutable G1 artifacts and add only the one raw cursor supplement plus one bundled G2 recheck JSON; stop for owner scope decision if reviewability cannot fit the 14-file phase bound |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|------------------|-------------------|
| `data/communities.json` | Phases B–C | Preserve North Star/schema/archive contracts; Phase D alone writes live observed facts and populated approved archives |
| `README.md` | Phase C | Phase C presentation stays generator-owned; Phase D diff is only the deterministic result of observed data |
| `CHANGELOG.md` | Phase B | Preserve project/framework separation; Phase D creates the first evidence-backed dated catalog snapshot |
| `KNOWLEDGE.md` | Phases A–C docs | Add D15 once after actual behavior; do not duplicate/rewrite D8–D14 |
| `TECH_DEBT.md` | Phases A–C docs | Only TD-2/TD-4 may transition from Phase D evidence; TD-5/TD-10/TD-11 remain untouched |
| `tasks/TFW-4__showcase_reorg/*/status.md`, task journal, `tasks/00-INDEX.md` | Every phase | Preserve Phase A–C `DONE` statuses; advance only the real Phase D lifecycle in its own status, append immutable events, and regenerate the non-authoritative projection |

---

*TS — TFW-4 / Phase D: Live Sweep & First Release | 2026-08-27*

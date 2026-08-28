# TS — 20260828-201343__catalog_intake_commands / Phase B: Clean candidate run and catalog integration

> **Date**: 2026-08-29
> **Author**: Coordinator (Codex)
> **Status**: ✅ APPROVED FOR HANDOFF — owner mandated autonomous Phase A then Phase B; exact apply approval remains absent
> **Parent HL**: [Master HL](../HL-20260828-201343__catalog_intake_commands.md)
> **Phase HL**: [Phase B HL](HL__phase-b__candidate_integration.md)
> **Predecessor Actual**: [Phase A RF](../phase-a/RF__phase-a__intake_engine.md)

---

## 1. Objective

Use the reviewed Phase A intake engine to run the sealed twenty-case holdout first, reconcile all
29 source occurrences and 28 unique candidates, and prepare a complete evidence-backed canonical
preview for the exact eligible ADD set. Before current owner approval, the phase must stop with
production catalog/projection bytes unchanged, a clean controlled worktree, an authoritative
Reviewer readiness audit, and one exact approval statement. The same lineage resumes later for the
bound apply, final verification, RF, and formal review.

## 2. Scope

### In Scope

- Verify and adopt exact task-controlled copies of the sealed discovery batch, owner note, full
  partition, and seal metadata while preserving both originals byte-for-byte.
- Derive deterministic task inputs from the sealed occurrence mapping and execute the twenty-case
  holdout before using calibration outcomes or running the full universe.
- Run non-mutating parse/probe through `scripts/kz_intake.py`; retain raw ledgers, observations,
  transport limitations, and source-to-occurrence provenance.
- Independently determine identity, liveness, peer type, live/archive/canonical/alias/cross-input
  duplicates, Kazakhstan relevance, IT/startup relevance, commerciality/spam risk, valid category,
  observed member count when present, verification date, and explicit EN/RU/KK copy.
- Assign every unique candidate exactly one proposed action (`add`, `reject`, `duplicate`, or
  `unresolved`) and retain a concrete evidence-linked reason for every non-addition.
- Build the complete bundle, staged source/projections, canonical preview, human rendering,
  payload/action digests, exact ADD IDs, controlled-path before/expected-after hashes, and action
  digest without mutating production.
- Run an independent readiness/copy audit in the one persistent Reviewer task. Use a safe advisory
  Antigravity `gemini-3.7-flash-high` plan+sandbox audit when available, without granting it
  mutation authority or precedence over the Reviewer.
- Transition Phase B to `BLOCKED` at the exact owner gate and send the Main Coordinator the
  complete readiness report and single exact statement for owner affirmation.
- After a later exact owner response, resume the same lineage to create the separate approval
  envelope, recheck all gates, apply exact staged bytes, verify/re-probe, write RF, and run formal
  `/tfw-review`.

### Out of Scope

- Any production catalog/projection mutation before exact current owner approval of the final
  payload and action projection.
- Creating or claiming the approval envelope from this TS, the broad add-all direction, a previous
  owner preference, the candidate notes, or an agent-authored owner name.
- Changing Phase A code, tests, parser/classifier behavior, command/skill bodies, schema/generator
  rules, or permanent fixtures in response to the holdout.
- Authenticated/private Telegram guessing, contacting community owners, posting, joining, sending,
  browser login, or other external mutation.
- Archiving existing entries, running a release, tagging, pushing, deploying, changing settings,
  or editing generated projections by hand.
- Editing, staging, deleting, moving, or claiming cleanliness for
  `D:/projects/KZ-IT-telegram-list/tasks/CANDIDATES-2026-08-28.md` or
  `C:/Users/c0rpa/obsidian/c0rp/c0rp/Untitled 1.md`.
- Formal Phase B approval before a bound apply receipt and complete RF exist.

## 3. Principles Check

| # | Principle (from Master HL §7) | Enforced by | Gate |
|---|---|---|---|
| P1 | Accuracy governs coverage | AC-2, AC-3, AC-6 | No candidate is added without target-bound current evidence and every uncertainty stays explicit |
| P2 | Observation and judgement stay separate | AC-2, AC-3 | Machine observations, editorial evidence, Reviewer ruling, and owner authority remain distinct artifacts |
| P3 | Preview before mutation | AC-4, AC-5, AC-6 | Exact staged bytes and digests exist before approval; production is hash-identical at the gate |
| P4 | Complete copies, enforced parity | AC-7 | Existing command parity/runtime contracts remain unchanged and pass final checks |
| P5 | Fail closed and account for every input | AC-1, AC-2 | 29 occurrences and 28 cases reconcile with no silent omission; ambiguous states are non-additions |
| P6 | Holdout evidence must be honest | AC-1 | The twenty-case run occurs first and any holdout-driven durable change invalidates the clean result |
| P7 | Generated output remains generated | AC-4, AC-6 | Expected and applied projections come only from the generator and pass currency checks |

## 4. Affected Files

### Production controlled paths — modifications permitted only after exact current approval

| File | Action | Description |
|---|---|---|
| `data/communities.json` | MODIFY CONDITIONALLY | Add only exact approved, still-eligible rows and mechanically rebind localization-review metadata |
| `README.md` | MODIFY CONDITIONALLY | Generator-owned English/GitHub projection |
| `index.md` | MODIFY CONDITIONALLY | Generator-owned English site projection |
| `ru/index.md` | MODIFY CONDITIONALLY | Generator-owned Russian projection |
| `kk/index.md` | MODIFY CONDITIONALLY | Generator-owned Kazakh projection |

### Task-local artifacts

| File | Action | Description |
|---|---|---|
| `phase-b/ONB__phase-b__candidate_integration.md` | CREATE | Executor onboarding and authority confirmation |
| `phase-b/evidence/` | CREATE | Exact source copies, ledgers, observations, judgements, preview, hashes, advisory records, and EV |
| `phase-b/review/readiness.md` | CREATE | Authoritative bounded Reviewer readiness/copy audit; not a formal REVIEW verdict |
| `phase-b/RF__phase-b__candidate_integration.md` | CREATE AFTER APPLY | Complete post-apply RF only; absent at the pre-approval blocker |
| `phase-b/review/{map,verify,judge}.md` | CREATE AFTER RF | Formal post-apply review traces |
| `phase-b/REVIEW__phase-b__candidate_integration.md` | CREATE AFTER RF | Formal Reviewer verdict |

**Budget:** 0 new production files, at most 5 production modifications, and no production code
change. Task-local TFW/evidence artifacts are additional, claim-driven, and bounded to this phase.
Any non-task path beyond the five controlled paths is a scope violation. Any engine or rule change
invalidates the current clean-holdout result and requires re-planning with a new independent set.

## 5. Acceptance Criteria

### AC-1: Seal integrity and clean holdout-first evaluation

The exact committed corpus is reproducible and the twenty holdout cases are evaluated once before
calibration outcomes or full-universe reconciliation can influence Phase B decisions.

- [ ] Exact task-controlled copies match source hashes `ffeb4b39…`, `1fdc1286…`, partition
  `5b9fb0dd…`, seal metadata `e35af73f…`, Phase A calibration `cbdf4f48…`, and commitment
  `f7d4530d…`; originals remain untouched.
- [ ] Independent audit proves 29 occurrences, 28 unique cases, one `aws_kz` overlap, unique
  case keys/scores, eight lowest-score calibration cases, and twenty holdout cases.
- [ ] A deterministic twenty-URL holdout input is derived from the committed mapping and is parsed
  and probed first; raw ledger/observations and controlled before/after hashes are retained.
- [ ] No holdout outcome changes a Phase A rule, command, prompt, permanent fixture, expected
  disposition, or admission contract. If such a change is needed, the clean result is marked
  invalid and execution stops without catalog mutation.

Gate: Independent hashes/partition audit plus timestamps and artifact order prove the holdout run
preceded Phase B use of calibration/full-universe evidence; `git diff` proves no Phase A code drift.

Evidence: VERIFIED only with retained public Telegram preview responses/observation hashes for all
twenty cases and explicit unresolved transport/identity limitations. No authenticated fallback.

### AC-2: Lossless all-universe observation and collision reconciliation [depends: AC-1]

All source occurrences and candidates receive current mechanical evidence without inheriting
preliminary discovery claims.

- [ ] A deterministic 29-URL input preserves both `aws_kz` occurrences and maps losslessly to 28
  candidates; no occurrence or unsupported condition disappears.
- [ ] Every candidate records requested/canonical identity, target binding, transport/liveness,
  declared/observed peer type, visible name, count only if observed, and verification date.
- [ ] Every candidate records live, archive, canonical, alias, and cross-input collision results;
  similar handles and wrong-target previews fail closed.
- [ ] Every candidate has exactly one action and a concrete evidence-linked reason. The totals sum
  to 28 and every occurrence maps to its candidate/non-candidate disposition.

Gate: Closed observation validators, catalog collision audit, action-total reconciliation, and an
independent Reviewer sample/recheck cover all 28 candidates and all 29 occurrences.

Evidence: Retained public-preview observations and evidence references per candidate; unavailable,
private, ambiguous, stale, or inconsistent targets remain `unresolved` or `reject` as applicable.

### AC-3: Evidence-backed editorial judgements and EN/RU/KK copy [depends: AC-2]

Only target-bound eligible candidates may become proposed ADD rows, and every proposed field is
current, human-readable, neutral, and independently reviewed.

- [ ] Each candidate independently records IT/startup relevance, Kazakhstan relevance,
  commerciality/spam risk, activity limitation, and category validity with specific evidence.
- [ ] Each ADD row uses only observed identity/type/name/count/date facts; an unobserved count is
  omitted/null and no fact is copied from the preliminary discovery table as current evidence.
- [ ] EN/RU/KK descriptions are concise, natural, equivalent in meaning, non-promotional, and
  supported by the inspected source; every category exists in current catalog data.
- [ ] The persistent Reviewer rules on every disposition and proposed row/copy. An available safe
  Antigravity advisory audit is retained separately; disagreements are resolved in favor of the
  evidence and Reviewer, never by majority or fluency.

Gate: Complete per-candidate judgement table plus Reviewer readiness verdict contains no open
blocking copy or eligibility finding for any ADD row.

Evidence: Public target/source excerpts or hashes with bounded paraphrases; Reviewer readiness
artifact; advisory audit when available or an explicit unavailable limitation.

### AC-4: Canonical preview and staged integrity [depends: AC-3]

The exact proposed action set is bound to complete staged bytes and a human rendering without
changing production.

- [ ] The closed bundle passes producer-possible observation validation and contains exactly one
  action per candidate; only all-gates-pass rows use `add` with a complete proposed entry.
- [ ] An isolated staged project contains exact expected `data/communities.json` bytes and all four
  generator-owned projections; schema validation, generator currency, intake/command/catalog
  regressions, and diff checks pass there.
- [ ] `preview.json` and `preview.md` expose the payload SHA-256, actions SHA-256, exact ADD IDs,
  complete disposition table, evidence paths, and exact before/expected-after SHA-256 for all five
  controlled paths.
- [ ] Production controlled paths are byte-identical to their pre-run hashes; no pending marker,
  approval envelope, receipt, or partial production state exists.

Gate: `kz_intake.py preview`, staged schema/currency/tests, renderer-completeness check, five-path
hash comparison, and clean scoped Git audit all pass.

Evidence: Canonical preview, human rendering, staged verification log, exact hashes, and action
digest retained in `phase-b/evidence/`.

### AC-5: Exact owner hard stop and readiness report [depends: AC-4]

The pre-approval phase stops safely with one complete decision envelope and no inferred authority.

- [ ] The Phase B lifecycle is `BLOCKED` on missing exact current owner approval, with a new
  immutable transition event; production controlled paths remain unchanged and the phase branch
  is clean after committing task-local readiness evidence.
- [ ] No `kz-intake-approval/v1` is created and no owner name/time is agent-filled as authority.
- [ ] The Main Coordinator receives exact totals/dispositions, proposed rows/copy, evidence
  limitations, payload/actions hashes, exact ADD IDs, all five before/expected-after hashes,
  Reviewer/advisory readiness, commits/status, and one exact owner statement.
- [ ] Any owner-requested row/copy/action/baseline change produces a successor preview and requires
  a new exact statement; the broad earlier add-all mandate is explicitly rejected as apply proof.

Gate: Status/journal validation, `git status`, controlled-path hash equality, absence of approval/
pending/receipt artifacts, and the Reviewer readiness audit all pass.

Evidence: EV blocker row, no-mutation hashes, commit list, readiness audit, and the exact statement
included in the Coordinator report.

### AC-6: Exact apply and final catalog verification [depends: AC-5]

This criterion begins only after the owner later affirms the exact statement. It cannot be closed
by the readiness audit.

- [ ] The durable owner evidence is converted into a separate approval envelope binding the exact
  payload SHA, actions SHA, ADD IDs, owner handle, evidence ref, and time without altering preview.
- [ ] Authority, observation freshness, collisions, eligibility, category/copy, staged schema/
  currency, and all controlled B/A/X states are rechecked immediately before apply.
- [ ] Apply writes only exact approved staged bytes, or returns exact already-applied no-op; any
  baseline drift, subset, unknown state, or unmarked mixture stops and requires a successor preview.
- [ ] Schema, generator currency, complete relevant regression suite, exact new-entry re-probes,
  final five-path hashes, receipt, and all 28 final dispositions pass and are retained.

Gate: `kz_intake.py apply` with current owner evidence, followed by schema/currency/tests/re-probes,
receipt validation, final hash/action reconciliation, and clean scoped Git audit.

Evidence: Live exact re-probes of every added target, apply receipt, final controlled hashes,
complete EV, and post-apply RF. Only formal `/tfw-review` after RF may approve this criterion.

### AC-7: Cross-tool and non-release boundaries remain intact [depends: AC-6]

Phase B integration must not weaken the approved command or release contracts.

- [ ] `python scripts/sync_kz_commands.py --check` and the complete relevant Python regression
  suite pass at the final applied tree.
- [ ] Safe routing-only Claude/Codex checks are retained when needed to bind the final tree; they
  do not apply, archive, release, tag, push, deploy, or change settings.
- [ ] No existing catalog row is archived or rewritten outside generator/localization mechanics,
  and no unrelated original/owner work is staged.

Gate: Command parity/tests, scoped diff, Git history/status, and explicit absence of release/tag/
push/deployment side effects.

Evidence: Safe local/runtime logs or N/A with evidence that Phase A command bytes are unchanged;
Git/tag/remote-state read-only checks; final EV and RF.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__candidate_integration.md` | Structured per-AC evidence and blocker/final verdict |
| `evidence/source/` | Exact sealed source/partition/metadata copies and independent verification record |
| `evidence/holdout/` | Derived twenty-case input, ledger, observations, and clean-run audit |
| `evidence/universe/` | Full 29-occurrence input, ledger, observations, collisions, judgements, copy, and dispositions |
| `evidence/preview/` | Bundle, staged verification, canonical preview, human rendering, digests, and controlled hashes |
| `review/readiness.md` | Persistent Reviewer’s bounded pre-approval readiness/copy audit |
| `evidence/advisory-language-review.md` | Safe Antigravity advisory result or explicit availability limitation |
| `evidence/approval/` | Created only after later exact approval: owner record, envelope, pending marker if used, and receipt |

## 6. Technical Guidance

- Treat `.agents/skills/kz-add/SKILL.md` as the complete local operational contract. The task
  authority permits the mandated non-mutating evaluation; it does not fabricate literal owner
  arguments or current apply authority. Use task-controlled files derived from the committed
  partition as the exact `--file` inputs and retain how every URL maps back to its source occurrence.
- The sealed material is under
  `C:/Users/c0rpa/.codex/sealed/20260828-201343__catalog_intake_commands/v1`. The two original
  sources are read/hash-only. Copy exact bytes, then work only from Phase B evidence copies.
- Run holdout cases first. Do not inspect Phase A calibration outcomes to set expected dispositions
  before the holdout artifacts are durably recorded. The holdout may reveal real limitations; it
  may not silently become a tuning set.
- `scripts/kz_intake.py` accepts fixed root HTTPS URLs, not the discovery file’s bare handles. A
  deterministic derived URL input is therefore required. Preserve the original bare-handle
  occurrences and byte offsets in provenance while passing their committed `derived_url` values to
  the engine. The full-universe input must retain both `aws_kz` occurrences.
- Use the current catalog categories and exact entry type names (`groups`, `channels`, `bots`).
  Preliminary proposed categories and counts are hypotheses only.
- Public Telegram preview responses may be fetched under the approved bounded read-only semantics.
  Do not use authenticated/private clients or guess from search snippets. For activity limits not
  observable from a target preview, state the limitation rather than infer freshness.
- The staging root must be isolated from production. Expected bytes come from the fixed ADD action
  projection and current generator; direct edits to staged generated projections are invalid.
- The exact approval statement should bind the canonical payload SHA-256, action SHA-256, ordered
  ADD candidate IDs, and the preview artifact that contains all five before/expected-after hashes.
  The later durable owner response supplies the authority evidence reference and approval time.
- Reuse the same Executor and Reviewer tasks for every correction. Do not create replacements.

## 7. Definition of Failure

- ❌ Holdout material is used after calibration/full-universe outcomes, or a holdout result changes
  a durable Phase A rule/fixture/prompt while still being called a clean evaluation.
- ❌ Any of the 29 occurrences or 28 cases disappears, `aws_kz` overlap is collapsed without trace,
  or disposition totals do not reconcile exactly.
- ❌ A target’s identity/type/name/count/date is inferred from another page, stale note, search
  result, or preliminary table; an unobserved count is estimated.
- ❌ A non-IT, non-Kazakhstan, purely commercial/spam, inactive/private/ambiguous, wrong-type, or
  duplicate target is proposed to add merely because its URL resolves.
- ❌ EN/RU/KK copy is placeholder, fallback, promotional, semantically divergent, unsupported, or
  not independently reviewed.
- ❌ Production data or projections change before the exact current owner statement, or an agent
  creates/claims the approval envelope from broad planning/execution authority.
- ❌ Preview/actions/staged bytes/controlled hashes/ADD IDs diverge, or a subset/baseline change is
  applied without a successor preview and approval.
- ❌ The pre-approval readiness audit is represented as formal Phase B APPROVE or as closing AC-6.
- ❌ Original owner work is edited/staged/deleted, unrelated work is absorbed, or either source
  checkout is called clean despite the known untracked batch.
- ❌ Any archive, release, tag, push, deployment, settings change, authenticated Telegram action,
  or other external mutation occurs.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Live previews change between holdout, full reconciliation, approval, and apply | Bind observation timestamps/hashes and require material freshness recheck/successor preview |
| Holdout-first order is hard to prove after the fact | Commit/retain exact run artifacts and timestamps before opening calibration outcomes for Phase B use |
| Source notes overstate KZ fit or activity | Require current public evidence or explicit owner-evidence classification; otherwise reject/unresolved |
| Category/copy choices become subjective and inconsistent | Use current taxonomy, evidence-cited rationale, Reviewer ruling, and optional advisory language check |
| Large candidate table hides one missing/non-add reason | Machine total reconciliation plus human per-disposition table and Reviewer full audit |
| Production baseline changes while owner decides | Approval expires on any before-hash or material evidence change; regenerate a successor preview |
| Network throttling yields partial evidence | Preserve per-candidate transport result, rate limit, resume read-only probing, and never turn failure into liveness |
| Temporary staging leaks into commits | Stage outside the repository or under ignored task-temporary storage; commit only declared evidence/traces |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `data/communities.json` | Discoverability Phase A; TFW-4 Phases C/D | Keep structured North Star, locale review digest/cardinality, archive, and observed-fact contracts exact |
| `README.md`, `index.md`, `ru/index.md`, `kk/index.md` | Catalog discoverability Phases A/B | Generator is the sole writer; canonical/hreflang/site metadata must remain current |
| `scripts/kz_intake.py`, `scripts/validate_links.py` | Phase A | Read/use only; any modification is a scope and clean-evaluation failure |
| `.claude/commands/kz-*.md`, `.agents/skills/kz-*/SKILL.md` | Phase A | Read/check only; complete byte parity and safety semantics must remain unchanged |

---

*TS — 20260828-201343__catalog_intake_commands / Phase B: Clean candidate run and catalog integration | 2026-08-29*

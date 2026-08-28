# TS — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-28
> **Author**: Coordinator (Codex)
> **Status**: ✅ APPROVED — owner autonomous-continuation mandate, 2026-08-28
> **Parent Phase HL**: [Phase A HL](HL__phase-a__intake_engine.md)
> **Parent Master HL**: [Master HL](../HL-20260828-201343__catalog_intake_commands.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) · [Iteration 2 RES](../research/iter2/RES.md)
> **Mode**: AG for local implementation and deterministic tests; CL/read-only for calibration and
> fresh runtime evidence. No production candidate addition, push, tag, release, or external mutation.

---

## 1. Objective

Deliver a safe reusable intake engine and complete synchronized Claude/Codex command bodies for
`/kz-add`, `/kz-stats`, and `/kz-release`. Phase A proves lossless input accounting, non-mutating
candidate observation, exact preview/authority/apply semantics, and cross-runtime command behavior
without exposing the twenty-case holdout or changing a production catalog fact.

## 2. Scope

### In Scope

- Parse exactly one `--text` or `--file` source into a lossless occurrence ledger before grouping.
- Accept only fixed HTTPS root peer links on `t.me`, `telegram.me`, and `telegram.dog`; explicitly
  disposition every other Telegram-like or malformed occurrence without parent/prefix salvage.
- Fetch a candidate preview once and reuse the unchanged typed classifier for groups, channels,
  and bots under the I2-C1R aggregation invariant.
- Detect live/archive/cross-input collisions and represent mechanical versus editorial gates
  separately; positive IT/KZ/commercial/category/locale decisions remain evidenced proposals.
- Produce and validate a closed canonical preview, separate approval envelope, pending execution
  marker, and receipt with exact controlled-path B/A/X semantics.
- Implement complete location-neutral command copies and deterministic inventory/sync/parity gates.
- Use synthetic fixtures and the eight disclosed calibration cases; retain calibration evidence
  without adding them to `data/communities.json`.
- Prove fresh literal routing, argument receipt, loaded copy, and safety stops in Claude and Codex.

### Out of Scope

- Reading, enumerating, searching for, probing, or embedding the twenty holdout cases or their
  source paths; using them in prompts, fixtures, smokes, or expected outcomes.
- Applying any real candidate to the catalog, changing live counts/dates, archiving, or generating
  production projections from candidate additions.
- Generic Telegram deep-link support, message/story parent extraction, `tg:` resolution, username
  subdomains, query/fragment acceptance, private invites, authenticated Telegram data, or guessing.
- A shared observation-module refactor, generic RFC 8785 dependency, owner signing-key ceremony,
  third command source, GUI/service, release, tag, push, or external mutation.

## 3. Principles Check

| # | Principle (Master HL §7) | Enforced by | Gate |
|---|---|---|---|
| P1 | Accuracy governs coverage | AC-1, AC-2, AC-4 | Invalid identity/type/gate state is explicit and never promoted |
| P2 | Observation and judgement stay separate | AC-2, AC-3 | Network fields and editorial evidence/actions are distinct |
| P3 | Preview before mutation | AC-3, AC-4 | Exact payload and current authority precede fixture-only apply |
| P4 | Complete copies, enforced parity | AC-5, AC-7 | Full-body inventory/parity plus fresh runtime proof |
| P5 | Fail closed and account for every input | AC-1, AC-2 | Occurrence totals precede grouping; every loss/failure is visible |
| P6 | Holdout evidence must be honest | AC-6, AC-8 | Calibration-only scope and leakage audit |
| P7 | Generated output remains generated | AC-4, AC-8 | Production source/projections remain byte-identical |

## 4. Affected Files

| File | Action | Description |
|---|---|---|
| `scripts/kz_intake.py` | CREATE | Source/occurrence, preview/authority/apply-state orchestration |
| `scripts/sync_kz_commands.py` | CREATE | Exact inventory, completeness, sync, and parity gate |
| `scripts/test_kz_intake.py` | CREATE | Deterministic parser/canonical/authority/apply/observation tests |
| `scripts/test_kz_commands.py` | CREATE | Inventory, loader, path-neutrality, completeness, and parity tests |
| `scripts/validate_links.py` | MODIFY | Minimum fetch-once seam while preserving classifier and stats behavior |
| `.claude/commands/kz-add.md` | CREATE | Complete `/kz-add` command body and exact authoring copy |
| `.claude/commands/kz-stats.md` | MODIFY | Location-neutral complete body; safety semantics unchanged |
| `.claude/commands/kz-release.md` | MODIFY | Location-neutral complete body; pre-tag/push stop unchanged |
| `.agents/skills/kz-add/SKILL.md` | CREATE | Exact complete Codex copy |
| `.agents/skills/kz-stats/SKILL.md` | CREATE | Exact complete Codex copy |
| `.agents/skills/kz-release/SKILL.md` | CREATE | Exact complete Codex copy |
| `AGENTS.md` | MODIFY | Truthfully register the three available project commands |

**Implementation budget:** 8 new files, 4 modifications, 12 paths, at most 2500
insertion-plus-deletion lines. Generated calibration/TFW evidence is not implementation scope.
Exceeding any limit or adding a dependency requires re-planning.

## 5. Acceptance Criteria

### AC-1: Lossless, closed candidate source grammar

- [ ] Exactly one of `--text` and `--file` is required; missing files and invalid UTF-8 stop.
- [ ] Every Telegram-like raw span has stable source/ordinal/byte offsets, raw bytes/text, any
  trimmed suffix, link-kind disposition, and optional candidate ID before deduplication.
- [ ] Only `https://{t.me|telegram.me|telegram.dog}/{HANDLE}` with optional `/` can produce a
  candidate; reserved/private/message/action/query/fragment/subdomain/http/tg/port/user-info/
  percent-encoded/spoofed/malformed forms never do.
- [ ] Case variants and repeated occurrences remain separate ledger rows and one grouped candidate.

Gate: `python -m unittest scripts.test_kz_intake -v` with adversarial synthetic vectors and exact
occurrence/candidate totals.

Evidence: N/A — deterministic source parsing has no live dependency.

### AC-2: Non-mutating arbitrary-candidate observation  [depends: AC-1]

- [ ] A network seam returns immutable fetched bytes or a stable transport result without identity
  interpretation; catalog update/archive paths remain separate.
- [ ] The same bytes enter all three unchanged typed classifier calls. Type is accepted only for
  exactly one verified result and two target-bound matching declared-type mismatches.
- [ ] Zero/multiple verified results, target disagreement, unexpected tuples, conflict, private,
  dead, or transport failure are unresolved and expose no downstream fact as approved.
- [ ] Existing stats summary, retry, identity/decoy, update, and archive tests remain exact.

Gate: predecessor suite plus `python -m unittest scripts.test_kz_intake -v`; source audit confirms
`classify_response` semantics are unchanged.

Evidence: surface: public Telegram previews for exactly the eight calibration cases; method: one
read-only probe per candidate with bounded retry; artifact: Phase A EV; fallback: unresolved with
retained reason—no browser/authenticated escalation is required for Phase A acceptance.

### AC-3: Closed preview and separate current authority  [depends: AC-1, AC-2]

- [ ] `kz-canonical-json/v1` rejects duplicate/unknown fields, lexical `-0`, floats/exponents,
  unsafe integers, invalid Unicode, non-ASCII keys, invalid order/reference/totals, and hidden
  significant fields; canonical UTF-8/LF vectors reproduce exact hashes.
- [ ] Preview binds source/occurrence/candidate ledgers, collisions, observations, editorial
  evidence, exact localized proposed rows/actions, contract versions, totals, and controlled-path
  before/expected-after hashes; it excludes its own digest and later authority.
- [ ] Human rendering accounts for every significant field and visibly distinguishes observed,
  editorial, rejected, duplicate, unresolved, and proposed-add state.
- [ ] Approval is a separate envelope bound to the exact payload/action projection and a durable
  current owner evidence reference; an agent-written owner string or subset edit cannot authorize.

Gate: deterministic canonicalization/tamper/replay/renderer-completeness tests.

Evidence: N/A for Phase A production authority; synthetic approval fixtures prove validation only.

### AC-4: Strict, idempotent, crash-aware apply boundary  [depends: AC-3]

- [ ] Apply rechecks payload/envelope, exact controlled-path state, live freshness for add actions,
  collision/eligibility, staged schema, and generated currency before the first replacement.
- [ ] All-before may apply exact staged after bytes; all-after writes no controlled byte and reports
  `already_applied_exact`; any unknown state stops.
- [ ] Mixed before/after may recover only with a durable matching pending marker created before the
  first replacement; unmarked/corrupt/mismatched mixtures stop.
- [ ] Receipt is separate and binds payload, envelope, execution, before/final path hashes,
  validations, exact applied IDs, and outcome.
- [ ] Production `data/communities.json`, README, and three site projections remain byte-identical
  throughout Phase A; apply tests use isolated temporary copies only.

Gate: failure-injection/idempotency/stale-state tests plus before/after production hashes.

Evidence: N/A — production mutation is forbidden in Phase A.

### AC-5: Complete synchronized `kz-*` command inventory

- [ ] Exact names are `kz-add`, `kz-stats`, and `kz-release` at both frozen runtime locations.
- [ ] Each pair is byte-identical, uses common valid `name`/`description` metadata and
  location-neutral root textual paths, and contains the complete authority, inputs, ordered
  operation, outputs, failures, validations, and hard stops locally.
- [ ] No body depends on opening its counterpart, generated source, separate workflow, or runbook
  to learn missing behavior; identical thin copies fail completeness review.
- [ ] Explicit sync is Claude-source-to-Codex; `--check` never mutates and fails missing/extra/
  mismatched names, metadata, paths, body markers, newline/byte drift, or forbidden references.
- [ ] Existing stats owner triage and release pre-tag/pre-push approval semantics do not weaken.

Gate: `python scripts/sync_kz_commands.py --check` and
`python -m unittest scripts.test_kz_commands -v`, followed by formal standalone-body inspection.

Evidence: N/A — runtime behavior is AC-7.

### AC-6: Preserve the sealed evaluation boundary

- [ ] Phase A input matches the committed calibration manifest and public seal commitment; it
  contains eight cases and no holdout identity, URL, raw text, expected outcome, or source path.
- [ ] Code, fixtures, commands, prompts, transcripts, and evidence contain no holdout material.
- [ ] Calibration results may refine Phase A before review but are never hardcoded as permanent
  current facts or represented as the clean evaluation result.
- [ ] The unrelated original source files remain unstaged, unmodified, and outside Executor scope.

Gate: exact manifest/hash/count audit plus repository and task-context leakage scan by the Reviewer.

Evidence: Phase A EV binds the public seal commitment and eight calibration outcomes only.

### AC-7: Fresh Claude and Codex literal command behavior  [depends: AC-5]

- [ ] Static inventory/parity passes at one exact implementation SHA in a clean disposable
  worktree/archive that excludes untracked source/holdout files.
- [ ] One fresh nonpersistent tools-disabled Claude session and one fresh non-forked read-only
  Codex task invoke literal `/kz-add` with a synthetic reserved-action sentinel and perform routing-
  only `/kz-stats` and `/kz-release` smokes.
- [ ] Evidence binds loaded local path/hash, complete arguments, no candidate network/apply for the
  sentinel, stats owner-triage boundary, release pre-tag/push stop, and before/after clean hashes.
- [ ] `$kz-add`, static files, or the current contextualized task cannot substitute for literal
  Codex `/kz-add`; insufficient fresh evidence blocks AC-7.

Gate: inspect exact-SHA transcripts, runtime file hashes, and before/after Git/controlled hashes.

Evidence: Phase A EV plus redacted complete fresh-runtime transcripts; no external mutation.

### AC-8: Preserve scope and predecessor behavior  [depends: AC-2, AC-4, AC-5, AC-6, AC-7]

- [ ] Schema, all existing generation/site tests, new intake/command tests, and index validation pass.
- [ ] No production candidate/count/date/archive fact or generated projection byte changes.
- [ ] No holdout/source snapshot is adopted, no release/tag/push occurs, and unrelated dirty paths
  are not staged, overwritten, or claimed clean.
- [ ] Final implementation path/line counts remain within §4 and RF names exact deviations.

Gate: full test suite, `git diff --check`, path/LOC audit, exact production hashes, and mutation log.

Evidence: Phase A EV records commands, hashes, calibration/live limitations, runtime smokes, and
explicit zero external mutation.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/input-commitment.json` | Public source/seal/method/8–20 commitment without holdout identities |
| `evidence/calibration-input.json` | Exact eight disclosed calibration cases and their occurrences |
| `evidence/EV__phase-a__intake_engine.md` | Per-AC environment, commands, hashes, calibration, runtime, and no-mutation evidence |
| `evidence/claude-runtime-smoke.jsonl` | Fresh Claude literal-routing transcript |
| `evidence/codex-runtime-smoke.md` | Fresh Codex task identity, loaded skill hashes, outputs, and before/after state |

## 6. Technical Guidance

- Preserve `classify_response` as the sole identity/type authority. Extract only the minimum
  immutable fetch/retry result needed to reuse the same HTML across declared types.
- Keep runtime dependencies in the Python standard library. `kz-canonical-json/v1` is a closed
  domain, not a general JCS claim.
- Treat the operation as deterministic scripts plus complete agent orchestration instructions;
  agent prose is not parser/classifier evidence.
- Controlled production paths are `data/communities.json`, `README.md`, `index.md`, `ru/index.md`,
  and `kk/index.md`; Phase A expects their before and after hashes to be equal.
- Command paths are literal repository-root text, not Markdown links relative to runtime files.
- The Coordinator supplies only the committed calibration manifest. Do not search outside the
  dedicated worktree or inspect the original untracked/external sources.

## 7. Definition of Failure

- ❌ Any raw occurrence silently disappears or any unsupported URL produces a candidate by salvage.
- ❌ Candidate observation mutates catalog data, changes classifier semantics, or treats three
  declared types as independent votes/fetches.
- ❌ Canonical bytes, human rendering, owner action, expected post-state, and applied bytes can diverge.
- ❌ A real catalog byte changes, or a holdout case enters Phase A implementation/evidence/context.
- ❌ A command copy is thin, incomplete, location-dependent, drifted, undiscoverable, or weakens
  stats/release authority.
- ❌ Literal fresh Codex evidence is waived or replaced by static/`$skill` evidence.
- ❌ File/LOC budgets are exceeded, unrelated dirty work is staged, or any push/tag/release/external
  mutation occurs.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Calibration network failures | Preserve unresolved outcomes; Phase A tests safety, not eight positive admissions |
| Runtime model echoes rather than loads local command | Combine transcript read/path/hash evidence with command-specific behavior and static bytes |
| Canonical implementation grows into a second schema system | Closed minimal schema and fallback to reviewed RFC 8785 only through re-planning |
| Multi-path apply fixture hides rollback bug | Failure injection at each replacement and marker corruption/missing cases |
| Shared checkout contains raw sources | Execute in a dedicated exact-base worktree containing only calibration input |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `scripts/kz_intake.py` | Phase B | Phase B consumes the reviewed interface; holdout-driven durable edits invalidate clean evidence |
| `.claude/commands/kz-add.md` and exact Codex copy | Phase B only if a formally reviewed defect requires revision | Any change invalidates Phase A fresh-runtime and holdout evidence |
| `AGENTS.md` | Phase B only for truthful state wording if needed | Command contract itself must not drift |
| `data/communities.json` and generated projections | Phase B | Byte-invariant in A; exact approved additions only in B |

---

*TS — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

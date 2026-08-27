# TFW Conventions

## 1) Purpose

TFW turns work (analytics, documents, code, research) into a reproducible process:
- context is captured,
- decisions are traced,
- results are repeatable,
- any agent can continue the project in a new session.

## 2) Required Artifacts (project root)

- `README.md` — human explanation: why/what/how. Contains Task Board.
- `AGENTS.md` — AI agent behavior rules for the project.
- `TECH_DEBT.md` — accumulated tech debt from reviews (observations → triage → registry).
- `KNOWLEDGE.md` _(optional)_ — project knowledge index: architecture, decisions, legacy. Template: `.tfw/templates/KNOWLEDGE.md`.
- `RELEASE.md` _(optional)_ — project release strategy and context. Template: `.tfw/templates/RELEASE.md`.
- `.tfw/README.md` — TFW philosophy, lifecycle, values.
- `.tfw/conventions.md` — project conventions (this file).
- `.tfw/glossary.md` — project glossary.
- `.tfw/templates/HL.md` — canonical HL template.
- `.tfw/templates/TS.md` — canonical TS template.
- `.tfw/templates/RF.md` — canonical RF template.
- `.tfw/templates/ONB.md` — canonical Onboarding Report template.
- `.tfw/templates/RES.md` — canonical Research Report template.
- `.tfw/templates/REVIEW.md` — canonical Review template.
- `.tfw/workflows/init.md` — canonical initialization workflow.
- `.tfw/workflows/plan.md` — canonical planning workflow.
- `.tfw/workflows/research/base.md` — canonical research workflow (entry point).
- `.tfw/workflows/handoff.md` — canonical execution workflow.
- `.tfw/workflows/review.md` — canonical review workflow.
- `.tfw/workflows/resume.md` — canonical resume workflow.
- `.tfw/workflows/docs.md` — canonical knowledge update workflow.
- `.tfw/workflows/release.md` — canonical release workflow.
- `.tfw/workflows/update.md` — canonical upstream update workflow.
- `.tfw/workflows/config.md` — interactive config change workflow.
- `.tfw/VERSION` — current framework version (semver, single line).
- `.tfw/CHANGELOG.md` — version history (Keep a Changelog format).
- `.tfw/project_config.yaml` — project configuration (stack, build commands, task prefix, execution engine).
- `.tfw/compilable_contract.md` — build-time compilation specification (Source Manifest, Reference Format, Output Structure).

## 3) Artifact Types (canonical)

> See also: [glossary.md](glossary.md) for terminology, [README.md](README.md) for philosophy.

### HL (High Level)
Context/frame. Not a task — a "map of meaning".
Format: strictly follows `.tfw/templates/HL.md`.

#### HL Contract

An approved HL is a contract, not a draft. Approval is the moment it freezes.

| HL section | State after owner approval |
|------------|---------------------------|
| §1 Vision · §3 Target State (incl. §3.1, §3.2) · §4 Phases · §5 DoD · §6 DoF · §7 Principles (incl. §7.1) | 🔒 FROZEN |
| §2 Current State · §7.2 Knowledge Citations · §8 Dependencies · §9 Risks · §10 RESEARCH Case · §11 Strategic Insights | 🟢 FREE |
| §12 Amendment Log | 🟢 APPEND-ONLY |

1. **The contract state is artifact state.** The HL header carries a `Contract` field with two values: `📝 DRAFT — not yet approved` and `🔒 FROZEN — approved by {owner} YYYY-MM-DD`. Task status tracks the pipeline; the `Contract` field tracks the artifact. They are not interchangeable.
2. **Free sections stay free.** Research and the coordinator update §2, §7.2, §8, §9, §10 and §11 directly, with no proposal and no verdict. Risk registers, hypothesis statuses and dependency statuses are required to move.
3. **A frozen section may not be edited.** The only channel is §12 Amendment Log: propose, wait for the owner's verdict, then apply. This holds for every role, including the coordinator that authored the HL.
4. **§12 is append-only.** Rows are never deleted, rewritten or renumbered. A refused proposal stays visible as an attempt — that visibility is the point.
5. **The frozen unit is the declarative claim, not the section text.** Frozen at claim level: the phase set and each phase's declared outcome, §3's to-be claims, each §5 and §6 item, each §7 principle, and §1. Rewording a claim without changing it is not an amendment; changing what it commits to is.
6. **Deliverable lists inside an already-approved phase are free** — specifying *how* a phase meets its declared outcome is refinement. **Tripwire:** if the change cannot be accepted under §5 and §6 *as they stand at the moment of classification*, it is an amendment. Two tables decide it; no judgement call is required.
7. **Non-substantive edits are not amendments** — typos, broken links, formatting, renumbering of free-section rows.
8. **A verdict is a distinct recorded act.** Input given inside a research thread, a review or a chat is evidence for a proposal, never approval of one. A proposal is ruled only by an explicit owner verdict written onto its §12 row.
9. **An owner-initiated change to a frozen section is an amendment too** — logged in §12 with the owner as `Proposer` and the verdict on the same row. The log's value is the record, not the gate: a §12 that omits the owner's own changes cannot answer the question it exists to answer.
10. **A restrictive change applies on filing.** Narrowing — adding a DoF item, tightening scope, dropping a deliverable — is logged with `Type` = `RESTRICT` and verdict `✅ APPLIED — no owner verdict required`. Restrictive-free is prohibited: the classifier benefits from the label, so the log costs nothing and removes the incentive.
11. **`Type` states relation to the baseline, never disposition.** `EXTEND` adds and the original stays in force; `SUPERSEDE` replaces; `RESTRICT` narrows. Disposition belongs in `Verdict`.
12. **A proposal without evidence, cost and a considered alternative is not a proposal.** The burden sits on the proposer, which is what keeps declining cheap.

**Contract Baseline** — a frozen contract that cannot be diffed is not frozen.

13. **The approved HL is committed before the first research iteration.** An uncommitted baseline makes "frozen" permanently unverifiable (TFW-48 precedent).
14. **The baseline reference is a reserved `freeze` scope word** in the commit subject, per the `[agent/task/scope/role]` grammar in §4: `[claude-code/PROJ-7/freeze/coordinator] freeze approved hl`. It applies to the **first** freeze and to every re-freeze after an approved amendment.
15. **Recovery form:** `git log --format="%h %s"`, filtered on `^\S+ \[[^]]*/{TASK-ID}/freeze/`. Both properties were learned from live failures and survive any edit: filter the **subject**, never the message — `--grep` also returns commits that merely quote a freeze subject; and never start the pattern with `/` — some shells rewrite a leading slash as a path.
16. **No header field can name its own commit** — a commit's SHA cannot appear in its own content. The baseline lives in the commit subject, not in the file, and needs no separate registry.

**Delegated authority**

17. **A delegated mandate is a ceiling, never a source of new permission.** It bounds what an agent may do; it does not create what an agent may do.
18. **No agent may widen its own grant.** Authority that can justify its own extension is not authority, it is a loop.
19. **Delegation is never valid authority to accept a scope or budget overrun.** "I was delegated this decision" does not convert an overrun into a compliant result.

**Phase HL**

20. **A Phase HL is derivation-only.** It may restate master content and add execution context — files, sequencing, phase-local risks.
21. **A Phase HL may not carry its own §1, §5, §6 or §7.** Vision, acceptance criteria, failure conditions and principles exist once, in the master HL. A Phase HL that authors them is a second, unapproved contract.

### Project North Star

The layer above every task HL: what the product is for, and what it must never become. Together with the
contract baseline it is the reference set of the Purpose Check (`templates/review/judge.md` row 2a),
and it is PV priority 0 (`glossary.md`).

1. **Locus: designated section(s) of a README.** More than one location is permitted — a project whose
   product is its own method may designate sections of both its root README and its philosophy paper.
2. **A task HL may never be nominated.** Nominating one promotes a task contract to project authority with
   no gate at the promotion point, and imports contract drift one level up. Supporting that locus properly
   would need a project-level freeze mechanism, which TFW does not define.
3. **Payload: purpose, principles and non-goals.** Non-goals are not optional. The failure mode this layer
   exists to catch is *excess*, not opposition, and a purpose statement alone cannot detect excess.
4. **Admission criteria.** A clause belongs here if it states what the product *is for* or *must never
   become*. If a single task's implementation choice could satisfy or violate it, it is a principle
   (HL §7), not a north-star clause. This is a criterion, not a size cap — a list carrying implementation
   detail satisfies a citation requirement forever while blocking nothing.
5. **Optional, with a declared fallback:** project north star → master HL §1 at the contract baseline. A
   review is never blocked on a missing north star.
6. **PV priority 0 and priority 1 may name the same file.** They are distinguished by what the section says
   — *what we are building* versus *how we build* — never by which file holds it. Where the product is the
   methodology, one file legitimately carries both.
7. **Citation namespace:** `NS{n}` for north-star clauses; HL §7 keeps `P{n}`; a project principle registry
   uses `PP{n}` (see `compilable_contract.md` §2).

### RES (Research Report)
Structured investigation artifact. Produced via Briefing → Gather → Extract → Challenge stages in `research/` subfolder.
RES file = synthesis (Decisions, Hypotheses, HL Recommendations, Conclusion). Stage files = raw investigation.
Created between HL and TS (pipeline) or standalone for any research.
Format: strictly follows `.tfw/templates/RES.md`.

### TS (Task Spec)
Task definition. Always self-contained: inputs/outputs/constraints/DoD.
Format: strictly follows `.tfw/templates/TS.md`.

### RF (Result File)
Results/facts/data/final text. RF has priority as source of truth.
Contains mandatory Observations table (structured, typed).
Format: strictly follows `.tfw/templates/RF.md`.

### ONB (Onboarding Report)
Structured executor report before starting: understanding, questions, risks, inconsistencies.
Coordinator/human answers directly in the file (Q&A format).
Format: strictly follows `.tfw/templates/ONB.md`.

### REVIEW (Review Report)
Formal coordinator report after reviewing RF: checklist, verdict, tech debt.
Format: strictly follows `.tfw/templates/REVIEW.md`.

### Fact Candidates (section in RF, REVIEW, RES)
Raw observations about the project recorded during work. Cognitive mode: pure reporting — record factual without interpretation. NOT verified facts — they become facts after `/tfw-knowledge` consolidation. Each artifact has a Fact Candidates section with a structured table (Category, Candidate, Source, Confidence). Quality filter: "Would the next agent decide differently knowing this?"

### Visual Sections (per-template)

> **Decision criterion:** "Does the cognitive mode CHANGE between templates?" If yes → per-template naming. If no → unified.
> Visual sections trigger different cognitive modes per template context (empirically validated: RES3 D22, RES4 Exp1+Exp2).

| Template | Section | Cognitive Mode | What it produces |
|----------|---------|---------------|-----------------|
| HL | §3.1 Result Visualization | Narrative / Outcome | Outcome preview — Working Backwards style ("imagine it's done") |
| HL | §3.2 Value Flow | Strategic / Value-oriented | Value streams, INPUT→PROCESSING→OUTCOME, transformation tables |
| RF | §9 Diagrams | Technical / Engineering | Architecture, ERD, sequence diagrams, component diagrams |
| RES | Findings Map | Analytical / Research | Root cause analysis, hypothesis trees, priority matrices |
| REVIEW | — | — | No visual section (checklist artifact, not result) |

### Knowledge Capture Sections (unified naming)

| Section | Name | Templates | Cognitive Mode |
|---------|------|-----------|---------------|
| §7 | Fact Candidates | RF, RES, REVIEW | Pure reporting: record without interpretation |
| §8/§11 | Strategic Insights + qualifier | HL (Planning), RF (Execution), RES (Research) | Deep analytical synthesis: capture + add implications |

### Knowledge Input Sections (unified naming)

| Section | Name | Templates | Cognitive Mode |
|---------|------|-----------|----------------|
| §7.2 | Knowledge Citations | HL | Input tracing: cite what was read from PV Index with links |
| §7 | Knowledge Citations | ONB | Input tracing: confirm read of HL §7.2 citations, add new items |
| _(section)_ | Knowledge Citations Verified | review/verify.md | Verification: check that citation links resolve to real items |

> **Unified naming rationale (D43/D28/D39):** cognitive mode is the same across all three — "report what you read and how it applies." Same mode = same name. Scan scope differs by role: Coordinator + Reviewer do full PV scan, Executor references coordinator's citations. See glossary.md → Project Values (PV).

### Evidence Sections (per-template)

> Evidence = real-world verification of completed work in its intended environment.
> Separate from Verification (RF §4 — synthetic tool output: lint, test, build).
> Status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A.
> Role pipeline: Coordinator designs (TS) → Executor collects (EV file) → Reviewer audits (REVIEW).
>
> **Mandatory folder:** Every task directory MUST contain an `evidence/` subfolder with a structured EV file.
> The EV file captures environment metadata, per-AC verification results, and a verdict summary.
> RF §5 is a pointer to the EV file — not a duplicate of the evidence table.
> Template: `.tfw/templates/evidence/EV.md`.

| Template | Section | Cognitive Mode | What it produces |
|----------|---------|---------------|------------------|
| TS | Evidence field (in §5 AC items) | Prescriptive / Planning | What to verify in real environment, suggested tools |
| EV file | `evidence/EV__{...}.md` | Observational / Verification | Environment header, per-AC evidence table, verdict, attachments |
| RF | §5 Evidence (pointer) | Summary / Reference | One-line pointer to EV file + verdict summary |
| review/verify.md | Evidence Verification | Audit / Trust-but-verify | Artifact existence checks, claim-vs-reality |
| review/judge.md | Check #7 Evidence completeness | Judicial / Completeness | All TS Evidence fields covered in EV file? |

## 4) Task Numbering

ID format is defined in `.tfw/project_config.yaml` (field `tfw.task_prefix`).

File naming:

| Artifact | Format | Example |
|----------|--------|---------|
| Master HL | `HL-{PREFIX}-{N}__{title}.md` | `HL-PROJ-3__tfw-setup.md` |
| Single-phase RES | `RES__{PREFIX}-{N}__{title}.md` | `RES__PROJ-3__tfw-setup.md` |
| Single-phase TS | `TS__{PREFIX}-{N}__{title}.md` | `TS__PROJ-3__tfw-setup.md` |
| Single-phase RF | `RF__{PREFIX}-{N}__{title}.md` | `RF__PROJ-3__tfw-setup.md` |
| Single-phase ONB | `ONB__{PREFIX}-{N}__{title}.md` | `ONB__PROJ-3__tfw-setup.md` |
| Single-phase REVIEW | `REVIEW__{PREFIX}-{N}__{title}.md` | `REVIEW__PROJ-3__tfw-setup.md` |
| Phase RES | `RES__phase-{x}__{title}.md` | `RES__phase-a__conventions.md` |
| Phase TS | `TS__phase-{x}__{title}.md` | `TS__phase-a__conventions.md` |
| Phase RF | `RF__phase-{x}__{title}.md` | `RF__phase-a__conventions.md` |
| Phase ONB | `ONB__phase-{x}__{title}.md` | `ONB__phase-a__conventions.md` |
| Phase REVIEW | `REVIEW__phase-{x}__{title}.md` | `REVIEW__phase-a__conventions.md` |
| Single-phase EV | `EV__{PREFIX}-{N}__{title}.md` | `EV__PROJ-3__tfw-setup.md` |
| Phase EV | `EV__phase-{x}__{title}.md` | `EV__phase-a__conventions.md` |

> **Rule:** ALL artifact filenames MUST include the task ID (`{PREFIX}-{N}`) or Phase identifier. A filename without either is an error.

Task folder: `tasks/{PREFIX}-{N}__{title}/`

### Commit Attribution

Every AI-authored commit MUST use `[agent/task/scope/role] summary`: set `agent` to the lowercase AI product name from explicit context, `task` to the canonical TFW task ID (`project` only when none exists), `scope` to the established lowercase work-slice slug or a lowercase hyphenated form of its explicit label, and `role` to the lowercase canonical TFW workflow owner from §15/Role Lock; keep `summary` short and imperative, commit locally, and push only after explicit user approval.

Example: `[codex/TFW-50/task/coordinator] define minimal commit attribution`

### Research subfolder

Research artifacts live in a single `research/` container at task root. Each iteration gets its own numbered subfolder:

```
tasks/{ID}/research/
  iterations.yaml              ← control file
  iter1/
    1_briefing.md              ← numbered stage files
    2_gather.md
    3_extract.md
    4_challenge.md
    RES.md                     ← synthesis co-located with stages
  iter2/
    1_briefing.md
    2_gather.md
    3_extract.md
    4_challenge.md
    RES.md
```

File existence = stage completion. Stage file format: see `.tfw/templates/research/` (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`).

#### Multi-iteration research

When research spans multiple iterations, each iteration gets its own subfolder and RES:

| Iteration | Stage files folder | RES file |
|-----------|-------------------|----------|
| 1 | `research/iter1/` | `research/iter1/RES.md` |
| 2 | `research/iter2/` | `research/iter2/RES.md` |
| N | `research/iterN/` | `research/iterN/RES.md` |

**Trace rule:** Iteration folders accumulate — never delete or overwrite previous iteration's files. Each `research/iterN/` folder is a trace. Deleting them = deleting reasoning.

**Control file:** `research/iterations.yaml` tracks iteration state. Created by coordinator in `plan.md` Step 6 before launching research. Format:

```yaml
task_id: PROJ-N
title: research focus description
min_iterations: 2       # from tfw.research.min_iterations or coordinator override
max_iterations: 5       # soft ceiling
iterations:
  - number: 1
    focus: "initial investigation of H1-H3"
    hypotheses: [H1, H2, H3]
    status: complete     # pending | in_progress | complete
    res_file: research/iter1/RES.md
    # agent: antigravity           # optional — which tool/agent ran this iteration
    # sources: [external, codebase] # optional — what sources were consulted
  - number: 2
    focus: "deepen findings from iter 1, test H4"
    hypotheses: [H4]
    status: pending
    res_file: research/iter2/RES.md
```

The `agent` field records which tool or agent conducted the iteration — for traceability, not dispatch. The `sources` field records what source categories were consulted. Both fields are optional; simple single-agent tasks can omit them.

Coordinator updates `research/iterations.yaml` after each iteration (marks status, adds next iteration if needed). Researcher reads it at start to understand predecessor context and assigned hypotheses.


### Review subfolder

Review stage files (`review/map.md`, `review/verify.md`, `review/judge.md`) — intermediate review traces written during the review process. Created in task phase directory. Parallels research stage files (`research/iterN/1_briefing.md`, etc.). The REVIEW artifact synthesizes these files. Stage file format: see `.tfw/templates/review/` (map.md, verify.md, judge.md).

### Evidence subfolder

Every task directory (or phase directory for multi-phase tasks) MUST contain an `evidence/` subfolder. The subfolder always contains at least one structured EV file (`EV__{PREFIX}-{N}__{title}.md` or `EV__phase-{x}__{title}.md`). Additional binary artifacts (screenshots, API responses, logs) go into the same `evidence/` folder and are indexed in the EV file's Attachments section. Template: `.tfw/templates/evidence/EV.md`.

### Multi-phase folder structure

For multi-phase tasks, master artifacts (HL, RES) stay at task root. Each phase gets a subfolder:

```
tasks/PROJ-5__query_redesign/
  HL-PROJ-5__query_redesign.md        ← Master HL
  research/                           ← Master research (if any)
  phase-a/
    HL__phase-a__data_model.md
    TS__phase-a__data_model.md
    ONB__phase-a__data_model.md
    RF__phase-a__data_model.md
    REVIEW__phase-a__data_model.md
    evidence/                         ← Mandatory evidence folder
      EV__phase-a__data_model.md      ← Structured evidence file
  phase-b/
    HL__phase-b__api_layer.md
    ...
```

## 5) Task Statuses

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
                                                                              │
                                                                    ┌─────────┴─────────┐
                                                                    🔄 REVISE          ❌ REJECT
                                                                 (back to dev)    (user decides)
                    (skip: 📝 HL_DRAFT ··· 🟡 TS_DRAFT)        ↓
                                                           ❌ BLOCKED

  from any status ──→ ❌ REJECTED     terminal · no edge leads out · the trace is kept
```

| Status | Meaning |
|--------|---------|
| ⬜ TODO | Task planned, HL not started |
| 📝 HL_DRAFT | HL being drafted, awaiting review/approval |
| 🔬 RES | Research in progress (optional — user can skip to TS_DRAFT) |
| 🟡 TS_DRAFT | TS written, awaiting approval for execution |
| 🟠 ONB | Onboarding: executor studying the task |
| 🟢 RF | Execution complete, RF written |
| 🔍 REV | Review: reviewer checking RF |
| 📚 KNW | Knowledge capture: tfw-docs + tfw-knowledge applied (optional — reviewer can pre-close with N/A) |
| ✅ DONE | Task closed, traces updated |
| ❌ BLOCKED | Blocked by dependency |
| ❌ REJECTED | Task closed unsuccessfully and permanently. Distinct from ❌ BLOCKED, which is waiting and resumes when the dependency clears. Terminal: no status follows it, and the task folder and its board row are never deleted. This is a task status — not the review verdict ❌ REJECT, and not the HL §12 amendment verdict ❌ REJECTED; neither of those is terminal |

Task Board format — ID column must be a relative link to the task folder:
```
| [PROJ-1](tasks/PROJ-1__title/) | Description | Status | ... |
```

Review verdicts:
- ✅ **APPROVE** — all ok → 📚 KNW (run tfw-docs + tfw-knowledge), then ✅ DONE
- 🔄 **REVISE** — specific issues → back to execution (same task)
- ❌ **REJECT** → 🛑 User decides: (a) 📝 HL_DRAFT (rework HL), (b) 🔬 RES (new research), (c) 🟡 TS_DRAFT (rewrite TS)

> **Branch (a) does not thaw the contract.** For an HL that is 🔒 FROZEN, "rework HL" means *file an
> amendment against the frozen sections* — a §12 row per change, with evidence, cost and an
> alternative, awaiting an owner verdict. Re-entry to `📝 HL_DRAFT` reopens the free sections only;
> a rejection is not a re-approval and does not unlock §1, §3, §4, §5, §6 or §7. Without this,
> REJECT is the one documented path that reopens frozen sections with no proposal and no log.
> Rules: §3 → HL Contract.

## 6) Scope Budgets (per Phase)

> Configured in `.tfw/project_config.yaml` (`tfw.scope_budgets`).
> Values below are defaults. Override in project_config.yaml for your project.

| Parameter | Default | Rationale | Config key |
|-----------|---------|-----------|------------|
| Files per phase | 30 | Agent maintains full context of changed files | `max_files_per_phase` |
| New files per phase | 15 | Limits blast radius of new abstractions | `max_new_files` |
| LOC per phase | 3000 | Keeps changes reviewable in one pass | `max_loc` |
| Modified files | 30 | Prevents scattered, hard-to-review diffs | `max_modified_files` |

## 7) Execution Modes

### CL (Chat Loop) — default
- AI proposes steps, human approves/executes.
- AI does NOT execute external actions without approval.

### AG (Autonomous) — explicit request only
- AI works independently within approved TS scope.
- Makes incremental commits.
- Stops when encountering issues not covered by TS.

## 8) Workflows

TFW defines the following canonical workflows in `.tfw/workflows/`:

| Workflow | Role | Purpose |
|----------|------|---------|
| [init.md](workflows/init.md) | Coordinator | Discover project → interview → knowledge → setup → verify |
| [plan.md](workflows/plan.md) | Coordinator | Research → HL → RESEARCH gate → scope decision → TS |
| [research/base.md](workflows/research/base.md) | Researcher | Structured investigation → RES artifact (pipeline or standalone) |
| [handoff.md](workflows/handoff.md) | Executor | Context load → ONB → execute → RF |
| [review.md](workflows/review.md) | Reviewer | Read RF → checklist → verdict → tech debt → traces |
| [resume.md](workflows/resume.md) | Coordinator | Locate task → status matrix → decide next phase |
| [docs.md](workflows/docs.md) | Coordinator | Update KNOWLEDGE.md and TECH_DEBT.md after task completion |
| [knowledge.md](workflows/knowledge.md) | Coordinator | Consolidate fact candidates into verified project knowledge (Orient → Gather → Consolidate → Prune) |
| [release.md](workflows/release.md) | Coordinator | Read RELEASE.md → scope release → version bump → CHANGELOG → tag |
| [update.md](workflows/update.md) | Coordinator | Fetch upstream → compare versions → categorize changes → update checklist → re-sync adapters |
| [config.md](workflows/config.md) | Coordinator | Interactive config change → propagate to all inline values |

## 9) Tool Adapter Pattern

`.tfw/` is the tool-agnostic core — one copy per project. Each development tool reads its own entry point, which references `.tfw/`:

```
CLAUDE.md ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.cursor/rules ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
.agent/rules ──→ "Read .tfw/README.md, follow .tfw/conventions.md"
AGENTS.md + .agents/skills/tfw-*/SKILL.md ──→ Codex `/tfw-*` command routing
```

Adapters are chosen at project init. See `.tfw/quickstart.md` for setup.

For Codex, `/tfw-*` is the primary human-facing command contract. Root `AGENTS.md`
provides always-on recognition and fallback routing; repository-local skills provide
discoverability and progressive workflow loading. Skills are implementation, not a
separate wrapper users must learn. Adapter source lives in `.tfw/adapters/codex/` and
installed copies live in `.agents/skills/tfw-*/`.

## 10) Context Loading Order (new session, strict)

1. `AGENTS.md`
2. `.tfw/conventions.md`, `.tfw/glossary.md`
3. `KNOWLEDGE.md` (if exists)
4. Relevant HL/TS/RF for the current task

## 10.1) Fact Categories

> Universal categories for Fact Candidates. Open list — agents can use custom categories when none fit.

| Category | Scope | Examples |
|----------|-------|----------|
| `environment` | Where the work lives | servers, tools, platforms, classrooms, labs, hosting |
| `process` | How work gets done, business processes | schedules, approvals, reporting cadence, grading cycles |
| `stakeholder` | Who needs what | priorities, pain points, expectations, quotes, key decisions |
| `constraint` | What limits exist | contractual obligations, regulatory deadlines, resource caps, technical limits |
| `convention` | Agreed standards | naming, style, format, language, tone |
| `domain` | Subject matter knowledge | revenue patterns, client segments, market metrics, business rules, curriculum |
| `context` | Background that shapes decisions | market conditions, competitive landscape, regulatory changes, prior decisions |
| `risk` | Known dangers | client concentration, market dependency, knowledge silos, fragile dependencies |
| `philosophy` | Values, principles, vision | design rationale, methodology beliefs, north star decisions, "why we do it this way" |

## 10.2) Knowledge Infrastructure

| File | Purpose |
|------|---------|
| `knowledge/` | Project root folder for topic files (per-category verified facts) |
| `knowledge/{category}.md` | Topic file — verified facts for a category. Template: `.tfw/templates/topic_file.md` |
| `.tfw/knowledge_state.yaml` | Consolidation tracking: last seq, date, statistics |
| `.tfw/workflows/knowledge.md` | 4-phase consolidation workflow (Orient → Gather → Consolidate → Prune) |
| `tfw.knowledge` in project_config.yaml | Configurable limits: interval, gate_mode, max_index_lines, max_facts_per_topic, max_topic_files |

## 10.3) File Classification in `.tfw/`

`.tfw/` contains three categories of files with different lifecycle rules:

| Category | Files | Init | Update | Owner |
|----------|-------|------|--------|-------|
| **Framework** | workflows/, templates/, conventions.md, glossary.md, README.md, CHANGELOG.md, VERSION, compilable_contract.md, quickstart.md, adapters/ | Copy from upstream | Overwrite/merge from upstream | Upstream repo |
| **State** | knowledge_state.yaml | Create from template | **NEVER** overwrite | Project (tfw-knowledge) |
| **Config** | project_config.yaml | Create from template → fill project values | Merge: framework sections update, project sections preserve | Project + upstream |

**Templates** for state and config files: `.tfw/templates/knowledge_state.yaml`, `.tfw/templates/project_config.yaml`.

**Rule:** `init.md` and `update.md` MUST respect these categories. State files are NEVER sourced from upstream — only from templates.

## 10.4) YAML File Naming Convention

All YAML configuration and state files in `.tfw/` use `lower_snake_case` naming:
- `project_config.yaml` (not `PROJECT_CONFIG.yaml`)
- `knowledge_state.yaml` (not `KNOWLEDGE_STATE.yaml`)

Markdown templates in `.tfw/templates/` also follow `lower_snake_case`:
- `topic_file.md` (not `TOPIC_FILE.md`)

Uppercase names are reserved for project-root documents (`KNOWLEDGE.md`, `TECH_DEBT.md`, `AGENTS.md`) and `.tfw/` framework docs (`CHANGELOG.md`, `VERSION`).

## 11) Quality Standard (no compromises)

- No placeholders.
- Results must be usable without manual edits.
- If a result is wrong — fix the prompt/context and retry until quality is met.
- Tasks are atomic and human-verifiable.
- **Content Language:** Template structure (headings, labels, field names) is always English.
  Artifact content is filled in the language specified by `tfw.content_language` in project_config.yaml.
  Default: `en`. Agent MUST check this value before writing artifacts.

### Design Rules

- **Token density**: workflow instructions ≤1200 words. Templates own format; workflows reference templates
- **Inline enforcement**: enforcement-critical values MUST be inline (Pattern A: defaults + config key). Pure refs (Pattern B) = broken
- **DNA/Library**: Role Lock + Mindset = always inline. Reference data = via ref-inside-step. Step self-contained, ref adds precision
- **Progressive Disclosure**: agent loads only what it needs now. Mode files loaded at Step 2, not at start

## 12) Safety and Execution Honesty

- In CL mode, never claim something was "run" or "tested" outside the session.
- Never request secrets in plain text. Use environment variables.
- Evidence requires real-environment observation — deploying, opening, running, or viewing completed work in conditions beyond the build/test toolchain. VERIFIED status requires an artifact reference (file path or inline output).

## 13) Trace Discipline

Every task produces an **RF file** with results, decisions, and observations. The **Task Board** in README.md tracks all task statuses. Together, these form the project's memory across sessions.

Reverting a result does not revert its trace. A rejected task's folder and its board row are never deleted: the work may leave the working tree, the record that the work happened stays.

## 14) Anti-patterns (prohibited)

- Executor starts coding before all blocking questions resolved
- Executor skips reading HL and goes straight to code
- Coordinator skips review and closes without REVIEW file
- RF file doesn't mention test results or observations
- TS is written without an approved HL
- Executor modifies Master HL without coordinator approval
- Executor makes architectural decisions not in HL
- Executor modifies files outside TS scope (even "obvious fixes")
- Executor does "bonus fixes" without documenting in RF deviations
- Executor writes RF before build/lint passes
- Executor sees tech debt / dead code but doesn't report in Observations
- Coordinator ignores executor Observations — must triage to TECH_DEBT.md
- Coordinator writes ONB, RF, or implements code → **Role Lock violation**
- Executor writes HL, TS, or changes scope → **Role Lock violation**
- Executor writes REVIEW file → **Role Lock violation**
- Reviewer approves without opening any files — Step 2 (Verify) requires spot-checking RF claims against actual artifacts
- A review checklist row is added without an evidenced firing rate — a row that cannot produce a finding is ceremony, and without a measured rate "it might catch something" is unfalsifiable. A row may be kept on consequence rather than frequency (a rare failure with asymmetric cost), and that reason must be written into the row
- Executor omits RF §7-9 (Fact Candidates, Strategic Insights, Diagrams) — sections are mandatory; empty content ("No X.") is valid, absent section is not
- Researcher omits Findings Map in RES — section is mandatory; "No findings map." is valid if genuinely no visualization relevant
- Coordinator reads KNOWLEDGE.md in context loading but never cites relevant items in HL §4 — "read but don't use" pattern breaks cross-task knowledge flow
- TS contains ready-made implementation — TS §5 must contain acceptance criteria (WHAT), not code or steps (HOW); implementation belongs to executor
- Coordinator reads own TS instead of RF when planning next phase — before writing TS for Phase N, read RF of the latest completed phase; plan ≠ fact
- Executor writes RF without opening template — RF template must be opened before writing; writing from memory drifts from required structure
- Coordinator answers ONB questions without source — when uncertain, present options and context, not decisions on behalf of the stakeholder
- Executor marks evidence VERIFIED without artifact reference in `evidence/` folder — assertion without evidence
- Executor marks evidence N/A without justification from TS Evidence field or documented reason
- Executor writes RF §5 Evidence before actually collecting evidence — evidence must be contemporaneous, not reconstructed
- Reviewer approves RF without checking that evidence artifact references resolve to real files or inline output
- Executor marks evidence DEFERRED without naming the specific blocker (missing environment, unavailable device, pending deployment)
- Anyone edits a frozen HL section without a §12 row carrying a logged owner verdict — the silent contract edit the amendment channel exists to replace
- Researcher submits HL recommendations without classifying each row as a refinement or an amendment proposal — one undifferentiated channel is how "risk probability is Medium" and "drop Phase B" arrive together
- Coordinator applies an amendment before its verdict — the proposal and the change become the same act, and the owner rules on something already done
- Research starts on an uncommitted approved HL — the baseline cannot be diffed, so drift becomes documented and permanently unverifiable
- Any role treats a remark inside a research thread, a review or a chat as an amendment verdict — a comment is input, a verdict is a distinct recorded act
- An agent cites its own delegation as authority to accept a scope or budget overrun — a mandate is a ceiling, and authority that extends itself is not authority
- A Phase HL authors its own acceptance criteria, failure conditions, vision or principles — a second, unapproved contract one level below the one that was ruled on
- A reviewer approves work that satisfies the TS but not the approved contract or the north star — the TS is downstream of any drift, so a green review against it can only confirm the drift
- A reviewer asserts alignment without citing the clause it serves — an unciteable claim is indistinguishable from a fabricated one, and a citation that resolves while being irrelevant is the same defect one layer in
- A whole-tree restore reverts the Task Board past a task's failure status — restoring every file to an older tree also restores rows to a state that never contained the newer ones, so the loss happens silently and nobody decides it

### 14.1 Terminology Origin (maintainer reference)

The following terms used in research stage templates are TFW-native and intentionally avoid methodology names:

| TFW Term | Meaning | Origin |
|----------|---------|--------|
| Dimension | An independent decision factor (degree of freedom) in the problem | Zwicky's GMA: "parameter" |
| Alternative | One valid value for a Dimension | Zwicky's GMA: "parameter value" |
| Configuration Space | The full cross-product of all Dimension alternatives | Zwicky's GMA: "morphological box" |
| Consistency Check | Pairwise incompatibility analysis eliminating invalid combinations | Zwicky's GMA: "cross-consistency assessment (CCA)" |
| Surviving Configuration | A configuration that passed all pairwise checks | Zwicky's GMA: "compatible solution" |

> **Scope:** This note is for framework maintainers only. The terms "Zwicky", "GMA", "General Morphological Analysis", "morphological box", and "cross-consistency assessment" MUST NOT appear in any researcher-facing template or workflow instruction.

## 15) Role Lock Protocol

Each workflow declares a **🔒 ROLE LOCK** at the top. The agent MUST refuse any action outside the locked role.

| Workflow | Role Lock | Permitted Artifacts | Forbidden Artifacts |
|----------|-----------|---------------------|---------------------|
| `init.md` | Coordinator | RES, RF, project config files | HL, TS, code |
| `plan.md` | Coordinator | HL, TS | ONB, RF, RES, REVIEW, code |
| `research/base.md` | Researcher | RES, research/ stage files | HL, TS, ONB, RF, REVIEW, code |
| `handoff.md` | Executor | ONB, RF, code | HL, TS, RES, REVIEW |
| `review.md` | Reviewer | review stage files (map.md, verify.md, judge.md), REVIEW | ONB, RF, HL, TS, code |
| `resume.md` | Coordinator | Status matrix, Phase HL, Phase TS | ONB, RF, RES, REVIEW, code |
| `docs.md` | Coordinator | KNOWLEDGE.md, TECH_DEBT.md | code |
| `release.md` | Coordinator | VERSION, CHANGELOG.md | code |
| `update.md` | Coordinator | `.tfw/` files, adapter copies | code |
| `config.md` | Coordinator | project_config.yaml, workflow files, convention files, adapter copies | code |

### Hard Stop Rule

When a Coordinator reaches the end of planning (TS approved), the correct action is:
1. Inform the user that planning is complete
2. Instruct: "Start `/tfw-handoff` to begin execution"
3. **Do NOT continue into execution**

When an Executor finishes RF, the correct action is:
1. Inform the user that execution is complete
2. Instruct: "Start `/tfw-review` to review the results"
3. **Do NOT write a REVIEW file**

When a Researcher finishes RES, the correct action is:
1. Inform the user that research is complete
2. Instruct: "Continue with `/tfw-plan` to apply research findings"
3. **Do NOT write HL or TS**

## 16) Compilable Contract

> Build-time specification for deterministic compilation of TFW artifacts into documentation.
> Defines the Source Manifest, Reference Format, and Output Structure.
> Full contract: [compilable_contract.md](compilable_contract.md)

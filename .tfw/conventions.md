# TFW Conventions

## 1) Purpose

TFW turns work (analytics, documents, code, research) into a reproducible process:
- context is captured,
- decisions are traced,
- results are repeatable,
- any agent can continue the project in a new session.

## 2) Required Artifacts (project root)

- `README.md` — human explanation: why/what/how, and a permanent route to the derived portfolio index. It carries no live task table and is not edited by a lifecycle transition.
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
- `.tfw/templates/status.md` — canonical task state carrier.
- `.tfw/templates/journal_event.md` — canonical journal event.
- `.tfw/templates/team_profile.md` — canonical participant profile.
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
| §7.2 | Knowledge Citations | HL | Input tracing: cite the exact PV clause/item read, link it, and state its concrete application |
| §7 | Knowledge Citations | ONB | Input tracing: confirm the exact HL §7.2 items read and how each applies; add new relevant items |
| _(section)_ | Knowledge Citations Verified | review/verify.md | Verification: check link resolution, item existence, semantic match, and relevance to the asserted application |

> **Unified naming rationale (D43/D28/D39):** cognitive mode is the same across all three — "report what you read and how it applies." Same mode = same name. Scan scope differs by role: Coordinator + Reviewer do full PV scan, Executor references coordinator's citations. See glossary.md → Project Values (PV).
>
> **Semantic integrity:** a citation that resolves to a real file or anchor but names an absent, irrelevant,
> or semantically different item is a discrepancy, not a verified citation. Priorities 0 and 1 must be
> recorded and checked as distinct meaning even when one README contains both.

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

## 4) Task Identity and Location

### Where tasks live

`tfw.task_containers` in `.tfw/project_config.yaml` is an **ordered list** of container paths.
A task is **created** in the first entry; a task is **resolved** by searching every entry in
order. That is one setting, not two supported layouts.

```
{container}/{YYYY}/{id}__{slug}/
```

The year is the year the task was **created**, and it never changes. A task opened in December
and closed the following March stays in the earlier folder. Recomputing it would move a
directory, and moving a directory breaks every reference into it.

**No lifecycle state is expressed by moving a directory.** Not `TODO`, not `DONE`, not
`REJECTED`. A path is created once and outlives every state the task passes through. Status
lives in the task's own `status.md`; a folder move would ask a sync engine to relocate a
directory other participants may be writing inside, and would invalidate references that
already resolve.

A project migrating from a pre-2.0.0 layout lists its old container second. Its existing
tasks are not renamed, not moved and not reorganized: both identifier grammars stay readable
everywhere, and the old paths keep resolving.

### Identifier

```
YYYYMMDD-HHMMSS__slug        the whole directory name IS the identifier
```

**The timestamp alone is not an identifier.** Two participants offline from each other can
reach the same second; only the slug tells them apart, so a bare `YYYYMMDD-HHMMSS` cannot
name exactly one task and no consumer may accept one as if it did. Every reference, commit
subject and index row carries the full identifier.

**No participant reads a project-wide maximum to learn which identifier is free.** There is no
counter, no registry and no allocation step. Creating a task reads no other task directory —
which is what lets two people offline from each other create tasks that cannot collide.

**Two tasks created in the same second do not collide unless their slugs also match.**
Including the slug is what makes the offline-uniqueness promise satisfiable at all: the
alternative — an identifier that is only a second — demands uniqueness of a value two people
can reach independently, which no rule can deliver without shared state.

Same second **and** same slug means two participants created the same task. That is a signal
worth surfacing, not a defect to prevent; the two directories are identical in name and merge
as one.

Creation is a create-or-fail on the directory: if it already exists, take a **new actual
timestamp**, never reuse and never overwrite. The retry is **bounded** by
`tfw.id_max_retries` and then fails visibly — a wall clock that steps backwards (an NTP
correction, a resumed machine, a restored image) can otherwise re-offer a used value forever.

None of this is a project-wide read. It consults no counter, no maximum and no other task's
contents: one existence check at the moment of the write, which is what lets two participants
offline from each other stay safe with nothing shared between them.

The legacy grammar `{PREFIX}-{seq}` is still read by every consumer and is never issued again.
`tfw.task_prefix` is retained only so old identifiers resolve.

### Task control files

| File | What it is |
|------|------------|
| `{task}/status.md` | **The only authority for that task's live state.** Closed key set, bounded fields, no free-text body. Template: `.tfw/templates/status.md` |
| `{task}/journal/{YYYYMMDD-HHMMSS}__{kind}__{actor}.md` | One event, immutable once written. The filename **is** the event identifier — nothing allocates it. Template: `.tfw/templates/journal_event.md` |
| `team/{handle}.md` | One participant, human or agent. Declared attribution, never authentication. Template: `.tfw/templates/team_profile.md` |

**The actor is part of the event filename**, because it is the only field that separates two
concurrent writers: `on_behalf_of` names the same accountable person for both, and `via`
names the same provider for two sessions of one tool. Without it, two participants recording
the same kind of event in the same second produce one filename and one event is lost
silently. If that exact filename already exists — one actor writing twice inside a second —
take the next actual second; never a counter, because a counter is the shared state this
model exists to remove.

The timestamp is **read from the system clock at the moment of writing** and is never
composed, guessed, rounded or typed. A typed timestamp destroys the ordering the journal
exists to provide.

A written event is never edited and never deleted; a correction is a new event that
references the one it corrects. A rule introduced later may describe older entries but never
rewrite them.

Every event carries three identity fields, answering three different questions:

| Field | Answers | Value |
|---|---|---|
| `actor` | who performed it | a `team/` handle — a person, or an agent's own name |
| `on_behalf_of` | who is accountable | **always a human handle.** Whoever launched it answers for it |
| `via` | what produced it | provider family — `claude`, `codex`, `gemini`; absent for a hand edit |

**An event without `on_behalf_of` is invalid and is refused.** There is no such thing as a
record nobody answers for; when a person acts directly, `actor` and `on_behalf_of` are the
same handle and the repetition is deliberate. **A provider name is never an actor** — two
sessions of one tool are two writers and need two names.

### Artifact file naming

| Artifact | Format | Example |
|----------|--------|---------|
| Master HL | `HL-{ID}.md` | `HL-20260826-143000__query_redesign.md` |
| Single-phase RES | `RES__{ID}.md` | `RES__20260826-143000__query_redesign.md` |
| Single-phase TS | `TS__{ID}.md` | `TS__20260826-143000__query_redesign.md` |
| Single-phase RF | `RF__{ID}.md` | `RF__20260826-143000__query_redesign.md` |
| Single-phase ONB | `ONB__{ID}.md` | `ONB__20260826-143000__query_redesign.md` |
| Single-phase REVIEW | `REVIEW__{ID}.md` | `REVIEW__20260826-143000__query_redesign.md` |
| Single-phase EV | `EV__{ID}.md` | `EV__20260826-143000__query_redesign.md` |
| Phase RES | `RES__phase-{x}__{title}.md` | `RES__phase-a__conventions.md` |
| Phase TS | `TS__phase-{x}__{title}.md` | `TS__phase-a__conventions.md` |
| Phase RF | `RF__phase-{x}__{title}.md` | `RF__phase-a__conventions.md` |
| Phase ONB | `ONB__phase-{x}__{title}.md` | `ONB__phase-a__conventions.md` |
| Phase REVIEW | `REVIEW__phase-{x}__{title}.md` | `REVIEW__phase-a__conventions.md` |
| Phase EV | `EV__phase-{x}__{title}.md` | `EV__phase-a__conventions.md` |

**`{ID}` is the task's whole identifier**, and it means the same thing everywhere: in a path,
in a filename, in a reference and in `status.md`. For a clock task that is
`20260826-143000__query_redesign` — the slug is already part of it, so **no title is appended**.
Appending one produces a doubled slug and a name this contract rejects.

A legacy task keeps `{PREFIX}-{N}`, where the identifier does *not* carry a slug, so its
historical filenames have the form `RES__TFW-60__conflict_resistant_shared_workspace.md`.
Those files are never renamed; the two-part form is history, not a second rule.

> **Rule:** ALL artifact filenames MUST include the task ID or Phase identifier. A filename
> without either is an error.

### Discovery

`{first container}/00-INDEX.md` is a **derived** portfolio view, generated by
`docs/scripts/gen_index.py` from task state. It declares that it is derived, names its source
count and its freshness, and reports every legacy, malformed or unresolved input rather than
dropping it.

It is never authoritative. A workflow acting on a selected task **re-reads that task's
`status.md` first**. Absent, stale or malformed, the index degrades discovery and changes no
task state — the project stays workable and says visibly that the view is behind.

The `00-` prefix is a hint at position, not a promise: file managers that group directories
before files place the year folders above it. The guaranteed entry point is the route in the
root `README.md`.

### Commit Attribution

Every AI-authored commit MUST use `[agent/task/scope/role] summary`: set `agent` to the lowercase AI product name from explicit context, `task` to the canonical TFW task ID (`project` only when none exists), `scope` to the established lowercase work-slice slug or a lowercase hyphenated form of its explicit label, and `role` to the lowercase canonical TFW workflow owner from §15/Role Lock; keep `summary` short and imperative, commit locally, and push only after explicit user approval.

Example: `[codex/TFW-50/task/coordinator] define minimal commit attribution`

### Research subfolder

Research artifacts live in a single `research/` container at task root. Each iteration gets its own numbered subfolder:

```
{task}/research/
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

Every task directory (or phase directory for multi-phase tasks) MUST contain an `evidence/` subfolder. The subfolder always contains at least one structured EV file (`EV__{ID}.md` or `EV__phase-{x}__{title}.md`). Additional binary artifacts (screenshots, API responses, logs) go into the same `evidence/` folder and are indexed in the EV file's Attachments section. Template: `.tfw/templates/evidence/EV.md`.

### Multi-phase folder structure

For multi-phase tasks, master artifacts (HL, RES) stay at task root. Each phase gets a subfolder:

```
{container}/2026/20260826-143000__query_redesign/
  status.md                           ← Live state — the authority for this task
  journal/                            ← One immutable file per event
    20260826-143000__created__saubakirov.md
    20260901-091500__handoff__saubakirov.md
  HL-20260826-143000__query_redesign.md   ← Master HL
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
   multi-phase:  ⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🧩 PHASES → 📚 KNW → ✅ DONE   (each phase runs the full flow in its own status.md)
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
| 🧩 PHASES | The task is multi-phase and its phases are running. **A task-level rollup of phase state is prohibited** — each phase carries its own `status.md`, and a summary would be a second fact that must agree with them |
| 🟡 TS_DRAFT | TS written, awaiting approval for execution |
| 🟠 ONB | Onboarding: executor studying the task |
| 🟢 RF | Execution complete, RF written |
| 🔍 REV | Review: reviewer checking RF |
| 📚 KNW | Knowledge capture: tfw-docs + tfw-knowledge applied (optional — reviewer can pre-close with N/A) |
| ✅ DONE | Task closed, traces updated |
| ❌ BLOCKED | Blocked by dependency |
| ❌ REJECTED | Task closed unsuccessfully and permanently. Distinct from ❌ BLOCKED, which is waiting and resumes when the dependency clears. Terminal: no status follows it, and the task folder and its board row are never deleted. This is a task status — not the review verdict ❌ REJECT, and not the HL §12 amendment verdict ❌ REJECTED; neither of those is terminal |

Status lives in the task's own `status.md` and nowhere else. A transition is one write, inside
one task directory — which is what lets two tasks advance at the same time without their
authors meeting in a shared file. The lifecycle value must be one of the ids above, or
`UNDECLARED` carrying the source value verbatim (→ glossary.md).

### A phase carries its own state

A task with phase directories carries one `status.md` **inside each phase directory**, on the
same closed schema — nothing new is learned in order to read it. Its owner is that phase's
owner, and two phases running under two owners write two different files.

**The task-level `lifecycle` never summarizes phase state.** A rollup is a fact that has to
agree with other files, which is exactly the synchronization problem the carrier already
forbids: two files that must agree is what previously required an engine to solve. The task
file describes the task's own arc and nothing more:

```
TODO → HL_DRAFT → RES → 🧩 PHASES → KNW → DONE
```

While `PHASES` stands, *which* phase is where is answered by reading that phase's own state —
which is the same answer the board's per-phase columns used to give, without a shared table.

A phase state file is created when its phase directory is created, never in advance.

A material transition is also recorded as a journal event, so the *why* survives the session
that decided it. The state file says where the task is; the journal says how it got there.

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

Every task produces an **RF file** with results, decisions and observations, a **`status.md`** carrying its live state, and a **`journal/`** recording the events that moved it. Together with the derived portfolio index, these form the project's memory across sessions — and because each lives inside its own task, two tasks can advance without their traces colliding.

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
- A whole-tree restore reverts task state past a task's failure status — restoring every file to an older tree also restores state files to a state that never contained the newer ones, so the loss happens silently and nobody decides it
- A workflow acts on a task using the derived index instead of re-reading that task's `status.md` — the index may be stale by construction, and acting on it makes a projection authoritative
- A task directory is moved to express its status, or corrected into a different year folder — the year is the year of creation, and a move breaks every reference that already resolves
- An identifier is allocated by reading a project-wide maximum, a counter or another task's directory — that read is exactly what makes two offline participants collide
- A journal event is edited or deleted after it was written — a correction is a new event; rewriting one erases the record the journal exists to keep
- A journal event copies HL, RES, TS, RF, REVIEW, evidence or chat text instead of referencing it — this is how the journal becomes the next unbounded shared file
- A status value outside the declared vocabulary is normalized into one that is inside it — the listing looks tidier and a recorded fact has been silently rewritten
- Identity is inferred from an OS username, hostname, folder name or account display string — a machine does not know who is sitting at it, and the guess becomes a durable attribution nobody made
- A per-user file is kept on the shared tree — gitignored is not sync-ignored, so under file synchronization it reaches every participant

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

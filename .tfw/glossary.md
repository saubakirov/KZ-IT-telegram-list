# TFW Glossary

## Execution Modes

### CL (Chat Loop Mode)
Default mode. AI proposes steps, user approves/executes. AI does NOT run external commands without approval. Used for: task planning, code review, architecture decisions, any work touching external systems.

### AG (Autonomous Mode)
AI works independently within the file system. Only for pre-approved scope (e.g., executing an approved TS). Must fail safely if context is missing.

## Artifact Types

> Full definitions, naming rules, and format requirements → [conventions.md](conventions.md) §3

### HL (High Level)
Context/frame artifact for a task — the "map of meaning". → conventions.md §3

### RES (Research Report)
Structured investigation artifact for the RESEARCH stage. Living document: decisions at top, stage logs below. → conventions.md §3

### TS (Task Spec)
Task definition for a single phase. Self-contained: scope, steps, acceptance criteria. → conventions.md §3

### RF (Result File)
Results, decisions, artifacts. RF has priority as source of truth. Contains mandatory Observations table. → conventions.md §3

### ONB (Onboarding Report)
Structured executor report before starting work: understanding, blocking questions, risks, inconsistencies. → conventions.md §3

### REVIEW (Review Report)
Formal reviewer report after reviewing RF: 4-stage process (Map → Verify → Judge → Decide) with stage files as evidence, verdict (APPROVE/REVISE/REJECT), tech debt triage. Synthesized from `review/map.md`, `review/verify.md`, `review/judge.md`. → conventions.md §3

### TECH_DEBT.md
Accumulated tech debt registry. Fed by: executor Observations in RF → coordinator triage in REVIEW → append to TECH_DEBT.md.

### KNOWLEDGE.md
Project knowledge index (optional). Central map of architecture, decisions, legacy, and principles. Updated via `tfw-docs` workflow. Principle: index, don't duplicate.

### RELEASE.md
Optional project-level artifact defining release strategy (audience, triggers, version scheme, checklist). Template: `.tfw/templates/RELEASE.md`.

## Contract and Purpose Defence

### HL Contract
The state an HL enters when the owner approves it: §1, §3, §4, §5, §6 and §7 freeze; §2, §7.2 and §8–§11 stay free; §12 becomes append-only. Carried by the header `Contract` field, which tracks the artifact — task status tracks the pipeline. → conventions.md §3 HL Contract

### Contract Baseline
The commit carrying the approved HL — the point a frozen section is diffed against. It lives in the commit subject through the reserved `freeze` scope word, never in the file: no header field can name its own commit. Re-frozen after every approved amendment. → conventions.md §3 rules 13-16

### Frozen Section
An HL section locked by owner approval. The frozen unit is the declarative claim, not the section text — rewording a claim is not an amendment, changing what it commits to is. Editing one outside §12 is prohibited for every role, the coordinator included. → conventions.md §3 rules 3, 5

### Amendment
A proposal to change a frozen claim, ruled by an explicit owner verdict. Without evidence, cost and a considered alternative it is not a proposal. `Type` states relation to the baseline — `EXTEND` adds, `SUPERSEDE` replaces, `RESTRICT` narrows — never disposition, which belongs in `Verdict`. → conventions.md §3 rules 10-12

### Amendment Log
HL §12: the append-only table carrying every amendment and its verdict. Rows are never deleted, rewritten or renumbered, so a refused proposal stays visible as an attempt — that visibility is the point. Renders `No amendments.` rather than being absent. Its ❌ REJECTED verdict refuses a proposal, not a task — the terminal task status of the same name is conventions.md §5. → conventions.md §3 rule 4

### Project North Star
The layer above every task HL: what the product is for, and what it must never become. Locus is designated section(s) of a README — never a task HL. Payload: purpose, principles and non-goals. PV priority 0; optional, with a declared fallback. → conventions.md §3 Project North Star

### Purpose Check
Judge row 2 clause (a) — does the work serve what the project set out to do? Reference set: the contract baseline plus the Project North Star, never the TS and never a Phase HL. One field quotes the clause served and names the concrete harm. → `templates/review/judge.md`

### not fit for purpose
The Purpose Check's failure finding. It grounds ❌ REJECT with every quality check passing, and routes to the owner rather than back to the executor. *"The TS scoped it this way"* and *"tests are green"* are not sufficient grounds to approve. → `templates/review/judge.md`

### Deferral confession
The second of the Purpose Check's three tests: does the spec or the result itself name a different home for this work and ship it here anyway? A misfit the author already noticed is still a misfit. → `templates/review/judge.md` Purpose Check

## Knowledge Terms

### Fact Candidate
Raw observation about the project recorded during work in an artifact's Fact Candidates section. NOT a verified fact — becomes a fact after `/tfw-knowledge` consolidation. Quality filter: "Would the next agent decide differently knowing this?" Categories: → conventions.md §10.1

### Strategic Insight
Human-sourced domain knowledge captured with deep analytical synthesis. Appears in three contexts with qualifiers: HL §11 "Strategic Insights (Planning)", RF §8 "Strategic Insights (Execution)", RES "Strategic Insights (Research)". The agent's cognitive mode: capture the insight, then ADD implications — what does it mean for the project? High-value signals: user corrections, emotional statements, vision framing, alternative selection. Contrast with Fact Candidate (pure reporting, no interpretation).

### Value Flow
Visual section in HL template (§3.2). Visualizes HOW value gets created — the process from user pain through pipeline steps to value delivered. Cognitive mode: strategic/value-oriented (INPUT→PROCESSING→OUTCOME). Distinct from §3.1 Result Visualization (outcome preview). → conventions.md §3 Visual Sections

### Result Visualization
Visual section in HL template (§3.1). Shows the finished outcome written from the finished state, rendered visually — prose alone does not satisfy it. It carries the value, not only the artifact. The owner's checkpoint before the spend, not an illustration of the plan. → conventions.md §3 Visual Sections

### Findings Map
Visual section in RES template. Visualizes research findings: root cause analysis, hypothesis trees, priority matrices, relationship maps between discoveries. Cognitive mode: analytical/research. → conventions.md §3 Visual Sections

### Per-template Naming
Design principle: when a section's cognitive mode differs across templates, use a different section name per template. When the mode is the same — use a unified name. Applied to: visual sections (per-template: Value Flow, Diagrams, Findings Map) vs knowledge capture sections (unified: Fact Candidates, Strategic Insights). Decision criterion: "Does the cognitive mode CHANGE between templates?" → conventions.md §3 Visual Sections

## Evidence Terms

### Evidence
Real-world verification of completed work in its intended environment. Separate from Verification (RF §4 — synthetic tool output: lint, test, build). Evidence requires observable outcomes — deploying, opening, running, sending, or viewing the result in conditions beyond the build/test toolchain. Three-role pipeline: coordinator designs (TS Evidence field), executor collects (RF §5), reviewer audits (REVIEW / verify.md). → conventions.md §3 Evidence Sections

### Evidence Plan
The coordinator-authored `Evidence:` field in TS §5 Acceptance Criteria items. Specifies what live verification is needed for each AC, what environment and tools are suggested, and what constitutes sufficient proof. Follows MAY-deviate pattern (executor can adjust with justification in RF). When evidence is unnecessary for a trivial AC, coordinator writes `Evidence: N/A`. → `templates/TS.md` §5

### Evidence Collection
The executor activity in handoff.md Step 11 (between build gate and Pre-RF Gate). The executor runs, deploys, opens, or views the completed work in real conditions and captures artifacts (screenshots, logs, command output). Results recorded in RF §5 Evidence table with status vocabulary. If no TS AC items have Evidence fields — step is skipped entirely. → `handoff.md` Step 11

### Evidence Audit
The reviewer verification of evidence artifacts during the review process. Performed in verify.md (Evidence Verification section: check that RF §5 artifacts exist and match claims) and judge.md (Check #7: all TS Evidence fields covered in RF §5). → `templates/review/verify.md`, `templates/review/judge.md`

### Evidence Status Vocabulary
Fixed 4-status vocabulary for evidence results in RF §5. No custom statuses permitted.
- **VERIFIED** — outcome observed in real environment with artifact reference (file path or inline output)
- **DEFERRED** — evidence cannot be collected now; must name the specific blocker (missing environment, unavailable device, pending deployment)
- **BLOCKED** — evidence collection is impossible due to external constraint beyond executor control
- **N/A** — TS Evidence field was N/A or AC does not require real-world verification

→ conventions.md §3 Evidence Sections, §12 Safety and Execution Honesty

## Commit Attribution

A declared structured prefix in the first-line subject of an AI-authored commit for searchable trace context; it is separate from Git author/committer metadata, is not actor authentication, and does not classify unmarked commits as human-authored. The canonical rule is in [conventions.md](conventions.md) §4.

## Task Naming

Format: `{YYYYMMDD-HHMMSS}__{short-title}`, and the whole name is the identifier. Legacy tasks keep `{PREFIX}-{N}__{short-title}` and are never renamed. Full naming rules → conventions.md §4

## Status Flow

Full status diagram, transitions, and review verdicts → conventions.md §5

```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → 📚 KNW → ✅ DONE
```

10 pipeline statuses: TODO, HL_DRAFT, RES, PHASES, TS_DRAFT, ONB, RF, REV, KNW, DONE. `PHASES` belongs to a multi-phase task only, and never summarizes what its phases are doing. RES and KNW are optional. Two statuses sit outside the pipeline: ❌ BLOCKED — waiting, the task resumes when the dependency clears; ❌ REJECTED — closed unsuccessfully, terminal, the trace is kept. `❌ REJECTED` here is a **task status** — not the review verdict `❌ REJECT`, and not the HL §12 amendment verdict `❌ REJECTED`; neither of those is terminal.

**The legend.** This is the full declared vocabulary, and it lives here — with the terms it defines — rather than beside a table of tasks. It moved here at 2.0.0 when the root Task Board was removed.

| | Status | Meaning |
|---|---|---|
| ⬜ | `TODO` | registered, work not started |
| 📝 | `HL_DRAFT` | the HL is being drafted or discussed |
| 🔬 | `RES` | research in progress — optional |
| 🧩 | `PHASES` | a multi-phase task whose phases are running; each phase has its own `status.md` |
| 🟡 | `TS_DRAFT` | the TS is written, awaiting approval |
| 🟠 | `ONB` | the executor is onboarding |
| 🟢 | `RF` | execution complete, the RF is written |
| 🔍 | `REV` | review in progress |
| 📚 | `KNW` | knowledge capture — optional |
| ✅ | `DONE` | closed, terminal |
| ❌ | `BLOCKED` | waiting on a dependency, resumes when it clears |
| ❌ | `REJECTED` | closed unsuccessfully, terminal, the trace is kept |

### UNDECLARED
Not a status anyone selects. A task carrier records `UNDECLARED` when its source held a value outside the vocabulary above, and keeps that value verbatim in `lifecycle_verbatim`. A consumer treats it as non-actionable and reports it. **Normalizing such a value to a declared one is prohibited** — it would silently rewrite a recorded fact to make a listing look tidy. `❄️ FROZEN` in the 2.0.0 board snapshot is the worked example.

### KNW (Knowledge Capture)
Post-review status indicating docs and knowledge workflows have been applied. Triggered after REVIEW ✅ APPROVE. Markers in REVIEW §4: `tfw-docs: Applied/N/A`, `tfw-knowledge: Applied/N/A`. Both markers set → status transitions to ✅ DONE. For trivial tasks, reviewer pre-marks both as N/A during review. → conventions.md §5

## Concept Taxonomy

| Concept | Definition | Where it lives |
|---------|------------|----------------|
| **Document Type** | Type of artifact: HL, RES, TS, ONB, RF, REVIEW | glossary.md (Artifact Types) |
| **Template** | Canonical format for a document type | `.tfw/templates/` |
| **Workflow** | Tool-agnostic process description (plan, research, handoff...) | `.tfw/workflows/` |
| **Adapter Command** | Tool-specific invocation of a workflow (slash-command, skill) | `.claude/commands/`, `.agent/workflows/`, `.agents/skills/tfw-*/SKILL.md` (Codex) |
| **Status** | Process status of a task on the board | `project_config.yaml` `tfw.statuses` |

## Roles

### User (Human)
Approves HL and TS before execution. Provides secrets via env vars. Reviews RF outputs. Final authority on task closure.

### Coordinator (AI)
Writes HL and TS. Advances task state and appends coordination events to the task's journal. Hands off to researcher, executor, and reviewer.

### Researcher (AI)
Dedicated research agent. Writes RES and stage files in `research/` subfolder. Follows OODA loop per stage. Hard Stop: after writing RES, says "Research complete. Continue with `/tfw-plan`."

### Executor (AI)
Reads approved TS. Writes ONB before starting. Implements changes. Makes incremental commits. Writes RF documenting results. Reports observations (tech debt, issues).

### Reviewer (AI — coordinator under the reviewer Role Lock)
Reads RF and TS (for DoD verification). Creates review stage files (map.md, verify.md, judge.md) then synthesizes into REVIEW file using one universal 10-row Judge checklist — every row asked in every review, with explicit `⚪ N/A` where a row does not apply. Triages executor Observations → TECH_DEBT.md. Cannot: write code, write ONB, write RF, modify HL/TS.

## Execution Gates

### Acceptance Criteria (TS)
The required-outcomes section (§5) of a TS file. Defines WHAT the result must achieve, with a verifiable gate per item. Uses `[depends: AC-X]` annotations to express prerequisite relationships. Contrast with Technical Guidance (§6 — reference material) and Definition of Failure (§7 — hard reject conditions). → `templates/TS.md` §5

### Technical Guidance (TS)
The reference-material section (§6) of a TS file. Provides context, patterns, and constraints to inform the executor's approach. Explicitly NOT implementation instructions — the executor MAY deviate with justification in RF. Contrast with Acceptance Criteria (§5), which states WHAT must be achieved. → `templates/TS.md` §6

### Definition of Failure (TS)
The hard-reject section (§7) of a TS file. Lists specific conditions that, if present in the RF, constitute grounds for an automatic REJECT verdict. Any triggered item means the RF must be revised before review can proceed. Reviewer uses this section as a first-pass filter in the Judge stage. → `templates/TS.md` §7

### Principles Check
The TS §3 table mapping each HL §7 principle to a specific Acceptance Criteria item and a verifiable gate. Ensures HL principles are structurally enforced rather than left as decorative text. Reviewer verifies this table during the Judge stage. → `templates/TS.md` §3, `review.md` Step 3

### AC Dependency Annotation
The `[depends: AC-X]` syntax used in TS §5 to mark prerequisite relationships between Acceptance Criteria items. When present, triggers an Execution Loop: the dependent AC may not begin implementation until the prerequisite AC gate has been verified. → `templates/TS.md` §5, `handoff.md` Phase 2

### Execution Loop
The self-verification cycle triggered when TS AC items carry `[depends: AC-X]` annotations. The executor verifies the prerequisite AC gate passes before starting implementation of the dependent AC. Independent ACs (no `[depends]`) may be implemented in any order. Purpose: catch dependent-chain failures at execution time, not at review. → `handoff.md` Phase 2 Step 8

### Pre-TS Gate
Coordinator gate in `plan.md` Step 7: before writing the TS for any phase after the first, read the RF of the latest completed phase in the dependency chain. Ensures the TS is written against actual output (RF), not against the coordinator's prior plan (TS N-1). Addresses the plan≠fact drift failure mode observed in HD-18. → `plan.md` Step 7 (3b), `conventions.md` §14

### Pre-RF Gate
Executor gate in `handoff.md` Phase 3: before writing the RF, open `.tfw/templates/RF.md` and read all section headings. Ensures the RF follows the template structure and no mandatory sections are omitted from memory. Addresses the RF drift failure mode observed in HD-9. → `handoff.md` Phase 3 Step 11

### Session Naming
Step 0 convention present in every TFW workflow: name the current session as `Role | Task-ID | Phase` (e.g., `Executor | TFW-41 | Phase D`) before doing anything else. Enables navigation across sessions and enforces role awareness at the start of each session. → `handoff.md` Step 0, `plan.md` Step 0, `review.md` Step 0

### Phase Dependencies
The HL §4 section that visualizes phase execution order as a mermaid graph plus a dependency table (Depends on, Shared files, Can run in parallel with). Enables any coordinator to understand phase sequencing and write a Phase TS without reading all prior phases. → `templates/HL.md` §4

## RESEARCH
Stage between HL and TS in the pipeline. Structured investigation: gathering information, extracting hidden knowledge, critical analysis. Produces recommendations in pros/cons format for coordinator decision. Can also run standalone via `/tfw-research`. Produces a RES artifact.

## Stage (Research)
One thematic block within RESEARCH: Gather, Extract, or Challenge. Each stage ends with a checkpoint. Stages form a checklist — the agent must cover all three, but the order is flexible.

## Pass (Research)
A full round-trip across all three RESEARCH stages. Each stage runs an OODA loop with a sufficiency verdict at the end. Minimum 1 pass required. Additional passes cover stages that need deeper investigation (recommended max: 3 passes).

## Iteration (Research)
One full round of `/tfw-research` within a multi-iteration task. Each iteration has its own subfolder (`research/iterN/`), its own RES file (`research/iterN/RES.md`), and a mandatory Iteration Status block. Iteration 1 = standard research. Iteration 2+ = builds on predecessor findings, addresses open threads and gaps. Minimum iterations configurable via `tfw.research.min_iterations` in project_config.yaml (default: 2). → conventions.md §4 Research subfolder

## iterations.yaml
Control file inside the `research/` subfolder for multi-iteration research. Created by coordinator in `plan.md` Step 6b. Contains: `task_id`, `title`, `min_iterations`, `max_iterations`, and an `iterations` array tracking each iteration's number, focus, hypotheses, status, and RES file path. Optional fields: `agent` (free-text — which tool/agent ran the iteration, for traceability) and `sources` (list — what source categories were consulted). Coordinator owns this file — researchers read it, coordinator updates it. → conventions.md §4 Research subfolder

## min_iterations
Configurable hard floor for research iterations. Default: 2 (from `tfw.research.min_iterations` in project_config.yaml). Coordinator gate in `plan.md` Step 6c blocks TS until this many iterations complete. Coordinator can override per task in `iterations.yaml`. Rationale: researchers optimize for speed, structural enforcement ensures minimum depth. → plan.md Step 6c

## Read-only AG
A mode within RESEARCH where the agent autonomously reads project files and web sources but writes only to the RES artifact. No code changes, no other file modifications.

## Research — Dimensional Analysis

### Dimension (Research)
An independent decision factor in the problem space, identified during the Gather stage. Each Dimension has ≥3 Alternatives. Dimensions feed into the Configuration Space in the Extract stage. When fewer than 3 independent Dimensions exist, use a comparison matrix in Gather instead — Extract and Challenge adapt accordingly. → `templates/research/gather.md`, `research/base.md` Step 5

### Alternative (Research)
One valid value for a Dimension, identified during the Gather stage. Alternatives within a Dimension must be mutually exclusive and collectively cover the realistic options. A Dimension with ≥3 Alternatives is required to construct a Configuration Space in Extract. → `templates/research/gather.md`, `research/base.md` Step 5

### Configuration Space (Research)
The cross-reference table built in the Extract stage by mapping all Gather Dimensions against each other. Makes combinations visible that would not be seen in isolation. Incomplete Dimensions in Gather make the Configuration Space impossible to fill — the cross-stage dependency is a natural enforcement mechanism. → `templates/research/extract.md`, `research/base.md` Step 5

### Consistency Check (Research)
The pairwise incompatibility analysis performed in the Challenge stage to eliminate invalid combinations from the Configuration Space. Two configurations are incompatible if they cannot coexist given domain constraints. Configurations that fail any check are eliminated. Surviving Configurations proceed to RES synthesis. → `templates/research/challenge.md`, `research/base.md` Step 5

### Surviving Configuration (Research)
A configuration from the Configuration Space that has passed all pairwise Consistency Checks in the Challenge stage. Surviving Configurations represent the viable options that the RES presents for coordinator decision. → `templates/research/challenge.md`, `research/base.md` Step 5

## Phase
A bounded unit of work within a multi-phase task. Each phase has its own HL → TS → ONB → RF → REVIEW cycle. Named with letters (A, B, C) or numbers. Subject to scope budgets (→ conventions.md §6).

## Multi-phase Handoff
Convention for tasks with 3+ phases: master HL §4 includes a Context block per phase (Requires, Shared files, Key decisions, Deliverables) enabling independent coordinators to write Phase HL without reading all research. → `templates/HL.md` §4, `plan.md` Step 7.

## Scope Budget
Limits per phase calibrated for AI executor agents. Exceeding limits degrades quality. When exceeded — split the phase. Values → `tfw.scope_budgets` in project_config.yaml.

## Topic File
Per-category knowledge file in the `knowledge/` folder. Contains verified facts in a structured table. Template: `.tfw/templates/topic_file.md`. Updated by `/tfw-knowledge` consolidation.

## Knowledge Gate
Periodic consolidation checkpoint in Step 2 of `plan.md`. Mode configurable: `hard` (stop + justification), `soft` (reminder only), `off` (skip). → `tfw.knowledge.gate_mode` in project_config.yaml.

## Consolidation
4-phase process for converting Fact Candidates into verified project knowledge: Orient → Gather → Consolidate → Prune. Executed via `/tfw-knowledge` workflow.

## Project Values (PV)
The complete set of accumulated project context that MUST inform decisions. When someone says "check values", "check against experience", or "verify alignment" — scan the PV Index. Project Values include beliefs, validated principles, architecture decisions, agreed standards, and known anti-patterns. Not just moral values — everything that has VALUE for making decisions.

### PV Index (scan order)

| Priority | Source | What it contains |
|----------|--------|-----------------|
| 0 | **Project North Star** — designated README sections; in this starter: root `README.md` opening / § How It Works and `.tfw/README.md` `NS1`–`NS3` | What we are building, why, and **what we are deliberately not building**. Distinct in kind from everything below it: priorities 1-7 all describe *how we build*. Defined in `conventions.md` §3. A project may not have one — fall back to the master HL §1 at its contract baseline; a review is never blocked on a missing north star |
| 1 | `.tfw/README.md` § Methodology values / § Success Criteria — **methodology** values and outcomes | How TFW work is practiced and what observable success looks like: candor, structural enforcement, naming, portability, complete bounded results, honest claims, owned truth, authorized resumption, traceable material decisions, and verified knowledge compounding |
| 2 | `knowledge/philosophy.md` | Validated principles and design rationale |
| 3 | `KNOWLEDGE.md` §1 | Architecture Decisions (D-records) |
| 4 | `conventions.md` §3, §11, §14 | Naming rules, Design rules, Anti-patterns |
| 5 | `knowledge/convention.md` | Agreed standards and patterns |
| 6 | `knowledge/process.md` | Process facts and workflow patterns |
| 7 | Other `knowledge/*.md` | Domain, constraint, stakeholder, environment facts |

> Priorities 0 and 1 may name the same file. They are distinguished by what the section says — *what we
> are building* versus *how we build* — not by which file holds it. Rules: `conventions.md` §3 → Project
> North Star.

**Who scans PV:**
- **Coordinator** — priorities 0–4 in full and 5–7 by relevance during planning. Output: HL §7.2 Knowledge Citations table naming the exact clause/item and its concrete application; priorities 0 and 1 remain separate even when they share a file.
- **Reviewer** — priorities 0–4 in full and 5–7 by relevance during verification. Output: verify.md Knowledge Citations Verified section checking resolution, item existence, semantic match, and relevance to the asserted application.
- **Executor** — reads coordinator's citations from HL §7.2. Output: ONB §7 confirming read + any new items found.
- **Researcher** — reads HL §7.2 citations. Cross-references in RES Fact Candidates.

## Config Sync Registry
A table in `config.md` workflow mapping `project_config.yaml` keys to their inline display locations. AI agent reads the registry to find where values appear, compares with YAML, and proposes updates.

## Tool Adapter
A tool-specific entry point (CLAUDE.md, .cursor/rules, .agent/workflows/, or Codex root `AGENTS.md` + `.agents/skills/tfw-*/SKILL.md`) that references `.tfw/` as the single source of truth. Across tools, `/tfw-*` is the primary human-facing command contract. Codex implements the commands with repository-local skills and uses AGENTS.md as always-on recognition and fallback routing. → conventions.md §9

## status.md
The task's own state file, and the **only** authority for its live state. Closed key set, bounded fields, no free-text body. Lives inside the task directory, so advancing one task writes nothing another task is reading. Retired the root Task Board at 2.0.0. → conventions.md §4

## journal/
A directory inside a task holding **one immutable file per coordination event**, each named from the clock — the filename *is* the event identifier, so nothing allocates one and nothing counts. Two participants appending at the same moment create two files rather than contending for a byte range. A written event is never edited; a correction is a new event. Entries carry references, not copied artifact prose, under a measured length ceiling. → conventions.md §4

## Portfolio index
`{first container}/00-INDEX.md` — a **derived, non-authoritative** view rebuilt from task state by `docs/scripts/gen_index.py`. It declares its source count and freshness and reports every unresolved input. A workflow acting on a task re-reads that task's `status.md` first; absent or stale, the index degrades discovery and changes nothing. → conventions.md §4

## team/
One file per participant, human or agent alike. A profile is **declared attribution, not authentication**: it says who a handle refers to, and grants nothing. The binding from a machine to a handle is held outside the project tree, because a per-user file that is gitignored is still not sync-ignored. → conventions.md §4

## Task Board *(retired at 2.0.0)*
A Markdown table in `README.md` that was the single source of truth for every task's status until TFW 2.0.0. Every lifecycle transition rewrote it, so two people advancing unrelated tasks collided in one file. Replaced by per-task `status.md` plus a derived index. The table as it stood on the day it was removed is preserved verbatim in `tasks/BOARD-SNAPSHOT.md`.

## project_config.yaml
Per-project configuration file in `.tfw/`. Defines: stack, build commands, task prefix, execution engine, template paths, scope budgets, knowledge settings.

## VERSION
Single-line file in `.tfw/` containing the current framework version in semver format (MAJOR.MINOR.PATCH).

## CHANGELOG.md
Structured version history in `.tfw/`. Follows Keep a Changelog format.

## Compilable Contract
Build-time specification for deterministic compilation of TFW artifacts. → [compilable_contract.md](compilable_contract.md)

## Reference Format
Standard text patterns for cross-artifact citations (e.g., `RF TFW-18`, `D24`, `TD-59`). Build-time resolver converts to hyperlinks. → [compilable_contract.md](compilable_contract.md) §2

## Source Manifest
Ordered list of project files that compilation utilities read. → [compilable_contract.md](compilable_contract.md) §1

---

## Project-Specific Terms

> Remove or replace this section when forking to a new project.

*Add project-specific terminology here.*

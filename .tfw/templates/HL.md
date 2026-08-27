# HL — {ID}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 📝 HL_DRAFT — Awaiting review
> **Contract**: 📝 DRAFT — not yet approved
> **Frozen**: §1 · §3 · §4 · §5 · §6 · §7 — locked on owner approval
> **Free**: §2 · §7.2 · §8 · §9 · §10 · §11 — research updates these directly
> **Append-only**: §12 Amendment Log — the only channel for changing a frozen section
> **Baseline**: freeze commits — recovery form in `conventions.md` §3 rule 15

> **Contract field** — one line, two states. Until the owner approves:
> `📝 DRAFT — not yet approved`. On approval the coordinator replaces it with
> `🔒 FROZEN — approved by {owner} YYYY-MM-DD` and commits the file before research starts.
> A frozen section may not be edited afterwards: propose in §12, wait for the verdict.
> Rules: conventions.md §3 → HL Contract. Add further header fields below this block, not inside it.

> **Project North Star**: {one or more designated README sections — e.g. `README.md § How It Works` · `.tfw/README.md #ns1 · #ns2 · #ns3`} · or `N/A — no project north star designated`

> **Project North Star field** — the reviewer's Purpose Check reads this before anything else. It takes a **list**:
> a project whose product is its own method designates sections of more than one file. With no north star
> the chain falls back to §1 Vision at the contract baseline, and the field still renders — `N/A`, never
> absent (F21). Rules: conventions.md §3 → Project North Star.

---

## 1. Vision 🔒 FROZEN
{Strategic narrative: what we want and why — 2-3 sentences. Write as if it's already done.}

**Impact:** {What changes when this is done — for users, team, product}

> Key quote from the stakeholder perspective — what they would say when this ships.

## 2. Current State (As-Is) 🟢 FREE
Current state: problems, structure, metrics, constraints.
Tables with REAL data where applicable.

## 3. Target State (To-Be) 🔒 FROZEN
What it should look like after. Clear deliverables.
Tables comparing As-Is → To-Be where applicable.

### 3.1 Result Visualization

> **Assemble what you would put in front of the stakeholder.** Not a description of it — the thing.
> §3.1 is a gate, not an illustration: the owner's checkpoint **before** the spend of tokens and
> time, the last point at which the result can still be judged cheaply. You imagine; the reader
> must not have to.
>
> **Nothing Imagined Test:** could the stakeholder judge this without constructing anything
> mentally? If understanding it requires the reader to picture what you described, you have
> written a plan.
>
> Four properties, all required:
>
> 1. **Working Backwards — from the finished state**, as if the result already exists. Six months
>    after launch: what does the stakeholder see, what changed?
> 2. **Rendered.** ASCII diagrams, flows, file and folder trees, before/after tables with real
>    data, outlines and mockups, sample output, a narrative timeline. *Which* rendering is a
>    choice; rendering is not. Prose alone is not a rendering.
> 3. **The value is visible** in the same picture as the thing that changes — not only the artifact.
> 4. **Whole in one view.** A multi-phase task labels every change with its phase and gives each
>    phase one line saying what it is for. A partial picture of five phases is not a preview.
>
> Not a process diagram or architecture flow — those are §3.2 Value Flow. (RF §9 Diagrams covers
> technical visualization.)

### 3.2 Value Flow

> Visualize HOW value gets created — the machine, not the outcome.
> Show the flow from user pain → pipeline steps → value delivered.
>
> Formats:
> - **ASCII flow** — `INPUT → PROCESSING → OUTCOME` with value labels
> - **Mermaid diagram** — for complex multi-path flows
> - **Value stream table** — columns: Step, Input, Transformation, Value Created
>
> This is NOT the outcome preview (§3.1) — this is the process that creates the outcome.

## 4. Phases 🔒 FROZEN
Break into Phases (A, B, C...) with priorities 🔴🟡🟢.
Each Phase = separate TS→RF cycle.

### Phase Dependencies

> For multi-phase tasks: visualize dependencies and shared files.
> Omit for single-phase tasks.

{mermaid graph or ASCII flow showing phase order and dependencies}

```mermaid
graph LR
  A[Phase A: {title}] --> B[Phase B: {title}]
  A --> C[Phase C: {title}]
  B --> D[Phase D: {title}]
  C --> D
```

| Phase | Depends on | Shared files | Can run in parallel with |
|-------|-----------|--------------|-------------------------|
| A | Independent | — | — |
| B | A | {files modified by both} | C |
| C | {A or Independent} | {files modified by both} | B |
| D | B + C | {files modified by both} | — |

### Phase A: {title} 🔴

> **For multi-phase tasks (3+ phases):** include Context block per phase.
> Phase coordinator reads ONLY this block + referenced files — not all research.
>
> **Requires:** {Independent | Requires: Phase X ✅}
>
> **⚠️ Shared files with Phase X:** {files modified by multiple phases — omit if none}
>
> **Context for coordinator:** numbered list of files + specific §/D-references to read before writing Phase TS
>
> **Key decisions:** D-numbers with inline one-line summaries
>
> **⚠️ Cascade dependency:** {if modifying workflow steps — warn about adjacent steps. Omit if none}
>
> **Deliverables:** numbered list

- {bullet list of deliverables — for simple tasks without Context block}

### Phase B: {title} 🟡
- {bullet list of deliverables}

## 5. Definition of Done (DoD) 🔒 FROZEN
Numbered list. Each item starts with ✅.
Must cover all deliverables from §4 Phases.

- ✅ 1. {Criterion 1}
- ✅ 2. {Criterion 2}

## 6. Definition of Failure (DoF) 🔒 FROZEN
Numbered list. Each item starts with ❌.
What to do on failure: rollback, rethink, escalate.

- ❌ 1. {Failure condition 1}
- ❌ 2. {Failure condition 2}

**On failure:** {action plan}

## 7. Principles 🔒 FROZEN
Design philosophy. Non-negotiable rules.

1. **{Principle name}** — {description}
2. **{Principle name}** — {description}

> **Subsections inherit their parent's state** unless they carry a marker of their own.
> §3.1 and §3.2 are frozen with §3; §7.1 is frozen with §7; §7.2 is marked free explicitly.

## 7.1 Quality Contract (optional, for multi-phase tasks) 🔒 FROZEN
Anti-patterns, style rules, and constraints that MUST be copied into each Phase TS.
Purpose: prevent executor agents from drifting.
Only needed for tasks where consistency across phases matters.

### 7.2 Knowledge Citations 🟢 FREE

> Coordinator: scan PV Index (glossary.md → Project Values).
> Full scan of priorities 0-4 (Project North Star, methodology values, philosophy.md,
> KNOWLEDGE.md §1, conventions.md); scan priorities 5-7 by relevance.
> Name the exact clause/item read and its concrete application. Record priorities 0 and 1
> as distinct rows even when they share a file; a file-only citation is insufficient.
> Reviewer will verify link resolution, item existence, semantic match, and asserted relevance.

| # | Source | Item | How it applies |
|---|--------|------|----------------|

> Explicit N/A is allowed only after the required scan and must state the reason. For new projects
> with empty KNOWLEDGE.md: "No applicable knowledge items — project in bootstrap phase."

## 8. Dependencies 🟢 FREE
| Dependency | Status |
|------------|--------|
| {dependency} | ⬜ / ✅ |

## 9. Risks 🟢 FREE
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {risk} | Low/Medium/High | Low/Medium/High | {mitigation} |

## 10. RESEARCH Case 🟢 FREE

### Blind Spots
- {What we do NOT know that could affect our approach}

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | {Statement to verify} | open |

> **Filter:** Each hypothesis: "If proven false, would our approach change?" If no — remove.

### Risks of Not Researching
{What happens IF we skip RESEARCH}

### Proposed RESEARCH Focus
1. **Gather**: {specific question}
2. **Extract**: {specific question}
3. **Challenge**: {specific question}

### Why Not Just...?
- Why not {obvious alternative A}? — {reason}
- Why not {obvious alternative B}? — {reason}

## 11. Strategic Insights (Planning) 🟢 FREE

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge,
> then ADD implications — what does this insight mean for the project's direction?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate (§7).
>
> **High-value signals to watch for:**
> - User corrects direction or reframes the problem
> - User expresses emotion (frustration, excitement, urgency)
> - User shares domain knowledge not in any artifact
> - User makes strategic decisions between alternatives
> - User reveals business context, stakeholder priorities, or constraints
>
> **Categories:** conventions.md §10.1.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |

## 12. Amendment Log 🟢 APPEND-ONLY

> **Append-only.** Every proposed change to a frozen section lands here before it is applied.
> A frozen section may not be edited before its row carries a verdict. Rows are never deleted,
> never rewritten and never renumbered — a refused proposal stays visible as an attempt.
>
> **A proposal without evidence, cost and a considered alternative is not a proposal.** The three
> columns are the gate: they put the burden on the proposer, which is what keeps declining cheap.
>
> **A remark inside a research thread is input, never a verdict.** Only an explicit owner ruling,
> recorded on the row, changes a proposal's status. An **owner-initiated** change to a frozen
> section is an amendment too: same row, `Proposer` = owner, verdict on the same line.
>
> **`Type` states the change's relation to the baseline** — never its disposition:
> - `EXTEND` — adds to a frozen claim, the original stays in force
> - `SUPERSEDE` — replaces a frozen claim
> - `RESTRICT` — narrows: adds a DoF item, tightens scope, drops a deliverable. A restrictive
>   change applies **on filing** and is logged with the verdict `✅ APPLIED — no owner verdict
>   required`. Restrictive-free is prohibited — the classifier benefits from the label.
>
> **`Verdict` values:** `PROPOSED` (awaiting a ruling) · `✅ APPROVED — {ruler}, YYYY-MM-DD` ·
> `❌ REJECTED — {ruler}, YYYY-MM-DD` · `✅ APPLIED — no owner verdict required` (`RESTRICT` only) ·
> `🚫 WITHDRAWN — {proposer}, YYYY-MM-DD` (retracted by its own proposer, only before a ruling —
> the row stays, because deleting it would break append-only and marking it `❌ REJECTED` would
> credit the owner with a decision they never made).
> `PROPOSED` describes the state of the *request*, which is what this log tracks — not the state of
> the world, which is what the frozen sections already record.
>
> An approved amendment is applied and then **re-frozen**: a new freeze commit at the new baseline.
> Full rules: conventions.md §3 → HL Contract.
>
> If nothing was ever proposed, write: **No amendments.**

| # | Date | § | Type | Proposer | Proposed change | Evidence | Cost | Alternatives considered | Verdict |
|---|------|---|------|----------|-----------------|----------|------|------------------------|---------|
| A1 | YYYY-MM-DD | §{n} | `EXTEND` / `SUPERSEDE` / `RESTRICT` | {owner / coordinator / research iterN / executor} | {what changes} | {where the finding comes from} | {what it costs to accept} | {what else was weighed and why it lost} | `PROPOSED` |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*HL — {ID}: {Title} | YYYY-MM-DD*

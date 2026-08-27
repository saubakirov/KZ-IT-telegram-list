# RES — {ID}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🔬 RES — In progress
> **Parent HL**: [HL-{ID}](path) _(pipeline only)_
> **Mode**: Pipeline / Standalone

---

## Research Context
{One paragraph: what we are researching and why.}

## Briefing
{Copied from or reference to `1_briefing.md` in iteration folder.}

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | {text} | open | 🟡 testing | |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** Every recommendation names the HL
> section it targets and lands in one of the two tables below. Editing the HL is not a researcher
> output — see conventions.md §15 Role Lock.
>
> - **Refinements** target the free sections (§2, §7.2, §8, §9, §10, §11). The coordinator applies
>   them directly, no ceremony.
> - **Amendment Proposals** target the frozen sections (§1, §3, §4, §5, §6, §7). The coordinator
>   may **not** apply them. They are transcribed into HL §12 Amendment Log with verdict `PROPOSED`
>   and wait for an owner ruling. Nothing in a frozen section moves before that ruling exists.
>
> Which class a finding belongs to is decided by the granularity rule in conventions.md §3 —
> the frozen unit is the declarative claim, not the section text.
>
> If a class is empty, say so: **No refinements.** / **No amendment proposals.**

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §{n} | {what changes} | {stage finding} |

### Amendment Proposals — frozen sections, owner verdict required

> Same column grammar as HL §12, minus the three fields a researcher cannot fill: the coordinator
> adds `Date` and `Proposer` on transcription, and `Verdict` opens as `PROPOSED`. The `#` column
> exists in both — number rows `A1`, `A2` … locally here; the coordinator re-assigns them into the
> HL's continuing sequence, because §12 is append-only and never renumbers.
> A row without evidence, cost and a considered alternative is not a proposal.

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| A1 | §{n} | `EXTEND` / `SUPERSEDE` / `RESTRICT` | {what changes} | {where the finding comes from} | {what it costs to accept} | {what else was weighed and why it lost} |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during research.
> Record facts about THIS project — not findings about alternatives,
> not implementation details (those belong in tfw-docs).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|

> **Source format**: Use reference patterns (e.g., `HL-TFW-19`, `D24`). See compilable_contract.md §2.

## Strategic Insights (Research)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge
> observed during research briefings, then ADD implications — what does this insight
> mean for the project's direction?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate.
>
> **When to fill:** Only when the human provides domain knowledge, corrections, or strategic
> context in research briefings. If no human interaction occurred — write "No strategic insights."
>
> **Categories:** conventions.md §10.1.

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | {category} | {insight} | User, {context} | ★★★/★★☆/★☆☆ |

## Findings Map

> **Cognitive mode:** Analytical research visualization.
> Visualize research findings: root cause analysis, hypothesis trees, priority matrices,
> relationship maps between discoveries.
>
> Formats: ASCII, mermaid, or structured tables.
> Focus: WHAT was discovered and WHY — pattern relationships, causal chains, decision trees.
>
> If no visualization is relevant — write "No findings map."

## Iteration Status

> **Mandatory block.** Every RES must include this, even for single-iteration research.

- **Iteration:** {N} of {min} (min) / {max} (max)
- **Hypotheses tested:** {H1 (status), H2 (status)...}
- **Hypotheses deferred:** {HN (reason) — or "None"}
- **Gaps discovered:** {list — or "None"}
- **Superseded decisions:** {DN supersedes DM (reason) — or "None"}

### Open Threads (for next iteration)

> If no open threads — write "No open threads."

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | {thread description} | {impact if not addressed} | {what next iteration should do} |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — {specify what and why}
- [ ] **BLOCKED** — {specify blocker}

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion
{One paragraph. What was researched. Key decisions made. What RESEARCH provided that would have been missed without it. Self-critique.}

---

*RES — {ID}: {Title} | YYYY-MM-DD*

# REVIEW — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {reviewer}
> **Verdict**: ✅ APPROVE / 🔄 REVISE / ❌ REJECT
> **RF**: [RF Phase {X}](path-to-RF)
> **TS**: [TS Phase {X}](path-to-TS)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

{2-3 sentence summary of understanding: what was done, key decisions, scope}

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|

> Raw verification log: see `review/verify.md`. If verification was limited: state what could NOT be verified.

## 3. Judge

> Ten rows, matching `review/judge.md` one-for-one and in the same order.
> `⚪ N/A` is permitted on any row and requires a stated reason — a skipped row is never a bare ✅.

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅/❌/⚪ | {specific} |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅/❌/⚪ | |
| 3 | Tech debt documented | ✅/❌/⚪ | |
| 4 | Style & standards | ✅/❌/⚪ | |
| 5 | Observations collected | ✅/❌/⚪ | |
| 6 | RF completeness (§7-9 present) | ✅/❌/⚪ | |
| 7 | Evidence completeness — does it exist? | ✅/❌/⚪ | |
| 8 | Evidence sufficiency — does it establish the claim? | ✅/❌/⚪ | |
| 9 | Backward compatibility | ✅/❌/⚪ | |
| 10 | Safety | ✅/❌/⚪ | |

## 4. Verdict

**{✅ APPROVE / 🔄 REVISE / ❌ REJECT}**

{Rationale referencing §2 Verify and §3 Judge evidence}

### If REVISE — items to fix:
1. {specific item to fix}

### If REJECT — fundamental issues:
1. {issue requiring HL/TS rework}

> **If the ground is purpose** — finding `not fit for purpose`: quote the baseline or north-star clause
> the work fails to serve, name the concrete harm, and say plainly that the quality checks passed if they
> did. Routes to the owner, not back to the executor. If the reference set itself is inconsistent, record
> a **contract defect** with both conflicting clauses quoted — also to the owner.

## 5. Tech Debt Collected

> **Source format**: Use reference patterns (compilable_contract.md §2).

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF observations | Low/Med/High | `file.py` | {description} | → backlog / → next phase |

## 6. Traces Updated

- [ ] README Task Board — status updated
- [ ] HL status — updated if phase completes
- [ ] project_config.yaml — initial_seq incremented if needed
- [ ] Other project files — checked for stale info
- [ ] tfw-docs: {Applied — updated Sections X, Y / N/A (minor)}
- [ ] tfw-knowledge: {Applied / N/A / Deferred to batch}

## 7. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Reviewer-observed project patterns discovered during the review process.
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", implementation details (→ Observations → tfw-docs),
> or reviewer analysis/opinions (those belong in §4 Verdict rationale).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | {category} | {what you learned} | {where from} | High/Medium/Low |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.

> **Categories** (open list): `environment`, `process`, `stakeholder`, `constraint`, `convention`, `domain`, `context`, `risk`, `philosophy`

---

*REVIEW — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*

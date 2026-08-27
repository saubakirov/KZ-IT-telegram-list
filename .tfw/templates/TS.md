# TS — {ID} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-{ID}](path-to-HL)

---

## 1. Objective
{One paragraph: what this phase delivers and why it matters.}

## 2. Scope

### In Scope
- {what will be done}

### Out of Scope
- {what will NOT be done in this phase}

## 3. Principles Check

> Map HL §7 principles to specific AC items. Each principle MUST have at least one AC enforcing it.
> If a principle has no applicable AC — mark as "N/A" with reason.

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | {principle name} | AC-{N} | {how verified} |
| P2 | {principle name} | N/A | {reason not applicable} |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `path/to/file` | CREATE / MODIFY / DELETE | {description} |

**Budget:** {N} new files, {M} modifications. Defaults: max {max_files} files, max {max_new} new, max {max_loc} LOC.

## 5. Acceptance Criteria

> Describe WHAT the result should achieve, not HOW to implement it.
> Each AC must be independently verifiable. Mark dependencies with `[depends: AC-X]`.
> Executor verifies dependent ACs in order — a dependent AC cannot pass before its prerequisite.
>
> **Evidence field:** Coordinator specifies what real-environment verification is needed.
> Gate = synthetic verification (tools). Evidence = real-world verification (live environment).
> Grammar: full spec, minimal spec, `N/A — {reason}`, `DEFERRED — {reason}`, or empty (executor decides).
> Executor MAY deviate from Evidence field with justification in RF (same as §6 Technical Guidance).

### AC-1: {title}
{What the result should achieve — 1-2 sentences.}
- [ ] {Verifiable criterion}
- [ ] {Verifiable criterion}
Gate: {How to verify — a command, query, visual check, or stakeholder confirmation}
Evidence: {What to verify in real environment — or N/A with reason}

### AC-2: {title}  [depends: AC-1]
{What the result should achieve — 1-2 sentences.}
- [ ] {Verifiable criterion}
Gate: {How to verify}
Evidence: {What to verify in real environment — or N/A with reason}

### Evidence Artifacts

> List expected evidence files. Minimum: one EV file (always required).
> Additional binary artifacts (screenshots, API responses, logs) if applicable.

| File | Description |
|------|-------------|
| `evidence/EV__{ID}.md` | Structured evidence: environment header, per-AC table, verdict _(required)_ |
| `evidence/{additional_file}` | {description} _(if applicable)_ |

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.
- {Relevant context: where things are, what patterns exist, what constraints apply}

## 7. Definition of Failure

- ❌ {Condition that causes RF rejection — hard reject, not a warning}

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| {risk} | {mitigation} |

## 9. Cross-Phase Modifications (multi-phase only)

> Include only for multi-phase tasks. Omit section entirely for single-phase tasks.

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `path/to/file` | Phase {X} | {what to watch for} |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*TS — {ID} / Phase {X}: {Title} | YYYY-MM-DD*

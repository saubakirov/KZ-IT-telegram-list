# EV — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {executor}
> **Task**: {PREFIX}-{N}
> **TS**: [TS Phase {X}](path-to-TS)

---

## Environment

> Capture the common verification environment. Fields marked "(if applicable)"
> may be omitted when irrelevant to the task type.

| Field | Value |
|-------|-------|
| OS | {e.g., Windows 11, Ubuntu 22.04, macOS 14} |
| Language / Runtime | {e.g., Python 3.12, Node 20} _(if applicable)_ |
| Database | {e.g., PostgreSQL 16, ClickHouse 24.3} _(if applicable)_ |
| Deploy target | {e.g., staging, localhost:3000, Vercel preview} _(if applicable)_ |
| CI / Pipeline | {e.g., GitHub Actions, local} _(if applicable)_ |

## Evidence

> One row per AC item. When a single verification covers multiple ACs,
> list them comma-separated in the AC column (e.g., "AC-3, AC-5").
> Use only the 4-status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A.

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-{N} | {description of what was observed} | {specific environment detail if different from header} | {VERIFIED / DEFERRED / BLOCKED / N/A} | {file path in evidence/ or inline output} |

## Verdict

Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A

## Attachments

> Index of binary artifacts stored in this `evidence/` folder.
> Omit this section if no binary artifacts exist.

| File | Description |
|------|-------------|
| `{filename}` | {what it captures} |

---

> **File naming:**
> - Single-phase: `EV__{PREFIX}-{N}__{title}.md`
> - Multi-phase: `EV__phase-{x}__{title}.md`

*EV — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*

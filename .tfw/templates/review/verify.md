# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: {from project_config.yaml, default 0.42}
> RF files claimed: {N}
> Files to verify: ⌈N × ratio⌉ = {M}

## Verification Log

### {V1: file path}
- **RF claim:** {what RF says about this file}
- **Actual:** {what the file actually contains}
- **Match:** ✅ / ❌ / ⚠️ partial

### {V2: file path}
...

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | {build/test/lint command} | {output summary} |

> If no commands could be run: state why. "No test runner" is valid.

## Claim & Source Checks

> Unconditional — every review, whatever the deliverable is. Three actions, all mandatory:
> 1. **Spot-check 2-3 key claims or sources** for accuracy — chosen by how much the result rests on them, not by which are easiest to open.
> 2. **Confirm each citation traces to a real artifact** — a reference that looks plausible but resolves to nothing is a finding, not a formatting issue.
> 3. **Verify data claims against a primary source** where one is reachable — a number quoted from a summary is not verified.
>
> Feeds judge.md row 8 (*evidence sufficiency*). If the deliverable contains no claims, citations or
> data, write "N/A — no claims to check" and state what it does contain.

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | {the claim or citation, quoted} | {file + section} | {real artifact, primary source, or "does not resolve"} | ✅ / ❌ |

## Discrepancies Found

{List. If none: "No discrepancies."}

> On ANY discrepancy: escalate to 100% verification (check all files).

## Evidence Verification

> Verify that RF §5 Evidence artifact references resolve to real files or inline output.
> Check that evidence statuses match the actual content.

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | {evidence/file.ext or inline ref} | ✅ / ❌ | ✅ / ❌ — {brief note} |

> If RF §5 has no evidence items (all N/A): write "N/A — no evidence artifacts to verify."

## Knowledge Citations Verified

> Verify that HL §7.2 and ONB §7 citation links resolve to real items.
> If ANY link doesn't resolve → flag as hallucination in Discrepancies.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #{N} | {KNOWLEDGE.md D-number or knowledge/*.md F-number} | ✅ / ❌ | ✅ / ❌ |

> If HL §7.2 says "No applicable knowledge items" — write "N/A — no citations to verify."

## Checkpoint

**Self-check:**
- [ ] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [ ] Ran at least 1 build/test command (or documented why not)?
- [ ] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)?
- [ ] Each RF §3 (AC) checkmark verified against actual file?
- [ ] KNOWLEDGE.md checked — contradictions with changes documented?
- [ ] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: {N}, verified: {M}, hallucinations: {H}
- [ ] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: {N}, verified: {M}, missing: {H}

Stage complete: YES / NO

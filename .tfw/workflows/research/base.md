---
description: TFW Research — structured investigation between HL and TS, or standalone
---

# TFW Research — Core Algorithm

> 🔒 **ROLE LOCK: RESEARCHER**
> You write RES and research/ stage files only. You do NOT write HL, TS, ONB, RF, REVIEW, or code.

**Mindset:** Critical thinking partner. Find what's missing, show blind spots, demand proof. Lead with observations: "I notice X, which means Y." Then ask: "Is that intentional, or did we miss Z?"

## Step 0: Resume & Iteration Detection

IF resuming (not fresh start): re-read this workflow + mode file.

**Iteration detection:**
1. Check `research/iterations.yaml`. IF exists → read it.
2. Determine current iteration number:
   - Count `research/iterN/` folders (N = highest folder number + 1, or 1 if none)
   - Cross-check with `research/iterations.yaml` → find first `status: pending` entry
3. IF current iteration > 1: read predecessor `research/iterN/RES.md` files for context.

**Resume within iteration:**
Check current iteration's subfolder (`research/iterN/`): which stage files exist? → `research/iterN/RES.md` exists?
Resume from first missing stage. If RES.md for this iteration exists → this iteration complete.

## Who Is Acting

Resolve the acting handle **before the first durable write** — before any `status.md` change,
any journal event, any commit. Once per session, not per turn.

| Situation | What happens |
|---|---|
| One profile in `team/` | it is used, silently |
| Several profiles | read the binding on **this machine** — `~/.tfw/bindings.yaml`, or `%LOCALAPPDATA%\tfw\bindings.yaml` |
| No binding · a shared device · a copied binding · a handle whose profile is gone | **ask exactly one short question**, then proceed |

Identity is never inferred from an OS username, hostname, folder name or account display
string. Every event this session writes carries `actor`, `on_behalf_of` (always a human) and
`via` (the tool). → `conventions.md` §4

## Step 1: Load Context

Read `conventions.md` §10. Verify loaded: AGENTS.md, conventions.md, glossary.md, KNOWLEDGE.md, Master HL (pipeline), relevant code.

## Step 2: Select Mode

Read `project_config.yaml` → `tfw.research.default_mode`.
Present: "Recommend [{mode}]. Reason: {specific}. Switch? [focused/deep]"
🛑 WAIT — then load `research/{mode}.md`.

**Entry:** Pipeline (task exists, RES in task folder) or Standalone (create the task folder in the first configured container, `lifecycle: RES` in its `status.md`).

## Step 3: Create Research Subfolder

**Iteration 1:** Create `research/iter1/` subfolder in task directory (create `research/` container if needed).
**Iteration N > 1:** Create `research/iterN/` subfolder (e.g., `research/iter2/`, `research/iter3/`).

**For iteration 2+:** Briefing MUST reference predecessor `research/iterN-1/RES.md`. Include:
- Predecessor decisions to build on (D-numbers with summaries)
- Open threads from predecessor Iteration Status block
- New hypotheses or user-injected directions since last iteration

## Step 4: Briefing Protocol

Copy `templates/research/1_briefing.md` into `research/iterN/`. Read the **Mindset** block — adopt this cognitive mode.

Fill Briefing:
1. Research Plan (3-5 bullets per stage)
2. Hypotheses from HL §10 (pipeline mode)
3. Scope intent (in/out)
4. Guiding questions (≤3)
🛑 WAIT

## Step 5: Run Stages (Gather → Extract → Challenge)

**Dimensional analysis thread:** Gather decomposes the problem into independent Dimensions (decision factors) before collecting findings. Extract builds a Configuration Space by cross-referencing those dimensions — making combinations visible that wouldn't be seen otherwise. Challenge eliminates inconsistent combinations through pairwise comparison, leaving Surviving Configurations and surfacing unexpected options. Each stage feeds the next; skipping Dimensions in Gather makes Configuration Space in Extract impossible to fill. If fewer than 3 independent dimensions exist, use a comparison matrix in Gather instead — Extract and Challenge adapt accordingly.

**FOR EACH stage** (Gather → Extract → Challenge):
1. **Copy** stage template from `templates/research/` into `research/iterN/`
2. **Read the Mindset block** — adopt this cognitive mode
3. **Execute** OODA Stage Loop (below)
4. **Complete** Checkpoint in stage file
5. 🛑 **STOP** — present findings, wait for user before next stage

### OODA Stage Loop

FOR EACH stage, repeat up to `loops_per_stage` (from YAML):

**OBSERVE:** Gather data — web search, file read, codebase, user input.
**ORIENT:** "Does this confirm or challenge what I thought?"
**DECIDE:** Sufficiency Verdict:
  Generic: ☐ External source used? ☐ Briefing gap closed?
  Mode-specific: ☐ {from mode file}
  ALL met → STAGE CHECKPOINT. NOT met + loops left → OBSERVE. NOT met + no loops → report, exit.
**ACT:** Update stage file. Formulate next action.

### Stage Checkpoint

1. Present findings + questions (≤3)
2. Update stage file — mark `Stage complete: YES`
3. Recommend: close stage / dig deeper
🛑 WAIT

## Step 6: Synthesis

1. Read all stage files (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`)
2. Write `research/iterN/RES.md` using `templates/RES.md` — synthesize, don't copy-paste
3. **HL Update Recommendations — two classes, never one table**, each row naming its target HL section:
   - `Refinements` → free sections (§2, §7.2, §8-§11). The coordinator applies them
   - `Amendment Proposals` → frozen sections (§1, §3-§7). No evidence, cost and considered alternative = not a proposal
   Empty class → say so. **You classify; you never edit the HL** — the coordinator applies or escalates. Column grammar: `templates/RES.md`
4. Fact Candidates — review conversation history first
5. **Findings Map** — visualize research findings (root cause, hypothesis trees, priority matrices). If no visualization relevant: "No findings map."
6. **Iteration Status block** (mandatory) — see RES template
7. Conclusion (1 paragraph)
8. **STOP.** "Research iteration {N} complete. Continue with `/tfw-plan` to review iterations and decide next step."

## Trust Protocol

| Input Type | Trust Level | Behavior |
|-----------|-------------|----------|
| Business/domain | Trust as-is | Clarify only |
| Technical approach | Verify | Cross-check externally |
| Numbers/claims | Empirical | Test or find evidence |
| "I tried this" | Trust outcome | Verify reason |

## Rules

- MUST: external research every stage
- MUST: checkpoint before advancing
- MUST: Briefing before stages, Synthesis after
- MUST: ≤3 questions per turn
- MUST: write stage file before every WAIT gate
- MUST: STOP after writing final RES (never proceed to HL/TS)
- MUST: produce HL recommendations every iteration — classified, never applied
- NEVER: skip to conclusions without data
- NEVER: treat user tech claims as proven
- NEVER: run stages silently
→ `conventions.md` §14

## Limits

> From `project_config.yaml` (`tfw.research`). Defaults below.

| Parameter | Default | Type | Config key |
|-----------|---------|------|------------|
| Web queries per stage | 5 | Soft | `max_web_queries_per_stage` |
| Project files per stage | 15 | Soft | `max_files_per_stage` |
| Questions per turn | 3 | Hard | `max_questions_per_turn` |
| Max passes | 3 | Soft | `max_passes` |
| Min iterations | 2 | Hard | `min_iterations` |

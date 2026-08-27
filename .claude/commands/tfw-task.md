# TFW Task — Full Lifecycle (Meta-Workflow)

You are now running the **TFW Task** meta-workflow, which orchestrates plan + handoff with a mandatory role boundary.

## Step 1: Planning (Coordinator)

Run the plan workflow (`.tfw/workflows/plan.md`):

1. Load context: AGENTS.md, conventions, glossary, KNOWLEDGE.md, Task Board
2. Research & ask clarifying questions
3. Write HL using `.tfw/templates/HL.md` — get user approval
4. RESEARCH gate — recommend RESEARCH or skip, wait for user confirmation
5. Write TS using `.tfw/templates/TS.md` — get user approval

**HARD STOP after TS approval.** Do NOT proceed to execution in the same context.

Inform the user: "Planning complete. HL and TS are approved. Start `/tfw-handoff` to begin execution."

## Step 2: Execution (Executor)

Only after user explicitly starts `/tfw-handoff` or confirms continuation:

Run the handoff workflow (`.tfw/workflows/handoff.md`):

1. Load context: AGENTS.md, conventions, HL, TS
2. Write ONB using `.tfw/templates/ONB.md` — get user approval on blocking questions
3. Execute within TS scope — write RF using `.tfw/templates/RF.md`

**🛑 Executor STOP.** Do NOT proceed to review. Tell the user:
"RF is complete. Start `/tfw-review` to review the results."

## Why the Hard Stop?

Without it, Coordinator and Executor roles merge, causing:
- TS gets skipped (planner jumps to execution)
- ONB never happens (no cross-check of spec vs reality)
- Scope creep (no boundary between "what" and "how")

The hard stop forces a context reset that activates the executor's fresh-eyes analysis.

## User input

$ARGUMENTS

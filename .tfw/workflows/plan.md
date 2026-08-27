---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR**
> You write HL and TS. You do NOT write ONB, RF, RES, REVIEW, or code.
> Violation = immediate stop + report.

**Mindset:** You are a strategic architect. Understand the problem deeply before proposing solutions. Show the finish line visually (§3.1). Identify what you DON'T know (§10). Challenge assumptions — be a thinking partner, not a yes-machine. Quality of planning > speed of pipeline progression.

## Step 0: Name This Session

**Name this session:** `Coordinator | {TASK-ID}`
Set this as the session/conversation name before doing anything else.

## Step 1: Load context

Read `conventions.md` §10 (Context Loading) and load anything on that list you are missing.

## Step 2: Knowledge Gate

1. Read `.tfw/knowledge_state.yaml`
2. Read `tfw.knowledge.gate_mode` from project_config.yaml
3. Compute: `current_seq - last_consolidation_seq`
4. IF `>= interval` AND gate_mode = `hard`:
   → **HARD STOP**: "Knowledge consolidation overdue ({N} tasks). Run `/tfw-knowledge` before proceeding."
   Skip allowed with justification. Record: `knowledge-gate: skipped (reason: ...)`
5. IF `>= interval` AND gate_mode = `soft`:
   → Reminder: "Knowledge consolidation recommended ({N} tasks since last)."
6. IF gate_mode = `off`: skip silently

## Step 3: Research & Understand

1. **Identify context** — read relevant code, existing HL files, knowledge items
2. **Understand the problem deeply** — what is broken, what is missing, and what does the user actually need vs what they asked for?
3. **Study references** — how similar problems were solved before (existing Architecture Decisions)
4. **Scan Project Values (PV)** — the `glossary.md` PV Index: priorities 0-4 in full, 5-7 by relevance.
      Fill HL §7.2 Knowledge Citations with the exact clause/item read, a link, and its concrete
      application. Record priority 0 and priority 1 as distinct semantic items even when they share
      a file; a file-only citation is insufficient. Explicit N/A is allowed only after the required
      scan and must state why. New projects add: "No applicable knowledge items — project in bootstrap phase."
5. **Ask clarifying questions** — batch all questions, max 3-5
🛑 WAIT for user answers

## Step 4: Write HL

1. **Know who is acting.** Before the first durable write of the session, resolve the acting
   handle: one profile in `team/` → use it silently; several → read the binding on this
   machine (`~/.tfw/bindings.yaml`, or `%LOCALAPPDATA%\tfw\bindings.yaml`); no binding, a
   copied binding, or a handle whose profile is gone → **ask exactly one short question**,
   once, then proceed. Never infer identity from an OS username, hostname or folder name.

2. **Create the task folder.**

   ```
   container = tfw.task_containers[0]          # from project_config.yaml
   stamp     = system clock, read now, as YYYYMMDD-HHMMSS
   repeat at most tfw.id_max_retries times:
       dir = {container}/{stamp[0:4]}/{stamp}__{slug}
       if dir does not exist:  create it and stop
       stamp = system clock, read AGAIN                 # a new actual reading
   otherwise: STOP and report — the clock is not advancing
   ```

   **The whole directory name is the identifier**, not the timestamp: two participants
   offline from each other can reach the same second, and only the slug tells them apart.
   Same second *and* same slug means they created the same task — a signal, not a collision.

   The bound matters. A wall clock that steps backwards — an NTP correction, a resumed
   machine, a restored image — can re-offer a used value forever, and an unbounded retry
   would spin silently instead of saying so.

   **Read no counter, no project-wide maximum and no other task's contents.** The one
   existence check above is what lets two offline participants stay safe with nothing shared
   between them.

3. **Write the task's own state and its first event** — `status.md` from
   `.tfw/templates/status.md`, and a `created` event in `journal/` named
   `{stamp}__created__{actor}.md`, carrying `actor`, `on_behalf_of` and `via`. The event's
   `time` is read from the clock, never typed.

4. **Create HL file** — use `templates/HL.md` as canonical format
5. **Fill §3.1** — the visualization gate is mandatory; its four properties and format options are in the template.
6. **Fill §10 (RESEARCH Case)** — 2-4 hypotheses. The filter and the remaining subsections are in the template.
7. **Set the task's own state** — `lifecycle: HL_DRAFT` in `{task}/status.md`; fields and bounds in `conventions.md` §4
8. **Capture Strategic Insights** — review the conversation history, fill HL §11. The test and the categories are in the template.

**GATE: User approves HL**
🛑 WAIT — present HL for review. Incorporate feedback. Repeat until approved.

**On approval — freeze the contract:**
1. Set the HL header `Contract` field to `🔒 FROZEN — approved by {owner} YYYY-MM-DD`
2. Commit the HL with the reserved `freeze` scope word **before** the first research iteration — an uncommitted baseline cannot be diffed
3. What freezes, what stays free, and the recovery form: `conventions.md` §3 (HL Contract), rule 15

## Step 5: Hypothesis Iteration

Present §10 hypotheses to user one by one:
  FOR EACH hypothesis:
    USER: "I know the answer" → mark confirmed/refuted in table, record answer
    USER: "Not sure" → mark needs-research
    USER: "This is obvious" → remove from table
  AFTER iteration:
    IF all confirmed/refuted → RESEARCH optional (offer skip)
    IF any needs-research → recommend RESEARCH
    IF coordinator sees remaining blind spots → still recommend RESEARCH despite user closure
🛑 WAIT for user response

## Step 6: RESEARCH decision & iteration management

### 6a. Initial RESEARCH decision

Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
- Default recommendation: **run RESEARCH**
- Frame as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
- Skipping requires concrete justification (not just "task is simple")

IF user skips → confirm, proceed to Step 7.
IF user approves research:

### 6b. Create iterations.yaml

Create `research/iterations.yaml` in the task's `research/` folder. Format and field list: `conventions.md` §4 (Research subfolder).
`min_iterations`: from `project_config.yaml` → `tfw.research.min_iterations` (default: 2). `max_iterations`: soft ceiling (default: 5).

**Then:** "Start `/tfw-research`. Researcher role takes over." **STOP.**

### 6c. Iteration gate (after each research iteration returns)

Read all `research/iterN/RES.md` files and `research/iterations.yaml`. For each completed iteration:
1. Update `research/iterations.yaml`: mark iteration `status: complete`, record `res_file`
2. Read Iteration Status block from RES: gaps, open threads, recommendation
3. **Classify every recommendation by its target section and `conventions.md` §3 rule 6** — never by the table it arrived in:
   - free section, or a free unit inside a frozen one → apply it
   - frozen claim → transcribe into HL §12 with verdict `PROPOSED`; the section itself stays untouched
4. **Escalate once per iteration** — one message carrying every proposal with its evidence, cost and considered alternative. A coordinator may not apply a proposal it filed; only an owner verdict moves one

**Gate check:**
- IF completed iterations < `min_iterations` → **MUST** launch next iteration.
  Add next entry to `research/iterations.yaml` (focus = gaps/threads from previous RES).
  "Starting iteration {N}. `/tfw-research`." **STOP.**
- IF completed iterations ≥ `min_iterations`:
  - IF researcher recommends MORE NEEDED and coordinator agrees → launch next iteration
  - IF researcher recommends SUFFICIENT or coordinator overrides → proceed to Step 7
  - Coordinator may override `min_iterations` with documented justification

After the final iteration: every proposal is ruled or escalated before Step 7 — a TS written over an open proposal derives from a contract that may still move.

### 6d. Amendment verdicts — whenever one arrives, in research, ONB, review or execution

- **✅ Approved** → apply it to the frozen section, record the verdict on its §12 row, then commit at the new baseline with the reserved `freeze` scope word
- **❌ Rejected** → the row keeps its verdict and stays; the original contract holds; resume work
- **`RESTRICT`** → applies on filing, no verdict required (`conventions.md` §3 rule 10)

## Step 7: Write TS

1. **Determine complexity** — single-phase or multi-phase?
2. **Budget check** — count files, new files and estimated LOC against `tfw.scope_budgets` (`conventions.md` §6).
   Over any limit → split into phases, or document the override with justification.
3. **Evidence fields** — write an `Evidence:` field per AC item. Grammar and proportionality: `templates/TS.md` §5.

### Small task (single phase):
3a. Write TS using `templates/TS.md`
4a. Get user approval on TS
5a. **STOP.** "TS is approved. Suggest execute `/tfw-handoff`. After RF, run `/tfw-review`."

### Large task (multi-phase):
3b. **Pre-TS Gate (multi-phase):** Before writing the TS for Phase N (any phase after the first), read the RF of the latest completed phase in the dependency chain. Verify: what was actually delivered? What deviated from plan? Read RF (actual output), not TS (planned output) — these differ. Skip if this is the first phase (no predecessor RF exists).

4b. Create the phase subfolder + write Phase HL + TS using `templates/TS.md`.
Folder layout: `conventions.md` §4 (Multi-phase folder structure). The Phase HL is derivation-only — §3 rules 20-21.
Each phase: HL → TS → `/tfw-handoff` → ONB → RF → `/tfw-review` → REVIEW
5b. Suggest execute via `/tfw-handoff`. Repeat the cycle per phase.

> → Role Lock: `conventions.md` §15

**Footer — Self-check before submitting:**
Read `conventions.md` §14 (Anti-patterns) — did I violate any? Then §5 (status transitions).

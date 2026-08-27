---
description: TFW Knowledge — consolidate fact candidates into verified project knowledge
---

# TFW Knowledge — Knowledge Consolidation Workflow

> **Role:** Coordinator
> **Output:** Updated `knowledge/` topic files, `KNOWLEDGE.md` §4 (index), `knowledge_state.yaml`
> **Trigger:** Manual (`/tfw-knowledge`) or gate in plan.md Step 2
> **Duration:** 5-20 minutes

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: reading all project artifacts, writing to KNOWLEDGE.md, `knowledge/` topic files, `.tfw/knowledge_state.yaml`.
> Forbidden: writing code, modifying RF/REVIEW/RES/HL/TS files (except adding `fact-candidates: processed` marker).

## Prerequisites

1. Read `.tfw/knowledge_state.yaml` — current state, last consolidation seq
2. Read `KNOWLEDGE.md` — current knowledge index
3. Read all topic files in `knowledge/` — current verified facts
4. Read `.tfw/project_config.yaml` → `tfw.knowledge` section for limits

## Phase 1: Orient

1. Note `last_consolidation_seq` → compute task range to scan
2. List topic files with fact counts
3. Read conventions.md §10.1 → list all canonical categories. Note which have topic files and which don't
4. Present orientation summary to user (include category coverage gaps)

## Phase 2: Gather

> **⚠️ Knowledge ≠ technical documentation.**
> Knowledge is what would be UNKNOWN without the human saying it: vision, priorities, emotions,
> business context, architectural philosophy, process corrections.
> Technical implementation details (tools config, API constraints, build errors) belong in tfw-docs.
>
> **YES**: "primary output = knowledge graph, not docs site", "close as MVP, don't stretch phases"
> **NO**: "MkDocs docs_dir cannot be project root", "use directory URLs not .md"

1. Scan artifacts for tasks since `last_consolidation_seq`:
   - **HL §11 (Strategic Session Insights)** — coordinator's captured signals from planning sessions
   - **RF §8 (Execution Session Insights)** — executor's captured signals from live testing (if exists)
   - **RF, REVIEW, RES §Fact Candidates** — standard FC sections
2. Review conversation history for the current session — extract facts from user messages not captured in artifacts
3. Category coverage check: do any candidates belong to categories without topic files? Don't force facts into existing categories — create new topic file when justified. Ref: conventions.md §10.1
4. Present gathered candidates to user:

```
Found {N} candidates from {M} artifacts:
| # | Candidate | Category | Source | Confidence |
|---|-----------|----------|--------|------------|
```

> **Priority**: §11/§7 insights are pre-filtered strategic signals → higher value than standard FC. Standard FC mix strategic + technical; apply Human-Only Test more strictly.

🛑 **WAIT** — user reviews candidates before consolidation

## Phase 3: Consolidate

For each candidate:

1. **Human-Only Test** — would this fact be unknown without the human saying it?
   If an agent can discover it by reading code, running commands, or checking docs → **reject**
2. **Deduplicate** — check if fact already exists in topic files → skip
3. **Contradiction check** — if contradicts existing fact → flag, ask user
   - DO NOT auto-resolve contradictions — present both, user decides
4. **Verification**:
   - ≥2 independent sources → ✅ verified
   - 1 source → present to user for confirmation or skip
5. **Write to topic file** — `knowledge/{category}.md`
   - Category: see conventions.md §10.1. If no topic file exists for the category, create from `.tfw/templates/topic_file.md`
   - Check `max_facts_per_topic` and `max_topic_files` limits (see `tfw.knowledge` in project_config.yaml)
6. **Mark processed** — add marker to source artifact:
   ```
   > fact-candidates: processed YYYY-MM-DD
   ```

Present consolidation results to user before finalizing.

🛑 **WAIT** — user approves changes before writing

## Phase 4: Update

1. Review existing facts for staleness (source > 20 tasks ago or source artifact deleted) → flag for user, DO NOT auto-delete
2. Update `KNOWLEDGE.md` §4 (Project Facts): update category counts + links to topic files
   > ⚠️ Do NOT write to §1 (Architecture Map) or §2 (Key Artifacts) — those belong to `/tfw-docs` (Combination scope)
3. Update `.tfw/knowledge_state.yaml`:
   - `last_consolidation_seq` → current task seq
   - `last_consolidation_date` → today
   - Stats: total_facts, verified, unverified, rejected, candidates_processed, sources_scanned
4. Present summary to user

🛑 **WAIT** — user approves before final write

## Behavior Rules

- **DO NOT invent facts** — only consolidate from artifacts and conversation
- **DO NOT auto-resolve contradictions** — ask user
- **DO NOT delete facts** without user confirmation
- **DO NOT modify RF/REVIEW/RES content** — only add the `fact-candidates: processed` marker
- **DO NOT default all facts to existing categories** — check §10.1 for full list, create new topic files when justified

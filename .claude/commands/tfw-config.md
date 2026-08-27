---
description: TFW Config — interactive config change, propagate to all inline values
---

# TFW Config — Config Sync Workflow

> **Role:** Coordinator
> **Output:** Updated project_config.yaml + all inline value locations + synced adapters
> **Trigger:** Manual (`/tfw-config`) when config values need changing or auditing

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: reading/writing project_config.yaml, workflow files, convention files, adapter copies.
> Forbidden: writing code, modifying HL/TS/ONB/RF/REVIEW files.

## Modes

### Edit Mode (default)

1. **Ask**: "What would you like to change in the configuration?"
2. **User answers** with config key and desired value (e.g., "scope budget max_files до 10")
3. **Read** `.tfw/project_config.yaml` — get current value
4. **Read** Config Sync Registry (below) — find all inline locations
5. **Propose batch update** — list every file + line that will change:
   ```
   Proposed changes (config key: tfw.scope_budgets.max_files_per_phase, 14 → 10):
   - project_config.yaml: 14 → 10
   - .tfw/workflows/plan.md §Scope Budget per Phase: 14 → 10
   - .tfw/conventions.md §6 Scope Budgets: 14 → 10
   "Apply? ({N} files)"
   ```
6. **User approves** → update all files
7. **Sync adapters** — copy modified workflows to adapter folders (see §Adapter Sync)

### Verify Mode

Invoked with: `/tfw-config verify`

1. **Read** `.tfw/project_config.yaml` — all config values
2. **Read** every target in Config Sync Registry — extract current inline values
3. **Compare** — report mismatches or confirm "All values in sync"
4. **Output format**:
   ```
   Config Sync Report:
   ✅ scope_budgets.max_files_per_phase: 14 (config) = 14 (plan.md) = 14 (conventions.md)
   ❌ scope_budgets.max_loc: 1200 (config) ≠ 1000 (plan.md)
   ...
   ```

## Config Sync Registry

> Maps `project_config.yaml` keys to their inline display locations.
> Agent reads this table to find where values appear, compares with YAML, and proposes updates.

### scope_budgets

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `scope_budgets.max_files_per_phase` | `.tfw/workflows/plan.md` | Scope Budget per Phase | Files per phase |
| `scope_budgets.max_files_per_phase` | `.tfw/conventions.md` | 6) Scope Budgets | Files per phase |
| `scope_budgets.max_new_files` | `.tfw/workflows/plan.md` | Scope Budget per Phase | New files per phase |
| `scope_budgets.max_new_files` | `.tfw/conventions.md` | 6) Scope Budgets | New files per phase |
| `scope_budgets.max_loc` | `.tfw/workflows/plan.md` | Scope Budget per Phase | LOC per phase |
| `scope_budgets.max_loc` | `.tfw/conventions.md` | 6) Scope Budgets | LOC per phase |
| `scope_budgets.max_modified_files` | `.tfw/workflows/plan.md` | Scope Budget per Phase | Modified files |
| `scope_budgets.max_modified_files` | `.tfw/conventions.md` | 6) Scope Budgets | Modified files |

### research

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `research.max_web_queries_per_stage` | `.tfw/workflows/research/base.md` | Limits | Web queries per stage |
| `research.max_files_per_stage` | `.tfw/workflows/research/base.md` | Limits | Project files read per stage |
| `research.max_questions_per_turn` | `.tfw/workflows/research/base.md` | Limits | Questions to user per turn |
| `research.max_passes` | `.tfw/workflows/research/base.md` | Limits | Max passes |
| `research.default_mode` | `.tfw/workflows/research/base.md` | Step 2: Select Mode | (read in step) |
| `research.modes.focused.loops_per_stage` | `.tfw/workflows/research/focused.md` | Stage Behavior | OODA loops per stage |
| `research.modes.deep.loops_per_stage` | `.tfw/workflows/research/deep.md` | Stage Behavior | OODA loops per stage |

### knowledge

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `knowledge.interval` | `.tfw/workflows/knowledge.md` | Limits | Consolidation interval |
| `knowledge.gate_mode` | `.tfw/workflows/knowledge.md` | Limits | Gate mode |
| `knowledge.max_facts_per_topic` | `.tfw/workflows/knowledge.md` | Limits | Max facts per topic |
| `knowledge.max_topic_files` | `.tfw/workflows/knowledge.md` | Limits | Max topic files |

### review

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `review.min_verify_ratio` | `.tfw/workflows/review.md` | Step 2: Verify | Min verify ratio |

### content_language

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `content_language` | `.tfw/conventions.md` | 11) Quality Standard | Content Language |

## Adapter Sync

Two adapter folders hold **full byte copies** of the workflows. After modifying any workflow file,
copy it to **both**. Copy only what changed in this session.

| Source in `.tfw/workflows/` | Copy name in `.claude/commands/` and `.agent/workflows/` |
|---|---|
| `plan.md` · `handoff.md` · `review.md` · `resume.md` | `tfw-plan.md` · `tfw-handoff.md` · `tfw-review.md` · `tfw-resume.md` |
| `docs.md` · `knowledge.md` · `config.md` · `init.md` | `tfw-docs.md` · `tfw-knowledge.md` · `tfw-config.md` · `tfw-init.md` |
| `release.md` · `update.md` | `tfw-release.md` · `tfw-update.md` |
| `research/base.md` | `tfw-research.md` |

```bash
# one workflow, both folders — {name} = source stem, e.g. review
cp .tfw/workflows/{name}.md .claude/commands/tfw-{name}.md
cp .tfw/workflows/{name}.md .agent/workflows/tfw-{name}.md
```

**Not copied, and why:**

| File | Reason |
|---|---|
| `research/deep.md`, `research/focused.md` | Mode files, read from `.tfw/` on demand — no adapter copy exists |
| `.claude/commands/tfw-task.md`, `.agent/workflows/tfw-task.md` | Adapter-only meta-workflow; it has no `.tfw/` source to copy from |
| Codex `tfw-*/SKILL.md` | Thin routers, not copies. They name the command and point at the canonical workflow, so a body change needs no re-copy. Re-sync only when a command name, its routing or its contract changes — source `.tfw/adapters/codex/skills/`, installed `.agents/skills/` |

### Drift check

Run after syncing, and before any release. Prints every copy that no longer matches its source:

```bash
for f in .claude/commands/tfw-*.md .agent/workflows/tfw-*.md; do
  b=$(basename "$f" .md); s=".tfw/workflows/${b#tfw-}.md"
  [ "$b" = "tfw-research" ] && s=".tfw/workflows/research/base.md"
  [ "$b" = "tfw-task" ] && continue
  [ -f "$s" ] && { diff -q "$s" "$f" >/dev/null || echo "DRIFT: $f vs $s"; }
done
```

Silent output = every copy matches. Any `DRIFT:` line means that environment is running a different
workflow than `.tfw/` defines — the adapter-parity promise is broken until it is re-copied.

## Anti-patterns

- Modifying inline values without updating project_config.yaml (source of truth)
- Modifying project_config.yaml without updating inline locations
- Skipping adapter sync after workflow modification
- Copying a workflow to one adapter folder and not the other — one environment then runs a different workflow than the rest
- Reporting an adapter sync as done without running the drift check
- Adding new inline value locations without updating the Config Sync Registry

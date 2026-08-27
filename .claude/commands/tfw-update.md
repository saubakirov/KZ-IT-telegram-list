---
description: TFW Update — upgrade project's .tfw/ from upstream starter
---

# TFW Update — Framework Upgrade Workflow

> **Role:** Coordinator
> **Trigger:** Manually, when a new TFW version is available upstream
> **Source:** Upstream starter repository configured in `tfw.upstream`

## Prerequisites

1. Read project's `.tfw/project_config.yaml` → `tfw.version` (current) and `tfw.upstream` (source URL)
2. Fetch upstream into `.tfw/.upstream/` (see Step 0)
3. Read `.tfw/.upstream/.tfw/VERSION` → target version
4. Read `.tfw/.upstream/.tfw/CHANGELOG.md` → changes since current version

## Step 0: Fetch Upstream

Read `tfw.upstream` from `.tfw/project_config.yaml` — this is the source repository URL.

Clean any previous staging directory and clone fresh:

**Linux / macOS:**
```bash
rm -rf .tfw/.upstream
git clone --depth 1 {tfw.upstream} .tfw/.upstream
```

**Windows (PowerShell):**
```powershell
if (Test-Path .tfw/.upstream) { Remove-Item -Recurse -Force .tfw/.upstream }
git clone --depth 1 {tfw.upstream} .tfw/.upstream
```

> In CL mode, present the exact command with the resolved URL for the user to run.
> `.tfw/.upstream/` is gitignored — safe to create in the project directory.

## Step 1: Compare Versions

```
Current: {project tfw.version}
Target:  {.tfw/.upstream/.tfw/VERSION}
```

If current == target → already up to date. Stop.

## Step 2: Review CHANGELOG

Read all entries in `.tfw/.upstream/.tfw/CHANGELOG.md` between current and target version. List every change.

## Step 3: Categorize Changes

For each changed file, classify:

| Category | Symbol | Meaning | Action |
|----------|--------|---------|--------|
| State | ⚫ | Project runtime state — never part of framework | **NEVER overwrite.** Skip entirely |
| Safe | 🟢 | New file, or file not customized by project | Copy from `.tfw/.upstream/.tfw/` directly |
| Merge | 🟡 | File exists and may have project-specific changes | Manual review: diff `.tfw/.upstream/.tfw/` vs local, merge carefully |
| Breaking | 🔴 | File removed, renamed, or structurally changed | Follow migration notes in CHANGELOG |

### Files that are project state (⚫ — NEVER overwrite):
- `.tfw/knowledge_state.yaml` — project knowledge consolidation tracking
- `knowledge/` — project-specific verified facts (NOT from upstream)
- `KNOWLEDGE.md` — project knowledge index (NOT from upstream)
- `TECH_DEBT.md` — project tech debt (NOT from upstream)

### Files typically safe to overwrite (🟢):
- `.tfw/VERSION` ← copy from `.tfw/.upstream/.tfw/VERSION`
- `.tfw/CHANGELOG.md` ← copy from `.tfw/.upstream/.tfw/CHANGELOG.md`
- New templates in `.tfw/templates/`
- New workflows in `.tfw/workflows/`

### Files requiring merge (🟡):
- `.tfw/conventions.md` — project may have added project-specific conventions
- `.tfw/glossary.md` — project may have added project-specific terms
- `.tfw/project_config.yaml` — project has custom values
  **Project sections** (preserve): `project.*`, `tfw.task_prefix`, `tfw.initial_seq`,
  `tfw.content_language`, `build.*`, `stack.*`, `tfw.user_preferences`
  **Framework sections** (update): `tfw.version`, `tfw.templates`, `tfw.workflows`,
  `tfw.statuses`, `tfw.scope_budgets`, `tfw.research`, `tfw.review`, `tfw.knowledge`

### Files to check for breaking changes (🔴):
- Any file listed under `### Removed` or `### Changed` in CHANGELOG
- Template structural changes (new required sections, renamed fields)

## Step 4: Generate Update Checklist

Create a concrete checklist of actions:

```markdown
## Update Checklist: v{current} → v{target}

### 🟢 Auto-apply
- [ ] Copy `.tfw/VERSION` from `.tfw/.upstream/.tfw/VERSION`
- [ ] Copy `.tfw/CHANGELOG.md` from `.tfw/.upstream/.tfw/CHANGELOG.md`
- [ ] Copy `.tfw/workflows/{new-workflow}.md` from `.tfw/.upstream/.tfw/workflows/`
- [ ] Copy `.agent/workflows/tfw-{new-workflow}.md` (adapter)

### 🟡 Manual merge
- [ ] Diff `.tfw/conventions.md` — merge new sections, keep project customizations
- [ ] Diff `.tfw/glossary.md` — add new terms, keep project terms

### 🔴 Breaking changes
- [ ] {Specific migration action from CHANGELOG}
```

## Step 5: Execute Update

Apply changes from the checklist. For each item:
1. Apply the change
2. Verify no project customizations were lost
3. Check the item off

## Step 6: Re-sync Adapters

Update tool-specific adapter copies from `.tfw/`:

| Adapter | Source | Target |
|---------|--------|--------|
| Antigravity workflows | `.tfw/workflows/*.md` | `.agent/workflows/tfw-*.md` |
| Antigravity rules | `.tfw/adapters/antigravity/` | `.agent/rules/` |
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/` |
| Codex skills | `.tfw/adapters/codex/skills/tfw-*/SKILL.md` | `.agents/skills/tfw-*/SKILL.md` |
| Codex routing | `.tfw/adapters/codex/AGENTS.md.template` managed block | Root `AGENTS.md` managed block |

Only re-sync adapters that the project uses.

For Codex, read `.tfw/adapters/codex/README.md` and run its Install or Repair
procedure. Re-copy only the `tfw-*` directories present under
`.tfw/adapters/codex/skills/`. Replace or append only the marker-bounded TFW block in
root `AGENTS.md`. Never glob or overwrite unrelated `.agents/skills/*` or instructions
outside the markers. Remove `source-command-tfw-*` only when inspection confirms it is
a legacy migrated copy of a canonical TFW workflow.

## Step 7: Update Version Marker

Update `tfw.version` in `.tfw/project_config.yaml` to the target version.

## Step 8: Verify

- `tfw.version` in project_config.yaml matches `.tfw/VERSION`
- All adapter copies are in sync with `.tfw/workflows/`
- Codex `.agents/skills/tfw-*` copies match `.tfw/adapters/codex/skills/tfw-*` when the project uses Codex
- Root `AGENTS.md` has exactly one current TFW managed block when the project uses Codex
- Literal `/tfw-*` smoke test routes to the matching local workflow; `$tfw-*` and `/skills` are fallbacks, not required user syntax
- Project-specific customizations preserved in conventions.md and glossary.md
- Build/lint/test still pass (if applicable)

## Step 9: Cleanup

Remove the staging directory:

**Linux / macOS:**
```bash
rm -rf .tfw/.upstream
```

**Windows (PowerShell):**
```powershell
Remove-Item -Recurse -Force .tfw/.upstream
```

Optional — `.tfw/.upstream/` is gitignored, so leaving it is harmless.

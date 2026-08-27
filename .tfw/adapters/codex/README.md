# TFW Codex Adapter

> **Instructions for Codex:** install or repair this adapter so people can use the same
> `/tfw-*` commands they use in Claude Code and Antigravity. Do not require users to
> learn a Codex-specific wrapper.

## Required Outcome

After setup, a person can open the repository in Codex and type:

```text
/tfw-plan Describe the task
/tfw-handoff TASK-12 phase b
/tfw-review TASK-12 phase b
/tfw-resume
```

Codex must recognize the project as TFW, load the correct local workflow, enforce its
role lock and gates, and leave a filesystem trace that another agent can resume.

## Architecture

| Layer | Location | Responsibility |
|-------|----------|----------------|
| Always-on project guidance | Root `AGENTS.md` | Recognize TFW, route literal `/tfw-*` prompts, define the fallback when a skill is unavailable |
| Command implementation | `.agents/skills/tfw-*/SKILL.md` | Give every workflow a separately discoverable, progressively loaded Codex entry point |
| Framework-owned source | `.tfw/adapters/codex/skills/tfw-*/SKILL.md` | Canonical adapter files copied into `.agents/skills/` |
| Process source of truth | `.tfw/workflows/` | Full workflow logic, roles, gates, artifacts, and hard stops |

Skills are the supported Codex format for repository-shared workflows. They are an
implementation detail of the command surface: public TFW instructions lead with
`/tfw-*`. `$tfw-*` and `/skills` are explicit-selection fallbacks for Codex surfaces
that need them.

## Command Map

| User command | Canonical workflow |
|--------------|--------------------|
| `/tfw-plan` | `.tfw/workflows/plan.md` |
| `/tfw-research` | `.tfw/workflows/research/base.md` |
| `/tfw-handoff` | `.tfw/workflows/handoff.md` |
| `/tfw-review` | `.tfw/workflows/review.md` |
| `/tfw-resume` | `.tfw/workflows/resume.md` |
| `/tfw-docs` | `.tfw/workflows/docs.md` |
| `/tfw-knowledge` | `.tfw/workflows/knowledge.md` |
| `/tfw-release` | `.tfw/workflows/release.md` |
| `/tfw-update` | `.tfw/workflows/update.md` |
| `/tfw-config` | `.tfw/workflows/config.md` |
| `/tfw-init` | `.tfw/workflows/init.md` |

`/tfw-task` is intentionally absent. It is not a canonical workflow and duplicates
the plan/handoff logic across a mandatory role boundary.

## Install or Repair

Run this procedure from the repository root. It is idempotent.

### 1. Detect project state

1. If `.tfw/` is absent, stop. Obtain the TFW core first, then run `/tfw-init`.
2. If `.tfw/` exists but the project has no configured Task Board or task traces,
   continue the full `.tfw/workflows/init.md` workflow.
3. If `.tfw/`, a configured Task Board, and task traces already exist, treat this as
   **Codex attach/repair**. Do not recreate or reset `project_config.yaml`,
   `knowledge_state.yaml`, `KNOWLEDGE.md`, `TECH_DEBT.md`, `README.md`, or `tasks/`.

### 2. Install exact command copies

Create `.agents/skills/`, then copy every source `tfw-*` directory from
`.tfw/adapters/codex/skills/`. Preserve unrelated skills.

Linux/macOS:

```bash
mkdir -p .agents/skills
cp -R .tfw/adapters/codex/skills/tfw-* .agents/skills/
```

Windows PowerShell:

```powershell
$tfwSkillSource = ".tfw/adapters/codex/skills"
$tfwSkillTarget = ".agents/skills"
New-Item -ItemType Directory -Force -Path $tfwSkillTarget | Out-Null
Get-ChildItem -LiteralPath $tfwSkillSource -Directory -Filter "tfw-*" |
  Copy-Item -Destination $tfwSkillTarget -Recurse -Force
```

Commit `.agents/skills/tfw-*/SKILL.md` with the project. Never install these files
only in a user's home directory: the next contributor and the next agent must receive
the same commands from the repository.

### 3. Merge the always-on routing block

The file `AGENTS.md.template` contains an adapter-owned block delimited by:

```text
<!-- TFW:CODEX:START -->
<!-- TFW:CODEX:END -->
```

- If root `AGENTS.md` has the markers, replace only the text between them with the
  current template block.
- If it has no markers, append the complete block.
- If root `AGENTS.md` is absent, create it with project guidance plus the block.
- Never replace instructions outside the markers. They belong to the project.
- Keep exactly one managed block.

### 4. Remove obsolete imported copies

Old Codex imports may have created `.agents/skills/source-command-tfw-*` skills that
embed complete snapshots of `.tfw/workflows`. They are stale second sources of truth
and create duplicate commands.

Remove a `source-command-tfw-*` directory only when its `SKILL.md` identifies itself
as a migrated source command or contains a copied TFW workflow body. Preserve any
unrelated or independently authored skill. Current TFW commands are the `tfw-*`
directories sourced from this adapter.

### 5. Verify

Codex must verify all of the following before reporting success:

- The command set exactly matches `tfw.workflows` in `.tfw/project_config.yaml`:
  plan, research, handoff, review, resume, docs, knowledge, release, update, config,
  and init.
- Every installed `SKILL.md` is byte-identical to its adapter source.
- Every skill has valid `name` and `description` frontmatter and names its `/tfw-*`
  command in the description.
- Root `AGENTS.md` contains exactly one managed TFW block.
- No confirmed legacy `source-command-tfw-*` duplicate remains.
- Literal `/tfw-*` input routes to the matching local workflow. Use a safe smoke test:
  `/tfw-resume Verify Codex adapter routing only; do not modify project.`

Codex normally detects skill changes automatically. If the command does not appear or
route after files pass verification, start a new Codex task or restart Codex, then run
the smoke test again. Do not claim success from file existence alone.

## Runtime Contract

When any `/tfw-*` command reaches Codex:

1. Prefer the matching repository-local `tfw-*` skill.
2. Read the referenced `.tfw/workflows/` file completely; it is authoritative.
3. Load only the context that workflow requires, using progressive disclosure.
4. Enforce the workflow's role lock, approval gates, templates, evidence rules, and
   hard stop exactly.
5. Recommend the next step using `/tfw-*`, never an adapter-specific wrapper.
6. If the skill is unavailable but `.tfw/` exists, route directly through the command
   table in root `AGENTS.md`; missing discoverability must not block correct behavior.

## Official Codex Basis

- [Build skills](https://learn.chatgpt.com/docs/build-skills): repository skills live
  in `.agents/skills`, use progressive disclosure, and can be invoked explicitly or
  implicitly.
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): durable
  repository guidance is loaded automatically.
- [Import from another agent](https://learn.chatgpt.com/docs/import): Codex maps
  imported slash commands to Skills. Deprecated custom prompts are not used by this
  adapter.

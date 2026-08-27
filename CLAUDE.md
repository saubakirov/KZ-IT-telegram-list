# KZ-IT-telegram-list — Claude Code Adapter

> [`AGENTS.md`](AGENTS.md) is the canonical project contract. Read it before acting and follow
> it for project purpose, data rules, workflows, quality standards, and safety boundaries.
> Duplicating those rules in this adapter is a defect because the copies can diverge.

## Context Loading

Claude Code auto-loads this file. For a new session, continue in this order:

1. `AGENTS.md`
2. `.tfw/conventions.md`
3. `.tfw/glossary.md`
4. `KNOWLEDGE.md`, when present
5. `tasks/00-INDEX.md` to locate the task, then that task's own `status.md`
6. Only the HL, TS, RF, and other traces relevant to the active task

## Slash-Command Routing

The files under `.claude/commands/` are Claude Code adapters. They route to the canonical
workflows under `.tfw/workflows/`; adapters do not redefine those workflows.

| Command | Claude Code adapter | Canonical workflow |
|---------|---------------------|--------------------|
| `/tfw-plan` | `.claude/commands/tfw-plan.md` | `.tfw/workflows/plan.md` |
| `/tfw-research` | `.claude/commands/tfw-research.md` | `.tfw/workflows/research/base.md` |
| `/tfw-handoff` | `.claude/commands/tfw-handoff.md` | `.tfw/workflows/handoff.md` |
| `/tfw-review` | `.claude/commands/tfw-review.md` | `.tfw/workflows/review.md` |
| `/tfw-resume` | `.claude/commands/tfw-resume.md` | `.tfw/workflows/resume.md` |
| `/tfw-docs` | `.claude/commands/tfw-docs.md` | `.tfw/workflows/docs.md` |
| `/tfw-knowledge` | `.claude/commands/tfw-knowledge.md` | `.tfw/workflows/knowledge.md` |
| `/tfw-release` | `.claude/commands/tfw-release.md` | `.tfw/workflows/release.md` |
| `/tfw-update` | `.claude/commands/tfw-update.md` | `.tfw/workflows/update.md` |
| `/tfw-config` | `.claude/commands/tfw-config.md` | `.tfw/workflows/config.md` |
| `/tfw-init` | `.claude/commands/tfw-init.md` | `.tfw/workflows/init.md` |
| `/tfw-task` | `.claude/commands/tfw-task.md` | Meta-workflow adapter; obeys each invoked workflow's hard stop |

## Execution Mode

Claude Code defaults to CL (Chat Loop). AG (Autonomous) local execution is permitted only when
an approved TFW task or phase specification explicitly grants it. External-state actions remain
subject to the gates in the canonical project contract and active specification.

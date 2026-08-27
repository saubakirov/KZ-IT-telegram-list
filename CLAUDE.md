# KZ-IT-telegram-list — Claude Code Rules

## Project Identity
- Name: KZ-IT-telegram-list ("Awesome Kazakhstan IT Telegram")
- Stack: Python 3.10+ scripts over a JSON source of truth; no runtime service, no build system
- Owner: saubakirov

## Mandatory Rules
1. **No sycophancy**: Be direct, precise, concrete.
2. **No placeholders**: Provide complete working code/config. Never invent a community, a handle, or a member count.
3. **Language**: Reply in the user's latest message language. TFW artifact content is written in English (`tfw.content_language: en`).
4. **TFW task discipline**: Follow `.tfw/workflows/` for every task.
5. **Critical mindset**: Question assumptions, flag risks.

## TFW 1.3.0
This project follows Trace-First Workflow 1.3.0. Read `.tfw/README.md` for philosophy and lifecycle.

### Context Loading (new session)
1. `CLAUDE.md` — this file (auto-loaded)
2. `AGENTS.md` — AI role and mission
3. `.tfw/conventions.md` — TFW conventions
4. `.tfw/glossary.md` — TFW glossary
5. `KNOWLEDGE.md` — project knowledge index
6. `tasks/README.md` — Task Board (current work)
7. Relevant HL/TS/RF for the current task

### Slash Commands

| Command | Workflow | Role | Purpose |
|---------|----------|------|---------|
| `/tfw-plan` | `.tfw/workflows/plan.md` | Coordinator | Research, write HL, RESEARCH gate, write TS |
| `/tfw-research` | `.tfw/workflows/research/base.md` | Researcher | Structured investigation — pipeline or standalone |
| `/tfw-handoff` | `.tfw/workflows/handoff.md` | Executor | ONB, implement, RF |
| `/tfw-review` | `.tfw/workflows/review.md` | Reviewer | Review RF against checklist, write REVIEW |
| `/tfw-resume` | `.tfw/workflows/resume.md` | Coordinator | Status matrix, decide next phase |
| `/tfw-docs` | `.tfw/workflows/docs.md` | Coordinator | Update KNOWLEDGE.md and TECH_DEBT.md |
| `/tfw-knowledge` | `.tfw/workflows/knowledge.md` | Coordinator | Consolidate verified facts into `knowledge/` |
| `/tfw-task` | Meta-workflow | Coordinator | Full lifecycle: plan + handoff with hard stop |
| `/tfw-config` | `.tfw/workflows/config.md` | Coordinator | Propagate project_config.yaml changes |
| `/tfw-release` | `.tfw/workflows/release.md` | Coordinator | Version bump, CHANGELOG, tag |
| `/tfw-init` | `.tfw/workflows/init.md` | Coordinator | Initialize TFW — discover, interview, setup |
| `/tfw-update` | `.tfw/workflows/update.md` | Coordinator | Fetch upstream, compare, sync adapters |

### Templates
Canonical artifact templates in `.tfw/templates/` — see `tfw.templates` in `.tfw/project_config.yaml`.

### Key References
- `.tfw/README.md` — philosophy
- `.tfw/conventions.md` — all formal rules
- `.tfw/CHANGELOG.md` — framework version history
- `.tfw/project_config.yaml` — project parameters

## Execution Mode
**Default: CL (Chat Loop)** — AI proposes, user approves.
**AG (Autonomous):** Only after the user approves the plan.

Use CL for anything that depends on live external state (Telegram link liveness, member
counts). Use AG for local file operations once a plan is approved.

## Code Standards

### The generation contract — read this before touching README.md
```
data/communities.json  ← the ONLY source of truth. Edit this.
        ↓  scripts/generate_readme.py
README.md              ← fully overwritten on every run. NEVER edit by hand.
```
`generate_readme.py` writes `README.md` from scratch — any hand-edit to `README.md` is
silently destroyed on the next run. Content that must appear in `README.md` has to be
emitted by the generator.

### Change procedure
1. Edit `data/communities.json`
2. `python scripts/validate_schema.py` — structure, required fields, category membership
3. `python scripts/validate_links.py` — link liveness and member counts (network; CL mode)
4. `python scripts/generate_readme.py` — regenerate `README.md`
5. Commit JSON and the regenerated README together

### Data rules
- Required fields: `name`, `handle`, `description`, `last_verified`; `category` for groups
- `handle` — bare Telegram handle, no `@` and no `t.me/` prefix
- Dates — ISO `YYYY-MM-DD`
- `category` must exist in the `categories` map in `data/communities.json`
- English `description` is required; `description_ru` is optional
- `member_count` is an integer or absent — never a guess

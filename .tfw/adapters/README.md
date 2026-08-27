# TFW Adapters

## Available Adapters

| Tool | Adapter Dir | Entry Point |
|------|------------|-------------|
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/tfw.mdc` |
| Antigravity | `.tfw/adapters/antigravity/` | `.agent/rules/tfw.md` |
| Codex | `.tfw/adapters/codex/` | Root `AGENTS.md` + `.agents/skills/tfw-*/SKILL.md` |

See each adapter's README for setup instructions.

## How to Write a New Adapter

An adapter is a bridge between a development tool and `.tfw/`. Requirements:

1. **Entry point** — the file or skill directory your tool discovers (e.g., CLAUDE.md, .cursor/rules/*.mdc, .agents/skills/*/SKILL.md)
2. **References `.tfw/`** — points to conventions, glossary, workflows. Never duplicates them.
3. **Minimal** — ≤35 lines of content. Project-specific sections only.
4. **Contains**:
   - Reference to `.tfw/README.md` (philosophy)
   - Reference to `.tfw/conventions.md` (rules)
   - Context loading order
   - Reference to `.tfw/workflows/` (all canonical workflows)
   - Conduct rules (no sycophancy, no placeholders)

### Template structure

```markdown
# TFW {version}
Read `.tfw/README.md` for philosophy. Follow `.tfw/conventions.md`.
Workflows: see `tfw.workflows` in `.tfw/project_config.yaml`.
Context: AGENTS.md → .tfw/conventions.md → .tfw/glossary.md
Rules: no sycophancy, no placeholders, user's language.
```

> When creating an adapter from a template, replace `{version}` with the value from `tfw.version` in `.tfw/project_config.yaml`.
> The `tfw-update` workflow re-copies templates, so version is refreshed automatically on updates.

Place adapter template in `.tfw/adapters/{tool-name}/` with a README explaining setup.

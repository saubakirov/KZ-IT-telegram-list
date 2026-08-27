# Compilable Contract

> TFW artifacts are structured by design. This contract defines what structure utilities expect
> for deterministic compilation into documentation sites, MCP endpoints, or other output formats.
> Agents maintain structure (Layer 1). Utilities consume this contract (Layer 2).

## 1) Source Manifest

All `.md` files below are compilable. The utility walks these paths:

| # | Source Path | Output Path | Behavior |
|---|------------|-------------|----------|
| 1 | `README.md` | `index.md` | Full copy. If `docs/index.md` exists, use it as override |
| 2 | `.tfw/README.md` | `concepts/philosophy.md` | Copy + frontmatter |
| 3 | `.tfw/quickstart.md` | `getting-started.md` | Copy + frontmatter |
| 4 | `.tfw/conventions.md` | `reference/conventions.md` | Copy + frontmatter |
| 5 | `.tfw/glossary.md` | `reference/glossary.md` | Copy + frontmatter |
| 6 | `.tfw/CHANGELOG.md` | `reference/changelog.md` | Copy + frontmatter |
| 7 | `KNOWLEDGE.md` | `knowledge-index.md` | Copy + frontmatter (whole file, no split) |
| 8 | `knowledge/*.md` | `knowledge/{filename}.md` | Copy each + frontmatter |
| 9 | `TECH_DEBT.md` | `reference/tech-debt.md` | Copy + frontmatter |
| 10 | `RELEASE.md` | `reference/release.md` | Copy + frontmatter. Optional — skip if absent |
| 11 | `tasks/**/*.md` | `tasks/{same relative path}` | Copy + frontmatter. Preserve folder structure |
| 12 | `.tfw/workflows/**/*.md` | `reference/workflows/{path}` | Copy + frontmatter |
| 13 | `.tfw/templates/**/*.md` | `reference/templates/{path}` | Copy + frontmatter |
| 14 | `.tfw/compilable_contract.md` | `reference/compilable-contract.md` | Copy + frontmatter |

> **Principle:** `tasks/` preserve their folder structure in output so that all relative links
> between artifacts (HL→TS, RF→HL, REVIEW→RF) work without rewriting.

File existence rules:

| Source | Required? | On Missing |
|--------|-----------|------------|
| `README.md` | Required | ERROR |
| `.tfw/README.md`, `conventions.md`, `glossary.md`, `CHANGELOG.md`, `quickstart.md` | Required | ERROR |
| `KNOWLEDGE.md` | Optional | WARNING, skip page |
| `knowledge/` | Optional | WARNING, skip section |
| `TECH_DEBT.md` | Optional | WARNING, skip page |
| `RELEASE.md` | Optional | Skip silently |
| `tasks/` | Optional | Skip silently |
| `docs/index.md` | Optional | Falls back to README.md |

## 2) Reference Format

Agents write **text references** to other artifacts. A build-time resolver converts these into
hyperlinks. Agents do NOT write full markdown links for cross-artifact references (saves tokens,
reduces errors).

Standard reference patterns:

| Pattern | Example | Resolves to |
|---------|---------|-------------|
| `{TYPE} {PREFIX}-{N}` | `RF TFW-18` | `tasks/TFW-18*/RF__*.md` (glob) |
| `{TYPE} {PREFIX}-{N} §{section}` | `RF TFW-18 §6` | Same file, anchor to section |
| `{TYPE} {PREFIX}-{N}/{PHASE}` | `RF TFW-18/A` | `tasks/TFW-18*/phase-a/RF__phase-a*.md` |
| `HL-{PREFIX}-{N}` | `HL-TFW-19` | `tasks/TFW-19*/HL-TFW-19*.md` |
| `D{N}` | `D24` | KNOWLEDGE.md §1 Architecture Decisions row |
| `P{N}` | `P7` | HL §7 Principles row (task-local) |
| `PP{N}` | `PP2` | Project principle registry row — `KNOWLEDGE.md` §0 where a project keeps one. Reserved: no resolution in a project without §0 |
| `NS{N}` | `NS3` | Project North Star clause — the designated README section(s), conventions.md §3 |
| `F{N}` in knowledge context | `F4` | knowledge/{category}.md row |
| `TD-{N}` | `TD-59` | TECH_DEBT.md row |
| `S{N}` | `S9` | HL §11 Strategic Insights row (task-local) |

Where references appear:
- `KNOWLEDGE.md` §1 Source column, §2 Key Artifact column, §3 Source column
- `knowledge/*.md` Source(s) column
- `TECH_DEBT.md` Source column
- `RF.md` §2 Key Decisions (rationale text), §7 FC Source column
- `REVIEW.md` §3 Tech Debt Source column, §7 FC Source column
- `RES.md` Decisions Rationale column, HL Recommendations Source column, FC Source column
- Any inline mention in artifact prose

Resolution rules:
- Resolver uses `tfw.task_prefix` from project_config.yaml to know the prefix
- Glob-based: `{TYPE} TFW-18` → find `tasks/TFW-18*/{TYPE}__*.md`
- If glob returns multiple matches → use first alphabetically, emit WARNING
- If glob returns zero matches → leave as text, emit WARNING
- Phase references: `RF TFW-18/A` → search in `tasks/TFW-18*/phase-a/` first, then task root
- `D{N}`, `P{N}`, `F{N}`, `PP{N}`, `NS{N}`, `TD-{N}` → anchor links within the appropriate index page
- Resolver runs as a post-processing step on generated pages (regex scan + replacement)

## 3) Frontmatter Convention

Every output page gets YAML frontmatter:

```yaml
---
title: "{from first # heading or filename}"
source: "{relative path to source file}"
---
```

## 4) Output Navigation Structure

```
Home                              <- README.md (full, with Task Board)
Getting Started                   <- .tfw/quickstart.md
Concepts/
  Philosophy                      <- .tfw/README.md
Architecture/
  Knowledge Index                 <- KNOWLEDGE.md (whole file)
  Knowledge/
    {topic files}                 <- knowledge/*.md
Reference/
  Conventions                     <- .tfw/conventions.md
  Glossary                        <- .tfw/glossary.md
  Compilable Contract             <- .tfw/compilable_contract.md
  Tech Debt                       <- TECH_DEBT.md
  Changelog                       <- .tfw/CHANGELOG.md
  Release                         <- RELEASE.md
  Workflows/                      <- .tfw/workflows/**/*.md
  Templates/                      <- .tfw/templates/**/*.md
Tasks/
  {task folders with all artifacts} <- tasks/**/*.md (preserved structure)
```

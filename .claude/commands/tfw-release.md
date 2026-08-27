---
description: TFW Release — cut a versioned release of the project
---

# TFW Release — Version Release Workflow

> **Role:** Coordinator / Maintainer
> **Trigger:** Manually, when accumulated changes justify a new version
> **Prerequisite:** `RELEASE.md` exists with project-specific release context

## Prerequisites

1. Read `RELEASE.md` — understand what a release means for this project
2. Read `.tfw/CHANGELOG.md` — see the last released version
3. Read `.tfw/VERSION` — confirm current version
4. Read Task Board — identify tasks completed since last release

## Step 1: Scope the Release

1. List all tasks completed since the last version tag
2. Categorize changes:
   - **Framework changes** — templates, workflows, conventions, adapters
   - **Project changes** — task artifacts, documentation, internal improvements
3. Decide: do the accumulated changes justify a release? Consult `RELEASE.md` §4 (triggers)

> If NO → stop. Record decision in next RF if applicable.

## Step 2: Determine Version Bump

Consult `RELEASE.md` §3 (version scheme):

| Change type | Bump |
|-------------|------|
| Breaking changes (conventions, template structure, workflow steps changed/removed) | MAJOR |
| New features (new workflows, new templates, new optional artifacts) | MINOR |
| Fixes, clarifications, typos | PATCH |

> When in doubt, prefer MINOR over PATCH. Breaking changes MUST be MAJOR.

## Step 3: Pre-Release Checklist

Run through `RELEASE.md` §5 checklist. All items must pass before proceeding.

## Step 4: Write CHANGELOG Entry

Add a new section to `.tfw/CHANGELOG.md` under `## [Unreleased]`:

```
## [X.Y.Z] — YYYY-MM-DD
### Added
- ...
### Changed
- ...
### Deprecated
- ...
### Removed
- ...
### Fixed
- ...
```

Move items from `[Unreleased]` to the new version section. Only include categories that have entries.

## Step 5: Update Version Files

1. Update `.tfw/VERSION` to the new version
2. Update `tfw.version` in `.tfw/project_config.yaml`

## Step 6: Project-Specific Release Steps

Follow `RELEASE.md` §6 for any additional steps (git tag, deploy, publish, notify).

## Step 7: Verify

- `.tfw/VERSION` matches CHANGELOG latest entry
- `tfw.version` in project_config.yaml matches VERSION
- CHANGELOG entry has correct date and accurate content
- All pre-release checklist items passed

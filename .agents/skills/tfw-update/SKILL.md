---
name: tfw-update
description: Command /tfw-update upgrades and synchronizes local Trace-First Workflow files and adapters while preserving project state. Use for /tfw-update, upstream upgrades, version comparison, migration, or adapter repair.
---

# /tfw-update

This repository skill implements the `/tfw-update` command.

## Contract

- Treat literal `/tfw-update` input as a command. Also accept `tfw-update` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, `.tfw/VERSION`, `.tfw/CHANGELOG.md`, and `.tfw/adapters/README.md` in that order.
- Read `.tfw/workflows/update.md` completely before updating; it is the canonical workflow.
- Enforce the Coordinator role lock: permit `.tfw/` framework/config merges and adapter copies; forbid code changes.
- Never overwrite project state such as `.tfw/knowledge_state.yaml`, `knowledge/`, `KNOWLEDGE.md`, or `TECH_DEBT.md`; preserve project customizations during merges.
- Re-sync only adapters used by the project. Scope Codex installation to `.tfw/adapters/codex/skills/tfw-*/` → `.agents/skills/tfw-*/` and the marker-bounded TFW block in root `AGENTS.md`.
- Follow categorization, cleanup, and verification gates exactly as the workflow requires.

Report framework version status, copied adapters, preserved state, and manual merge risks.

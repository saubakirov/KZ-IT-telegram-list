---
name: tfw-init
description: Command /tfw-init initializes Trace-First Workflow or attaches and repairs TFW tooling in an existing project. Use for /tfw-init, first-time setup, project discovery, adapter installation, or Codex adapter repair.
---

# /tfw-init

This repository skill implements the `/tfw-init` command.

## Contract

- Treat literal `/tfw-init` input as a command. Also accept `tfw-init` and matching natural-language requests.
- If `.tfw/` exists, read `.tfw/workflows/init.md` completely; it is the canonical workflow. If `.tfw/` is missing, do not invent framework files—obtain the framework source or explain the missing prerequisite.
- Load available `AGENTS.md`, README files, project documentation, repository structure, and existing TFW state before changing files.
- Enforce the Coordinator role lock: permit TFW setup/config, adapters, and the init task's RES/RF traces required by the workflow; forbid HL, TS, and code unrelated to TFW setup.
- Use `.tfw/templates/*` whenever the workflow creates an artifact or state file.
- Detect an already-configured project and run the adapter attach/repair path without resetting project state. Do not rerun full initialization without user direction.
- Follow interview, research, verification, and stop gates exactly as the workflow requires.

Report created or updated files and project-specific assumptions requiring confirmation.

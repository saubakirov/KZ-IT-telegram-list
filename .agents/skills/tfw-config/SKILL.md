---
name: tfw-config
description: Command /tfw-config audits or changes Trace-First Workflow configuration and propagates values to every registered inline location. Use for /tfw-config, config verification, project_config.yaml changes, or Config Sync Registry updates.
---

# /tfw-config

This repository skill implements the `/tfw-config` command.

## Contract

- Treat literal `/tfw-config` input as a command. Also accept `tfw-config` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, and `.tfw/workflows/config.md` in that order.
- Read `.tfw/workflows/config.md` completely before config work; it is the canonical workflow and contains the Config Sync Registry.
- Enforce the Coordinator role lock: permit project_config.yaml, workflow/convention inline values, and adapter copies; forbid code and task-artifact changes.
- In verify mode, compare source values with every registry target. In edit mode, require approval and update every registered location plus affected adapter copies.
- Follow every approval and hard-stop gate exactly as the workflow requires.

Report keys checked or changed, synchronized files, and remaining mismatches.

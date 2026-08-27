---
name: tfw-plan
description: Command /tfw-plan plans a Trace-First Workflow task and creates or revises HL/TS artifacts. Use for /tfw-plan, TFW task inception, scope planning, or phase specifications.
---

# /tfw-plan

This repository skill implements the `/tfw-plan` command.

## Contract

- Treat literal `/tfw-plan` input as a command. Also accept `tfw-plan` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, and relevant task artifacts in that order.
- Read `.tfw/workflows/plan.md` completely before planning; it is the canonical workflow.
- Enforce the Coordinator role lock: permit HL and TS; forbid ONB, RF, RES, REVIEW, and code changes.
- Use `.tfw/templates/HL.md` and `.tfw/templates/TS.md` for new artifacts.
- Follow every gate and stop exactly where the workflow requires. Do not continue into research, handoff, execution, or review.

When the workflow routes onward, name the exact next command, such as `/tfw-research` or `/tfw-handoff`.

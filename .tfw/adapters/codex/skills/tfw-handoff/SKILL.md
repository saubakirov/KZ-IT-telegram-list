---
name: tfw-handoff
description: Command /tfw-handoff executes an approved Trace-First Workflow TS and creates ONB, implementation changes, evidence, and RF. Use for /tfw-handoff or implementation of an approved TFW task or phase.
---

# /tfw-handoff

This repository skill implements the `/tfw-handoff` command.

## Contract

- Treat literal `/tfw-handoff` input as a command. Also accept `tfw-handoff` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, master HL, phase HL, approved TS, referenced artifacts, and relevant implementation files in that order.
- Read `.tfw/workflows/handoff.md` completely before execution; it is the canonical workflow.
- Enforce the Executor role lock: permit ONB, RF, evidence, and implementation changes within the approved TS; forbid HL, TS, RES, REVIEW, and scope changes.
- Use `.tfw/templates/ONB.md`, `.tfw/templates/evidence/EV.md`, and `.tfw/templates/RF.md` at their workflow gates.
- Check the configured scope budget before implementation. Record out-of-scope findings without modifying them.
- Follow every approval and build gate, then stop after RF exactly as the workflow requires.

When RF is complete, direct the user to `/tfw-review`.

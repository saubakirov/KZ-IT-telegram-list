---
name: tfw-resume
description: Command /tfw-resume locates and resumes a Trace-First Workflow task from filesystem traces and Task Board state. Use for /tfw-resume, a phase status matrix, interrupted work, or selection of the next TFW stage.
---

# /tfw-resume

This repository skill implements the `/tfw-resume` command.

## Contract

- Treat literal `/tfw-resume` input as a command. Also accept `tfw-resume` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, and relevant task artifacts in that order.
- Read `.tfw/workflows/resume.md` completely before resuming; it is the canonical workflow.
- Enforce the Coordinator role lock for resume: permit read-only status analysis plus Phase HL/TS when the workflow reaches planning; forbid ONB, RF, RES, REVIEW, and code changes.
- Use artifact existence and Task Board state as evidence instead of chat memory.
- Follow the decision gate and stop exactly where the workflow requires.

Report the status matrix and name the exact next `/tfw-*` command after the user chooses a phase.

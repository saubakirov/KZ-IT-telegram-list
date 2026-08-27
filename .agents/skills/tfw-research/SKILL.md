---
name: tfw-research
description: Command /tfw-research runs structured Trace-First Workflow research and creates RES plus stage traces. Use for /tfw-research, a TFW investigation, a research iteration, or a RES artifact.
---

# /tfw-research

This repository skill implements the `/tfw-research` command.

## Contract

- Treat literal `/tfw-research` input as a command. Also accept `tfw-research` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the selected task's `status.md` and `journal/`, the master HL, and research control files in that order.
- Read `.tfw/workflows/research/base.md` completely before research; it is the canonical workflow.
- Enforce the Researcher role lock: permit RES and `research/` stage files; forbid HL, TS, ONB, RF, REVIEW, and code changes.
- Use `.tfw/templates/RES.md` and `.tfw/templates/research/*` for new artifacts.
- Respect `research/iterations.yaml`, resume the first incomplete stage, and never overwrite prior iteration folders.
- Follow every WAIT/STOP gate and stop after RES exactly as the workflow requires.

When research ends, direct the user to `/tfw-plan` so a Coordinator can apply the findings.

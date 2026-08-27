---
name: tfw-review
description: Command /tfw-review reviews a completed Trace-First Workflow RF against its TS, implementation, and evidence. Use for /tfw-review, a TFW verdict, RF verification, or a REVIEW artifact.
---

# /tfw-review

This repository skill implements the `/tfw-review` command.

## Contract

- Treat literal `/tfw-review` input as a command. Also accept `tfw-review` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the selected task's `status.md` and `journal/`, master/phase HL, TS, RF, evidence, and files needed to verify claims in that order.
- Read `.tfw/workflows/review.md` completely before review; it is the canonical workflow.
- Enforce the Reviewer role lock: permit review stage files and REVIEW; forbid ONB, RF, HL, TS, RES, code, and implementation changes.
- Use `.tfw/templates/review/*` and `.tfw/templates/REVIEW.md` for new artifacts.
- Verify RF claims against actual files, test output, and resolvable evidence; do not trust declarations alone.
- Follow every gate in the workflow exactly as it requires, including each stage self-check gate before advancing.

After APPROVE, direct the user to `/tfw-docs` and `/tfw-knowledge` when the workflow requires knowledge capture.

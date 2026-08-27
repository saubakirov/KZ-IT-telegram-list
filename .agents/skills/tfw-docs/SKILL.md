---
name: tfw-docs
description: Command /tfw-docs updates Trace-First Workflow project documentation and technical debt after review. Use for /tfw-docs or updates to KNOWLEDGE.md sections 1-3 or TECH_DEBT.md from RF/REVIEW results.
---

# /tfw-docs

This repository skill implements the `/tfw-docs` command.

## Contract

- Treat literal `/tfw-docs` input as a command. Also accept `tfw-docs` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md`, `TECH_DEBT.md`, the task's `status.md`, and the relevant REVIEW/RF in that order.
- Read `.tfw/workflows/docs.md` completely before documentation work; it is the canonical workflow.
- Enforce the Coordinator role lock: permit the documentation, convention, and debt surfaces named by the workflow; forbid code and implementation changes.
- Preserve traceability to RF, REVIEW, and task artifacts. Do not consolidate Fact Candidates into `knowledge/`; that belongs to `/tfw-knowledge`.
- Follow the triage gate and stop exactly where the workflow requires.

If Fact Candidates remain, direct the user to `/tfw-knowledge`.

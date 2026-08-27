---
name: tfw-knowledge
description: Command /tfw-knowledge consolidates Trace-First Workflow Fact Candidates into verified project knowledge. Use for /tfw-knowledge, the knowledge gate, fact promotion, topic files, or knowledge_state.yaml maintenance.
---

# /tfw-knowledge

This repository skill implements the `/tfw-knowledge` command.

## Contract

- Treat literal `/tfw-knowledge` input as a command. Also accept `tfw-knowledge` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, `.tfw/knowledge_state.yaml`, `KNOWLEDGE.md`, all `knowledge/` topic files, the Task Board, and candidate-bearing artifacts in that order.
- Read `.tfw/workflows/knowledge.md` completely before consolidation; it is the canonical workflow.
- Enforce the Coordinator role lock: permit `knowledge/`, KNOWLEDGE.md §4, knowledge state, and processed markers; forbid code and substantive edits to source artifacts.
- Treat every Fact Candidate as unverified until the workflow verifies it. Never invent facts or resolve contradictions without the user.
- Follow every WAIT gate and stop exactly where the workflow requires.

Report promoted, rejected, deferred, and unchanged facts with their sources.

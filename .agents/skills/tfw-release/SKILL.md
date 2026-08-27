---
name: tfw-release
description: Command /tfw-release prepares and cuts a versioned release under Trace-First Workflow. Use for /tfw-release, release scoping, version bumps, changelog entries, tag planning, or release verification.
---

# /tfw-release

This repository skill implements the `/tfw-release` command.

## Contract

- Treat literal `/tfw-release` input as a command. Also accept `tfw-release` and matching natural-language requests.
- Confirm the repository contains `.tfw/` and `RELEASE.md`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `RELEASE.md`, `.tfw/VERSION`, `.tfw/CHANGELOG.md`, task state across the configured containers, and relevant task artifacts in that order.
- Read `.tfw/workflows/release.md` completely before release work; it is the canonical workflow.
- Enforce the Coordinator/Maintainer role lock: permit version and changelog artifacts plus explicit project release steps; forbid unrelated code changes.
- Do not tag, push, publish, or deploy unless both the workflow and user authorization permit it.
- Follow every pre-release gate and stop exactly where the workflow requires.

Report the resolved version, changelog changes, verification results, and blocked gates.

# RF — TFW-4 / Phase B: Contract & Docs

> **Date**: 2026-08-27
> **Author**: Executor (Codex)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Phase HL**: [Phase B HL](HL__phase-b__contract_docs.md)
> **TS**: [TS Phase B](TS__phase-b__contract_docs.md)
> **Revision source**: [Phase B REVIEW](REVIEW__phase-b__contract_docs.md) (`REVISE`)

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `CHANGELOG.md` | Root Keep-a-Changelog catalog history, separated from framework history and seeded with truthful `[Unreleased]` Phase B work |
| `RELEASE.md` | Dated verified snapshot definition, triggers, gates, tag form, and stop-before-tag-and-push authority boundary |
| `ONB__phase-b__contract_docs.md` | Executor scope analysis, protected dirty-state fingerprints, risk review, and all 20 Master HL knowledge-citation confirmations |
| `evidence/EV__phase-b__contract_docs.md` | Environment, per-AC evidence statuses, deterministic outputs, commit audit, and protected-path comparison |
| `evidence/protected_manifest.tsv` | Ordered 115-row protected-path manifest retained for deterministic aggregate and file-hash replay |
| `RF__phase-b__contract_docs.md` | Phase B implementation result and review handoff |

### Modified Files

| File | Changes |
|------|---------|
| `AGENTS.md` | Removed hardcoded catalog statistics, removed the dead singular adapter from the repository map, added the live Codex adapter locus and project-operation declarations, and preserved the managed Codex block byte-for-byte |
| `CLAUDE.md` | Replaced duplicated project rules with a thin Claude Code adapter: canonical pointer, context loading, slash-command routing, and execution-mode default |
| `data/communities.json` | Added only the exact approved top-level `north_star` purpose and four ordered non-goals |
| `CONTRIBUTING.md` | Replaced copied mutable reference tables and stale instructions with canonical pointers, North Star gates, `master`, evidence rules, and archive-not-delete policy; revision removed the divergent copied validation sequence in favor of a pure `AGENTS.md` procedure pointer |
| `KNOWLEDGE.md` | Added D8–D12 while preserving D1–D7 and both accepted Phase A documentation rows |
| `tasks/README.md` | Advanced only the TFW-4 Phase B lifecycle state and trace links while preserving the existing Coordinator handoff hunk |

### Local Commits Before RF

| Commit | Scope |
|--------|-------|
| `ea4a694` | ONB only — `[codex/TFW-4/contract-docs/executor] record phase b onboarding` |
| `836c099` | Exactly the seven implementation paths — `[codex/TFW-4/contract-docs/executor] establish project contract` |
| `ce01b17` | Original EV/RF only — `[codex/TFW-4/contract-docs/executor] record phase b result` |
| `958ceb5` | Revision implementation, only `CONTRIBUTING.md` — `[codex/TFW-4/contract-docs/executor] remove duplicated contributor procedure` |

No network, live sweep, release command, tag, push, or whole-tree restore was performed.

## 2. Key Decisions

1. Treat the generated Codex region as an opaque byte range. Canonicalization occurred only
   around it, and the ONB hash was rechecked immediately after the edit and at AC-5.
2. Keep `CLAUDE.md` adapter-specific even where repeating a project rule would make the file more
   self-contained. D9 requires a structural pointer, not parallel prose that can drift.
3. Store the North Star as data without pulling Phase C forward. The existing validator and
   generator still ignore it; Phase B proves exact storage and catalog preservation only.
4. Use `[Unreleased]` for the documentation/data-contract result and make `RELEASE.md` explicitly
   future-facing. This records completed Phase B work without asserting a verified snapshot.
5. Patch current dirty `KNOWLEDGE.md` and Task Board state rather than reconstruct either file
   from `HEAD`. The accepted Phase A and Coordinator hunks are part of the handoff baseline.
6. Make `CONTRIBUTING.md` point to the canonical `AGENTS.md` change procedure without reproducing
   its command sequence. This closes the `--update` divergence while leaving procedure ownership
   in one place.
7. Retain the ordered protected-path rows and their exact serialization contract in evidence.
   Reviewers can now replay the 115-file snapshot without reconstructing hidden selection or
   ordering assumptions.

### Deviations

- No scope, acceptance-criteria, or implementation deviation occurred.
- The first AC-1 harness pattern did not account for Markdown backticks around the `AGENTS.md`
  link label and returned a false negative. A corrected read-only assertion passed against the
  unchanged implementation; the event is retained in EV for verification honesty.
- During the revision, an initial one-character manifest transcription error was caught by a
  line-by-line comparison and fixed before evidence acceptance. Two combined PowerShell harness
  attempts also stopped on local syntax/path mistakes before their affected gates ran; corrected
  focused gates subsequently passed. Neither event changed protected or out-of-scope files.

## 3. Acceptance Criteria

- [x] **AC-1 — Establish one canonical agent contract.** `AGENTS.md` owns the count-free project
  contract and both project-operation declarations; `CLAUDE.md` is adapter-only; the managed
  block remains `1515` bytes with ONB SHA-256 `3ec08a…bf46`; revision replay resolves all 35
  local links across the six Markdown implementation paths, while the original 24 named
  workflow/adapter paths remain resolved.
- [x] **AC-2 — Store the approved Project North Star without catalog drift.** Purpose and four
  non-goals match the frozen strings exactly; `archive` is absent; semantic hashes for `meta`,
  all live arrays, and `categories` match ONB; schema validation exits zero; generator output
  leaves `README.md` byte-identical.
- [x] **AC-3 — Publish truthful contributor and release policies.** Contributor guidance points
  to canonical sources, applies all non-goals, uses `master`, and requires evidence plus owner
  triage. It contains a pure pointer to the `AGENTS.md` change procedure and zero copied
  validation/generation commands. `RELEASE.md` defines dated snapshots and owner gates; root
  `CHANGELOG.md` contains only `[Unreleased]` work; no release state or tag exists.
- [x] **AC-4 — Index decisions D8–D12 without losing accepted knowledge.** D8–D12 each occur
  once, D13–D15 do not occur, and the D1–D7 plus Phase A row hashes equal ONB.
- [x] **AC-5 — Keep Phase B bounded, truthful, and ready for Phase C.** Implementation commit
  `836c099` contains exactly seven TS paths and revision commit `958ceb5` contains only
  `CONTRIBUTING.md`, both with current Codex attribution. The ordered 115-file manifest replays
  the ONB aggregate and every protected file hash with zero mismatches; the managed block,
  README, and empty tag set match ONB; unrelated dirty work remains outside executor commits.

## 4. Verification

- Lint (`python scripts/validate_schema.py`): **PASS** — exit 0, schema errors 0.
- Tests (`python scripts/validate_links.py`): **N/A** — this command is network-bound and the
  approved Phase B TS prohibits network access and live validation.
- Verify (`python scripts/validate_schema.py` then `python scripts/generate_readme.py`): **PASS** —
  both exit 0; `README.md` SHA-256 remains
  `cc730c6b5a442174b2821a0d891fbaf723a11c7a4356e809942e8856b64894f9` before and after.
- Build/compile gate: **N/A** — no build or compile command applies to this documentation and
  contract-data phase.
- JSON semantic comparison: **PASS** — every pre-existing top-level value matches baseline; only
  exact `north_star` data is new.
- Document/link gate: **PASS** — all 35 local Markdown links across the six Markdown
  implementation paths resolve; no forbidden placeholder or hardcoded catalog-statistic
  addition was found.
- Contributor-procedure gate: **PASS** — the canonical `AGENTS.md#change-procedure` pointer is
  present and the copied validation/generation command count is zero.
- Protected-path gate: **PASS** — the retained 115-row manifest serializes to SHA-256
  `14802fad376f4c906278b115820b2b57ef0afb361cc507559c1eba5108fa4864`; replay reports zero
  mismatches after removing only Reviewer-owned TD-10/TD-11 rows in memory.
- Attribution/tag gate: **PASS** — all four recorded executor commits use
  `[codex/TFW-4/contract-docs/executor]`, current metadata, and no pointing tag; tag count remains
  zero.

## 5. Evidence

See [EV file](evidence/EV__phase-b__contract_docs.md) for evidence details.

Evidence verdict: 0/5 VERIFIED, 0 DEFERRED, 0 BLOCKED, 5 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `AGENTS.md` | 195 | naming | The protected generated Codex block says the Task Board is in `README.md`, while project D7 and the canonical contract place it in `tasks/README.md`. It was preserved byte-for-byte as required; the adapter source should be corrected through its owning workflow rather than hand-edited here. |
| 2 | `.tfw/adapters/claude-code/CLAUDE.md.template` | 31 | naming | The framework template routes `/tfw-research` to nonexistent `.tfw/workflows/research.md` instead of `.tfw/workflows/research/base.md`. The live thin adapter is correct, but a future adapter reinstall from this template could reintroduce the broken route. |

## 7. Fact Candidates

No fact candidates. The user supplied execution authority and preservation constraints, not new
domain knowledge requiring consolidation.

## 8. Strategic Insights (Execution)

No strategic insights. The execution conversation added no new human-sourced strategic or domain
context beyond the approved Phase B contract.

## 9. Diagrams

```mermaid
graph TD
  AG[AGENTS.md<br/>canonical project contract] --> CL[CLAUDE.md<br/>Claude Code adapter]
  AG --> CO[CONTRIBUTING.md<br/>canonical pointers]
  NS[data/communities.json<br/>north_star] --> CO
  NS -. Phase C enforcement .-> VS[validate_schema.py]
  NS -. Phase C rendering .-> RD[README.md § Purpose]
  RL[RELEASE.md<br/>dated snapshot gates] --> KR[/kz-release<br/>Phase C adapter]
  KR --> CH[CHANGELOG.md<br/>catalog history]
```

---

*RF — TFW-4 / Phase B: Contract & Docs | 2026-08-27*

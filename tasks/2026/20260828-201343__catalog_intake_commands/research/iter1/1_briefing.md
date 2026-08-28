# Briefing — "What should we investigate?"
> **Mindset:** Strategist. This iteration plans an investigation rather than selecting an implementation. The approach must change if classifier safety, input accounting, self-contained copy parity, or holdout independence cannot be evidenced.
> **Test:** The investigation exists because the current catalog can validate only already-admitted handles, the new input surface has no loss-accounting grammar, editorial gates mix observable and human-governed claims, and complete agent copies create a new synchronization obligation.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Research Plan

### Gather

- Decompose the decision space across classifier integration, versioned evidence output, source grammar and loss accounting, approval binding, editorial responsibility, full-copy synchronization, and calibration/holdout isolation.
- Inspect the existing Telegram classifier, catalog schema/generator contracts, Claude `kz-*` commands, Codex/TFW adapter patterns, and the two supplied candidate sources without modifying or adopting their bytes.
- Compare complete-copy command arrangements in ready local projects and official Claude Code/Codex command or skill contracts; seek failure cases where apparent self-containment still depends on an unavailable runtime reference.
- Review primary guidance for CLI argument/file parsing, deterministic structured output, approval tokens or manifests, and train/test leakage controls that can be translated into this repository's small workflow.
- Test H2–H4 against counter-evidence: classifier coupling, ambiguous URL syntax, partial network failure, human-only editorial criteria, and leakage through candidate-aware fixture design.

### Extract

- Build configurations by cross-referencing probe boundary, parser boundary, approval artifact, agent-copy source/synchronization model, editorial allocation, and calibration/holdout partition strategy.
- Trace actual data and authority flow from raw occurrence through normalized candidate, live observation, product-fit decision, exact approval, atomic apply, and final disposition.
- Identify which combinations preserve existing identity/update/archive invariants and which introduce a second source of truth, incomplete copies, unverifiable approvals, or unaccounted occurrences.
- Derive minimal stable schemas for occurrence accounting, per-candidate evidence, approval binding, and resumable partial failure without writing an implementation specification.

### Challenge

- Attack surviving configurations with duplicate URL forms, requested/canonical mismatches, aliases, live/archive collisions, wrong type, private/dead/ambiguous previews, rate limits, mixed valid/malformed files, and idempotent reruns.
- Test command-copy drift, format-specific front matter, literal discovery, standalone readability, and behavior parity under independent Claude and Codex loading.
- Seek counter-evidence to a clean 28-candidate split: prior discovery notes, source ordering, recognizable hard cases, adaptive rules, and editorial outcome leakage.
- Determine whether any result contradicts a frozen claim and therefore needs an amendment proposal; prefer free-section refinements or downstream specification detail when the approved contract already admits the finding.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H2 | The existing Telegram classifier can expose an arbitrary non-mutating candidate probe with a stable summary while preserving every current identity/type/update/archive safety property. | needs-research — owner does not know |
| H3 | One `/kz-add <source>` grammar can unambiguously cover a single URL, multiple URLs, and Markdown/text files while remaining idempotent and accounting for every malformed/duplicate input. | needs-research — owner does not know |
| H4 | The 28-candidate universe can be partitioned into calibration and holdout sets so automated evidence narrows owner work without pretending that theme, Kazakhstan relevance, or commerciality are purely machine facts. | needs-research — owner does not know |
| A1 constraint | Every Claude/Codex `kz-*` command must be a complete self-contained synchronized copy; thin runtime links are prohibited. | approved and frozen — feasibility and synchronization design still require evidence |

## Scope Intent

- **In scope:** H2–H4; the approved A1 full-copy constraint; current classifier seams and invariants; one/many/file occurrence grammar; duplicate and malformed-input accounting; non-mutating evidence; exact approval binding; editorial versus observable gates; honest calibration/holdout design; comparable local projects and official primary technical sources; candidate-source shape as read-only research input.
- **Out of scope:** Editing HL/TS/status/journal/code/adapters/data/generated projections; deciding or hardcoding final dispositions for the 28 candidates; live catalog mutation; release/tag/push; Search Console or other external writes; adopting the unrelated dirty candidate files into a commit.

## Guiding Questions

1. What is the smallest boundary that lets an arbitrary candidate reuse the reviewed identity/type classifier without inheriting catalog-only lookup or any update/archive mutation path?
2. What input, evidence, and approval representations guarantee one explicit outcome per source occurrence and bind any later apply step to the exact reviewed candidate set?
3. Which full-copy synchronization and calibration/holdout configuration is independently testable in both agents without circular evidence or automated editorial overclaiming?

## User Direction

- The owner approved `deep` research and delegated stage-to-stage coordination, subject to canonical TFW WAIT gates.
- The owner does not know the answers to H2–H4 and asked research to decide from project value and purpose.
- The owner requires one `/kz-add <source>` command, a non-mutating preview followed by approval of an exact add set, and complete handling of the combined candidate corpus at the end.
- Some real candidates may calibrate the workflow; a disjoint set must remain for a clean final run.
- Every candidate must receive normal duplicate, topic, liveness, identity, and project-fit validation. “Add all” means complete accounting and adding all qualified approved entries, not bypassing eligibility.
- Amendment A1 is binding: Claude and Codex receive complete self-contained copies for all `kz-*` commands, with reproducible synchronization and parity checks and no thin runtime links.
- No push is authorized.

---
Stage complete: YES

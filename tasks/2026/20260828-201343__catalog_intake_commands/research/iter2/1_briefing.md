# Briefing — "What should we investigate?"
> **Mindset:** Strategist. Iteration 1 proved feasibility and eliminated incoherent families; Iteration 2 must close the exact choices that would otherwise leak into TS as assumptions.
> **Test:** The investigation must change the eventual specification if a URL form cannot be loss-accounted, an approval cannot be replay-safe, command parity cannot be reproduced in fresh runtimes, or holdout allocation requires exposing its raw inputs.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Predecessor Decisions to Build On

| # | Iteration 1 decision retained |
|---|---|
| D1 | Reuse the reviewed conflict-safe classifier; source parsing must not become a second identity classifier. |
| D2 | Account at occurrence level before grouping 29 occurrences into 28 unique candidates. |
| D3 | Classify Telegram link kind before normalization; unsupported/non-peer forms still receive explicit outcomes. |
| D4 | Requested/canonical identity binds before type, name, count, or any downstream fact is exposed. |
| D5 | Approval is an immutable preview payload plus an owner authority envelope and apply-time baseline/gate recheck. |
| D6 | Claude/Codex runtime bodies can be byte-identical; reproducible copy, standalone completeness, inventory, and runtime behavior are separate gates. |
| D7 | Mechanical observation, evidence-supported editorial analysis, and owner admission authority remain distinct. |
| D8 | Holdout allocation precedes implementation; any holdout-influenced rule, fixture, smoke, or expectation invalidates the clean run. |
| D9 | C2 is the smallest balanced family and C3 the conservative authority-heavy family; C1/C4/C5/C14 remain explicit trade-off alternatives. |

## Open Threads from Iteration 1

1. Exact public-peer grammar and explicit disposition taxonomy for message, invite, phone, reserved action, query, punctuation, multi-link, and malformed forms.
2. Minimal canonical preview payload, separate approval envelope, digest boundary, current catalog baseline, freshness, retry lineage, and apply-time invalidation.
3. Complete-copy source direction and fresh Claude/Codex evidence for literal discovery, argument receipt, preview/no-mutation, stats triage, and release hard stops.
4. A sealed calibration/holdout allocation and access protocol that does not run the intake parser or adapter smoke against raw holdout inputs before the clean run.
5. Concrete proof-cost comparison of C2 orchestration, C3 separate approval, and C4 shared observation module.
6. Durable adoption/provenance for the untracked 23-candidate discovery batch without overwriting parallel work or promoting preliminary notes to facts.

## Research Plan

### Gather

- Derive an explicit candidate/non-candidate Telegram URL taxonomy from official link specifications and the existing `handle_from_url`/classifier responsibilities; use synthetic examples only, never raw holdout occurrences.
- Compare canonical JSON/envelope patterns for stable hashing, content selection, anti-replay, baseline/freshness, retry lineage, and exact owner authorization; identify the smallest fields that make resumption and apply independently checkable.
- Inspect the current complete Claude command bodies, Codex skill loader contract, available local Claude/Codex CLIs, and safe fresh-session invocation surfaces; compare project-source, Claude-source, and Codex-source copy directions without modifying commands.
- Define a raw-input sealing/allocation protocol from already-recorded counts, hashes, and overlap facts only; do not enumerate, parse, or probe holdout candidates.
- Map file/dependency/test boundaries for C2, C3, and C4 and snapshot the untracked batch's known provenance metadata without adopting or reading its candidate body.

### Extract

- Cross the accepted URL taxonomy, occurrence schema, payload/envelope representation, source-copy direction, runtime proof mode, observation boundary, and holdout/provenance protocol into a small configuration space.
- Trace representative synthetic flows: multi-link text, unsupported Telegram action, identity/type conflict, partial live failure, stale approval, copy drift, fresh runtime routing, and holdout access denial.
- Compare C2/C3/C4 on modified surfaces, regression obligations, evidence strength, owner workload, and failure containment rather than architectural preference.
- Produce exact research-level contracts and invariants suitable for Coordinator selection while avoiding file budgets, AC wording, or implementation prescriptions that belong in TS.

### Challenge

- Attack grammar with documented Telegram aliases, reserved paths, public message suffixes, invite/phone ambiguity, query actions, Markdown punctuation, duplicates, and multiple occurrences per line.
- Attack evidence/approval with canonicalization mismatch, self-reference, omitted significant fields, stale catalog/category/locale data, replay, retry replacement, partial apply, and “same visible table, different bytes.”
- Attack A1 with identical thin bodies, incomplete command inventory, front-matter/name mismatch, missing literal route, dropped arguments, fresh-session context loss, and unsafe stats/release side effects.
- Attack holdout/provenance with pre-allocation parsing, candidate-aware strata, raw-file access during smoke, overlap leakage, preliminary-note promotion, changed untracked bytes, and post-run rule tuning.
- Determine whether C2/C3/C4 evidence selects a sufficient family, whether a third iteration is justified, and whether any finding truly requires a frozen amendment rather than a free refinement or TS detail.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | Iteration 2 test |
|---|-----------|-----------|------------------|
| H1 | Literal cross-agent `kz-*` behavior without copied bodies | refuted; superseded by A1 | Not reopened. Test only the approved complete-copy architecture. |
| H2 | Existing classifier can expose arbitrary non-mutating candidate evidence while preserving identity/type/update/archive safety | supported with conditions | Determine whether C2 orchestration is sufficient or C4 extraction materially reduces proof/risk. |
| H3 | One `/kz-add <source>` grammar can cover one/many/file with idempotent, complete malformed/duplicate accounting | supported with conditions | Close the accepted URL taxonomy, occurrence dispositions, payload identity, retry, and stale-approval semantics. |
| H4 | Current 28 can support calibration/holdout without automated editorial overclaim | supported procedurally | Close an allocation/access/invalidation protocol without inspecting raw holdout candidates or encoding expected outcomes. |
| A1 constraint | Every Claude/Codex `kz-*` command is a complete synchronized runtime copy, never a thin link | approved and frozen; feasibility supported | Select a reproducible source direction and obtain safe fresh-runtime discovery/argument/hard-stop evidence where available. |

## Iteration 2 Working Hypotheses

| # | Hypothesis |
|---|-----------|
| I2-H1 | A bounded documented public-peer grammar can normalize useful URL forms while every other Telegram-like occurrence receives a stable explicit disposition, without changing classifier identity semantics. |
| I2-H2 | A canonical preview payload plus a physically separate approval envelope can bind every significant proposed fact, owner authority, current baseline, and retry lineage without self-reference or replay ambiguity. |
| I2-H3 | One existing runtime copy can be the authoring source for byte-identical complete copies, and safe fresh sessions can separately prove discovery, literal routing, arguments, and hard stops for all three commands. |
| I2-H4 | A sealed allocation can be created from already-recorded provenance/count/overlap metadata without loading holdout raw occurrences into implementation, fixtures, smokes, or expected outcomes. |
| I2-H5 | C2 orchestration can preserve the reviewed classifier and mutation boundaries with less proof surface than C4; C3's separate approval artifact may be adopted as an authority feature without requiring a separate architecture family. |

## Scope Intent

- **In scope:** Official Telegram public-peer/deep-link grammar; synthetic occurrence cases; stable occurrence/candidate dispositions; canonical payload and separate approval envelope; catalog baseline/freshness/retry/replay semantics; complete-copy source direction for all three `kz-*` commands; read-only fresh Claude/Codex discovery/argument/hard-stop probes; C2/C3/C4 boundary comparison; sealed allocation protocol; already-recorded source hashes/counts/overlap; untracked-batch provenance/adoption rules.
- **Out of scope:** Reading or enumerating raw holdout candidates; using holdout URLs in parser fixtures or command smokes; live candidate probing; candidate/editorial dispositions; editing HL/TS/status/iterations/journal/code/data/commands/adapters; adopting or staging `tasks/CANDIDATES-2026-08-28.md`; changing unrelated dirty work; tag, release, push, or any external mutation.

## Guiding Questions

1. What exact grammar and versioned payload/envelope contract makes every source occurrence, candidate fact, approval, retry, and apply transition independently checkable without broadening the reviewed classifier?
2. Which complete-copy source direction and safe fresh-runtime evidence proves all three literal commands in Claude and Codex with the fewest unverified assumptions?
3. What sealed allocation/provenance and observation-boundary configuration preserves an honest holdout while remaining small enough for a bounded TS?

## User Direction

- The Coordinator explicitly authorized Iteration 2 in `deep` mode and assigned the six open-thread areas above.
- The Researcher must not inspect raw holdout candidates; only sealing/allocation protocol design and already-recorded aggregate provenance are permitted.
- Every canonical WAIT remains mandatory; Iteration 2 stage files and RES are the only writable surfaces.
- No external mutation, production candidate probe, catalog change, command edit, push, tag, or release is authorized.

---
Stage complete: YES

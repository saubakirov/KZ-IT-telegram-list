# RES — 20260828-201343__catalog_intake_commands: Safe intake, exact command copies, and honest validation

> **Date**: 2026-08-28
> **Author**: saubakirov
> **Status**: 🔬 RES — Iteration 1 complete; further research recommended
> **Parent HL**: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> **Mode**: Pipeline · deep

---

## Research Context

Iteration 1 tested whether the approved `/kz-add <source>` vision is technically coherent before a TS commits to an unsafe parser, a second Telegram classifier, an unverifiable approval prompt, drifting Claude/Codex adapters, or a contaminated holdout. Research inspected the current classifier and catalog contracts, the 29 supplied source occurrences representing 28 unique handles, existing `kz-*` operations, local adapter precedents, and primary documentation for both agent loaders, Telegram links, canonical evidence, evaluation leakage, and transaction authorization. The result is a bounded set of feasible architecture families and a smaller set of exact questions for the mandatory next iteration.

## Briefing

The approved scope, hypotheses, and stage plan are in [1_briefing.md](1_briefing.md). Raw dimensional findings, configuration analysis, and attacks are retained separately in [2_gather.md](2_gather.md), [3_extract.md](3_extract.md), and [4_challenge.md](4_challenge.md).

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Keep source parsing outside the reviewed target-identity semantics; reuse the existing conflict-safe classifier rather than implement a second classifier. | The existing pure classification/retry functions already separate observation from catalog update/archive. The prior identity-decoy regression makes shared behavior materially safer than output-equivalent reimplementation. C11 was eliminated. |
| D2 | Account first at occurrence level, then group into unique candidates. | The real corpus is 29 occurrences but 28 handles because `aws_kz` appears twice. Unique-only and line-only schemas silently lose malformed, duplicate, or multi-link occurrences. |
| D3 | Classify Telegram link kind before handle normalization; only stable public-peer forms can become candidates, while every unsupported/reserved/private/message form still receives an explicit occurrence disposition. | Telegram officially assigns overlapping-looking `t.me` syntax to usernames, messages, private invites, phone numbers, bots, share actions, and reserved services. First-path extraction can turn non-candidates into handles. |
| D4 | Bind requested/canonical identity before exposing observed type, name, or member count. | A foreign canonical target can otherwise contribute plausible type/count facts. Declared type, observed type, and unresolved type remain separate fields; no type interpretation may override an identity conflict. |
| D5 | Model authorization as an immutable preview payload plus an owner authority envelope, followed by a final apply-time baseline and eligibility recheck. | A digest binds bytes but not authority; embedding approval in its own hash is circular; conversational “yes” and boolean flags do not bind exact proposed rows. The payload/envelope model also invalidates stale or modified approvals instead of replaying them. |
| D6 | Use complete byte-identical command bodies at the frozen Claude and Codex runtime paths, with a reproducible one-way copy/check mechanism and separate completeness/runtime evidence. | Claude command files accept the common front matter and ignore `name`; Codex requires `name` and `description`. Thus one full document can occupy both paths unchanged. Hash parity alone is insufficient because identical thin or incomplete bodies would still fail A1. |
| D7 | Separate mechanical facts, evidence-supported editorial analysis, and owner admission authority. | Syntax, target binding, observed type/liveness, exact collision, category membership, and locale presence can be mechanical. Alias continuity, IT/Kazakhstan relevance, commerciality, category/copy correctness, and positive inclusion remain evidence-backed human judgments. |
| D8 | Seal the calibration/holdout allocation before implementation; prohibit holdout raw inputs, outcomes, types, or known cases from tuning parser rules, fixtures, adapter smokes, or expected results. | Leakage can happen before a network request. Any holdout-driven rule/fixture change invalidates the “clean” run and starts a new evidence cycle. The current holdout is procedural no-tuning evidence, not a claim that identities were globally unknown. |
| D9 | Carry C2 as the smallest balanced family and C3 as the conservative authority-heavy family; retain C1/C4/C5/C14 only as explicit trade-off alternatives. | Pairwise Challenge eliminated C6–C13. C2 composes the reviewed classifier, occurrence ledger, exact-copy commands, mixed structural/editorial gates, and stratified holdout. C3 safely permits unresolved type and a physically separate approval artifact at higher review cost. |

## Surviving Family Comparison

| Family | Configurations | What it preserves | Main cost/risk | Iteration 1 disposition |
|---|---|---|---|---|
| Orchestrated exact-copy intake | C2 | Existing classifier behavior; occurrence-first parser; exact byte copies; structural negative gates plus owner fit; sealed stratified holdout | Must define one canonical source direction and prove literal Codex routing separately from file parity | Strongest balance; carry as the primary comparison family |
| Conservative approval/review | C3 | Same reuse/accounting; unresolved type stays explicit; physical approval artifact; independent advisory review | More artifacts and owner/reviewer work; risk of payload/approval drift if cross-check is weak | Strongest authority boundary; carry as a fallback/variant |
| In-place candidate mode | C1 | Small code-location change; existing retry/classifier; exact approval | Highest risk of mixing candidate observation with current `--update`/archive/catalog-only enrichment paths; type requires explicit curator input | Viable only with strict mutually exclusive non-mutating mode |
| Shared observation module | C4/C5 | Clean reusable observation API and explicit type strategies | Larger refactor; must reproduce every historical identity/update/archive regression; C5 adds reconciliation complexity | Viable if Iteration 2 evidence justifies refactor cost |
| Source-isolated evaluation | C14 | Simple partition provenance and separate approval | Weaker isolation because prior notes exist; known overlap must be assigned once; source split may be unbalanced | Evaluation alternative only, never a global-unseen claim |

The eliminated families fail a frozen property rather than a stylistic preference: C6 lacks a reproducible source/copy relationship; C7/C9 lose occurrences; C8 rejects the known overlap instead of accounting for it; C10 lacks a current-28 holdout; C11 duplicates the classifier; C12/C13 cannot bind exact owner authority to immutable proposal bytes.

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | What exact public-peer URL forms are accepted, normalized, or explicitly unsupported, especially public message links, `tg://resolve`, `<username>.t.me`, query actions, and punctuation? | Open — Iteration 2 | Iteration 1 proved that kind classification must precede normalization but intentionally did not freeze the accepted grammar. |
| Q2 | Which source direction gives the smallest complete-copy contract: a third project-owned source, Claude-as-source, or Codex-as-source? | Open — Iteration 2 | Exact-byte runtime copies are feasible in all three one-way arrangements; the choice needs drift, contributor ergonomics, and current-file preservation comparison. |
| Q3 | What is the smallest versioned payload/envelope schema and named canonicalization contract that binds occurrence ledger, candidate evidence, exact proposed rows, owner IDs, and current catalog baseline without self-reference? | Open — Iteration 2 | ED1/CD4 establish the two layers; field set, digest boundary, freshness rule, and canonical JSON profile remain to be fixed. |
| Q4 | Can literal `/kz-add`, `/kz-stats`, and `/kz-release` be proven in fresh Claude and Codex sessions with complete argument/hard-stop parity and zero production mutation? | Open — Iteration 2 | Official loader contracts make the files feasible; empirical loader/routing evidence has not yet been collected. |
| Q5 | Which exact candidates/occurrences form calibration and holdout, and how is the allocation sealed without using the intake parser or encoding expected outcomes? | Open — Iteration 2 | A pre-implementation manual/research inventory is required; candidate IDs, sizes, strata, overlap assignment, and access discipline remain open. |
| Q6 | Does classifier reuse need only a separate orchestrator (C2/C3), or does a shared observation module (C4/C5) materially reduce proof cost enough to justify refactoring? | Open — Iteration 2 | Both families survived; no implementation experiment or dependency/scope comparison has selected the boundary. |
| Q7 | How is the untracked discovery batch adopted as Phase B input without overwriting unrelated work or treating preliminary notes as verified facts? | Open — coordinator/Iteration 2 | Its content/hash is known and untouched; durable provenance and adoption authority still need an explicit plan. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Claude/Codex can share literal `kz-*` behavior without copied bodies | refuted/superseded by A1 | Not retested; remains superseded | Owner-approved A1 requires complete copies, so thin routing is outside the solution space. |
| H2 | Existing classifier can expose arbitrary non-mutating candidate evidence while preserving safety | needs-research | 🟢 Supported with conditions; implementation proof pending | Pure `classify_response`/retry seams already exist; selection/enrichment/mutation are separable. C1–C5 survive only with identity-first facts, non-mutating separation, and the full historical regression matrix. |
| H3 | One source grammar can cover one/many/file with idempotent complete accounting | needs-research | 🟢 Supported with conditions; exact grammar pending | Occurrence-first parsing followed by candidate grouping handles 29→28, malformed/reserved links, retry, and exact payload approval. Generic `@file`, line-only, and unique-only variants failed. |
| H4 | Current 28 can support calibration/holdout without automated editorial overclaim | needs-research | 🟢 Supported procedurally; allocation pending | A sealed pre-implementation no-tuning split is defensible even though preliminary notes exist. Mechanical/editorial/owner authority is separable. Parser/smoke leakage invalidates the clean-run claim. |
| A1 | Complete self-contained synchronized Claude/Codex copies are feasible at frozen paths | approved constraint | 🟢 Feasible; runtime proof pending | Common `name` + `description` front matter permits byte-identical complete bodies at `.claude/commands/*.md` and `.agents/skills/*/SKILL.md`; inventory/completeness/discovery/behavior need separate gates. |

## HL Update Recommendations

> The researcher classifies and does not apply. These are free-section refinements only; no frozen declarative claim needs amendment.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current Reality | Record the existing reusable classifier/retry seam, its catalog-only CLI selection, its typed precondition, and the historical identity-decoy reason to prohibit a second classifier. | Gather G1; Challenge C2 |
| R2 | §7.2 Constraints & Inputs | Refine “Telegram link” into an occurrence-accounted public-peer grammar: accepted public-peer forms may normalize; invite/phone/reserved/message forms must be explicitly supported or disposed, never silently first-path parsed. | Challenge C1; Telegram deep-link primary source |
| R3 | §7.2 Constraints & Inputs | State the two-layer evidence contract: immutable canonical preview payload, owner approval envelope referencing its digest/exact IDs, current catalog baseline, and apply-time invalidation on any significant change. | Extract E3; Challenge C4 |
| R4 | §8 Dependencies | Record exact-byte full-copy feasibility at the existing frozen paths and make fresh Claude/Codex literal-routing/argument/hard-stop evidence an unresolved dependency distinct from copy parity. | Extract E4; Challenge C5 |
| R5 | §9 Risks | Add reserved/private/message-link misclassification, approval replay/TOCTOU, identical-but-incomplete adapter copies, and holdout leakage through parser/smoke inputs before network access. | Challenge C1, C4, C5, C7 |
| R6 | §10 Research Case | Mark H2/H3/H4 “supported with conditions” and replace broad blind spots with Q1–Q7 and the C2/C3 primary survivor comparison. | This RES Hypotheses, Open Questions, Surviving Family Comparison |
| R7 | §11 Strategic Insights | Clarify S4: “unseen” means sealed no-tuning before the clean run, not unknown identities; any holdout-driven rule/fixture change invalidates that evidence cycle. | Gather GD3; Challenge CD5; user direction captured in HL §11 S4 |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** Official loader compatibility, explicit non-candidate link dispositions, procedural holdout isolation, and payload/envelope approval all refine the approved contract without changing §§1 or 3–7.

## Fact Candidates

**No Fact Candidates.** The owner-supplied directions relevant to this research are already captured in HL §11 and amendment A1. Iteration 1 introduced no new human-only factual report; all other observations are agent-discoverable from code, files, or external primary sources.

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | philosophy | The durable product is one small human operation, not a proliferation of commands for source cardinality. **Implication:** one parser/evidence model must absorb one/many/file variation while preserving explicit outcomes. | User, planning direction captured in HL §11 S1–S2 | ★★★ |
| SS2 | philosophy | Catalog accuracy outranks coverage; “add all” means process all candidates and add every qualified approved row, not waive gates. **Implication:** unresolved/rejected/duplicate are successful accounted outcomes, not workflow failure or omitted work. | User, planning direction captured in HL §11 S5 | ★★★ |
| SS3 | constraint | Every Claude/Codex command must be a complete runtime copy, even though thin adapters normally reduce drift. **Implication:** synchronization assurance must combine reproducible copying with standalone completeness and fresh-runtime behavior, not rely on hashes alone. | User correction, approved HL amendment A1 / §11 S6 | ★★★ |
| SS4 | process | Real candidates must calibrate the workflow while a disjoint subset remains for a clean final run. **Implication:** allocation and access discipline are part of the evidence design, and an exposed/tuning-influenced holdout must be invalidated rather than rationalized. | User, planning direction captured in HL §11 S4 | ★★★ |

## Findings Map

```text
RAW INPUT                                         CROSS-CUTTING ASSURANCE
  │                                               ┌──────────────────────────┐
  ├─ classify Telegram link kind                  │ complete kz-add/stats/   │
  │    ├─ stable public peer ───────────────┐      │ release bodies           │
  │    └─ malformed/private/reserved/etc.   │      │ exact source→copy check │
  │          └─ explicit occurrence outcome │      │ fresh Claude/Codex smoke│
  │                                         │      └──────────────────────────┘
  ├─ occurrence ledger [29]                 │
  │    └─ normalize/group candidate [28] ◄──┘      ┌──────────────────────────┐
  │         ├─ live/archive/overlap collision      │ allocation sealed before│
  │         └─ target-bound fetch/classifier       │ implementation           │
  │              ├─ identity conflict → unresolved│ calibration only opens   │
  │              └─ bound identity                │ calibration inputs       │
  │                   ├─ observed type/facts       │ holdout opens once after │
  │                   └─ editorial evidence        │ Phase A review           │
  │                        └─ owner judgment        └──────────────────────────┘
  │
  ├─ immutable preview payload + digest
  ├─ owner envelope: exact IDs/rows + authority
  ├─ current baseline/freshness/gate recheck
  └─ apply source once → validate → regenerate → final dispositions

Root failure modes avoided:
  first-path parsing · foreign-target facts · unique-only loss · approval replay
  identical thin copies · automated editorial overclaim · pre-network holdout leakage
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H2 (supported with conditions), H3 (supported with conditions), H4 (supported procedurally), A1 feasibility (supported)
- **Hypotheses deferred:** None; empirical implementation/runtime proof remains an open thread rather than an untested hypothesis.
- **Gaps discovered:** exact accepted public-peer grammar; canonical payload/envelope schema; command source direction; fresh Claude/Codex literal-routing evidence; sealed candidate allocation; orchestrator-versus-shared-module proof cost; durable adoption/provenance of the untracked batch.
- **Superseded decisions:** CD1 eliminates Extract configurations C6–C13 after pairwise attack; CD4 strengthens ED1 from an alternative representation into a condition of every survivor. No owner decision is superseded.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Accepted URL grammar and disposition taxonomy | A wrong parser can probe invite hashes/reserved services or silently strip message context. | Define candidate/non-candidate forms from official Telegram syntax and derive a synthetic occurrence matrix, including punctuation and multi-link lines. |
| 2 | Evidence payload, approval envelope, and freshness | Exact approval is the only catalog mutation authority; ambiguity or self-reference creates replay/TOCTOU risk. | Compare a named repository canonical JSON profile versus JCS, define digest boundaries/IDs/baseline/freshness, and walk stale/retry/apply examples. |
| 3 | Full-copy source direction and empirical parity | Exact bytes are feasible, but the source-of-truth direction and literal runtime behavior are not proven. | Compare D6 A/B/C against existing file history; design or run safe fresh-session Claude/Codex discovery, arguments, preview/no-mutation, stats, and release-stop probes. |
| 4 | Sealed calibration/holdout allocation | Any allocation after parser/fixture work weakens Phase B evidence and violates the configured minimum research depth. | Predeclare candidate/occurrence inventory, overlap ownership, neutral strata, access rules, invalidation rule, and candidate counts without expected outcomes. |
| 5 | C2 versus C3/C4 boundary | The TS needs one implementable boundary; too small risks coupling, too large raises regression/scope cost. | Compare concrete dependency/file/safety surfaces for orchestrator, separate approval artifact, and shared observation module against historical tests. |
| 6 | Candidate-batch provenance | The 23-candidate file is unrelated untracked work and cannot be silently adopted or overwritten. | Define read-only snapshot/adoption evidence and how Phase B references preliminary notes without promoting them to facts. |

### Recommendation

- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — run Iteration 2 because `min_iterations: 2` is mandatory and Q1–Q7 still affect exact grammar, authorization, adapter source/parity, holdout validity, and implementation boundary.
- [ ] **BLOCKED** — no external blocker; the next iteration can proceed from this trace.

> Coordinator decides whether to continue or proceed. Researcher recommends but does not decide.

## Conclusion

Iteration 1 establishes that H2–H4 and A1 are feasible without a frozen amendment, but only under stricter boundaries than the initial wording makes visible: occurrence accounting precedes dedupe, public-peer kind classification precedes normalization, identity precedes type/facts, approval is an immutable payload plus authority envelope and final recheck, complete exact copies require more than hash equality, and holdout leakage can occur before any live probe. C2 and C3 now give the next iteration concrete architecture families rather than an open-ended search. The main self-critique is deliberate: this iteration did not launch clean Claude/Codex runtime probes, freeze the exact URL grammar/schema, or allocate the real holdout, because doing those prematurely would either exceed the Researcher role or contaminate the evidence it is meant to design. Iteration 2 should close those exact gaps, after which `/tfw-plan` can translate the result into TS.

---

*RES — 20260828-201343__catalog_intake_commands: Safe intake, exact command copies, and honest validation | 2026-08-28*

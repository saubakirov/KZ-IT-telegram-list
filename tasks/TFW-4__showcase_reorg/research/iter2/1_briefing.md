# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Establish an honest, repeatable evidence boundary for Telegram liveness so the catalog can publish dated verification without inferring identity, life, death, or member counts.

## Predecessor Context

Iteration 1 decisions carried forward:

- **D1:** count compatibility and liveness classification are separate questions; public group/channel counts still parse, but marker-free HTTP 200 pages can be false positives.
- **D2:** target-specific preview, count availability, and liveness are separate signals.
- **D3:** H2 remains inconclusive; C4 alone supports neither an alive nor a dead/private verdict.
- **D5:** classifier correction belongs in Phase C, but the proposed §5 gate requires an owner verdict.
- **D6:** iteration 2 must resolve C4 identity evidence and frozen DoD 22 achievability before Phase D.

Open threads carried from iteration 1:

1. Distinguish a legitimate private/contact-only handle from an absent handle when both present as C4.
2. Define what evidence may refresh `last_verified` and what evidence may start archive triage.
3. Determine whether frozen DoD 22 is achievable for `mobile_developers_kz` without treating proposed A5 as approved.

## Research Plan

### Gather

- Inspect the current liveness implementation and iteration 1 response taxonomy to state exactly what C4 lacks.
- Use a bounded set of read-only external signals for `mobile_developers_kz` plus explicit positive/private-or-contact and absent controls; do not repeat the eight-handle sample.
- Separate signals that prove target identity from signals that prove only route syntax, historical existence, or Telegram ownership of the page.
- Use a comparison matrix because the problem has two coupled decisions rather than three independent dimensions: identity evidence and verification/archive consequence.

### Extract

- Compare the observed signal combinations and assign the strongest claim each combination supports.
- Formalize two evidence rules: one for setting `last_verified`, one for admitting an entry to owner-evidenced archive triage.
- Evaluate `mobile_developers_kz` against those rules and frozen DoD 22 exactly as written.
- Identify whether the result is a free-section refinement or evidence for a new frozen-section amendment proposal; do not apply or endorse A5.

### Challenge

- Attack false-positive cases: renamed targets, search-engine residue, Telegram contact shells, generic landing pages, and unrelated invite references.
- Attack false-negative cases: legitimate private groups, client-only resolution, transient access failure, and missing numeric counts.
- Check whether any proposed rule can both date `mobile_developers_kz` honestly and avoid turning ambiguity into death.
- Return `SUFFICIENT` only if the Coordinator has enough evidence to specify Phase C and to route any contract conflict to the owner.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | `t.me/{handle}` still exposes compatible public counts, while genuinely absent/private targets need a safe classification beyond the current negative-marker test. | partial — count markup confirmed; C4 identity unresolved |
| H2 | At least one current catalog handle is dead or private, allowing Phase D to exercise archive triage with real data. | inconclusive — iteration 1 found one ambiguous C4 catalog response, not a death |

## Scope Intent

- **In scope:** Bounded, read-only identity signals for C4; explicit evidence semantics for `last_verified`; admission criteria for owner-evidenced archive triage; frozen DoD 22 achievability for `mobile_developers_kz`; recommendation classification.
- **Out of scope:** The 63-entry sweep; repeating iteration 1 public-count, eight-handle, rate-limit, or GitHub-anchor probes; data/code/HL/control-file changes; applying A5; archive decisions; push, tag, or release work.

## Guiding Questions

1. Which bounded signal, if any, positively binds `mobile_developers_kz` to a current Telegram target rather than merely showing that the URL shape exists?
2. What minimum evidence permits `last_verified` to change, and what distinct evidence permits owner archive triage to begin?
3. Under that rule, can every currently live entry satisfy frozen DoD 22, specifically `mobile_developers_kz`, without an owner-approved amendment?

## User Direction

The delegated owner direction fixes iteration 2's focus, forbids a full 63-entry sweep, requires preservation of Coordinator edits, and states that A5 remains unapproved. Only an explicit owner verdict can change frozen §5. No additional user question is required before the bounded read-only investigation.

---
Stage complete: YES

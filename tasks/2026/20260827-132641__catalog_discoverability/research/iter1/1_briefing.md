# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> Goal: Make one verified Kazakhstan IT Telegram catalog easy to discover, understand, and use in English, Russian, and Kazakh without creating drifting catalogs or weakening accuracy.

## Research Plan

### Gather

- Inspect the live GitHub Pages and GitHub README renders, repository metadata, source data, schema validator, generator, and publication constraints; decompose the decision into language routing, page identity/metadata, intent taxonomy, and maintenance cost dimensions.
- Compare official GitHub Pages/Jekyll, GitHub repository-discovery, Google Search, Schema.org, and relevant AI-crawler/retrieval guidance, explicitly separating controllable indexability signals from ranking or model-inclusion claims.
- Sample a small set of strong, actively maintained catalogs whose multilingual routing, intent navigation, static-site architecture, or machine-readable access is relevant at this repository's scale.
- Measure the present catalog's cross-type category coverage and identify what can be derived from existing facts versus what would require new reviewed classifications.

### Extract

- Build a configuration space across language-route shape, GitHub/Pages source layout, metadata strategy, intent model, and machine-readable surface.
- Trace each candidate to the current one-source generator contract and identify the minimum structured fields, validation invariants, and public routes a later TS would need.
- Distinguish supported search/discovery mechanisms from optional or weakly evidenced additions such as `llms.txt`, query-variant prose, or agent-only files.
- Extract cross-render and multilingual failure modes, including heading identity, URL/canonical/hreflang behavior, Markdown portability, fallbacks, and translation ownership.

### Challenge

- Pairwise-test candidate configurations against the frozen DoD/DoF, GitHub Pages limitations, GitHub README portability, mobile first-screen constraints, and repository maintenance cost.
- Seek counter-evidence for H2, H3, and H4, including cases where metadata is ignored, facets misclassify entries, or Jekyll routing adds more surface than value.
- Test whether the smallest surviving configuration still gives each language one-action access and exposes groups, channels, bots, and high-value intents without duplicating catalog facts.
- Convert unresolved external behavior—search recrawl, ranking, AI citation, and unsupported crawler conventions—into bounded evidence expectations rather than implementation promises.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Separate generated language entry points linked above the fold produce a smaller and clearer experience than one trilingual README while preserving one catalog. | Confirmed in principle; exact routes and generator design remain open and are supporting research for this iteration. |
| H2 | Clear first-screen structure, accurate repository/site metadata, stable facts, and crawlable source data create more defensible search/AI discoverability than `llms.txt`, keyword blocks, or agent-only prose. | Needs research; primary Iteration 1 hypothesis. |
| H3 | A small derived intent model can expose AI, startups, jobs, events, and engineering across groups/channels/bots without duplicate entries or scope expansion. | Needs research; primary Iteration 1 hypothesis. |
| H4 | Lightweight GitHub Pages configuration can create one coherent page identity and multilingual metadata while keeping GitHub's README experience intact. | Needs research; primary Iteration 1 hypothesis. |

## Scope Intent

- **In scope:** EN/RU/KZ route alternatives; current data/generator constraints; cross-type intent navigation; GitHub README and GitHub Pages behavior; official repository, search, structured-data, and AI-discovery guidance; comparable static catalogs; controllable verification signals; recommendations precise enough to support a later TS.
- **Out of scope:** Code or generated-output changes; edits to HL, TS, task state, or iteration control; repository settings changes; unreviewed translations; new community vetting; search-rank promises; building a client-side search application, portal, CMS, or agent-only shadow catalog.

## Guiding Questions

1. What is the smallest route and generator architecture that gives EN/RU/KZ one-action access on GitHub Pages while keeping the GitHub README coherent and one-source?
2. Which visible, machine-readable, repository, and site-level signals have documented consumers, and which proposed search/AI additions lack evidence proportional to their maintenance cost?
3. What minimal cross-type intent model can be derived or safely added without duplicating entries, widening scope, or misrepresenting bots and partially classified channels?

## User Direction

- 2026-08-27 — The owner instructed Iteration 1 to focus on multilingual routes, search/AI discoverability signals, cross-type intent navigation, and lightweight GitHub Pages integration; test H2–H4 and treat H1 as confirmed only in principle.
- 2026-08-27 — Coordinator approved **deep** mode because H2–H4 span live rendering, multilingual information architecture, official search/AI guidance, intent classification, and counter-evidence; focused mode would leave material blind spots.
- 2026-08-27 — Coordinator authorized continuation through the iteration checkpoints without further approval unless a genuinely owner-only decision emerges.

---
Stage complete: YES

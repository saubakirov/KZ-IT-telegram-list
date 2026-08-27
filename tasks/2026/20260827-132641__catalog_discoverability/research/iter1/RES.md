# RES — 20260827-132641__catalog_discoverability: Multilingual routes, intent navigation, and discoverability

> **Date**: 2026-08-27
> **Author**: Researcher (Codex)
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> **Mode**: Pipeline (deep)

---

## Research Context

Iteration 1 tested whether the frozen multilingual/discoverability outcome can be specified without a new website application or a second catalog. It inspected the live GitHub Pages DOM and mobile/desktop render, current data/schema/generator, public GitHub repository state, official Jekyll/GitHub/Google/OpenAI/IANA/RFC/Schema.org guidance, multilingual search snapshots, and five comparable catalogs. The investigation separated controllable page/indexability signals from non-guaranteed rank or AI inclusion. It made no code, generated-catalog, HL, TS, status, iteration-control, repository-setting, or journal change.

## Briefing

The approved deep-mode scope and rationale are recorded in [1_briefing.md](1_briefing.md). Gather mapped the live/repository/documentation evidence in [2_gather.md](2_gather.md); Extract formed the configuration space in [3_extract.md](3_extract.md); Challenge attacked the survivors in [4_challenge.md](4_challenge.md).

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Use English at `/`, Russian at `/ru/`, and Kazakh at `/kk/`; link all three from every public entry point. | This is the smallest one-action route set, preserves a useful root page, and aligns the Kazakh route with the registered `kk` language code. A neutral selector adds a fourth page without a distinct job. |
| D2 | Keep `README.md` as the GitHub projection and generate dedicated Pages `index.md`, `ru/index.md`, and `kk/index.md` projections. | GitHub Markdown portability and Jekyll front matter/layout metadata are different contracts. Dedicated generated indexes remove hidden README-as-index coupling while retaining one source. |
| D3 | Use one locale-aware renderer and make generator currency cover every generated projection. | This preserves the existing one-source contract and converts multilingual drift into an executable failure. Pages front matter remains generated output, not hand-maintained catalog state. |
| D4 | Keep the catalog type-first and add one compact cross-type intent map backed by reviewed intent definitions over category IDs plus exceptional live handles. | Existing AI/startups/jobs/events/engineering meaning overlaps categories. A central definition is explicit and lower-churn than mandatory facets on all 62 entries; keyword inference and category-only derivation are inaccurate. |
| D5 | Extend category validation to every type that carries a category and validate intent/category/handle/anchor references. | The intent projection is only trustworthy when its inputs and generated destinations cannot silently disappear. Human review still owns semantic membership. |
| D6 | Baseline reciprocal language alternates, self-canonicals, correct per-page language/title/description, sitemap, coherent social metadata, a public JSON link, and accurate `Dataset`/`DataDownload` markup. | Each has a documented human, crawler, dataset, or preview consumer. Their job is metadata/access eligibility, never guaranteed rank or citation. |
| D7 | Do not baseline `llms.txt`, a project-path `robots.txt`, keyword/query pages, or a client-side application. | Concise Markdown and canonical JSON are already public; no distinct unmet consumer job was found. Standard robots rules operate at the host root, and static content satisfies the current scale. |
| D8 | Test semantic DOM/link/route invariants in addition to syntax and structured-data validity. | The current live page produces no W3C HTML errors while still showing two primary identities and losing one Telegram anchor through Markdown pipe parsing. |
| D9 | Treat repository settings, Pages publishing settings, Search Console, recrawl, rank, and AI answer inclusion as explicit external evidence boundaries. | Public read-only evidence cannot authenticate owner settings, and implementation cannot control ranking or answer selection. Phase B can prove configuration/access and record timestamped retrieval snapshots only. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which exact Kazakh UI, category, purpose, non-goal, and entry-description wording is accurate and owner-approved? | Open — Iteration 2 | `kk` is the standards-valid language code, but routing evidence does not validate translations. The system must fail closed until qualified review supplies complete Kazakh wording. |
| Q2 | What exact categories and exceptional handles belong to AI, startups, jobs, events, and engineering? | Open — Iteration 2 | The representation is selected, but semantic completeness—especially engineering breadth, startup exceptions, and AI overlap—cannot be proven from keywords alone. |
| Q3 | What branch/folder currently publishes GitHub Pages, and can Phase B retain root-source publication? | Open — external setting verification | Public responses and the published JSON strongly imply root publication, but the unauthenticated Pages API did not establish the configured source. C1 remains viable; `docs/` is a fallback, not a recommendation. |
| Q4 | Which repository description, topics, homepage, and social-preview asset will the owner approve? | Open — Phase B owner gate | Current public settings are measurable, but changing external repository metadata is outside Researcher authority and exact copy/asset approval remains with the owner. |
| Q5 | Is Search Console access available for post-publication evidence? | Open — optional Phase B dependency | Absence of access limits indexing evidence but does not justify additional machine-facing files or block static publication. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Separate generated language entry points linked above the fold produce a smaller and clearer experience than one trilingual README while preserving one catalog. | confirmed in principle; routes/generator open | 🟢 CONFIRMED WITH RECOMMENDED DESIGN | Extract E1-E2 and Challenge C1-C2: `/`, `/ru/`, `/kk/` plus dedicated generated Pages indexes give one-action access without a selector, long trilingual flow, or hand-maintained copies. |
| H2 | Clear first-screen structure, accurate repository/site metadata, stable facts, and crawlable source data create more defensible search/AI discoverability than `llms.txt`, keyword blocks, or agent-only prose. | needs-research | 🟢 SUPPORTED WITH EXTERNAL-OUTCOME LIMIT | Gather G5-G8 and Challenge C5: official Google/OpenAI guidance supports ordinary technical clarity and crawler access; Dataset has a bounded discovery job; Google ignores `llms.txt` for visibility/rank; all rank/citation outcomes remain non-guaranteed. |
| H3 | A small derived intent model can expose AI, startups, jobs, events, and engineering across groups/channels/bots without duplicate entries or scope expansion. | needs-research | 🟠 CONDITIONALLY SUPPORTED | Gather G2, Extract E3, Challenge C3: a compact map over validated categories and reviewed exceptional handles can link to canonical entries across types. Exact membership and qualified human review remain unresolved. |
| H4 | Lightweight GitHub Pages configuration can create one coherent page identity and multilingual metadata while keeping GitHub's README experience intact. | needs-research | 🟢 TECHNICALLY CONFIRMED; SETTING UNVERIFIED | Gather G1/G3-G4, Extract E1-E2, Challenge C2: supported Jekyll pages/layout/SEO/sitemap facilities can implement the routes and metadata without a custom build. The authenticated source-folder setting remains external. |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** The frozen HL, task status, and Coordinator-owned `iterations.yaml` were not edited.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Add that all 62 live records have Russian descriptions, none has a Kazakh description, categories are required/validated only for groups, 18/20 channels carry unvalidated categories, and bots carry none. Record that the public JSON already returns `200 application/json`. | Gather G1-G2 |
| R2 | §7.2 Knowledge Citations | Add official citations for Jekyll front matter/permalinks, GitHub Pages supported dependencies, Google localized pages/generative guidance/Dataset/sitemaps, OpenAI crawler roles, IANA `kk`, RFC 9309 robots location, and Schema.org Dataset/DataDownload. | Gather G3-G6; Extract E1/E4; Challenge C2/C5 |
| R3 | §8 Dependencies | Mark native Jekyll route/layout/plugin capability verified; add authenticated Pages-source inspection, qualified Kazakh wording review, reviewed intent membership, external repository-setting approval, and optional Search Console access with their exact authority boundaries. | D1-D6, D9; Open Questions Q1-Q5 |
| R4 | §9 Risks | Add silent intent omission and generic-validator blindness. Mitigate with reviewed category-plus-handle definitions, validated references/anchors, representative special-character fixtures, and semantic DOM/link assertions. | Challenge C3-C4 |
| R5 | §10 H1 | Record confirmed design: English `/`, Russian `/ru/`, Kazakh `/kk/`; generated `README.md` plus dedicated generated Pages indexes from one locale-aware renderer. | D1-D3; Extract E1-E2; Challenge C1-C2 |
| R6 | §10 H2 | Set supported-with-limit: ordinary visible structure, accurate metadata, reciprocal routes, sitemap, public JSON, documented crawler access, and accurate Dataset linkage have defensible jobs; omit `llms.txt` from the baseline; no rank or AI-inclusion guarantee. | D6-D7/D9; Gather G5-G8; Challenge C5 |
| R7 | §10 H3 | Set conditionally supported and record the selected central intent-definition model over validated categories plus reviewed exceptional handles; defer the exact membership set to Iteration 2. | D4-D5; Extract E3; Challenge C3 |
| R8 | §10 H4 | Set technically confirmed with an external setting dependency: repository-owned Jekyll layout, explicit generated page front matter, supported SEO/sitemap plugins, no custom Actions build; verify the authenticated publishing source before Phase B. | D2-D3/D6; Gather G3-G4; Extract E1; Challenge C2 |
| R9 | §10 Proposed RESEARCH Focus | Scope Iteration 2 to qualified EN/RU/KK terminology/translation ownership, the exact intent membership matrix, and an executable static render/metadata validation contract; do not repeat general SEO/AEO searches. | Open Questions Q1-Q3; Iteration Status |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** The recommended architecture and remaining questions fit the frozen vision, phases, DoD, DoF, and principles; Iteration 1 found no evidence requiring a frozen contract change.

## Fact Candidates

No fact candidates. The delegated owner/Coordinator messages supplied iteration scope, mode, and execution authority rather than enduring human-only project facts.

## Strategic Insights (Research)

No strategic insights. The deep-mode rationale was an operational research-depth decision, not new domain or product knowledge beyond the frozen HL.

## Findings Map

```text
data/communities.json
├─ community facts (one owner)
├─ reviewed EN/RU/KK strings
└─ reviewed intent definitions
   ├─ validated category ids
   └─ exceptional live handles
              │
              ▼
       one locale-aware renderer
       ├─ README.md       ──► GitHub visitor
       ├─ index.md        ──► Pages `/`
       ├─ ru/index.md     ──► Pages `/ru/`
       └─ kk/index.md     ──► Pages `/kk/`
              │
              ▼
 repository-owned Jekyll layout + supported plugins
 ├─ one identity / one h1 / correct html lang
 ├─ self-canonical + reciprocal hreflang
 ├─ concise type navigation + one intent map
 ├─ sitemap + accurate Dataset → public JSON
 └─ coherent title/description/social metadata
              │
              ▼
 evidence boundary
 ├─ controllable: generated currency, routes, DOM, links, metadata, access
 └─ external: recrawl, rank, Search Console, AI inclusion/citation
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (confirmed with `/`, `/ru/`, `/kk/` dedicated-index design), H2 (supported with external-outcome limit), H3 (conditionally supported), H4 (technically confirmed; Pages setting unverified)
- **Hypotheses deferred:** None
- **Gaps discovered:** exact qualified Kazakh wording and review ownership; exact intent category/exception membership; authenticated Pages publishing source; owner-approved repository metadata/social image; optional Search Console availability; executable cross-render/metadata test details.
- **Superseded decisions:** D4 supersedes Extract ED3's undecided carry of per-entry facets versus central mapping; D6-D7 supersede Extract ED4's unresolved baseline/optional signal boundary.

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | EN/RU/KK terminology and translation review contract | The frozen contract forbids invented meaning and silent fallback; Kazakh content does not yet exist. | Build a finite string inventory, source/owner rules, and fail-closed acceptance matrix; obtain qualified native review rather than machine inference. |
| 2 | Exact AI/startups/jobs/events/engineering membership | The representation is selected, but a wrong seed map would create authoritative-looking omissions or false inclusion. | Review current categories and exceptional handles entry by entry for only these five intents; specify semantics and non-goals for each. |
| 3 | Static render and validation proof | H4 is technically supported, but the later TS needs executable evidence precise enough to catch today's semantically broken but HTML-valid output. | Define route/front-matter/layout fixtures and assertions for headings, special characters, anchors, language/canonical/alternate sets, Dataset links, mobile first-screen navigation, and GitHub/Pages parity. |
| 4 | Pages and repository external settings | Source folder and owner-approved discovery metadata cannot be established or changed from public read-only evidence. | Confirm authenticated Pages source; prepare before/after evidence and exact owner approval boundary for homepage, description, topics, and social preview. |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — the hard minimum is two iterations, and qualified translation/terminology, exact intent membership, and executable render-contract evidence remain material before a safe TS.
- [ ] **BLOCKED** — no current blocker; the Coordinator should scope Iteration 2 from the open threads.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 found a proportional static design that would have been missed by treating the task as “translate the README” or “add SEO files”: keep one type-first catalog, generate a GitHub README plus three standards-aligned Pages routes, derive one compact intent map from reviewed category/handle definitions, and give every metadata addition a documented consumer job. It also found important negative evidence: `kz` is not the Kazakh language tag, a project-path robots file cannot control the host, subdirectory `WebSite` markup cannot promise a distinct Google site name, `llms.txt` is adopted but not a Google/OpenAI search contract, and HTML validity can pass while a catalog link is semantically broken. The recommendation is **MORE NEEDED** because the mandatory second iteration must settle translation authority, exact intent membership, and executable render evidence. Self-critique: public research cannot authenticate Pages/Search Console settings, validate native Kazakh meaning, or measure future rank/AI citation; those limits are preserved as explicit gates rather than converted into implementation promises.

---

*RES — 20260827-132641__catalog_discoverability: Multilingual routes, intent navigation, and discoverability | 2026-08-27*

# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> Goal: Make one verified Kazakhstan IT Telegram catalog easy to discover, understand, and use in English, Russian, and Kazakh without creating drifting catalogs or weakening accuracy.

## Consistency Check

Each Gather dimension was checked pairwise against the other five and then against the frozen DoD/DoF. The table records incompatible combinations; pairs not listed can coexist technically, although later stress tests may still make them disproportionate.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------|------------------|
| D1 | One trilingual document | D6 | Silent English fallback | Neither gives each language a complete independent reading flow; together they directly violate DoD 2 and DoF 3. |
| D1 | Three distinct language routes | D5 | Rely mainly on repository topics/description/homepage | Repository metadata cannot express route-level language, canonical, or reciprocal-alternate semantics required by DoD 5. |
| D3 | Type-first plus cross-type intent map | D4 | Existing single category only | Current AI and startups evidence spans categories; this pair cannot render the required intents without omissions or false broadening. |
| D3 | Intent-first catalog | D4 | Keyword inference | It makes unreviewed generated meaning the primary catalog organization, conflicting with accuracy and DoF 3. |
| D3 | Client-side search/filter | D2 | Custom Actions-built site | Static generated content already satisfies the measured scale; this combination creates the expressly forbidden new application/maintenance surface in DoF 7. |
| D4 | Any reviewed intent representation | D6 | Automatic build-time translation | Reviewed classification cannot make unreviewed translated meaning exact; the public projection would still fail closed-language requirements. |
| D4 | Keyword inference | D6 | Silent fallback | Both replace missing reviewed meaning with hidden behavior and cannot satisfy DoD 7's completeness gate. |
| D5 | Reciprocal alternates/sitemap/Dataset | D1 | Flat GitHub-only language files with no canonical Pages routes | The language URLs and canonical public pages needed by those signals do not exist as a stable route contract. |

Two alternatives are also independently incompatible with the frozen contract regardless of their pair: automatic translation/silent fallback violate DoF 3, and a full client-side application violates DoF 7 while the corpus remains satisfiable with static links.

**Surviving configurations** (from Extract's Configuration Space, after removing rows containing incompatible pairs):

| Config | D1 | D2 | D3 | D4 | D5 | D6 | Notes |
|--------|----|----|----|----|----|----|-------|
| C1 | Root EN + `/ru/` + `/kk/` | Dedicated generated indexes | Type-first + intent map | Category + reviewed handle map | Standard + alternates/sitemap/Dataset/JSON | Descriptions + dictionary | Meets the frozen constraints with no runtime. |
| C2 | Root EN + `/ru/` + `/kk/` | README as Pages index | Type-first + intent map | Per-entry reviewed facets | Standard + alternates/sitemap/Dataset/JSON | All structured strings | Technically feasible if README/Jekyll metadata coupling is controlled. |
| C3 | Neutral root + `/en/` + `/ru/` + `/kk/` | Dedicated generated indexes | Type-first + intent map | Category + reviewed handle map | Standard + alternates/sitemap/Dataset/JSON | Descriptions + dictionary | Feasible but adds a selector page. |
| C5 | Root EN + `/ru/` + `/kk/` | Dedicated generated indexes | Intent-first | Per-entry reviewed facets | Standard + alternates/sitemap/Dataset/JSON | All structured strings | Feasible, but changes the primary catalog organization. |
| C6 | Root EN + `/ru/` + `/kk/` | Dedicated generated indexes | Repeated intent summaries | Per-entry reviewed facets | Standard + alternates/sitemap/Dataset/JSON | All structured strings | Feasible if summaries contain links only, not copied facts. |
| C7 | Root EN + `/ru/` + `/kk/` | `docs/` Pages source | Type-first + intent map | Category + reviewed handle map | Standard + alternates/sitemap/Dataset/copied JSON | Descriptions + dictionary | Feasible with generated copies and settings changes. |
| C9 | Root EN + `/ru/` + `/kk/` | Dedicated generated indexes | Type-first + intent map | Per-entry reviewed facets | Visible metadata + JSON | Descriptions + dictionary | Feasible but underspecifies multilingual crawl signals. |
| C10 | Root EN + `/ru/` + `/kk/` | Dedicated generated indexes | Type-first + intent map | Category + reviewed handle map | C1 signals + `llms.txt` | Descriptions + dictionary | Feasible; extra file still needs a distinct job. |
| C14 | Root EN + `/ru/` + `/kk/` | README as Pages index | Repeated intent summaries | Category + reviewed handle map | Standard + alternates/sitemap/Dataset/JSON | Descriptions + dictionary | Feasible but combines two forms of output coupling. |

**Unexpected survivors:**

- **C2:** required per-entry intent arrays survive the accuracy attack because an explicit empty array can make review completeness testable. They are not required merely because they are sound.
- **C7:** a `docs/` publishing source can preserve one-source truth if every file is generated, including JSON. Its disadvantage is extra projection/settings work, not logical inconsistency.
- **C10:** `llms.txt` can coexist with the architecture and has an emerging agent-navigation audience. It fails proportionality here, not technical validity.

## Findings

### C1: Pairwise elimination leaves C1 as the smallest complete configuration

The surviving families were challenged against every frozen DoD item and the subtractive principle:

| Candidate | Attack | Result |
|-----------|--------|--------|
| C1 | Can dedicated Pages indexes drift from README? | Survives if all four artifacts are generator-owned and generator-current checks enumerate every output. |
| C2/C14 | Can README safely serve GitHub and own explicit Jekyll metadata/layout behavior? | Possible, but it couples GitHub portability and Pages front matter again. It offers no user value over a generated `index.md`, so the risk has no distinct consumer job. |
| C3 | Does a neutral selector improve access? | No measured need. It increases three content pages to four and makes root visitors choose before seeing value; English at root already exposes the same three-way switch. |
| C5 | Does intent-first browsing improve all users? | It makes a reviewed secondary facet the primary taxonomy and weakens direct groups/channels/bots discovery. The type-first catalog plus top intent map serves both paths with less restructuring. |
| C6 | Do repeated summaries avoid record duplication? | They can avoid copied descriptions, but they still repeat navigation material throughout the document and risk pushing entries below the first screen. A single compact map has the same job. |
| C7 | Does moving to `docs/` reduce complexity? | No. It requires a Pages source-setting change and generated copies of JSON/layout/assets while the repository root already publishes the data. Keep it as fallback only if authenticated settings disprove root publishing. |
| C9 | Are visible content and JSON enough? | Not for the frozen multilingual metadata outcome. It omits reciprocal alternates and route discovery that have documented jobs. |
| C10 | What new access does `llms.txt` enable? | None demonstrated for this 62-entry catalog: concise Markdown and canonical JSON are already public and linkable. Adoption is counter-evidence, but no distinct unmet job was found. |

The surviving baseline is therefore **C1** with one refinement: “separate handle-to-intent mapping” means structured intent definitions that select validated categories and add reviewed exceptional handles. It is not an unstructured second catalog.

### C2: C1 survives the one-source, route, and render invariants

A later TS can make C1 executable with the following invariants:

| Boundary | Required invariant | Failure caught |
|----------|--------------------|----------------|
| Source | Community facts exist once in `data/communities.json`; every public language string required by a route is present and reviewed | Hand-maintained translations, fallback, fact drift |
| Generator | One locale-aware renderer writes `README.md`, `index.md`, `ru/index.md`, and `kk/index.md`; check mode compares all four | Stale or partially generated projections |
| Routes | Every Pages output has explicit permalink/language/title/description data and links to all three language routes | Broken one-action access, wrong language metadata |
| Layout | One repository-owned layout emits one `h1`, correct `html lang`, self-canonical, reciprocal self-inclusive alternates, coherent Open Graph, and a matching Dataset download URL | Current identity split and contradictory metadata |
| Entries | Markdown-special text is escaped; stable handle-derived anchors are unique; every generated Telegram link and intent link resolves | Current pipe/table corruption and dead internal links |
| Sitemap | Only canonical public routes are emitted with absolute project URLs | Source-noise URLs or canonical conflict |
| Evidence | GitHub and Pages desktop/mobile render snapshots plus DOM assertions are checked after publication | A source-only pass that misses browser behavior |

GitHub Pages limits do not challenge this design: the official service limits are orders of magnitude above three static routes and one dataset, and the native Jekyll build avoids a custom workflow. Google describes sitemap submission as a hint, not a crawling guarantee, and recommends absolute canonical URLs; that bounded role is compatible with DoD 8. Schema.org defines `Dataset` as structured information about a topic and `DataDownload` as a downloadable distribution at a specific location/format, which fits the existing JSON when the markup stays factual.

Sources: <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits>; <https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap>; <https://schema.org/Dataset>; <https://schema.org/DataDownload>.

### C3: Central intent definitions survive only with semantic and structural gates

The attack against the central map is silent omission: a new AI community filed under `jobs` will not enter the AI intent unless a human adds its handle. Per-entry `intents` has a parallel failure—an author may enter an incomplete or wrong list—but a required field at least forces a syntactic decision.

C1 remains preferable only under these conditions:

- every required high-value intent is declared once with a reviewed set of contributing category IDs and exceptional live handles;
- channel categories become required or explicitly nullable and every non-null value is schema-validated;
- every declared category and handle exists, every handle resolves to exactly one live entry of any type, and every required intent renders at least one route;
- category anchors and handle anchors are deterministic and validated in every locale;
- the intent section renders compact links to canonical category or entry anchors, never duplicated entry descriptions or inferred synonyms;
- a human reviews the initial AI/startups/jobs/events/engineering mapping and any later semantic change. Automation proves structural completeness, not truth of classification.

This model can include bots through an exceptional handle without inventing bot categories, but no intent needs a token bot merely to appear “cross-type.” Visitors still receive a direct Bots type route. Exact intent membership, especially the engineering umbrella and startup exceptions, remains a material Iteration 2 question.

### C4: Syntax validation alone cannot establish presentation correctness

On 2026-08-27, the W3C Nu validator checked the live Pages URL and returned no HTML errors, only informational messages about trailing slashes on void elements. Yet the DOM still has two competing `h1` elements and the `Землетрясения | Казахстан` entry has lost its Telegram anchor because Markdown interpreted the pipe as table syntax.

This is useful counter-evidence against relying on a generic “valid HTML” gate. A later TS needs semantic assertions for exactly one primary heading, expected link targets, unique anchors, language/canonical/alternate sets, first-screen route presence, and representative special-character fixtures, in addition to HTML/structured-data validation.

Source: <https://validator.w3.org/nu/> against <https://saubakirov.github.io/KZ-IT-telegram-list/> on 2026-08-27.

### C5: Discovery evidence must distinguish configuration, eligibility, and outcome

The strongest rejected claim is that adding supported metadata proves better search rank or AI inclusion. It does not. The evidence ladder is:

1. **Configuration:** rendered canonical, alternates, sitemap, Dataset link, repository metadata, and public JSON match expected values.
2. **Eligibility/access:** routes return 200, are not excluded by applicable host robots rules, and crawler-visible HTML/JSON is retrievable.
3. **Observed retrieval:** timestamped search/AI queries can cite or surface the public source after deployment.
4. **Outcome:** rank, click-through, citation frequency, and recrawl timing remain variable external behavior.

Phase B can prove levels 1–2 and record level 3 snapshots. It cannot make level 4 a release guarantee. Search Console can add owner-specific indexing evidence if access exists; lack of access is an evidence limitation, not a reason to add more files.

### C6: Challenge-stage research decisions

| # | Decision | Reason |
|---|----------|--------|
| CD1 | Recommend C1: root English, `/ru/`, `/kk/`, dedicated generated Pages indexes, type-first catalog, and one compact structured intent map. | It is the only survivor with every frozen consumer job and no redundant page, runtime, copied record, or optional agent file. |
| CD2 | Use reviewed intent definitions over category IDs plus exceptional live handles, not keyword inference or mandatory facets on all 62 entries. | It expresses observed overlaps with bounded data churn; strict referential/anchor gates expose structural drift while human review owns semantics. |
| CD3 | Include reciprocal language metadata, sitemap, accurate Dataset/DataDownload linkage, and coherent repository metadata; exclude `llms.txt` from the baseline. | The included signals have documented consumers; the excluded file has adoption but no distinct unmet job for this concise Markdown/JSON catalog. |
| CD4 | Require semantic DOM/link/route assertions in addition to syntax validators. | The current live page passes W3C error validation while remaining semantically broken for identity and one Telegram link. |
| CD5 | Treat Pages source settings, repository settings, Search Console, search rank, and AI inclusion as external evidence boundaries. | Read-only public evidence cannot authenticate settings, and no implementation controls ranking or answer selection. |

## OODA Log

| Loop | Observe | Orient | Decide / revise | Sufficiency result |
|------|---------|--------|-----------------|--------------------|
| 1 — frozen-contract attack | Checked every configuration against DoD/DoF and every pair of Gather dimensions. | Several options are technically possible but redundant; custom apps, automatic translation, fallback, inference, and category-only intents conflict directly with the contract. | Reduce nine technical survivors to C1 by distinct consumer job and maintenance cost. | H4 confirmed conditionally without requiring an amendment. |
| 2 — semantic-integrity attack | Compared central intent mapping with required entry facets and tested the live page through W3C validation. | Neither representation automates semantic truth, and generic HTML validity misses current user-visible failures. | Keep central mapping only with human-reviewed seed semantics plus referential, anchor, and route assertions. | H3 conditionally supported; exact membership remains a named gap. |
| 3 — discoverability-claim attack | Rechecked sitemap, structured-data, crawler, and Pages limits against outcome claims. | Official mechanisms establish hints, metadata, and eligibility, not rank or inclusion; `llms.txt` adds no current distinct job. | Bound Phase B evidence to configuration/access/retrieval snapshots and reject outcome guarantees. | H2 supported with counter-evidence and explicit external limits. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 is a supported static architecture with a precise one-source and route contract. | Authenticated confirmation of the current Pages publishing source belongs before Phase B settings work. |
| Central category-plus-handle intent definitions are the smallest honest overlap model. | Native/domain review must settle exact AI/startups/jobs/events/engineering membership. |
| `/kk/`, `lang=kk`, self-canonicals, reciprocal alternates, sitemap, and accurate Dataset linkage have bounded consumer jobs. | Kazakh terminology and all new Kazakh descriptions require qualified review; no silent fallback is acceptable. |
| `llms.txt`, a project-path robots file, and a client application do not earn baseline scope. | Post-publication search/AI retrieval and Search Console evidence remain external and non-guaranteed. |
| Generic HTML validity misses the current broken entry and competing identity. | TS must choose executable DOM/link/anchor/cross-render checks. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?
- [x] At least one hypothesis tested? H2 was supported, H3 conditionally supported, and H4 conditionally confirmed.
- [x] Counter-evidence sought? Technically valid alternatives, W3C validation's blind spot, `llms.txt` adoption, sitemap limits, semantic-review risk, and external retrieval variance were preserved.
- [x] Metacognitive check completed? Yes. C1 is a proportional recommendation, not proof that every facet label, translation, or future crawler outcome is correct.

Stage complete: YES
→ User decision: Proceed to the Iteration 1 RES under the Coordinator's briefing authorization.

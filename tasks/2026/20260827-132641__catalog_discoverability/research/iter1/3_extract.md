# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> Goal: Make one verified Kazakhstan IT Telegram catalog easy to discover, understand, and use in English, Russian, and Kazakh without creating drifting catalogs or weakening accuracy.

## Configuration Space

Gather produced six dimensions with four alternatives each (4,096 raw permutations). The table keeps the distinct, non-obviously-contradictory structural families that can change the implementation or maintenance contract. Orthogonal D5/D6 variants are represented explicitly rather than repeating every route/navigation row; no row is ranked in this stage.

| Config | D1: Language route shape | D2: GitHub/Pages source coupling | D3: Primary browsing model | D4: Intent ownership | D5: Search and machine signals | D6: Translation ownership |
|--------|--------------------------|----------------------------------|----------------------------|----------------------|--------------------------------|---------------------------|
| C1 | EN `/`; RU `/ru/`; KK `/kk/` | Dedicated generated Pages indexes; README retained | Type-first plus compact intent map | Separate handle-to-intent mapping | Metadata + alternates/sitemap/Dataset + public JSON | Entry descriptions plus UI/category dictionary |
| C2 | EN `/`; RU `/ru/`; KK `/kk/` | README is Pages index | Type-first plus compact intent map | Per-entry reviewed intents | Metadata + alternates/sitemap/Dataset + public JSON | Every localized public string in structured data |
| C3 | Neutral `/`; pages at `/en/`, `/ru/`, `/kk/` | Dedicated generated Pages indexes; README retained | Type-first plus compact intent map | Separate handle-to-intent mapping | Metadata + alternates/sitemap/Dataset + public JSON | Entry descriptions plus UI/category dictionary |
| C4 | Flat `README.ru.md` and `README.kk.md` | README is Pages index | Type-first plus compact intent map | Existing category only | Visible content + stable metadata + public JSON | Entry descriptions plus UI/category dictionary |
| C5 | EN `/`; RU `/ru/`; KK `/kk/` | Dedicated generated Pages indexes; README retained | Intent-first with type badges | Per-entry reviewed intents | Metadata + alternates/sitemap/Dataset + public JSON | Every localized public string in structured data |
| C6 | EN `/`; RU `/ru/`; KK `/kk/` | Dedicated generated Pages indexes; README retained | Type sections plus repeated intent summaries | Per-entry reviewed intents | Metadata + alternates/sitemap/Dataset + public JSON | Every localized public string in structured data |
| C7 | EN `/`; RU `/ru/`; KK `/kk/` | Pages source moved to `docs/` | Type-first plus compact intent map | Separate handle-to-intent mapping | Metadata + alternates/sitemap/Dataset + copied JSON | Entry descriptions plus UI/category dictionary |
| C8 | EN `/`; RU `/ru/`; KK `/kk/` | Custom Actions-built static site | Client-side search/filter | Per-entry reviewed intents | Metadata + alternates/sitemap/Dataset + public JSON + `llms.txt` | Every localized public string in structured data |
| C9 | EN `/`; RU `/ru/`; KK `/kk/` | Dedicated generated Pages indexes; README retained | Type-first plus compact intent map | Per-entry reviewed intents | Visible content + stable metadata + public JSON | Entry descriptions plus UI/category dictionary |
| C10 | EN `/`; RU `/ru/`; KK `/kk/` | Dedicated generated Pages indexes; README retained | Type-first plus compact intent map | Separate handle-to-intent mapping | Metadata + alternates/sitemap/Dataset + public JSON + `llms.txt` | Entry descriptions plus UI/category dictionary |
| C11 | One trilingual document with anchors | README is Pages index | Type-first plus compact intent map | Existing category only | Repository topics/description/homepage plus public JSON | Every localized public string in structured data |
| C12 | EN `/`; RU `/ru/`; KK `/kk/` | Dedicated generated Pages indexes; README retained | Type-first plus compact intent map | Generated keyword inference | Metadata + alternates/sitemap/Dataset + public JSON | Automatic build-time translation |
| C13 | Neutral `/`; pages at `/en/`, `/ru/`, `/kk/` | Custom Actions-built static site | Client-side search/filter | Per-entry reviewed intents | All listed machine signals | Every localized public string in structured data |
| C14 | EN `/`; RU `/ru/`; KK `/kk/` | README is Pages index | Type sections plus repeated intent summaries | Separate handle-to-intent mapping | Metadata + alternates/sitemap/Dataset + public JSON | Entry descriptions plus UI/category dictionary |

C1 is a previously unstated combination: it treats intent as a validated central projection over existing categories and exceptional handles, rather than adding a facet to every entry, while still generating language-specific static pages. This preserves an explicit review boundary without forcing 62 new entry fields.

## Findings

### E1: Language entry points and publication artifacts should be separate concerns

The route decision has three independent layers:

1. **User route:** `/`, `/ru/`, and `/kk/` are the shortest coherent set when English remains the default. A neutral selector adds another maintained page and makes every visitor choose before seeing catalog value; it is useful only if there is no defensible default language.
2. **Generated artifact:** GitHub needs a portable `README.md`; Pages needs per-route front matter and page metadata. Generating a dedicated `index.md`, `ru/index.md`, and `kk/index.md` keeps those contracts explicit instead of making README rendering depend on `jekyll-readme-index` behavior.
3. **Jekyll shell:** a small layout and include can own one page title, `html lang`, canonical, reciprocal alternates, social metadata, and Dataset JSON-LD without changing the catalog body model.

Jekyll's official documentation supports page front matter, custom variables, layouts, and explicit `permalink` values. A material constraint is that a page permalink supplied only through front-matter defaults is ignored; each generated page therefore needs explicit front matter. `jekyll-seo-tag` covers common title/description/canonical/Open Graph/JSON-LD output but states that it does not cover every use case. Reciprocal `hreflang`, language-specific `html lang`, and the project-specific Dataset node still need a small repository-owned head contract. `jekyll-sitemap` is supported by GitHub Pages and can create a discoverable route list without a separate build.

Sources: <https://jekyllrb.com/docs/front-matter/>; <https://jekyllrb.com/docs/configuration/front-matter-defaults/>; <https://jekyllrb.com/docs/permalinks/>; <https://github.com/jekyll/jekyll-seo-tag>; <https://github.com/jekyll/jekyll-sitemap>.

### E2: A four-output renderer preserves one-source truth more cleanly than translated source trees

The smallest deterministic projection is one renderer with locale input that writes:

- `README.md` for GitHub's primary repository experience;
- `index.md` for the English Pages root;
- `ru/index.md` for Russian;
- `kk/index.md` for Kazakh.

All four are generated from `data/communities.json` plus a small reviewed terminology dictionary. The English README can link directly to all three Pages routes above the fold, avoiding relative-link behavior that differs between GitHub and Pages. The Pages files can contain explicit front matter because they are not expected to be the repository README. Existing live data remains the only entry source; translated files are projections, not manually edited catalogs.

This arrangement also isolates the Markdown-special-character defect: the renderer needs one escaping/anchor contract used by every projection. A stable entry anchor derived from the Telegram handle allows intent maps to link to the canonical full entry without duplicating descriptions. Exact output filenames are an implementation detail for TS, but the separation of repository and Pages projections is a research-level invariant.

### E3: The intent model can be explicit without becoming entry-level taxonomy

Three candidate ownership models remain structurally credible after Gather:

| Model | Representation | Completeness invariant | Maintenance consequence |
|-------|----------------|------------------------|-------------------------|
| Per-entry facets | Required `intents: []` on every live entry | Every entry is reviewed, including an explicit empty list | Strong local semantics; broad data churn and repeated decisions for all 62 entries |
| Central derived map | Each intent declares contributing categories plus explicit exceptional handles | Categories/handles must exist; referenced entries must be live; rendered links must resolve | Small, inspectable cross-type projection; overlapping exceptions remain explicit |
| Existing category only | Intent points to one or more categories | Category must exist and be validated on the relevant types | Lowest change cost; cannot express AI/jobs and startups/news overlap honestly |

The central map is a distinct configuration, not synonym inference. For example, an AI intent may include the `ai` category and reviewed exceptional handles currently categorized as jobs or data analytics. Engineering may link a reviewed set of technical category anchors instead of repeating dozens of entries. Jobs and events can presently derive from their categories. Startups needs reviewed exceptional handles because no live entry uses the existing startups category. This produces a small navigation projection while each full community record still appears once.

For this model to remain truthful, channel categories must join the validation contract; otherwise a derived link can silently depend on an unvalidated value. Bots can remain discoverable by type when there is no reviewed intent classification. The intent map must not imply that every community with a keyword belongs to an intent.

### E4: Machine signals form a consumer matrix, not an SEO bundle

| Signal | Documented consumer/job | Required content invariant |
|--------|-------------------------|----------------------------|
| Visible localized headings and summaries | People; ordinary search extraction | Match the selected route language and catalog facts |
| Self-canonical + reciprocal `hreflang` | Search language routing | All alternates exist, are fully qualified, reciprocal, and self-inclusive |
| Sitemap | Crawlers discovering static routes | Contain canonical public pages, not generated source noise |
| Public JSON link + `Dataset`/`DataDownload` | Dataset-oriented discovery and programmatic consumers | Describe the same visible catalog and a real downloadable JSON URL |
| Repository description/topics/homepage | GitHub discovery and social/repository context | Match the maintained public identity and correct Pages URL |
| `OAI-SearchBot` access | Eligibility for ChatGPT search crawling | Not blocked at the host authority; no inclusion promise |
| `llms.txt` | Emerging agent-navigation proposal | Add only if it offers navigation unavailable from concise Markdown and JSON |

This matrix exposes why “all machine signals” is not automatically a stronger configuration. The current catalog already publishes Markdown and JSON; a new `llms.txt` would mostly restate links unless an identified consumer or access problem appears. Conversely, `hreflang` and Dataset markup each have a documented but bounded job. Search rank, recrawl time, AI citation, and answer inclusion remain outside the generated artifact's control.

### E5: Extract-stage research decisions

| # | Decision | Reason |
|---|----------|--------|
| ED1 | Carry a dedicated generated Pages-index family into Challenge as the cleanest GitHub/Pages boundary. | Jekyll page metadata and GitHub README portability are different render contracts; explicit generated pages avoid hidden `jekyll-readme-index` coupling. |
| ED2 | Carry English at `/` with `/ru/` and `/kk/` as the minimal route family; retain the neutral selector only as counterfactual. | It meets one-action language access with three content pages instead of four and aligns URL and language codes. |
| ED3 | Carry both a required per-entry facet and a validated central category-plus-handle map into Challenge. | Both can express overlap explicitly; their completeness and data-churn costs differ materially. |
| ED4 | Treat standard metadata, reciprocal language links, sitemap, and accurate Dataset linkage as separable baseline candidates; treat `llms.txt` as an optional experiment. | Each baseline signal has a documented consumer. `llms.txt` adoption is real, but no examined Google/OpenAI search contract uses it. |

## OODA Log

| Loop | Observe | Orient | Decide / revise | Sufficiency result |
|------|---------|--------|-----------------|--------------------|
| 1 — routes and artifacts | Crossed four route shapes with four publication approaches and checked Jekyll page/front-matter behavior. | README-as-index saves a file but couples two renderers; a neutral selector adds a page without adding catalog value. | Promote the dedicated-index/root-English family to Challenge; preserve the alternatives for pairwise elimination. | H1's exact route/generator question materially narrowed using external Jekyll evidence. |
| 2 — intent and translation ownership | Compared entry facets, category-only derivation, keyword inference, and a central mapping against observed overlaps. | Explicit meaning is necessary, but it need not be copied into every entry; category-plus-exception definitions are auditable. Automatic translation and silent fallback cannot meet exactness. | Define validation invariants for both explicit survivors and expose the central-map configuration as a novel combination. | H3 has two challengeable configurations and concrete completeness tests. |
| 3 — consumer signals | Mapped every proposed metadata file/field to Google, OpenAI, GitHub, Jekyll, or a human consumer. | Signals with different consumers cannot be treated as additive ranking points; emerging agent conventions need a distinct unmet job. | Separate baseline language/canonical/sitemap/Dataset work from optional `llms.txt` and external repository settings. | H2 and H4 have bounded, testable implementation surfaces and explicit non-guarantees. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| A generated `README.md` plus three dedicated Pages indexes gives the repository and Jekyll explicit contracts. | Challenge the extra generated English index against README-as-index and `docs/` alternatives. |
| `/`, `/ru/`, `/kk/` is the smallest standards-aligned route family. | Verify that no frozen requirement actually needs a neutral selector or `/en/`. |
| A validated intent definition over categories and exceptional handles is a lower-churn alternative to 62 entry facets. | Test silent omission risk and compare it pairwise with required entry-level facets. |
| Standard metadata, language alternates, sitemap, Dataset linkage, and repository settings have distinct jobs. | Eliminate unsupported or redundant machine-facing additions and state external evidence limits. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] At least one hypothesis tested? H2, H3, and H4 were narrowed into falsifiable configurations.
- [x] Counter-evidence sought? README-as-index, neutral selection, per-entry facets, `llms.txt`, and custom-site families remain explicit alternatives for Challenge.
- [x] Metacognitive check completed? Yes. The novel central-map configuration shows that explicit reviewed overlap does not require either category-only loss or per-entry facet churn.

Stage complete: YES
→ User decision: Continue to Challenge under the Coordinator's briefing authorization.

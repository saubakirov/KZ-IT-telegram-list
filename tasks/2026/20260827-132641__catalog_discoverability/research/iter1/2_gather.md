# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> Goal: Make one verified Kazakhstan IT Telegram catalog easy to discover, understand, and use in English, Russian, and Kazakh without creating drifting catalogs or weakening accuracy.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Language route shape | English at `/`; Russian at `/ru/`; Kazakh at `/kk/` | Neutral selector at `/`; language pages at `/en/`, `/ru/`, `/kk/` | Flat generated files such as `README.ru.md` and `README.kk.md` | One trilingual document with in-page anchors |
| D2: GitHub/Pages source coupling | Keep `README.md` as the Pages index through `jekyll-readme-index` | Generate a dedicated Pages `index.md` plus language directories while retaining `README.md` for GitHub | Move the Pages source to a `docs/` directory | Build and publish a separate static site with a custom Actions workflow |
| D3: Primary browsing model | Type-first catalog plus a compact cross-type intent map | Intent-first catalog with type badges | Type sections plus repeated generated intent summaries | Client-side search/filter interface |
| D4: Intent ownership | Derive intent only from the existing single `category` | Add reviewed multi-value `intents` on each live entry | Infer intent at generation time from names/descriptions | Maintain a separate handle-to-intent mapping |
| D5: Search and machine signals | Visible content, stable metadata, canonical routes, and the already-public JSON | Add reciprocal language annotations, sitemap, and accurate `Dataset`/`DataDownload` markup | Add `llms.txt` and Markdown alternates for agent consumers | Rely mainly on GitHub repository topics, description, and homepage |
| D6: Translation ownership | Store every public localized string in structured data | Store entry descriptions plus a small UI/category terminology dictionary | Translate generator output automatically at build time | Permit silent fallback to English when a localized string is absent |

No alternative is selected here. Extract will make combinations visible; Challenge will eliminate incompatible combinations.

## Findings

### G1: The live Pages render confirms structural and portability defects

Observed 2026-08-27 at <https://saubakirov.github.io/KZ-IT-telegram-list/> using the rendered DOM, a 1536×730 desktop viewport, and a 390×844 mobile viewport:

- The document has two `h1` elements: the theme-generated repository title `KZ-IT-telegram-list` and the generated catalog title `Awesome Kazakhstan IT Telegram`.
- On the 390×844 viewport, the first live Telegram entry begins at approximately 1671 CSS pixels, well below the first screen. The `Groups` heading begins at approximately 1567 pixels.
- The live head reports Jekyll 3.10.0 and `jekyll-seo-tag` 2.8.0. The title is `Awesome Kazakhstan IT Telegram | KZ-IT-telegram-list`; `html lang` is `en-US`.
- The canonical is correct for the current English root, but there are no `hreflang` alternates.
- The description and Open Graph description still use the older bilingual repository wording. No `og:image` is present.
- JSON-LD declares a `WebSite` whose `name` is the repository slug and whose `headline` is the catalog title, reproducing the identity split in structured form.
- The live name `Землетрясения | Казахстан` is parsed into a two-cell HTML table inside a list item. No `https://t.me/kzquake` anchor survives. `format_entry()` does not escape Markdown-special characters for live entries; only archive table cells are escaped.
- `https://saubakirov.github.io/KZ-IT-telegram-list/data/communities.json` returns `200 application/json`; machine-readable data is already public. The project-path `robots.txt`, `sitemap.xml`, and `feed.xml` return 404.

Sources: live rendered DOM and response headers; [`scripts/generate_readme.py`](../../../../../scripts/generate_readme.py); <https://pages.github.com/versions/>.

### G2: The data already contains most of the raw navigation signal, but its contract is inconsistent across types

Current source observations:

| Type | Entries | Russian descriptions | Category state |
|------|---------|----------------------|----------------|
| Groups | 38 | 38/38 present | Required and validated; 14 categories currently used |
| Channels | 20 | 20/20 present | Present on 18 entries but neither required nor validated; generator ignores it |
| Bots | 4 | 4/4 present | No category on any bot |

There is no Kazakh description field or localized category/section dictionary. `categories` contains English display names only. The validator requires English descriptions for all types, requires a category only for groups, and does not validate `description_ru` completeness.

The high-value intents are not equivalent to the existing single category:

| Intent probe | Existing evidence | Why single-category derivation is incomplete |
|--------------|-------------------|----------------------------------------------|
| Jobs | One group and five channels have `category: jobs` | This intent is already cross-type and can be linked without inference. |
| Events | One channel has `category: events` | It is cross-type-capable but currently has only one qualifying entry. |
| AI | Cursor group is `ai`; ML Jobs is `jobs`; DS/ML News is `data-analytics` | A valid AI route needs overlapping classification; treating all data analytics as AI would misclassify BI/DWH entries. |
| Startups | Three descriptions mention startups, under `general`, `news`, and `education` | No live entry uses the existing `startups` category; keyword inference would make unreviewed semantics authoritative. |
| Engineering | Many technical categories contribute | It is an umbrella intent over multiple categories rather than one category value. |

This confirms that H3 cannot be implemented honestly by simply exposing channel categories. A later design must choose between an explicit reviewed facet and a weaker link map whose limitations are visible.

Sources: [`data/communities.json`](../../../../../data/communities.json); [`scripts/validate_schema.py`](../../../../../scripts/validate_schema.py); [`scripts/generate_readme.py`](../../../../../scripts/generate_readme.py).

### G3: GitHub Pages can support a small multilingual static surface without a new application

Official GitHub documentation establishes that:

- Pages/Jekyll supports standalone Markdown pages with front matter and explicit permalinks.
- `_config.yml` controls supported themes and plugins; theme defaults can be overridden with repository-local layout files.
- `jekyll-seo-tag` 2.8.0 and `jekyll-sitemap` 1.4.0 are in the supported GitHub Pages dependency set alongside Jekyll 3.10.0.
- Unsupported plugins require a separately generated static site, but nothing discovered in the required route/metadata design needs one.
- Branch publishing builds automatically after changes reach the configured source. The unauthenticated Pages API does not reveal this repository's source settings, so the exact branch/folder remains an external setting to verify before Phase B.

The current render and public `/data/communities.json` strongly imply that the repository root is in the publication source. That is an inference, not an authenticated settings fact.

Sources: <https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll>; <https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll>; <https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll>; <https://pages.github.com/versions/>.

### G4: Language routes and language metadata are separate decisions

Google's localized-page guidance requires each language version to list itself and all alternates with fully-qualified reciprocal `hreflang` links. A self-referential canonical should point to the same-language URL; canonicalizing translations to English would suppress the language routes as duplicates. HTML `lang` is still required for document semantics even though Google says it detects content language algorithmically rather than using `lang` for that detection.

The standards-valid language tag for Kazakh is `kk`; the IANA language subtag registry has records for `en`, `ru`, and `kk`, and no language record for `kz`. Google likewise requires an ISO 639-1 language code and warns that a country code alone is not a language code. A route slug is technically arbitrary, but using `/kk/` keeps URL, `html lang`, and `hreflang` aligned. The visible switch label can still be `KZ` or, preferably, the language's own name `Қазақша` after owner review.

The regional comparable <https://qazaqitcom.kz/> redirects to `/en` and exposes `/ru` and `/kz`, with matching `html lang` values. It demonstrates that explicit language routes are understandable to users, but it also demonstrates the metadata trap: its fetched HTML had no canonical or reciprocal alternate links, and `lang="kz"` is not a registered language tag.

Sources: <https://developers.google.com/search/docs/specialty/international/localized-versions>; <https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry>; live Qazaq IT Community responses observed 2026-08-27.

### G5: H2 is supported for discoverability, with a narrower role left open for `llms.txt`

Official search and crawler guidance separates three concerns:

1. **Google Search and generative features.** Google's 2026 guidance says the same technical foundation and people-first content apply to generative AI results. It explicitly says Google ignores `llms.txt` for visibility and ranking, needs no AI-specific markup or keyword rewriting, and recommends clear structure, unique value, device quality, reduced duplication, and Search Console measurement.
2. **ChatGPT search crawling.** OpenAI documents `OAI-SearchBot` as the crawler used to surface websites in ChatGPT search and distinguishes it from GPTBot training and user-triggered `ChatGPT-User`. Allowing a crawler makes inclusion possible; it is not an answer or ranking guarantee.
3. **The `llms.txt` proposal.** Version 2 records meaningful ecosystem adoption and explicitly frames itself as a proposal for guided agent access, especially for large documentation sites. This is counter-evidence against calling the file useless. It is not evidence that Google or OpenAI Search uses it, and this catalog already exposes concise Markdown plus its canonical JSON.

The host-level `https://saubakirov.github.io/robots.txt` returns 404. RFC 9309 permits crawlers to access resources when `/robots.txt` returns a 4xx response. A file at `/KZ-IT-telegram-list/robots.txt` would not control standard robots because the protocol location is the authority root `/robots.txt`; the project repository cannot independently create that host-root resource. Therefore a project-path robots file would be redundant or misleading.

Sources: <https://developers.google.com/search/docs/fundamentals/ai-optimization-guide>; <https://developers.openai.com/api/docs/bots>; <https://llmstxt.org/>; <https://www.rfc-editor.org/rfc/rfc9309.html>.

### G6: Some current structured data and repository signals have bounded, documented jobs

- Google's site-name feature uses `WebSite` structured data, visible headings, titles, and `og:site_name`, but it does not support a distinct site name at a subdirectory level. This project lives at `saubakirov.github.io/KZ-IT-telegram-list/`, so the current `WebSite` node cannot be counted as evidence that Google will show `Awesome Kazakhstan IT Telegram` as a project-specific site name.
- Google explicitly supports `Dataset`, `DataCatalog`, and `DataDownload` structured data for Dataset Search. A JSON catalog qualifies in principle as a structured object intended for processing. Accurate `Dataset` metadata linked to the already-public JSON has a documented consumer job, but it must describe visible content and does not improve general ranking by promise.
- GitHub documents repository topics as a discovery and classification mechanism. The live repository API reports an empty homepage and only `almaty`, `astana`, `kazakhstan`, and `telegram`; the current bilingual description is also the stale Pages description.
- GitHub supports a repository social-preview image as an external setting. The current Pages head has no `og:image`, and repository metadata exposes no owner-validated catalog homepage.

Sources: <https://developers.google.com/search/docs/appearance/site-names>; <https://developers.google.com/search/docs/appearance/structured-data/dataset>; <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics>; <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview>; GitHub repository API observed 2026-08-27.

### G7: Comparable catalogs validate separate projections, but scale determines how much machinery is justified

| Comparable | Strong pattern | Counter-evidence / limit for this task |
|------------|----------------|----------------------------------------|
| [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) | Hundreds of thousands of stars; separate language files and static Pages routes; a central language index makes language choice explicit. | The inspected English and Russian Pages both render generic `Index` metadata and no `hreflang`; separate routes alone do not create multilingual discoverability. Its separate dynamic search site addresses a vastly larger corpus. |
| [Awesome Python](https://github.com/vinta/awesome-python) | A Python build parses one README into a static site with category pages, sitemap, and other projections; it demonstrates that a generator can serve GitHub and the web without a runtime application. | Its `website/` builder, parsers, templates, metrics jobs, and filters are substantial machinery for a much larger catalog. It also generates `llms.txt`, showing real adoption but not a search-ranking guarantee. |
| [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | Puts a recommended HTML surface in front of a very large legacy Markdown catalog. | The scale and category count justify a dedicated website; copying this solution to 62 live entries would violate the task's subtractive constraint. |
| [Public APIs](https://github.com/public-apis/public-apis) | Very large category index and machine-oriented entry fields. | Its current README begins with extensive commercial promotion before the curated catalog, a direct first-screen anti-pattern for this task. |
| [Qazaq IT Community](https://qazaqitcom.kz/) | Regional EN/RU/Kazakh routes and native-language content. | Uses `/kz` and `lang="kz"`, lacks fetched canonical/alternate metadata, and uses a full Next.js application; it is a route/terminology reference, not an architecture to copy. |

### G8: Search retrieval is a dated external snapshot, not a DoD promise

A 2026-08-27 three-language query snapshot (`Kazakhstan IT Telegram groups channels bots`; `IT сообщества Казахстана Telegram группы каналы`; `Қазақстан IT Telegram қауымдастықтары арналар топтар`) surfaced the GitHub repository alongside generic directories, TGStat, Telegram pages, and Qazaq IT Community. The repository result used the old bilingual description. The snapshot shows that the source is retrievable and that localized competitors exist; it does not establish stable rank, per-language rank, freshness, or future AI citation.

### G9: Stage research decisions

| # | Decision | Reason |
|---|----------|--------|
| GD1 | Treat published DOM, response metadata, and direct data URLs as the current public authority; treat local generator intent as explanatory evidence. | H2 and H4 concern what consumers receive, and the live render reveals defects that source inspection alone misses. |
| GD2 | Separate user-facing language labels from standards-valid route and metadata codes. | `KZ` is understandable branding shorthand, but `kk` is the registered Kazakh language code required for interoperable language metadata. |
| GD3 | Model H3 as overlapping intent facets rather than as renamed categories. | AI/jobs and startups/news overlap in current entries; a single category cannot represent both without loss or false inference. |
| GD4 | Require a named documented consumer for every machine-facing addition while preserving counter-evidence about emerging adoption. | Google rejects AI-specific SEO hacks, OpenAI documents crawler controls, and `llms.txt` has adoption but no evidenced ranking or inclusion contract for these consumers. |

## OODA Log

| Loop | Observe | Orient | Decide / revise | Sufficiency result |
|------|---------|--------|-----------------|--------------------|
| 1 — current surface | Measured live DOM/head/mobile layout and compared it with generator/data/schema. | H4 is not just a theme question: current default layout creates identity duplication, while unescaped live names break links. | Expand H4 to include an explicit render contract and cross-render escaping, not only route creation. | External live surface used; H4 materially tested; new defects found. |
| 2 — official mechanisms | Checked GitHub Pages/Jekyll, Google multilingual/search/structured-data, OpenAI crawler, RFC robots, and IANA language-tag documentation. | H2 is strengthened for ordinary structure but `WebSite`, robots, and `llms.txt` have narrower or different jobs than assumed. | Separate general search, dataset discovery, ChatGPT crawl eligibility, and agent navigation as distinct consumers. | Counter-evidence found; H2 tested beyond confirmation. |
| 3 — taxonomy and comparables | Measured category/description overlap and inspected five comparable catalogs/surfaces plus a multilingual query snapshot. | H3 needs reviewed multi-value meaning; large-catalog web apps are disproportionate here; separate language files do not solve metadata automatically. | Carry explicit facets, a compact link-map alternative, and a no-app static configuration into Extract. | H3 tested; briefing gaps narrowed enough to form configurations. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The live root has measurable two-`h1`, metadata, first-screen, and special-character defects. | Choose the smallest Pages/generator arrangement that fixes them without coupling GitHub rendering to Jekyll front matter. |
| Correct public language semantics are `en`, `ru`, and `kk`; reciprocal routes need self-canonical and reciprocal alternates. | Decide whether English remains `/` or a neutral selector justifies an extra route. |
| Ordinary search foundations and documented crawler access are more defensible than AI-only copy; `Dataset` has a bounded consumer job. | Decide whether `llms.txt` has any distinct job in this small catalog after Markdown and JSON are linked. |
| Cross-type intents overlap and cannot be inferred safely from one category. | Compare explicit reviewed `intents` with a weaker category-link map and quantify validation cost. |
| Lightweight Jekyll pages/layouts/plugins are supported. | Eliminate configurations that rely on unverified Pages settings, unsupported metadata, or a new app. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one hypothesis tested? H2, H3, and H4 were each tested.
- [x] Counter-evidence sought? `llms.txt` adoption, comparable-route metadata failures, structured-data limits, intent-maintenance cost, and large-catalog architectures were examined.
- [x] Metacognitive check completed? Yes. New findings include the `kk`/`kz` distinction, host-root robots constraint, project-subdirectory site-name limitation, existing public JSON, and concrete cross-intent overlaps.

Stage complete: YES
→ User decision: Continue to Extract under the Coordinator's briefing authorization.

# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Make one verified Kazakhstan IT Telegram catalog easy to discover, understand, and use in English, Russian, and Kazakh without creating drifting catalogs or weakening accuracy.

## Configuration Space

The six Gather dimensions yield 4,096 raw combinations. The table retains the distinct closure-contract families that change what a later TS can verify; it does not reconsider the selected routes, renderer, or static Pages architecture.

| Config | D1: Review binding | D2: Incomplete locale | D3: Intent rules | D4: Render evidence | D5: External disposition | D6: Destinations |
|--------|--------------------|-----------------------|------------------|---------------------|--------------------------|------------------|
| C1 | Locale payload digest | Fail multilingual gate | Categories + exceptional includes | Layered source/API/Jekyll/public DOM | Typed per dependency | Explicit generator-owned IDs |
| C2 | Per-field metadata | Fail multilingual gate | Categories + include/exclude handles | Layered source/API/Jekyll/public DOM | Typed per dependency | Explicit generator-owned IDs |
| C3 | Locale payload digest | Omit incomplete route | Categories + exceptional includes | Layered source/API/Jekyll/public DOM | Typed per dependency | Explicit generator-owned IDs |
| C4 | Out-of-band checklist | Publish incomplete status | Full handle enumeration | Post-deployment DOM only | Conditional evidence | Display-text slugs |
| C5 | Presence alone | Silent fallback | Keyword inference | Source assertions only | Positive rank/inclusion gate | Numeric anchors |
| C6 | Locale payload digest | Fail multilingual gate | Full handle enumeration | GitHub API + local Jekyll | All external items required | Explicit generator-owned IDs |
| C7 | Per-field metadata | Fail multilingual gate | Categories + include/exclude handles | Source assertions only | Typed per dependency | Explicit generator-owned IDs |
| C8 | Locale payload digest | Fail multilingual gate | Categories + exceptional includes | Post-deployment DOM only | Typed per dependency | Explicit generator-owned IDs |
| C9 | Locale payload digest | Fail multilingual gate | Categories + exceptional includes | Layered source/API/Jekyll/public DOM | All external items required | Explicit generator-owned IDs |
| C10 | Locale payload digest | Fail multilingual gate | Categories + exceptional includes | Layered source/API/Jekyll/public DOM | Typed per dependency | Renderer heading slugs |

C1 is the combination the Briefing did not spell out: a content-bound linguistic approval can coexist with a compact category-derived taxonomy when every rendered fact and destination is independently verified. It does not require per-entry approval flags, full intent enumerations, or duplicated review evidence.

## Findings

### E1: One canonical locale payload turns “qualified review” into an executable gate

For each locale, construct this review payload from source data and the shared UI registry:

```text
locale payload
├─ meta: title, description
├─ north_star: purpose, non_goals[4]
├─ categories: all 19 id → display-value pairs
├─ ui: all 39 key → display-value pairs
├─ live_descriptions: all live handle → description pairs
└─ archive_text: all archive handle → {description, reason} pairs
```

The payload has 131 values on the current snapshot, but the validator derives the live/archive quantities from source; it must never hardcode “62” or “2.” The UI and category key sets are exact. The review digest algorithm is:

1. recursively normalize every payload string to Unicode NFC;
2. preserve declared array order, especially the four non-goals;
3. serialize JSON with UTF-8, recursively sorted object keys, no ASCII escaping, and compact separators;
4. compute lowercase SHA-256 over those bytes.

RFC 8785 confirms the underlying requirement: hashing is reliable only when JSON first has an invariant representation. This string-only project payload does not need to import the full JCS number serialization; the project-specific algorithm above is smaller and fully specified.

Source: <https://www.rfc-editor.org/rfc/rfc8785.html>.

An approval record is acceptable only when it has the locale, owner-designated human reviewer, recorded language/domain qualification, ISO review date, `APPROVED` verdict, and exact recomputed digest. Review records are excluded from their own digest. EN defines approved meaning; RU/KK compare against EN and invariant community identity. Any changed value invalidates only that locale's approval record, but the frozen three-language outcome makes the complete generation gate fail until all three approvals match again.

This contract explicitly does **not** decide who supplies translations or claim current Russian/Kazakh approval. It makes that external content input finite and testable. Machine/AI output can be a candidate but can never set the approval verdict.

### E2: The exact intent configuration is compact and complete

The selected current configuration is:

```yaml
display_order: [ai, startups, jobs, events, engineering]
definitions:
  ai:
    categories: [ai]
    include_handles: [ml_jobs_kz, dsmlkz_news]
  startups:
    categories: [startups]
    include_handles: [thetechkzchat, thetechkz, saubakirov]
  jobs:
    categories: [jobs]
    include_handles: []
  events:
    categories: [events]
    include_handles: []
  engineering:
    categories:
      - ai
      - blockchain
      - data-analytics
      - devops-sysadmin
      - gamedev
      - hardware
      - mobile
      - programming-languages
      - qa-testing
      - security
      - web-development
    include_handles:
      - devkz
      - illuminatinc
      - teamleads_kz
      - datanomika
      - DevSkills
      - nu_acm_w
      - sysadm_in_up
      - saubakirov
      - cleverskz
      - Get_Telegram_ID_bot
```

No runtime exclusion list is needed for the current data: none of the selected categories contains a false-positive member. Gather G4-G5 records every semantic exclusion and the full 62-entry disposition. Adding redundant negative lists would create another fact that can drift. If a future member genuinely conflicts with an otherwise-correct category rule, that change must either correct the member's category or add a reviewed exclusion capability through a later task.

Validation and generation invariants are exact:

- intent IDs and display order are exactly the five values above;
- every category ID exists; every exceptional handle resolves case-insensitively to exactly one live entry; archive handles are forbidden;
- an exceptional handle cannot already be selected by that intent's categories;
- derived membership is category union exceptional handles, with at least one current member per intent;
- current snapshot set equality is AI 3, startups 3, jobs 6, events 1, engineering 46, using the exact rows in Gather G5 as the baseline fixture;
- every full entry is emitted once per surface; intent navigation contains only internal links;
- future totals/membership are derived, while semantic rule changes remain reviewed source changes.

### E3: Explicit anchor grammar removes renderer disagreement from navigation identity

Display text is localized and therefore cannot own a stable identifier. The minimum explicit ID grammar is:

| Destination | ID grammar | Example |
|-------------|------------|---------|
| Type section | `type-{type}` | `type-groups` |
| Type/category section | `type-{type}-category-{category-id}` | `type-channels-category-jobs` |
| Intent section | `intent-{intent-id}` | `intent-ai` |
| Full live entry | `entry-{handle.casefold()}` with underscores preserved | `entry-get_telegram_id_bot` |

An intent category selector links to each non-empty type/category destination generated from that category. An exceptional handle links to its single entry ID. Empty selected categories such as current `blockchain` produce no link, not a dead destination. Every internal `href` must resolve to exactly one ID on GitHub-rendered README and every Pages route.

GitHub documents that automatically generated section anchors change when headings or duplicate-heading order changes. Explicit IDs decouple destination identity from localized wording and renderer-specific slug algorithms.

Source: <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links>.

### E4: A later TS can use this executable evidence contract

Expected target sets, labels, and counts are always derived from the catalog at the commit under test. “Current 64” is a research fixture, not a permanent assertion.

#### Pre-publication / repository-controlled gates

| ID | Surface | Executable assertion | Failure disposition |
|----|---------|----------------------|---------------------|
| A1 | Locale source | Exact locale set `en,ru,kk`; exact 19 category keys and 39 UI keys; derived live/archive description key equality; all values non-blank/non-placeholder; no undeclared visible locale literal | Block Phase A |
| A2 | Review binding | Each locale has owner-designated qualified human, `APPROVED`, ISO date, and matching canonical payload digest; AI/provider cannot be reviewer | Block Phase A; no partial route generation |
| A3 | Intent source | Exact five IDs/order; category/handle references valid; no redundant exceptional handle; baseline membership equals Gather G5 fixture; future membership derived | Block Phase A |
| A4 | Generator currency | `README.md`, `index.md`, `ru/index.md`, and `kk/index.md` all match one generator run/check; invariant name/handle/count/date sets equal source | Block Phase A |
| A5 | Generated Markdown | Each full live/archive record appears once; every Telegram URL/text pair equals source; current `Землетрясения \| Казахстан` target survives; special-character fixtures cover pipe, brackets, emphasis, underscore, backtick, backslash, angle bracket, and ampersand | Block Phase A |
| A6 | GitHub rendered Markdown | Fetch HTML media for `README.md` at the exact commit/ref; article has exactly one `h1`; expected Telegram anchor `(text, href)` multiset equals source; every internal fragment resolves once | Block Phase A/release candidate |
| A7 | Local Pages build | Build with the GitHub Pages dependency set from the actual publishing source; `/`, `/ru/`, `/kk/`, sitemap, layout, JSON-LD, and link/ID assertions pass before publication | Block Phase B deployment |

GitHub officially documents local Pages/Jekyll preview through the publishing source and recommends Bundler to reduce dependency drift. The rendered-Markdown API supplies GitHub's markup behavior; local Jekyll supplies the Pages renderer. Neither replaces public evidence.

Sources: <https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll>; <https://docs.github.com/en/rest/repos/contents#get-repository-content>.

#### Post-publication / real-environment gates

| ID | Surface | Executable assertion | Failure disposition |
|----|---------|----------------------|---------------------|
| P1 | HTTP routes | `/`, `/ru/`, `/kk/` return 200 `text/html`; `/sitemap.xml` returns 200 XML; `/data/communities.json` returns 200 with `application/json` | Block Phase B acceptance |
| P2 | GitHub README article | Exactly one article `h1`; direct absolute EN/RU/KK links occur before the first full entry; expected external Telegram `(name, URL)` multiset equals source; all internal fragments resolve uniquely | Block Phase B acceptance |
| P3 | Each Pages DOM | Exactly one document `h1`; `html lang` equals route (`en`,`ru`,`kk`); expected invariant names/targets and locale descriptions appear once; language/type/intent links resolve; no repo-slug competing primary identity | Block Phase B acceptance |
| P4 | Canonical/alternates | One self-canonical per route; every route has the identical three-link fully qualified alternate set `{en:/, ru:/ru/, kk:/kk/}` including itself; no `x-default` because root is English content, not a neutral selector | Block Phase B acceptance |
| P5 | Sitemap | Contains all three canonical route URLs once; every listed catalog URL returns 200; no duplicate README/locale variant or 404 route; sitemap existence is recorded as a discovery hint, not crawl proof | Block supported-metadata acceptance |
| P6 | Dataset JSON-LD | Exactly one `Dataset` node per route with locale title/summary reused as `name`/`description`, description length 50–5000, self URL, `inLanguage`, source `dateModified`, CC0 license, and one `DataDownload` pointing to the public JSON with `application/json` | Block supported-structured-data acceptance |
| P7 | Public JSON parity | Downloaded body passes schema validation; content type is JSON; normalized/canonical digest equals `data/communities.json` at the deployed commit | Block machine-access/freshness acceptance |
| P8 | Bounded responsive evidence | At 390×844 and 1366×768, Pages has no horizontal overflow; `h1`, one summary, generated freshness, all three language links, type/intent navigation, and at least one live Telegram target are wholly inside the viewport. For GitHub, apply the same bound relative to the README article top because GitHub owns surrounding chrome. Capture screenshots plus numeric bounding boxes. | Block first-screen/responsive acceptance |

Playwright's official assertions support role-based locators, exact counts/attributes, viewport intersection, response checks, and screenshots. The contract is tool-independent, but these primitives show it is executable rather than visual-review prose.

Source: <https://playwright.dev/docs/test-assertions>.

### E5: Cross-render target parity requires set and structure checks

The three current Pages misses demonstrate separate failure shapes:

1. `kzquake`: the URL remains as text in malformed table structure, so a URL-substring test passes while the user has no link.
2. Two archive handles: the intended Markdown link text exists inside a raw HTML table but Jekyll does not emit anchor elements, so source/text checks again pass.
3. GitHub renders all three correctly, so a GitHub-only check cannot establish Pages parity.

The required assertion is therefore the multiset of anchor pairs `(visible source name, normalized https://t.me/{handle})`, scoped to full catalog entries. Intent navigation must point internally and must not create additional Telegram anchors. The current expected set has 64 pairs; future expected sets come from live+archive data. Generic HTML validity remains supplementary only.

### E6: External evidence becomes a state machine, not an architecture question

| Gate | Entry condition | Pass | Unavailable/fail behavior |
|------|-----------------|------|---------------------------|
| G-PAGES-SOURCE | Before Phase B build/deployment changes | Authenticated evidence says `master` + repository root, or owner explicitly authorizes changing the source to that selected contract | Phase B publication is DEFERRED/BLOCKED on owner access; do not redesign routes or move to `docs/` by inference. |
| G-REPO-SETTINGS | Before description/homepage/topics/social-preview mutation | Before snapshot + exact owner-approved target values/asset + after snapshot/public result | Do not mutate. Phase A and repository-controlled site files remain independently judgeable. |
| G-SEARCH-CONSOLE | After public routes exist, only if owner access is supplied | URL/sitemap inspection recorded with date and property | Record access limitation; do not fail publication or add compensating SEO files. |
| G-RETRIEVAL | After publication | Timestamped EN/RU/KK search/AI observations record query, locale, date, surface, and result verbatim | Positive or negative result never changes release verdict; any rank/inclusion guarantee is a failure. |

This removes the last “unknown implementation design” from H2/H4: every external item has a gate owner and a failure disposition.

### E7: Extract-stage decisions

| # | Decision | Reason |
|---|----------|--------|
| ED1 | Use one canonical 131-unit locale payload digest and fail the complete multilingual gate when any locale approval is absent/stale. | It binds human review to exact content with one record per locale and makes fallback/partial publication structurally impossible. |
| ED2 | Use the exact five category-plus-exception definitions in E2 with no runtime exclusion list. | The entry-by-entry audit found no category false positive; negative runtime data would be redundant, while the semantic exclusion trace remains explicit in Gather. |
| ED3 | Use explicit type/category/intent/handle IDs and assert every internal destination across GitHub and Pages. | Display/localized headings and renderer slug rules are unstable ownership for cross-render navigation. |
| ED4 | Require layered source, GitHub-rendered, local-Jekyll, public-response, DOM, and viewport evidence. | Each layer catches a measured failure another layer misses; the current three missing Pages anchors prove the need. |
| ED5 | Apply G-PAGES-SOURCE, G-REPO-SETTINGS, G-SEARCH-CONSOLE, and G-RETRIEVAL exactly as typed gates. | Authenticated access and variable retrieval stop being architecture questions or fabricated pass conditions. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Canonical locale payload/digest and fail-closed states make qualified review finite and executable. | Challenge reviewer identity, digest lifecycle, equal-value terms, and incomplete-output edge cases. |
| Exact category-plus-exception definitions plus stable IDs implement the 62-entry audit without duplicate records. | Attack false-positive/false-negative boundaries and future-entry behavior. |
| A1–A7 and P1–P8 form a layered evidence contract with exact assertions/dispositions. | Remove redundant checks and confirm every frozen DoD item is covered without depending on rank or owner credentials. |
| Four external gates have entry/pass/unavailable behavior. | Confirm none must become a new research iteration or architecture branch. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] At least one focused-stage decision made? ED1–ED5 select a complete closure configuration while preserving Iteration 1 architecture.

Stage complete: YES
→ User decision: Continue to Challenge under the Coordinator's focused-mode authorization.

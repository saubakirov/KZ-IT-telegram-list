# Phase HL — 20260827-132641__catalog_discoverability / Phase B: Published Discovery Surface

> **Date**: 2026-08-27
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS APPROVED — owner mandate, 2026-08-27
> **Contract**: DERIVATION-ONLY — inherits frozen Master HL baseline `00a21bb`
> **Parent HL**: [Master HL](../HL-20260827-132641__catalog_discoverability.md)
> **Pre-spec gate**: [Phase A RF](../phase-a/RF__phase-a__multilingual_catalog.md) · [Phase A REVIEW](../phase-a/REVIEW__phase-a__multilingual_catalog.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) · [Iteration 2 RES](../research/iter2/RES.md)
> **Authority**: The owner's 2026-08-27 mandate pre-authorizes autonomous planning,
> repository-controlled implementation, targeted revision, and formal local acceptance. It does not
> authorize a push, tag, release, Pages/source/settings mutation, Search Console submission, or any
> other external mutation. Phase B therefore ends this run at an approved local candidate plus an
> explicit authorization/public-evidence checkpoint.

> This Phase HL adds execution context only. It does not define an independent vision,
> acceptance contract, failure contract, or principles. Master HL §§1, 5, 6, and 7 remain the
> sole authority under `conventions.md` §3 rules 20–21.

---

## 2. Phase Context

Phase A is formally approved and closed at locale payload digest
`51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`. Its RF, not its
planned TS, establishes the delivered baseline: one explicit EN/RU/KK source, one renderer, four
generator-current projections, five exact intent definitions, stable destinations, twelve passing
regression tests, GitHub-render target/fragment parity, and unchanged catalog facts. The Phase A
REVIEW approves that exact digest and makes any later locale-content change invalidate the verdict.

The current local base is `d9fe27c6dce80008326fa8eb731d3aff40fd3726`. Read-only state
inspection on 2026-08-27 established the publication boundary:

| Surface | Current evidence | Phase B consequence |
|---------|------------------|---------------------|
| Pages publishing source | Authenticated GitHub settings: `Deploy from a branch`, `master`, `/(root)`; default domain; HTTPS required | Keep this setting unchanged; repository root files are the supported source |
| Public deployment | Site is live; settings link deployment run `33050462939`; remote `master` is `e4986e787018dbe92f51733e243916eba60cd2c4` | Public state predates the approved local Phase A candidate and is evidence of the before state only |
| Public routes | `/` is 200; `/ru/`, `/kk/`, and `/sitemap.xml` are 404 | Never claim route/public metadata completion before an authorized push and deployment |
| Public root metadata | `lang=en-US`, two H1s, self-canonical root, zero `hreflang`, no `og:image` | Repository candidate must correct these properties locally and retain exact post-deploy checks |
| Public catalog JSON | `/data/communities.json` is 200 `application/json` | Dataset `DataDownload.contentUrl` can name this real distribution |
| Repository discovery | Old bilingual description; blank homepage; topics `almaty`, `astana`, `kazakhstan`, `telegram` | Prepare exact target settings; do not apply them in this run |
| Repository social preview | General settings offers “Upload an image”; repository OG uses GitHub's generated fallback | Prepare and validate the upload asset; do not upload it in this run |

Official capability remains proportional: GitHub Pages dependency version 232 supports Jekyll
3.10.0; Jekyll front matter, Liquid pages, and repository-owned layouts are native;
Google's localized-page guidance calls for reciprocal alternates; and Dataset markup has a bounded
job when its name/description and JSON distribution match visible content. No custom application,
Actions build, `llms.txt`, project-path robots file, or second content system is needed.

The pinned `jekyll-sitemap` 1.4.0 plugin was rejected during the first local build because it
unconditionally emitted a project-path `robots.txt`. That output has no controlling job at a
subdirectory site and conflicts with Research Iteration 1 D7. Phase B instead uses a supported
Jekyll/Liquid `sitemap.xml` page and proves the same exact canonical three-route result without the
redundant robots surface.

## 3. Derived Phase Outcome

```text
approved Phase A source + unchanged locale digest
                    │
                    ▼
 generated route front matter ──► repository-owned Jekyll layout/head
 index.md   ru/index.md   kk/index.md
                    │
          ┌─────────┼──────────┐
          ▼         ▼          ▼
   visible body   metadata   stable machine access
   EN/RU/KK       canonical  sitemap + Dataset → JSON
   one H1         hreflang   social preview
   intent nav     Open Graph
          └─────────┼──────────┘
                    ▼
 deterministic build/DOM tests + 390×844 and 1366×768 browser evidence
                    │
                    ▼
 formal local REVIEW APPROVE (if warranted)
                    │
                    ▼
 authorization checkpoint: push/settings/deploy/public verification remain unapplied
```

The local candidate has one responsive static layout and one generated body contract. Each route
has a self-canonical URL, reciprocal `en`/`ru`/`kk` alternates plus English `x-default`, localized
head/social fields, and the same accurate Dataset description of the canonical JSON. The sitemap is
produced by the supported GitHub Pages plugin. Styling changes reading comfort and first-screen
reach without hiding body content, introducing client-side behavior, or turning the catalog into a
marketing page.

The exact external target package is:

| Setting | Proposed value |
|---------|----------------|
| Description | `Verified catalog of Kazakhstan IT and startup Telegram groups, channels, and bots — in English, Russian, and Kazakh.` |
| Homepage | `https://saubakirov.github.io/KZ-IT-telegram-list/` |
| Topics | `almaty`, `artificial-intelligence`, `astana`, `awesome-list`, `developer-community`, `it`, `jobs`, `kazakh-language`, `kazakhstan`, `russian-language`, `startups`, `telegram` |
| Social preview | Upload repository candidate `assets/social-preview.png` (1280×640 PNG, under 1 MB) |
| Pages | Preserve `Deploy from a branch` → `master` → `/(root)`; no source/settings change |

## 4. Scope, Sequence, and Files

| Path | Phase action | Boundary |
|------|--------------|----------|
| `_config.yml` | CREATE | Root-source GitHub Pages/Jekyll config and public-source exclusions |
| `Gemfile` | CREATE | Reproducible local build through the supported `github-pages` dependency |
| `_layouts/default.html` | CREATE | One semantic layout/head for locale, canonical/alternates, Dataset and social metadata |
| `assets/css/catalog.css` | CREATE | Restrained responsive styling with no client-side runtime |
| `assets/social-preview.svg` | CREATE | Deterministic editable source for the exact preview composition |
| `assets/social-preview.png` | CREATE | GitHub-upload-ready 1280×640 asset, under 1 MB |
| `scripts/generate_readme.py` | MODIFY | Add generated route/head fields without changing approved body or review payload |
| `scripts/test_catalog_generation.py` | MODIFY | Preserve and extend all Phase A source/body/digest assertions |
| `scripts/test_site_metadata.py` | CREATE | Deterministic Jekyll-output, metadata, sitemap, asset, and DOM contract checks |
| `sitemap.xml` | CREATE | Supported Jekyll/Liquid sitemap page for the exact three canonical routes |
| `index.md`, `ru/index.md`, `kk/index.md` | MODIFY — GENERATED | Add generated Phase B front matter; body bytes after front matter remain Phase A-equivalent |

Sequence:

1. Freeze the Phase A body/digest baseline in tests before adding any Phase B field.
2. Add supported Jekyll configuration, generated per-route head inputs, one layout, and one stylesheet.
3. Add the Jekyll/Liquid sitemap, visible-content-consistent Dataset metadata, social metadata, and the deterministic preview asset.
4. Extend the deterministic suite and build the site through the supported GitHub Pages dependency.
5. Inspect local EN/RU/KK routes at 390×844 and 1366×768, including first-screen navigation,
   headings, targets, metadata, overflow, and representative intent paths.
6. Run Antigravity on the final visible copy and metadata, bind the result to exact hashes, and
   disposition every finding before RF.
7. Submit the unchanged repository candidate to the one persistent formal Reviewer task; reuse the
   same Executor and Reviewer for every `REVISE` loop.
8. Stop at the authorization/public-evidence checkpoint with exact settings and commands prepared.

### Scope Budget

| Measure | Estimate | Limit | Result |
|---------|----------|-------|--------|
| Implementation paths | 13 | 30 | Within budget |
| New implementation files | 8 | 15 | Within budget |
| Modified implementation files | 5 | 30 | Within budget |
| Estimated implementation/generated delta | <2500 LOC | 3000 | Within budget |

No override is authorized. A custom Actions workflow, application/runtime, extra discovery file,
unlisted content surface, or scope-budget overrun returns to `/tfw-plan`.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Frozen Master HL | ✅ baseline `00a21bb` |
| Actual Phase A result and verdict | ✅ RF and REVIEW read; digest `51db402d…` approved at base `d9fe27c6…` |
| Two completed research iterations | ✅ D1–D16 retained; no broad research reopened |
| Pages source | ✅ authenticated read-only inspection: `master` / `/(root)` / branch deployment |
| Supported Jekyll/sitemap capability | ✅ GitHub Pages 232 and Jekyll 3.10.0; a Liquid sitemap page avoids the plugin's project-robots side effect |
| Repository-controlled planning/implementation/revision/local acceptance | ✅ owner mandate, 2026-08-27 |
| Push, tag, release, settings upload/edit, Pages mutation, Search Console | ⬜ explicitly unauthorized in this run |
| Public post-deploy evidence | ⬜ unavailable until authorized push/deploy; must remain deferred, not fabricated |

## 9. Phase Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Phase B changes approved locale body or digest | Medium | High | Byte-compare stripped bodies and recompute digest; any content change invalidates Phase A approval |
| Layout emits duplicate canonical/social fields | Medium | High | Own the complete head in one layout and assert exact singleton fields per route |
| Sitemap lists internal trace pages or omits a locale route | Medium | Medium | Configure excludes and assert the exact public route set in built output |
| Dataset claims unsupported or invisible facts | Medium | High | Limit to visible title/description/date/language/license/scope and the real JSON distribution |
| CSS hides useful content or breaks narrow screens | Medium | High | Two fixed viewport gates, overflow checks, first-useful-entry bounds, no script-dependent navigation |
| Social asset contains inaccurate generated text | Medium | Medium | Use deterministic vector source and exact-text raster output; inspect dimensions, bytes and rendered image |
| Public state is mistaken for candidate evidence | High | High | Label all existing public checks as before-state; mark post-deploy checks DEFERRED until publication |
| External settings drift before authorization | Medium | Medium | Re-read settings immediately before any later authorized mutation and abort on unexpected state |
| Antigravity advice is treated as the verdict | Medium | High | Record it as advisory; the formal TFW Reviewer alone issues APPROVE/REVISE |

---

*Phase HL — 20260827-132641__catalog_discoverability / Phase B: Published Discovery Surface | 2026-08-27*

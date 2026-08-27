# External checkpoint — 20260827-132641__catalog_discoverability / Phase B

> **Captured**: 2026-08-27T21:03:26.2750969+05:00
> **Mode**: authenticated read-only GitHub API, unauthenticated public HTTP, and `git ls-remote`
> **Authenticated actor**: `saubakirov`
> **Mutation count**: 0

## Current repository and Pages settings

The configured Git credential helper was used only to authenticate read-only REST/GraphQL requests;
no credential value was printed or stored in evidence. The in-app browser was also checked and was
signed out, so the authenticated API response is the settings authority for this checkpoint.

| Field | Current value |
|---|---|
| Description | `List of useful telegram groups about IT in Kazakhstan // Полезные Казахстанские IT каналы и группы в телеграм ` (including the trailing space returned by the API) |
| Homepage | blank |
| Topics | `almaty`, `astana`, `kazakhstan`, `telegram` |
| Default branch | `master` |
| Pages status / build type | `built` / `legacy` |
| Pages source | branch `master`, folder `/` |
| Pages URL | `https://saubakirov.github.io/KZ-IT-telegram-list/` |
| Custom domain | none |
| HTTPS enforced | `true` |
| Custom 404 | `false` |
| Latest Pages build | `built`; commit `e4986e787018dbe92f51733e243916eba60cd2c4`; created `2026-08-27T07:36:58Z`; updated `2026-08-27T07:37:37Z` |
| Social preview | GitHub default; GraphQL `openGraphImageUrl` was `https://opengraph.githubassets.com/ee935601bbcc0c71251d067ea4ba915e6fa10da0a0b1cc383d3f940546e0f072/saubakirov/KZ-IT-telegram-list` |

Remote refs at the checkpoint:

- `refs/heads/master` → `e4986e787018dbe92f51733e243916eba60cd2c4`
- existing `refs/tags/data-2026-08-27` → `45d9c3cb12c1e71c7df7429f1da32028bcfbeb89`

The existing tag is historical catalog-release identity. It must not be moved, reused, deleted, or
replaced by this presentation phase.

## Current public state

| URL | Status | Current response facts |
|---|---:|---|
| `/` | 200 | 18,994 UTF-8 bytes; SHA-256 `d643ddc0ddfc018d7f7163fdd26b8716c96dc927fd4e14e10dfd6824f8981cd8`; two H1s; `lang=en-US`; canonical root; zero `hreflang`; zero `og:image` |
| `/ru/` | 404 | Not deployed |
| `/kk/` | 404 | Not deployed |
| `/sitemap.xml` | 404 | Not deployed |
| `/data/communities.json` | 200 | 22,622 UTF-8 bytes; SHA-256 `b773a69d8f828b3732d387f797a5c41cbd37376d62be18e559b9a39d7d325de3`; 38 groups, 20 channels, 4 bots, 19 categories, 2 archived, `last_updated=2026-08-27` |

These values are before-state evidence only. They do not establish that any Phase B byte is public.

## Exact proposed target

| Setting | Target |
|---|---|
| Description | `Verified catalog of Kazakhstan IT and startup Telegram groups, channels, and bots — in English, Russian, and Kazakh.` |
| Homepage | `https://saubakirov.github.io/KZ-IT-telegram-list/` |
| Topics | `almaty`, `artificial-intelligence`, `astana`, `awesome-list`, `developer-community`, `it`, `jobs`, `kazakh-language`, `kazakhstan`, `russian-language`, `startups`, `telegram` |
| Social preview upload | reviewed file `assets/social-preview.png` only |
| Pages source | keep branch `master`, folder `/(root)` unchanged |
| Domain / HTTPS | keep default project domain and HTTPS enforcement unchanged |

No target in this table has been applied.

## Publication and public-verification runbook

Only the Coordinator may execute this runbook, and only after explicit owner authorization and a
formal Phase B `APPROVE`. The formal REVIEW must name one exact 40-character reviewed-base SHA; no
working-tree state, abbreviated SHA, or later unreviewed commit is eligible.

1. Re-open the Phase B REVIEW, require verdict `APPROVE`, extract its exact reviewed-base SHA, and
   verify it resolves locally. Require a clean worktree. Re-run schema, all catalog tests, generator
   currency, the supported pinned Jekyll build, metadata tests, and asset hashes on that SHA.
2. Repeat this entire read-only checkpoint immediately before mutation: authenticated repository,
   Pages source/build, social preview, remote `master`, the existing tag, and all five public URLs.
   Stop and return to the Coordinator on any unexplained drift. Never move the existing tag.
3. Confirm the reviewed SHA is a descendant of the freshly observed remote `master`. Push exactly
   `<reviewed-sha>:refs/heads/master` with ordinary `git push origin` and no force option. A non-fast-
   forward rejection is a hard stop; do not retry with force.
4. Poll the authenticated Pages latest-build endpoint until its `commit` equals the reviewed SHA and
   its status is `built`. Fail closed on `errored`, `canceled`, another SHA, or timeout. Re-read Pages
   settings and confirm source remains `master` / `/`; do not click Save or change the source.
5. Only under the same explicit settings authorization, update the repository description, homepage,
   and the exact twelve-topic set above. Upload only the reviewed `assets/social-preview.png` whose
   required facts are 1280×640, 27,394 bytes, SHA-256
   `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`.
6. Fetch `/`, `/ru/`, `/kk/`, `/sitemap.xml`, and `/data/communities.json`; require HTTP 200. Assert
   the sitemap contains exactly the canonical root, `/ru/`, and `/kk/` URLs, with no deployed
   project-path `robots.txt` or `llms.txt`. Parse every route for its exact singleton title,
   description, canonical, four reciprocal `hreflang` links, Open Graph/Twitter fields, Dataset
   JSON-LD, one H1, 64 name/Telegram target pairs, and the stable fragment set.
7. Repeat the six in-app-browser cases at 390×844 and 1366×768. Require no horizontal overflow,
   hidden critical content, clipping, executable scripts, or broken representative language/type/
   intent/catalog/JSON/contribution links, and capture fresh public screenshots.
8. Re-read repository metadata and GraphQL `openGraphImageUrl`; verify the exact description,
   homepage, twelve topics, and uploaded social preview. Verify each public route's `og:image` and
   `twitter:image` resolve to the reviewed PNG.
9. Search Console submission/index-coverage checks require separate explicit authorization and
   account access. Do not submit a sitemap or claim indexing/retrieval without that later evidence.
10. Bind the deployed SHA, settings values, build record, HTTP/head/browser/social evidence, and any
    remaining Search Console status into refreshed EV/RF, then resume the same formal Reviewer task.

## Deferred public outcomes

The following remain **DEFERRED — pending explicit authorization and deployment**: public `/ru/`,
`/kk/`, sitemap, final metadata, final social preview, responsive public-browser evidence, indexing,
Search Console, search visibility, AI retrieval/citation, traffic, and community-join outcomes.

## No-mutation record

This Executor performed authenticated GET/GraphQL reads, public GETs, and `git ls-remote` only. There
was no push, tag, release, deployment, repository/Pages/settings edit, upload, Search Console action,
or other external mutation.

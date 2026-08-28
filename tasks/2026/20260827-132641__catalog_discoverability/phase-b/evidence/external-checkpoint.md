# External checkpoint — 20260827-132641__catalog_discoverability / Phase B

> **Captured**: 2026-08-28T19:18:20.7169478+05:00
> **Revalidated after harness recovery**: 2026-08-28T19:25:03.0692872+05:00
> **Mode**: authenticated read-only GitHub REST/GraphQL, read-only Git ref/history probes,
> unauthenticated public GET/HEAD, and live Chrome inspection
> **Authenticated actor**: `c0rp-aubakirov`
> **Executor mutation count**: 0
> **Eligible reviewed deployment**: `bd7af42165c341d653e3efbb20091c131c9f7a40`

## Deployment and Pages state

The configured Git credential helper was used only for authenticated read-only requests. No
credential value was printed or stored. This checkpoint independently observed the external state
created before this Executor run; it did not create, retry, or alter that state.
The post-recovery recheck returned the same custom-image URL/bytes, repository settings, remote
master, Pages state/build, and protected tag facts recorded below.

| Field | Observed value |
|---|---|
| Authenticated `master` ref | `bd7af42165c341d653e3efbb20091c131c9f7a40` |
| Local remote-tracking reflog | Exactly one matching `update by push` entry to `bd7af421…`, at `2026-08-28 17:44:29 +0500` |
| Fast-forward evidence | Prior remote `e4986e787018dbe92f51733e243916eba60cd2c4` is the exact merge base and an ancestor; authenticated comparison is ahead 43, behind 0 |
| Pages status / build type | `built` / `legacy` |
| Pages source | branch `master`, folder `/` |
| Pages URL | `https://saubakirov.github.io/KZ-IT-telegram-list/` |
| Custom domain / HTTPS | none / enforced `true` |
| Latest Pages build | `built`; commit `bd7af42165c341d653e3efbb20091c131c9f7a40`; created `2026-08-28T12:44:30Z`; updated `2026-08-28T12:45:02Z`; no error |
| Matching recent build records | exactly 1 in the authenticated ten-build window |

The one matching local remote-tracking reflog entry, exact prior-SHA ancestry, zero-behind
comparison, authenticated remote ref, and matching Pages build jointly establish one observed
ordinary fast-forward push of the reviewed SHA. No force operation is present in the observed
history.

## Repository settings

| Setting | Observed value | Result |
|---|---|---|
| Description | `Verified catalog of Kazakhstan IT and startup Telegram groups, channels, and bots — in English, Russian, and Kazakh.` | exact target applied |
| Homepage | `https://saubakirov.github.io/KZ-IT-telegram-list/` | exact target applied |
| Topics | `almaty`, `artificial-intelligence`, `astana`, `awesome-list`, `developer-community`, `it`, `jobs`, `kazakh-language`, `kazakhstan`, `russian-language`, `startups`, `telegram` | exact sorted 12-topic set applied |
| Default branch / Pages source | `master`; branch `master`, folder `/` | unchanged as required |
| Repository social preview | GraphQL `openGraphImageUrl` is `https://repository-images.githubusercontent.com/92145063/3d01cb70-f0b7-406e-b18e-82b18df39588` | **VERIFIED** — non-fallback custom repository image |

The Coordinator delegation attributes the completed official-UI upload to the owner. This Executor
did not upload, retry, edit, or activate any setting. The resulting external state was independently
verified three ways: authenticated GraphQL returned the exact non-fallback URL above; GET and HEAD
both returned 200 `image/png`, 27,394 bytes, SHA-256
`13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`, byte-identical to
`assets/social-preview.png`; and authenticated Chrome Settings visibly rendered the same URL as a
640×320 repository card. The fresh 955×510 screenshot is
`repository-social-preview-settings.png`, 30,121 bytes, SHA-256
`e9d158759aa3df45f2eeffde09bccb3c8aed362df3b4bbab30e8c1256860119d`.

## Public HTTP and exact-byte state

Both GET and HEAD returned the status shown. Successful response bodies were compared byte-for-byte
with a fresh supported Jekyll build from an exact Git archive of `bd7af421…`.

| Public path | GET / HEAD | Bytes | SHA-256 | Reviewed build |
|---|---:|---:|---|---|
| `/` | 200 / 200 | 33,669 | `64597def18f8777f92739d131649299c1639af1923f7cccde34b86d7ea61de21` | byte-identical |
| `/ru/` | 200 / 200 | 40,530 | `fef3499ecf2d5678a52fea4d1a93d51ce5d168d883652087bb02d776c144ec0f` | byte-identical |
| `/kk/` | 200 / 200 | 41,343 | `2d4465e7dc55856683247bf036f113380b452db1053424d82935dff81d4fba49` | byte-identical |
| `/sitemap.xml` | 200 / 200 | 338 | `79dcb9bbd3dda14054fe33695f89f6f62cdeea08881a427ec059d5e2d1665767` | byte-identical |
| `/data/communities.json` | 200 / 200 | 45,260 | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` | byte-identical |
| `/assets/css/catalog.css` | 200 / 200 | 2,035 | `6079176c27db6ced57ff8ad71c7671cbd694a13a39322566da4d2b9b3f157b6d` | byte-identical |
| `/assets/social-preview.png` | 200 / 200 | 27,394 | `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d` | byte-identical |
| `/robots.txt` | 404 / 404 | 9,379 | `b620507312c5e97566a3c6cfaf99144fefc18a0da7d941401dfa0f5f58fb0368` | absent as required |
| `/llms.txt` | 404 / 404 | 9,379 | `b620507312c5e97566a3c6cfaf99144fefc18a0da7d941401dfa0f5f58fb0368` | absent as required |

The public metadata parser produced the exact existing 11,097-byte summary with SHA-256
`bbf30af0cdf5fbc26d547a80e97d9199035841e47b370cd2b0dc238a527f0552`, byte-identical to the
fresh exact-deploy local build summary. It establishes exact EN/RU/KK title, description, language,
self-canonical, four reciprocal alternates, Open Graph/Twitter fields, one Dataset JSON-LD object,
64 name/Telegram target pairs, and the stable fragment contract on every route.

The public sitemap contains exactly the canonical root, `/ru/`, and `/kk/` URLs. The public JSON
parses as 38 groups, 20 channels, 4 bots, 19 categories, 2 archived entries, and
`last_updated=2026-08-27`.

Each public route's `og:image` and `twitter:image` points to the 200 response for the reviewed
27,394-byte PNG. That page-level metadata remains **VERIFIED** and is byte-identical to the now
**VERIFIED** repository-setting preview above.

Full status, response-header, hash, settings, Pages, ref, tag, and parsed-contract facts are bound in
canonical-LF `public-http.json`.

## Live browser state

Fresh live Chrome cases at 390×844 and 1366×768 for EN, RU, and KK all passed: exact viewport,
one H1, expected language/title/canonical/head counts, loaded CSS, zero horizontal overflow, zero
hidden critical elements, zero executable or external scripts, no fixed/sticky obstruction, and a
one-action `#type-groups` jump that leaves the first catalog entry in view. The exact five
browser-observed representative hrefs per case passed 30/30 read-only HEAD checks. The canonical-LF
matrix and six fresh screenshots are task-local attachments.

A separate fresh authenticated Chrome Settings read inspected the visible `Social preview` card.
The card's computed background URL exactly matched GraphQL and rendered at 640×320. The visible
`Edit` control was not activated. The bound screenshot is the task-local attachment named above.

## Tag preservation

- `refs/tags/data-2026-08-27` remains annotated-tag object
  `45d9c3cb12c1e71c7df7429f1da32028bcfbeb89`.
- It still peels to commit `ee2e4f8f69b7bfc66b905801f950d8e832caa02f`.
- This Executor did not move, reuse, delete, replace, or create a tag.

## Remaining continuation

F4's repository-level custom-preview evidence condition is now satisfied. Phase B status remains
unchanged under the Executor role lock until the same formal Reviewer judges this refreshed RF/EV.
Search Console submission and index-coverage checks remain **DEFERRED** because no authorization or
evidence exists. Return this exact closure evidence to the persistent Reviewer; do not claim complete
publication or close the phase before that review.

## No-mutation record

This Executor performed authenticated GET/GraphQL queries, public GET/HEAD requests, Git read-only
ref/history checks, proportional local gates, and authenticated browser reads/screenshots only.
There was no push, tag, release, deployment, repository/Pages/settings edit, upload, Search Console
action, or other external mutation during this evidence refresh. The owner-performed upload occurred
before this Executor capture and is distinguished from the zero-mutation Executor record above.

# Verify — "Does the evidence establish the claims?"
> **Mindset:** Independent verifier. Reproduce proportionally and bind conclusions to exact bytes.
> **Reviewed base:** `a67e353573ddb36183c8e5764017adff5c38a6fb`
> **Parent:** `3280a618b6d9f1a1afd87a51ef382f6922baa0ae`
> **Deployed repository SHA:** `bd7af42165c341d653e3efbb20091c131c9f7a40`

## Verification Log

| # | Check | Result |
|---|---|---|
| 1 | Exact base, ancestry, scope, and attribution | PASS — `a67e353…` directly follows `3280a618…`; its 12 paths are RF, EV, six browser PNGs, browser matrix, external checkpoint, build log, and new public HTTP evidence only. No implementation/spec/status/journal change. |
| 2 | Deployed implementation binding | PASS — implementation paths differ by zero bytes between `bd7af421…` and `a67e353…`; authenticated Pages data binds the public build to exact `bd7af421…`. |
| 3 | Phase A digest and bodies | PASS — digest is exactly `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`; `data/communities.json` and `README.md` are byte-identical to accepted Phase A base `d9fe27c6…`; localized visible bodies remain exact. |
| 4 | Schema, generation, and regression tests | PASS — schema reports 38 groups, 20 channels, 4 bots, 19 categories, 2 archived, zero errors; all four projections are current; 13/13 tests pass. AST comparison proves all 12 predecessor tests unchanged and exactly one preservation test added. |
| 5 | Supported pinned Pages/Jekyll build | PASS — official pinned image digest `sha256:6791ebfd…` / image ID `sha256:ac7c0ad…`; Ruby 3.3.4, Bundler 2.5.11, Jekyll 3.10.0; output hashes match refreshed EV/public state. |
| 6 | Public HTTP outputs | PASS — EN, RU, KK, sitemap, JSON, CSS, and PNG return 200 with exact expected sizes/hashes; robots and llms return 404 with the recorded GitHub 404 body. |
| 7 | Route/head/Dataset/social contract | PASS — each locale has one H1, exact language, self-canonical, four reciprocal alternates, 12 OG fields, 5 Twitter fields, one visible-consistent Dataset JSON-LD block, 64 target pairs, and 93 stable fragments. |
| 8 | Sitemap/robots/llms | PASS — sitemap is 338 bytes with exactly the three locale URLs and is rendered by the repository-owned Jekyll/Liquid page; no project robots or llms source/output. Frozen Master HL remains untouched. |
| 9 | Deterministic preview | PASS — committed/public PNG is 1280×640 RGB, 27,394 bytes, SHA-256 `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`; the checked-in SVG command was rerun twice and both outputs are byte-identical. |
| 10 | Six-case browser evidence | PASS — final Git blob is 87,008 bytes / `35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`, with zero CRLF; all six exact 390×844/1366×768 EN/RU/KK cases parse, show no overflow/hidden critical content, and pass 30/30 representative local links. All six PNGs were visually inspected. |
| 11 | Current authenticated GitHub/Pages state | PASS with one blocker — default branch `master`; exact description, homepage, and 12 topics applied; Pages built from `master` `/` with HTTPS; latest build exact `bd7af421…`. Repository `openGraphImageUrl` remains generated fallback. |
| 12 | Protected tag/no-mutation boundary | PASS — `data-2026-08-27` remains annotated object `45d9c3cb12c1e71c7df7429f1da32028bcfbeb89`, peeled commit `ee2e4f8f69b7bfc66b905801f950d8e832caa02f`; no tag reuse/move/delete, push, release, settings edit, upload, or Search Console action occurred in review. |
| 13 | Refreshed Antigravity record | PASS — executable/model/mode/I/O/no-bypass/conversation and every byte binding are exact; SUCCESS/PASS, no findings or nits. Advisory only. |
| 14 | RF/EV/evidence completeness | PASS — all refreshed references/attachments exist and match. RF truthfully leaves the custom repository-card preview outcome unresolved rather than claiming success. |

## Commands Executed

| # | Command / operation | Result |
|---|---|---|
| 1 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archived, zero errors. |
| 2 | `python scripts/generate_readme.py --check` | PASS — all four projections current; digest exact. |
| 3 | `python -m unittest scripts.test_catalog_generation -v` | PASS — 13/13; predecessor-test AST audit separately confirms 12 retained plus one addition. |
| 4 | Supported pinned Pages image `/entrypoint.sh` build against the exact current implementation bytes | PASS — Ruby 3.3.4, Bundler 2.5.11, Jekyll 3.10.0; exact output bindings reproduced. |
| 5 | `python scripts/test_site_metadata.py --site <fresh-site>` | PASS — three routes, heads, Dataset, targets/fragments, sitemap, preview shape, and absent robots/llms. |
| 6 | Checked-in CairoSVG preview command, run twice | PASS — both outputs are 27,394 bytes / `13e34836…`, identical to committed/public PNG. |
| 7 | Final-Git browser JSON parsing, newline audit, screenshot inspection, and representative local-link checks | PASS — six cases, zero CRLF, 30/30 links, no overflow or hidden critical content. |
| 8 | Authenticated read-only GitHub REST/GraphQL/Pages checks plus public GET/HEAD checks | PASS except F4 — exact deploy/settings/public bytes; repository-card image remains fallback; mutation count zero. |
| 9 | Git ancestry/path/diff/tag checks and `git diff --check` | PASS — evidence-only current base, unchanged deployed implementation/tag, Reviewer write scope clean. |

## Public Output Bindings

| Route/artifact | HTTP | Bytes | SHA-256 |
|---|---:|---:|---|
| `/` | 200 | 33,669 | `64597def18f8777f92739d131649299c1639af1923f7cccde34b86d7ea61de21` |
| `/ru/` | 200 | 40,530 | `fef3499ecf2d5678a52fea4d1a93d51ce5d168d883652087bb02d776c144ec0f` |
| `/kk/` | 200 | 41,343 | `2d4465e7dc55856683247bf036f113380b452db1053424d82935dff81d4fba49` |
| `/sitemap.xml` | 200 | 338 | `79dcb9bbd3dda14054fe33695f89f6f62cdeea08881a427ec059d5e2d1665767` |
| `/data/communities.json` | 200 | 45,260 | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` |
| `/assets/css/catalog.css` | 200 | 2,035 | `6079176c27db6ced57ff8ad71c7671cbd694a13a39322566da4d2b9b3f157b6d` |
| `/assets/social-preview.png` | 200 | 27,394 | `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d` |
| `/robots.txt` | 404 | 9,379 | `b620507312c5e97566a3c6cfaf99144fefc18a0da7d941401dfa0f5f58fb0368` |
| `/llms.txt` | 404 | 9,379 | `b620507312c5e97566a3c6cfaf99144fefc18a0da7d941401dfa0f5f58fb0368` |

The refreshed `public-http.json` is 14,666 bytes / SHA-256
`133cd56811d202577b7f0dca9198a2ba0831d3702d232c317f31f8203af43bf8`.
The complete current browser matrix is 87,008 bytes / SHA-256
`35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`, canonical LF.
The supported build log is 5,899 bytes / SHA-256
`d03d372e69d73061fecd8a07b6ce03932a5c3a15c685fb25ccb6cc4ae92c65de`.

## Evidence Verification

| Ref | Acceptance boundary | Exists? | Claim established? |
|---|---|---|---|
| E1 | Supported Pages/Jekyll build and exact routes | ✅ | ✅ |
| E2 | Localized canonical/hreflang metadata | ✅ | ✅ |
| E3 | Dataset/social metadata and deterministic page asset | ✅ | ✅ for page output; repository-card custom upload is separately governed by E7 |
| E4 | Liquid sitemap; absent robots/llms | ✅ | ✅ |
| E5 | Responsive/browser matrix and screenshots | ✅ | ✅ |
| E6 | Phase A digest/body/test preservation | ✅ | ✅ |
| E7 | External publication/settings outcome | ✅ | ❌ repository-card custom preview remains generated fallback |
| E8 | Antigravity advisory provenance | ✅ | ✅ |
| E9 | Scope, attribution, and resumability | ✅ | ✅ |

## Antigravity Provenance Audit

- Executable: `C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`; 186,767,512 bytes; SHA-256
  `059b96c1069206158d340ee2a8912894eca5002195e62b8cd281c26c01cd794e`.
- Exact model `gemini-3.7-flash-high`; plan+sandbox; object-valued UTF-8 stream-json;
  request-review permissions; no permission-bypass flag; zero tool steps.
- Conversation `5f3edb10-3f79-4dbf-8aa8-2c3885dbc28c`; status `SUCCESS`.
- Prompt SHA-256 `e789f8d7301d0825a98a4c532121bdb4385affc31ae8f358cd96d038cdf960fb`.
- Input SHA-256 `aba88a1bcc48a36f7fd3ac06268c4464ae37965dc2c30b6e118dbbbabddde8ba`.
- Output SHA-256 `b560698faada053bc896d8da0a4ba106683e2fcbde96eb970c8f474fb0b07d86`.
- Response SHA-256 `7ce63b5f0a4207b1ebd7e153f55319933f6133432ffe46c86e3ed006fe28dbaf`;
  exact advisory `PASS`, disposition not required, findings none, nits none.

Antigravity is advisory. It does not replace this formal TFW judgment.

## Claim & Source Checks

| Claim | Primary evidence | Result |
|---|---|---|
| Approved Phase A body/digest contract is preserved | Actual Phase A RF/REVIEW, accepted Git base, current generated files/tests | ✅ Exact |
| Pages build is exact deployed repository candidate | Authenticated Pages build SHA plus public/local output hashes | ✅ Exact `bd7af421…` |
| Description/homepage/topics are applied | Authenticated read-only repository data | ✅ Exact |
| Custom repository-card preview is applied | Authenticated GraphQL `openGraphImageUrl` | ❌ Generated fallback remains |
| Existing dated tag is protected and no mutation occurred | Read-only remote tag objects and execution log | ✅ Exact |

## Knowledge Citations Verified

All 21 previously audited citations remain applicable and unchanged:

| Rows | Authorities | Result |
|---|---|---|
| PV0, PV1, PV1b | README purpose/non-goals; TFW values/success criteria | ✅ Resolve and match |
| PV2 | Optional `knowledge/philosophy.md` | ✅ Correctly absent; no fabricated citation |
| PV3a–PV3c | `KNOWLEDGE.md` D1, D11, D13 | ✅ Resolve and match |
| PV4a–PV4b | Conventions North Star and quality standard | ✅ Resolve and match |
| PV5–PV6 | Optional topic/process files | ✅ Correctly absent |
| PV7 | `knowledge/domain.md` F1–F2 | ✅ Resolve and match |
| PV8–PV17 | Jekyll/Pages, Google, IANA/RFC, Schema.org, W3C, GitHub, RFC 8785, URL Inspection/Playwright primary references | ✅ All ten resolve, meaning matches, and remain relevant |

Totals: 21/21 resolved or correctly recorded absent; 21/21 semantic checks pass; zero irrelevant or
hallucinated citations.

## Discrepancy

**F4 — material:** authenticated GitHub still exposes the generated repository Open Graph image.
The committed and public page-level asset is correct, but it does not prove the repository-card
custom-image setting. The official upload cannot proceed until the owner changes the Chrome
extension file-URL permission. The Reviewer neither changed that permission nor attempted an
unofficial endpoint.

## Harness / Session Deviations

- The harness interrupted the attempted fresh full live browser matrix after the public-root probe.
  The final-Git matrix, six images, public bytes, live root, and representative links supply the
  independent evidence used here. This is not a candidate finding.
- Handoff operation `exec-17c43827-2136-4159-a79d-2e68677e7636` transferred source
  `01a04383-b2eb-78b2-80e3-0b0fc62e00d9` to destination
  `01a04881-4c15-7f21-a3c9-4a50ddcf9daa`; all five steps completed and no `create_thread` call
  occurred. This is a harness/session identity deviation only.

## Checkpoint

**Self-check:**
- [x] Every current RF acceptance claim checked against exact files and independent output.
- [x] All 12 refreshed RF/EV/evidence paths and all 13 relevant implementation paths reviewed proportionally.
- [x] All nine evidence references and attachments checked.
- [x] Phase A approval, digest, tests, bodies, and frozen authority reverified.
- [x] Public GitHub/Pages state checked read-only; zero external mutation.
- [x] Sole blocker and both harness/session deviations classified precisely.

Stage complete: YES

# EV — 20260827-132641__catalog_discoverability / Phase B: Published Discovery

> **Date**: 2026-08-28
> **Author**: saubakirov (Codex Executor)
> **Task**: 20260827-132641__catalog_discoverability
> **TS**: [TS Phase B](../TS__phase-b__published_discovery.md)
> **Integrated pre-execution base**: `f97c890c98440a8442cc51e689c39b5d013da754`
> **Reviewed deployed SHA**: `bd7af42165c341d653e3efbb20091c131c9f7a40`
> **Approved Phase A base**: `d9fe27c6dce80008326fa8eb731d3aff40fd3726`

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 11 `10.0.26200`; PowerShell 5.1.26100.8655 |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1 |
| Deploy target | Public GitHub Pages project site at `https://saubakirov.github.io/KZ-IT-telegram-list/` |
| CI / Pipeline | Pages `legacy` build from `master` `/`; latest authenticated build is `built` at exact `bd7af421…` |
| Local build | Official `actions/jekyll-build-pages:v1.0.13` image at digest `sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041` |
| Browser | Existing six-case live Google Chrome matrix plus fresh authenticated Chrome Settings card inspection; no control activated |
| GitHub API | Authenticated read-only REST/GraphQL as `saubakirov`; credential value neither printed nor stored |
| Advisory | Existing bound Antigravity `gemini-3.7-flash-high` result; no rerun because visible copy, metadata, SVG, and PNG bytes are unchanged |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Exact deployed SHA rebuilds through the supported Pages surface; public EN/RU/KK, JSON, CSS, PNG, and sitemap bodies are byte-identical to that fresh build | Pinned Pages container plus public GET/HEAD | VERIFIED | `jekyll-build.txt`; `public-http.json` |
| E2 | AC-2 | Public EN/RU/KK have exact language, singleton title/description/canonical, and reciprocal `en`/`ru`/`kk`/`x-default` metadata; public parser output is byte-identical to local | Public route bodies and metadata parser | VERIFIED | `metadata-summary.json`; `public-http.json` |
| E3 | AC-3 | Public Open Graph, Twitter, Dataset JSON-LD, JSON distribution, and page-level preview point to the reviewed 1280×640 PNG; asset bytes and reproduction contract remain exact | Public route heads/assets plus prior deterministic raster proof | VERIFIED | `metadata-summary.json`; `public-http.json`; `social-preview-inspection.png`; `jekyll-build.txt` |
| E4 | AC-4 | Public Liquid sitemap is exactly the three canonical routes; project `robots.txt` and `llms.txt` return GET/HEAD 404 and are absent from the local build | Public GET/HEAD plus XML/local build assertions | VERIFIED | `public-http.json`; `jekyll-build.txt` |
| E5 | AC-5 | Fresh live EN/RU/KK cases at both exact viewports have no overflow, hidden critical content, scripts, clipping, or obstruction; type navigation works; exact observed links pass 30/30 | Live Chrome plus read-only HEAD checks | VERIFIED | `browser-matrix.json`; six fresh screenshots |
| E6 | AC-6 | Phase A digest/source/README/visible-body/target/fragment/test contract is unchanged; generator/schema gates and all 13 tests pass | Local immutable-base and Python checks | N/A | Deterministic gates below |
| E7 | AC-7 | Exact deploy/ref/build/settings/public/tag state is captured with zero Executor mutation; the owner-uploaded repository preview resolves to the exact reviewed PNG through authenticated GraphQL, HTTP, and visible Settings UI evidence | Authenticated GitHub REST/GraphQL and Chrome, Git history, public HTTP | VERIFIED | `external-checkpoint.md`; `public-http.json`; `repository-social-preview-settings.png` |
| E8 | AC-8 | Exact visible copy/metadata/asset bytes remain those formally approved and previously passed by the bound Antigravity advisory; refreshed deployed evidence is ready for the same Reviewer | Existing advisory and formal candidate REVIEW plus byte comparison | VERIFIED | `antigravity-input.txt`; `antigravity-output.jsonl`; `public-http.json` |
| E9 | AC-9 | This refresh changes only Executor-owned EV/RF/evidence; implementation remains the approved 13-path boundary, lifecycle remains `BLOCKED`, and forbidden Coordinator/Reviewer artifacts are untouched | Git path/role audit | N/A | RF and final Git audit |

## Verdict

Evidence verdict: 7/9 VERIFIED, 0 DEFERRED, 0 BLOCKED, 2 N/A

F4's evidence condition is satisfied, but this is not the formal Phase B verdict. Search Console
submission/index coverage remains explicitly DEFERRED and unauthorized. Phase status stays unchanged
under the Executor role lock until the same Reviewer judges this refreshed RF/EV.

## Deterministic gates and preservation

```text
python scripts/generate_readme.py --check
  -> All 4 catalog projections are generator-current
  -> locale payload sha256=51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc

python scripts/validate_schema.py
  -> 38 groups; 20 channels; 4 bots; 19 categories; 2 archive entries; errors=0

python -m unittest scripts.test_catalog_generation -v
  -> Ran 13 tests; OK
  -> all twelve Phase A predecessor tests remain present

python scripts/test_site_metadata.py --site <exact-deploy-build> --summary <local-summary>
  -> Built EN/RU/KK route structure is valid

python scripts/test_site_metadata.py --site <public-success-mirror> --summary <public-summary>
  -> Built EN/RU/KK route structure is valid
  -> public and local summaries are byte-identical

git diff --check
  -> no output
```

- Locale payload digest: exact approved
  `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`.
- README: 16,627 bytes / `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d`,
  byte-identical to Phase A.
- `data/communities.json`: 45,260 bytes /
  `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d`,
  byte-identical to Phase A and the public response.
- Stripped EN/RU/KK body hashes remain `c26880eb87025557b3426d870b04d6ef352cd610693c7cfaf6b40a6c57eaf038`,
  `127cf17b024367a3ac484ab29883db2b52d97e331e817f3b4880121f6c4d2d7e`, and
  `92b32502cf67768e58fd818a62d0da00375dfdd8db0a7ac418ea07b4f4b2d1f1`.

## Deployment, settings, and public-byte bindings

- Authenticated `master`: `bd7af42165c341d653e3efbb20091c131c9f7a40`.
- Exactly one local remote-tracking `update by push` reflog entry targets that SHA. Prior remote
  `e4986e787018dbe92f51733e243916eba60cd2c4` is its exact merge base/ancestor; authenticated
  comparison is ahead 43, behind 0.
- Latest Pages build: `built` at exact `bd7af421…`, created `2026-08-28T12:44:30Z`, updated
  `2026-08-28T12:45:02Z`, no error; source remains `master` `/`, HTTPS enforced.
- Description, homepage, and the exact sorted twelve-topic set match the authorized targets.
- Historical `data-2026-08-27` tag remains object
  `45d9c3cb12c1e71c7df7429f1da32028bcfbeb89`, peeled commit
  `ee2e4f8f69b7bfc66b905801f950d8e832caa02f`.

| Public output | Status | Bytes | SHA-256 | Exact deploy build |
|---|---:|---:|---|---|
| EN `/` | 200 | 33,669 | `64597def18f8777f92739d131649299c1639af1923f7cccde34b86d7ea61de21` | identical |
| RU `/ru/` | 200 | 40,530 | `fef3499ecf2d5678a52fea4d1a93d51ce5d168d883652087bb02d776c144ec0f` | identical |
| KK `/kk/` | 200 | 41,343 | `2d4465e7dc55856683247bf036f113380b452db1053424d82935dff81d4fba49` | identical |
| Sitemap | 200 | 338 | `79dcb9bbd3dda14054fe33695f89f6f62cdeea08881a427ec059d5e2d1665767` | identical |
| JSON | 200 | 45,260 | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` | identical |
| CSS | 200 | 2,035 | `6079176c27db6ced57ff8ad71c7671cbd694a13a39322566da4d2b9b3f157b6d` | identical |
| Page preview PNG | 200 | 27,394 | `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d` | identical |

GET and HEAD both returned 200 for those seven outputs. Project `robots.txt` and `llms.txt` both
returned GET/HEAD 404. The public sitemap contains exactly `/`, `/ru/`, and `/kk/`. Public JSON parses
as 38 groups, 20 channels, 4 bots, 19 categories, 2 archived entries, and
`last_updated=2026-08-27`.

`public-http.json` is canonical LF, 17,255 bytes, SHA-256
`2a5d501b9b9a0c66c246e2d66c08badfc749a893c484db1c8acf945e2565cdf0`.
`external-checkpoint.md` is 8,341 bytes, SHA-256
`dd859005a2024f43b505829a33e05aacff3524ec9a76d2ec0ef644e5ef3ea979`.
The refreshed `jekyll-build.txt` is 5,899 bytes, SHA-256
`d03d372e69d73061fecd8a07b6ce03932a5c3a15c685fb25ccb6cc4ae92c65de`.
The parsed metadata summary remains 11,097 bytes, SHA-256
`bbf30af0cdf5fbc26d547a80e97d9199035841e47b370cd2b0dc238a527f0552`.

## Live browser bindings

The browser supplied exact viewport, DOM/head/style/visibility/overflow, screenshot, and one-action
navigation facts. Its read-only page-evaluation scope did not expose `fetch`; the exact five hrefs
captured from each of the six live cases were therefore checked with 30 read-only HEAD requests before
canonical-LF serialization. All 30 returned 200.

The final canonical-LF `browser-matrix.json` is 87,008 bytes, SHA-256
`35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`, with zero CRLF pairs.

| Screenshot | Bytes | SHA-256 |
|---|---:|---|
| `browser-390x844-en.png` | 64,133 | `67cccfc84fb4d74dd34804157fd1fc05d87a99eb86376252b9a86e14a4d063f2` |
| `browser-390x844-ru.png` | 63,218 | `63dcb0b8b0d5fa5c9bbb964f8596ce2e76df559fbb7b59c0972d575adf7f062c` |
| `browser-390x844-kk.png` | 66,705 | `0d6ff536ed289c61f671b09635cb92c8b6841d38f21a384e95fc0c1377a1d2e8` |
| `browser-1366x768-en.png` | 98,772 | `3789e840b6306d697e68e65d971fb1b3892b8bb37cbd5a52c92521a7b02f63a4` |
| `browser-1366x768-ru.png` | 108,403 | `0a5f710c65db0c12a5fdee2d2ebc7183d54fd8d51a696ae4dd131af8c4548ad9` |
| `browser-1366x768-kk.png` | 106,523 | `2180c1fbcfb4770eaf605deff4e6000c40cfc590900a30bb8aeab2b3357179a9` |

All six screenshots were visually inspected. The required identity, promise, freshness, language,
type, and intent controls are legible without horizontal clipping; the matrix confirms the useful
first catalog entry after one type-navigation action.

## Social preview closure

The page-level `og:image` and `twitter:image` on every route resolve to the reviewed 200 PNG above.
The source remains 1,158 bytes /
`9f46ff6812ab2b22d852fb11321f9075ef6e53184f7d97df949ae93214d19d82`; the PNG and inspection
attachment remain byte-identical at 27,394 bytes /
`13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`. The exact CairoSVG 2.8.2
command and producing environment remain fully bound in `jekyll-build.txt`.

Authenticated GraphQL now returns the distinct non-fallback repository URL
`https://repository-images.githubusercontent.com/92145063/3d01cb70-f0b7-406e-b18e-82b18df39588`.
GET and HEAD both return 200 `image/png`; the response is 27,394 bytes / SHA-256
`13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d` and is byte-identical to
`assets/social-preview.png`. Fresh authenticated Chrome Settings inspection independently observed
that exact URL as the visible card's 640×320 computed background. The 955×510 attachment
`repository-social-preview-settings.png` is 30,121 bytes / SHA-256
`e9d158759aa3df45f2eeffde09bccb3c8aed362df3b4bbab30e8c1256860119d`.

The Coordinator delegation attributes the upload to the owner. This Executor only verified the
resulting state and did not activate the visible `Edit` control or perform an upload/settings action.

## Antigravity advisory record

No rerun was required: no visible copy, head metadata, Dataset field, SVG source, PNG byte, or proposed
setting string changed. The existing content-fed result remains bound to executable
`C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`, version 1.1.22, model
`gemini-3.7-flash-high`, plan+sandbox, object-valued UTF-8 stream-json, request-review permissions,
zero tool steps, and no bypass.

- Prompt: `e789f8d7301d0825a98a4c532121bdb4385affc31ae8f358cd96d038cdf960fb`.
- Input: 170,401 bytes / `aba88a1bcc48a36f7fd3ac06268c4464ae37965dc2c30b6e118dbbbabddde8ba`.
- Output: 3,342 bytes / `b560698faada053bc896d8da0a4ba106683e2fcbde96eb970c8f474fb0b07d86`.
- Conversation: `5f3edb10-3f79-4dbf-8aa8-2c3885dbc28c`; `SUCCESS`; `PASS`; findings none;
  nits none; disposition not required.
- Usage: 58,569 input, 7,096 output, 6,823 thinking, 0 cache-read, 65,665 total tokens.

Antigravity remains advisory and does not replace formal TFW review.

## No-mutation and continuation record

This Executor used authenticated read-only REST/GraphQL, public GET/HEAD, Git read-only probes, a
local exact-SHA build, and live browser reads only. There was no push, tag, release, deploy,
repository/Pages/settings change, upload, Search Console action, or other external mutation.

F4's custom-preview evidence condition is now satisfied. Phase B remains unchanged in task status
because this Executor cannot alter lifecycle authority; return this refreshed RF/EV to the same
Reviewer. Search Console remains separately DEFERRED and unauthorized. Complete publication is not
claimed before formal review.

## Attachments

| File | Description |
|---|---|
| `public-http.json` | Canonical-LF authenticated repository/Pages/ref/tag and exact public GET/HEAD/body/hash evidence |
| `external-checkpoint.md` | Human-readable deployed/settings state, F4 closure, tag, continuation, and no-mutation checkpoint |
| `jekyll-build.txt` | Original deterministic build/raster proof plus exact-SHA post-publication build comparison |
| `metadata-summary.json` | Exact local/public-identical route metadata and Dataset summary |
| `browser-matrix.json` | Canonical-LF six-case live Chrome DOM/head/overflow/navigation/link matrix |
| `browser-390x844-en.png` | Fresh live EN mobile viewport |
| `browser-390x844-ru.png` | Fresh live RU mobile viewport |
| `browser-390x844-kk.png` | Fresh live KK mobile viewport |
| `browser-1366x768-en.png` | Fresh live EN desktop viewport |
| `browser-1366x768-ru.png` | Fresh live RU desktop viewport |
| `browser-1366x768-kk.png` | Fresh live KK desktop viewport |
| `social-preview-inspection.png` | Byte-identical final page-preview visual-inspection attachment |
| `repository-social-preview-settings.png` | Fresh authenticated GitHub Settings card showing the owner-uploaded custom preview |
| `antigravity-input.txt` | Existing complete content-fed advisory input |
| `antigravity-output.jsonl` | Existing object-valued stream-json advisory output |

---

*EV — 20260827-132641__catalog_discoverability / Phase B: Published Discovery | 2026-08-28*

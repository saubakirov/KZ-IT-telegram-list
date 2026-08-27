# EV — 20260827-132641__catalog_discoverability / Phase B: Published Discovery

> **Date**: 2026-08-27
> **Author**: saubakirov (Codex Executor)
> **Task**: 20260827-132641__catalog_discoverability
> **TS**: [TS Phase B](../TS__phase-b__published_discovery.md)
> **Approved handoff**: `4776edfa29304eb0955393af6f288a654fdac822`
> **Approved Phase A base**: `d9fe27c6dce80008326fa8eb731d3aff40fd3726`

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows NT 10.0.26200.0 |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1; PowerShell; CairoSVG 2.8.2 |
| Deploy target | Local production Jekyll build only; no deployment or publication |
| CI / Pipeline | Official GitHub-maintained `actions/jekyll-build-pages:v1.0.13` image at immutable digest `sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041`; Docker 24.0.6 |
| Pages runtime | Ruby 3.3.4; Bundler 2.5.11; `github-pages` 232; Jekyll 3.10.0; `jekyll-sitemap` 1.4.0 installed transitively but intentionally not enabled |
| Browser | Codex in-app Chromium browser against read-only localhost build |
| Advisory | Antigravity CLI `agy.exe`; exact `gemini-3.7-flash-high`; plan+sandbox |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Root-source candidate built successfully with the supported Pages dependency; one layout produced exactly EN/RU/KK routes plus the repository-owned sitemap; no built `robots.txt` | Pinned official Pages container | VERIFIED | `jekyll-build.txt` |
| E2 | AC-2 | Exact locale, singleton title/description/canonical, and reciprocal `en`/`ru`/`kk`/`x-default` alternates on all built routes | Local parsed built HTML | N/A | `metadata-summary.json` |
| E3 | AC-3 | Exact Open Graph, Twitter, Dataset JSON-LD, JSON distribution, and final 1280×640 preview bytes/text | Local parser plus final-byte image viewer | VERIFIED | `metadata-summary.json`; `social-preview-inspection.png` |
| E4 | AC-4 | Built sitemap contains exactly canonical `/`, `/ru/`, `/kk/`; source and build contain no project `robots.txt` or `llms.txt` | Supported build plus XML assertion | N/A | `metadata-summary.json`; `jekyll-build.txt` |
| E5 | AC-5 | EN/RU/KK at 390×844 and 1366×768 have zero horizontal overflow, zero hidden critical elements, zero executable/external scripts, loaded CSS, working representative links, and a one-action type jump that leaves the first entry in view | In-app Chromium browser | VERIFIED | `browser-matrix.json`; six screenshots |
| E6 | AC-6 | Phase A digest, source facts, README bytes, visible bodies, all targets/fragments, and all twelve predecessor tests are preserved; one preservation test was added and 13/13 pass | Local Python/Git immutable-base comparison | N/A | Commands and hashes below |
| E7 | AC-7 | Current repository/Pages/settings/public state captured through authenticated read-only APIs and public HTTP; exact proposed settings and later runbook recorded; every post-deploy outcome remains deferred | GitHub REST/GraphQL, Pages HTTP, `git ls-remote` | DEFERRED | `external-checkpoint.md` |
| E8 | AC-8 | Exact final content-fed copy/metadata bundle received `PASS`, no findings, no nits from pinned Antigravity in request-review permission mode, with object-valued UTF-8 NDJSON and no tool calls or permission bypass | Antigravity CLI | VERIFIED | `antigravity-input.txt`; `antigravity-output.jsonl` |
| E9 | AC-9 | Implementation stays at the Coordinator-revised 13-path boundary (8 new, 5 modified), and all evidence is task-local; formal REVIEW remains outside Executor ownership | Git/path/role audit | N/A | Scope record below |

## Verdict

Evidence verdict: 4/9 VERIFIED, 1 DEFERRED, 0 BLOCKED, 4 N/A

This verdict covers the repository-controlled candidate only. Formal acceptance belongs to the
existing Reviewer task. Public deployment, settings effects, indexing, search visibility, and
retrieval remain deferred pending explicit authorization.

## Deterministic gates

```text
python scripts/generate_readme.py --check
  -> All 4 catalog projections are generator-current
  -> locale payload sha256=51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc

python scripts/validate_schema.py
  -> 38 groups; 20 channels; 4 bots; 19 categories; 2 archive entries; errors=0

python -m unittest scripts.test_catalog_generation -v
  -> Ran 13 tests; OK
  -> original Phase A test-name set is an asserted subset of the current suite

python scripts/test_site_metadata.py --site _site --summary evidence/metadata-summary.json
  -> Built EN/RU/KK route structure is valid

git diff --check
  -> no output
```

Exact preservation bindings:

- README: 16,627 bytes, SHA-256 `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d`, byte-identical to Phase A.
- `data/communities.json`: SHA-256 `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d`, byte-identical to Phase A.
- Locale payload: exact approved digest `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`.
- Stripped EN body: SHA-256 `c26880eb87025557b3426d870b04d6ef352cd610693c7cfaf6b40a6c57eaf038`, byte-identical to Phase A.
- Stripped RU body: SHA-256 `127cf17b024367a3ac484ab29883db2b52d97e331e817f3b4880121f6c4d2d7e`, byte-identical to Phase A.
- Stripped KK body: SHA-256 `92b32502cf67768e58fd818a62d0da00375dfdd8db0a7ac418ea07b4f4b2d1f1`, byte-identical to Phase A.

## Build and metadata bindings

- Built EN: 33,669 bytes; SHA-256 `64597def18f8777f92739d131649299c1639af1923f7cccde34b86d7ea61de21`.
- Built RU: 40,530 bytes; SHA-256 `fef3499ecf2d5678a52fea4d1a93d51ce5d168d883652087bb02d776c144ec0f`.
- Built KK: 41,343 bytes; SHA-256 `2d4465e7dc55856683247bf036f113380b452db1053424d82935dff81d4fba49`.
- Built sitemap: 338 bytes; SHA-256 `79dcb9bbd3dda14054fe33695f89f6f62cdeea08881a427ec059d5e2d1665767`.
- Metadata summary: SHA-256 `84f36a217871ab6ad4116e8077902c4c3d726f1fea7489016ab8e9e96e96e547`.
- Final CSS: 2,035 bytes; SHA-256 `6079176c27db6ced57ff8ad71c7671cbd694a13a39322566da4d2b9b3f157b6d`.

## Browser and asset bindings

`browser-matrix.json` SHA-256 is
`b83d6fdcbda447a0baa810b13bca8542b29f2e67becc54087a1fc9ba9fccb025`.
Every matrix case reports its exact viewport, DOM rectangles, head counts, local response checks,
overflow/visibility/script facts, screenshot byte count, and post-click fragment/entry position.

| Screenshot | SHA-256 |
|---|---|
| `browser-390x844-en.png` | `76b3e944089d80a0885964c301338b426bd99510bc47fe26fb9d387437a6b1ab` |
| `browser-390x844-ru.png` | `f3d7f090841c933a68021d700671949a265e6c71af606cdba57a5e77aafe82ed` |
| `browser-390x844-kk.png` | `9647f0ac5409a20cbc923567a1e640a9d557ba43ebf71a1a136fcfa164e2ec0d` |
| `browser-1366x768-en.png` | `0516e47f42a98279c6d19324d5ce83072029e6225f9e5430176971fecaa9ce5e` |
| `browser-1366x768-ru.png` | `a2a623b09cf435b997eea15c79a02692e3ab43092dccb0f53a26d8c9b9e76396` |
| `browser-1366x768-kk.png` | `d1f2adc666d454013ec05cbcace4a84c5e14d9c0a76316808a6af1a6301434ff` |

The deterministic vector source is 1,158 bytes, SHA-256
`9f46ff6812ab2b22d852fb11321f9075ef6e53184f7d97df949ae93214d19d82`.
CairoSVG 2.8.2 produced a 24-bit RGB PNG at exactly 1280×640, 27,391 bytes, SHA-256
`323c124343db406b32170dfa9fe6ec18e5d14479f57691dc6b638f99df2ce9c5`.
Final-byte inspection confirmed legible unclipped text and no counts, dates, ranking, verification,
publisher, or other unsupported claim. The inspection attachment is byte-identical to the PNG.

The repository-local image workflow selected deterministic SVG plus raster output because exact
typography is load-bearing; AI bitmap generation was correctly not used for this code-native asset.

## Antigravity advisory record

Installed-surface discovery:

- `agy.exe --help` exposed `--model`, `--mode`, `--sandbox`, `--input-format`,
  `--output-format`, `--print-timeout`, and the disabled-by-contract
  `--dangerously-skip-permissions` option.
- `agy.exe models` exposed exact `gemini-3.7-flash-high` (`Gemini 3.7 Flash (High)`); no fallback.

Invocation contract: executable `C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`; model
`gemini-3.7-flash-high`; `--mode plan`; `--sandbox`; `--input-format stream-json`;
`--output-format stream-json`; `--print-timeout 15m`; no permission-bypass flag. The input was one
UTF-8 object-valued `user` event containing complete built EN/RU/KK HTML bytes, sitemap, config,
layout, CSS, SVG source, artifact hashes, PNG facts, README binding, catalog binding, and locale digest.

- Prompt content: 127,190 bytes; SHA-256 `722e0e1b5dffe7a4c33925a79bd55342f12da51f9e19916d201ea0c0687af759`.
- Input NDJSON: 132,079 bytes; SHA-256 `c74627cd6ba8800287a4604420af6c7f8a549577b7d3fc0fa2d4b9480a0f46ef`.
- Output NDJSON: 3,168 bytes, six object-valued lines; SHA-256 `0b9bb339c374d64950f2fa74246b4f90cbc973199d57dce95e98eead6e497a09`.
- Conversation: `4e1d1d0d-5343-4cee-a6a4-840088a02947`; status `SUCCESS`; permission mode `request-review`; tool steps `0`.
- Usage: input 57,547; output 8,513; thinking 8,240; cache-read 0; total 66,060 tokens.
- Response SHA-256: `7ce63b5f0a4207b1ebd7e153f55319933f6133432ffe46c86e3ed006fe28dbaf`.
- Advisory: `VERDICT: PASS`; `DISPOSITION_REQUIRED: NO`; `FINDINGS: NONE`; `NITS: NONE`.
- Disposition: no material finding or nit exists; no source change is requested or accepted.

Antigravity is advisory evidence only and does not replace the formal TFW Reviewer.

## Coordinator revision and no-mutation record

The initial plugin-backed sitemap approach was abandoned after the Coordinator identified that
`jekyll-sitemap` 1.4.0 unavoidably emits project-path `robots.txt`, contradicting RES-1 D7 and the
approved no-robots outcome. Under the owner-preauthorized Coordinator revision, the final candidate
does not enable that plugin, owns `sitemap.xml` as a Jekyll/Liquid source page, asserts exactly three
URLs, and emits no `robots.txt`. The revised implementation budget is 13 paths, 8 new and 5 modified.
The Executor did not edit HL or TS.

Authenticated read-only GitHub API, public GET, Antigravity advisory, and `git ls-remote` calls caused
zero external mutations. There was no push, tag, release, deploy, Pages-source/settings edit,
description/homepage/topics/social-preview mutation, upload, Search Console action, or other external
write. Exact proposed settings and later authorization/public-verification steps are in
`external-checkpoint.md`; all public outcomes remain deferred.

## Attachments

| File | Description |
|------|-------------|
| `browser-390x844-en.png` | EN mobile viewport |
| `browser-390x844-ru.png` | RU mobile viewport |
| `browser-390x844-kk.png` | KK mobile viewport |
| `browser-1366x768-en.png` | EN desktop viewport |
| `browser-1366x768-ru.png` | RU desktop viewport |
| `browser-1366x768-kk.png` | KK desktop viewport |
| `social-preview-inspection.png` | Byte-identical final social-preview visual-inspection attachment |

---

*EV — 20260827-132641__catalog_discoverability / Phase B: Published Discovery | 2026-08-27*

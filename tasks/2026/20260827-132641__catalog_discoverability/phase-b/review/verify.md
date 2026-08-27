# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Min verify ratio:** 0.42
> **RF implementation files claimed:** 13
> **Initial files required:** `ceil(13 × 0.42) = 6`
> **Actual implementation files opened:** 13/13 (100%; discrepancies triggered full verification)
> **Reviewed base:** `ae4898df0b0b5050cf6f23179d4e090ff04f93db`

## Verification Log

| # | File | RF claim | Actual | Match |
|---|---|---|---|---|
| V1 | `Gemfile` | Supported Pages dependency pinned | Pins `github-pages` exactly to 232 | ✅ |
| V2 | `_config.yml` | Root-source Pages config and exclusions | Exact `url`/`baseurl`, strict front matter, and trace/tool exclusions; no sitemap plugin enabled | ✅ |
| V3 | `_layouts/default.html` | One localized semantic head/layout | Singleton title/description/canonical, four alternates, OG/Twitter, Dataset JSON-LD, one stylesheet, no executable JS | ✅ |
| V4 | `assets/css/catalog.css` | Restrained responsive presentation | 146-line static stylesheet with system fonts, focus-visible state, overflow-safe tables, mobile rule, and reduced-motion handling | ✅ |
| V5 | `assets/social-preview.svg` | Deterministic editable 1280×640 source | Exact dimensions/text and a documented CairoSVG 2.8.2 command are present | ⚠️ Partial — see F1 |
| V6 | `assets/social-preview.png` | Reproducible 1280×640 raster, 27,391 bytes | Valid 1280×640 RGB PNG, 27,391 bytes, hash `323c1243…`, legible and claim-safe; documented regeneration does not reproduce it | ❌ F1 |
| V7 | `sitemap.xml` | Repository-owned Liquid sitemap | Checked-in front matter/Liquid emits only canonical EN/RU/KK URLs | ✅ |
| V8 | `scripts/generate_readme.py` | Add Phase B route/head inputs without changing approved body | Adds the projection/front-matter model while retaining one source renderer; Phase A preservation test and immutable-base comparison pass | ✅ |
| V9 | `scripts/test_catalog_generation.py` | Extend, never weaken, twelve Phase A tests | Diff from Phase A adds constants/helpers and one preservation test; no predecessor test definition is removed or changed; 13/13 pass | ✅ |
| V10 | `scripts/test_site_metadata.py` | Built route/head/sitemap/Dataset/social/asset assertions | 393-line independent parser validates the claimed route and metadata contract, but validates asset dimensions/bytes only and does not reproduce SVG→PNG | ⚠️ Partial — see F1 |
| V11 | `index.md` | Generated EN front matter with Phase A-equivalent body | Exact Phase B front matter; stripped body and digest preservation gate pass | ✅ |
| V12 | `ru/index.md` | Generated RU front matter with Phase A-equivalent body | Exact Phase B front matter; stripped body and digest preservation gate pass | ✅ |
| V13 | `kk/index.md` | Generated KK front matter with Phase A-equivalent body | Exact Phase B front matter; stripped body and digest preservation gate pass | ✅ |

Implementation scope is exactly 13 paths: 8 added and 5 modified. Text delta is 789 additions and
6 deletions (795 total); the binary PNG is counted as one added path. `data/communities.json` and
`README.md` are byte-identical to the approved Phase A base
`d9fe27c6dce80008326fa8eb731d3aff40fd3726`.

## Acceptance-Criteria Verification

| AC | Independent result | Evidence |
|---|---|---|
| AC-1 | ✅ Holds | Fresh build from the exact reviewed commit archive passed in GitHub's pinned `jekyll-build-pages` image; EN/RU/KK are the only HTML catalog routes and share one layout/stylesheet. |
| AC-2 | ✅ Holds | Fresh metadata test and six browser cases confirm exact `lang`, self-canonical, and reciprocal `en`/`ru`/`kk`/`x-default` singleton links on every route. |
| AC-3 | ❌ Does not fully hold | Dataset and social fields match visible/source facts, and the PNG is valid/legible, but the checked-in raster is not reproduced by its documented CairoSVG 2.8.2 command (F1). |
| AC-4 | ✅ Holds | Fresh sitemap is 338 bytes with exactly three canonical URLs; source/build/local HTTP have no project `robots.txt` or `llms.txt`. |
| AC-5 | ✅ Holds | Independent in-app Chromium QA at 390×844 and 1366×768 for all locales found no horizontal overflow, hidden critical content, or executable scripts; one visible type action brings the first entry into view. |
| AC-6 | ✅ Holds | Digest remains exactly `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`; schema/generator/13 tests pass; prior data/README/bodies/tests are preserved. |
| AC-7 | ✅ Holds within repository boundary | Authenticated current state, exact target settings, safe publication runbook, existing-tag non-reuse, and zero mutations are recorded; every public outcome remains correctly DEFERRED. |
| AC-8 | ⚠️ Advisory half holds; formal criterion pending | Antigravity provenance and PASS are exact. This formal review cannot approve while F1–F3 remain. |
| AC-9 | ⚠️ Scope holds; trace integrity does not | Scope/history/clean-base requirements hold, but the stale Phase HL plugin sentence (F3) and incorrect evidence hash binding (F2) make the continuation trace internally inconsistent. |

## Commands Executed

| # | Command / operation | Result |
|---|---|---|
| 1 | `python scripts/validate_schema.py` | PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archived; zero errors; digest exact. |
| 2 | `python scripts/generate_readme.py --check` | PASS — all four projections current; digest exact. |
| 3 | `python -m unittest scripts.test_catalog_generation -v` | PASS — 13/13, including the new Phase A preservation contract. |
| 4 | Immutable-base Git diffs and `git diff --check` | PASS — Phase A data/README unchanged; 13-path budget exact; frozen Master HL sections unchanged from `00a21bb9e1475568a9baef4a9be3b0a8e72e383e`. |
| 5 | Pinned official Pages container build from `git archive ae4898…` | PASS — Ruby 3.3.4, Bundler 2.5.11, Jekyll 3.10.0; fresh EN/RU/KK/sitemap/CSS/PNG hashes match EV. A preliminary read-only source bind was unsuitable because Bundler writes `Gemfile.lock`; the exact archive build is the authoritative rerun. |
| 6 | `python scripts/test_site_metadata.py --site <fresh-site>` | PASS — routes, heads, Dataset, target/fragment parity, sitemap, asset shape, and absent robots/llms. |
| 7 | Local HTTP checks for `/`, `/ru/`, `/kk/`, sitemap, JSON, robots, llms | 200/200/200/200/200/404/404. |
| 8 | In-app Chromium, EN/RU/KK × 390×844 and 1366×768 | PASS — exact viewport and DOM/navigation checks; screenshots visually inspected. |
| 9 | `python -m cairosvg assets/social-preview.svg -o <temp>.png -s 1` with CairoSVG 2.8.2 | FAIL contract — repeat runs are stable at 27,394 bytes / `13e34836…`, but differ from the checked-in 27,391-byte / `323c1243…` PNG by 72 pixels (maximum channel delta 19). |
| 10 | SHA-256 audit of all Phase B evidence attachments | F2 — every asserted attachment hash checked; `browser-matrix.json` is `7ea6616a…`, not EV's `b83d6fdc…`. |
| 11 | Authenticated GitHub REST GET, public HTTP GET, and `git ls-remote` | Current state matches the checkpoint; zero mutation. |
| 12 | Antigravity NDJSON/provenance/hash audit | PASS — exact executable/model/mode/sandbox/permissions/conversation and prompt/input/output bindings; no findings/nits. |
| 13 | HL/ONB knowledge-citation resolution and official-source checks | 21/21 citation rows semantically checked; 9/9 local targets resolve and all 20 unique official endpoints returned 200 (one transient retry). |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | Phase A approved body/digest contract is unchanged | TS AC-6; RF §§2–4 | Phase A RF + final REVIEW, immutable base `d9fe27c6…`, generator tests, current artifacts | ✅ Exact digest `51db402d…`; prior twelve tests extended, not weakened |
| C2 | Repository-owned Liquid sitemap is supported and avoids project robots output | Revised Phase B HL/TS; RF §§2–4 | Coordinator revision `b08d0f1…`, Jekyll source, pinned supported build, Google/RFC primary guidance | ✅ Implementation/output holds; Phase HL retains one contradictory plugin sentence (F3) |
| C3 | Current Pages/repository/public state is unchanged and no tag/settings mutation occurred | TS AC-7; external checkpoint; RF boundary | Authenticated GitHub GETs, public HTTP bytes, `git ls-remote` | ✅ `master=e4986e…`; Pages legacy `master:/`; tag ref `45d9c3…` (peeled commit `ee2e4f8…`); public RU/KK/sitemap still 404 |
| C4 | Preview is reproducibly generated from the checked-in vector | TS AC-3; RF §§1–4; EV | Checked-in SVG command and independent CairoSVG 2.8.2 rerender | ❌ F1 |

## Discrepancies Found

### F1 — Preview raster is not reproducible by its checked-in command (material)

`assets/social-preview.svg` instructs `python -m cairosvg ... -s 1`, and RF/EV claim CairoSVG 2.8.2
reproducibility. On the reviewed host, that exact command with CairoSVG 2.8.2 produces stable bytes
`13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d` (27,394 bytes), not checked-in
`323c124343db406b32170dfa9fe6ec18e5d14479f57691dc6b638f99df2ce9c5` (27,391 bytes). Pixel comparison
finds 72 changed pixels within the text raster (maximum channel delta 19). The visual asset is good,
but the acceptance/evidence claim is not established. Pin and document the complete producing
environment or regenerate the raster through the documented method, then rerun every affected hash,
metadata, visual, advisory, EV, and RF binding.

### F2 — EV binds `browser-matrix.json` to a nonexistent hash (material evidence defect)

EV records `b83d6fdcbda447a0baa810b13bca8542b29f2e67becc54087a1fc9ba9fccb025`, while the reviewed file is
`7ea6616ad428e74530015b14e984ffc4c84ff2ef38820e5a81d641041049da48` (67,908 bytes). Both the Executor
commit `07bf62b…` and integrated commit `5217d92…` contain the latter bytes; no committed version of
this path has the asserted EV hash. The matrix content independently passes, but the durable byte
binding must be corrected by the Executor and re-audited.

### F3 — Phase B HL still states the rejected plugin produces the sitemap (material trace defect)

The Coordinator revision correctly changes Phase B HL §§2, 4, and 8 and the TS to the
repository-owned Liquid sitemap, but Phase B HL §3 still says, “The sitemap is produced by the
supported GitHub Pages plugin.” That directly contradicts the final architecture and could cause a
future continuation to re-enable the rejected plugin and recreate the forbidden project robots
surface. The Coordinator must correct this free, derived Phase HL sentence; the Reviewer role lock
forbids editing it here.

## Evidence Verification

| # | RF evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 / AC-1 | EV + `jekyll-build.txt` | ✅ | ✅ Fresh supported build matches recorded output |
| E2 / AC-2 | Deterministic built-output assertions | ✅ Inline/test | ✅ Exact head contract independently verified |
| E3 / AC-3 | `metadata-summary.json`; preview inspection | ✅ | ❌ Metadata/visual facts hold, but SVG→PNG reproducibility does not (F1) |
| E4 / AC-4 | Metadata summary + build log | ✅ | ✅ Exact sitemap/no robots/no llms |
| E5 / AC-5 | `browser-matrix.json`; six screenshots | ✅ | ⚠️ Contents/screenshots independently pass; EV byte binding is wrong (F2) |
| E6 / AC-6 | Commands and hashes in EV | ✅ | ✅ Digest/body/data/README/test preservation exact |
| E7 / AC-7 | `external-checkpoint.md` | ✅ | ✅ Correctly DEFERRED; fresh read-only state matches |
| E8 / AC-8 | Antigravity input/output | ✅ | ✅ Exact PASS/no findings/no nits provenance verified |
| E9 / AC-9 | Git/path/role audit | ✅ | ⚠️ Scope holds; F2/F3 reduce trace integrity |

Evidence artifacts: 9/9 references exist; 6 fully match, 2 partially match, 1 fails its offered
reproducibility claim. Because discrepancies exist, all 13 implementation files and all attachments
were verified.

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Resolves / exists | Meaning matches? | Relevant? |
|---|---|---|---|---|---|
| 1 | HL/ONB | PV0 — `README.md` Purpose and four non-goals | ✅ | ✅ Accuracy/generated ownership/exact-count boundary | ✅ |
| 2 | HL/ONB | PV1 — `.tfw/README.md` Methodology values | ✅ | ✅ Candor, structural gates, portability | ✅ |
| 3 | HL/ONB | PV1b — `.tfw/README.md` Success Criteria 4 | ✅ | ✅ Complete, usable, inspectable result | ✅ |
| 4 | HL/ONB | PV2 — optional `knowledge/philosophy.md` absent | ✅ absence | ✅ No citation fabricated | ✅ |
| 5 | HL/ONB | PV3a — `KNOWLEDGE.md` D1 | ✅ | ✅ JSON plus generator owns content | ✅ |
| 6 | HL/ONB | PV3b — `KNOWLEDGE.md` D11 | ✅ | ✅ Purpose/non-goals remain data-owned | ✅ |
| 7 | HL/ONB | PV3c — `KNOWLEDGE.md` D13 | ✅ | ✅ Freshness reported, not schema-enforced | ✅ |
| 8 | HL/ONB | PV4a — Conventions §3 Project North Star | ✅ | ✅ Purpose/non-goals prevent excess surfaces | ✅ |
| 9 | HL/ONB | PV4b — Conventions §11 Quality Standard | ✅ | ✅ No placeholders/manual cleanup | ✅ |
| 10 | HL/ONB | PV5–6 — optional convention/process topic files absent | ✅ absence | ✅ Existing authorities used | ✅ |
| 11 | HL/ONB | PV7 — `knowledge/domain.md` F1–F2 | ✅ | ✅ Archive facts preserved | ✅ |
| 12 | HL/ONB | PV8 — Jekyll front matter/permalinks/Pages dependencies | ✅ | ✅ Jekyll/Liquid/root source is supported; plugin is transitive but disabled | ✅, with F3 trace correction required |
| 13 | HL/ONB | PV9 — Google localized pages/sitemaps | ✅ | ✅ Self canonicals and reciprocal alternates/sitemap | ✅ |
| 14 | HL/ONB | PV10 — Google AI guidance/OpenAI crawler roles | ✅ | ✅ Ordinary visible clarity; no AI promise | ✅ |
| 15 | HL/ONB | PV11 — IANA `kk` and RFC 9309 | ✅ | ✅ `kk`; host-root robots semantics | ✅ |
| 16 | HL/ONB | PV12 — Google/Schema.org Dataset/DataDownload | ✅ | ✅ Bounded real JSON distribution | ✅ |
| 17 | HL/ONB | PV13 — W3C language declarations | ✅ | ✅ Exact route language, not quality certification | ✅ |
| 18 | HL/ONB | PV14 — GitHub rendered content/anchors | ✅ | ✅ Explicit stable IDs and target parity | ✅ |
| 19 | HL/ONB | PV15 — Pages sources/local testing | ✅ | ✅ Authenticated source and supported local build | ✅ |
| 20 | HL/ONB | PV16 — RFC 8785 | ✅ | ✅ Canonical locale approval payload | ✅ |
| 21 | HL/ONB | PV17 — URL Inspection/Playwright assertions | ✅ | ✅ Local executable checks; public indexing deferred | ✅ |

Citation totals: 21 rows checked; 21 resolved or correctly documented as absent; 21 semantically
verified; 0 irrelevant; 0 hallucinated. The independent PV scan covered PV0–PV4 in full and PV7 by
relevance; optional PV2/PV5/PV6 files are absent as recorded.

## Checkpoint

**Self-check:**
- [x] Opened 13/13 claimed implementation files, exceeding `ceil(13 × 0.42) = 6`; discrepancies escalated verification to 100%.
- [x] Ran build, unit, schema, generation, metadata, browser, rasterization, hash, Git, and read-only external checks.
- [x] Claim/source checks include the approved digest, sitemap architecture, primary GitHub state, and raster reproducibility.
- [x] Verified every RF §3 acceptance claim against actual files and independent output.
- [x] Checked `KNOWLEDGE.md`; no implementation contradiction exists.
- [x] Verified all 21 HL §7.2 / ONB §7 citation rows: 21 resolved/legitimate absences, 21 semantic matches, 0 irrelevant, 0 hallucinated.
- [x] Verified all 9 RF §5 evidence references: 9 exist, 6 fully match, 2 partially match, 1 fails the offered claim.

Stage complete: YES

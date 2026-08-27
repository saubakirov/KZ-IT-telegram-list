# TS — 20260827-132641__catalog_discoverability / Phase B: Published Discovery Surface

> **Date**: 2026-08-27
> **Author**: Coordinator (Codex)
> **Status**: ✅ APPROVED — owner mandate, 2026-08-27
> **Parent Phase HL**: [Phase B HL](HL__phase-b__published_discovery.md)
> **Parent Master HL**: [Master HL](../HL-20260827-132641__catalog_discoverability.md)
> **Predecessor facts**: [Phase A RF](../phase-a/RF__phase-a__multilingual_catalog.md) · [Phase A REVIEW](../phase-a/REVIEW__phase-a__multilingual_catalog.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) · [Iteration 2 RES](../research/iter2/RES.md)
> **Mode**: AG for repository-controlled implementation, local build/browser QA, read-only public/settings inspection, advisory Antigravity review, revision, and formal local acceptance
> **Approval boundary**: No push, tag, release, publication, GitHub settings/Pages mutation, Search Console submission, upload, or other external mutation. Stop at the exact authorization/public-evidence checkpoint.

---

## 1. Objective

Deliver a formally reviewed, release-ready repository candidate for the multilingual GitHub Pages
discovery surface. The candidate adds one supported Jekyll layout/head, self-canonical and reciprocal
language metadata, a supported sitemap, accurate Dataset and social metadata, a reproducible preview
asset, restrained responsive CSS, and deterministic/local-browser evidence while preserving the
approved Phase A body and locale digest. External settings, push, deployment, and public verification
remain explicit later operations requiring authorization.

## 2. Scope

### In Scope

- Preserve the approved Phase A locale payload digest
  `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`, catalog facts,
  visible copy, intent membership, destinations, and body contract.
- Generate the minimum per-route front matter required by one repository-owned Jekyll layout.
- Give `/`, `/ru/`, and `/kk/` correct document language, localized title/description, self-canonical,
  reciprocal `hreflang` (`en`, `ru`, `kk`, and English `x-default`), and consistent Open Graph/Twitter metadata.
- Emit visible-content-consistent Schema.org `Dataset`/`DataDownload` JSON-LD whose distribution is
  the existing public `data/communities.json` and whose language/date/license/scope agree with the page.
- Generate `sitemap.xml` as a supported Jekyll/Liquid page and restrict it to the intended three
  public catalog routes without the project-path `robots.txt` side effect of `jekyll-sitemap` 1.4.0.
- Add one static semantic layout and restrained responsive CSS; no client-side application or runtime.
- Create a deterministic 1280×640 social-preview PNG under 1 MB plus its editable vector source.
- Extend, never replace or weaken, the Phase A deterministic tests; add exact built-output/head/sitemap checks.
- Build locally with the supported GitHub Pages dependency and inspect all three routes in the in-app
  browser at 390×844 and 1366×768, including representative type/intent/language navigation.
- Run the installed Antigravity CLI on the final visible copy and metadata after discovering its
  actual help/model surface; use `C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`, model
  `gemini-3.7-flash-high`, plan+sandbox, object-valued UTF-8 stream-json I/O, complete content-fed
  bytes, and no permission bypass. Bind prompts/results to exact hashes and disposition every finding.
- Record current read-only GitHub/Pages state, exact target settings/assets, and a precise
  publication/public-verification runbook without applying any external change.
- Produce Phase B ONB, evidence, and RF through `/tfw-handoff`, then one formal `/tfw-review` verdict.

### Out of Scope

- Any push, force-push, tag, release, deployment, GitHub Pages source/settings change, repository
  description/homepage/topics/social-preview mutation, file upload, Search Console submission, or
  other external mutation.
- Claiming the local candidate is already public, indexed, ranked, cited by an AI system, or visible
  in a social preview.
- Any locale copy change without returning through the complete Phase A digest/advisory/formal-review contract.
- Telegram liveness/member-count refresh, entry addition/removal/archive/identity changes, or any
  other live catalog-fact mutation.
- `llms.txt`, project-path `robots.txt`, keyword/query pages, custom Actions build, client-side search,
  analytics, web application, CMS, JavaScript navigation, or another catalog/data source.
- Replacing the approved generator or tests with an independent site-content build pipeline.
- Treating Antigravity as the formal TFW Reviewer or as authority to approve metadata/copy.

## 3. Principles Check

| # | Principle (from Master HL §7) | Enforced by | Gate |
|---|-------------------------------|-------------|------|
| P1 | Subtract before adding | AC-1, AC-4, AC-9 | One layout/stylesheet/asset, exact route set, no speculative surface |
| P2 | Accuracy before reach | AC-2, AC-3, AC-6 | Visible-copy parity, exact metadata, no catalog-fact or locale-digest change |
| P3 | One truth, many projections | AC-1, AC-2, AC-6 | Generated route fields and one layout derive from the approved source |
| P4 | People first, machines through clarity | AC-3, AC-4, AC-5 | Visible navigation and readable layout align with crawler/social/Dataset fields |
| P5 | Narrow is valuable | AC-3, AC-7 | Metadata/settings describe only Kazakhstan IT/startup Telegram scope |
| P6 | Measure what is controllable | AC-5, AC-6, AC-8 | Deterministic build/browser/hash evidence; external results explicitly deferred |
| P7 | Three languages, one experience | AC-1, AC-2, AC-5 | Reciprocal routes, localized head, body parity, identical viewport matrix |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `_config.yml` | CREATE | Root-source Jekyll/site configuration and public-source exclusions |
| `Gemfile` | CREATE | Pin the supported GitHub Pages build dependency |
| `_layouts/default.html` | CREATE | Semantic HTML shell, localized head, alternates, social and Dataset metadata |
| `assets/css/catalog.css` | CREATE | Restrained responsive presentation |
| `assets/social-preview.svg` | CREATE | Reproducible editable preview source |
| `assets/social-preview.png` | CREATE | 1280×640 GitHub/social upload asset under 1 MB |
| `scripts/generate_readme.py` | MODIFY | Generate route metadata inputs without changing approved bodies |
| `scripts/test_catalog_generation.py` | MODIFY | Extend Phase A assertions with body/digest preservation and front-matter checks |
| `scripts/test_site_metadata.py` | CREATE | Built route/head/sitemap/Dataset/social/asset assertions |
| `sitemap.xml` | CREATE | Jekyll/Liquid sitemap source for the exact canonical route set |
| `index.md` | MODIFY — GENERATED | English route front matter only; approved body preserved |
| `ru/index.md` | MODIFY — GENERATED | Russian route front matter only; approved body preserved |
| `kk/index.md` | MODIFY — GENERATED | Kazakh route front matter only; approved body preserved |

**Budget:** 8 new files, 5 modifications, 13 implementation paths, estimated delta below 2500 LOC.
Limits: 30 files, 15 new files, 3000 LOC, 30 modified files. Mandatory ONB/RF/EV/review trace
files are additional phase artifacts inside the existing phase folder. No override is authorized.

## 5. Acceptance Criteria

### AC-1: Build one supported three-route Jekyll surface

The root-source repository candidate builds through the supported GitHub Pages/Jekyll dependency and
uses one repository-owned layout for exactly the English, Russian, and Kazakh catalog routes.

- [ ] `_config.yml` uses the canonical `url`/`baseurl` and excludes
  non-public task/tooling material without excluding `data/communities.json` or required assets.
- [ ] The supported dependency is reproducible from `Gemfile`; no unsupported plugin, custom Actions
  workflow, client runtime, theme dependency, or second catalog renderer is introduced.
- [ ] `/`, `/ru/`, and `/kk/` build successfully from generated `index.md` files through one layout.
- [ ] Each built route has exactly one HTML H1 whose text equals the corresponding approved visible H1,
  and body target/fragment sets remain source-derived and locale-parallel.

Gate: `python scripts/validate_schema.py`; `python scripts/generate_readme.py --check`;
`python scripts/test_catalog_generation.py`; supported local Jekyll build; `python scripts/test_site_metadata.py --site <built-site>`.

Evidence: surface: local built EN/RU/KK site; environment: supported GitHub Pages dependency; method:
record dependency versions, build command/output and built route inventory; artifacts:
`evidence/EV__phase-b__published_discovery.md` and `evidence/jekyll-build.txt`; fallback: if the
native Windows Ruby toolchain is absent, a pinned official/containerized GitHub Pages build is allowed
with image/version/digest recorded; a source-only or hand-simulated build is insufficient.

### AC-2: Emit exact locale, canonical, and reciprocal language metadata  [depends: AC-1]

Every route has one unambiguous identity and the same complete alternate set.

- [ ] `<html lang>` is exactly `en`, `ru`, or `kk` for the matching route.
- [ ] Each route has exactly one localized `<title>` and meta description derived from the approved source.
- [ ] Each route has exactly one self-canonical absolute URL under
  `https://saubakirov.github.io/KZ-IT-telegram-list/`.
- [ ] Every route exposes exactly the reciprocal `en`, `ru`, `kk`, and English `x-default`
  alternates with absolute URLs; no route points to itself under the wrong language.
- [ ] No inherited theme/plugin field emits a conflicting canonical, alternate, title, description, or H1.

Gate: parse all built HTML with `scripts/test_site_metadata.py`; assert exact singleton values and
the same locale→URL matrix on every route.

Evidence: N/A — exact head values are deterministic built-output assertions; browser evidence in AC-5 verifies the rendered routes.

### AC-3: Align supported Dataset and social metadata with visible content  [depends: AC-2]

Machine and preview fields describe the same narrow catalog users see; no field invents a publisher,
guarantee, count, or claim absent from the page/source.

- [ ] Each route emits one valid JSON-LD `Dataset` with localized `name` and `description`, self `url`,
  `inLanguage`, source-derived `dateModified`, CC0 license, free-access flag, Kazakhstan spatial scope,
  repository identity, and one `DataDownload` for the absolute public JSON URL with `application/json`.
- [ ] Dataset name/description/date/language/license/download values are exact source or repository facts
  and are consistent with visible title/description/freshness/license/download content.
- [ ] Each route emits one coherent Open Graph set: type, site name, localized title/description,
  self URL, locale plus alternates, absolute preview image, dimensions and meaningful alt text.
- [ ] Each route emits one matching `summary_large_image` Twitter set; no contradictory duplicate social field exists.
- [ ] The final preview PNG is 1280×640, under 1 MB, legible at reduced size, free of unverifiable
  counts/dates, and generated reproducibly from the checked-in vector source.

Gate: JSON parse and exact semantic assertions in `scripts/test_site_metadata.py`; inspect asset
format/dimensions/size; compare head text against visible body/source.

Evidence: surface: local route heads and preview image; environment: built site plus image viewer;
method: capture parsed JSON-LD/social summaries and visually inspect the PNG; artifacts:
`evidence/metadata-summary.json` and `evidence/social-preview-inspection.png`; fallback: none for the
asset or deterministic metadata. Google public validation is post-publication evidence and remains DEFERRED.

### AC-4: Generate the intended sitemap without a new discovery surface  [depends: AC-1]

The supported Jekyll build produces one Liquid-backed sitemap that identifies only the three public catalog routes.

- [ ] `sitemap.xml` is rendered by Jekyll/Liquid from repository-owned source, not copied from built output.
- [ ] Its catalog URL set is exactly root, `/ru/`, and `/kk/`; it contains no task trace, README,
  review artifact, tool file, duplicate route, or missing locale.
- [ ] Sitemap URLs are absolute, HTTPS, canonical, and mutually consistent with route head metadata.
- [ ] No project-path `robots.txt`, `llms.txt`, query page, or extra machine-only prose is added.

Gate: supported Jekyll build plus exact XML URL-set assertion in `scripts/test_site_metadata.py`.

Evidence: N/A — generated XML and exact URL-set assertions are deterministic. Public HTTP evidence remains AC-7 deferred work.

### AC-5: Provide restrained responsive/browser-verified presentation  [depends: AC-1, AC-2]

One static stylesheet makes all three routes readable and useful on mobile and desktop without
changing approved copy, hiding content, or requiring JavaScript.

- [ ] At 390×844 and 1366×768, each route shows one primary identity, its concise promise,
  generated freshness, all three language choices, type navigation, and intent navigation without
  horizontal document overflow, clipped text, overlapping controls, or inaccessible links.
- [ ] A useful catalog entry is reachable by one visible action/scroll from the first screen; the
  supporting Purpose/process/license material remains available after the catalog.
- [ ] Representative language, type, intent, entry, canonical JSON, and repository links resolve in
  the local built site; browser DOM target/fragment sets match deterministic expectations.
- [ ] CSS remains restrained, honors system fonts/color contrast/focus visibility/reduced motion,
  and introduces no client-side script, hidden catalog text, sticky obstruction, or decorative SEO block.

Gate: in-app browser inspection of `/`, `/ru/`, `/kk/` at both exact viewports plus deterministic
DOM/overflow assertions; record bounding boxes for first-screen blocks and first useful entry.

Evidence: surface: local built site; environment: in-app Chromium browser; method: exact viewport
matrix and representative navigation checks; artifacts: six viewport screenshots and
`evidence/browser-matrix.json`; fallback: if in-app browser control fails after documented recovery,
Playwright Chromium at the same sizes is allowed with the exact deviation recorded.

### AC-6: Preserve the approved Phase A body, digest, and regression contract  [depends: AC-1]

Phase B may add front matter/layout/head/style only. It cannot silently reopen the accepted content result.

- [ ] Canonical locale payload digest remains exactly `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`.
- [ ] `data/communities.json`, catalog facts, locale values, intent definitions/memberships, generated
  visible bodies after front-matter normalization, Telegram target pairs, and stable fragments remain unchanged.
- [ ] All twelve Phase A tests remain present and passing; Phase B adds assertions rather than replacing,
  weakening, renaming away, or bypassing them.
- [ ] `README.md` remains generator-current and byte-identical to the approved Phase A base unless a
  deterministic newline-only difference is explicitly proven and accepted by the formal Reviewer.
- [ ] Any locale-content/body change stops Phase B and returns through the complete Phase A digest,
  Antigravity, and formal-review loop before Phase B may continue.

Gate: compare against `d9fe27c6dce80008326fa8eb731d3aff40fd3726`; rerun schema, generator
currency, Phase A test suite, exact digest, source-fact, stripped-body, target-pair, and fragment comparisons.

Evidence: N/A — immutable-base diffs and deterministic checks are authoritative.

### AC-7: Prepare, but do not apply, external settings/publication  [depends: AC-3, AC-4, AC-5, AC-6]

The repository candidate includes exact target values and a runnable publication/verification procedure,
while the current run performs no external mutation and makes no public-outcome claim.

- [ ] Read-only evidence records the current description, blank homepage, four topics, default GitHub
  social preview, Pages `master`/root source, default domain/HTTPS, remote HEAD, deployment run, public
  route/status/head values, and public JSON response.
- [ ] Exact proposed settings are fixed as: description
  `Verified catalog of Kazakhstan IT and startup Telegram groups, channels, and bots — in English, Russian, and Kazakh.`;
  homepage `https://saubakirov.github.io/KZ-IT-telegram-list/`; topics `almaty`,
  `artificial-intelligence`, `astana`, `awesome-list`, `developer-community`, `it`, `jobs`,
  `kazakh-language`, `kazakhstan`, `russian-language`, `startups`, `telegram`; social-preview upload
  `assets/social-preview.png`; Pages remains branch `master`, folder `/(root)`.
- [ ] The runbook includes a fresh read-only drift check, non-force push of the exact reviewed SHA,
  unchanged Pages-source verification, deployment-run/SHA wait, settings edits/uploads only after
  explicit authorization, and exact post-deploy route/head/sitemap/JSON/browser/social/search checks.
- [ ] Existing `data-2026-08-27` tag is reported and never moved or reused. This presentation phase
  creates no tag under the dated catalog-release contract unless a later `/tfw-release` decision
  explicitly selects an allowed new release identity.
- [ ] Public `/ru/`, `/kk/`, sitemap, metadata, social preview, indexing, and retrieval checks are marked
  `DEFERRED — pending explicit authorization and deployment`, not VERIFIED/BLOCKED/N/A or silently omitted.
- [ ] No push, tag, release, deploy, settings/source change, upload, Search Console submission, or other external mutation occurs.

Gate: review EV before/target/remaining-operation tables; inspect git remote/ref state and browser/network
read-only records; confirm mutation log is empty; compare final tree with exact authorized file scope.

Evidence: surface: authenticated read-only GitHub settings plus current public site; environment:
GitHub and GitHub Pages; method: timestamped before-state capture only; artifact:
`evidence/external-checkpoint.md`; post-publication fields: DEFERRED with explicit authorization/deployment blocker.

### AC-8: Obtain independent final copy/metadata advice and formal review  [depends: AC-3, AC-5, AC-6, AC-7]

Antigravity independently reviews the final visible EN/RU/KK copy in context and every user-facing/head/
social/Dataset/settings string; the formal Reviewer alone decides whether the repository candidate passes.

- [ ] Executor or Reviewer discovers and records the actual `agy --help` and model surface before use,
  then invokes the exact executable/model/mode/I/O contract stated in §2 without permission bypass.
- [ ] Complete final visible copy and metadata bytes are content-fed; prompt, input bundle, output,
  model, conversation ID, exit status, and SHA-256 hashes are recorded.
- [ ] Every material finding and nit is dispositioned against exact source/asset bytes; any accepted
  change reruns AC-1–AC-7 and a refreshed Antigravity pass when its reviewed content changed.
- [ ] `/tfw-review` independently verifies the advisory provenance, hashes, findings/dispositions,
  frozen Master HL, Phase A contract, this TS, implementation and evidence before issuing APPROVE/REVISE/REJECT.
- [ ] `APPROVE` applies only to the repository-controlled candidate. It does not satisfy or erase the
  outstanding external authorization/public-evidence checkpoint.

Gate: exact hash/advisory reconciliation plus formal REVIEW by the one persistent Reviewer task.

Evidence: surface: final copy/metadata/asset and review record; environment: local candidate plus
Antigravity; method: formal audit; artifacts: `evidence/EV__phase-b__published_discovery.md`, advisory
input/output files, and `REVIEW__phase-b__published_discovery.md`; fallback: none for the formal Reviewer.

### AC-9: Keep scope minimal, traceable, and resumable  [depends: AC-7, AC-8]

The final local state is clean, linearly integrated, and stops at the correct authorization boundary.

- [ ] Only §4 implementation paths plus mandatory Phase B ONB/RF/EV/review traces, task-local journal,
  allowed Coordinator HL/TS/status/docs/index updates, and evidence attachments change.
- [ ] Actual path/new/modified/LOC totals remain within budget and all commits follow
  `[codex/20260827-132641__catalog_discoverability/{scope}/{role}] summary`.
- [ ] Executor and Reviewer attribution/role locks are preserved; the same two Codex tasks are reused
  for every revision and later authorized publication/review loop.
- [ ] The integrated worktree is clean and the phase lifecycle retains the outstanding external gate
  (normally `BLOCKED` after local APPROVE), rather than falsely becoming full `DONE`.
- [ ] RF/REVIEW/runbook name the exact continuation: who authorizes, which reviewed SHA is eligible,
  which settings/commands execute, what public evidence is collected, and when formal review is refreshed.

Gate: file/LOC/commit/status/journal audit, full local validation, clean `git status`, and formal REVIEW.

Evidence: N/A — repository history, task-local state, trace artifacts, and clean-worktree checks are authoritative.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-b__published_discovery.md` | Required environment, per-AC statuses, hashes, commands, advisory and checkpoint summary |
| `evidence/jekyll-build.txt` | Supported dependency versions and complete successful build log |
| `evidence/metadata-summary.json` | Parsed per-route locale/canonical/alternate/social/Dataset/sitemap values |
| `evidence/browser-matrix.json` | Exact viewport/route/DOM/overflow/navigation results |
| `evidence/browser-390x844-{en,ru,kk}.png` | Mobile route screenshots |
| `evidence/browser-1366x768-{en,ru,kk}.png` | Desktop route screenshots |
| `evidence/social-preview-inspection.png` | Preview asset visual inspection at final bytes |
| `evidence/antigravity-input.txt` | Complete content-fed copy/metadata bundle with hashes |
| `evidence/antigravity-output.jsonl` | Exact object-valued UTF-8 stream-json advisory output |
| `evidence/external-checkpoint.md` | Timestamped current settings/public state, targets, no-mutation record, and runbook |

## 6. Technical Guidance

- The frozen authority is Master HL baseline `00a21bb`. Phase A facts come from its RF and approved
  REVIEW, not from the predecessor TS. The accepted local base is `d9fe27c6…` and locale digest `51db402d…`.
- Current authenticated settings establish that root-source branch deployment is already configured;
  do not change Pages source or add a custom workflow. `_config.yml`, one layout, and a supported
  Jekyll/Liquid sitemap page are the intended repository-owned surface.
- As of planning, GitHub Pages dependency 232 exposes Jekyll 3.10.0. Pin `github-pages` compatibly
  and record resolved versions. Do not enable `jekyll-sitemap` 1.4.0: the first pinned build proved
  that it unconditionally emits a project-path `robots.txt`, conflicting with RES-1 D7 and AC-4.
- `sitemap.xml` may use ordinary Jekyll front matter/Liquid with the canonical site `url`/`baseurl`
  and the fixed researched locale-route set. The built XML, not copied source prose, is the evidence.
- The layout should own the complete head so no theme/SEO helper emits duplicates. A custom layout is
  preferred to `jekyll-seo-tag` here because reciprocal localized alternates and exact Dataset/social
  fields are phase requirements; equivalent supported output may be used with RF justification.
- Canonicals are `https://saubakirov.github.io/KZ-IT-telegram-list/`, `/ru/`, and `/kk/`.
  Reciprocal alternates are `en`, `ru`, `kk`, and `x-default` → English root on every route.
- Route front matter should be generated from existing explicit source values. Locale content and the
  review digest exclude Phase B routing/head fields; prove that boundary rather than modifying locale copy.
- Dataset markup should stay minimal: `Dataset` name/description/url/inLanguage/dateModified/license/
  isAccessibleForFree/spatialCoverage/sameAs plus one `DataDownload` for the JSON. Omit unsupported
  creators, mutable copied counts, invented identifiers, ranking claims, and keywords with no visible job.
- Keep CSS semantic and modest: readable width, wrapping navigation, visible focus, table overflow
  containment, responsive typography/spacing, and no animation requirement. Do not hide content for SEO.
- The social asset's job is repository/site identity at link-preview scale. Use exact deterministic
  typography and a solid-background composition; avoid unverified counts/dates, Telegram trademark
  imitation, generated gibberish, gradients/effects that hurt reduction, or a second slogan.
- Preserve all Phase A test methods and add checks. A new site-metadata test module may consume the
  built `_site`; it may not render an independent replacement for Jekyll.
- For local QA, use the in-app browser-control workflow when available. Serve built `_site` locally,
  use explicit viewport overrides, and reset them after evidence collection. Standalone Playwright is fallback only.
- Public state at planning is a before snapshot: remote `master` `e4986e…`; `/` 200 with two H1s,
  `lang=en-US`, one root canonical, no hreflang/OG image; `/ru/`, `/kk/`, `/sitemap.xml` 404; JSON 200.
- Exact later continuation: re-read remote/settings; require explicit authorization; push reviewed SHA
  without force only if remote state is expected; wait for the Pages deployment matching that SHA;
  apply exact repository settings/social asset only if separately authorized; collect public route/head/
  sitemap/JSON/viewport evidence; record Search Console as VERIFIED only with access, otherwise N/A or
  DEFERRED as the owner directs; rerun the same Reviewer task before closing Phase B.

## 7. Definition of Failure

- ❌ The Phase A locale digest, visible copy/body, catalog facts, intent membership, targets, fragments,
  or README bytes change without the complete predecessor approval loop.
- ❌ A generated projection is hand-edited, Phase A tests are removed/weakened, or a second content renderer appears.
- ❌ Any route has a wrong/missing document language, canonical, reciprocal alternate, or conflicting duplicate head field.
- ❌ Dataset/social metadata contradicts visible content, copies mutable totals, invents authority, or links a non-existent distribution.
- ❌ Sitemap is hand-maintained, omits a locale, or publishes internal traces/tooling.
- ❌ Mobile/desktop QA shows duplicate H1, overflow, clipping, inaccessible navigation, hidden content, or script dependence.
- ❌ Preview asset contains inaccurate text/facts, wrong dimensions/format, exceeds 1 MB, or lacks reproducible source.
- ❌ Antigravity advice is missing, stale, partially content-fed, undispositioned, or presented as formal approval.
- ❌ Public/deployed/indexed/social/search evidence is claimed from local bytes or before an authorized deployment.
- ❌ Any push, tag, release, deploy, upload, settings/source edit, Search Console submission, or other external mutation occurs.
- ❌ A custom app, Actions build, `llms.txt`, project robots file, keyword page, analytics, or other unapproved surface enters the phase.
- ❌ The phase exceeds a scope budget or formal review uses replacement Executor/Reviewer tasks.

Any deterministic, build, browser, asset, or advisory failure returns through the same Executor task.
A formal `REVISE` returns to that task and then to the same Reviewer. A local `APPROVE` advances to the
external authorization/public-evidence checkpoint but cannot close the phase as fully published.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Jekyll/local environment differs from Pages | Use supported `github-pages` dependency and record exact versions/image digest |
| Custom head duplicates plugin/theme metadata | One layout owns head; exact singleton assertions across all routes |
| Phase A body drifts under richer front matter | Strip/compare generated bodies and recompute exact digest against approved base |
| Sitemap leaks repository internals | Explicit excludes plus exact built URL-set test |
| Responsive styling delays useful entries | Numeric viewport evidence at the two researched sizes |
| Preview graphic becomes promotional | One identity job, exact text, no counts/dates/claims, deterministic source |
| Repository/public evidence is stale by authorization time | Repeat before-state checks immediately before later mutation and fail closed on drift |
| External checkpoint is mistaken for task completion | Keep phase lifecycle non-DONE and name DEFERRED evidence explicitly |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `scripts/generate_readme.py` | Phase A | Preserve one renderer and the approved body/digest contract; add only generated route metadata |
| `scripts/test_catalog_generation.py` | Phase A | Extend all twelve tests; never replace or weaken source/body/anchor assertions |
| `index.md`, `ru/index.md`, `kk/index.md` | Phase A | Remain generated; front matter may expand while approved visible bodies stay invariant |

---

*TS — 20260827-132641__catalog_discoverability / Phase B: Published Discovery Surface | 2026-08-27*

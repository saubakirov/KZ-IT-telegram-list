# RF — 20260827-132641__catalog_discoverability / Phase B: Published Discovery

> **Date**: 2026-08-28
> **Author**: saubakirov (Codex Executor)
> **Status**: 🟠 RF — Deployed evidence refreshed; repository custom preview BLOCKED
> **Parent HL**: [Phase B HL](HL__phase-b__published_discovery.md)
> **Master HL**: [Master HL](../HL-20260827-132641__catalog_discoverability.md)
> **TS**: [TS Phase B](TS__phase-b__published_discovery.md)
> **Integrated pre-execution base**: `3280a618b6d9f1a1afd87a51ef382f6922baa0ae`
> **Reviewed deployed SHA**: `bd7af42165c341d653e3efbb20091c131c9f7a40`
> **Implementation/evidence source commit**: `de4060bf817bfb69441f08344f82dd14bc856649`

---

## 1. What Was Done

No implementation byte changed. This bounded continuation independently refreshed only deployed
Phase B evidence and this RF.

### New Files

| File | Description |
|---|---|
| `phase-b/evidence/public-http.json` | Canonical-LF authenticated repository/Pages/ref/tag state and exact public GET/HEAD/body/hash evidence |

### Modified Files

| File | Changes |
|---|---|
| `phase-b/evidence/EV__phase-b__published_discovery.md` | Reconciles deployed, public, browser, blocker, no-mutation, and attachment evidence |
| `phase-b/evidence/external-checkpoint.md` | Replaces the pre-publication before-state with the observed exact deployment/settings/public state and remaining blocker |
| `phase-b/evidence/jekyll-build.txt` | Adds exact-`bd7af421…` rebuild and public byte-comparison facts while preserving the deterministic PNG proof |
| `phase-b/evidence/browser-matrix.json` | Fresh canonical-LF live Chrome matrix for six required cases and 30/30 representative link checks |
| `phase-b/evidence/browser-390x844-{en,ru,kk}.png` | Fresh live mobile screenshots |
| `phase-b/evidence/browser-1366x768-{en,ru,kk}.png` | Fresh live desktop screenshots |
| `phase-b/RF__phase-b__published_discovery.md` | Records the bounded post-publication evidence result and continuation |

The approved implementation boundary remains exactly 13 paths: 8 new and 5 modified. Phase A
source, README, visible bodies, locale digest, implementation, settings, status, HL, TS, REVIEW,
review stages, journal, index, knowledge, and debt were not modified by this Executor.

## 2. Key Decisions

1. Public claims are split by surface. The route-level `og:image`/`twitter:image` is verified because
   it resolves to the reviewed PNG, while GitHub's repository-card `openGraphImageUrl` remains a
   generated fallback and is the sole material blocker.
2. Public byte identity is established against a fresh supported build from an exact Git archive of
   deployed `bd7af421…`, not against a mutable working tree or a hash-only assumption.
3. The six browser cases use the live public URLs at the exact required viewports. Browser-observed
   hrefs are status-checked separately because the browser's read-only evaluation surface exposes no
   `fetch`; all 30 checks are nevertheless bound in the canonical-LF matrix.
4. Antigravity was not rerun because no reviewed visible copy, metadata, setting string, SVG, or PNG
   byte changed. The existing exact advisory binding remains applicable under TS AC-8.
5. This Executor observed previously created external state but made zero external mutation. The
   phase stays `BLOCKED` and returns to the same Reviewer only after Coordinator resolution of the
   repository custom-preview setting.

## 3. Acceptance Criteria

- [x] AC-1 — exact deployed SHA rebuilds through the supported GitHub Pages/Jekyll surface; all seven approved public outputs are byte-identical.
- [x] AC-2 — public EN/RU/KK language, title, description, canonical, and reciprocal alternate metadata are exact.
- [x] AC-3 — public Dataset/Open Graph/Twitter metadata and the page-level preview PNG align with visible/source facts and reviewed bytes.
- [x] AC-4 — public sitemap is exactly the three canonical routes; project `robots.txt` and `llms.txt` are 404 and absent from the local build.
- [x] AC-5 — all six fresh live Chrome cases pass viewport, visibility, overflow, script, navigation, and 30/30 representative-link checks.
- [x] AC-6 — Phase A digest, catalog/source facts, README, stripped bodies, targets, fragments, all twelve predecessor tests, and the preservation extension remain exact; 13/13 tests pass.
- [ ] AC-7 — deploy/ref/build/description/homepage/topics/public/tag evidence is complete, but the repository custom-preview upload has not succeeded; Search Console remains DEFERRED and unauthorized.
- [ ] AC-8 — repository candidate approval and exact Antigravity advice remain valid; this refreshed deployed evidence still requires disposition by the same formal Reviewer.
- [x] AC-9 — the refresh is limited to Executor-owned EV/RF/evidence, the phase remains `BLOCKED`, attribution and continuation are explicit, and forbidden lifecycle/spec/review files are untouched.

Complete publication is not claimed.

## 4. Verification

- Generator currency (`python scripts/generate_readme.py --check`): PASS — four projections current; digest `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`.
- Schema (`python scripts/validate_schema.py`): PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, zero errors.
- Tests (`python -m unittest scripts.test_catalog_generation -v`): PASS — 13/13, including every Phase A test name and preservation extension.
- Supported build: PASS — exact `bd7af421…` archive in pinned official Pages image; Ruby 3.3.4, Bundler 2.5.11, Jekyll 3.10.0; no built robots/llms.
- Local metadata: PASS — exact EN/RU/KK structure, head, Dataset, targets/fragments, sitemap, and preview.
- Public metadata: PASS — downloaded successful-response mirror produces the same 11,097-byte metadata summary as the local build.
- Public HTTP: PASS for approved route/asset surface — GET/HEAD 200 on EN/RU/KK/sitemap/JSON/CSS/PNG; all seven bodies byte-identical to the exact deployed build; project robots/llms GET/HEAD 404.
- Repository/Pages/settings: PASS except custom preview — authenticated `master` and latest built Pages SHA are exact `bd7af421…`; description, homepage, 12 topics exact; Pages source unchanged; historical tag unchanged; GraphQL preview remains fallback.
- Browser: PASS — live EN/RU/KK at 390×844 and 1366×768; zero overflow/hidden critical content/executable scripts/fixed obstruction; type jump works; 30/30 links 200. Matrix: 87,008 bytes / `35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`, canonical LF.
- Asset: PASS — public/repository/inspection PNG is 1280×640, 27,394 bytes / `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`; exact CairoSVG reproduction proof unchanged.
- Antigravity: PASS, unchanged binding — conversation `5f3edb10-3f79-4dbf-8aa8-2c3885dbc28c`; exact model/plan+sandbox/object stream-json/no bypass; findings/nits none.
- Whitespace (`git diff --check`): PASS — no output.

## 5. Evidence

See [EV file](evidence/EV__phase-b__published_discovery.md) for evidence details.

Evidence verdict: 6/9 VERIFIED, 0 DEFERRED, 1 BLOCKED, 2 N/A

Primary refreshed bindings:

- `public-http.json`: 14,666 bytes / `133cd56811d202577b7f0dca9198a2ba0831d3702d232c317f31f8203af43bf8`.
- `browser-matrix.json`: 87,008 bytes / `35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`; zero CRLF; 6 cases; 30/30 links.
- Public EN/RU/KK: 33,669 / 40,530 / 41,343 bytes with exact reviewed hashes.
- Public sitemap/JSON/CSS/PNG: 338 / 45,260 / 2,035 / 27,394 bytes with exact reviewed hashes.
- Page-level preview: VERIFIED at exact reviewed PNG.
- Repository-level preview: BLOCKED at generated `opengraph.githubassets.com` fallback.
- Executor external mutation count: 0.

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

No fact candidates. The custom-preview file-chooser limitation is a task-specific external blocker
already recorded in EV/RF, not reusable human-only project knowledge.

## 8. Strategic Insights (Execution)

No strategic insights. The required distinction between page-level and repository-level preview
surfaces was explicit in the delegated execution boundary and is applied directly here.

## 9. Diagrams

```text
reviewed deploy bd7af421… ──► Pages build at bd7af421… ──► public routes/assets exact
          │                                                   │
          │                                                   ├── page OG/Twitter PNG: VERIFIED
          │                                                   └── live browser matrix: PASS
          │
          └── GitHub repository card preview: generated fallback ──► BLOCKED
```

## Execution Deviations and Boundaries

| Item | Disposition |
|---|---|
| Harness recovery moved the interrupted dirty state into `D:\projects\KZ-IT-telegram-list` | Inspected both locations first; recovered checkout remained at exact `3280a618…` with the complete intended evidence-only delta, while the former worktree was clean. Work continued only on the preserved recovered state. |
| Browser page evaluation exposes no `fetch` | Captured every exact href in live Chrome, then ran read-only HEAD checks on those 30 hrefs before matrix serialization; recorded in EV/matrix. |
| Public mirror initially included saved 404 bodies for robots/llms | Metadata validation used a second mirror containing only the seven successful approved outputs; robots/llms remained separately bound as GET/HEAD 404. No public byte was rewritten. |
| Repository custom-preview upload | BLOCKED. Authenticated GraphQL still returns the generated fallback; Coordinator-reported Chrome chooser/local-file permission limitation remains unresolved. Executor attempted no upload. |
| Search Console | DEFERRED and unauthorized; no submission or indexing claim. |
| Antigravity | Not rerun because reviewed copy/metadata/asset/setting-string bytes are unchanged; prior exact result remains bound. |
| Build-only artifacts | Created only under an external temporary directory; no `_site/` or `Gemfile.lock` was created or committed in the repository. |
| External operations | Zero Executor push/tag/release/deploy/settings/source/upload/Search Console/other external mutations. |

## Continuation

Phase B remains `BLOCKED`. The Coordinator must resolve the repository-level custom-preview upload
through an authorized compliant UI surface, capture the resulting authenticated GraphQL value, and
return this same Phase B RF/EV to the persistent Reviewer. Do not close the phase or claim complete
publication before that formal review.

---

*RF — 20260827-132641__catalog_discoverability / Phase B: Published Discovery | 2026-08-28*

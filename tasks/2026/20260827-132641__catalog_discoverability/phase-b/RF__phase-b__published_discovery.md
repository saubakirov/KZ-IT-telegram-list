# RF — 20260827-132641__catalog_discoverability / Phase B: Published Discovery

> **Date**: 2026-08-28
> **Author**: saubakirov (Codex Executor)
> **Status**: 🟢 RF — F4 closure evidence refreshed; formal review pending
> **Parent HL**: [Phase B HL](HL__phase-b__published_discovery.md)
> **Master HL**: [Master HL](../HL-20260827-132641__catalog_discoverability.md)
> **TS**: [TS Phase B](TS__phase-b__published_discovery.md)
> **Integrated pre-execution base**: `f97c890c98440a8442cc51e689c39b5d013da754`
> **Reviewed deployed SHA**: `bd7af42165c341d653e3efbb20091c131c9f7a40`
> **Implementation/evidence source commit**: `de4060bf817bfb69441f08344f82dd14bc856649`

---

## 1. What Was Done

No implementation byte changed. This bounded continuation independently verified the owner-uploaded
repository social preview and refreshed only Phase B evidence and this RF to close formal finding F4.

### New Files

| File | Description |
|---|---|
| `phase-b/evidence/repository-social-preview-settings.png` | Fresh authenticated GitHub Settings card showing the custom repository preview |

### Modified Files

| File | Changes |
|---|---|
| `phase-b/evidence/EV__phase-b__published_discovery.md` | Reconciles F4 closure, exact custom-image bytes, zero Executor mutation, and Reviewer continuation |
| `phase-b/evidence/external-checkpoint.md` | Replaces the custom-preview blocker with independently verified GraphQL/HTTP/Chrome evidence |
| `phase-b/evidence/public-http.json` | Refreshes authenticated repository/settings state and binds custom-image/UI evidence in canonical LF |
| `phase-b/RF__phase-b__published_discovery.md` | Records the bounded F4 evidence closure and same-Reviewer handoff |

The approved implementation boundary remains exactly 13 paths: 8 new and 5 modified. Phase A
source, README, visible bodies, locale digest, implementation, settings, status, HL, TS, REVIEW,
review stages, journal, index, knowledge, and debt were not modified by this Executor.

## 2. Key Decisions

1. Repository-preview proof requires three aligned surfaces: authenticated GraphQL must return a
   non-fallback URL, its HTTP bytes must match the reviewed PNG, and authenticated Settings must
   visibly render that same URL. All three now agree exactly.
2. The Coordinator delegation attributes the upload to the owner. This Executor records that actor
   boundary separately from the independently verified resulting state and made zero external mutation.
3. Existing deployed/public/browser/build evidence remains current because remote master, Pages build,
   public hashes, tag, settings, implementation bytes, and the six-case matrix are unchanged.
4. Antigravity was not rerun because no reviewed visible copy, metadata, setting string, SVG, or PNG
   byte changed. The existing exact advisory binding remains applicable under TS AC-8.
5. F4 evidence is closed, but formal disposition still belongs to the persistent Reviewer. Status,
   REVIEW, and review-stage files remain untouched under the Executor role lock.

## 3. Acceptance Criteria

- [x] AC-1 — exact deployed SHA rebuilds through the supported GitHub Pages/Jekyll surface; all seven approved public outputs are byte-identical.
- [x] AC-2 — public EN/RU/KK language, title, description, canonical, and reciprocal alternate metadata are exact.
- [x] AC-3 — public Dataset/Open Graph/Twitter metadata and the page-level preview PNG align with visible/source facts and reviewed bytes.
- [x] AC-4 — public sitemap is exactly the three canonical routes; project `robots.txt` and `llms.txt` are 404 and absent from the local build.
- [x] AC-5 — all six fresh live Chrome cases pass viewport, visibility, overflow, script, navigation, and 30/30 representative-link checks.
- [x] AC-6 — Phase A digest, catalog/source facts, README, stripped bodies, targets, fragments, all twelve predecessor tests, and the preservation extension remain exact; 13/13 tests pass.
- [x] AC-7 — deploy/ref/build/description/homepage/topics/public/tag evidence remains exact; the owner-uploaded repository preview is independently verified by authenticated GraphQL, exact HTTP bytes, and visible Settings UI; Search Console remains DEFERRED and unauthorized.
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
- Repository/Pages/settings: PASS — authenticated `master` and latest built Pages SHA are exact `bd7af421…`; description, homepage, 12 topics exact; Pages source unchanged; historical tag unchanged; GraphQL returns the exact non-fallback repository image.
- Browser: PASS — live EN/RU/KK at 390×844 and 1366×768; zero overflow/hidden critical content/executable scripts/fixed obstruction; type jump works; 30/30 links 200. Matrix: 87,008 bytes / `35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`, canonical LF.
- Asset: PASS — public/repository/inspection PNG is 1280×640, 27,394 bytes / `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`; exact CairoSVG reproduction proof unchanged.
- Antigravity: PASS, unchanged binding — conversation `5f3edb10-3f79-4dbf-8aa8-2c3885dbc28c`; exact model/plan+sandbox/object stream-json/no bypass; findings/nits none.
- Whitespace (`git diff --check`): PASS — no output.

## 5. Evidence

See [EV file](evidence/EV__phase-b__published_discovery.md) for evidence details.

Evidence verdict: 7/9 VERIFIED, 0 DEFERRED, 0 BLOCKED, 2 N/A

Primary refreshed bindings:

- `public-http.json`: 17,259 bytes / `11f508d8b92021bd37f0707b43b8d8efc086749c174c59982729d7d8411f84c7`, canonical LF.
- `external-checkpoint.md`: 8,345 bytes / `5bc71240b68e27e71163eb4fccfb76c4777dddbf069ed87c0c983aead8ce6b83`.
- `browser-matrix.json`: 87,008 bytes / `35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`; zero CRLF; 6 cases; 30/30 links.
- Public EN/RU/KK: 33,669 / 40,530 / 41,343 bytes with exact reviewed hashes.
- Public sitemap/JSON/CSS/PNG: 338 / 45,260 / 2,035 / 27,394 bytes with exact reviewed hashes.
- Page-level preview: VERIFIED at exact reviewed PNG.
- Repository-level preview: VERIFIED at `https://repository-images.githubusercontent.com/92145063/3d01cb70-f0b7-406e-b18e-82b18df39588`; 200 `image/png`, 27,394 bytes, exact reviewed SHA-256 and bytes.
- Authenticated Settings visual: `repository-social-preview-settings.png`, 955×510, 30,121 bytes / `e9d158759aa3df45f2eeffde09bccb3c8aed362df3b4bbab30e8c1256860119d`.
- Executor external mutation count: 0.

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

No fact candidates. The owner-upload attribution is delegated execution context; the resulting
GraphQL/HTTP/Settings state is independently discoverable task evidence, not reusable human-only knowledge.

## 8. Strategic Insights (Execution)

No strategic insights. The required distinction between page-level and repository-level preview
surfaces was explicit in the delegated execution boundary and is applied directly here.

## 9. Diagrams

```text
reviewed PNG bytes ──► public page OG/Twitter PNG ──► exact 200 bytes
         │
         └── owner upload ──► GraphQL custom URL ──► exact 200 bytes
                                      │
                                      └── authenticated Settings card: visible
```

## Execution Deviations and Boundaries

| Item | Disposition |
|---|---|
| Prior deployed-evidence loop harness recovery | Preserved from the earlier RF history: the recovered checkout was based on exact `3280a618…`; that loop produced `a67e353…` before the F4 review. This closure began cleanly at exact integrated base `f97c890…`. |
| Browser page evaluation exposes no `fetch` | Captured every exact href in live Chrome, then ran read-only HEAD checks on those 30 hrefs before matrix serialization; recorded in EV/matrix. |
| Public mirror initially included saved 404 bodies for robots/llms | Metadata validation used a second mirror containing only the seven successful approved outputs; robots/llms remained separately bound as GET/HEAD 404. No public byte was rewritten. |
| Repository custom-preview upload | Owner-performed before this capture, per Coordinator delegation. Executor independently verified the resulting GraphQL/HTTP/Settings state and performed no upload or setting mutation. |
| Chrome Settings capture | The pre-existing Settings tab was controlled by the Coordinator session, so the Executor opened a separate authenticated read-only tab. Two framing scroll calls reported bounded timeouts after applying the scroll; fresh DOM rectangles confirmed the state, the final screenshot succeeded, and no control was activated. |
| Search Console | DEFERRED and unauthorized; no submission or indexing claim. |
| Antigravity | Not rerun because reviewed copy/metadata/asset/setting-string bytes are unchanged; prior exact result remains bound. |
| Build-only artifacts | Created only under an external temporary directory; no `_site/` or `Gemfile.lock` was created or committed in the repository. |
| External operations | Zero Executor push/tag/release/deploy/settings/source/upload/Search Console/other external mutations. |

## Continuation

F4's evidence condition is satisfied. Phase B task status remains unchanged under the Executor role
lock; return this exact RF/EV/evidence refresh to the persistent Reviewer. Do not close the phase or
claim complete publication before that formal review.

---

*RF — 20260827-132641__catalog_discoverability / Phase B: Published Discovery | 2026-08-28*

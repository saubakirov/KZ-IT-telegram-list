# RF — 20260827-132641__catalog_discoverability / Phase B: Published Discovery

> **Date**: 2026-08-27
> **Author**: saubakirov (Codex Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Phase B HL](HL__phase-b__published_discovery.md)
> **Master HL**: [Master HL](../HL-20260827-132641__catalog_discoverability.md)
> **TS**: [TS Phase B](TS__phase-b__published_discovery.md)
> **Implementation/evidence commit**: `de4060bf817bfb69441f08344f82dd14bc856649`
> **Initial implementation/evidence commit**: `07bf62b77e5a1d6a1233bba47b63dc9e93ea9a7c`
> **Approved handoff**: `4776edfa29304eb0955393af6f288a654fdac822`
> **Bounded REVISE base**: `4538836b80426980f7823495cffbabed1ceb0fb0`

---

## 1. What Was Done

### New Files

| File | Description |
|------|-------------|
| `_config.yml` | Project URL/base path, exact catalog identity, exclusions, and strict front matter for the supported Pages build |
| `Gemfile` | Pins supported `github-pages` dependency version 232 |
| `_layouts/default.html` | One repository-owned layout with exact locale/canonical/alternate/social/Dataset head and no executable JavaScript |
| `assets/css/catalog.css` | Restrained responsive, focus-visible, overflow-safe static presentation |
| `assets/social-preview.svg` | Deterministic 1280×640 vector source with the exact approved visible text |
| `assets/social-preview.png` | Reproducible 1280×640 raster output, 27,394 bytes |
| `sitemap.xml` | Repository-owned Jekyll/Liquid sitemap for exactly `/`, `/ru/`, `/kk/` |
| `scripts/test_site_metadata.py` | Built-output parser/assertions for routes, metadata, Dataset, pairs, fragments, sitemap, preview, and no robots/llms output |
| `phase-b/evidence/` | EV, complete build/metadata/browser/image/advisory/external-checkpoint evidence bundle |

### Modified Files

| File | Changes |
|------|---------|
| `scripts/generate_readme.py` | Generates locale-specific Jekyll front matter/head inputs while retaining the visible projection renderer |
| `scripts/test_catalog_generation.py` | Adds immutable-base assertions for Phase A source, README, stripped bodies, digest, and predecessor test-name contract |
| `index.md` | Generated EN route front matter only; visible body unchanged |
| `ru/index.md` | Generated RU route front matter only; visible body unchanged |
| `kk/index.md` | Generated KK route front matter only; visible body unchanged |

The implementation boundary is exactly 13 paths: 8 new and 5 modified. Text insertion-plus-deletion
scope is 795 lines, below the 3,000-line implementation cap. Mandatory task-local evidence files are
trace attachments rather than implementation-budget paths.

## 2. Key Decisions

1. One custom layout owns the entire head. This prevents theme/SEO helpers from emitting duplicate
   canonical, locale, social, or Dataset metadata and keeps all three routes structurally identical.
2. The generator owns route front matter. Visible Markdown bodies remain generated from the accepted
   Phase A source, while title/description/canonical/locale values cannot drift from it.
3. The social asset uses deterministic SVG source plus CairoSVG 2.8.2 rasterization. The exact
   checked-in SVG command produces the checked-in PNG, and two fresh rerenders are byte-identical.
   Exact typography is load-bearing, and the final PNG contains no mutable counts, dates, rankings,
   or unsupported claim.
4. The Coordinator-authorized sitemap revision replaces the initially planned `jekyll-sitemap`
   activation. Version 1.4.0 unavoidably emits a project-path `robots.txt`; the final repository-owned
   Liquid sitemap produces the exact three URLs and no robots file while remaining within the supported
   GitHub Pages/Jekyll surface.
5. Public/settings work stops at a read-only checkpoint. All target settings are labeled proposed,
   no external mutation occurred, and every public post-deploy outcome is explicitly deferred.

## 3. Acceptance Criteria

- [x] AC-1 — supported GitHub Pages/Jekyll dependency builds exactly three catalog routes through one layout.
- [x] AC-2 — exact route language, singleton identity, canonical, and reciprocal alternate metadata.
- [x] AC-3 — visible copy, Open Graph, Twitter, Dataset JSON-LD, JSON distribution, and preview asset align without invented claims.
- [x] AC-4 — repository-owned supported sitemap builds exactly the three canonical URLs and emits no `robots.txt` or `llms.txt`.
- [x] AC-5 — all six required browser cases pass responsive, visibility, script, link, and one-action entry checks.
- [x] AC-6 — Phase A digest, catalog/source facts, README bytes, visible bodies, targets, fragments, and all twelve predecessor tests are preserved; test suite extended to 13.
- [x] AC-7 — current settings/public state, exact proposed targets, no-mutation record, and authorization/public-verification runbook are complete; post-deploy claims remain deferred.
- [ ] AC-8 — Executor advisory/evidence contract is complete and formal REVIEW findings F1/F2 are resolved; renewed formal approval by the same Reviewer remains pending under the Executor role lock.
- [x] AC-9 — implementation/evidence scope, attribution, resumability, and outstanding external gate are explicit; no HL, TS, or REVIEW was modified/created.

## 4. Verification

- Generator currency (`python scripts/generate_readme.py --check`): PASS — four projections current; digest `51db402d…`.
- Schema (`python scripts/validate_schema.py`): PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, zero errors.
- Tests (`python -m unittest scripts.test_catalog_generation -v`): PASS — 13/13, including all twelve Phase A test names.
- Supported build: PASS — pinned official Pages container, Ruby 3.3.4, Bundler 2.5.11, Jekyll 3.10.0; no built robots; exact sitemap built.
- Metadata (`python scripts/test_site_metadata.py --site _site --summary ...`): PASS — all three built routes and assets valid.
- Browser: PASS — fresh EN/RU/KK at 390×844 and 1366×768, zero overflow/hidden critical content/executable scripts, representative links 200, first entry visible after one type action; committed canonical-LF matrix 70,133 bytes / SHA-256 `f96aa96e6a60a8d26d46d570e463f516944ca60dbc0995121e34a6bcd29cb269`.
- Asset: PASS — SVG SHA-256 `9f46ff6812ab2b22d852fb11321f9075ef6e53184f7d97df949ae93214d19d82`; PNG SHA-256 `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`; 1280×640; 27,394 bytes; two fresh rerenders and the visual-inspection attachment are byte-identical.
- Antigravity: PASS — CLI 1.1.22 / executable SHA-256 `059b96c1069206158d340ee2a8912894eca5002195e62b8cd281c26c01cd794e`; exact pinned model, plan+sandbox, object-valued UTF-8 stream-JSON, request-review permissions, zero tool steps, no bypass, `SUCCESS`, no findings/nits.
- Whitespace (`git diff --check`): PASS — no output.

## 5. Evidence

See [EV file](evidence/EV__phase-b__published_discovery.md) for evidence details.

Evidence verdict: 4/9 VERIFIED, 1 DEFERRED, 0 BLOCKED, 4 N/A

Key advisory bindings: prompt `e789f8d7301d0825a98a4c532121bdb4385affc31ae8f358cd96d038cdf960fb`;
input `aba88a1bcc48a36f7fd3ac06268c4464ae37965dc2c30b6e118dbbbabddde8ba`;
output `b560698faada053bc896d8da0a4ba106683e2fcbde96eb970c8f474fb0b07d86`;
conversation `5f3edb10-3f79-4dbf-8aa8-2c3885dbc28c`; `PASS`; findings/nits none.
Advisory usage: 58,569 input, 7,096 output, 6,823 thinking, 0 cache-read, 65,665 total tokens.

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

No fact candidates. The Coordinator's sitemap and authorization-wording corrections are phase
decisions already captured in this RF and the evidence, not human-only project facts.

## 8. Strategic Insights (Execution)

No strategic insights. The exact-typography and external-authorization constraints were explicit
execution requirements and were applied directly rather than generalized beyond this phase.

## 9. Diagrams

```text
data/communities.json (accepted Phase A source)
                    │
                    ▼
       scripts/generate_readme.py
          ┌─────────┼──────────┐
          ▼         ▼          ▼
       index.md  ru/index.md  kk/index.md
          └─────────┼──────────┘
                    ▼
      Jekyll 3.10 + default layout + static CSS
          ┌─────────┼──────────┐
          ▼         ▼          ▼
          /        /ru/        /kk/
                    │
                    ├── exact reciprocal metadata + Dataset JSON-LD
                    └── shared deterministic social preview

sitemap.xml (Liquid) ──► exact three canonical URLs; no robots.txt
```

## Execution Deviations and Boundaries

| Item | Disposition |
|---|---|
| Formal REVIEW F1 — documented PNG rerender did not match the checked-in asset | Resolved in `de4060bf817bfb69441f08344f82dd14bc856649`: regenerated by the exact SVG command under the fully probed CairoSVG 2.8.2 environment; two fresh rerenders, the checked-in PNG, and the inspection attachment are all 27,394 bytes / `13e34836…`; every affected build, metadata, external proposed-upload, Antigravity, EV, and RF fact was rebound. |
| Formal REVIEW F2 — EV hash did not bind the committed browser matrix | Resolved in `de4060bf817bfb69441f08344f82dd14bc856649`: complete six-case matrix/screenshots recaptured; canonical-LF matrix is 70,133 bytes / `f96aa96e…`, first checked from the staged blob and then independently from exact committed bytes with `git show`; zero CRLF pairs. |
| Formal REVIEW F3 — Phase HL plugin wording | Already corrected by the Coordinator in exact base `4538836b80426980f7823495cffbabed1ceb0fb0`; preserved unchanged under the Executor role lock. |
| Original plugin-backed sitemap plan produced an unavoidable `robots.txt` | Replaced by the owner-preauthorized Coordinator revision with repository-owned Liquid `sitemap.xml`; implementation count changed to 13 paths / 8 new / 5 modified. |
| Native Windows Ruby/Bundler unavailable | Used the TS-authorized pinned official GitHub Pages build container and recorded image/version/digest. |
| Local project-path browser serving | Used a read-only localhost handler that maps `/KZ-IT-telegram-list` to built `_site`; no built byte was rewritten. |
| Authenticated GitHub settings UI unavailable in the in-app browser | Used authenticated read-only REST/GraphQL through the configured credential helper without printing/storing credentials; captured the same required settings surface. |
| `Gemfile.lock` and `_site/` generated locally | Build-only artifacts; excluded from commits and removed before clean handoff. |
| External operations | Zero push/tag/release/deploy/settings/source/upload/Search Console/other external mutations. |

The proposed description, homepage, topics, preview upload, publication procedure, public evidence,
and Search Console steps remain unauthorized and deferred. Only a later explicit owner authorization
after formal approval may advance that checkpoint.

---

*RF — 20260827-132641__catalog_discoverability / Phase B: Published Discovery | 2026-08-27*

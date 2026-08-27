# RF — 20260827-132641__catalog_discoverability / Phase B: Published Discovery

> **Date**: 2026-08-27
> **Author**: saubakirov (Codex Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Phase B HL](HL__phase-b__published_discovery.md)
> **Master HL**: [Master HL](../HL-20260827-132641__catalog_discoverability.md)
> **TS**: [TS Phase B](TS__phase-b__published_discovery.md)
> **Implementation/evidence commit**: `07bf62b77e5a1d6a1233bba47b63dc9e93ea9a7c`
> **Approved handoff**: `4776edfa29304eb0955393af6f288a654fdac822`

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
| `assets/social-preview.png` | Reproducible 1280×640 raster output, 27,391 bytes |
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
3. The social asset uses deterministic SVG source plus CairoSVG 2.8.2 rasterization. Exact typography
   is load-bearing, and the final PNG contains no mutable counts, dates, rankings, or unsupported claim.
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
- [ ] AC-8 — Executor advisory/evidence contract is complete; the separate formal `/tfw-review` verdict is intentionally pending under the Executor role lock.
- [x] AC-9 — implementation/evidence scope, attribution, resumability, and outstanding external gate are explicit; no HL, TS, or REVIEW was modified/created.

## 4. Verification

- Generator currency (`python scripts/generate_readme.py --check`): PASS — four projections current; digest `51db402d…`.
- Schema (`python scripts/validate_schema.py`): PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, zero errors.
- Tests (`python -m unittest scripts.test_catalog_generation -v`): PASS — 13/13, including all twelve Phase A test names.
- Supported build: PASS — pinned official Pages container, Ruby 3.3.4, Bundler 2.5.11, Jekyll 3.10.0; no built robots; exact sitemap built.
- Metadata (`python scripts/test_site_metadata.py --site _site --summary ...`): PASS — all three built routes and assets valid.
- Browser: PASS — EN/RU/KK at 390×844 and 1366×768, zero overflow/hidden critical content/executable scripts, representative links 200, first entry visible after one type action.
- Asset: PASS — SVG SHA-256 `9f46ff6812ab2b22d852fb11321f9075ef6e53184f7d97df949ae93214d19d82`; PNG SHA-256 `323c124343db406b32170dfa9fe6ec18e5d14479f57691dc6b638f99df2ce9c5`; 1280×640; 27,391 bytes; visually inspected.
- Antigravity: PASS — pinned model, plan+sandbox, object-valued UTF-8 NDJSON, request-review permissions, zero tool steps, no bypass, `SUCCESS`, no findings/nits.
- Whitespace (`git diff --check`): PASS — no output.

## 5. Evidence

See [EV file](evidence/EV__phase-b__published_discovery.md) for evidence details.

Evidence verdict: 4/9 VERIFIED, 1 DEFERRED, 0 BLOCKED, 4 N/A

Key advisory bindings: prompt `722e0e1b5dffe7a4c33925a79bd55342f12da51f9e19916d201ea0c0687af759`;
input `c74627cd6ba8800287a4604420af6c7f8a549577b7d3fc0fa2d4b9480a0f46ef`;
output `0b9bb339c374d64950f2fa74246b4f90cbc973199d57dce95e98eead6e497a09`;
conversation `4e1d1d0d-5343-4cee-a6a4-840088a02947`; `PASS`; findings/nits none.

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

# ONB — 20260827-132641__catalog_discoverability / Phase B: Published Discovery Surface

> **Date**: 2026-08-27
> **Author**: saubakirov (Codex Executor)
> **Status**: 🟠 ONB — Complete; no blocking questions
> **Parent HL**: [Phase B HL](HL__phase-b__published_discovery.md)
> **TS**: [Phase B TS](TS__phase-b__published_discovery.md)

---

## 1. Understanding

Implement the approved repository-controlled GitHub Pages candidate from the unchanged Phase A
catalog: add one supported Jekyll layout, exact localized head/Dataset/social metadata, a generated
three-route sitemap, restrained responsive CSS, and a deterministic SVG-to-PNG social preview. Extend
the existing generator and all twelve tests without changing visible bodies, catalog facts,
destinations, README bytes, or locale digest `51db402d…`. Collect deterministic build and local
browser evidence, obtain hash-bound Antigravity advice, document the read-only external checkpoint,
and stop after Phase B RF with every public/post-deploy result still deferred.

## 2. Entry Points

- `data/communities.json` — immutable Phase A content/fact source and locale digest input.
- `scripts/generate_readme.py` — the only catalog renderer; Phase B may add front matter only.
- `scripts/test_catalog_generation.py` — twelve Phase A regression tests that must remain intact.
- `README.md`, `index.md`, `ru/index.md`, `kk/index.md` — approved generated projections.
- `_config.yml`, `Gemfile`, `_layouts/default.html`, `assets/css/catalog.css` — approved Jekyll surface.
- `assets/social-preview.svg`, `assets/social-preview.png` — exact deterministic preview source/output.
- `scripts/test_site_metadata.py` — new built-site/head/sitemap/asset/DOM contract gate.
- `phase-b/evidence/` — build, browser, metadata, advisory, asset, and external-checkpoint evidence.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved TS fixes the routes, metadata values, asset contract, external
boundary, evidence matrix, build fallback, and Antigravity invocation requirements. The existing
Phase B state and handoff commit record authorization for autonomous repository-controlled work.

## 4. Recommendations (suggestions, not blocking)

No recommendations. The TS already selects the smallest supported implementation surface and gives
deterministic fallbacks where local tooling may vary.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Windows may lack a compatible native Ruby/Bundler toolchain; use only the TS-authorized pinned
   container fallback and record its exact image identity if the native build cannot run.
2. Jekyll will copy static repository files unless exclusions are complete; verify the entire built
   output inventory and the sitemap URL set, not only the three expected HTML files.
3. Browser screenshots can look correct while internal fragment semantics are wrong; bind visual
   evidence to deterministic DOM target/fragment comparisons and representative click results.
4. Antigravity stream-json shape is CLI-version-specific; discover help/model/mode syntax before the
   content-fed run and retain raw object-valued UTF-8 input/output and exit status.

## 6. Inconsistencies with Code (spec vs reality)

No blocking inconsistencies. The repository is clean at handoff commit
`4776edfa29304eb0955393af6f288a654fdac822`; Phase A outputs are generator-current; the approved
digest is present; and the twelve-test suite exists unchanged. The listed Phase B Jekyll, CSS,
metadata-test, and preview paths are correctly absent because they are CREATE actions.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV0 — `README.md` Purpose | ✅ | Applied | Preserve accuracy, curation, generated ownership, and exact-count honesty while changing presentation only. |
| 2 | PV1 — `.tfw/README.md` Methodology values | ✅ | Applied | Use executable gates, candid deferred claims, ordinary durable artifacts, and provider-independent source bytes. |
| 3 | PV1b — `.tfw/README.md` Success Criteria | ✅ | Applied | Deliver complete build/evidence/runbook artifacts with no manual-cleanup placeholders. |
| 4 | PV2 — `knowledge/philosophy.md` absent | ✅ | N/A | Confirmed the optional priority-2 source does not exist; no citation is fabricated. |
| 5 | PV3a — `KNOWLEDGE.md` D1 | ✅ | Applied | Keep JSON/source plus one renderer as the only catalog-content path. |
| 6 | PV3b — `KNOWLEDGE.md` D11 | ✅ | Applied | Keep Purpose/non-goals data-owned and visible after the catalog. |
| 7 | PV3c — `KNOWLEDGE.md` D13 | ✅ | Applied | Surface the source-derived freshness date without making age a schema failure. |
| 8 | PV4a — Conventions §3 Project North Star | ✅ | Applied | Reject extra agent/query/robots/application surfaces. |
| 9 | PV4b — Conventions §11 Quality Standard | ✅ | Applied | No placeholder metadata, partial asset, or post-handoff cleanup. |
| 10 | PV5–6 — optional convention/process topic files absent | ✅ | N/A | Confirmed both optional files are absent; project rules come from existing cited sources. |
| 11 | PV7 — `knowledge/domain.md` F1–F2 | ✅ | Applied | Preserve both archive records and their exact facts/targets. |
| 12 | PV8 — Jekyll front matter/permalinks/Pages dependencies | ✅ | Applied | Use generated YAML front matter, one `_layouts/default.html`, and supported `github-pages`/`jekyll-sitemap` versions. |
| 13 | PV9 — Google localized pages/sitemaps | ✅ | Applied | Emit self canonicals, reciprocal `en`/`ru`/`kk` plus English `x-default`, and one generated sitemap. |
| 14 | PV10 — Google AI guidance/OpenAI crawler roles | ✅ | Applied | Provide ordinary visible clarity and access only; make no ranking or AI-inclusion claim. |
| 15 | PV11 — IANA `kk`/RFC 9309 | ✅ | Applied | Keep `kk` route/language and add no ineffective project-path robots file. |
| 16 | PV12 — Google/Schema.org Dataset/DataDownload | ✅ | Applied | Emit the bounded visible-content-consistent Dataset and real JSON distribution only. |
| 17 | PV13 — W3C language declarations | ✅ | Applied | Set each route’s actual `html lang`; do not treat that as language-quality evidence. |
| 18 | PV14 — GitHub rendered content/anchors | ✅ | Applied | Preserve explicit stable IDs and exact target/fragment parity. |
| 19 | PV15 — GitHub Pages source/local testing | ✅ | Applied | Build the actual root-source shape locally and leave Pages settings unchanged. |
| 20 | PV16 — RFC 8785 | ✅ | Applied | Preserve the approved canonical locale-payload hash boundary. |
| 21 | PV17 — URL Inspection/Playwright assertions | ✅ | Applied | Use executable DOM/viewport checks; keep Search Console/post-deploy checks deferred. |

No additional Project Values item changes the approved execution approach.

---

*ONB — 20260827-132641__catalog_discoverability / Phase B: Published Discovery Surface | 2026-08-27*

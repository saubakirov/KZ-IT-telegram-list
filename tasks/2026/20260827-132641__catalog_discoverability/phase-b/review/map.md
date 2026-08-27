# Map — "What was done?"
> **Mindset:** Experienced newcomer. Understand before judging.
> **RF:** [Phase B RF](../RF__phase-b__published_discovery.md)
> **TS:** [Phase B TS](../TS__phase-b__published_discovery.md)
> **Reviewed base:** `ae4898df0b0b5050cf6f23179d4e090ff04f93db`

## Understanding

The Executor added a repository-controlled GitHub Pages/Jekyll projection for the approved Phase A
EN/RU/KK catalog. The implementation supplies one layout and stylesheet, generated route front
matter, exact canonical/alternate/social/Dataset metadata, a repository-owned Liquid sitemap, and a
checked-in SVG/PNG preview while preserving the Phase A body/digest contract. It also extends the
existing deterministic tests, adds built-site assertions, records local browser/build/advisory
evidence, and stops before every external mutation and public-outcome claim.

The Coordinator revised the original plugin-backed sitemap plan before execution: `jekyll-sitemap`
1.4.0 remains transitively installed but is not enabled, and checked-in `sitemap.xml` owns the exact
three-route output. The final integrated implementation is commit
`5217d928ae0ce04f7f83d1e8d3b02bdb0075c220`, equivalent on every implementation/evidence path to
Executor commit `07bf62b77e5a1d6a1233bba47b63dc9e93ea9a7c`; commit
`d6c2c2c679033d06f1d1f4361227e8485de1be48` then removed one trailing space from the Jekyll log only.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|---|---|---|
| AC-1 — supported three-route Jekyll surface | Pinned `github-pages` 232 build; one layout; exact EN/RU/KK output | ✅ Claimed |
| AC-2 — exact locale, canonical, and reciprocal language metadata | Singleton localized head values, self canonicals, `en`/`ru`/`kk`/`x-default` alternates | ✅ Claimed |
| AC-3 — visible-content-consistent Dataset/social metadata and reproducible preview | Exact Dataset/OG/Twitter assertions and CairoSVG 2.8.2 SVG-to-PNG record | ✅ Claimed |
| AC-4 — exact repository-owned sitemap, no robots/llms surface | Liquid sitemap with three URLs; plugin disabled; no forbidden output | ✅ Claimed |
| AC-5 — responsive local-browser presentation | Six EN/RU/KK cases at 390×844 and 1366×768 with link/navigation assertions | ✅ Claimed |
| AC-6 — Phase A body/digest/regression preservation | Digest `51db402d…`, unchanged data/README/body, all twelve predecessor tests plus one new test | ✅ Claimed |
| AC-7 — prepare but do not apply publication/settings | Read-only checkpoint, exact target package and runbook; public results deferred | ✅ Claimed |
| AC-8 — independent advice and formal review | Hash-bound Antigravity PASS recorded; this formal review remained pending | ✅ Claimed as pending formal verdict |
| AC-9 — minimal, traceable, resumable scope | 13 implementation paths, task-local evidence, clean integrated base, external gate retained | ✅ Claimed |

## Deviations from TS

- Public deployment, repository settings, upload, Search Console, indexing, retrieval, and outcome
  evidence are intentionally deferred exactly as AC-7 requires; the RF does not claim publication.
- The RF describes 13 implementation paths (8 new, 5 modified) plus mandatory task-local trace and
  evidence artifacts, consistent with the Coordinator-revised TS budget.
- The integrated commit identity differs from the Executor-source commit identity because the
  Coordinator revision and dispatch traces were already in the integration ancestry; implementation
  and evidence blobs are identical between the two commits.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§9 completely.
- [x] Read TS DoD and matched AC-1 through AC-9 to RF §3.
- [x] Read frozen Master HL §7 principles: subtract unnecessary surfaces, protect accuracy and one
  source, serve people through clear projections, keep the catalog narrow, measure controllable
  evidence, and preserve one experience across EN/RU/KK.
- [x] Read ONB; it records no blocking questions and names the plugin/robots risk, immutable Phase A
  boundary, evidence inventory, external stop, and all knowledge citations.

Stage complete: YES

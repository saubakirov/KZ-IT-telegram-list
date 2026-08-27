# RES — 20260827-132641__catalog_discoverability: Catalog Discoverability and Multilingual Presentation — Iteration 2

> **Date**: 2026-08-27
> **Author**: saubakirov
> **Status**: 🔬 RES — Iteration 2 complete
> **Parent HL**: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> **Predecessor**: [Iteration 1 RES](../iter1/RES.md)
> **Mode**: Pipeline (focused)

---

## Research Context

Iteration 1 selected the multilingual routes, one-source generator architecture, compact intent-map pattern, and bounded search/AI signals. Iteration 2 was deliberately focused: it did not reopen those choices or repeat broad SEO/AEO research. It closed the remaining TS-critical contracts for qualified EN/RU/KK review, exact current intent membership, GitHub-versus-Pages rendering and metadata evidence, and owner-controlled external gates. The work inspected every current catalog entry, the live GitHub and Pages renders, the current data/generator/validators, and targeted primary documentation.

## Briefing

See [1_briefing.md](1_briefing.md). The Coordinator approved focused mode because the remaining scope was narrow and architecture selection was closed. The iteration preserved Iteration 1 D1–D9 and tested the conditional parts of H1–H4.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D10 | Define one common locale manifest with 131 current semantic values per language: 92 data-backed values plus 39 exact UI keys. Derive live/archive quantities; do not hardcode mutable catalog totals. | The finite inventory eliminates “translation complete” as a subjective claim while keeping identity facts, counts, dates, IDs, brands, and code tokens invariant. An optional English-only workflow appendix has eight additional keys and joins the common manifest if ever emitted on RU/KK. |
| D11 | Require owner-designated qualified human approval per locale, bound to a canonical NFC/sorted-JSON/SHA-256 payload digest, immutable prior approved Git ref and digest, and computed exact changed-key set; fail the complete multilingual gate if any locale is missing, stale, incomplete, placeholder-filled, fallback-derived, or unapproved. | This proves that reviewed language is the language generated and makes review diffs reproducible. Machine/AI output may be a candidate but cannot certify English, Russian, or Kazakh. Complete approved payloads are a Phase A entry input, so this research invents or certifies no Kazakh wording. |
| D12 | Use the exact five category-plus-exception intent definitions from Extract E2 and the full 62-row audit in Gather G5. Current memberships are AI 3, startups 3, jobs 6, events 1, and engineering 46; use no runtime exclusions. | Validated categories carry normal membership, while reviewed exceptional live handles cover cross-category semantics. The audit records exclusions and caveats without duplicating full entries or inferring intent from localized prose. |
| D13 | Give generator-owned stable destinations explicit type, type/category, intent, and case-folded handle IDs; intent navigation links to non-empty category destinations and exceptional entry destinations. | Localized display text and renderer-generated slugs are not stable across EN/RU/KK, GitHub Markdown, and Jekyll. GitHub officially supports custom anchors, but every destination must still be tested on both renderers. |
| D14 | Require the layered pre-publication contract A1–A7 and post-publication contract P1–P8 in Extract E4, including one H1, route/status/content types, language/canonical/reciprocal alternates, sitemap, Dataset/DataDownload, deployed JSON parity, unique fragments, exact Telegram anchor-pair parity, and numeric first-screen bounds at 390×844 and 1366×768. | The live Pages render has 61 Telegram anchors where GitHub has all 64: `kzquake` loses link structure through pipe parsing and two archive links remain non-interactive inside raw HTML. URL-substring, source-only, GitHub-only, or generic HTML-validity checks each miss a real defect. |
| D15 | Treat qualified language content, authenticated Pages source, repository settings, Search Console, and retrieval observations as typed gates with distinct phase/disposition rules. | Missing language approvals block Phase A; unknown Pages source blocks only Phase B; settings are never mutated without exact owner-approved values; unavailable Search Console is `N/A` or explicitly `DEFERRED`; rank/indexing/AI inclusion are timestamped positive-or-negative observations, never release gates. |
| D16 | Recommend research **SUFFICIENT** after Iteration 2. | All remaining unknowns are owner inputs, access/settings facts, deployment evidence, or non-guaranteed external outcomes. None is an unresolved implementation architecture or semantic-model question requiring Iteration 3. |

### Exact intent definition summary

The authoritative entry-by-entry disposition is Gather G5. This summary is sufficient for TS source configuration; membership is the union of selected categories and exceptional handles.

| Intent | Selected categories | Exceptional live handles | Current count | Important semantic exclusions |
|--------|---------------------|--------------------------|---------------|-------------------------------|
| AI | `ai` | `ml_jobs_kz`, `dsmlkz_news` | 3 | Generic analytics/BI/DWH communities are not AI by implication. |
| Startups | `startups` | `thetechkzchat`, `thetechkz`, `saubakirov` | 3 | Marketplaces and project-management communities are not founder/venture ecosystems. |
| Jobs | `jobs` | None | 6 | Education/career communities are not vacancy feeds without a primary jobs purpose. |
| Events | `events` | None | 1 | Communities that sometimes host events are not event-announcement catalogs. |
| Engineering | `ai`, `blockchain`, `data-analytics`, `devops-sysadmin`, `gamedev`, `hardware`, `mobile`, `programming-languages`, `qa-testing`, `security`, `web-development` | `devkz`, `illuminatinc`, `teamleads_kz`, `datanomika`, `DevSkills`, `nu_acm_w`, `sysadm_in_up`, `saubakirov`, `cleverskz`, `Get_Telegram_ID_bot` | 46 | Excludes jobs-only feeds, general tech news, marketplaces, project management, public-service bots, and the event feed. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Who supplies and qualifies the EN, RU, and KK reviewers and complete approved string payloads? | OPEN — Phase A input gate | The owner designates reviewers; every locale record must state language fluency/native competence and Kazakhstan IT/Telegram domain competence. This is required before implementation/generation, but reviewer identity is not a research design question. |
| Q2 | What publishing source is authenticated for the live GitHub Pages site? | OPEN — Phase B access gate | Obtain owner-authenticated branch/workflow and source-folder evidence before local build/deployment changes. If unavailable, defer/block Phase B only; do not infer a switch to root or `/docs`. |
| Q3 | What exact repository description, homepage, topics, and social-preview asset are owner-approved? | OPEN — Phase B settings gate | Record before state, exact approved target values/asset, and after/public evidence. Do not mutate settings without these inputs. |
| Q4 | Will the owner supply Search Console access? | CONDITIONAL — post-public evidence | If available, record property/date/URL and sitemap inspection. If unavailable, record `N/A — owner access unavailable`; use `DEFERRED` only when the owner keeps it pending. |
| Q5 | Will the routes rank, be indexed promptly, or appear in AI answers? | EXTERNAL OBSERVATION — never a gate | Record timestamped query, locale, surface, and positive or negative result. No implementation or research can guarantee ranking, indexing latency, or AI inclusion. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Separate generated language entry points linked above the fold produce a smaller and clearer experience than one trilingual README while preserving one catalog. | confirmed design | 🟢 CONFIRMED AND CLOSED | Gather G1–G3, Extract E1, Challenge C1–C2: exact 131-value common payload, digest/diff qualified approval, and fail-all generation make `/`, `/ru/`, and `/kk/` complete projections of one source without fallback or invented Kazakh. |
| H2 | Clear first-screen structure, accurate repository/site metadata, stable facts, and crawlable source data create more defensible search/AI discoverability than `llms.txt`, keyword blocks, or agent-only prose. | supported with external-outcome limit | 🟢 SUPPORTED WITH EXECUTABLE BOUNDARY | Gather G6–G8, Extract E4–E6, Challenge C5–C7: the contract verifies visible structure, reciprocal metadata, sitemap, Dataset linkage, public JSON, and crawl eligibility; rank/indexing/AI inclusion remain non-guaranteed observations. |
| H3 | A small derived intent model can expose AI, startups, jobs, events, and engineering across groups/channels/bots without duplicate entries or scope expansion. | conditionally supported | 🟢 CONFIRMED FOR CURRENT SNAPSHOT | Gather G4–G5, Extract E2–E3, Challenge C3: all 62 entries were reviewed, exact category/exception definitions yield 3/3/6/1/46 memberships, and compact stable destinations link into one full catalog. |
| H4 | Lightweight GitHub Pages configuration can create one coherent page identity and multilingual metadata while keeping GitHub's README experience intact. | technically confirmed with external setting dependency | 🟢 CONFIRMED WITH PHASE B ACCESS GATE | Gather G6–G8, Extract E3–E6, Challenge C4–C7: explicit anchors and A1–A7/P1–P8 are executable across GitHub and Jekyll. Authenticated source/settings remain owner gates, not unresolved architecture. |

## HL Update Recommendations

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Add the 2026-08-27 measured render snapshot: GitHub/REST exposes all 64 live+archive Telegram anchors; Pages exposes 61, missing interactive `kzquake`, `mobile_developers_kz`, and `kzqacommunity` anchors although their URL strings remain in HTML. Record present locale coverage as EN 92/92, RU 64/92, KK 0/92 without implying approval. | Gather G1/G6; Extract E5 |
| R2 | §7.2 | Add W3C language declarations, GitHub rendered Contents API/custom anchors/Pages source and local-test documentation, RFC 8785 canonicalization rationale, Google URL Inspection, and Playwright assertion primitives as contract citations. | Gather G1/G6/G7; Extract E1/E3/E4; Challenge C4–C6 |
| R3 | §8 | Mark exact intent membership and the finite localization/evidence contract complete. Recast actual qualified language payloads as a Phase A input gate, and Pages source/settings/Search Console as the typed Phase B or conditional gates in D15. | D10–D15 |
| R4 | §9 | Add review-digest churn, broad Engineering semantics, and cross-render target-set drift; mitigate through prior-digest/changed-key review, category-plus-exception audit, and anchor-pair parity. | Challenge C1/C3/C4 |
| R5 | §10 | Mark H1 closed, H3 confirmed for the current snapshot, and H2/H4 closed within their controllable boundaries. Replace the proposed research focus with “Iteration 2 complete; no further broad research recommended,” while retaining actual translations/settings/retrieval as gated inputs/evidence. | Challenge C7–C9; D16 |

### Amendment Proposals — frozen sections, owner verdict required

No amendment proposals. Iteration 2 makes the frozen outcome executable without changing its declarative claims.

## Fact Candidates

No fact candidates. The Coordinator's focused-mode and closed-architecture directions are workflow decisions, not enduring project facts for the knowledge gate.

## Strategic Insights (Research)

No strategic insights. The owner supplied no new domain correction or philosophy in this iteration; the research operationalized the already-frozen contract.

## Findings Map

| Frozen outcome | Research closure | Executable proof | External boundary |
|----------------|------------------|------------------|-------------------|
| Complete EN/RU/KK | 131-value manifest + qualified digest/diff approval | A1–A2; generation fails all on any stale locale | Reviewer identities and approved payloads enter before Phase A |
| One catalog, five intents | Exact categories + exceptional handles; 62-row audit | A3; current exact sets 3/3/6/1/46; stable IDs | Later owner TS approval ratifies semantics |
| GitHub + Pages parity | Generator-owned destinations + Telegram anchor-pair multiset | A4–A7 and P1–P8 | Authenticated publishing source/settings enter before Phase B |
| Defensible discovery | Canonical/alternates/sitemap/Dataset/public JSON/visible first screen | P4–P8 and conditional inspection | Indexing, rank, and AI inclusion are observations, never guarantees |

The causal chain is finite: **approved source payloads → one locale-aware generator → four generated projections → GitHub/Jekyll/public assertions → optional external observations**. No downstream surface becomes a second catalog or a substitute for language review.

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (confirmed and closed), H2 (supported within controllable scope), H3 (confirmed for current snapshot), H4 (confirmed with Phase B access gate)
- **Hypotheses deferred:** None
- **Gaps discovered:** Actual qualified EN/RU/KK payloads/attestations; authenticated Pages source; owner-approved repository settings; optional Search Console access; variable rank/indexing/AI results. Each has a phase, owner, and failure disposition and is therefore a gated input/evidence boundary rather than a research gap.
- **Superseded decisions:** None. D10–D16 refine and close the conditional portions of Iteration 1 D4–D5/D8–D9 without reversing D1–D9.

### Open Threads (for next iteration)

No open research threads. The open questions above belong to TS input/evidence gates; Iteration 3 would repeat external access checks or wait for inputs rather than reduce design uncertainty.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — not recommended; no TS-critical design gap remains
- [ ] **BLOCKED** — not recommended; gated inputs can be represented honestly in TS

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Focused Iteration 2 converted four conditional research areas into finite TS-ready contracts. It enumerated the complete localization payload without supplying or certifying Kazakh, classified every current entry into exact intent sets with exclusions and caveats, proved why GitHub and Pages need independent anchor/DOM evidence, and separated controllable metadata from authenticated settings and non-guaranteed retrieval. The key result that broad guidance alone would have missed is the measured cross-render failure: all source URLs and GitHub links can be correct while Pages silently loses three interactive Telegram anchors. Self-critique: the research cannot supply linguistic approval, authenticated repository settings, Search Console access, or future retrieval outcomes; instead of treating those limits as unresolved design, it gives each an explicit blocking or non-blocking disposition.

---

*RES — 20260827-132641__catalog_discoverability: Catalog Discoverability and Multilingual Presentation — Iteration 2 | 2026-08-27*

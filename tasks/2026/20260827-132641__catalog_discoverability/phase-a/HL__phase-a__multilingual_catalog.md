# Phase HL — 20260827-132641__catalog_discoverability / Phase A: One-source Multilingual Catalog

> **Date**: 2026-08-27
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS APPROVED — owner mandate, 2026-08-27
> **Contract**: DERIVATION-ONLY — inherits frozen Master HL baseline `00a21bb`
> **Parent HL**: [Master HL](../HL-20260827-132641__catalog_discoverability.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) · [Iteration 2 RES](../research/iter2/RES.md)
> **Authority**: The owner approved the Phase A TS in substance on 2026-08-27, authorized autonomous
> completion, and delegated the final language verdict to the pipeline. Antigravity provides an
> independent advisory text review; the formal Reviewer verifies its findings, dispositions, and
> the final digest. No separate human chat approval is represented.

> This Phase HL adds execution context only. It does not define an independent vision,
> acceptance contract, failure contract, or principles. Master HL §§1, 5, 6, and 7 remain the
> sole authority under `conventions.md` §3 rules 20–21.

---

## 2. Phase Context

The repository already has one catalog owner, one English generator, passing schema validation,
and a generator-current `README.md`. The current source has English descriptions and Russian
description candidates for every live record, but no complete locale registry, no Kazakh content,
no reviewed five-intent source, and no generated Pages indexes. GitHub and Pages also disagree on
three interactive Telegram anchors despite generic HTML validity.

Research selected the smallest architecture that preserves the existing product:

| Decision surface | Phase A derivation | Governing source |
|------------------|--------------------|------------------|
| Language routes | English `/`, Russian `/ru/`, Kazakh `/kk/`; all linked in one action | RES-1 D1–D3 |
| Source ownership | Community facts remain in `data/communities.json`; locale and intent data are validated source, never copied into hand-maintained pages | Master HL P3; RES-1 D3–D5 |
| Browsing | Type-first catalog plus one compact AI/startups/jobs/events/engineering map | RES-1 D4; RES-2 D12–D13 |
| Generated surfaces | `README.md`, `index.md`, `ru/index.md`, `kk/index.md` from one renderer | RES-1 D2–D3 |
| Portability | Stable explicit destinations, escaped Markdown, derived Telegram target parity | RES-1 D8; RES-2 D13–D14 |
| Language approval | Complete candidates first; Antigravity advisory review; formal Reviewer verification of findings, dispositions, and the ready content digest | Owner mandate 2026-08-27; Master HL S5 |

The final-review direction refines a free dependency and does not amend the frozen contract. The
contract forbids shipping unreviewed or fallback language; it does not require review before the
generator and complete candidate renders exist.

## 3. Derived Phase Outcome

```text
data/communities.json
├─ invariant community facts
├─ complete EN/RU/KK candidate values
├─ five reviewed intent definitions
└─ content-bound review state
             │
             ▼
   one locale-aware generator
   ├─ README.md       GitHub projection
   ├─ index.md        Pages EN body
   ├─ ru/index.md     Pages RU body
   └─ kk/index.md     Pages KK body
             │
             ▼
 schema · currency · stable IDs · escaping · target parity
             │
             ▼
 Antigravity text-quality advice → formal Reviewer digest-bound verdict
             │
             ▼
 Phase A accepted and ready for Phase B metadata/layout/publication work
```

The ready experience starts with one catalog identity, one concise promise, generated freshness,
three language links, type and intent routes, then useful entries. Purpose, non-goals,
contribution, process, and license context remain available but do not repeat or delay the catalog.

Phase A does not publish or configure the site. It produces complete reviewed content, generated
projections, and repository-controlled evidence. Phase B owns Jekyll layout/head metadata,
sitemap/Dataset integration, repository settings, deployment, viewport evidence, and retrieval
observations.

## 4. Scope, Sequence, and Files

| Path | Phase action | Boundary |
|------|--------------|----------|
| `data/communities.json` | MODIFY | Complete locale, intent, and final review-bound source without changing unverified live facts |
| `scripts/validate_schema.py` | MODIFY | Validate locale completeness, categories across types, intents, review binding, and invariants |
| `scripts/generate_readme.py` | MODIFY | One locale-aware renderer and four-output currency check |
| `scripts/test_catalog_generation.py` | CREATE | Deterministic positive/negative regression coverage for schema and generated Markdown |
| `README.md` | MODIFY — GENERATED | Concise English GitHub projection; never hand-edited |
| `index.md` | CREATE — GENERATED | English Pages body and route declaration |
| `ru/index.md` | CREATE — GENERATED | Complete Russian Pages body and route declaration |
| `kk/index.md` | CREATE — GENERATED | Complete Kazakh Pages body and route declaration |

Sequence:

1. Establish the locale/intent/review source contract and deterministic validators.
2. Produce complete candidate strings and the four generated projections.
3. Prove source, currency, structure, special-character, stable-anchor, and GitHub-render parity.
4. Run the independent Antigravity text-quality pass on the ready renders.
5. Disposition the review findings against the exact changed-key/digest record and rerun all checks
   after any wording change.
6. Submit the final ready renders, Antigravity record, dispositions, and exact digest to the formal
   Reviewer; only a defensible APPROVE may close Phase A.

### Scope Budget

| Measure | Estimate | Limit | Result |
|---------|----------|-------|--------|
| Implementation paths | 8 | 30 | Within budget |
| New implementation files | 4 | 15 | Within budget |
| Modified implementation files | 4 | 30 | Within budget |
| Estimated implementation/generated delta | <3000 LOC | 3000 | Within budget, Executor must report actual |
| Full phase new files including lifecycle trace | 14 maximum | 15 | Within budget |

The estimate is intentionally close to the LOC ceiling because four complete projections are
counted even though three are deterministic outputs. Any new application, layout system, or extra
language surface exceeds this phase and requires re-planning rather than a budget override.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Frozen Master HL | ✅ baseline `00a21bb` |
| Research architecture and evidence contracts | ✅ Iterations 1–2 sufficient |
| Existing structured catalog, generator, and validators | ✅ available and passing |
| Complete candidate EN/RU/KK wording | 🟡 produced during Phase A; existing RU presence is not inherited approval |
| Independent Antigravity language-quality review | ⬜ final advisory gate; use the requested Gemini Flash 3.7 model as exposed by `agy`, or the nearest supported Gemini Flash 3.x fallback with the exact reason recorded |
| Formal Reviewer language verdict | ⬜ required Phase A acceptance gate; must verify Antigravity findings/dispositions and bind to the final digest under the owner mandate |
| Authenticated Pages publishing source | N/A — Phase B gate, not required to prepare Phase A bodies |
| Repository settings or Search Console access | N/A — Phase B only |
| Push or public deployment | N/A — not authorized by this phase |

## 9. Phase Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Final-only language review causes late rework | Medium | High | Stabilize structure first; review all ready renders together; regenerate and re-run deterministic gates after every wording change |
| Machine-drafted Kazakh sounds fluent but changes meaning | High | High | Treat all text as candidate; independent advisory review plus formal Reviewer verification; no fallback or automatic certification |
| Antigravity findings are incompletely dispositioned | Medium | High | Record each material finding against the final digest and require the formal Reviewer to verify the disposition before APPROVE |
| Intent navigation looks complete while silently omitting entries | Medium | High | Use the researched category-plus-exception rules and derive future memberships from validated data |
| Generated projections become four drifting catalogs | Medium | High | One renderer and one currency command must fail when any output differs |
| Markdown passes locally but GitHub loses links or destinations | High | High | Test exact anchor text/URL pairs and internal fragments against GitHub-rendered Markdown |
| Phase B metadata or styling leaks into content implementation | Medium | Medium | Keep `_config.yml`, layouts, sitemap, Dataset/head markup, deployment, and repository settings out of Phase A |

---

*Phase HL — 20260827-132641__catalog_discoverability / Phase A: One-source Multilingual Catalog | 2026-08-27*

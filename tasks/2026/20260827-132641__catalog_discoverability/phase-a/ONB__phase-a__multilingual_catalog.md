# ONB — 20260827-132641__catalog_discoverability / Phase A: One-source Multilingual Catalog

> **Date**: 2026-08-27
> **Author**: Executor (Codex)
> **Status**: 🟢 READY — No blocking questions
> **Parent HL**: [Phase A HL](HL__phase-a__multilingual_catalog.md)
> **TS**: [TS Phase A](TS__phase-a__multilingual_catalog.md)
> **Execution baseline**: `a646f59794fdb639a8e0471838b33727bd4ac31c`

---

## 1. Understanding

Phase A must turn the current English-only generated catalog into four deterministic projections—
the English GitHub `README.md` plus EN/RU/KK Pages bodies—while `data/communities.json` remains the
only owner of community and localized content. The implementation must add an exact locale/review
contract, the researched five-intent definitions, stable renderer-independent destinations,
portable Markdown escaping, fail-closed validation, and regression coverage. It must preserve all
community identity, liveness, count, verification, and archive facts, obtain exact-byte read-only
GitHub render evidence, run a final advisory Antigravity language pass, and stop after EV/RF without
performing Phase B work or any external mutation.

## 2. Entry Points

- `data/communities.json` — invariant records, current EN/RU candidate descriptions, categories,
  archive, and the source location for the new locale/intent/review contract.
- `scripts/validate_schema.py` — current offline North Star, entry, archive, date, category, and
  freshness validation.
- `scripts/generate_readme.py` — current one-output English renderer and non-mutating currency gate.
- `scripts/test_catalog_generation.py` — new deterministic positive/negative regression suite.
- `README.md`, `index.md`, `ru/index.md`, `kk/index.md` — generated outputs only.
- RES Iteration 2 D10–D16, Gather G1–G5, and the 62-entry intent audit — exact semantic reference.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved TS, frozen Master HL, owner mandate, and research tables define
the required source, projection, review, and evidence boundaries sufficiently for autonomous local
execution.

## 4. Recommendations (suggestions, not blocking)

1. Represent each entry description as an explicit `en`/`ru`/`kk` map and keep locale UI values in
   one validated registry. This removes the legacy `description_ru` special case without creating
   independent language files.
2. Record a deterministic `CANDIDATE` payload digest and changed-key set in source before formal
   review. The later TFW REVIEW, not source metadata or Antigravity, supplies the acceptance verdict;
   this keeps pre-review generation possible without fabricating approval.
3. Preserve the existing command contract (`python scripts/generate_readme.py` and `--check`) while
   making both operations cover all four outputs atomically.
4. Use explicit HTML anchor destinations in generated Markdown and parse rendered anchors by
   semantics. Display-text slugs are not stable across locales or renderers.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Canonical payload hashing can drift across platforms unless strings are NFC-normalized, JSON is
   key-sorted with stable separators, UTF-8 is explicit, and the payload excludes its own review
   metadata.
2. Case-folded handle destinations must be collision-checked because existing handles preserve case
   (`iOSDevelopers_KZ`, `MikroTikKZ`, `AQA_kz`) while anchor identity does not.
3. Escaping a pipe fixes `kzquake`, but brackets, backticks, backslashes, angle brackets, ampersands,
   and archive-table content require context-specific escaping rather than one generic replacement.
4. A public GitHub renderer call can be rate-limited; AC-4 has no fallback, so the exact request and
   response must be captured before RF and a failure would block completion.

## 6. Inconsistencies with Code (spec vs reality)

1. The TS requires categories to be validated for every typed record that carries one; current code
   validates categories only for groups and group archives.
2. The TS requires four atomic generated outputs; current code knows only `README.md` and its
   `--readme` override.
3. The TS requires stable explicit destinations and semantic fragment checks; current navigation
   relies on display-name-derived GitHub slugs and has no destination registry.
4. The TS requires exact Telegram anchor parity; current live-entry formatting does not escape the
   pipe in `Землетрясения | Казахстан`, and the raw HTML archive wrapper prevents two archive
   Markdown links from becoming interactive on Pages.
5. The TS requires deterministic regression gates; the repository currently has no test module for
   schema or catalog generation.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV0 — `README.md` Purpose and non-goals | ✅ | Applied | Accuracy, narrow IT scope, source ownership, and exact-count rules remain unchanged. |
| 2 | PV1 — TFW Methodology values | ✅ | Applied | Locale completeness, currency, digest, and anchor parity become executable gates; evidence remains candid and portable. |
| 3 | PV1b — TFW Success Criteria | ✅ | Applied | All four outputs and the EV/RF package must be complete and acceptance-ready. |
| 4 | PV2 — `knowledge/philosophy.md` | ✅ | N/A | The cited file does not exist; no substitute principle is fabricated. |
| 5 | PV3a — KNOWLEDGE D1 | ✅ | Applied | JSON remains the single source and every public document is generated. |
| 6 | PV3b — KNOWLEDGE D11 | ✅ | Applied | Localized Purpose/non-goals remain structured data projected by the renderer. |
| 7 | PV3c — KNOWLEDGE D13 | ✅ | Applied | Freshness is rendered and reported but valid age is not made fatal. |
| 8 | PV4a — Conventions Project North Star | ✅ | Applied | The phase adds only surfaces with a demonstrated human/render consumer job. |
| 9 | PV4b — Conventions Quality Standard | ✅ | Applied | No placeholder, fallback, or post-handoff manual cleanup is allowed. |
| 10 | PV5–6 — optional convention/process topic files | ✅ | N/A | Both cited optional files are absent; local standards come from D-records and the approved TS. |
| 11 | PV7 — `knowledge/domain.md` F1–F2 | ✅ | Applied | Both archived records and their evidence facts remain intact and render in every locale. |
| 12 | PV8 — Jekyll front matter/permalinks/dependencies | ✅ | Applied narrowly | Phase A emits only minimal generated route declarations; layout/plugin behavior stays in Phase B. |
| 13 | PV9 — localized versions and sitemaps | ✅ | Applied narrowly | One-action EN/RU/KK route links are emitted; canonical/hreflang/sitemap work stays in Phase B. |
| 14 | PV10 — Google AI guidance/OpenAI crawlers | ✅ | N/A for implementation | Confirms that no AI-only prose or inclusion claim belongs in Phase A. |
| 15 | PV11 — IANA `kk` and RFC 9309 | ✅ | Applied | Kazakh uses `kk`; no project-path `robots.txt` is created. |
| 16 | PV12 — Dataset/DataDownload | ✅ | N/A | Structured metadata is explicitly Phase B scope. |
| 17 | PV13 — W3C language declarations | ✅ | Applied narrowly | Generated route metadata declares `en`, `ru`, and `kk`; translation correctness remains review-bound. |
| 18 | PV14 — GitHub rendered content/anchors | ✅ | Applied | Stable generator-owned IDs and exact-byte rendered anchor assertions implement AC-4. |
| 19 | PV15 — Pages publishing source/local testing | ✅ | N/A | Authenticated source, Jekyll layout, build, and publication are Phase B gates. |
| 20 | PV16 — RFC 8785 canonicalization | ✅ | Applied | NFC, key-sorted compact UTF-8 JSON and SHA-256 bind the ready locale payload. |
| 21 | PV17 — URL Inspection/Playwright | ✅ | N/A for Phase A | Public index and viewport assertions remain Phase B; Phase A proves Markdown structure and GitHub render semantics. |

No new PV item was found that changes the approved Phase A choices.

---

*ONB — 20260827-132641__catalog_discoverability / Phase A: One-source Multilingual Catalog | 2026-08-27*

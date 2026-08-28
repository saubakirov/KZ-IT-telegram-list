# REVIEW — 20260827-132641__catalog_discoverability / Phase B: Published discovery surface

> **Date**: 2026-08-28
> **Author**: saubakirov (Codex Reviewer)
> **Verdict**: 🔄 REVISE
> **Reviewed base**: `a67e353573ddb36183c8e5764017adff5c38a6fb`
> **Parent**: `3280a618b6d9f1a1afd87a51ef382f6922baa0ae`
> **Deployed repository SHA**: `bd7af42165c341d653e3efbb20091c131c9f7a40`
> **RF**: [RF Phase B](RF__phase-b__published_discovery.md)
> **TS**: [TS Phase B](TS__phase-b__published_discovery.md)
> **Stage files**: [`review/map.md`](review/map.md), [`review/verify.md`](review/verify.md), [`review/judge.md`](review/judge.md)

---

## Verdict History

| Review pass | Exact base | Formal result |
|---|---|---|
| Initial | `ae4898df0b0b5050cf6f23179d4e090ff04f93db` | 🔄 REVISE — F1 non-reproducing preview, F2 invalid matrix byte binding, F3 contradictory Phase-HL sitemap sentence |
| Corrected candidate | `b16aac00a7f2b94cbc2e1be29c7c30eaea9350d9` | ✅ APPROVE — repository-controlled candidate; F1–F3 closed |
| Pre-publication rebind | `bd7af42165c341d653e3efbb20091c131c9f7a40` | ✅ APPROVE — exact deployable repository-controlled candidate |
| Post-publication evidence | `a67e353573ddb36183c8e5764017adff5c38a6fb` | 🔄 REVISE — sole remaining repository-card custom-preview blocker |

No earlier verdict is rewritten. The prior approval remains valid for the exact deployed repository
bytes at `bd7af421…`; this review judges completion of the broader post-publication Phase B boundary
using the refreshed evidence base `a67e353…`.

## 1. Map

The exact approved repository candidate is publicly deployed. Authenticated Pages state binds the
build to `bd7af421…`; public EN/RU/KK pages, sitemap, JSON, CSS, and social-preview asset reproduce
the supported pinned Jekyll build. Repository description, homepage, and twelve topics are applied.
The current Executor commit is evidence-only and changes no implementation, HL, TS, ONB, status, or
journal file.

The sole material blocker is external settings evidence: authenticated GitHub GraphQL still exposes
the generated `opengraph.githubassets.com` repository-card fallback. The committed/public page-level
preview asset is correct, deterministic, and exact, but the custom repository-card upload itself has
not occurred. Official GitHub handling is UI-only here and remains blocked until the owner manually
enables the ChatGPT Chrome extension's **Allow access to file URLs** permission.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| 1 | Exact base/scope | ✅ | `a67e353…`, parent `3280a618…`; 12 RF/EV/evidence paths only |
| 2 | Phase A contract | ✅ | Digest `51db402d…`; data/README/bodies exact; 13/13 tests; predecessor tests extended, not weakened |
| 3 | Supported build/public bytes | ✅ | Exact `bd7af421…` Pages build; every route/asset hash matches |
| 4 | Locale/metadata/sitemap | ✅ | Exact EN/RU/KK routes, self-canonical and reciprocal hreflang, visible-consistent Dataset/social metadata, Liquid sitemap |
| 5 | robots/llms | ✅ | No project output; public 404/404 |
| 6 | Preview asset | ✅ | 1280×640, 27,394 bytes, `13e34836…`; two independent byte-identical rerenders |
| 7 | Responsive/browser | ✅ | Six 390×844/1366×768 EN/RU/KK cases, 30/30 representative links, images inspected |
| 8 | GitHub settings | ✅ | Description, homepage, 12 topics, Pages source/HTTPS/build |
| 9 | Repository-card custom preview | ❌ | Generated fallback remains |
| 10 | Tag/no-mutation boundary | ✅ | `data-2026-08-27` unchanged; zero external mutation by Reviewer |
| 11 | Antigravity | ✅ | Exact provenance and byte bindings; SUCCESS/PASS, no findings/nits; advisory only |

The fresh `public-http.json` is 14,666 bytes / `133cd56811d202577b7f0dca9198a2ba0831d3702d232c317f31f8203af43bf8`.
The final-Git browser matrix is 87,008 bytes / `35378c30a592629b1b4275f748d1d68c04a766f4820baef62cf40f9032135bd8`
with zero CRLF pairs. The public preview is 27,394 bytes /
`13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`.

Antigravity audit: exact executable `C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe`, exact model
`gemini-3.7-flash-high`, plan+sandbox, object-valued UTF-8 stream-json, request-review permissions,
and no bypass. Conversation `5f3edb10-3f79-4dbf-8aa8-2c3885dbc28c` is bound to prompt/input/output
SHA-256 values `e789f8d7301d0825a98a4c532121bdb4385affc31ae8f358cd96d038cdf960fb`,
`aba88a1bcc48a36f7fd3ac06268c4464ae37965dc2c30b6e118dbbbabddde8ba`, and
`b560698faada053bc896d8da0a4ba106683e2fcbde96eb970c8f474fb0b07d86`. The run is `SUCCESS` and
its advisory is exactly `PASS`, no findings, no nits. The formal verdict remains this Reviewer's.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-7 custom repository-card preview incomplete; AC-8 therefore returns REVISE. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | Frozen multilingual verified-catalog outcome and accuracy North Star are served; the static design remains sound. |
| 3 | Tech debt documented | ✅ | No separate debt; F4 is active acceptance work. |
| 4 | Style & standards | ✅ | Supported implementation and trace/evidence conventions hold. |
| 5 | Observations collected | ✅ | Sole blocker is recorded honestly; no additional observation or nit. |
| 6 | RF completeness (§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and Diagrams present and appropriate. |
| 7 | Evidence completeness — does it exist? | ✅ | E1–E9 and every attachment exist, including blocker evidence. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | It proves deployment/settings except, and affirmatively disproves, custom repository-card completion. |
| 9 | Backward compatibility | ✅ | Phase A bodies/digest/tests and consumers remain exact. |
| 10 | Safety | ✅ | Read-only review; no external mutation or secret disclosure. |

Rows 7 and 8 intentionally differ: the evidence inventory is complete, and that complete evidence
is precisely why the full post-publication claim cannot yet be approved.

## 4. Verdict

**🔄 REVISE**

The exact repository-controlled candidate `bd7af42165c341d653e3efbb20091c131c9f7a40` remains approved
and is proven deployed. The full post-publication Phase B candidate reviewed at
`a67e353573ddb36183c8e5764017adff5c38a6fb` requires one bounded correction.

| ID | Material finding | Required correction |
|---|---|---|
| F4 | GitHub repository card still uses the generated Open Graph fallback; custom `assets/social-preview.png` is not applied. | Owner enables the Chrome extension's file-URL permission; Coordinator performs only the already-authorized official GitHub UI upload; read-only GraphQL confirms a non-fallback custom image; Executor refreshes RF/EV; same Reviewer reruns. |

No other finding or nit remains. Search Console is deferred and unauthorized and is not a material
blocker. No unofficial endpoint, extension-permission change, upload, push, tag/release, Pages/
settings edit, or Search Console action was performed during this review.

### Required lifecycle / documentation / knowledge route

Keep Phase B `BLOCKED`. After the owner-only extension permission change, the Coordinator resumes the
same phase for the authorized official UI action and evidence refresh, then returns to `/tfw-review`.
Only after a future full `✅ APPROVE` may the Coordinator move to `KNW`, run `/tfw-docs`, run
`/tfw-knowledge` only if Fact Candidates exist (currently N/A), and finally move to `DONE`.

## 5. Tech Debt Collected

None. F4 is an active acceptance blocker, not deferred technical debt.

## 6. Traces Updated

- [x] This REVIEW and existing `review/map.md`, `review/verify.md`, and `review/judge.md` refreshed.
- [x] Prior verdict history preserved.
- [x] Status, journal, index, implementation, HL, TS, ONB, RF, EV, evidence, knowledge, and debt left unchanged under the Reviewer role lock.
- [x] `/tfw-docs`: deferred until a full post-publication APPROVE.
- [x] `/tfw-knowledge`: N/A — no human-only Fact Candidate.

## 7. Fact Candidates

None.

## Harness / Session Deviations

- The harness interrupted a fresh full live browser matrix after the public-root probe. Exact final-Git
  matrix parsing, all six screenshot inspections, fresh public byte checks, and the live root probe
  remain sufficient for the bounded judgment; this is not a repository finding.
- Codex handoff operation `exec-17c43827-2136-4159-a79d-2e68677e7636` moved source
  `01a04383-b2eb-78b2-80e3-0b0fc62e00d9` to destination
  `01a04881-4c15-7f21-a3c9-4a50ddcf9daa`; all five transfer steps completed and no
  `create_thread` call occurred. This is a harness/session deviation, not a repository finding.

---

*REVIEW — 20260827-132641__catalog_discoverability / Phase B: Published discovery surface | 2026-08-28*

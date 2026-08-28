# Map — "What was done?"
> **Mindset:** Experienced newcomer. Understand before judging.
> **RF:** [Phase B RF](../RF__phase-b__published_discovery.md)
> **TS:** [Phase B TS](../TS__phase-b__published_discovery.md)
> **Reviewed base:** `12765032994afc7b3276e575bef2d4bee72712d2`
> **Parent:** `e4eec09c4e54c3c9cffad912bc5152c196a9db44`
> **Deployed repository SHA:** `bd7af42165c341d653e3efbb20091c131c9f7a40`

## Understanding

Phase B projects the approved Phase A catalog through a repository-controlled GitHub Pages/Jekyll
surface. It provides exact EN, RU, and KK routes; localized canonical, reciprocal hreflang, social,
and Dataset metadata; a repository-owned Liquid sitemap; responsive language/type/intent navigation;
and a deterministic social-preview asset. It preserves the Phase A catalog bodies and digest while
extending the existing deterministic tests.

This pass reviews the bounded F4 closure only. The direct post-review ancestry is
`f97c890c98440a8442cc51e689c39b5d013da754` →
`e4eec09c4e54c3c9cffad912bc5152c196a9db44` →
`12765032994afc7b3276e575bef2d4bee72712d2`. The two Executor commits cumulatively change exactly
five paths: RF, EV, `external-checkpoint.md`, `public-http.json`, and the new authenticated Settings
screenshot. They change no implementation, specification, lifecycle, knowledge, or prior review byte.

The owner-uploaded repository preview is now independently established on three aligned surfaces:
authenticated GraphQL returns a distinct `repository-images.githubusercontent.com` URL; its PNG is
27,394 bytes with SHA-256 `13e34836df46d850b6a3fe4919dce83fa8a38cf7011da289c287696a794c194d`
and is byte-identical to `assets/social-preview.png`; and the authenticated Settings screenshot visibly
shows that custom card. The immutable capture records actor `c0rp-aubakirov` and zero Executor
mutation. The approved candidate remains deployed at exact `bd7af421…`.

## Verdict History

| Pass | Exact base | Result |
|---|---|---|
| Initial | `ae4898df0b0b5050cf6f23179d4e090ff04f93db` | 🔄 REVISE — F1–F3 |
| Corrected repository candidate | `b16aac00a7f2b94cbc2e1be29c7c30eaea9350d9` | ✅ APPROVE — repository-controlled candidate |
| Pre-publication rebind | `bd7af42165c341d653e3efbb20091c131c9f7a40` | ✅ APPROVE — exact deployable repository candidate |
| Initial post-publication evidence | `a67e353573ddb36183c8e5764017adff5c38a6fb` | 🔄 REVISE — F4 custom repository preview still fallback |
| F4 post-publication closure | `12765032994afc7b3276e575bef2d4bee72712d2` | ✅ APPROVE — full Phase B post-publication boundary |

No earlier verdict is rewritten. F1–F3 remain closed, and this pass formally closes F4.

## TS ↔ RF Alignment

| TS requirement | Current RF/evidence result | Aligned? |
|---|---|---|
| AC-1 — supported three-route Jekyll surface | Exact `bd7af421…` Pages build; public `/`, `/ru/`, `/kk/` hashes match the supported pinned build | ✅ |
| AC-2 — exact locale, canonical, reciprocal language metadata | One H1, correct route language, self-canonical, and `en`/`ru`/`kk`/`x-default` alternates on all routes | ✅ |
| AC-3 — visible-consistent Dataset/social metadata and reproducible preview | Page metadata and public 1280×640 PNG match; two fresh rerenders reproduce the exact 27,394 bytes | ✅ |
| AC-4 — repository-owned sitemap and no robots/llms surface | Three-route Liquid sitemap exact; public and built robots/llms absent | ✅ |
| AC-5 — responsive browser presentation | Six 390×844/1366×768 EN/RU/KK cases and 30 representative links pass; images inspected | ✅ |
| AC-6 — Phase A preservation | Digest `51db402d…`, data/README/bodies exact, 12 predecessor tests unchanged, one preservation test added | ✅ |
| AC-7 — publication/settings package applied and evidenced | Pages, description, homepage, twelve topics, and custom repository preview are exact; protected tag untouched | ✅ |
| AC-8 — advisory and formal independent review | Exact Antigravity advisory remains SUCCESS/PASS with no findings/nits; this formal review approves | ✅ |
| AC-9 — minimal, traceable, resumable scope | Five-path evidence-only closure, clean ownership/attribution, and zero Executor/Reviewer external mutation | ✅ |

## Findings and Dispositions

| ID | Prior finding | Final disposition |
|---|---|---|
| F1 | Preview raster did not reproduce | CLOSED at `b16aac…`; two further rerenders in this pass are exact. |
| F2 | Browser-matrix byte binding was invalid | CLOSED at `b16aac…`; current canonical-LF six-case matrix remains exact. |
| F3 | Phase-HL sitemap wording contradicted the implementation | CLOSED at `b16aac…`; Phase HL/TS/implementation consistently say repository-owned Liquid page, while frozen Master HL remains exact. |
| F4 | Repository card used GitHub's generated fallback | CLOSED at `1276503…`; non-fallback GraphQL URL, exact HTTP bytes, and visible Settings card agree. |

No material finding or nit remains.

## Deviations from TS

- No implementation or acceptance-scope deviation was found.
- Search Console remains explicitly deferred and unauthorized; it is N/A to the approved acceptance
  boundary and is not a finding.
- The immutable evidence capture binds authenticated actor `c0rp-aubakirov`. The Reviewer used a
  separate configured credential session only to revalidate the same read-only state; this does not
  rewrite the recorded capture identity.

## Harness / Session Deviations

- The same logical Reviewer lineage resumed after harness recovery; exact base and clean state were
  re-established before verification.
- A prior fresh browser rerun was interrupted after its public-root probe. The final-Git six-case
  matrix, all six screenshots, fresh public bytes, and representative-link checks remain sufficient.
- Handoff operation `exec-17c43827-2136-4159-a79d-2e68677e7636` transferred source
  `01a04383-b2eb-78b2-80e3-0b0fc62e00d9` to destination
  `01a04881-4c15-7f21-a3c9-4a50ddcf9daa`; all five steps completed and no `create_thread` call
  occurred. This is a session-identity deviation, not a repository finding.
- `gh` was unavailable in the recovered shell. The same current state was revalidated through the
  configured Git credential helper and read-only GitHub REST/GraphQL requests; no credential was
  printed or persisted.

## Checkpoint

**Self-check:**
- [x] RF §§1–5, TS DoD, frozen Master-HL authority, Phase HL, and ONB read.
- [x] Exact reviewed base, parent, two-commit ancestry, five-path scope, and attribution proved.
- [x] Every TS acceptance criterion mapped to current RF/evidence.
- [x] Prior verdict history and F1–F4 dispositions preserved.
- [x] External publication state revalidated read-only; no external mutation performed.

Stage complete: YES

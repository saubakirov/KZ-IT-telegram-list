# Map — "What was done?"
> **Mindset:** Experienced newcomer. Understand before judging.
> **RF:** [Phase B RF](../RF__phase-b__published_discovery.md)
> **TS:** [Phase B TS](../TS__phase-b__published_discovery.md)
> **Reviewed base:** `a67e353573ddb36183c8e5764017adff5c38a6fb`
> **Parent:** `3280a618b6d9f1a1afd87a51ef382f6922baa0ae`
> **Deployed repository SHA:** `bd7af42165c341d653e3efbb20091c131c9f7a40`

## Understanding

Phase B projects the approved Phase A catalog through a repository-controlled GitHub Pages/Jekyll
surface. It provides exact EN, RU, and KK routes; localized canonical, reciprocal hreflang, social,
and Dataset metadata; a repository-owned Liquid sitemap; responsive language/type/intent navigation;
and a deterministic social-preview asset. It preserves the Phase A catalog bodies and digest while
extending the existing deterministic tests.

The review history is preserved rather than overwritten:

| Pass | Exact base | Result |
|---|---|---|
| Initial | `ae4898df0b0b5050cf6f23179d4e090ff04f93db` | 🔄 REVISE — F1–F3 |
| Corrected repository candidate | `b16aac00a7f2b94cbc2e1be29c7c30eaea9350d9` | ✅ APPROVE — repository-controlled candidate |
| Pre-publication rebind | `bd7af42165c341d653e3efbb20091c131c9f7a40` | ✅ APPROVE — exact deployable repository candidate |
| Post-publication evidence | `a67e353573ddb36183c8e5764017adff5c38a6fb` | 🔄 REVISE — custom repository-card preview remains unapplied |

The current base is an evidence-only continuation. Its parent is the prior Reviewer commit, and the
current Executor commit changes RF/EV and ten evidence attachments only. The implementation, HL, TS,
ONB, status, and journal are unchanged. A direct comparison from deployed SHA `bd7af421…` confirms
zero implementation-path changes. GitHub Pages reports an exact `bd7af421…` build; public EN/RU/KK,
sitemap, JSON, CSS, and preview bytes match the supported local build. Repository description,
homepage, and twelve topics are applied.

One externally visible acceptance item remains incomplete: authenticated GitHub GraphQL still
reports the generated `opengraph.githubassets.com` fallback for the repository card. The official
GitHub custom-image flow is UI-only in this environment and is blocked until the owner manually
enables the ChatGPT Chrome extension's **Allow access to file URLs** permission. That owner-only
dependency is recorded honestly; no unofficial upload path or external mutation was attempted.

## TS ↔ RF Alignment

| TS requirement | Current RF/evidence result | Aligned? |
|---|---|---|
| AC-1 — supported three-route Jekyll surface | Exact `bd7af421…` Pages build; public `/`, `/ru/`, `/kk/` hashes match supported pinned build | ✅ |
| AC-2 — exact locale, canonical, reciprocal language metadata | One H1, correct route language, self-canonical, and `en`/`ru`/`kk`/`x-default` alternates on all routes | ✅ |
| AC-3 — visible-consistent Dataset/social metadata and reproducible preview | Page metadata and public 1280×640 PNG match; two independent rerenders reproduce 27,394 exact bytes | ✅ |
| AC-4 — repository-owned sitemap and no robots/llms surface | Three-route Liquid sitemap exact; public and built robots/llms both absent | ✅ |
| AC-5 — responsive browser presentation | Six committed 390×844/1366×768 EN/RU/KK cases and 30 representative links pass; images inspected | ✅ |
| AC-6 — Phase A preservation | Digest `51db402d…`, data/README/bodies exact, 12 predecessor tests unchanged, one preservation test added | ✅ |
| AC-7 — approved publication/settings package applied and evidenced | Pages, description, homepage, and topics applied; repository-card custom preview is still fallback | ❌ BLOCKED |
| AC-8 — advisory and formal independent review | Antigravity PASS is exact; this formal review returns REVISE because AC-7 is incomplete | 🔄 |
| AC-9 — minimal, traceable, resumable scope | Evidence-only current commit, clean ownership, no unauthorized mutation | ✅ |

## Findings

| ID | Finding | Materiality | Required disposition |
|---|---|---|---|
| F4 | The repository card still uses GitHub's generated Open Graph fallback; the approved custom `assets/social-preview.png` has not been uploaded through the official UI. | Material to the Phase B publication/settings acceptance boundary (AC-7); not an implementation defect. | Owner manually enables the Chrome extension file-URL permission; Coordinator uses only the already-authorized official GitHub UI flow; read-only GraphQL verifies a non-fallback custom image; Executor refreshes RF/EV; Reviewer reruns. |

F1–F3 remain closed. No additional finding or nit was identified.

## Deviations from TS

- No unauthorized implementation deviation was found. AC-7 is incomplete, not silently narrowed:
  the repository-level custom preview remains the generated fallback.
- Search Console remains explicitly deferred and unauthorized under the approved boundary; it is
  not work that was shipped under a different name and is not a finding.
- The browser interruption and handoff identity transformation below are execution-harness
  deviations only. Neither changes repository bytes, authority, or evidence truth.

## Harness / Session Deviations

- A fresh six-case live browser rerun was interrupted by the harness after the public-root probe.
  This is not a repository finding: the exact committed matrix was parsed from the final Git blob,
  all six screenshots were independently inspected, every public output hash was freshly fetched,
  and the public root was additionally inspected live.
- Codex handoff operation `exec-17c43827-2136-4159-a79d-2e68677e7636` moved source task
  `01a04383-b2eb-78b2-80e3-0b0fc62e00d9` to destination
  `01a04881-4c15-7f21-a3c9-4a50ddcf9daa`. All five transfer steps completed and no
  `create_thread` call occurred. This identity transformation is a harness/session deviation, not a
  repository or evidence finding.

## Checkpoint

**Self-check:**
- [x] Exact reviewed base and parent identified.
- [x] Current evidence-only scope and deployed implementation binding proved.
- [x] Every TS acceptance criterion mapped to current RF/evidence.
- [x] Prior verdict history and F1–F3 closure preserved.
- [x] Sole material blocker separated from harness/session deviations.
- [x] No external mutation performed.

Stage complete: YES

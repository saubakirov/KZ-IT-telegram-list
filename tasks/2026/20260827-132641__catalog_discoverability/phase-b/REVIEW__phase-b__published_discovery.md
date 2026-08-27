# REVIEW — 20260827-132641__catalog_discoverability / Phase B: Published discovery surface

> **Date**: 2026-08-27
> **Author**: saubakirov (Codex Reviewer)
> **Verdict**: 🔄 REVISE
> **Reviewed base**: `ae4898df0b0b5050cf6f23179d4e090ff04f93db`
> **RF**: [RF Phase B](RF__phase-b__published_discovery.md)
> **TS**: [TS Phase B](TS__phase-b__published_discovery.md)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file synthesizes the stage findings. It does not claim publication or satisfy the outstanding
> external authorization/public-evidence checkpoint.

---

## 1. Map

The candidate adds a supported repository-controlled Jekyll projection of the approved Phase A
catalog: one layout/stylesheet, generated EN/RU/KK front matter, exact localized discovery metadata,
a Liquid three-route sitemap, and a checked-in social preview. It extends all twelve Phase A tests,
adds built-output assertions, and supplies build/browser/advisory/external-checkpoint evidence while
making zero external mutation.

The Coordinator-authorized sitemap change is present in the implementation and TS: the transitively
installed `jekyll-sitemap` plugin is not enabled, checked-in Liquid owns `sitemap.xml`, and the
Executor's later `d6c2c2c679033d06f1d1f4361227e8485de1be48` commit changes only one trailing space in
the build-log trace. The integrated implementation commit `5217d928ae0ce04f7f83d1e8d3b02bdb0075c220`
is blob-equivalent on implementation/evidence paths to Executor commit
`07bf62b77e5a1d6a1233bba47b63dc9e93ea9a7c`.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| 1 | Frozen authority and Phase A contract | ✅ | Frozen sections unchanged from `00a21bb9e1475568a9baef4a9be3b0a8e72e383e`; actual Phase A RF/REVIEW read; digest exact at `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`. |
| 2 | 13/13 implementation paths and final integrated diff | ⚠️ | Scope and implementation architecture match TS; the preview reproduction claim fails (F1). |
| 3 | Schema, generator, and Phase A regression preservation | ✅ | Schema/generator checks pass; 13/13 tests pass; all twelve predecessor tests remain unchanged and one preservation test is added. |
| 4 | Supported GitHub Pages/Jekyll build | ✅ | Fresh exact-commit archive build passes in pinned official image digest; Ruby 3.3.4, Bundler 2.5.11, Jekyll 3.10.0; fresh output hashes match EV. |
| 5 | EN/RU/KK routes, head, Dataset, social, sitemap, robots/llms | ✅ except preview reproducibility | Exact routes/self-canonicals/four alternates/visible-consistent metadata/sitemap pass; robots/llms absent; checked-in PNG is valid and legible but its documented rerender differs (F1). |
| 6 | Responsive/browser evidence | ✅ content; ❌ byte binding | Six independent 390×844/1366×768 cases pass; screenshots match. EV records the wrong `browser-matrix.json` hash (F2). |
| 7 | Antigravity advisory provenance and bytes | ✅ | Exact executable/model/plan+sandbox/object-valued UTF-8 NDJSON/request-review/no bypass/conversation/hashes verified; PASS, no findings, no nits. |
| 8 | Coordinator sitemap revision and trace-only whitespace fix | ❌ trace wording | Implementation revision and whitespace-only commit are correct, but Phase B HL §3 retains a contradictory plugin sentence (F3). |
| 9 | Current GitHub/Pages/public checkpoint and runbook | ✅ repository boundary only | Fresh authenticated/public read-only facts match; target settings/runbook/tag non-reuse exact; mutation count remains zero; public RU/KK/sitemap are still 404. |
| 10 | Knowledge/citation/evidence inventory | ⚠️ | 21/21 citation rows resolve and semantically hold; all evidence files exist, but F1/F2 prevent sufficiency. |

Raw verification, exact commands, hashes, route facts, and citation audit are in
[`review/verify.md`](review/verify.md).

Antigravity audit: executable `C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe` (version 1.1.22;
review-time executable SHA-256 `059b96c1069206158d340ee2a8912894eca5002195e62b8cd281c26c01cd794e`), exact model
`gemini-3.7-flash-high`, plan+sandbox, object-valued UTF-8 stream-json, request-review permissions,
zero tool steps, and no permission-bypass flag. Conversation
`4e1d1d0d-5343-4cee-a6a4-840088a02947` is bound to prompt/input/output SHA-256 values
`722e0e1b5dffe7a4c33925a79bd55342f12da51f9e19916d201ea0c0687af759`,
`c74627cd6ba8800287a4604420af6c7f8a549577b7d3fc0fa2d4b9480a0f46ef`, and
`0b9bb339c374d64950f2fa74246b4f90cbc973199d57dce95e98eead6e497a09`. Its advisory is exactly
`PASS`, disposition not required, findings none, nits none. Antigravity remains advisory; this REVIEW
issues the formal verdict.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-3 fails; AC-8 cannot receive formal approval; AC-9 trace integrity is incomplete. |
| 2 | Purpose Check + design soundness | ✅ | The result serves the frozen multilingual verified-catalog purpose without adjacent surfaces; the architecture is sound. Findings are bounded execution/trace defects. |
| 3 | Tech debt documented | ✅ | RF has no observations; F1–F3 are in-scope revision items, not deferrable debt. |
| 4 | Style & standards | ❌ | EV byte integrity and Phase HL internal consistency fail F2/F3. |
| 5 | Observations collected | ✅ | No out-of-scope observation was found; revision findings remain in scope. |
| 6 | RF completeness (§7–9 present) | ✅ | Fact Candidates, Strategic Insights, and Diagrams are present and appropriately populated. |
| 7 | Evidence completeness — does it exist? | ✅ | All RF/EV attachments exist. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Preview reproduction is not proved and the matrix hash does not bind to the committed file. |
| 9 | Backward compatibility | ✅ | Phase A data/README/body/digest/targets/fragments/tests remain exact. |
| 10 | Safety | ✅ | Read-only external access, zero mutation, no secret disclosure, non-force/tag-preserving runbook. |

## 4. Verdict

**🔄 REVISE**

The repository-controlled site candidate is technically strong: fresh supported build, exact locale
routes and metadata, Liquid sitemap, responsive browser behavior, Phase A preservation, current
external checkpoint, and Antigravity PASS all independently hold. Formal approval is still
unwarranted because one acceptance claim is not reproducible and two durable trace statements do not
match the reviewed bytes/architecture. These are bounded corrections, so REVISE—not REJECT—is the
proportionate verdict.

### Items to fix

1. **Executor — AC-3 asset reproduction:** make the checked-in PNG byte-reproducible from the
   checked-in vector by the documented command/environment, or regenerate it through a completely
   pinned method. The current exact command under CairoSVG 2.8.2 yields 27,394 bytes / `13e34836…`,
   not 27,391 bytes / `323c1243…`. Rerun and rebind every affected deterministic, visual,
   Antigravity, EV, and RF artifact.
2. **Executor — EV byte binding:** replace the nonexistent `b83d6fdc…` browser-matrix binding with a
   freshly verified binding to the final attachment. Current committed bytes are 67,908 bytes /
   `7ea6616a…`; update EV/RF only after all revised evidence is final.
3. **Coordinator — derived Phase HL consistency:** correct Phase B HL §3's sentence that says the
   sitemap is produced by a plugin. It must agree with the already-authorized repository-owned
   Jekyll/Liquid architecture. No frozen Master HL amendment is needed.
4. Integrate the bounded corrections on one new exact base, preserve zero external mutation, and
   return that base to this same Reviewer task. The external authorization/public-evidence checkpoint
   remains outstanding even after a later local APPROVE.

### Required lifecycle

Do **not** advance Phase B to `KNW`, `BLOCKED`, `DONE`, publication, or the external mutation
checkpoint. The REVISE verdict routes this same phase back to bounded execution/Coordinator trace
correction. Project precedent records the revised handoff as `RF`, then reopens `REV` for this same
Reviewer on the newly integrated exact base. The Coordinator owns those state/journal transitions.

## 5. Tech Debt Collected

No tech-debt item. F1–F3 are acceptance-blocking, in-scope revision work and must not be deferred to
the backlog.

## 6. Traces Updated

- [ ] Phase B `status.md` / transition journal — intentionally not modified under the delegated
  Reviewer-only write boundary; Coordinator must route the REVISE loop.
- [ ] Master/Phase HL status — intentionally not modified; the Coordinator owns F3 and lifecycle.
- [x] Review stage traces and this REVIEW are the only durable files created by the Reviewer.
- [x] Other project files checked for stale/unauthorized information; no implementation, HL, TS, ONB,
  RF, EV, evidence attachment, TECH_DEBT, knowledge, index, status, or journal file was changed.
- [x] `tfw-docs`: N/A — verdict is REVISE and no knowledge/documentation close is authorized.
- [x] `tfw-knowledge`: N/A — no human-only Fact Candidate exists.

## 7. Fact Candidates

No fact candidates. Every review observation was independently discoverable from files, commands,
or read-only external state and therefore fails the Human-Only Test.

---

*REVIEW — 20260827-132641__catalog_discoverability / Phase B: Published discovery surface | 2026-08-27*

# REVIEW — 20260827-132641__catalog_discoverability / Phase A: Multilingual Catalog

> **Date**: 2026-08-27
> **Author**: saubakirov (Codex Reviewer)
> **Verdict**: 🔄 REVISE
> **Digest reviewed**: `80ee30ba87003b61de862d63f0a01cea213d5bc08320019af6b4e513fbb33fd0`
> **Review base**: `8499d7da395e1368a8d17c06f0d11692aac4002a`
> **RF**: [RF Phase A](RF__phase-a__multilingual_catalog.md)
> **TS**: [TS Phase A](TS__phase-a__multilingual_catalog.md)
> **Stage files**: [`review/map.md`](review/map.md), [`review/verify.md`](review/verify.md), [`review/judge.md`](review/judge.md)
> This file synthesizes the stage findings. The stage files hold the raw audit record.

---

## 1. Map

The Executor added explicit EN/RU/KK catalog content and intent definitions to the canonical JSON,
extended one generator to produce four projections, strengthened validation, and added twelve
deterministic regression tests. The reviewed implementation is exactly eight paths; required
Executor evidence binds all 401 locale keys and the four generated outputs to one digest, while
Phase B, publication, repository settings, and every external mutation remain outside the diff.

The frozen Master HL baseline, derivation-only Phase A HL, approved TS, RES decisions, ONB, RF, EV,
changed-key attachment, implementation, and generated outputs were all independently inspected.
Map alignment is complete; the decisive dispute is whether the recorded AC-6 language pass is true.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|------------------|--------|----------|
| 1 | Frozen Master HL and approved-base authority | ✅ | Baseline recovered at `00a21bb…`; frozen §§1, 3–7 and append-only §12 remain unchanged; no amendment. Approved TS base `a646f597…`, requested review base `8499d7da…`. |
| 2 | RF file sample and evidence resolution | ✅ 100% | All 12 RF-claimed files opened; minimum was 6. All seven EV records/artifacts exist. |
| 3 | TS AC-1–AC-5 and AC-7 / all DoF exclusions | ✅ | Schema, currency, tests, independent source/base audit, exact output comparison, GitHub render, and scope diff all reproduce. |
| 4 | TS AC-6 and EV E6 | ❌ | Independent exact-byte `gemini-3.7-flash-high` run returns `FINDINGS`, contradicting the recorded `PASS`; seven material Russian defects are confirmed in source. |
| 5 | Approved-base fact invariants | ✅ | 38/20/4/2 cardinalities; zero changes to identity, category, count, date, type, archive date, or canonical archive reason. |
| 6 | Generated provenance and byte identity | ✅ | All four committed projections equal independent generator output; recorded SHA-256 values reproduce. |
| 7 | Public Markdown behavior | ✅ | Read-only GitHub render: HTTP 200, one H1, 64/64 Telegram targets, 71/71 fragments, no missing/extra targets or duplicate normalized IDs. |
| 8 | Exact path, new-file, modified-file, and LOC budgets | ✅ | Implementation: 8 paths, 4 new, 4 modified, 2,650 LOC delta. Full approved-base range with mandatory Reviewer files: 21 paths, 15 new, 6 modified; hard caps 30/15/30 and 3,000 implementation LOC are met. |
| 9 | HL/ONB knowledge and primary-source citations | ✅ | 42/42 citation applications resolve and match meaning/relevance; 0 irrelevant, 0 hallucinated. |
| 10 | Phase B/external mutation absence | ✅ | No forbidden Phase B path, deploy, setting mutation, publication, push, tag, or release. Reviewer network actions were read-only or sandboxed advisory calls. |

> Raw verification log: see [`review/verify.md`](review/verify.md). The AC-6 discrepancy triggered
> 100% RF-file verification rather than the configured 42% minimum.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | AC-6 fails on the exact reviewed digest; AC-1–AC-5 and AC-7 pass. |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | Frozen HL §1 promises visitors can “choose English, Russian, or Kazakh, and reach the right verified community”; misleading Russian copy threatens that materially, and the one-source/four-projection review-bound design is the sound P1–P7 mechanism for preventing it. |
| 3 | Tech debt documented | ✅ | RF §6 is present and accurately reports no out-of-scope observations; current language defects are acceptance work, not deferred debt. |
| 4 | Style & standards | ❌ | Structural/code standards hold, but Russian grammar, neutrality, and semantic fidelity do not meet AC-6 or the no-manual-cleanup quality standard. |
| 5 | Observations collected | ✅ | RF §6 is present; full review found no separate out-of-scope issue requiring debt capture. |
| 6 | RF completeness (§7–§9 present) | ✅ | Fact Candidates, Strategic Insights, and Diagram sections exist and are substantively appropriate. |
| 7 | Evidence completeness — does it exist? | ✅ | E1–E7 and all named artifacts/records exist. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | E6’s advisory `PASS` does not reproduce; same-model exact-byte evidence and direct source inspection establish contrary material findings. |
| 9 | Backward compatibility | ✅ | Existing source/generator commands, identities/facts, archive records, North Star, destinations, and generated consumers remain intact. |
| 10 | Safety | ✅ | No secrets, destructive action, permission bypass, deployment, publication, settings change, or other external mutation. |

## 4. Verdict

**🔄 REVISE**

The formal Phase A language verdict for digest
`80ee30ba87003b61de862d63f0a01cea213d5bc08320019af6b4e513fbb33fd0` is `REVISE`.
The deterministic implementation is technically sound and purpose-aligned, but the exact candidate
does not satisfy AC-6: its Russian projection contains confirmed grammar, tone, and semantic-fidelity
defects, while RF/EV incorrectly records `PASS` with no findings. Under the owner-delegated formal
pipeline, that content/evidence mismatch cannot be accepted and requires no separate human chat
approval to establish this verdict.

### Items to fix

1. **Correct the canonical Russian source copy in `data/communities.json`.** At minimum disposition
   these exact material keys before regeneration:
   - `ui.ru.stats.bots` (`4 ботов` renders incorrectly; use the grammatically valid count form);
   - `certkznews.description_ru` (`кибер атак` compound spelling);
   - `bluescreenkz.description_ru` (neutrality and EN/KK topic fidelity);
   - `dwhkz.description_ru` (natural Russian and DWH/Big Data scope fidelity);
   - `teamleads_kz.description_ru` (replace the slogan with the community scope);
   - `ml_jobs_kz.description_ru` (grammar, neutral tone, jobs-only fidelity);
   - `automation_kz.description_ru` (topic fidelity; do not narrow it to a young-engineer mission).
2. **Disposition the accepted Russian copy-edit nits in the same source pass.** Normalize compound or
   hyphenated specialist/job/article terms, `Ruby on Rails` casing/terminology, punctuation such as
   `о штрафах/налогах/пени`, and slang/promotional phrasing where it conflicts with the catalog’s
   concise neutral voice. The advisory suggestions to replace the `1C` brand token with a Cyrillic
   confusable and to treat Markdown escape backslashes as rendered characters are rejected; no change
   is required for those two nits.
3. **Regenerate; do not hand-edit outputs.** Run the generator so `README.md`, `index.md`,
   `ru/index.md`, and `kk/index.md` are all derived from the corrected source.
4. **Refresh the content-bound review record.** Any wording change invalidates this digest. Recompute
   the canonical payload SHA-256 and exact changed-key set; update source review metadata,
   `evidence/review_changed_keys.json`, EV, and RF so all hashes, findings, and dispositions describe
   the new bytes.
5. **Rerun every required gate after the final wording change:**
   `python scripts/test_catalog_generation.py`, `python scripts/validate_schema.py`,
   `python scripts/generate_readme.py --check`, `git diff --check`, the approved-base invariant/path/LOC
   audit, and the exact-byte read-only GitHub Markdown-render comparison.
6. **Rerun the final advisory on the complete new EN/RU/KK bytes.** Use the installed exact model
   `gemini-3.7-flash-high`, `--mode plan --sandbox`, stream-json input/output with an object-valued
   `message.content`, explicit UTF-8, and no permission bypass. Record the new prompt hash,
   conversation, digest, result, every finding, and its disposition in EV/RF.
7. Return the refreshed unchanged candidate to this same formal Reviewer pipeline for a new
   digest-bound verdict. Do not begin Phase B or mutate any external surface.

## 5. Tech Debt Collected

No items. RF §6 reports no observations, and this review found no separate out-of-scope debt. The
language findings above are current Phase A acceptance defects and must not be deferred to backlog or
Phase B.

## 6. Traces Updated

- [x] `review/map.md`, `review/verify.md`, `review/judge.md`, and this REVIEW artifact created.
- [ ] Task/phase `status.md`, journal, and `tasks/00-INDEX.md` — intentionally not modified under the delegated Reviewer write boundary; the Coordinator owns state transitions and closure.
- [ ] HL status — intentionally not modified; verdict is REVISE and the Coordinator owns lifecycle changes.
- [x] Other project files checked for stale or unauthorized information; no non-review file was changed by the Reviewer.
- [x] `tfw-docs`: N/A — there is no approved result to document and the delegated Reviewer write boundary forbids it.
- [x] `tfw-knowledge`: N/A — no human-only fact candidate and the delegated Reviewer write boundary forbids it.

This trace-update boundary is the only workflow deviation: canonical review state/journal updates are
reserved to the Coordinator by the owner’s explicit contract. It does not weaken any review gate.

## 7. Fact Candidates

No fact candidates. The owner’s messages supplied process authority and invocation shape for this
review, not a new enduring domain fact; all review findings are independently discoverable from the
repository, tools, or generated bytes.

---

*REVIEW — 20260827-132641__catalog_discoverability / Phase A: Multilingual Catalog | 2026-08-27*

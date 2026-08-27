# RES — TFW-4: Verify Phase C empirical assumptions

> **Date**: 2026-08-26
> **Author**: Researcher (Codex)
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> **Mode**: Pipeline (focused)

---

## Research Context

Iteration 1 tested the three empirical assumptions that the frozen TFW-4 HL requires before Phase C is designed: whether current public Telegram pages remain compatible with the member-count parser, whether a bounded catalog sample reveals a dead/private handle or rate limiting, and whether the generated category links resolve against GitHub's live heading ids. The investigation stayed read-only and bounded: Gather used five HTTP requests (the configured soft ceiling), Extract used eight at the existing throttle, and Challenge used one live GitHub page request. It did not update catalog data, run the 63-entry sweep, alter the HL or control file, or perform release work.

## Briefing

The scope, probe budgets, stage plan, and three guiding questions are recorded in [1_briefing.md](1_briefing.md). The Coordinator-fixed focus was H1, H2, and H4 under the focused one-loop mode.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Split compound H1 into count compatibility and liveness classification. | Live group/channel previews still match the count regexes. A malformed invalid route returns a generic HTTP 200 landing page without `tgme_page_error` and is incorrectly classified alive, while a random valid-form probe returns the same ambiguous C4 shell as a catalog group. One compound verdict would hide the distinction. |
| D2 | Treat target-specific preview, count availability, and liveness as separate signals. | Three bot previews are target-specific and alive-looking without a numeric count; a contact shell has no count but is indistinguishable between a catalog handle and the unresolved random valid-form probe. |
| D3 | Keep H2 inconclusive and make no archive recommendation. | The sample measured 0/8 explicit negative markers and no HTTP 429, not a 0/8 dead rate. C4 contact shells cannot be classified alive, private, or dead from the observed response alone. |
| D4 | Confirm H4 for every currently emitted anchor, not for every defined category. | All 13 TOC hrefs emitted for used categories exactly matched GitHub's live heading ids. Five of 18 definitions are unused and therefore have no heading or link to observe. |
| D5 | Keep the H1 classifier correction inside Phase C and propose a structural §5 gate. | Phase C already owns link classification, verification dates, dead-list output, and archive input. A separate task would split one safety boundary, but the current DoD can still pass while treating a contact shell as verified alive. |
| D6 | Require a second research iteration on C4 identity evidence before Phase D. | `min_iterations: 2` is a hard floor, and the current unresolved contact-shell state can prevent an honest DoD 22 verdict for `mobile_developers_kz`. |
| D7 | Report, but do not repair, research-control metadata drift. | `iterations.yaml` is Coordinator-owned. It names baseline `f871951` and A2 as proposed, while history contains later freeze `70ddfa6` and the current HL records A2 approved. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Is there a bounded, read-only target-identity signal that distinguishes a legitimate private/contact-only handle from an absent handle when both return C4? | Open — iteration 2 | Not answered by the `t.me/{handle}` HTML observed in iteration 1. |
| Q2 | If no independent C4 signal exists, what evidence must Phase D require before refreshing `last_verified` or proposing archive? | Open — depends on Q1 | At minimum, iteration 1 rules out treating HTTP 200/contact title alone as proof and rules out automatic archive. |
| Q3 | Can frozen DoD 22 remain achievable for every current entry without superseding it? | Open — iteration 2 / owner gate | It remains achievable only if C4 can be independently resolved or the affected entry is handled through owner-evidenced triage. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | `t.me/{handle}` exposes compatible member/subscriber counts, and a dead handle yields `tgme_page_error`. | needs-research | 🟠 PARTIAL — count clause confirmed; marker assumption refuted for malformed invalid input and unverified for genuinely dead/private targets | Gather G2-G4: `itmankz` and `workitkz` matched; a malformed route returned a generic marker-free landing page, and a random valid-form probe returned an ambiguous marker-free contact shell. |
| H2 | At least one of 63 catalog handles is dead/private, so Phase D exercises the archive path with real data. | needs-research | 🟡 INCONCLUSIVE | Extract E1-E3: 0/8 explicit negative markers; one C4 catalog response is ambiguous; no catalog-wide inference is valid. |
| H4 | The generator's category href expression matches GitHub heading anchors for every category name. | needs-research | 🟢 CONFIRMED FOR EMITTED ANCHORS | Challenge C1: 13/13 emitted hrefs matched the live GitHub ids; five unused definitions emitted no href or heading. |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** The current HL and Coordinator-owned control file were not edited.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Add a classifier defect alongside F6: HTTP 200 contact shells without target-specific preview metadata are currently treated as alive, and a generic Telegram landing page can produce a false count `0` from the phrase `200,000 members`. | Gather G3-G4 |
| R2 | §8 Dependencies | Mark network access to `t.me` verified for the bounded research environment; mark public group/channel count markup compatible; keep catalog-wide rate-limit behavior and C4 identity resolution unverified. | Gather G2; Extract E1 |
| R3 | §9 Risks | Expand the parser risk from “count regex may stop matching” to the higher-impact false-positive liveness path: contact shells and site-wide landing pages can pass the current negative-marker test. Mitigation: classify target-specific previews, ambiguous shells, generic pages, and explicit failures separately before Phase D. | Gather G3; Extract E2; Challenge C2 |
| R4 | §10 H1 | Replace the compound open status with separate results: count markup confirmed for public group/channel previews; `tgme_page_error` rejection refuted for malformed invalid input; genuinely dead/private target behavior still unverified. | D1; Gather G2-G4 |
| R5 | §10 H2 | Set `inconclusive`; record 0/8 explicit failure markers, one ambiguous C4 catalog handle, and the prohibition on extrapolating a full-catalog dead rate from the bounded sample. | D3; Extract E3 |
| R6 | §10 H4 | Set `confirmed-for-emitted-anchors`; state that 13 categories are used/emitted and 5 of 18 definitions are unused, so the live README exposes 13 testable anchors. | D4; Challenge C1 |
| R7 | §10 Proposed RESEARCH Focus | Set iteration 2 focus to bounded C4 identity discrimination and the evidence rule for ambiguous responses; do not repeat the 8-handle sample or expand into the 63-entry Phase D sweep. | D6; Open Questions Q1-Q3 |

### Amendment Proposals — frozen sections, owner verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| A1 | §5 Definition of Done | `EXTEND` | Add a classifier acceptance criterion before Phase D: (a) a target-specific public preview may be verified alive when no numeric count is present; (b) an HTTP 200 contact shell without positive preview evidence is reported as ambiguous and does not refresh `last_verified` or become an automatic archive candidate; and (c) member counts are parsed only from target-specific preview content, never site-wide landing-page prose. Verify with C3, C4, and C5 fixtures or captured response shapes. | Gather G3-G4 showed a malformed invalid route classified alive with count 0 and a random valid-form probe returning an ambiguous contact shell. Extract E1-E2 showed three valid no-count bot previews and `mobile_developers_kz` in the same C4 shape as the random probe. | A bounded classifier change plus deterministic tests/fixtures inside already-scoped Phase C; Phase D waits until the gate passes. No new phase or external dependency is required. | Merely refine §9 or TS guidance: rejected because DoD 22 can still pass on a freshly dated but unverified contact shell. Create TFW-5 and defer Phase D: rejected because Phase C already owns classification, archive input, and verification-date semantics. Treat every HTTP 200 as alive: rejected because C4 and C5 demonstrate false-positive outcomes. |

## Fact Candidates

No fact candidates. The delegated message supplied operational scope and authority, not enduring human-only project knowledge.

## Strategic Insights (Research)

No strategic insights. No human domain correction or strategic briefing occurred during this delegated research iteration.

## Findings Map

```text
t.me response
│
├─ explicit negative marker or non-success HTTP ──► failed/non-responding
│                                                   retry + owner evidence before archive
│
└─ HTTP 200
   │
   ├─ target-specific public preview
   │  ├─ numeric members/subscribers ─────────────► verified alive + observed count
   │  └─ no numeric count (C3 bots) ──────────────► verified preview; count remains absent
   │
   ├─ contact shell, no positive preview (C4) ────► AMBIGUOUS
   │                                               no inferred death, no fresh verification date
   │
   └─ site-wide landing page (C5) ────────────────► not target evidence
                                                   never parse generic “200,000 members”

GitHub README
└─ 18 category definitions
   ├─ 13 used/emitted ────────────────────────────► 13/13 live anchor matches
   └─ 5 unused/not emitted ───────────────────────► no live anchor claim to test
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (partial: count confirmed, marker rejection refuted for malformed invalid input and unverified for genuinely dead/private targets), H2 (inconclusive), H4 (confirmed for 13 emitted anchors)
- **Hypotheses deferred:** None
- **Gaps discovered:** C4 target identity cannot be established from the observed contact shell; DoD 22 may be unsatisfiable for an unresolved C4 entry; five unused categories have no live headings; `iterations.yaml` trails the current freeze and A2 status.
- **Superseded decisions:** None

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | Distinguish legitimate private/contact-only handles from absent handles in C4. | Without a positive signal, the pipeline can either falsely date a dead entry or falsely archive a private one. | Test bounded, read-only target-identity signals and document what each proves; do not run the 63-entry sweep. |
| 2 | Resolve DoD 22 against an unresolved C4 entry. | The frozen contract requires every live entry to receive an observed date, but iteration 1 cannot prove whether `mobile_developers_kz` is live. | Determine whether independent evidence makes DoD 22 achievable; if not, give the Coordinator evidence for a separate §5 proposal rather than silently weakening the claim. |
| 3 | Reconcile research control with the current contract baseline. | Iteration 2 must cite the actual frozen contract and settled A2 status. | Coordinator updates `baseline_commit`, `baseline_history`, and A2 metadata before dispatching iteration 2. |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [x] **MORE NEEDED** — the hard minimum is two iterations, and C4 identity/DoD 22 remains a blocking research gap before Phase C can be safely specified.
- [ ] **BLOCKED** — no external blocker; the next iteration needs Coordinator scoping.

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 1 confirmed that public group/channel counts and all currently emitted GitHub anchors still work, but it also found the more consequential failure that the Briefing's compound H1 concealed: Telegram serves marker-free HTTP 200 pages that the current classifier cannot safely interpret, while generic landing-page prose can be misparsed as count zero. The bounded sample further showed why a simple “no count means dead” correction would be wrong—three valid bot previews expose no numeric count—and why H2 must remain inconclusive. The recommendation is to correct classification inside Phase C under an owner-ruled §5 acceptance gate, then use mandatory iteration 2 to resolve C4 evidence and DoD 22. Self-critique: the focused sample cannot prove that the random valid-form probe is absent, estimate catalog-wide death or rate limiting, or directly test headings for five unused categories; those limits are preserved rather than extrapolated away.

---

*RES — TFW-4: Verify Phase C empirical assumptions | 2026-08-26*

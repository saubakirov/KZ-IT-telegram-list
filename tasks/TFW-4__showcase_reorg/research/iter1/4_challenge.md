# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Eliminate unsafe interpretations of Telegram and GitHub responses before Phase C turns them into automated claims.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Telegram response shape | public preview with `tgme_page_extra` | D3: Liveness discriminator | route/title classification without a preview | The D3 alternative explicitly applies when preview metadata is absent. |
| D1: Telegram response shape | contact shell without preview metadata | D2: Member-count evidence | leading digits inside `tgme_page_extra` | The response-shape alternative excludes `tgme_page_extra`. |
| D1: Telegram response shape | global Telegram landing page | D3: Liveness discriminator | positive public-preview marker | A site-level landing page contains no target-specific public preview. |
| D1: Telegram response shape | explicit error/deleted page | D3: Liveness discriminator | positive public-preview marker | A target cannot simultaneously be represented by an explicit negative marker and a positive public preview in one response classification. |

**Surviving configurations** (from Extract's Configuration Space, after removing rows containing incompatible pairs):

| Config | D1: Telegram response shape | D2: Member-count evidence | D3: Liveness discriminator | Notes |
|--------|-----------------------------|---------------------------|----------------------------|-------|
| C1 | public preview with `tgme_page_extra` | `N members` text | positive public-preview marker | observed on public groups |
| C2 | public preview with `tgme_page_extra` | `N subscribers` text | positive public-preview marker | observed on channels and one bot-labelled entry |
| C3 | public preview with `tgme_page_extra` | no count evidence | positive public-preview marker | observed on three bots |
| C4 | contact shell without preview metadata | no count evidence | route/title classification without a preview | observed for one catalog group and one random valid-form probe; ambiguous |
| C5 | global Telegram landing page | members-like text unrelated to the target | route/title classification without a preview | observed for a malformed route; broad regex false positive |
| C6 | explicit error/deleted page | no count evidence | explicit `tgme_page_error`/deleted marker | supported by current code path, not observed in this iteration |
| C7 | explicit error/deleted page | no count evidence | non-success HTTP status | supported by current HTTP error path, not observed in this iteration |

**Unexpected survivors**:

- C3: a target-specific preview without a numeric count is valid for bots, so count absence cannot invalidate liveness.
- C4: the same contact shell represents a catalogued handle and an independently unresolved random probe, so HTTP 200 and target-shaped title are not sufficient proof of liveness.
- C5: a generic landing page can satisfy the broad members regex with unrelated prose, so parser success is not proof that the response belongs to the requested target.

## Findings

### C1: Every currently emitted GitHub category anchor resolves

The live GitHub repository page `https://github.com/saubakirov/KZ-IT-telegram-list` returned HTTP 200 on 2026-08-26 and exposed the rendered README heading ids. The current generator emits headings only for categories used by a group: 13 of the 18 definitions.

| Category definition | Generator href | Live rendered heading id | Verdict |
|---------------------|----------------|--------------------------|---------|
| Programming Languages | `#programming-languages` | `user-content-programming-languages` | match |
| Web Development | `#web-development` | `user-content-web-development` | match |
| Mobile Development | `#mobile-development` | `user-content-mobile-development` | match |
| Data & Analytics | `#data--analytics` | `user-content-data--analytics` | match |
| DevOps & SysAdmin | `#devops--sysadmin` | `user-content-devops--sysadmin` | match |
| Security | `#security` | `user-content-security` | match |
| QA & Testing | `#qa--testing` | `user-content-qa--testing` | match |
| Game Development | `#game-development` | `user-content-game-development` | match |
| Hardware & Electronics | `#hardware--electronics` | `user-content-hardware--electronics` | match |
| Engineering Management | `#engineering-management` | `user-content-engineering-management` | match |
| General | `#general` | `user-content-general` | match |
| Jobs & Careers | `#jobs--careers` | `user-content-jobs--careers` | match |
| Marketplace | `#marketplace` | `user-content-marketplace` | match |
| Blockchain | `#blockchain` if used | not emitted | N/A—unused |
| Education & Learning | `#education--learning` if used | not emitted | N/A—unused |
| News | `#news` if used | not emitted | N/A—unused |
| Events | `#events` if used | not emitted | N/A—unused |
| Startups | `#startups` if used | not emitted | N/A—unused |

H4 is confirmed for every link the current generator actually emits, including all four emitted names containing `&`. The phrase "all 18 category names" in the research control is not directly testable against the live README because five categories have no group, heading, or TOC link. The frozen DoD 17 already uses the correct observable scope: every category anchor in the generated TOC.

**Challenge decision C-D1:** mark H4 `confirmed-for-emitted-anchors` and refine HL §10 to distinguish 13 emitted categories from 18 defined categories. No frozen-contract change is needed.

### C2: The H1 failure belongs inside Phase C, but needs a structural acceptance gate

The failing clause is not merely count parsing. It is target-response classification in `validate_links.py`, the same Phase C deliverable that must:

- refresh verification dates only after a successful liveness check;
- identify non-responders for `--archive`;
- supply Phase D's dead-list triage input; and
- preserve the network as the only authority on liveness.

Creating TFW-5 and deferring Phase D would split one classifier across tasks and leave Phase C's archive and verification-date behavior knowingly unsafe. The frozen Phase C outcome already owns this behavior, and HL §9 already says a refuted H1 parser assumption is fixed in Phase C before Phase D. Implementation therefore belongs inside Phase C, not a separate task.

However, the current DoD can pass without rejecting a contact shell or generic landing page. A structural gate should require that:

1. a target-specific positive preview may be alive even without a count (C3);
2. a contact shell with no positive preview is reported as ambiguous, not verified alive or dead (C4); and
3. generic landing-page prose is never accepted as the target's member count (C5).

Adding that outcome to frozen §5 is an `EXTEND` amendment proposal. Evidence is Gather G3-G4 and Extract E1-E2; cost is a bounded classifier test/fixture plus implementation inside already-scoped Phase C; the considered alternative—documenting the caveat only in §9—was rejected because DoD 22 could still pass on freshly dating an unverified contact shell.

**Challenge decision C-D2:** recommend a §5 amendment proposal; do not create a new task and do not defer Phase C wholesale. Phase D remains gated on the corrected classifier.

### C3: H2 cannot justify archive behavior yet

Neither the bounded sample nor the current classifier proves that any catalog handle is dead/private. C4 shows why: absence of a public preview is insufficient to choose between private/contact-only and absent. The safe output is an explicit ambiguous state for owner triage or follow-up evidence, not an automatic archive candidate.

Iteration 2 should investigate whether a bounded, read-only target-identity signal can distinguish C4 states without a full sweep or data mutation. If no such signal exists, Phase D's owner triage must treat C4 as unresolved and require independent confirmation.

**Challenge decision C-D3:** keep H2 `inconclusive`; no archive recommendation follows from iteration 1.

### C4: Research control metadata trails the current contract baseline

`research/iterations.yaml` names `f871951` and describes A2 as proposed. Git history contains the later freeze `70ddfa6 [claude-code/TFW-4/freeze/coordinator] re-freeze after A2 approved`, and the current HL records A2 approved. The H1/H2/H4 scope is unaffected, but iteration 2 should not inherit stale baseline metadata.

This is Coordinator-owned control state. The Researcher records the defect and leaves both the control file and HL untouched.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| All 13 emitted category hrefs exactly match live GitHub heading ids; five defined categories are unused and not emitted. | Future unused-category headings are outside the current live README and require no current DoD claim. |
| H1's liveness clause is refuted; the correction belongs inside Phase C and warrants a §5 acceptance-gate proposal. | The exact C4 identity signal is an iteration 2 research question. |
| H2 remains inconclusive and cannot support archive triage. | The full 63-entry liveness result remains Phase D work after classifier correction. |
| Control-file baseline/A2 metadata is stale relative to current history and HL. | Coordinator must reconcile it before defining iteration 2. |

**Sufficiency:**
- [x] External source used? The live GitHub-rendered repository README supplied all currently emitted heading ids.
- [x] Briefing gap closed? H4 was checked exhaustively for emitted anchors, and the H1 scope consequence was classified.
- [x] Pairwise incompatibility checked? Seven surviving configurations and four incompatible alternative pairs are recorded.

Stage complete: YES
→ User decision: Close Challenge; synthesize iteration 1 RES and return to `/tfw-plan`.

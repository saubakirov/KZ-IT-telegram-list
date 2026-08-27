# RES — TFW-4: Resolve C4 identity evidence and DoD 22

> **Date**: 2026-08-26
> **Author**: Researcher (Codex)
> **Status**: 🔬 RES — Iteration 2 complete
> **Parent HL**: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> **Mode**: Pipeline (focused)

---

## Research Context

Iteration 2 resolved the evidence-design gap left by iteration 1 without repeating its public-count, eight-handle, rate-limit, or GitHub-anchor probes and without running the 63-entry Phase D sweep. It compared the ambiguous `mobile_developers_kz` C4 response with a fresh valid-form probe and a public group control, grounded identifier semantics in official Telegram documentation, separated current handle binding from historical community existence, formalized distinct `last_verified` and archive-triage rules, and tested frozen DoD 22. The investigation remained read-only; it changed only this iteration's stage files and RES and did not alter the HL, control file, data, code, release state, tags, or remotes.

## Briefing

The predecessor decisions, fixed scope, three guiding questions, and explicit rule that pending A5 is not approved are recorded in [1_briefing.md](1_briefing.md).

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Separate **current handle-to-peer binding**, **historical community existence**, and **community death**. | Official Telegram semantics distinguish public usernames from private invites; a public username can be removed, reassigned, or held while the old community remains alive under another link. |
| D2 | Define `last_verified = D` as a dated network observation that positively binds the stored identifier to the intended Telegram peer of the declared type. | HTTP 200, an echoed contact title, historical presence, and owner recollection do not establish current target identity. Count availability is independent. |
| D3 | Admit ambiguous/failed links to investigation triage after retry, but authorize archive only with independent evidence that identifies the same historical community as deleted/closed. | Wrong-peer or unoccupied-username evidence proves a broken link, not community death; a valid replacement invite proves life and routes to repair. |
| D4 | Treat `mobile_developers_kz` DoD 22 as **conditionally achievable, not currently discharged**. | C4 alone cannot support a new date. Authenticated peer resolution plus continuity match can verify it; a replacement can be repaired and rechecked; proven death can archive it; otherwise DoD 22 remains open. |
| D5 | Require an explicit owner verdict on A5 before any TS encodes C4-as-ambiguous behavior. | A5 is `PROPOSED — awaiting owner verdict`. Research evidence cannot thaw or change frozen §5. Literal DoD 12 otherwise pressures the implementation to date any HTTP responder. |
| D6 | Make no new §5 amendment proposal in iteration 2. | Telegram documents a sufficient independent signal—`contacts.resolveUsername` or equivalent authenticated client resolution—so the control file's “if no independent signal is sufficient” trigger is not met. A duplicate would obscure pending A5. |
| D7 | Stop further unauthenticated C4 probing and return `SUFFICIENT`. | Alternate `/s/` pages preserve the ambiguity, while official documentation identifies the authenticated boundary. More public URL variants would repeat the same absence of peer identity rather than reduce uncertainty. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | What peer currently owns/resolves `mobile_developers_kz`, and is it continuous with the catalogued 2017 community? | Open — owner-authenticated CL observation | Public evidence cannot answer. Use `contacts.resolveUsername` or an equivalent owner in-client search/open; capture peer kind, ID, title/about, and continuity evidence. |
| Q2 | Does the owner approve, reject, or amend A5? | Open — owner verdict required | A5 remains pending. No stage or RES treats it as applied. |
| Q3 | If the old community is alive only under a private invite, should this catalog support invite links or require a public replacement? | Conditional Coordinator/owner choice | The evidence rule says repair rather than archive. The data-model choice arises only if Q1 finds a living private replacement and is outside Researcher authority. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Public Telegram pages expose compatible counts, while genuinely absent/private targets need a safe classifier beyond the current negative-marker test. | partial — public counts confirmed; C4 identity unresolved | 🟠 PARTIAL, OPERATIONAL GAP RESOLVED — original marker assumption remains refuted, but the sufficient identity path is now defined | Gather G1-G3: private invites and public usernames are distinct; C4 repeats on `/s/`; official `contacts.resolveUsername` returns current peer or `USERNAME_NOT_OCCUPIED`. Extract E1 and Challenge C1 define the evidence boundary. |
| H2 | At least one current catalog handle is dead or private, so Phase D exercises archive with real data. | inconclusive | 🟡 INCONCLUSIVE BY DESIGN — `mobile_developers_kz` is ambiguous, not proven dead/private; no catalog-wide claim was attempted | Gather G3-G4 and Extract E3: the public link is C4 and historical existence is proven, but current peer/community status requires authenticated owner evidence. The 63-entry result remains Phase D work. |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** The current HL, its pending A5 row, and Coordinator-owned `iterations.yaml` were not edited.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Record that `mobile_developers_kz` dates to a 2017 catalog row but currently exposes C4 on both plain and `/s/` surfaces; this proves provenance, not current target identity. Distinguish a stale public username, living private replacement, wrong peer, unoccupied username, and dead community. | Gather G1, G3-G4 |
| R2 | §8 Dependencies | Add an owner-authenticated Telegram peer-resolution/continuity check for `mobile_developers_kz` before its `last_verified` date can change or Phase D can claim DoD 22. Keep A5 owner verdict as a distinct dependency. | Extract E3; Challenge C3 |
| R3 | §9 Risks | Replace binary `alive/dead-private` reasoning with three dispositions: verify current target, repair a living community's stale link, or archive only proven death; unresolved evidence blocks release rather than becoming a guessed state. | Extract E2; Challenge C2 |
| R4 | §10 H1 | Retain the public-count confirmation and marker refutation, then add that authenticated `contacts.resolveUsername`/equivalent client evidence is the sufficient C4 discriminator; target kind plus continuity must match. | Gather G2; Extract E1; Challenge C1 |
| R5 | §10 H2 | Keep `inconclusive`; state explicitly that the 2017 provenance plus current C4 does not prove death or privacy and that full-catalog existence remains Phase D evidence. | Gather G4; Extract E3 |
| R6 | §10 Proposed RESEARCH Focus | Mark iteration 2 complete and research sufficient. Route the A5 verdict and one authenticated `mobile_developers_kz` observation to `/tfw-plan`; do not schedule iteration 3 for more unauthenticated URL variants. | Challenge C3-C4 |

### Amendment Proposals — frozen sections, owner verdict required

**No new amendment proposals.** Pending A5 remains exactly `PROPOSED — awaiting owner verdict`; iteration 2 neither applies it nor treats it as approved. A separate §5 proposal becomes warranted only if authenticated resolution cannot be obtained or yields a broken binding with neither replacement nor death evidence and the owner nevertheless wants TFW-4 to proceed past unresolved DoD 22.

## Fact Candidates

No fact candidates. The user supplied workflow scope and authority boundaries, not enduring human-only project knowledge; the Telegram and repository findings are independently discoverable technical evidence.

## Strategic Insights (Research)

No strategic insights. No new human domain correction or strategic briefing occurred during this delegated iteration.

## Findings Map

```text
current catalog handle
        │
        ├─ target-specific public preview ──────────────► VERIFY TARGET
        │                                                  write last_verified
        │                                                  count optional
        │
        └─ C4 / failure after retry
                 │
                 └─ authenticated resolve + continuity
                         │
                         ├─ intended peer ───────────────► VERIFY TARGET
                         │                                 write last_verified
                         │
                         ├─ living replacement link ─────► REPAIR LINK
                         │                                 recheck, then date
                         │                                 never archive as dead
                         │
                         ├─ broken binding + death proof ► ARCHIVE COMMUNITY
                         │                                 died_on + observed reason
                         │
                         └─ no resolution/death proof ───► UNRESOLVED
                                                           no date, no archive
                                                           DoD 22 remains open

frozen contract gates
        ├─ A5 verdict ───────────────────────────────────► owner only
        └─ mobile_developers_kz peer observation ───────► owner-authenticated CL
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (public count clause retained; original negative-marker clause refuted; C4 evidence path resolved), H2 (`mobile_developers_kz` remains inconclusive rather than misclassified)
- **Hypotheses deferred:** H2 catalog-wide existential result — deliberately deferred to the Phase D 63-entry sweep, not another research iteration
- **Gaps discovered:** Public handle failure and historical community death are distinct; living-private replacement requires a repair branch; frozen DoD 12 can conflict with evidence-safe C4 handling until A5 receives an owner verdict
- **Superseded decisions:** None; iteration 2 refines predecessor D2-D3 and completes predecessor D6's assigned gap

### Open Threads (for next iteration)

No further research threads. Two non-research gates remain for the Coordinator: obtain the explicit A5 owner verdict and capture one authenticated `mobile_developers_kz` peer/continuity observation (or encode it as a blocking evidence gate before Phase D).

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan tfw-4` to classify these recommendations, obtain the owner gates, and decide the next step
- [ ] **MORE NEEDED** — no further unauthenticated research would reduce the remaining uncertainty
- [ ] **BLOCKED** — research is complete; the remaining dependencies belong to owner/Coordinator planning

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 established that “private C4 handle” is not one Telegram state: public usernames, private invites, current peer binding, historical existence, and community death must be evaluated separately. It produced deterministic evidence rules for dates and archive triage, found the non-obvious repair path for a living community behind a stale handle, and showed that `mobile_developers_kz` can satisfy DoD 22 only after authenticated peer/continuity evidence, link repair, or proven death—not from its current C4 page. The research recommendation is `SUFFICIENT`, with A5 still pending and no new amendment proposal. Self-critique: the session could not perform authenticated resolution without user credentials and the PowerShell transport produced eight unusable attempts before three bounded `curl` observations succeeded; those limits are recorded, and no full-catalog inference is made.

---

*RES — TFW-4: Resolve C4 identity evidence and DoD 22 | 2026-08-26*

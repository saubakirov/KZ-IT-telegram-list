# Judge — TFW-4 / Phase B: Contract & Docs
> **Mindset:** Judge. Rule on quality from the Verify evidence.
> **Verify findings:** [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify V4/D1 finds AC-3 only partial: `CONTRIBUTING.md` points to the canonical change procedure and immediately republishes a divergent command. AC-5 therefore does not deliver a wholly canonical, ready-for-Phase-C document set. The other four ACs are materially established, subject to the V9 manifest-evidence limitation. |
| 2 | **(a) Purpose Check** + **(b) Design soundness** | ❌ | **(a) Aligned:** Master baseline §1 calls for “one canonical rules document instead of two that disagree,” while the implemented North Star says value is “accuracy” established by a dated network check; canonicalizing the contract and storing those clauses prevents materially stale or invented catalog claims, and the result adds no Phase C/D excess or confessed deferral. **(b) Fails:** Verify D1 shows the contributor flow recreates the exact P3 drift mechanism the phase is meant to remove, so the design is not yet sound even though the work is fit for the approved purpose. |
| 3 | Tech debt documented | ✅ | RF §6 contains two specific, source-located observations. Verify C5 confirms both; neither is filler. |
| 4 | Style & standards | ❌ | Naming, English artifact language, commit attribution, links, and count-free docs conform, but Master HL P3 (“One copy of every rule”) is violated by the duplicated/divergent contributor command. |
| 5 | Observations collected | ✅ | Both observations survive the quality filter: the active Codex board-locus conflict can misroute future sessions, and the dormant Claude template route can break a future reinstall. They are routed to adapter/framework debt, not executor revision. |
| 6 | RF completeness (§7–9) | ✅ | RF §§7–9 are present. “No fact candidates” and “No strategic insights” are credible because the review delegation adds no new human domain knowledge; the diagram accurately shows the Phase B/Phase C boundary. |
| 7 | Evidence completeness — does it exist? | ✅ | Mandatory EV exists and covers AC-1 through AC-5 with the TS-authorized five N/A external-evidence statuses plus deterministic inline gate logs. No evidence reference is missing. |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | Managed bytes, JSON semantics, README currency, links, decisions, commit sets/dates, and tags independently reproduce. EV E3 nevertheless marks AC-3 green despite the contributor divergence, and E5's 115-file aggregate cannot independently prove untracked-byte preservation without its manifest definition/content (Verify V9/D4). |
| 9 | Backward compatibility | ✅ | All 33 implementation links and 24 routing/adapter targets resolve; live `CLAUDE.md` research routing is correct; pre-existing JSON semantics, README bytes, D1–D7, Phase A rows, legacy traces, and current dirty state are preserved. The two adapter debts predate and were not introduced by the implementation. |
| 10 | Safety | ✅ | Seven implementation files remain byte-equal to `836c099`; tags = 0; no catalog facts, scripts, CI, README output, credentials, or release state changed. Review used no network. Historical no-push/no-network claims are not replayable, but no resulting local release or remote-tracking state exists. |

## Purpose Check — row 2 clause (a)

**Outcome: Aligned.** Baseline §1's “one canonical rules document instead of two that disagree”
and the implemented North Star's accuracy-through-dated-network-check clause directly justify
Phase B; the material harm is that divergent instructions can publish stale or inferred catalog
facts and make the repository fail as a traceable TFW reference implementation. There is no
Phase C/D excess, no deferral confession, and no conflict between the baseline and North Star.

The failed row 2 status is clause (b), design soundness, not a `not fit for purpose` finding and
not a frozen-contract defect. The contributor divergence is local implementation work already
authorized by the Phase B TS and routes back to the executor.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF / implementation claim | Contradiction? |
|---|----------------|---------------------------|----------------|
| 1 | D9 — `AGENTS.md` is the canonical project contract | `CONTRIBUTING.md` says it follows AGENTS but republishes a different validation command | **Yes — in-scope revision finding (Verify D1)** |
| 2 | D7 — Task Board lives in `tasks/README.md` | Preserved managed Codex text says `README.md` | **Yes — inherited adapter/config debt (Verify D2); RF discloses it** |
| 3 | D8–D12 | RF claims each decision was indexed and prior knowledge preserved | No — counts, semantics, hashes, and source links hold |
| 4 | D9 — AGENTS canonical, CLAUDE thin | RF claims `CLAUDE.md` is adapter-only | No — live document structure and routes hold |
| 5 | D11 — data-borne North Star rendered later | RF claims exact storage only; Phase C rendering deferred | No — exact `north_star` exists, README remains byte-identical |

## Finding Classification

1. **Executor revision target:** remove the duplicate contributor command sequence and point to
   the canonical `AGENTS.md` procedure (or otherwise make the contributor-specific difference
   explicit without claiming it is the same sequence). This needs no HL/TS amendment.
2. **Adapter/config debt:** Task Board locus conflict. D7 already authorizes
   `tasks/README.md`; no Master HL amendment is needed. The target is the Codex adapter source and
   generated skill copies through their owning sync/config workflow, not hand-editing the managed
   block during Phase B.
3. **Framework adapter debt:** nonexistent Claude research route. No TFW-4 amendment is needed;
   fix the adapter source upstream and synchronize via `/tfw-update` (or a separately approved
   framework-maintenance task).
4. **Evidence-format debt:** future protected manifests should retain the ordered path/hash list
   and serialization/exclusion rule, not only count + aggregate hash. This does not require a
   frozen TFW-4 amendment.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Every N/A carries a stated reason? — no checklist row is N/A
- [x] Row 2(a) answered against baseline `d31e60d` plus Project North Star with quoted clauses and named harm?
- [x] Rows 7 and 8 answered separately?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §§7–9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced and contradictions documented?
- [x] RF Fact Candidates reviewed? — none, credibly

Stage complete: YES

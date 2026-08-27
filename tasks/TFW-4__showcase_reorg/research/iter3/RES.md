# RES — TFW-4: Phase D G2 target-specific dispositions

> **Date**: 2026-08-27
> **Author**: Researcher (Codex)
> **Status**: 🔬 RES — Iteration 3 complete
> **Parent HL**: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> **Mode**: Pipeline (deep, Coordinator-approved)

---

## Research Context

Iteration 3 investigated the four remaining Phase D G2 evidence gaps without reopening the catalog-wide sweep or modifying execution artifacts. It combined Phase D live/retry/browser records, current target-specific Telegram surfaces, official archived posts, public directories, and repository history to distinguish current target binding, peer kind, cross-time continuity, living replacement, same-community death, and the strongest supportable mutation. The work preserved the dirty checkout and wrote only `research/iter3/**` plus the permitted iter3 status in `research/iterations.yaml`; it did not modify data, generated documentation, Phase D HL/TS/ONB/evidence/RF/REVIEW, code, archive state, commits, tags, or remotes.

## Briefing

The five dimensions, predecessor evidence, working hypotheses, scope exclusions, and Coordinator-approved threshold are recorded in [1_briefing.md](1_briefing.md). In particular, a target-bound type reclassification without a validator count required at least one independent cross-time continuity signal, and either contact shell had to remain `UNRESOLVED` unless evidence proved a same-community replacement or death.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Recommend an exact, conditional `datanomika` groups→channels structural repair. | Current Phase D evidence is target-bound and channel-typed; official 2021/current target content plus 2020 repository history independently preserve the exact handle, title/author, and BI/data purpose. No reassignment signal was found. |
| D2 | `datanomika` needs no copy edit. | `Datanomika` exactly matches the visible title; both descriptions are kind-neutral and supported. Only the section move and deterministic removal of group-only `category` are justified. |
| D3 | Recommend atomic K-coherent repair for `kzquake`: bots→channels plus exact factual target alignment. | Phase D binds the exact handle to a subscriber channel titled `Землетрясения \| Казахстан`; dated official posts and 2018 repository history preserve the specialized Kazakhstan-earthquake service. The current bot name/Russian bot wording would be false after a type-only move. |
| D4 | Reject K-min as a complete repair. | Moving the unchanged `KZ Quake Bot` row into channels would be structurally narrow but publication-incoherent. If the owner will not approve the atomic factual package, the safe disposition is `UNRESOLVED`, not degraded publication. |
| D5 | Keep `mobile_developers_kz` exact `UNRESOLVED`, no mutation; treat `mobile_dev_kz` only as an unbound alternative. | The old community has historical provenance, but its current URL is an unbound contact shell. No peer-ID, migration notice, admin cross-link, or source equates the living alternative with the historical community; no same-community death evidence exists. |
| D6 | Keep `kzqacommunity` exact `UNRESOLVED`, no mutation. | Historical identity is strong, including archived QA content and directory peer ID `1473118772`, but current target binding, a proven replacement, and independent closure/deletion evidence are all absent. A vacancy channel and directory inactivity are not continuity/death proof. |
| D7 | Make the exact post-change validator retry part of each proposed type repair. | A declared mismatch cannot provide a pipeline count. Only after the structural repair can the target-bound classifier return `verified` for `channels`; only that new output may update date/count. Research counts may not be copied. |
| D8 | Disclose service continuity as HIGH while preserving the peer-ID limitation. | Cross-time handle/name/topic signals meet the approved decision threshold, but persistent peer-ID identity/migration is undocumented for both `datanomika` and `kzquake`; Research does not upgrade service continuity into absolute peer-ID proof. |
| D9 | Return `SUFFICIENT` and route the exact packages to `/tfw-plan`. | The remaining unknowns are owner G2 authority, future post-mutation observations, and genuinely absent C4 evidence. More unauthenticated search would repeat the same absence rather than safely change a disposition. |

## Per-entry Evidence and Exact Disposition

### `datanomika`

| Required element | Result |
|------------------|--------|
| Observed facts | Phase D live/retry evidence: declared `groups`, `target_bound=true`, observed `channels`, visible `Datanomika`, old count `2800`, no observed count. Current official target exposes the exact handle/title and subscriber-channel semantics. |
| Sources/date | Phase D `phase-d/evidence/live_sweep_summary.json`, `retry_summaries.json`, and browser fallback bundle (2026-08-27); [`https://t.me/datanomika`](https://t.me/datanomika) (accessed 2026-08-27); dated official archive [`https://t.me/s/datanomika?before=252`](https://t.me/s/datanomika?before=252) (2021 content, accessed 2026-08-27); repository commit `f8f2da3a9257a72cff4acb51cb8263a11e9ecbd0` (2020-07-15). |
| Target binding | **Yes.** Phase D authoritative preview binding is true; official current/archived pages use the exact handle. |
| Correct peer kind | **Broadcast channel.** Target-specific subscriber/channel surface; no member/group action or contrary authenticated kind was found. |
| Continuity confidence | **HIGH service continuity.** Exact handle, title, author/company, and BI/data topic recur across 2020, 2021, and current evidence. Persistent peer-ID continuity is not documented. |
| Replacement/death evidence | Not applicable: current stored handle is live. No reassignment/conflicting peer or death evidence found. |
| Exact supportable mutation | Move the unchanged record from `groups` to `channels`; remove group-only `category: data-analytics`; retain `name: Datanomika`, `handle: datanomika`, `description: Data visualization, dashboards, business intelligence`, `description_ru: О визуализации данных, интерактивной отчетности, BI`, old count, and old date until recheck. |
| Mandatory post-change proof | Run `python scripts/validate_links.py --handle datanomika --update --summary-json "$env:TEMP\tfw4-g2-datanomika-recheck.json"` and retain/consolidate that raw summary in Phase D evidence. Require `classification=verified`, `declared_type=channels`, `observed_type=channels`, `target_bound=true`. Missing count is acceptable; only an actually parsed integer may replace `2800`. |
| Owner boundary | Exact per-entry Phase D G2 approval is still mandatory before mutation. Any failed/non-verified recheck returns the row to `UNRESOLVED` with no new date/count. |

### `kzquake`

| Required element | Result |
|------------------|--------|
| Observed facts | Phase D live/retry evidence: declared `bots`, `target_bound=true`, observed `channels`, visible `Землетрясения \| Казахстан`, old count `2168`, no observed count. Official target archive exposes subscriber/channel semantics, an about statement for operational Kazakhstan earthquake messages, and dated seismic bulletins. |
| Sources/date | Phase D `phase-d/evidence/live_sweep_summary.json`, `retry_summaries.json`, and browser fallback bundle (2026-08-27); official archive [`https://t.me/s/kzquake?before=1527`](https://t.me/s/kzquake?before=1527) and earlier [`https://t.me/s/kzquake?before=1163`](https://t.me/s/kzquake?before=1163) (2023/2024 content, accessed 2026-08-27); repository commit `fb345f9ebe9d24bf4756822eca059e42bd2878b3` (2018-10-22). |
| Target binding | **Yes.** Phase D authoritative preview binding is true; official archive binds the exact handle/title. |
| Correct peer kind | **Broadcast channel.** Subscriber/channel surface; no current bot-start action or separate bot target was found. |
| Continuity confidence | **HIGH service continuity.** Exact handle and the narrow operational Kazakhstan-earthquake function recur across 2018, dated 2023/2024 posts, and current Phase D evidence. A bot→channel migration notice and persistent peer-ID continuity are undocumented. |
| Replacement/death evidence | No replacement is needed for the current handle; no separate living bot, reassignment, or death evidence found. |
| Exact supportable mutation | One atomic K-coherent package: move `bots`→`channels`; set `name` to `Землетрясения \| Казахстан`; keep `handle: kzquake`; keep `description: Earthquake monitoring in Kazakhstan`; set `description_ru` to `Оперативные сообщения о землетрясениях на территории Казахстана`; preserve old count/date until recheck. |
| Contract boundary | These string changes are target-derived factual alignment, not editorial style work: exact visible title, unchanged accurate English description, and a conservative Russian statement derived from the official about text. K-min (type-only move with “Bot/Бот”) is rejected/degraded. |
| Mandatory post-change proof | Run `python scripts/validate_links.py --handle kzquake --update --summary-json "$env:TEMP\tfw4-g2-kzquake-recheck.json"` and retain/consolidate that raw summary in Phase D evidence. Require `classification=verified`, `declared_type=channels`, `observed_type=channels`, `target_bound=true`. Missing count is acceptable; research/approximate counts must not replace `2168`. |
| Owner boundary | Exact per-entry Phase D G2 approval must name the entire atomic before/after package and evidence. If the owner approves only a type move, rejects the strings, or the recheck is not verified, retain `UNRESOLVED`; do not publish K-min. |

### `mobile_developers_kz`

| Required element | Result |
|------------------|--------|
| Observed facts | Phase D and current public surface are an exact-handle Telegram contact shell with `target_bound=false`, no count, and no established current peer kind. Repository history proves a 2017 `Mobile Developers KZ` community. |
| Sources/date | Phase D evidence bundle (2026-08-27); historical directory [`https://kz.intelegram.one/chats/35`](https://kz.intelegram.one/chats/35) (accessed 2026-08-27); repository commit `fb5976c679440cbc6f780606365e67e2977e4ecb` (2017-07-04). Living alternative evidence: `mobile_dev_kz` directory/2024 roundup, but no old→new binding. |
| Target binding | **No.** Generic contact shell is not target evidence. |
| Correct peer kind | Historical entry was a group; current old-handle peer kind is **not established**. `mobile_dev_kz` appears to be a living supergroup but is not bound to the old community. |
| Continuity confidence | Historical old-community identity: **HIGH**. Old→`mobile_dev_kz` continuity: **LOW/UNPROVEN**. |
| Replacement/death evidence | `mobile_dev_kz` is only an unbound alternative. No migration, same-peer ID, admin cross-link, or independent same-community closure/deletion evidence found. |
| Exact supportable mutation | **None. UNRESOLVED.** Leave every catalog field unchanged; no link repair, date/count refresh, archive, or substitution. |
| Owner boundary | No mutation can be approved from current evidence. A future repair needs explicit continuity plus recheck; archive needs independent same-community death evidence plus exact owner approval. Current unresolved state blocks release. |

### `kzqacommunity`

| Required element | Result |
|------------------|--------|
| Observed facts | Phase D and current public surface are an exact-handle contact shell with `target_bound=false`; old catalog count is `762`. Historical sources preserve `KZ QA community`, QA purpose/content, and directory peer ID `1473118772`, but not current binding. |
| Sources/date | Phase D evidence bundle (2026-08-27); Telemetr overview/posts [`https://telemetr.io/en/channels/1473118772-kzqacommunity`](https://telemetr.io/en/channels/1473118772-kzqacommunity) and [`/posts`](https://telemetr.io/en/channels/1473118772-kzqacommunity/posts) (accessed 2026-08-27); 2024 exact-handle roundup; repository commit `fad259c9bd5ff4335d22ab5171c7eadbd1c5ab9f` (2022-11-10). |
| Target binding | **No.** Current official route is a generic contact shell. Directory history is not current Telegram target resolution. |
| Correct peer kind | Historical community was a QA group; current requested-handle kind is **not established**. |
| Continuity confidence | Historical identity: **HIGH**. Current living continuity: **UNKNOWN**; persistent historical ID is useful only if a future authenticated result supplies a comparable ID. |
| Replacement/death evidence | None. `qaz_qa_vacancies` is a vacancy channel, not a replacement for the general QA community. Telemetr “No data”/archived posts do not prove death. |
| Exact supportable mutation | **None. UNRESOLVED.** Leave every catalog field unchanged; do not copy Telemetr count, repair link, refresh date, or archive. |
| Owner boundary | No mutation is evidence-safe. A future repair/archive needs the same continuity/death gates and exact approval; current unresolved state blocks release. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Will the owner approve the exact `datanomika` structural package? | Open — G2 owner decision | Research supports it conditionally; no mutation is authorized until the exact approval and subsequent validator result exist. |
| Q2 | Will the owner approve the entire atomic K-coherent `kzquake` package? | Open — G2 owner decision | The package is evidence-backed and Phase D-compatible. Type-only K-min is not recommended; rejection leaves the entry unresolved. |
| Q3 | Can either contact shell later be bound to a current intended peer, a proven replacement, or independent death evidence? | Open external fact, not a current research gap | No such evidence was found. Preserve unresolved until a genuinely new signal exists; do not repeat generic-shell/directory probing as if it were progress. |
| Q4 | What count will either repaired channel expose to the exact validator? | Open future observation | It may remain unavailable. This does not prevent target/type verification; no research count may be copied or estimated. |

## Hypotheses (iteration 3 instantiation)

| # | Hypothesis | Prior status | RES Status | Evidence |
|---|-----------|--------------|------------|----------|
| H1 | The two target-bound declared-type mismatches are continuity-backed catalog kind errors that can be repaired and reverified without changing the stored link. | Open | 🟢 CONFIRMED WITH CONDITIONS | `datanomika` and `kzquake` each have current target binding, channel semantics, and independent cross-time exact-handle/name/topic evidence. Persistent peer-ID continuity remains undocumented; exact owner G2 and post-change retry are required. |
| H2 | At least one contact-shell entry has a safely provable living replacement or independent same-community death disposition. | Open | 🔴 NOT SUPPORTED | `mobile_dev_kz` is unbound; QA vacancy/directory material proves neither replacement nor death; closure/migration counter-search found no qualifying evidence. Both exact dispositions remain `UNRESOLVED`. |

## HL Update Recommendations

> **The researcher classifies. The researcher never applies.** This RES does not edit the Master or Phase D HL/TS. The Coordinator should route these recommendations through `/tfw-plan` and preserve every owner gate.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Record the four exact G2 outcomes: conditional type repair for `datanomika`, atomic K-coherent repair for `kzquake`, and no-mutation `UNRESOLVED` for both contact shells. Include the peer-ID limitation and the prohibition on copying research counts. | D1-D8; per-entry matrix |
| R2 | §8 Dependencies | Add two exact owner G2 decisions and their mandatory post-change exact validator retries. State that the two C4 unresolved rows independently block release until new evidence exists. | Challenge C-D1, C-D2, C-D4, C-D5 |
| R3 | §9 Risks | Add: type-only K-min can pass structural validation while publishing false bot-facing labels; cross-time service continuity does not equal persistent peer-ID proof; directory inactivity is not death; similarly scoped alternatives are not repairs. | Challenge consistency table and C2-C4 |
| R4 | §10 H1/H2 | Mark H1 confirmed-with-conditions for the two target-bound records and H2 not supported for both contact shells. Preserve exact evidence limits rather than converting absence into closure. | Hypothesis table above |
| R5 | §11 Next Step | Use `/tfw-plan tfw-4` to classify/incorporate this RES into the G2 decision package. Do not resume data mutation until exact owner approvals exist; do not proceed to release while either C4 row is unresolved. | D9; Challenge C-D5 |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** The frozen Phase D contract already permits evidence-backed exact repairs, requires post-repair recheck and owner G2, forbids editorial judgement/inferred facts, and defines unresolved/no mutation. K-coherent fits only as the exact evidence-backed factual repair described above; this RES does not widen that authority.

## Fact Candidates

No fact candidates. The user supplied task scope, evidence thresholds, and approval routing; the repository/Telegram findings are independently discoverable evidence rather than human-only project facts.

## Strategic Insights (Research)

No strategic insights. Coordinator checkpoint decisions constrained the research method and acceptance threshold but did not add human-only domain knowledge.

## Findings Map

```text
Phase D non-verified record
        │
        ├─ target_bound=true + observed channel
        │        │
        │        ├─ independent cross-time continuity
        │        │        │
        │        │        ├─ datanomika ── structural move only
        │        │        │                  no copy edits
        │        │        │
        │        │        └─ kzquake ───── atomic K-coherent repair
        │        │                           exact target title/RU fact
        │        │
        │        └─ no continuity/conflict ───────────────► UNRESOLVED
        │
        └─ target_bound=false contact shell
                 │
                 ├─ proven old→new continuity ───────────► LINK REPAIR + RECHECK
                 ├─ independent same-community death ────► ARCHIVE + OWNER APPROVAL
                 └─ neither (both current C4 entries) ───► UNRESOLVED / NO MUTATION

conditional repair branch
        exact owner G2
              ↓
        scoped before/after mutation
              ↓
        exact-handle validator as declared channel
              ├─ verified + target_bound ─► retain observed date/count if present
              └─ any other result ────────► fail closed to UNRESOLVED
```

## Iteration Status

- **Iteration:** 3 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (confirmed with owner/recheck/peer-ID limitations), H2 (not supported; both contact shells unresolved)
- **Hypotheses deferred:** None. Future C4 resolution depends on genuinely new external/authenticated evidence, not another repetition of the same research surfaces.
- **Gaps discovered:** Persistent peer-ID continuity is undocumented for both reclassification candidates; exact owner G2 is absent; future exact validator counts are unknown; both C4 entries still block Phase D release.
- **Superseded decisions:** K-coherent supersedes Extract's undecided K-min/K-coherent branch because Challenge established the frozen-contract boundary and rejected K-min as publication-incoherent. No predecessor RES decision is rewritten.

### Open Threads (for next iteration)

No further research iteration is recommended. Remaining work belongs to `/tfw-plan` and later owner-gated execution: classify the exact two repair packages, record G2 decisions, preserve both unresolved C4 outcomes, and require new evidence before reopening either.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan tfw-4` to classify these exact recommendations and prepare the owner G2 decision boundary
- [ ] **MORE NEEDED** — no current external source gap can be safely closed by repeating generic-shell, vacancy, directory, or count searches
- [ ] **BLOCKED** — research is complete; unresolved catalog state is an intentional Phase D gate, not a Researcher blocker

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 3 closed the decision-design gap for all four records. `datanomika` is a continuity-backed channel needing only a conditional structural move; `kzquake` is a continuity-backed channel whose safe repair is the exact atomic K-coherent package, not a bot-labelled type-only row. `mobile_developers_kz` and `kzqacommunity` remain deliberately unresolved because neither replacement continuity nor same-community death is proved. Every supportable repair still requires exact owner G2 and a post-change target-bound validator result; persistent peer-ID continuity remains undocumented, and no research count may enter the catalog. The recommendation is `SUFFICIENT` for `/tfw-plan`. Self-critique: cross-time service continuity is strong but not persistent-peer-ID proof, and public research cannot establish the present private/deleted state of either C4 community; the RES preserves those limits instead of manufacturing certainty.

---

*RES — TFW-4: Phase D G2 target-specific dispositions | 2026-08-27*

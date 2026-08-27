# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. The configurations are attacked below; every survivor needs evidence and every elimination needs a stated reason.
> **Test:** "Would the surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Close the Phase D G2 evidence gap for `datanomika`, `kzquake`, `mobile_developers_kz`, and `kzqacommunity` with an exact, evidence-bounded per-entry disposition.

## Consistency and Stress Test

| Candidate configuration/rule | Attack | Evidence/result | Disposition |
|------------------------------|--------|-----------------|-------------|
| X1 — `datanomika` is a broadcast channel | Telegram represents both broadcast channels and supergroups with the MTProto `channel` constructor | Phase D did not infer from that constructor: its target-bound preview contained subscriber/channel semantics, which `observed_preview_type()` maps to `channels` | Survives |
| X1 — same historical and current `datanomika` peer | A public username can be moved or reassigned | Exact handle, title, author/company, and BI/data subject recur in 2020 repository history, dated 2021 official archive, and current official target; no identity conflict was found | Survives with HIGH service-continuity confidence; persistent peer-ID proof remains unavailable |
| X2 — `datanomika` is actually a supergroup | Public preview classifier could be wrong | The target-specific surface says subscribers/channel, not members/group; no group-action or authenticated contrary result exists | Eliminated on current evidence; exact post-move retry remains the fail-closed check |
| X3 — current `datanomika` is a reassigned peer | Same handle could now name unrelated content | Current and historical author/topic/name signals align; counter-search found no different identity or migration | Eliminated unless future peer-ID or administrator evidence contradicts continuity |
| X4 — current `kzquake` is the catalogued earthquake service, now a channel | The 2018 “bot” row may have identified a separate bot whose handle was later reassigned to an unrelated channel | Exact handle and Kazakhstan-earthquake function recur in 2018 repository history, dated 2023/2024 official archive, and current Phase D target-bound preview; no distinct bot handle, peer, migration notice, or competing service was found | Survives with HIGH service-continuity confidence and explicit limitation that peer-ID migration is undocumented |
| X5 — a separate bot still exists behind the same public handle | The old name may be more reliable than current preview | One public username cannot simultaneously be the current public address of a bot and a broadcast channel; no separately addressable bot or bot-start action was found | Eliminated on available evidence |
| X6 — `kzquake` is reassigned | Same topic could have been recreated by a new operator | Possible in theory, but the unchanged exact handle, very specific operational earthquake function, dated posting history, and absence of any conflicting identity meet the Coordinator's cross-time threshold | Eliminated as the working configuration; residual uncertainty is disclosed for owner G2 |
| K-min — type-only `kzquake` move | Structural minimalism is safer | It would publish `KZ Quake Bot` and “Бот…” inside the channels section even though the retained target evidence identifies `Землетрясения \| Казахстан` and explicitly calls itself a channel | Rejected/degraded: structurally narrow but publication-incoherent |
| K-coherent — type move plus factual target alignment | Frozen Phase D forbids editorial rename/redescription | The TS forbids rename/redescription **on editorial judgement** (`TS` §2, line 63) and permits evidence-backed, exact owner-approved repairs (`TS` §§1, 4/AC-4/AC-5). Here the name is copied from the target and the Russian text is a conservative target-about fact; the English text is already accurate | Survives only as one exact evidence-backed G2 package approved in full by the owner |
| `datanomika` copy rewrite | A move from groups to channels may require public text changes | Existing name exactly matches the target; both descriptions are kind-neutral and remain supported by current/historical content | Eliminated: no copy edit is required or justified |
| Type repair automatically licenses a new count | Current external pages expose approximate or alternate counts | Phase D mismatch records expose no `observed_count`; Research observations are not pipeline update evidence | Eliminated: exact post-change validator result controls date/count; no count may be copied |
| X8 — `mobile_dev_kz` repairs `mobile_developers_kz` | Both are Kazakhstan mobile-development groups | The 2024 roundup and other directory material list a living `mobile_dev_kz`, but no migration, peer-ID, admin cross-link, or equivalence statement links it to the old community | Eliminated; the candidate remains an unbound alternative |
| X10 — archive `mobile_developers_kz` | Old link is a contact shell and the historical group is small/old | Generic shell, age, and lack of current count prove neither closure nor deletion; closure-focused searches on 2026-08-27 found no same-community death evidence | Eliminated |
| X12 — repair `kzqacommunity` to the vacancy channel or another QA target | Topic overlap is enough | `qaz_qa_vacancies` has a narrower vacancy purpose; no replacement or migration evidence exists | Eliminated |
| X13 — archive `kzqacommunity` | Telemetr has no recent statistics | Directory inactivity/“No data” is not a Telegram closure/deletion observation; exact historical identity remains visible but present state is unknown | Eliminated |
| X9/X14 — retain both contact shells unresolved | This blocks the release and may preserve dead rows | The alternative is worse: repair or archive would infer continuity/death. Frozen AC-4 explicitly requires unresolved/no mutation when binding, replacement, and death evidence are absent | Survives; intentionally conservative |

### Pairwise incompatibilities

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------------|------------------|
| D1 binding | target-bound exact handle | D1 binding | generic/unbound shell | These describe mutually exclusive current responses for one observation |
| D2 kind | broadcast channel | D5 mutation | retain a bot/group declaration as verified | The current validator cannot return `verified` when declared and observed types differ |
| D3 continuity | no old→new signal | D5 mutation | link repair to replacement | A similarly scoped alternative cannot become the same community by owner preference alone |
| D4 state | unknown | D5 mutation | archive | Archive requires independent same-community closure/deletion evidence, not absence of positive life evidence |
| D4 state | live at stored handle | D5 mutation | link repair | The stored handle does not need replacement; only its catalog peer kind/factual labels require correction |
| D3 continuity | target-backed factual name/about | D5 mutation | editorial rewrite beyond observed facts | Phase D permits repair facts, not new copy chosen for style or promotion |

## Surviving Configurations

| Config | Binding | Peer kind | Continuity | Present state | Exact disposition |
|--------|---------|-----------|------------|---------------|-------------------|
| S1 / Extract X1 — `datanomika` | Target-bound | Broadcast channel | HIGH: exact handle/name/author/topic across 2020, 2021, current | Live at stored handle | Conditional groups→channels repair; no copy edits; exact retry; owner G2 |
| S2 / Extract X4 — `kzquake` | Target-bound | Broadcast channel | HIGH service continuity: exact handle/specialized function across 2018, 2023/2024, current; no peer-ID proof | Live at stored handle | K-coherent bots→channels factual repair; exact retry; owner G2 |
| S3 / Extract X9 — `mobile_developers_kz` | Unbound contact shell | Current old peer kind not established | Historical old community only; no old→new link | Unknown | UNRESOLVED, no mutation; `mobile_dev_kz` is not a repair candidate |
| S4 / Extract X14 — `kzqacommunity` | Unbound contact shell | Current kind not established | Strong historical identity including peer ID `1473118772`; no current binding | Unknown | UNRESOLVED, no mutation |

**Unexpected survivor:** K-coherent survives the editorial-scope attack because every proposed changed value is target-derived and the frozen contract excludes editorial judgement rather than evidence-backed factual repair. It still fails closed without an owner G2 decision naming the entire exact package.

## Findings

### C1: `datanomika` needs only a structural type repair

The adversarial continuity attack does not displace S1. The dated official archive and current official target retain the same exact handle/title, identifiable author/company, and BI/data purpose. Recent official archive material further describes the target as a channel about corporate data, Self Service BI, and related AI/data subjects, consistent with the existing catalog copy. No counter-source identifies a different community.

Exact proposed catalog facts:

| Field | Proposed value/action | Evidence boundary |
|-------|-----------------------|-------------------|
| container | move `groups` → `channels` | Target-bound Phase D `observed_type=channels` plus cross-time continuity |
| `name` | `Datanomika` — unchanged | Exact current/historical visible title |
| `description` | `Data visualization, dashboards, business intelligence` — unchanged | Still a supported, kind-neutral subset of the target subject |
| `description_ru` | `О визуализации данных, интерактивной отчетности, BI` — unchanged | Still supported and kind-neutral |
| `category` | remove `data-analytics` | Structural consequence: channel entries do not carry group category membership |
| `handle` | `datanomika` — unchanged | Current target is bound; this is not link repair |
| count/date | preserve during move; then accept only the exact post-move validator observation | Research/browser counts are not mutation evidence |

No rename, redescription, link repair, archive, or editorial expansion is required. An exact retry after the move must return `verified`, `declared_type=channels`, `observed_type=channels`, `target_bound=true`; a missing observed count is acceptable and must not be estimated. Any other result returns the entry to UNRESOLVED without a new date/count.

**Challenge decision C-D1:** recommend the structural package above for exact owner G2 approval; no copy changes beyond deterministic section/schema movement.

### C2: K-coherent is the only publication-coherent `kzquake` repair within the evidence

The current official Telegram archive for `@kzquake`, accessed again during Challenge on 2026-08-27, exposes:

- title `Землетрясения | Казахстан`;
- subscriber/channel semantics;
- target about text stating that it publishes operational messages about earthquakes in Kazakhstan and is an informational channel;
- dated operational bulletins with Kazakhstan-region seismic data.

Those are observed target facts, not editorial preferences. The exact recommended before/after package is:

| Field | Current | Exact proposed value/action |
|-------|---------|-----------------------------|
| container | `bots` | move to `channels` |
| `name` | `KZ Quake Bot` | `Землетрясения \| Казахстан` |
| `handle` | `kzquake` | unchanged |
| `description` | `Earthquake monitoring in Kazakhstan` | unchanged |
| `description_ru` | `Бот следит за землетрясениями в КЗ` | `Оперативные сообщения о землетрясениях на территории Казахстана` |
| count/date | `2168` / old verification date | preserve during move; exact retry may update date and only an actually parsed integer count |

The Russian proposal is a concise factual normalization of the official about statement; it makes no prediction, official-affiliation claim, activity claim beyond publication of operational messages, or marketing assertion. The English description is already accurate and peer-kind-neutral, so changing it would add no evidence value.

Frozen-contract test:

1. TS §2 excludes renaming/redescribing **on editorial judgement**, not evidence-backed correction of false peer-kind/name facts.
2. TS AC-4 permits exact owner-approved repairs and requires recheck before date/count.
3. TS AC-5 permits owner-approved repair facts and forbids hiding an editorial catalog change in the sweep.
4. Therefore K-coherent is in scope only if the owner G2 record names the container move and the exact three string outcomes above, cites Phase D plus iter3 evidence, and the post-change target recheck succeeds.

K-min is not recommended: it would satisfy the classifier's container expectation while knowingly retaining a false bot name and Russian bot description. If the owner approves only a type move and rejects factual target alignment, the safe result is to keep the entry UNRESOLVED for a later scoped repair—not to publish K-min as complete.

**Challenge decision C-D2:** recommend K-coherent as one atomic G2 repair. Exact validator acceptance is `verified`, `declared_type=channels`, `observed_type=channels`, `target_bound=true`; otherwise fail closed.

### C3: Cross-time continuity is sufficient for G2 consideration, not a claim of peer-ID identity

Telegram usernames are mutable, so handle equality alone would fail Challenge. These two records exceed that weak case:

- `datanomika`: exact handle + exact title + identifiable author/company + narrow BI/data subject across multiple years;
- `kzquake`: exact handle + exact specialized Kazakhstan-earthquake service + matching archive title/content across multiple years.

No persistent peer-ID pair is available for either chain, and `kzquake` lacks a documented bot→channel migration notice. The recommendation is consequently not “identity mathematically proved”; it is “service continuity HIGH and sufficient for an exact owner G2 repair under the Coordinator's approved threshold, with the limitation visible.” A contradictory authenticated peer ID, administrator statement, or distinct historical bot artifact would reopen the disposition.

**Challenge decision C-D3:** do not overstate continuity; retain the peer-ID limitation in RES and in the G2 evidence row.

### C4: Both contact-shell entries withstand pressure only as unresolved

Challenge repeated closure/migration-oriented external searches on 2026-08-27. Results surfaced historical listings, the living but separate `mobile_dev_kz`, and Telemetr's QA archive; they did not surface a migration/equivalence statement or independent closure/deletion report for either old community.

- `mobile_developers_kz`: old historical identity is credible; current binding and state are unknown. `mobile_dev_kz` remains a useful curation lead for a future independent vetting task, not a Phase D repair candidate.
- `kzqacommunity`: peer ID `1473118772` and archived content strengthen historical identity only. Telemetr “No data” and an old member figure do not prove death. The vacancy channel is not a same-purpose replacement.

Exact disposition for both: **UNRESOLVED; leave every catalog field unchanged; do not refresh date/count; do not move to archive; stop Phase D before release preparation.** New evidence can change this only if it binds the current old target, proves old→new continuity, or independently proves same-community death. Owner approval alone cannot substitute for any of those facts.

**Challenge decision C-D4:** S3 and S4 survive unchanged; no implementation mutation is supportable.

### C5: Required execution sequence is a fail-closed branch, not an optimistic reclassification

For each owner-approved type repair, the future Executor must:

1. capture the exact approved before/after record and evidence reference;
2. apply only that record's structural/factual package;
3. run `python scripts/validate_links.py --handle <handle> --update --summary-json <new-evidence-path>`;
4. require a target-bound `verified` channel record; retain a new date/count only from that output;
5. if verification fails, restore only the scoped candidate mutation from the ONB byte snapshot and record UNRESOLVED—never reconstruct from `HEAD` in the dirty checkout;
6. after both approved packages, run schema validation, generator write, and generator `--check` as required by Phase D.

This research does not authorize or perform those steps. Exact owner G2 approval is still absent for both reclassifications. The contact-shell entries remain unresolved and therefore independently block AC-5/AC-6 even if both type repairs later pass.

**Challenge decision C-D5:** the G2 recommendation is exact but not self-authorizing; route contract/evidence incorporation through `/tfw-plan` before any resumed `/tfw-handoff` mutation.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| `datanomika`: structural groups→channels repair only; no name/description edits | Exact owner G2 and post-move target-bound validator result |
| `kzquake`: exact atomic K-coherent repair with target title, unchanged English description, exact Russian factual text | Exact owner G2 and post-move target-bound validator result; peer-ID migration remains undocumented |
| K-min is rejected/degraded because it knowingly publishes bot labels in a channel row | If owner will not approve K-coherent, retain UNRESOLVED and plan a later scoped repair |
| Both contact-shell rows remain exact UNRESOLVED/no mutation | New authenticated continuity/replacement/death evidence is absent; they block release |

**Sufficiency:**
- [x] External source used? Official current/archived Telegram target pages were rechecked, and closure/migration-focused external searches were repeated in this stage.
- [x] Briefing gap closed? Yes; every entry now has observed facts, binding/kind/continuity limits, exact supported mutation or no-mutation result, and remaining owner authority.
- [x] Pairwise incompatibility checked? Yes; six incompatible dimension pairs and four surviving configurations are explicit.
- [x] Counter-evidence tested? Yes; constructor ambiguity, username reassignment, separate-bot possibility, editorial-scope conflict, alternative-as-replacement, inactivity-as-death, and count copying were attacked.
- [x] Metacognitive check passed? Yes; the non-obvious survivor is the evidence-backed atomic K-coherent repair, while the seemingly conservative K-min is rejected as incoherent.

Stage complete: YES
→ Coordinator decision: close Challenge and synthesize iter3 RES with `SUFFICIENT` research for two conditional type repairs and exact `UNRESOLVED` dispositions for both contact shells; no subsequent mutation is authorized.

# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Map every evidence-bearing state that could change the exact G2 disposition of the four unresolved records.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Current requested-handle binding | Target-specific current peer | Generic shell / no peer binding | Wrong or reassigned peer | Current binding unavailable to public evidence |
| D2: Observed peer kind | Group | Channel | Bot | Not established |
| D3: Cross-time continuity | Independent dated same-handle/name/topic signal | Documented migration or replacement | Conflicting predecessor identity | No independent continuity signal |
| D4: Present community state | Live at stored handle | Live at replacement link | Independently proven closed/deleted | Not established |
| D5: Mutation class | Type-only reclassification | Link repair plus recheck | Archive with death evidence | Unresolved / no mutation |

## Findings

### G1 — Evidence baseline from Phase D

The full sweep and one exact-handle retry agree on all four records on 2026-08-27:

| Handle | Declared / observed | Target bound | Visible name | Count result | Evidence |
|--------|---------------------|--------------|--------------|--------------|----------|
| `datanomika` | groups / channels | true | `Datanomika` | old 2800; no accepted observed count because type mismatched | `phase-d/evidence/live_sweep_summary.json`; `retry_summaries.json` retry SHA-256 `5473e9c...` |
| `kzquake` | bots / channels | true | `Землетрясения \| Казахстан` | old 2168; no accepted observed count because type mismatched | Same artifacts; retry SHA-256 `0c774ba...` |
| `mobile_developers_kz` | groups / not established | false | none | no count | Same artifacts; retry SHA-256 `ad36687...`; `browser_fallback.pdf` p.2 |
| `kzqacommunity` | groups / not established | false | none | old 762; no observed count | Same artifacts; retry SHA-256 `ba7b4b5...`; `browser_fallback.pdf` p.3 |

The browser bundle records a generic contact shell for each C4 handle and explicitly classifies it as non-evidence; p.4 records one sequential temporary tab, successful close, and zero remaining temporary tabs. This is contemporaneous negative evidence against current public binding, not death evidence.

### G2 — `datanomika`: current channel plus cross-time continuity

Observed facts:

- The official target page `https://telegram.me/datanomika`, accessed 2026-08-27, binds `@datanomika` to visible name `Datanomika`, labels it a channel preview, shows 2,799 subscribers, and describes Alexander Polorotov / Datanomix.pro / AI and data events.
- The official public archive `https://t.me/s/datanomika?before=252`, accessed 2026-08-27, binds the same handle and title to subscriber-labelled channel posts whose content explicitly references February–March 2021. The posts are authored as Alexander Polorotov and cover Qlik, BI, data visualization, and Datanomix.
- Repository commit `f8f2da3a9257a72cff4acb51cb8263a11e9ecbd0` introduced the exact handle on 2020-07-15 under the then-group list with `1000+` and a description of open-data visualization, KPI dashboards, and business intelligence. Commit `d17b353...` carried it into structured JSON as `groups/data-analytics` on 2026-01-30.

Target binding is direct and current; peer kind is channel. Cross-time continuity is **high**: exact handle, exact current title, stable author/organization, stable BI/data topic, official 2021 channel archive, and the same magnitude of audience all align. The evidence more strongly supports a long-standing catalog type error than a newly reassigned username. The observed external count is a continuity signal only; Phase D should rerun the validator after any approved reclassification before writing date/count.

Counter-evidence sought: searches for reassignment, a different Datanomika Telegram peer, or a group-to-channel migration found no conflicting target. Absence of a conflicting search result is not proof by itself, so continuity rests on the positive cross-time bindings above.

### G3 — `kzquake`: current earthquake channel plus service continuity

Observed facts:

- The official archive `https://t.me/s/kzquake?before=1163`, accessed 2026-08-27, binds `@kzquake` to `Землетрясения | Казахстан`, labels the target with subscribers, and exposes a channel post sequence dated from at least 2023-08-29 through 2023-09-22. Every sampled post relays Kazakhstan earthquake bulletins from the relevant seismic network.
- Current search/open results on 2026-08-27 show about 2.0K subscribers and the description: operational earthquake reports for Kazakhstan, informative channel, posts after earthquakes, no predictions.
- Repository commit `fb345f9ebe9d24bf4756822eca059e42bd2878b3` introduced the exact handle on 2018-10-22 as “Бот следит за землетрясениями в КЗ”. Commit `d17b353...` carried the same handle/topic into structured JSON as a bot on 2026-01-30.

Target binding is direct and current; peer kind is channel. Cross-time continuity is **high, with one residual limitation**: exact handle and the unusually specific earthquake-monitoring function persist from 2018 through official 2023 posts and the 2026 target, while audience scale remains close to the stored 2,168. No source explicitly documents when or how a historical bot became a channel, so the evidence establishes service continuity more strongly than peer-ID continuity.

Counter-evidence sought: searches for a separate `kzquake` bot, migration notice, username reassignment, or distinct earthquake service produced no conflicting peer. Reclassification still requires owner approval and a post-mutation exact-handle recheck; the research does not treat search silence as identity proof.

### G4 — `mobile_developers_kz`: historical group, current shell, unbound alternative

Observed facts:

- Repository commit `fb5976c679440cbc6f780606365e67e2977e4ecb` introduced the exact handle on 2017-07-04 as a mobile-developer group, recording 12 members and an observation date of 2017-04-06.
- The public directory `https://kz.intelegram.one/chats/35`, accessed 2026-08-27, still indexes the exact handle and `Mobile Developers KZ` title with Kazakhstan mobile-chat rules. Its crawl/index date and current peer binding are not authoritative; it proves only an external historical trace consistent with the catalog.
- The current Phase D scripted and visible-browser evidence is only a Telegram contact shell. It binds no group peer, type, count, replacement, or death.
- A different living candidate exists: `https://tg-cat.com/@mobile_dev_kz?lang=ru`, accessed 2026-08-27, describes `Mobile Dev Kazakhstan` as a supergroup with about 1,005 members and an internal rules link under group id `1228999867`. A 2024-era LinkedIn community roundup (`https://ru.linkedin.com/posts/nikolay-kindyakov_%D0%BA%D0%B0%D0%BA-%D0%B6%D0%B5-%D0%BA%D1%80%D1%83%D1%82%D0%BE-%D1%87%D1%82%D0%BE-%D1%83-%D0%BD%D0%B0%D1%81-%D0%BF%D0%BE%D1%8F%D0%B2%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F-%D0%B2%D1%81%D1%91-%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5-activity-7183085791416352769-j38c`) independently lists that new handle as a Kazakhstan mobile-developer community.

The alternative is **not replacement evidence**: no migration notice, matching Telegram peer id, administrator statement, invite transition, or cross-link connects it to `mobile_developers_kz`. The old exact-handle directory entry and the new handle can represent distinct communities. Vacancy or topical similarity cannot close that gap.

Counter-evidence sought: a query combining the old handle with `closed`, `deleted`, `moved`, `new chat`, and `replacement` produced no migration or closure result; the accessible results only repeated the old directory entry and the separate new group. The Wayback CDX endpoint timed out without a response and supplied no archive evidence.

### G5 — `kzqacommunity`: strong historical identity, no current binding or death proof

Observed facts:

- Repository commit `fad259c9bd5ff4335d22ab5171c7eadbd1c5ab9f` introduced the exact handle on 2022-11-10 as a Kazakhstan QA group with `470+` members. Commit `d17b353...` preserved the same identity in structured JSON.
- The 2024-era LinkedIn roundup above independently binds `https://t.me/kzqacommunity` to `KZ QA community` and describes it as a Kazakhstan QA-specialist group.
- Telemetr pages `https://telemetr.io/en/channels/1473118772-kzqacommunity` and `/posts`, accessed 2026-08-27, retain Telegram id `1473118772`, the exact title and handle, the same group description, a QA-vacancies cross-link, and archived QA conversation content. They display 273 subscribers but no data for the last 30 days; this is a directory/archive observation, not current Telegram binding and not a reliable replacement count.
- The current official target `https://t.me/kzqacommunity`, the exact retry, and browser bundle all expose only a contact shell. They do not establish current peer kind, count, replacement, or death.

Historical continuity is **high through the last independent directory capture**, but present state is unestablished. The persistent external Telegram id is useful provenance; it does not prove that the username still resolves to that peer in August 2026. `@qaz_qa_vacancies` is a vacancy channel named in the old group's description, not a community replacement.

Counter-evidence sought: searches for closure, deletion, migration, replacement, and a current QA-community successor found no same-community notice. No independent source identifies the historical peer as closed/deleted, and no living replacement is continuity-bound.

### G6 — Deep OODA loop decisions

| Decision | Basis |
|----------|-------|
| GD1 — Treat official subscriber-labelled previews and the Phase D classifier as current channel-kind evidence for `datanomika` and `kzquake`. | Both requested handles are directly bound; the current pages expose channel-only subscriber/preview semantics, while the retry mismatch is reproducible. |
| GD2 — Treat cross-time handle + name/topic agreement as the minimum continuity signal, but require a post-reclassification recheck before any date/count write. | Both type-mismatch rows have repository provenance plus official historical channel content; no mutation may be based on count proximity alone. |
| GD3 — Do not promote `mobile_dev_kz` to a repair candidate beyond “unbound alternative”. | Same topic and country do not establish same community; no migration or peer-id link exists. |
| GD4 — Preserve both C4 rows as provisional `unresolved`; no archive hypothesis survived Gather. | Current shells are non-evidence, directory remnants prove history rather than death, and no independent closure source exists. |
| GD5 — Keep every observed external number non-mutating until Phase D reruns the exact handle after an approved type/link repair. | Research observations are evidence inputs, not production validator results, and the Phase D TS requires a recheck. |

### G7 — Metacognitive check

Gather discovered new information rather than only confirming Phase D: both type-mismatch records have positive cross-time continuity, `datanomika` was already demonstrably a channel in 2021, `mobile_dev_kz` is a real living but unbound alternative, and `kzqacommunity` has a persistent external Telegram id plus archived QA content despite the current shell. The important counter-result is also new: these external remnants narrow identity but still do not prove current life, replacement, or death for either C4 entry.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Current target binding and peer kind are established for both type mismatches; independent cross-time signals support continuity; historical identity is strengthened for both C4 records; no same-community replacement or death proof was found. | Extract the evidence packages into viable per-entry configurations and define the exact mutation/owner boundary; challenge username-reassignment and false-replacement alternatives. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one hypothesis tested? — H1 gained two positive target-bound channel cases; H2 remains unsupported because no death/private state is proven.
- [x] Counter-evidence sought?
- [x] Minimum two stage decisions recorded?
- [x] Metacognitive check completed?

Stage complete: YES
→ User decision: Close Gather and proceed to Extract; dig deeper only if the Coordinator has a target-specific source not yet tested.

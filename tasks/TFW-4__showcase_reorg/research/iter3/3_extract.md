# Extract — "What do we NOT see?"
> **Mindset:** Analyst. The raw findings are now arranged into an explicit configuration space; no disposition is accepted merely because it is the most convenient one.
> **Test:** "Does the configuration space reveal a combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Close the Phase D G2 evidence gap for `datanomika`, `kzquake`, `mobile_developers_kz`, and `kzqacommunity` with an exact, evidence-bounded per-entry disposition.

## Configuration Space

The five dimensions established in Briefing remain independent:

| Dimension | Values used below |
|-----------|-------------------|
| D1 — current requested-handle binding | target peer; generic/no target; wrong/reassigned peer; unavailable |
| D2 — observed peer kind | group/supergroup; broadcast channel; bot; not established |
| D3 — continuity | dated same handle/name/topic; documented migration/replacement; conflicting identity; no current continuity signal |
| D4 — present community state | live at stored handle; live at replacement; independently proven closed/deleted; unknown |
| D5 — strongest possible mutation | type reclassification; link repair; archive; unresolved/no mutation |

The rows are configurations that a G2 decision procedure must distinguish. They are not ranked here.

| ID | Entry | D1 binding | D2 kind | D3 continuity | D4 state | D5 possible disposition | Evidence that would select the row |
|----|-------|------------|---------|---------------|----------|-------------------------|------------------------------------|
| X1 | `datanomika` | target peer | broadcast channel | dated same handle/name/topic | live at stored handle | groups → channels reclassification | Current target-bound subscriber preview plus at least one independent dated same-handle, same-topic signal |
| X2 | `datanomika` | target peer | group/supergroup | dated same handle/name/topic | live at stored handle | unresolved/no mutation | A post-change or authenticated check contradicts the preview classifier and establishes group semantics |
| X3 | `datanomika` | wrong/reassigned peer | broadcast channel | conflicting identity | live wrong peer; old community unknown | unresolved/no mutation | Persistent peer ID, owner/admin notice, or other evidence shows the current username is not the historical catalogued community |
| X4 | `kzquake` | target peer | broadcast channel | dated same handle/name/topic | live at stored handle | bots → channels reclassification | Current target-bound subscriber preview plus an independent dated same-handle earthquake-service signal |
| X5 | `kzquake` | target peer | bot or mixed bot/channel service | dated same handle/name/topic | live at stored handle | unresolved/no mutation | Authenticated peer-kind evidence contradicts the public subscriber preview or shows a separately addressable bot |
| X6 | `kzquake` | wrong/reassigned peer | broadcast channel | conflicting identity | live wrong peer; old service unknown | unresolved/no mutation | Persistent peer ID or a dated migration record separates the historical bot identity from the current channel |
| X7 | `mobile_developers_kz` | unavailable/publicly unbound | group/supergroup | dated same historical identity only | stored peer may be private | unresolved/no mutation | Authenticated resolution binds the exact old username to the historical community, but no public target-specific preview exists |
| X8 | `mobile_developers_kz` | generic/no target | group/supergroup at `mobile_dev_kz` | documented migration/replacement | live at replacement | link repair | Same-peer ID, admin cross-link, explicit migration notice, or equivalent evidence binds old community to the candidate |
| X9 | `mobile_developers_kz` | generic/no target | group/supergroup at `mobile_dev_kz` | no current continuity signal | alternative is live; old community unknown | unresolved/no mutation | A live similarly scoped alternative exists without any migration, peer-ID, or administrator binding |
| X10 | `mobile_developers_kz` | unavailable/publicly unbound | not established | dated historical identity plus independent closure | independently proven closed/deleted | archive | Evidence explicitly identifies the same historical community as closed/deleted, followed by exact owner approval |
| X11 | `kzqacommunity` | unavailable/publicly unbound | group/supergroup | dated same historical identity only | stored peer may be private | unresolved/no mutation | Authenticated resolution binds the old username or persistent peer ID `1473118772` to a current private community |
| X12 | `kzqacommunity` | generic/no target | group/supergroup at a replacement | documented migration/replacement | live at replacement | link repair | Same-peer ID, explicit migration notice, or administrator cross-link identifies a current replacement |
| X13 | `kzqacommunity` | unavailable/publicly unbound | not established | historical peer ID plus independent closure | independently proven closed/deleted | archive | A source identifies peer `1473118772` / the exact historical community as closed or deleted, followed by exact owner approval |
| X14 | `kzqacommunity` | generic/no target | not established | dated historical identity only | unknown | unresolved/no mutation | Historical directory/archive material exists, but current binding, replacement, and same-community death all remain unproved |

X2 and X5 are newly visible counter-configurations: Telegram's technical `channel` object is not by itself proof of a broadcast channel because supergroups and broadcast channels share the MTProto channel constructor. The production validator avoids that ambiguity by inferring `groups` from target-bound `members`/group actions and `channels` from target-bound `subscribers`/channel actions (`scripts/validate_links.py:137-150,226-272`). Therefore the existing Phase D `observed_type=channels` rows are meaningful preview evidence, but an exact post-mutation validator recheck remains mandatory.

Official Telegram sources accessed 2026-08-27 support the discriminator boundary:

- [`Working with Channels, Supergroups, Gigagroups and Basic Groups`](https://core.telegram.org/api/channel) distinguishes broadcast channels from supergroups while explaining their shared underlying channel representation.
- [`channel` constructor](https://core.telegram.org/constructor/channel) exposes separate `broadcast` and `megagroup` flags.
- [`contacts.resolveUsername`](https://core.telegram.org/method/contacts.resolveUsername) returns a resolved peer or `USERNAME_NOT_OCCUPIED`; it establishes current username occupation, not historical continuity by itself.
- [`Bot API — Chat`](https://core.telegram.org/bots/api#chat) defines exact public chat kinds and a unique identifier. The repository's available historical sources do not expose comparable persistent IDs for both ends of either proposed replacement.

## Findings

### E1: `datanomika` has a bounded type-reclassification configuration

Current evidence selects X1 unless Challenge finds identity reassignment:

- Phase D live and exact-retry records bind the requested handle to visible `Datanomika`, classify the target-specific preview as `channels`, and expose no count while the entry is declared in `groups`.
- Current official Telegram preview (accessed 2026-08-27) binds `datanomika` to `Datanomika`, a subscriber surface, Alexander Polorotov/Datanomix, and data/BI subject matter.
- Official Telegram archive content at `https://t.me/s/datanomika?before=252` supplies a dated 2021 same-handle, same-title, same-author/topic signal.
- Repository commit `f8f2da3` supplies an independent 2020 catalog record for the exact handle and data/BI purpose. Nothing found indicates reassignment or a different historical peer.

The exact supportable mutation package is intentionally narrow:

1. move the unchanged `datanomika` record from `groups` to `channels`;
2. remove the group-only `category` field as required by the current schema shape;
3. preserve handle, name, descriptions, old count, and old verification date during the structural move;
4. run `python scripts/validate_links.py --handle datanomika --update --summary-json <new-evidence-path>` after the move;
5. accept a new count/date only from that fresh target-bound `verified` channel result, then run the normal schema/generator gates;
6. perform none of the above until the owner gives the exact Phase D G2 approval.

If the post-change exact retry is not `verified`, the package fails closed: do not retain a new date/count, do not call the record repaired, and return it to G2 unresolved.

**Extract decision E-D1:** X1 is the reclassification candidate; the post-move exact retry and owner G2 approval are mandatory parts of the decision.

### E2: `kzquake` supports the same structural repair, but exposes a label-consistency branch

Current evidence selects X4 unless Challenge finds an undocumented peer split:

- Phase D live and exact-retry records bind the requested handle to `Землетрясения | Казахстан`, classify the target-specific subscriber preview as `channels`, and expose no count while the entry is declared in `bots`.
- Official archive content at `https://t.me/s/kzquake?before=1163` shows the same handle/title and dated 2023 earthquake bulletins; the current Telegram page describes operational earthquake reports.
- Repository commit `fb345f9` supplies the independent 2018 exact-handle earthquake-monitoring record. The word “bot” in that old catalog row establishes the old declaration, not a distinct peer or a bot-to-channel migration.
- No separate bot handle, documented migration, historical/current peer-ID pair, or reassignment signal was found.

Two structural packages must not be silently conflated:

| Package | Exact edits supported | Consequence |
|---------|-----------------------|-------------|
| K-min | Move the unchanged record from `bots` to `channels`; retain handle/count/date; exact-retry as declared channel | Type is repaired, but published `name = KZ Quake Bot` and Russian text “Бот…” remain factually inconsistent with the observed peer |
| K-coherent | K-min plus change the display name to the observed `Землетрясения \| Казахстан` and replace the bot-specific Russian wording with a channel-kind statement limited to the observed earthquake-monitoring fact | Produces a coherent channel entry, but includes factual label/description edits beyond a pure type move and therefore needs explicit owner G2 wording |

Both packages require `python scripts/validate_links.py --handle kzquake --update --summary-json <new-evidence-path>` after the move; only a fresh target-bound `verified` channel result may write the new date/count. K-min is structurally narrower but is not publication-coherent. Research does not choose K-coherent or invent its final prose; Challenge must test whether Phase D's contract permits that factual correction or whether the Coordinator must split it into a later approved task.

**Extract decision E-D2:** X4 is the peer-kind disposition candidate, but exact G2 must distinguish type-only K-min from the separately authorized factual-label K-coherent branch.

### E3: `mobile_dev_kz` is only X9, not X8

The evidence configuration is:

- exact old handle: current contact shell, `target_bound=false`, no current count or peer kind;
- historical identity: 2017 repository record plus the exact-handle historical directory page;
- candidate `mobile_dev_kz`: a living mobile-development supergroup in a 2024 roundup/directory trail;
- continuity: no same-peer ID, migration notice, old/new cross-link, shared administrator assertion, or source explicitly equating the two communities;
- closure: no independent evidence that the historical community closed or was deleted.

The candidate therefore cannot select X8. A similarly scoped living group does not repair the stored link, and the generic shell does not select X10. The exact present disposition is X9: **UNRESOLVED, no mutation**. A future link repair requires explicit old→new continuity; an archive requires independent same-community death evidence and owner approval.

**Extract decision E-D3:** keep `mobile_developers_kz` unresolved; record `mobile_dev_kz` only as an unbound alternative that must not enter an implementation plan as a replacement.

### E4: `kzqacommunity` is historical-identity evidence without present-state evidence

The evidence configuration is:

- exact old handle: current contact shell, `target_bound=false`;
- historical identity: 2022 repository record, 2024 exact-handle roundup, and Telemetr's exact title/topic with persistent historical channel ID `1473118772` and archived QA content;
- current binding: neither official target preview nor authenticated resolution binds that ID/handle to a living QA community;
- replacement: none; `qaz_qa_vacancies` is a vacancy channel, not continuity evidence for the general QA community;
- closure: no independent same-community deletion/closure evidence.

This selects X14, not X12 or X13. The exact present disposition is **UNRESOLVED, no mutation**. The historical peer ID makes a future authenticated ID comparison decisive, but it does not prove present life or death on its own.

**Extract decision E-D4:** keep `kzqacommunity` unresolved; do not repair, archive, refresh its date, or replace its old count.

### E5: Exact validator semantics make the recheck evidence-bearing

The current validator first binds identity from preview-owned canonical/OG/primary-action URLs, rejects conflicting or non-target previews, and only then infers type from target-specific `members`, `subscribers`, or action text. A declared mismatch returns `ambiguous` with no observed count; after a correct structural reclassification, the same preview can become `verified` and only then yield a count and date (`scripts/validate_links.py:176-273,336-375`).

Consequently, external preview counts observed during Research are context, not mutation inputs. Neither `2,799` for `datanomika`, approximately `2.0K` for `kzquake`, nor Telemetr's historical QA number may be copied into data. The exact post-change retry is the authoritative new observation and must be preserved in Phase D evidence.

**Extract decision E-D5:** a G2 “reclassify” verdict is a conditional configuration: approved structural mutation → exact declared-type retry → verified/non-verified branch. It is not an unconditional data edit.

## Hypothesis and Counter-evidence Check

| Item | Result after Extract |
|------|----------------------|
| H1 — target-bound mismatches are type errors rather than dead links | Supported for both handles by cross-time handle/name/topic continuity; still conditioned on Challenge finding no reassignment or separate-peer evidence |
| H2 — one or both contact shells can be resolved to a safe repair/death disposition | Not supported. `mobile_dev_kz` remains unbound; QA has historical identity but no current binding; neither has death evidence |
| Counter-evidence search | Official Telegram type semantics refute any shortcut from a raw MTProto `channel` object to catalog `channels`; the repository validator's target-bound subscriber/group-action semantics avoids that shortcut. No persistent-ID or migration counter-evidence against either target-bound continuity chain was found |
| New combination absent from Briefing | K-min can repair the array type while leaving a publicly misleading bot label. Peer-kind repair and factual label coherence are separate authorization/configuration choices |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| `datanomika`: X1, conditional groups→channels reclassification; preserve facts, remove group-only category, exact retry, owner G2 | Challenge must try to falsify historical continuity/reassignment and the assumption that the public subscriber preview represents the same service |
| `kzquake`: X4, conditional bots→channels reclassification with K-min/K-coherent split | Challenge must test whether an undocumented bot/channel split is plausible and whether Phase D may include the coherent factual-label correction |
| `mobile_developers_kz`: X9 UNRESOLVED; `mobile_dev_kz` is an unbound alternative | A repair needs explicit old→new continuity; archive needs same-community death evidence; neither exists |
| `kzqacommunity`: X14 UNRESOLVED | Authenticated resolution/peer-ID comparison, documented replacement, or independent death evidence remains absent |

**Sufficiency:**
- [x] External source used? Official Telegram channel/supergroup, constructor, username-resolution, and Chat-type documentation were consulted in this stage.
- [x] All five Briefing dimensions used? Yes; every configuration names binding, kind, continuity, present state, and mutation boundary.
- [x] At least two decisions recorded? Yes; E-D1 through E-D5.
- [x] Hypotheses tested? H1 is conditionally supported; H2 is not supported.
- [x] Counter-evidence actively sought? Yes; the shared MTProto channel representation and potential separate-peer/reassignment cases were tested as alternatives.
- [x] Structured comparison reveals an unproposed combination? Yes; K-min repairs type while leaving false bot-facing labels.

Stage complete: YES
→ Coordinator decision: close Extract and proceed to Challenge, preserving both C4 entries as UNRESOLVED/no mutation and treating the two type repairs as conditional on exact post-change validator evidence plus owner G2 approval.

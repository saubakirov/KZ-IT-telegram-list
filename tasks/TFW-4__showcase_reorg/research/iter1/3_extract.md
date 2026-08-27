# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Structure the bounded Telegram observations so Phase C does not collapse liveness, preview availability, and count availability into one signal.

## Configuration Space

| Config | D1: Telegram response shape | D2: Member-count evidence | D3: Liveness discriminator |
|--------|-----------------------------|---------------------------|----------------------------|
| C1 | public preview with `tgme_page_extra` | `N members` text | positive public-preview marker |
| C2 | public preview with `tgme_page_extra` | `N subscribers` text | positive public-preview marker |
| C3 | public preview with `tgme_page_extra` | no count evidence | positive public-preview marker |
| C4 | syntactically valid contact shell without preview metadata | no count evidence | route/title classification without a preview |
| C5 | global Telegram landing page | members-like text unrelated to the target | route/title classification without a preview |
| C6 | explicit error/deleted page | no count evidence | explicit `tgme_page_error`/deleted marker |
| C7 | explicit error/deleted page | no count evidence | non-success HTTP status |

C3 is the combination not anticipated in the Briefing: a valid public preview can deliberately expose `tgme_page_extra` without any member/subscriber count, as observed for three bots. Count absence therefore cannot be used as a death signal.

## Findings

### E1: Bounded mixed-sample observations

Eight additional catalog handles were fetched on 2026-08-26 (+05:00) at the current script cadence: batches of three, 0.3 seconds after each request, and 1.5 seconds between batches. No HTTP 429 or other request error occurred.

| Type | Handle | Stored count | HTTP / response config | Parsed now | Evidence |
|------|--------|--------------|------------------------|------------|----------|
| group | `mobile_developers_kz` | absent | 200 / C4 contact shell | absent | title `Telegram: Contact @mobile_developers_kz`; no preview/error marker |
| group | `frontendkz` | 4440 | 200 / C1 | 4636 | `4 636 members, 1 136 online` |
| channel | `bluescreenkz` | 24549 | 200 / C2 | 24844 | `24 844 subscribers` |
| channel | `thetechkz` | 22929 | 200 / C2 | 26645 | `26 645 subscribers` |
| bot | `ShtrafKZBot` | absent | 200 / C3 | absent | preview title present; extra contains only `@ShtrafKZBot` |
| bot | `Get_Telegram_ID_bot` | absent | 200 / C3 | absent | preview title present; extra contains only `@Get_Telegram_ID_bot` |
| bot | `chat_prettier_bot` | absent | 200 / C3 | absent | preview title present; extra contains only `@chat_prettier_bot` |
| bot | `kzquake` | 2168 | 200 / C2 | 1984 | `1 984 subscribers` |

This sample covers all four entries that currently lack `member_count`. Three are C3—positive public previews with no count—and one is C4, which is observationally identical to the random valid-form probe shell from Gather.

### E2: Count availability, preview availability, and liveness are separate axes

The four missing-count entries do not share one response shape:

- The three bots provide positive target-specific preview metadata but no count. They support the frozen F6 fix: a legitimate successful check may have no parsed count, so count-gated `last_verified` updates are structurally wrong.
- `mobile_developers_kz` provides only a contact shell. The same response shape was returned for the random valid-form probe. The current classifier cannot distinguish a reachable private/contact-only target from a nonexistent target, so marking either one "verified alive" would overstate what the response proves.
- A positive `tgme_page_extra` marker is useful but not sufficient by itself to demand a count; bot previews use the same element for the handle.

### E3: H2 is not decided by this sample

All eight requests returned HTTP 200 and none carried a negative marker. That does not refute the existential claim that at least one of 63 handles is dead/private. More importantly, the C4 response is ambiguous: it may be a private/contact-only target or an absent handle, and the bounded observation supplies no independent identity signal.

The sample therefore measures a **0/8 explicit failure-marker rate**, not a 0/8 dead rate. Reporting the latter would violate the project's accuracy-over-coverage principle.

**Extract decision E-D1:** H2 remains inconclusive. The bounded sample can establish response configurations and rate-limit behavior, but neither settle a catalog-wide existential claim nor classify C4 as alive, private, or dead.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| No HTTP 429 occurred across eight requests at the existing throttle. | Behavior across the full 63-entry sweep remains Phase D evidence, not research evidence. |
| Three bot previews are valid C3 configurations: positive preview, no count. | Whether Telegram exposes a stronger target-identity signal for C4 contact shells requires a later focused investigation. |
| The catalog's no-count group is C4 and indistinguishable from the unresolved random valid-form probe under the current classifier. | H2 remains inconclusive; no owner archive triage is warranted from this sample. |

**Sufficiency:**
- [x] External source used? Eight public `t.me` catalog responses were observed under the control-file throttle.
- [x] Briefing gap closed? All four no-count entries, multiple types, explicit failures, and HTTP 429 behavior were covered within the bounded sample.
- [x] Configuration Space built from Gather dimensions? Seven non-contradictory response/parser/classifier configurations are recorded, including the unanticipated C3 bot case.

Stage complete: YES
→ User decision: Close Extract; proceed to Challenge for GitHub anchor verification and contract consistency checks.

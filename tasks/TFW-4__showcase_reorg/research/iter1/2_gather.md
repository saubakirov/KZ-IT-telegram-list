# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Determine whether Phase C can safely rely on the current Telegram response and parser assumptions before its tooling is specified.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1: Telegram response shape | public preview with `tgme_page_extra` | syntactically valid contact shell without preview metadata | global Telegram landing page | explicit error/deleted page |
| D2: Member-count evidence | `N members` text | `N subscribers` text | leading digits inside `tgme_page_extra` | no count evidence |
| D3: Liveness discriminator | explicit `tgme_page_error`/deleted marker | non-success HTTP status | positive public-preview marker | route/title classification without a preview |

## Findings

### G1: Current classifier assumptions in `validate_links.py`

The local parser checks two negative body markers—`tgme_page_error` and `This group or channel no longer exists`—then treats every other successful HTTP response as alive. Count parsing tries these regexes in order:

1. `(\d[\d\s]*)\s*members?`
2. `(\d[\d\s]*)\s*subscribers?`
3. `<div class="tgme_page_extra">(\d[\d\s]*)`

This means HTTP 200 plus neither negative marker is currently sufficient for an `OK` verdict even when no Telegram preview metadata exists.

### G2: Live public previews still expose compatible count markup

Observed from public `t.me` responses on 2026-08-26 (+05:00), using the same user agent, language header, and 15-second timeout as the script:

| Kind | Handle | HTTP | Relevant observed markup | Pattern results | Classifier implication |
|------|--------|------|--------------------------|-----------------|------------------------|
| high-count group | `itmankz` | 200 | `<div class="tgme_page_extra">8 210 members, 1 665 online</div>` | P1=`8 210`; P2=no match; P3=`8 210` | alive, count 8210 |
| channel | `workitkz` | 200 | `<div class="tgme_page_extra">34 808 subscribers</div>` | P1=no match; P2=`34 808`; P3=`34 808` | alive, count 34808 |

The count half of H1 is confirmed for both required public-page types. Pattern 3 remains a structural fallback, but patterns 1 and 2 win first for the observed pages.

### G3: A missing handle no longer yields the assumed error marker

Two synthetic routes exposed distinct non-preview responses:

| Route | HTTP | Preview/error markers | Meta evidence | Regex result | Current classifier result |
|-------|------|-----------------------|---------------|--------------|---------------------------|
| malformed over-length handle | 200 | no `tgme_page_extra`; no error/deleted marker | generic `Telegram – a new era of messaging` landing page | P1 falsely matched `000` inside `groups can hold up to 200,000 members` | alive, count 0 |
| syntactically valid random probe handle `tfw4probe20260826xqz` | 200 | no `tgme_page_extra`; no error/deleted marker | `Telegram: Contact @tfw4probe20260826xqz`, empty description | no pattern matched | alive, no count |

The first route demonstrates an additional false-positive count mode: the broad members regex can start after punctuation in `200,000 members`, capture `000`, and return integer zero. The second route demonstrates the C4 ambiguity, but the contact shell does not independently prove whether the random handle exists. The assumed `tgme_page_error` rejection is therefore refuted for a deliberately malformed invalid route and remains unverified for a genuinely dead/private target.

**Gather decision G-D1:** split compound H1. Public preview count compatibility is confirmed; marker-based rejection is refuted for malformed invalid input and unverified for genuinely dead/private targets. It must not be represented as one confirmed hypothesis.

### G4: Probe accounting

Gather made five external HTTP requests, equal to the configured soft limit of five web queries per stage. The planned three-request batch covered the two live handles and one malformed route. The unexpected generic landing page required one repeat to capture the exact false-match context; a final valid-form random probe corrected the malformed-route bias. The failed PowerShell invocation that rejected an unsupported parameter issued no HTTP request. No further Gather probes were made, and the catalog sample was not expanded.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Live group and channel count markup remains compatible with the current parser. | Whether the four no-count catalog entries are legitimate contact/bot pages or expose the same ambiguous shell. |
| Invalid/contact-style routes can return HTTP 200 without either negative marker, so the current classifier calls them alive. | Whether any actual catalog handle in the bounded sample returns an error, a contact shell, or HTTP 429. |
| The broad members regex can parse a generic landing-page capacity sentence as count zero. | Catalog-wide dead rate remains deliberately unknown; the full sweep belongs to Phase D. |

**Sufficiency:**
- [x] External source used? Five public `t.me` requests covering two live catalog handles, a malformed route (including one diagnostic repeat), and one valid-form random probe.
- [x] Briefing gap closed? H1's count and negative-marker clauses were independently tested with actual response bytes.
- [x] Dimensions identified? Three independent response/classification factors with at least three alternatives each.

Stage complete: YES
→ User decision: Close Gather; proceed to the bounded mixed-sample Extract stage.

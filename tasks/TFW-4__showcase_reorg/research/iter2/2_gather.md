# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Establish an honest, repeatable evidence boundary for Telegram liveness so the catalog can publish dated verification without inferring identity, life, death, or member counts.

## Comparison Matrix

The question has two coupled decisions—what a signal proves and what state transition it permits—rather than three independent dimensions. A comparison matrix is therefore more useful than a Configuration Space.

| Signal | Current target identity | Distinguishes group/channel from user or unassigned name? | May refresh `last_verified`? | May justify archive? |
|--------|-------------------------|----------------------------------------------------------|------------------------------|----------------------|
| Target-specific public `t.me` preview (`tgme_page_title` plus group/channel metadata) | Strong positive for the requested public target | Yes, when the preview exposes the declared chat type/content | Yes, after a successful same-run response; count may remain absent | No—positive evidence contradicts archive |
| HTTP 200 C4 contact shell (`Telegram: Contact @handle`, no preview metadata) | None beyond echoing the requested route | No; the same shape is returned for an unresolved random valid-form handle | No | No; ambiguity is not death |
| Authenticated Telegram `contacts.resolveUsername` returning a supergroup/channel peer | Authoritative current username-to-peer binding | Yes | Yes, if the returned peer matches the catalogued community; capture the response/client observation | No—positive evidence contradicts archive |
| Authenticated resolution returning a user, a different chat, or `USERNAME_NOT_OCCUPIED`/equivalent | Strong negative for the catalogued handle-to-community binding | Yes | No | Opens link-repair/death triage, but does not by itself prove the historical community died |
| Valid private invite checked through Telegram (`messages.checkChatInvite` or owner client) | Positive for the invite's current private chat | Yes for that invite, not for the old public username | Not for the unchanged `t.me/{handle}` entry; repair the catalog link first | No if the community is alive; update/repair is required |
| Historical repository row, search result, or old member count | Historical existence only | No current distinction | No | No |
| Explicit owner evidence that the actual community was deleted/closed after retry and target resolution | Negative current community evidence | Yes when the observation identifies the same community | No | Yes; archive rather than delete, with the observed reason |

## Findings

### G1: “Private handle” combines two different Telegram identifier models

Telegram's official [Channels FAQ](https://telegram.org/faq_channels) states that public channels have usernames while private channels require an invite link. The official [Invite Links API documentation](https://core.telegram.org/api/invites) says that only supergroups and channels may have public usernames and distinguishes those usernames from private invite links. The official [Deep Links documentation](https://core.telegram.org/api/links) likewise uses `t.me/<username>` for public links and `t.me/+<hash>` / `t.me/joinchat/<hash>` for private invitations.

Therefore a C4 `t.me/mobile_developers_kz` page cannot be labelled “a legitimate private group handle” from the public URL alone. The realistic states are:

1. the username currently resolves to the intended group but the unauthenticated web preview is withheld;
2. the old community is still alive under a private invite or a different username, while this public link is stale;
3. the username resolves to a user or another peer;
4. the username is not currently occupied/resolvable.

Only state 1 verifies the current catalog link. State 2 calls for link repair, not archive. States 3-4 prove that the catalog link is wrong, not that the historical community died.

**Gather decision G-D1:** model current handle binding and historical community existence as separate facts. Archive policy cannot collapse them into one `dead/private` status.

### G2: Telegram defines an authoritative current-identity operation, but it is authenticated

Telegram's official [Invite Links API documentation](https://core.telegram.org/api/invites) identifies `contacts.resolveUsername` as the operation that returns the peer bound to a public username. The same documentation identifies `messages.checkChatInvite` for inspecting a private invite. These operations can distinguish a current group/channel, a user/wrong peer, an unoccupied username, and a valid private replacement link. The unauthenticated `t.me` contact shell does not expose the resolved peer.

This is a CL dependency, not a parser trick: resolving C4 requires an authenticated Telegram client/API observation or an equivalent owner-performed in-client global-search/open check. The research session has no Telegram account authorization and appropriately did not request credentials.

**Gather decision G-D2:** authenticated peer resolution is sufficient identity evidence; HTTP status, echoed contact title, and URL syntax are not substitutes.

### G3: The `/s/` surface preserves the C4 ambiguity

Three usable `https://t.me/s/...` responses were observed on 2026-08-26 with `curl`, after the same user agent, 15-second timeout, and bounded cadence used by the project:

| Route | HTTP transport | Title | Positive preview markers | Error marker | What it proves |
|-------|----------------|-------|--------------------------|--------------|----------------|
| `/s/mobile_developers_kz` | success | `Telegram: Contact @mobile_developers_kz` | none | none | C4 remains ambiguous on the alternate public surface |
| `/s/tfw4probe20260826iter2` | success | `Telegram: Contact @tfw4probe20260826iter2` | none | none | a fresh valid-form probe has the same signal class; not proof that either name is occupied or absent |
| `/s/frontendkz` | success | `Telegram: View @frontendkz` | target title, description, `tgme_page_extra` | none | positive control: `/s/` can expose a target-specific public group preview when Telegram has one |

The first two responses differ in echoed handle text and byte length but not in any target-specific group/channel marker inspected. The positive control shows that the absence is not a universal `/s/` limitation.

**Gather decision G-D3:** alternate unauthenticated page shape does not close C4 identity; stop probing web variants and use the authoritative resolution boundary.

### G4: Repository history proves old existence, not present identity

`git log -S mobile_developers_kz` traces the link to commit `fb5976c` on 2017-07-04, whose README row recorded 12 members on 2017-04-06. The JSON representation was introduced in `d17b353` / the current line lineage on 2026-01-30 with no `member_count` and `last_verified: 2026-01-30`.

The current code refreshes `last_verified` only when a member count parses. Because this entry has no count and now returns C4, the repository cannot demonstrate a successful current target-specific check for it. Historical existence is useful for owner triage—there was once a real community behind the name—but it cannot date the current link.

**Gather decision G-D4:** treat the 2017 row as provenance, not liveness evidence.

### G5: Probe accounting and limit

The external evidence set used three official Telegram documentation searches and a bounded group of public-page attempts. Eight `Invoke-WebRequest` attempts produced no usable record because the local PowerShell wrapper raised a null-reference exception; three diagnostic `/s/` requests were then repeated with `curl` and recorded above. This exceeded the focused soft limit of five page attempts, but remained limited to one catalog target and two controls, did not repeat iteration 1's eight-handle sample, and did not approach the 63-entry sweep. No additional Gather probes were made after the usable comparison was obtained.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Official identifier semantics rule out equating a public username with a private invite link. | `mobile_developers_kz` still requires authenticated owner/client peer resolution; this session cannot supply it without credentials. |
| `/s/` reproduces C4 for the catalog target and a fresh probe, while a public group control exposes target-specific metadata. | Whether the old community is alive under a replacement link is an owner/community fact, not observable from C4. |
| The evidence matrix separates current handle binding, link repair, and community death. | Extract must turn that separation into deterministic `last_verified` and archive-triage rules and test frozen DoD 22. |

**Sufficiency:**
- [x] External source used? Official Telegram FAQ/API documentation plus three recorded live `t.me/s/` responses.
- [x] Briefing gap closed? The strongest bounded signal is identified: authenticated peer resolution; unauthenticated C4 variants are insufficient.
- [x] Comparison matrix used? Yes—fewer than three independent dimensions exist.

Stage complete: YES
→ User decision: close Gather; proceed to evidence-rule extraction within the fixed iteration-2 scope.

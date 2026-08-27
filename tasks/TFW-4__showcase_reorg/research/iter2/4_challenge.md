# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Establish an honest, repeatable evidence boundary for Telegram liveness so the catalog can publish dated verification without inferring identity, life, death, or member counts.

## Stress Test of Extract Cases

Gather used a comparison matrix, so Challenge stress-tests each Extract case against edge conditions and counter-evidence rather than constructing pairwise dimension combinations.

| Candidate rule | Attack | Result | Disposition |
|----------------|--------|--------|-------------|
| Any HTTP 200/contact title refreshes `last_verified` | Fresh valid-form probes receive the same C4 shell; the title only echoes the route | False positive | Eliminated |
| Historical existence plus C4 refreshes the date | A username can be removed, changed, reassigned, sold, or kept unassigned; 2017 evidence cannot bind the 2026 peer | False positive | Eliminated |
| `contacts.resolveUsername` success always proves the intended community | It proves the current peer, but the username may now bind a user or a different/reassigned chat | Incomplete | Survives only with declared-type and continuity/owner match |
| `USERNAME_NOT_OCCUPIED` proves the community died | A living group may have gone private or changed username | False death | Eliminated |
| A valid replacement invite permits archiving the old entry | The invite is positive evidence the community lives | Contradiction | Eliminated; repair link instead |
| Owner approval alone permits archive | Authority can approve a disposition but cannot manufacture death evidence | Evidence gap | Eliminated |
| Retry + target-specific preview or matched authenticated peer refreshes the date | Handles transient failure and positively binds current target | No counterexample found within scope | Survives |
| Retry + owner evidence of the same community's deletion archives it | Separates broken links from death and preserves trace | No counterexample found within scope | Survives |
| No independent result leaves the entry unresolved and blocks all-verified claims | Sacrifices coverage/release progress rather than inventing state | Deliberately conservative | Survives |

## Surviving Rules

| Rule | Required evidence | Permitted result | Notes |
|------|-------------------|------------------|-------|
| S1 — public target | Target-specific preview matching requested handle and declared peer kind | Refresh `last_verified`; count independent | Covers iteration 1 C1-C3 |
| S2 — withheld preview | Authenticated resolution returns intended peer kind and continuity is matched by title/about, prior peer knowledge, or owner client observation | Refresh `last_verified` with artifact | Necessary path for a legitimate C4 target |
| S3 — stale link, live community | Valid current username/invite for the same community | Repair stored link, recheck, then date | Never archive living community |
| S4 — dead community | Retry plus independent owner/client evidence identifying the historical community as deleted/closed | Archive with observed reason/date | Wrong/unoccupied username alone is insufficient |
| S5 — unresolved | No positive binding and no death/replacement evidence | No date, no archive; task gate remains open | Honest blocking state |

**Unexpected survivor:** S3. A broken public handle can coexist with a living community, so a correct workflow needs a repair branch even though the frozen Phase D prose emphasizes alive versus archive.

## Findings

### C1: Username mutability defeats historical-link and route-only proof

Telegram officially allows administrators to [change or remove a supergroup/channel username](https://core.telegram.org/method/channels.updateUsername). The official [Telegram FAQ](https://www.telegram.org/faq) says collectible usernames can be assigned to chats, sold, or kept for later use, and Telegram reserves the right to recall usernames from unused bots/channels. The official [Fragment username documentation](https://core.telegram.org/api/fragment) also describes associating, dissociating, and deactivating usernames when a group becomes private.

Consequences:

- `mobile_developers_kz` may once have named the 2017 group and now name nothing, a held collectible, a user, or a different chat;
- a positive current peer result is necessary, but continuity with the catalogued community must also be checked;
- a negative current result proves only that this link no longer names the intended public peer.

**Challenge decision C-D1:** strengthen authenticated resolution from “peer kind matches” to “peer kind plus identity continuity matches.” Record the returned peer ID in evidence even though adding it to the catalog schema is outside this research scope.

### C2: Legitimate private survival is a repair case, not an archive exception

Telegram's official [channel/group documentation](https://core.telegram.org/api/channel) distinguishes a public username from a private invite link, and `channels.updateUsername` allows an administrator to remove the username while the supergroup/channel continues to exist. Therefore the phrase “absent/private handle” must not be one archive reason.

If the owner opens the old community and supplies a valid private invite, the observation proves the community is alive. The current JSON schema and generator assume a bare public `handle`, so that invite may require a scoped link-model change or a current public replacement before the entry can return to the live catalog. That implementation choice is for the Coordinator; the research conclusion is only that archive-as-dead would violate frozen DoF 3.

**Challenge decision C-D2:** archive triage must expose repair, death, and unresolved branches. A binary alive/archive prompt is unsafe for C4.

### C3: DoD 22 has an honest success path but an unresolved owner gate

The strongest counterargument is that no amendment is needed: current DoD 12 says every HTTP responder is dated, so `mobile_developers_kz` can receive today's date and DoD 22 can pass. That reading fails the task's own evidence purpose. C4 supplies no positive target binding; the same public response class appears for a fresh probe. Writing the date would turn “Telegram served a generic contact shell” into “this mobile-development community was verified,” which is the inference forbidden by DoF 4 and the accuracy principle.

The honest paths are finite:

1. owner-authenticated resolution + continuity match → date it;
2. replacement current link/invite → repair, recheck, then date it;
3. owner evidence of historical-community death → archive it;
4. none of the above → DoD 22 remains unsatisfied.

Pending A5 would make the classifier represent C4 as ambiguous, but A5 remains `PROPOSED — awaiting owner verdict`. Until that verdict exists, a Coordinator cannot write a TS that silently uses its behavior. If A5 is rejected, the contradiction between literal DoD 12 and evidence-safe behavior must return to the owner; research cannot select a preferred frozen meaning.

**Challenge decision C-D3:** research is sufficient; planning is gated by the A5 verdict and one owner-authenticated `mobile_developers_kz` observation. Further unauthenticated probing would repeat the same ambiguity, not reduce it.

### C4: No new amendment proposal is warranted now, but a future trigger is explicit

The control file asks for a separate §5 proposal only if no independent signal is sufficient. `contacts.resolveUsername` plus continuity evidence is sufficient, so iteration 2 does not file a duplicate proposal. This is not an approval or application of A5.

A separate proposal becomes necessary only if:

- the owner cannot obtain authenticated resolution evidence, or
- the result is wrong/unoccupied and neither a replacement link nor death evidence exists, but the owner still wants TFW-4 to proceed without the unresolved entry.

At that point the proposal must state whether frozen DoD 22 is superseded, whether an unresolved/quarantine data state is added, or whether the phase is restricted. Those are owner choices with different contract costs; selecting one now would invent a preference before the triggering fact exists.

**Challenge decision C-D4:** recommend no new amendment proposal in this RES; preserve the precise future trigger and route it to `/tfw-plan`.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Route-only, historical-only, and wrong/unoccupied-to-death rules fail under official username mutability. | Actual current peer and continuity result for `mobile_developers_kz` remains an owner-authenticated CL observation. |
| Five evidence-safe rules survive and include the non-obvious repair branch. | A5 still needs an explicit owner verdict before its behavior can enter a TS. |
| DoD 22 is conditionally achievable and research-complete; unresolved state blocks the task rather than inviting inference. | Coordinator must decide whether to obtain the observation before TS or encode it as a Phase C/D evidence gate. |

**Sufficiency:**
- [x] External source used? Official Telegram username mutation, channel/private-link, FAQ, and collectible-username documentation.
- [x] Briefing gap closed? C4 identity, evidence rules, archive triage, and DoD 22 paths have all been adversarially tested.
- [x] Options stress-tested? Yes; false positives, false death, reassignment, private survival, transient failure, and frozen-contract conflict were covered.

Stage complete: YES
→ User decision: close Challenge; synthesize iteration 2 RES with `SUFFICIENT` recommendation.

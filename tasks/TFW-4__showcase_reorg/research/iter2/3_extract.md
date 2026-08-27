# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Establish an honest, repeatable evidence boundary for Telegram liveness so the catalog can publish dated verification without inferring identity, life, death, or member counts.

## Structured Comparison

Gather used a comparison matrix because the problem has fewer than three independent dimensions. The cases below cross-reference response class, independent identity evidence, and the strongest permitted result without evaluating implementation design.

| Case | Public response | Independent evidence | Strongest supported claim | `last_verified` consequence | Disposition consequence |
|------|-----------------|----------------------|---------------------------|-----------------------------|-------------------------|
| X1 | Target-specific group/channel preview | Same response binds handle and declared chat type | Current catalog target is reachable | Refresh; count separately observed or absent | Keep live |
| X2 | C4 contact shell | `contacts.resolveUsername` returns intended supergroup/channel | Current username is bound to the intended community despite withheld web preview | Refresh from authenticated observation; capture peer/type/title artifact | Keep live |
| X3 | C4 contact shell | Resolution returns user or wrong chat | Catalog link does not identify the catalogued community | Do not refresh | Repair/death triage; wrong binding is not proof the old community died |
| X4 | C4 contact shell | `USERNAME_NOT_OCCUPIED` / equivalent | No current peer occupies the public username | Do not refresh | Repair/death triage; non-occupation is not proof the old community died |
| X5 | C4 contact shell | Owner supplies valid invite/current replacement for same community | Community is alive, but the stored public link is stale | Do not refresh the stale entry; repair link, then recheck | Keep live after repair; never archive as dead |
| X6 | C4 or explicit failure after retry | Owner evidence identifies the same historical community as deleted/closed | Community death is evidenced | Do not refresh | Archive, never delete, with date and observed reason |
| X7 | C4 or transient failure | No independent evidence | Identity and life/death remain unknown | Do not refresh | Leave unresolved; block any claim that all live links were verified |

X5 is the non-obvious case revealed by the comparison: a handle can be invalid while the community is alive. It survives neither a binary alive/dead classifier nor an archive-on-failure policy, and it is exactly why target binding and community existence must remain separate.

## Findings

### E1: Evidence rule for `last_verified`

`last_verified = D` means: **on date D, a network observation positively bound the catalogued link identifier to the intended Telegram peer of the declared type.** It does not mean merely that Telegram returned HTTP 200, that a title echoed the requested string, that the community existed historically, or that a human remembered it.

Minimum admissible evidence is one of:

1. **Public-preview evidence:** a same-run, target-specific `t.me` preview exposes the requested username plus metadata consistent with the declared type (group/supergroup, channel, or bot). Numeric count is independent; its absence does not invalidate identity.
2. **Authenticated-resolution evidence:** Telegram's documented `contacts.resolveUsername` returns a `contacts.ResolvedPeer` whose peer and returned `chats`/`users` entry bind the requested username to the intended declared type. Record the date, handle, peer kind/flags, displayed title/name, and sanitized output or client screenshot.
3. **Repaired-link evidence:** if a stale handle is replaced with a current public username or supported invite link, validate that new stored link first; never transfer the old handle's date to the replacement by inference.

The official [`contacts.resolveUsername` method](https://core.telegram.org/method/contacts.resolveUsername) documents `USERNAME_NOT_OCCUPIED` as the negative result and returns `contacts.ResolvedPeer` on success. The official [`Contacts.ResolvedPeer` type](https://core.telegram.org/type/contacts.ResolvedPeer) carries the resolved peer plus chat/user vectors. The official [`messages.checkChatInvite` method](https://core.telegram.org/method/messages.checkChatInvite) can validate a private invite, but only users can call it and it validates that invite—not the stale public handle.

**Extract decision E-D1:** count success, HTTP success, and target verification are three independent states. Only target verification writes `last_verified`.

### E2: Evidence rule for archive triage

Archive handling has three gates, not one:

1. **Investigation admission:** after the required retry, C4, explicit negative marker, non-success response, wrong-peer resolution, or unoccupied username may enter owner-visible triage. This says “the current catalog link is not positively verified,” not “the community is dead.”
2. **Disposition evidence:** authenticated resolution or an owner in-client check must choose among current target, replacement link/private invite, wrong peer/unoccupied name, or unresolved. A replacement proves life and routes to link repair. Wrong peer/unoccupied name proves a broken binding and requires a separate community-status check.
3. **Archive authorization:** archive only when owner evidence identifies the same historical community as deleted/closed. Record the evidence-derived reason and date. If community life is unknown, preserve an unresolved/blocking state; do not convert uncertainty into death.

This rule is stricter than “owner approves archive” because approval is authority, not evidence. It also respects frozen DoF 3: a broken or reassigned link alone does not prove community death.

**Extract decision E-D2:** C4 may enter investigation triage after retry, but it cannot become an archive decision without independent identity and death evidence.

### E3: Frozen DoD 22 is conditionally achievable for `mobile_developers_kz`, not presently discharged

Current evidence places the entry in X7:

- plain and `/s/` surfaces expose only C4;
- the same response class appears for fresh valid-form probes;
- repository history proves an old community existed but gives no current peer binding;
- no authenticated Telegram result or owner client observation has been captured.

Therefore an honest new `last_verified` date cannot currently be written for this entry. One bounded owner-authenticated resolution can move it to a contract-relevant case:

| Resolution result | DoD 22 path |
|-------------------|-------------|
| Intended supergroup/channel peer | X2: capture evidence and refresh date; DoD 22 remains achievable for the entry |
| Valid replacement username/invite for the same living community | X5: repair the stored link, validate the repaired entry, then refresh; do not archive |
| Wrong peer or unoccupied username plus owner evidence the historical community died | X6: archive under the frozen death rule; it no longer remains an unresolved live entry |
| Wrong peer/unoccupied username but historical community status unknown | X7: no truthful date and no contract-compliant archive; DoD 22 remains blocked for the task |

There is also a frozen-text tension that the Coordinator must not hide. DoD 12 says `--update` refreshes every entry “that responds,” including the four no-count entries; C4 technically returns HTTP 200. Dating C4 literally satisfies that phrase and helps DoD 22 pass, but violates the evidence boundary and risks DoF 4's prohibition on inferred verification dates. Pending A5 was filed to classify C4 as ambiguous and prevent that date write, but its verdict is still `PROPOSED — awaiting owner verdict`. This research does not apply it.

**Extract decision E-D3:** before a Phase C TS can safely bind behavior, the Coordinator needs (a) the explicit owner verdict on A5 and (b) an owner-authenticated resolution of `mobile_developers_kz` or a TS evidence gate that blocks Phase D until that observation exists.

### E4: No duplicate §5 proposal is justified yet

Iteration 2 found an independent sufficient signal—`contacts.resolveUsername`/equivalent authenticated client resolution—so the control file's condition for a separate §5 proposal (“if no independent signal is sufficient”) is not met. A new proposal duplicating A5 would obscure the append-only contract record. The correct output is:

- preserve A5 exactly as pending;
- recommend the authenticated-resolution dependency in free §8/§9/§10;
- let the Coordinator seek the owner verdict and capture the CL observation;
- file a separate §5 proposal only if authenticated resolution cannot be obtained or leaves the historical community status unresolved and the owner wants the task to proceed anyway.

**Extract decision E-D4:** no new amendment proposal in iteration 2; A5 remains unresolved and is neither endorsed as approved nor applied.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Deterministic rules now separate target verification, link repair, investigation triage, and archive authorization. | The actual resolved peer/status of `mobile_developers_kz` requires owner-authenticated Telegram evidence. |
| DoD 22 has a finite decision path for every resolution result; current C4 alone cannot discharge it. | Challenge must test false positives/negatives and whether the rule conflicts with frozen DoD 12, DoF 3, or DoF 4. |
| A sufficient independent identity method exists, so no second §5 proposal is warranted at research time. | A5's explicit owner verdict remains outside Researcher authority and is a Coordinator gate. |

**Sufficiency:**
- [x] External source used? Official Telegram method/type pages for username and invite resolution.
- [x] Briefing gap closed? Both evidence rules and the `mobile_developers_kz` DoD 22 path are explicit.
- [x] Structured comparison built from Gather options? Yes; seven cases cover positive, negative, repaired, dead, and unresolved outcomes.

Stage complete: YES
→ User decision: close Extract; proceed to adversarial Challenge without assuming an A5 verdict.

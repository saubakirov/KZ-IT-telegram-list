# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. Every configuration is attacked against the frozen result, historical classifier failure, official Telegram link taxonomy, exact authorization, adapter loading, and holdout leakage.
> **Test:** The surviving configurations state their conditions; no row survives merely because its happy path works.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Consistency Check

### Pairwise coverage

All 28 dimension pairs were checked. “Conditional” means at least one alternative pair survives only with the stated boundary; the exact incompatible pairs follow.

| Pair | Result | Stress condition |
|---|---|---|
| D1 × D2 | Conditional | Requested/canonical identity must bind before any observed type is trusted; a second classifier cannot satisfy frozen reuse. |
| D1 × D3 | Compatible | Source parsing can remain offline and independent of the network-classifier location. |
| D1 × D4 | Compatible | Occurrence/candidate accounting must precede and wrap, not be inferred from, classifier calls. |
| D1 × D5 | Conditional | No candidate observation path may inherit `--update`/archive mutation; apply consumes reviewed evidence, not classifier side effects. |
| D1 × D6 | Compatible | Shared deterministic code and copied complete agent instructions solve different duplication problems. |
| D1 × D7 | Conditional | Target facts may feed editorial evidence; they cannot become a positive editorial verdict. |
| D1 × D8 | Conditional | Permanent classifier tests use synthetic HTML; live holdout outcomes cannot become fixtures. |
| D2 × D3 | Conditional | The frozen `<source>` does not carry type, so declared-type configurations need an explicit later prompt/field rather than silently guessing. |
| D2 × D4 | Compatible | Type can remain unresolved while every occurrence and normalized candidate stays accounted. |
| D2 × D5 | Conditional | An unresolved or conflicting type cannot appear in the approved add set. |
| D2 × D6 | Compatible | Both agent copies can express the same type-resolution contract. |
| D2 × D7 | Conditional | Owner-declared type is not evidence of observed type; the two fields cannot be collapsed. |
| D2 × D8 | Conditional | Holdout expected types may not be encoded in fixtures before the clean run. |
| D3 × D4 | Conditional | Multi-link lines require span/occurrence records; `@file` line expansion and line-only outcomes lose information. |
| D3 × D5 | Conditional | Approval binds decoded source bytes and normalized occurrences; a path string alone is not the reviewed input. |
| D3 × D6 | Compatible | The same `<source>` text can reach both complete command copies, but argument receipt needs runtime evidence. |
| D3 × D7 | Compatible | Grammar reports candidates; editorial authority is downstream. |
| D3 × D8 | Conditional | Holdout raw inputs must not be parsed during calibration merely to prove the grammar. |
| D4 × D5 | Conditional | Approval over unique rows alone is insufficient unless the payload also accounts for every source occurrence. |
| D4 × D6 | Compatible | Copy parity can assert the same occurrence/candidate totals and no-loss stop. |
| D4 × D7 | Compatible | One candidate disposition can map back to several occurrence dispositions. |
| D4 × D8 | Conditional | The `aws_kz` overlap must be allocated once at candidate level while both source occurrences remain visible. |
| D5 × D6 | Conditional | Byte-identical command copies do not make a boolean/conversational approval exact; both runtimes need the same payload/envelope check. |
| D5 × D7 | Conditional | Owner approval must identify exact proposed localized rows, not only handles or agent recommendations. |
| D5 × D8 | Conditional | Calibration approval cannot be replayed for holdout/final candidates; each payload is unique. |
| D6 × D7 | Compatible | Complete copies may contain the full authority split without duplicating project scripts. |
| D6 × D8 | Conditional | Adapter smoke tests use synthetic inputs; opening real holdout content to test an adapter is leakage. |
| D7 × D8 | Conditional | Preliminary editorial notes may define neither holdout rules nor expected holdout dispositions. |

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 | D — second intake classifier | D2 | B — reconcile all requested types | C11 proves a different classifier, not frozen reuse of the reviewed conflict-safe classifier; equivalence output cannot recover shared mutation-safety history. |
| D3 | C — repeatable URL/file/stdin | D4 | C — per-source-line result | C7 loses distinct outcomes when one line contains multiple Telegram URLs. |
| D3 | D — generic `@file` | D4 | C — per-source-line result | C9 treats Markdown lines as arguments and cannot preserve token spans, multiple links, or malformed Telegram-like occurrences. |
| D3 | B/C — file or mixed-source grammar | D4 | D — reject whole source on duplicate | The mandated combined source contains the known `aws_kz` overlap; C8 would reject the required production run instead of deduplicating and accounting for it. |
| D5 | A — conversational “yes” without content binding | D7 | D — independent review + owner | C12 cannot prove which immutable rows/baseline survived the handoff from reviewer to owner to apply. |
| D5 | B — boolean approval flag | D7 | C — evidence only, owner decides | C13 records that someone asserted approval, not the owner, exact candidate IDs, evidence digest, or proposed row bytes. |
| D6 | D — independently authored copies | D5 | C — manifest digest + IDs | C6/C11 can hash evidence yet lack the frozen reproducible source/copy mechanism; semantic similarity is not a declared format-only transformation. |
| D8 | D — present corpus only for calibration, future batch as holdout | D7 | D — independent review + owner | C10's future batch may add generalization evidence but does not satisfy the frozen clean run on a sealed subset of the current 28. |

### Absolute disqualifiers found

- D4 Alt A (unique handles only) cannot satisfy GD2 or the frozen 29-occurrence/28-candidate no-loss result by itself.
- D7 Alt A (automated decision for every gate) has no authoritative source for positive IT/Kazakhstan/commerciality/copy-quality judgments.
- D8 Alt A (random split after implementation) permits candidate-aware rules and fixture selection before allocation, violating the no-tuning holdout boundary.
- D5 Alt C is valid only as ED1's two-layer model: hash an immutable preview payload first, then record approval referencing that digest. A self-hashing object is not a survivor.

### Surviving configurations

| Config | D1 | D2 | D3/D4 | D5 | D6 | D7/D8 | Conditions of survival |
|--------|----|----|-------|----|----|-------|------------------------|
| C1 — extended typed CLI | A | A | B/B | C | B | C/B | Candidate mode is non-mutating and mutually exclusive with update/archive; declared and observed type remain distinct; Alt C uses payload + approval envelope. |
| C2 — exact-copy orchestrator | B | C | B/B | C | A | B/B | Source parser is occurrence-aware; observed type is trusted only after identity binding; complete runtime bodies are byte-identical; approval references the immutable payload. |
| C3 — approval envelope | B | D | C/B | D | A | D/B | Unresolved type blocks eligibility but not accounting; separate approval binds payload digest and exact IDs; independent review remains advisory to owner. |
| C4 — shared observation module | C | C | C/B | C | B | B/B | Refactor reproduces all historical identity/type/update/archive tests; no live holdout result is added to permanent fixtures. |
| C5 — multi-type shared module | C | B | B/B | D | C | D/B | All requested-type interpretations use the same target-bound HTML and cannot turn an identity conflict into success; source-to-copy direction is enforced. |
| C14 — source-isolated proof | C | D | B/B | D | C | B/C | “Source-based” means procedural no-tuning, not blind outcomes; `aws_kz` is assigned to one candidate partition and both occurrences remain recorded; the resulting five/23-ish split is acknowledged as weaker isolation. |

### Unexpected survivors

- **C2 — exact-copy orchestrator:** it survived the frozen-path attack because Claude command files accept the common skill front matter and ignore `name`, while Codex requires it. The same complete bytes can therefore serve both runtime locations without a format adapter.
- **C1 — extended typed CLI:** extending `validate_links.py` is not inherently unsafe if candidate observation is a mutually exclusive, non-mutating path and never reuses `enrich_result`/`apply_updates`; the threat is boundary mixing, not file location.
- **C14 — source-isolated proof:** it survives only under GD3's procedural definition and explicit overlap assignment. It is not evidence that the source or outcomes were globally unseen.

## Findings

### C1: “Telegram link” is a taxonomy, not a single handle regex

Telegram's official [deep-link documentation](https://core.telegram.org/api/links) distinguishes public username links, bot-start links, private invite links, phone-number links, public/private message links, chat-folder links, share links, and many reserved service paths. It also recognizes `t.me`, `telegram.me`, `telegram.dog`, `tg:` URIs, and `<username>.t.me`. The catalog, however, needs a stable public bare username for a group, channel, or bot.

The parser must therefore classify before normalizing. These attacks are materially different:

| Input example | Why naïve first-path extraction fails | Safe research disposition |
|---|---|---|
| `https://t.me/example` | Baseline public username form | Candidate handle may be normalized, then target-bound probe decides identity/type. |
| `http://telegram.me/example` or `https://example.t.me/` | Official aliases, not malformed merely because current helper is narrower | Either supported and canonicalized with explicit tests, or explicitly unsupported; never silently lost. |
| `tg://resolve?domain=example` | Username is in query, not path | Parse only the documented `resolve/domain` form; other `tg:` actions are not candidates. |
| `https://t.me/example/123` | Official public message link; first path is a dialog username but the URL names a message | Policy must explicitly accept the parent public dialog or retain `unsupported_message_link`; stripping the suffix silently is not acceptable. |
| `https://t.me/+inviteHash` / `t.me/joinchat/...` | Private invite identifies a revocable invite, not a durable public handle | Record occurrence as unsupported/unresolved; do not turn invite hash into a catalog handle. |
| `https://t.me/+7701...` | Official phone-number link shares the `+` prefix shape | Record non-candidate; never probe it as a username. |
| `https://t.me/share?url=...` / `t.me/addlist/...` | Reserved Telegram actions; first path token looks syntactically like a word | Record reserved/non-candidate rather than probing `share` or `addlist`. |
| `https://t.me/bot?start=x` | Underlying public peer can be a bot, but query denotes an action | Preserve raw occurrence; normalize only the documented peer component and let observed type verify it. |
| `(https://t.me/example).` | Common Markdown/prose punctuation | Span extraction must separate balanced punctuation without losing raw location. |

The current `handle_from_url` intentionally has a narrower purpose inside target-identity classification and currently returns the first path component for `t.me` forms. Broadening it to become the intake grammar would risk changing reviewed classifier semantics and can misread reserved/private links. A separate occurrence parser can support or reject the wider official taxonomy, normalize accepted public peer forms, and then probe `https://t.me/<handle>` through the unchanged classifier. This narrows implementation detail without changing the frozen promise: every Telegram-like occurrence gets an explicit result; not every Telegram deep link is eligible for catalog admission.

### C2: Identity conflict must dominate observed type and all downstream facts

Attack: requested `@candidate` resolves to a preview whose canonical or primary-action identity is `@other`, while the page says “10,000 subscribers.” An observed-first design could incorrectly conclude `channels`, retain the count, and ask only an editorial question. The historical classifier regression shows why that is unsafe.

For every surviving D2 alternative, target binding is the first gate:

1. parse authoritative canonical/OG/primary-action identity signals;
2. fail closed on conflicting identities or a canonical identity different from the requested handle;
3. only for a target-bound observation expose type, visible name, and count;
4. compare declared/proposed type with observed type; mismatch remains ineligible;
5. keep descriptive/contact links outside target identity.

D2 Alt C may derive an observed type from the same fetched bytes, but it cannot promote that field when identity is unbound. D2 Alt B may interpret those bytes against all expected types, but “one type verified” cannot override a canonical conflict. D2 Alt D preserves the candidate as unresolved without inventing a type. This attack eliminates the apparent convenience of type-first probing, not the surviving configurations themselves.

### C3: Partial failure needs complete dispositions, not whole-batch success theatre

Attack: 27 candidates produce evidence; one receives repeated HTTP 429/timeout. A command that emits only successful candidates silently changes the approval universe. A command that retries the full batch can duplicate network work and make previously observed facts appear fresher than they are. A whole-source rejection discards useful evidence and, with the known duplicate, may never reach probing.

The dual ledger allows a precise partial state:

- all 29 source occurrences have parse dispositions;
- all 28 unique candidates have candidate dispositions;
- successful observations retain their own timestamp and evidence binding;
- the failed candidate is `unresolved_live_observation`, never “dead” or rejected on topic;
- a retry creates a new observation/payload lineage for that candidate rather than mutating old evidence invisibly;
- owner may approve only the exact currently eligible subset; unresolved candidates remain accounted non-additions.

Attack: a process stops after editing `data/communities.json` but before generating all projections. This is after authorization but before a valid result. The implementation must make the apply boundary recoverable and idempotent: validate the exact proposal against a current catalog baseline, avoid per-row commits, regenerate from source, and report failure without claiming success. Challenge does not prescribe a filesystem transaction mechanism, but any later TS must prove that rerun cannot duplicate rows and that a failed apply is detected before an accepted result/commit.

### C4: Approval digest replay is a TOCTOU failure

OWASP's [Transaction Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html) is written for security transactions rather than catalog curation, but its relevant principles transfer directly: the user acknowledges significant transaction data (“what you see is what you sign”); changing that data invalidates authorization; a final control gate is tied to execution; and authorization is unique and time-bounded to prevent replay/TOCTOU.

Applied to catalog intake, the attacks are:

- owner approves handles A/B, then a locale description/category/count changes before apply;
- another task adds A or changes the category registry after preview;
- a previously approved payload is replayed against a later catalog baseline;
- approval says “all” while the human-visible table omitted or collapsed occurrences;
- candidate C becomes newly verified after approval and is appended without a new decision;
- an agent substitutes a different evidence file with the same display summary.

The surviving C/D approval alternatives bind at least: versioned canonical payload digest, current catalog baseline/digest, every occurrence outcome, exact candidate IDs, exact proposed localized rows/facts, observation timestamps, and explicit approved IDs. The approval envelope records the owner authority and current decision. Apply recomputes the payload/baseline and rechecks every eligibility gate; any changed significant field invalidates approval instead of “helpfully” updating it. The envelope may cite the owner conversation as authority, but a free-form “yes” or boolean alone is not the binding.

### C5: Byte parity can still produce three broken commands

Attacks against A1:

1. Claude and Codex files are byte-identical but both are thin pointers to another operation body.
2. `/kz-add` is synchronized while `/kz-stats` or `/kz-release` is missing or semantically weakened.
3. Claude invokes by filename `kz-add`, but Codex front matter declares a different `name`.
4. Both files exist, yet literal `/kz-add <source>` reaches the wrong behavior because Codex only documented `$skill` selection and project routing is absent.
5. The command loads but drops the trailing multi-link/file argument.
6. The fresh session has no authoring context, so an “obvious” approval hard stop present only in the author's memory disappears.
7. A copy update succeeds for one runtime path and parity check examines only content, not command inventory.
8. Exact copies preserve `/kz-stats` or `/kz-release` text but a shared helper change bypasses their owner triage/tag/push gates.

Survival requires four separate evidence layers: set inventory; standalone full-body structural contract; exact copy/hash (or only a declared generated format transformation); and independent fresh-runtime behavior. The smoke matrix must cover each of three commands in Claude and Codex, literal discovery/routing, argument receipt, preview/no-mutation, missing-approval stop, stats owner-triage preservation, and release pre-tag/pre-push stop. Synthetic inputs are sufficient for routing/authority checks; real holdout data is prohibited here. No runtime smoke may tag, push, or mutate production catalog state.

### C6: Alias, relevance, and commerciality resist a single automated disposition

Adversarial candidates include:

- requested handle redirects to a new handle with plausible continuity but no independent evidence;
- exact handle is new but names the same organization/community already cataloged under another handle;
- Kazakhstan organization publishes technology news but the Telegram surface is mainly product marketing;
- a broad global IT channel occasionally mentions Kazakhstan;
- a Kazakhstani business/startup channel is not materially IT-focused;
- an AI course/channel is useful but purely commercial;
- public preview is too sparse to establish topic or locale-copy truth.

Exact live/archive collision is mechanical. Cross-handle alias/continuity, topic, Kazakhstan relevance, commerciality, and content quality need cited observations and owner judgment. Automation may issue structural `ineligible` outcomes (invalid public handle, unbound identity, wrong type, exact live/archive duplicate, incomplete proposed locales) and may propose evidence-backed editorial assessments. It must not transform absence of contrary evidence into a positive pass. A sparse/private target stays unresolved. This removes D7 Alt A and preserves B/C/D only with explicit claim types and owner approval.

### C7: The holdout can leak before the first network call

Attack: the implementation parses all 28 to build the split, then uses failing holdout URL shapes to improve the parser before declaring calibration complete. No live outcome was fetched, yet holdout inputs already tuned a frozen rule. Attack: permanent tests encode a known holdout handle, expected type, or known canonical conflict from preliminary notes. Attack: a parity smoke invokes `/kz-add` on the real holdout file. Attack: after the clean run exposes a miss, the rule is patched and the same evidence is still called clean.

The allocation therefore precedes implementation and uses a manually/research-established raw-candidate inventory, not the intake engine under test. It binds raw source digests, occurrence IDs/locators, normalized candidate IDs, overlap assignment, partition method, and no expected eligibility/type/disposition. Phase A can open only calibration raw occurrences for live evidence; synthetic fixtures cover grammar and branch behavior. Phase B first runs the exact reviewed engine on sealed holdout raw occurrences. Any rules, fixtures, or expected-output change prompted by that run invalidates the clean-run claim and starts a new evidence cycle before remaining candidates are processed.

C14 source isolation remains possible but weak: `aws_kz` must belong to one candidate partition, its second occurrence remains visible, and known planning notes prevent a blindness claim. D8 Alt B's stratification can improve branch diversity without using outcomes, but strata such as “identity conflict” must be based only on already disclosed planning facts or neutral input shape; secretly inspecting holdout previews to stratify is leakage.

### C8: Configuration outcomes

| Config | Verdict | Material reason |
|---|---|---|
| C1 | SURVIVES WITH CONDITIONS | Existing CLI location is acceptable only with strict non-mutating mode separation and exact typed evidence. |
| C2 | SURVIVES | Reuses classifier, preserves occurrence accounting, supports exact-copy A1, mixed editorial authority, and procedural holdout. |
| C3 | SURVIVES | Unresolved type and separate approval envelope are safe, though owner/reviewer workload is higher. |
| C4 | SURVIVES WITH CONDITIONS | Shared-module refactor must reproduce the entire historical classifier/mutation regression contract. |
| C5 | SURVIVES WITH CONDITIONS | Multi-type interpretation is safe only over one identity-bound observation and with no “one success beats conflict” rule. |
| C6 | ELIMINATED | Independently authored runtime bodies lack the frozen reproducible source/copy mechanism and declared format-only relationship. |
| C7 | ELIMINATED | Line-only evidence cannot account for multiple URL occurrences on one line. |
| C8 | ELIMINATED | Known input duplicate prevents the required run rather than producing an explicit duplicate disposition. |
| C9 | ELIMINATED | Generic argument-file/line semantics are not Markdown occurrence accounting. |
| C10 | ELIMINATED | Future-only holdout does not execute the frozen clean holdout from the current 28. |
| C11 | ELIMINATED | A second classifier contradicts required reuse and reopens the reviewed identity-decoy failure. |
| C12 | ELIMINATED | Conversation-only approval lacks durable content/baseline binding across review/apply/resume. |
| C13 | ELIMINATED | Boolean approval does not identify owner authority or exact approved payload/IDs. |
| C14 | SURVIVES WITH CONDITIONS | Source split is procedurally valid only with overlap assignment and no global-unseen claim; isolation is weaker. |

### C9: Amendment audit

No frozen amendment is required.

- The frozen one/many/file promise does not require every Telegram deep-link action to become an eligible public community. Explicit `unsupported`, `malformed`, or `unresolved` occurrence outcomes satisfy no-loss accounting while a documented public-peer subset feeds candidate probing.
- The frozen Claude-command/Codex-skill paths accept exact complete copies using their common front matter; A1 can be implemented without changing paths or allowing thin links.
- The frozen holdout wording requires no tuning of rules/fixtures/expected outcomes before a clean run; GD3's procedural interpretation is exactly that boundary and does not claim historical identities were unknowable.
- Payload/envelope separation refines the approved exact-set boundary; it neither weakens nor expands owner authority.

## Challenge Decisions

1. **CD1 — Eliminate C6–C13; retain C1–C5 and C14 with explicit conditions.** Each elimination is tied to frozen reuse, no-loss, exact approval, reproducible-copy, or current-corpus holdout evidence rather than taste.
2. **CD2 — Carry C2 and C3 as distinct unexpected survivors into synthesis.** C2 demonstrates the smallest exact-copy orchestration family; C3 demonstrates the conservative unresolved-type/separate-approval family. C1/C4/C5/C14 remain viable comparison alternatives, not hidden defaults.
3. **CD3 — Treat only public-peer link forms as normalization candidates and every other Telegram-like form as an explicit occurrence disposition.** This prevents reserved/invite/message syntax from being silently misread while leaving the precise accepted subset to downstream specification.
4. **CD4 — Require approval to be WYSIWYS over immutable payload bytes and revalidated at execution.** ED1's payload/envelope split is now a consistency condition for every survivor, not an optional logging improvement.
5. **CD5 — Reject any “clean holdout” claim if holdout inputs tune parser rules, fixtures, command smoke, or expected outcomes before Phase B.** An invalidated run may be repeated only as a new evidence cycle, never relabeled clean retroactively.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Six configurations survive: C1–C5 and C14; C6–C13 except C14 fail exact frozen constraints or known input shape. | Synthesis must compare survivor cost/assurance and recommend a bounded family without writing TS. |
| Official Telegram taxonomy proves naïve first-path parsing is unsafe; stable public-peer candidates and unsupported Telegram actions need separate dispositions. | Downstream specification must enumerate the accepted public-peer grammar and synthetic branch matrix. |
| Identity binding dominates type/count/name; partial network failure remains unresolved and does not shrink the approval universe invisibly. | Synthesis must state the non-mutating probe and retry/evidence invariant. |
| Approval must bind significant data and current baseline, then be rechecked at execution to defeat replay/TOCTOU. | Synthesis must distinguish payload digest, owner envelope, and apply-time revalidation. |
| Exact bytes, full-body completeness, command inventory, literal discovery, argument receipt, and behavior are independent parity gates. | Downstream tests must prove all three commands in both fresh runtimes without live mutation/tag/push. |
| Holdout can leak through parsing, fixture design, or adapter smoke before live probing; allocation must precede implementation. | Synthesis must preserve the invalidation rule and procedural, not global-blind, claim. |
| Amendment audit found no frozen conflict. | Any later implementation discovery that changes a frozen path, authority boundary, or current-28 holdout would need a new explicit amendment proposal. |
| New discoveries: official Telegram link taxonomy expands the malformed/reserved threat model; holdout can leak through parser input before network access; exact approval benefits from a WYSIWYS/final-gate model. | No further Challenge loop is required for Iteration 1; synthesize after Coordinator authorization. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?
- [x] Hypothesis tested? (H2 identity/type/partial failure, H3 grammar/approval/idempotence, H4 pre-network leakage.)
- [x] Counter-evidence sought? (official non-peer Telegram links, identity decoy/conflict, 429/crash/replay, identical thin copies, ambiguous commercial/topic cases, and parser-level holdout leakage.)
- [x] Metacognitive check completed? (Holdout leakage before network access and the breadth of Telegram reserved link forms were new and changed survivor conditions.)

Stage complete: YES
→ User decision: Close Challenge; proceed to Iteration 1 synthesis after Coordinator authorization.

# Gather — "What do we NOT know?"
> **Mindset:** Explorer. This stage turns Iteration 1's surviving families into independently selectable contracts; it does not choose a final implementation.
> **Test:** The map must distinguish accepted peer identity from Telegram-shaped syntax, payload bytes from approval authority, authoring source from runtime copies, and a holdout commitment from holdout disclosure.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: accepted public-peer URL forms | Only root `https://t.me/<handle>` links | Root links on Telegram's documented HTTP aliases | HTTP aliases plus `<handle>.t.me` | HTTP forms plus `tg://resolve?domain=<handle>` |
| D2: child/action-link treatment | Reject every suffix or query beyond a root peer | Extract the public parent from documented message/story links and record the child form | Extract the public parent from bot-action queries only | Preserve every non-root form as unsupported/manual without parent extraction |
| D3: source decoding | One positional value: existing path if found, otherwise inline text | Explicit `--file` and `--text` modes behind one `/kz-add <source>` command | Inline text plus `--stdin` and explicit file mode | Typed source descriptor such as `file:<path>` / `text:<value>` |
| D4: occurrence extraction | URL-shaped span scanner with wrapper-aware punctuation trimming | Markdown parser plus plaintext fallback | Line-oriented tokenization with multiple-token expansion | Generic linkifier followed by Telegram-kind parser |
| D5: payload canonicalization | RFC 8785 JSON Canonicalization Scheme | Repository-defined restricted canonical JSON profile | Hash exact pretty-printed UTF-8 payload bytes | Canonical CBOR plus a separate JSON rendering |
| D6: approval-envelope representation | Separate JSON envelope referencing payload digest and exact action set | TFW approval record referencing payload digest plus a generated envelope | Detached signature over payload digest and action set | Append-only approval ledger with one record per payload |
| D7: freshness/replay binding | Exact raw `data/communities.json` SHA-256 | Git blob/tree identity | Baseline SHA-256 plus parser/observer contract version | Composite data, generator, schema, and command hashes |
| D8: complete-copy authoring direction | Claude command is authoring source; exact bytes copied to Codex skill | Codex skill is authoring source; exact bytes copied to Claude command | Neutral complete source rendered byte-identically to both runtime locations | Dual-edit runtime copies with an exact parity check |
| D9: fresh runtime proof | Static parse/hash/inventory only | Non-interactive CLI with tools disabled and synthetic sentinel | Fresh interactive/desktop task with a synthetic source | Disposable-worktree end-to-end smoke with synthetic fixtures |
| D10: observation boundary | Intake orchestrator imports and composes present validator seams | Intake mode/subcommand lives inside `validate_links.py` | Shared Telegram observation module serves stats and intake | Intake owns a second classifier with equivalence tests |
| D11: calibration/holdout allocation | Neutral manual stratification before implementation | Deterministic hash allocation performed by a non-Executor authority | Source-based allocation with overlap collapsed first | Seeded random allocation recorded before implementation |
| D12: holdout sealing | Hidden canonical manifest plus public digest/count commitment | Encrypted manifest plus digest, revealed only for the clean run | Dedicated worktree/task receives calibration only; Coordinator retains holdout | Procedural no-read rule over the present shared files plus post-run audit |
| D13: candidate-batch adoption | Adopt exact source bytes into task evidence after holdout opens | Adopt a canonical occurrence manifest that cites the source digest | Commit the preliminary note unchanged as a durable input | Keep only external-path/hash references and never adopt bytes |
| D14: apply rerun/partial-failure semantics | Any baseline drift stops, including an already-applied result | Recognize an exact already-applied post-state and emit a no-op receipt | Transaction-like staged validation before replacing catalog/projections | Per-candidate application with resumable receipts |

The alternatives are deliberately not marked as preferred. Some can be layered (for example, D6 approval representation is orthogonal to D10 observation boundary), while others become inconsistent only after Extract traces complete flows.

## Findings

### G1: Telegram's documented link space is much broader than the catalog's public-handle space

Telegram's official [Deep links](https://core.telegram.org/api/links) documentation distinguishes link kinds rather than treating every first path segment as a username. Public username links use `t.me/<username>` or `tg://resolve?domain=<username>`. The same documentation assigns different semantics to phone-number links (`t.me/+<phone_number>`), private invite links (`t.me/+<hash>` and legacy `t.me/joinchat/<hash>`), public/private message links, share links, chat folders, stickers, proxies, stories, bot starts, and many other reserved actions. It also documents `telegram.me`, `telegram.dog`, configured prefixes, and qualified `<username>.t.me` links as aliases, and says fragments are ignored by Telegram clients.

The official [Invite links](https://core.telegram.org/api/invites) page adds two constraints that matter to intake: ordinary groups must migrate to supergroups before receiving public usernames, and private invitation is a distinct mechanism from public username resolution. A private invite may eventually resolve to a peer, but it does not itself satisfy this repository's required bare public `handle` field. Phone links target users, not a catalog-eligible group/channel/bot identity.

This yields a synthetic, loss-accountable taxonomy without reading the holdout:

| Synthetic input class | Example | Identity information available before network observation | Required occurrence-level outcome family |
|-----------------------|---------|----------------------------------------------------------|------------------------------------------|
| Root public peer | `https://t.me/SyntheticTeam` | Candidate handle is syntactically present | accepted peer form or invalid handle |
| Documented HTTP alias | `https://telegram.dog/SyntheticTeam` | Candidate handle is syntactically present | accepted alias or explicitly unsupported alias |
| Username subdomain | `https://SyntheticTeam.t.me/` | Candidate handle is syntactically present, subject to Telegram's reserved-name rules | accepted subdomain or explicitly unsupported alias |
| Public message child | `https://t.me/SyntheticTeam/42` | Parent public handle is present; target object is a message | parent-derived candidate or explicit child-link disposition |
| Bot action | `https://t.me/SyntheticBot?start=demo` | Parent public handle is present; query changes action semantics | parent-derived candidate or explicit action-link disposition |
| Private invite | `https://t.me/+AbCdEf123` | No public handle is present | private-invite/manual/unsupported; never `+AbCdEf123` as a handle |
| Phone link | `https://t.me/+77000000000` | No catalog peer handle; syntax overlaps invite prefix | phone/private-user/manual/unsupported; never a handle |
| Reserved action | `https://t.me/share?url=https%3A%2F%2Fexample.test` | `share` is an action path, not a peer | reserved/non-peer |
| `tg:` peer resolution | `tg://resolve?domain=SyntheticTeam` | Candidate handle is in a query field | accepted URI form or explicitly unsupported URI form |
| Malformed/spoofed | `https://t.me.example/SyntheticTeam` | No Telegram authority | malformed/non-Telegram; never normalized as a peer |
| Duplicate occurrence | Root peer appears twice in one source | Same candidate, two positions | two occurrence records, one candidate group |

The public-peer grammar must therefore be an allowlist. Host, scheme, port/user-info, path shape, query shape, percent decoding, Telegram reserved paths, fragment policy, handle syntax, and trailing wrapper punctuation are separate validation steps. A generic “first segment of anything Telegram-looking” rule cannot provide H3's malformed/non-peer accounting.

### G2: The current URL helper is an identity-evidence helper, not a safe intake grammar

`scripts/validate_links.py` currently accepts `tg:` `domain` values and the first non-empty path segment on `t.me`, `telegram.me`, and their `www` forms. It does not recognize `telegram.dog` or `<username>.t.me`. More importantly, it would return `+AbCdEf123`, `joinchat`, `share`, or the parent segment of a message link if those values reached it. That behavior is safe only in its present narrower context: `classify_response` applies it to Telegram preview URLs that the HTML parser already classified as authoritative identity evidence for a requested handle.

Using `handle_from_url` directly as the source parser would broaden its trust boundary and convert official non-peer forms into apparent handles. Conversely, rewriting it into the complete intake grammar risks changing the reviewed stats classifier. D1–D4 need a source-kind parser before normalization, followed by the existing identity/type observation seam after a candidate handle exists. This preserves Iteration 1 D1 rather than creating a second identity classifier.

The catalog's structural validator further narrows an accepted handle to `^[a-zA-Z][a-zA-Z0-9_]{4,31}$`. Input grammar can account for a syntactically Telegram-like occurrence that violates this pattern, but it cannot promote it. Case-insensitive candidate grouping must occur after recording the raw occurrence; otherwise different spellings and duplicate locations disappear.

### G3: One command can cover one URL, many URLs, and files only if source selection and occurrence extraction are independent

The runtime command receives trailing user text, while a Python intake entry point must decide whether that text names a path or is itself content. Heuristic “existing path else inline text” is compact but ambiguous: a mistyped intended path silently becomes a text source, and literal text equal to an existing filename becomes a file. Explicit modes remove that ambiguity but add syntax behind the public `/kz-add <source>` surface. Standard argument-file expansion remains insufficient for arbitrary Markdown because it interprets lines as arguments, not as a source document with multiple links and punctuation.

Occurrence extraction also cannot be equivalent to splitting on whitespace. Synthetic cases such as `[team](https://t.me/SyntheticTeam), https://t.me/SyntheticTeam.` and two URLs on one line require wrapper-aware spans. A Markdown parser can recover link destinations but may miss plain pasted URLs; a regex can recover both but must not consume terminal punctuation or accept spoofed authorities. Every extractor alternative therefore feeds the same kind parser and emits stable positions before deduplication.

A minimal occurrence identity can be derived from immutable source identity plus ordinal and byte/character span; it must not depend on the eventual candidate handle because malformed and unsupported occurrences also need IDs. Candidate identity can then be the case-folded normalized handle with a schema/version namespace. The previously recorded aggregate remains the only corpus fact used here: 29 occurrences group into 28 unique candidates because one known handle overlaps the two sources. No raw holdout occurrence was opened or enumerated in this stage.

### G4: Canonical payload identity and human-readable rendering are related but not identical contracts

[RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html) defines JSON Canonicalization Scheme (JCS) for repeatable hashing/signing: I-JSON input, deterministic primitive serialization, recursive property sorting, and preserved array order. This is stronger than “`sort_keys=True`” when arbitrary numbers or non-ASCII property names exist. Python's standard JSON pretty-printer is deterministic under a controlled schema, but it is not by itself a claim of full JCS compatibility.

The project can avoid most cross-runtime ambiguity if a preview schema admits only strings, booleans, null, and bounded integers; rejects duplicate object names and floating-point values; keeps object keys ASCII; preserves Unicode string code points without normalization; defines array ordering; and hashes canonical UTF-8 bytes. D5 remains open between adopting JCS and defining/testing a narrower repository profile. Hashing exact pretty bytes is also possible, but it treats whitespace-only rewriting as a new approval and makes rendering part of authority. Canonical CBOR adds a new stack and a separate human rendering whose equality would need proof.

The preview payload's significant field families are now bounded:

1. `schema_version` and observation/parser contract version.
2. Source snapshots: durable `source_id`, content SHA-256, byte length, and non-authoritative label; no machine-specific absolute path as the sole identity.
3. Catalog baseline identity.
4. Complete occurrence ledger: stable occurrence ID, source ID, ordinal/span, raw occurrence or a durable lossless reference, parsed kind, parse disposition, and candidate ID when one exists.
5. Candidate groups: normalized handle, occurrence IDs, exact live/archive collision result, observation result and timestamp, requested/canonical identity binding, observed type, and unresolved reasons.
6. Proposed catalog record/action: exact EN/RU/KK text, category where required, member count only when observed, verification date, and every inclusion criterion disposition with evidence or unresolved state.
7. Deterministic totals and explicit no-apply/eligibility state.
8. Optional lineage to a predecessor payload digest for a retry or revised proposal.

The payload must not contain its own digest or a run ID derived from that digest. Paths, presentation-only table layout, conversation prose, and the later approval must not be silently mixed into the canonical significant-data projection. A human preview is a rendering of this payload; the envelope binds the payload digest, so a visually identical table with different hidden fields still changes authority.

### G5: A separate approval envelope needs evidence of authority, not merely an `owner` string

OWASP's [Transaction Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html) treats authorization as binding the user to significant transaction data, requires changed data to invalidate authorization, and places a final control gate immediately before execution. Although this repository uses conversational owner authority rather than a banking signature, the same failure modes apply: a boolean flag or an agent-written `owner: yes` field does not show what the owner reviewed.

A physically separate envelope can stay small because the payload already contains facts and proposed rows. Its independently checkable field families are:

- envelope schema/version and unique approval record ID or nonce;
- exact preview payload SHA-256 and canonicalization profile/version;
- exact approved action set (candidate IDs plus add/skip/unresolved action, or an exact selected-ID set whose semantics are versioned);
- owner identity as declared by the project plus a durable TFW conversation/journal evidence reference;
- approval timestamp and optional expiry policy;
- baseline identity repeated or mechanically asserted equal to the payload baseline;
- no agent-generated substitution for absent owner assent.

Cryptographic signing is one D6 alternative, but a self-generated signature or digest would still not create owner authority. Under the project's actual chat loop, the meaningful proof is an immutable digest shown to the owner, an unambiguous current response about that digest/action set, and a trace reference that a reviewer can inspect. The command can prepare an envelope candidate; only the authority event can complete it.

Retry and correction cannot mutate an approved payload in place. A new observation, description, category, action, or source snapshot creates a new payload digest with explicit `supersedes_payload_sha256`; previous approval does not transfer. This rule also handles partial live failures: successful and unresolved candidate observations remain in one immutable preview, and a retry creates a new whole preview rather than splicing new bytes under an old approval.

### G6: Apply needs three identities—preview, approval, and receipt—and an explicit stale/no-op policy

The exact raw bytes of `data/communities.json` are a portable baseline: they include current live/archive entries, categories, locale text, intents, and all other source-of-truth state. Binding that SHA-256 is intentionally stricter than a semantic subset; a formatting-only rewrite would invalidate approval under D7 Alt A. A Git blob/tree identity can bind repository state but couples the operation to Git and may include unrelated paths. Contract and script hashes can detect implementation drift but expand the owner-visible significant-data set. Extract must compare that proof cost rather than assuming more hashes are always safer.

At apply time, the operation can independently require: canonical payload digest match; envelope digest/authority/action-set match; current baseline match; every proposed row still absent or collision-compatible; observations still satisfy the freshness policy; schema validation; README generation/currency; and exact final diff limited to approved rows and generated projections. An apply receipt should be a third immutable artifact containing preview/envelope digests, before/after data and projection hashes, exact applied IDs, validation results, timestamp, and any no-op or rollback state. Mutating the approval envelope into a receipt destroys the original authority evidence.

Idempotency is still a separate D14 choice. A strict baseline check safely stops a rerun after success, but it reports drift rather than recognizing completion. Detecting an exact already-applied post-state can emit a no-op receipt, but only if every approved row and generated byte matches the first receipt; “handle exists” is insufficient. Per-candidate resume reduces repeated work after failure but permits a partially mutated catalog and complicates owner authority. Staging a complete proposed data/projection set before replacement contains failure but still needs a filesystem-specific commit/rollback design. These flows must be traced in Extract.

### G7: Exact Claude/Codex copies are format-feasible; the current project has no `kz-*` Codex copies

The two current Claude bodies are already substantial, self-contained operation contracts rather than one-line routers:

| Command source | Bytes | SHA-256 | Current front matter |
|----------------|------:|---------|----------------------|
| `.claude/commands/kz-stats.md` | 5,974 | `b124678abdf441a0b124602bd61e90fe5c0863ecd2375343cf30de6864d5b5ac` | `description` only |
| `.claude/commands/kz-release.md` | 4,404 | `3b680575764e46923fd9d9ca53d338d1def9fca167d791788618118c3cf95fc5` | `description` only |

No `.agents/skills/kz-*` directory exists, and `AGENTS.md` truthfully says `/kz-stats` and `/kz-release` are not invocable until their adapters ship. A1 therefore requires an inventory transition for all three names, not just the new command.

Official Anthropic documentation says `.claude/commands/<name>.md` and `.claude/skills/<name>/SKILL.md` both create `/<name>`; command files support the same front matter but ignore `name` and `paths`. It also specifies that `$ARGUMENTS` receives the trailing command text, with trailing input appended when no placeholder consumes it, and recommends `disable-model-invocation: true` for user-controlled side-effect workflows ([Claude Code skills/commands](https://code.claude.com/docs/en/slash-commands)). Thus a shared file may include `name` for Codex without changing Claude's filename-based command name, and `/kz-add` can explicitly consume the complete source string.

Official OpenAI documentation requires repository skills at `.agents/skills/<name>/SKILL.md` to have `name` and `description`; Codex initially sees skill metadata and loads the full `SKILL.md` when selected. The documented explicit Codex surfaces are `/skills` or `$skill-name`, with implicit selection by description ([OpenAI, Build skills](https://learn.chatgpt.com/docs/build-skills)). Literal `/kz-*` remains a project compatibility contract supplied by `AGENTS.md` and must be tested in the actual runtime; the official page does not itself promise arbitrary literal slash aliases.

These loader rules make byte identity feasible with common front matter containing at least `name` and `description`. They do not select D8. Claude-as-source preserves the existing authored bodies; Codex-as-source aligns authoring with the stricter mandatory metadata; a neutral source makes generated status symmetric; dual-edit avoids a third copy but relies entirely on checks. In every case, both runtime files must contain the complete operation body. A generator invocation or pointer to the other runtime file would violate A1 even if parity tests passed.

### G8: Comparable adapters prove two incomplete halves of A1, not the full contract

The repository's `.tfw/adapters/codex/README.md` implements a canonical-source-to-installed-copy model for TFW skills and checks that installed `SKILL.md` files are byte-identical to adapter sources. That is useful parity evidence, but those TFW skills intentionally load separate canonical workflows, so the pattern cannot be copied literally under A1's “no thin runtime links” constraint.

Two local comparable projects show the same split:

- `D:/projects/research/ai-first-devices` has Claude and Codex `/deploy` surfaces, but the Claude file (1,677 bytes, SHA-256 `0ec2b8…`) and Codex skill (1,253 bytes, `da1731…`) are not byte-identical, and both explicitly route to a runbook rather than holding complete deploy logic.
- `D:/projects/research/local-network` contains a complete migrated TFW plan body in a Codex skill (8,601 bytes, `777fe0…`), demonstrating that a large full body is loadable, but it wraps a different 8,437-byte Claude source (`367517…`) and has no exact synchronized-copy gate.

The first pattern supplies reproducible installation without complete bodies; the second supplies a complete body without exact runtime parity. Neither is a ready precedent for A1. The eventual parity gate must therefore prove exact inventory, common front matter validity, byte identity per name, standalone body completeness, and runtime behavior as separate assertions.

### G9: A safe Claude fresh-session harness is available; an equivalent local Codex CLI harness is not yet available

The local Claude CLI is `2.1.109`. Its observed help and official [CLI reference](https://code.claude.com/docs/en/cli-reference) expose print mode, `--no-session-persistence`, structured output, setting-source selection, plan permission mode, and `--tools ""` to disable built-in tools. Combined with a synthetic sentinel source, these surfaces can test fresh discovery, argument receipt, preview-only behavior, and stats/release hard-stop recognition without permitting repository or network mutation. Project commands require the `project` setting source; `--safe-mode` would intentionally hide them and is therefore not a valid discovery probe.

The Windows Codex app bundle is discoverable under `C:/Program Files/WindowsApps`, but direct `codex --version` and `codex --help` returned `Access is denied` in this shell. The running Codex Desktop app proves a product runtime exists, not that a fresh CLI smoke can be invoked from this Researcher shell. Static `.agents/skills` checks and the current already-contextualized session cannot be relabeled as fresh-session evidence. D9 therefore remains open between a fresh Desktop task, a repaired/available CLI, and later disposable-worktree execution evidence.

Fresh behavior also has more than one assertion:

1. command inventory/discovery in a new runtime;
2. literal `/kz-add <synthetic-sentinel>` routing, not only `$kz-add` selection;
3. complete argument receipt including spaces, multiple URLs, and a file form;
4. preview path performs no catalog mutation before exact approval;
5. `/kz-stats` preserves unresolved/owner-triage authority;
6. `/kz-release` stops before tag/push without current exact approval;
7. runtime output identifies the local complete copy it used, without following the other agent's file.

File presence, byte parity, and one successful prompt cannot substitute for this matrix.

### G10: C2, C3, and C4 occupy different axes; only C2 versus C4 is an observation-architecture choice

The present validator separates HTML parsing/type inference (`TelegramPreviewParser`, `observed_preview_type`), identity/type classification (`classify_response`), network retry (`check_link_with_retry`), persistence (`save_data`), live update, and archive operations. However, `check_link_with_retry` requires a declared `entry_type` and returns the typed classifier result; it does not expose a fetch-once, observed-type-first result to arbitrary intake candidates. The existing CLI's `--handle` also selects only entries already in the catalog.

This creates the following boundary map:

| Family | New/composed responsibility | Existing code touched | Regression burden | Failure containment |
|--------|-----------------------------|-----------------------|-------------------|---------------------|
| C2 orchestrator | source grammar, occurrence/candidate manifests, collisions/editorial proposal, approval/apply; imports present observation behavior | New intake surface plus either a small fetch/observe seam or an explicit type-establishment input | Intake tests plus unchanged validator classifier/regression suite; any new seam needs conflict/decoy proof | Stats mutation path remains separate; orchestration can fail before catalog write |
| C3 separate approval | payload/envelope schemas, authority capture, freshness, receipt | Layers on C2 or C4; does not decide how Telegram is observed | Canonicalization, tamper/replay/stale/subset/authority tests | Stronger authority separation, extra artifact lifecycle |
| C4 shared observation module | common fetch, parse, identity, type, retry results consumed by stats and intake | Extract functions from `validate_links.py`; update stats imports and add intake consumer | Full stats equivalence plus intake tests and module API compatibility | One behavior source, but regression can affect catalog-wide stats |

C2 is not literally “no validator changes” unless type is declared before probing or the orchestrator duplicates fetch/type observation. C4 avoids that pressure by exposing a shared observation result, but its proof surface includes every existing stats behavior. C3 can be combined with either and should be compared as an authority feature, not treated as a mutually exclusive classifier family. A second classifier remains visible in D10 only as counterfactual proof cost; Iteration 1 D1 rules it out unless a contradiction makes reuse impossible.

### G11: A clean current holdout is possible procedurally, but repository traces cannot prove a negative memory event

This Researcher did not open, parse, hash, enumerate, or probe the raw holdout candidates in Iteration 2. Only predecessor aggregates were used: 23 proposed candidates in the untracked discovery batch, six owner-supplied URLs, one known overlap, and 29 occurrences grouping to 28 candidates. The predecessor-recorded source digests remain the commitment inputs: `ffeb4b3903ae4a4eda2ee2676f31887552cc6b510ecedd65f8830e86fbef6ebb` for the candidate batch and `1fdc1286cb8c5ba1f04507c163a60b6b5171bc3c53123af1debb753b1d29a162` for the six-link note.

Scikit-learn's [data leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) requires the test split before preprocessing and model-choice steps, with the test data excluded from fitting. NIST's [agent-evaluation guidance](https://www.nist.gov/caisi/cheating-ai-agent-evaluations/4-practices-detecting-and-preventing-evaluation-cheating) likewise separates representative disclosed examples from held-out cases and treats leaked evaluation artifacts as a validity threat. Here, “fitting” includes parser rules, fixtures, command prompts, expected dispositions, category heuristics, and editorial wording—not just executable code.

A sealed protocol needs four roles/times:

1. Before Executor implementation, a non-Executor allocation authority resolves the known overlap once and produces a canonical 28-candidate partition manifest without running the proposed parser.
2. Only calibration identities/occurrences are disclosed to Phase A; the holdout manifest remains hidden, while its canonical digest, counts, allocation method/version, source digests, and overlap rule are committed.
3. Phase A uses synthetic grammar fixtures plus disclosed calibration only. Static/runtime command smokes use synthetic sentinels, never source or holdout URLs.
4. After rules, fixtures, copies, and expectations freeze, Phase B reveals the holdout manifest, verifies its digest/source coverage, runs once from a clean worktree/task, and records all outcomes. Any holdout-driven change invalidates that clean run and requires a newly independent evaluation set for the changed rules.

Because the present raw sources are accessible somewhere on the same workstation, a digest alone does not prove nobody read them. Stronger D12 variants reduce exposure: a dedicated Executor task/worktree contains only calibration material and is created without the raw source/path context; the Coordinator retains the canonical hidden manifest outside that worktree; the later holdout runner receives it only after freeze. Repository review can prove absence of raw URLs, fixtures, expected outcomes, and references in the implementation, but it cannot cryptographically prove absence from a person's or model's memory. The evaluation claim must be “precommitted no-tuning holdout under the recorded access protocol,” not globally unseen data.

Source-based allocation is also structurally suspect because the sources overlap and prior notes may already contain candidate-aware preliminary analysis. Manual stratification can balance known link/type/difficulty classes but risks candidate-aware selection; deterministic hashing is neutral only if performed by the allocation authority before disclosure and the rule/seed is precommitted. Extract must compare those leak and balance trade-offs without requesting raw inputs from this Researcher.

### G12: The untracked candidate batch is a valuable input snapshot, not yet durable provenance or catalog truth

The predecessor SHA-256 proves that exact bytes were observed at one point; it does not establish authorship, validation, or current byte equality. Filesystem timestamps are observations, not provenance. The file remains unrelated dirty work under the frozen contract until a later approved specification adopts it, and its preliminary statuses/descriptions cannot be promoted into catalog facts without the new validation workflow.

Durable adoption must preserve both source occurrence accounting and holdout isolation. Committing the raw batch before Phase A would disclose the holdout to every repository consumer. An exact post-reveal evidence copy preserves original context but may include non-candidate notes; a canonical occurrence manifest minimizes content but must retain source digest, stable locator/raw occurrence, and every malformed/duplicate/non-peer disposition. Keeping only the absolute path is not durable across machines. Any adoption flow must first rehash the current source and either match the predecessor digest or stop for explicit re-baselining; it must never overwrite, stage, or silently “clean up” the existing unrelated file.

Owner supply is a valid provenance statement (“the owner supplied this batch for intake”), while file authorship remains unknown unless separately evidenced. Final catalog adoption is per reviewed candidate, not wholesale: accepted rows enter `data/communities.json`; duplicates, rejected candidates, unsupported forms, and unresolved observations remain in the intake evidence so all 29 occurrences remain accounted for.

## Gather Constraints Carried Forward

1. **GC1 — Link kind precedes handle normalization.** Only an allowlisted public-peer form may produce a candidate handle; every Telegram-like non-peer/malformed occurrence receives an explicit stable disposition.
2. **GC2 — Source identity precedes occurrence identity, and occurrence identity precedes grouping.** The already-recorded `29 occurrences → 28 candidates` relation must be reproducible without deduplicating away source positions.
3. **GC3 — The canonical preview excludes its own digest and later approval.** Approval and apply receipt are separate immutable objects; every retry or proposal change produces a new payload and new approval requirement.
4. **GC4 — Authority evidence is not synthesized metadata.** A digest and `owner` field created by an agent do not replace an exact current owner response bound to the digest/action set.
5. **GC5 — A1 has four independent proof gates.** Inventory, byte-identical complete bodies, loader/front-matter validity, and fresh runtime behavior must all pass for `kz-add`, `kz-stats`, and `kz-release`.
6. **GC6 — C3 is orthogonal to C2/C4.** Extract must compare C2 and C4 observation boundaries while separately testing the C3 approval feature; it may not discard separate approval merely because C2 survives.
7. **GC7 — Holdout non-disclosure is a role/access protocol.** Phase A receives calibration plus synthetic fixtures only; literal/runtime smokes may not touch raw holdout sources. The clean claim is procedural no-tuning, not global blindness.
8. **GC8 — Candidate-batch adoption is post-snapshot and explicit.** A later phase must verify the known digest or re-baseline with owner authority; preliminary notes never become catalog facts by being copied.

These are consistency constraints derived from sources and predecessor decisions, not a selection among the dimension alternatives.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Official Telegram link taxonomy supports a bounded public-peer allowlist and explicit private/invite/message/action/non-peer dispositions; the current helper cannot be reused as the source grammar. | Cross D1–D4 into exact accepted/rejected synthetic flows, especially child-link parent extraction, aliases, punctuation, queries, and malformed authorities. |
| A minimal significant-data preview, separate approval envelope, and independent apply receipt can be named without self-reference. | Select D5–D7/D14 and trace stale baseline, retry, subset approval, same-visible-table/different-bytes, crash, and exact no-op rerun. |
| Claude command files can share Codex-required `name` metadata; current `kz-stats`/`kz-release` are complete bodies, but no `kz-*` Codex inventory exists. Comparable projects do not prove exact full-copy parity. | Select D8, define exact inventory/completeness/parity gates, and obtain fresh Claude plus Codex discovery/argument/hard-stop evidence without weakening A1. |
| Claude has a safe non-persistent, tools-disabled probe surface. Direct local Codex CLI execution is blocked by WindowsApps access, so fresh Codex behavior remains unproven. | Compare fresh Desktop-task, repaired CLI, and disposable-worktree proof paths; do not relabel static checks as runtime evidence. |
| C2 needs either declared type or a small observed-type seam; C4 extracts that seam but expands stats regression scope. C3 layers on either. | Trace C2+C3 and C4+C3 file/dependency/test surfaces and prove whether C4 buys enough risk reduction to justify extraction. |
| A sealed preimplementation allocation can use the recorded 28-candidate corpus without this Researcher seeing raw holdout; a repository digest cannot prove a negative memory event. | Select allocation/sealing mechanics, counts, reveal authority, invalidation rule, and clean-task boundary without exposing the raw holdout to Phase A. |
| The candidate note's recorded hash is a snapshot, not authorship or durable adoption. | Select post-reveal raw-copy versus occurrence-manifest adoption and exact drift/rebaseline behavior. |

**Sufficiency:**
- [x] External source used? (Telegram primary API documentation; Anthropic and OpenAI official runtime documentation; RFC 8785; OWASP; NIST; scikit-learn.)
- [x] Briefing gap closed? (Every Iteration 2 open thread now has an explicit configuration dimension and evidence boundary.)
- [x] Dimensions identified? (Fourteen independent or explicitly orthogonal factors, each with at least three alternatives.)
- [x] Hypothesis tested? (I2-H1–I2-H5 remain feasible with named constraints; no alternative is selected before Extract/Challenge.)
- [x] Counter-evidence sought? (Official non-peer Telegram forms, unsafe local helper broadening, non-JCS stdlib output, agent-written authority metadata, incomplete comparable adapters, Codex CLI access denial, and unprovable negative-memory claims.)
- [x] Metacognitive check completed? (New material discoveries: C3 is orthogonal rather than a peer architecture; C2 needs a type-establishment seam; byte-compatible front matter is feasible; clean holdout evidence is procedural, not cryptographic.)

Stage complete: YES
→ User decision: Close Gather; proceed to Extract after Coordinator authorization.

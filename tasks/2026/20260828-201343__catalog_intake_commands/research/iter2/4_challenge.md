# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. I2-C1 is not accepted because it is small; it survives only where malformed inputs, stale authority, runtime drift, and evaluation leakage fail to produce an unsafe state.
> **Test:** A different researcher must be able to reproduce every elimination, every conditional survivor, and every refinement without opening the raw holdout.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------|------------------|
| D1: accepted public-peer URL forms | A/B/C root-only grammar | D2: child/action-link treatment | B parent extraction | A message/story child becomes a candidate-producing form despite D1 saying only root forms are accepted. Parent extraction requires an explicitly broader D1 such as I2-C5, not a hidden exception. |
| D5: payload canonicalization | B restricted profile without lexical/schema rejection | D6: approval-envelope representation | Any digest-bound approval | Duplicate keys, floats, `-0`, non-ASCII keys, or unknown fields can parse/canonicalize differently or disappear from owner rendering; the envelope would bind ambiguous semantics. D5 B survives only with closed schema and lexical rejection. |
| D6: approval-envelope representation | A envelope with selectable subset | D14: apply semantics | Any precomputed expected post-state | Selecting a subset after payload hashing changes post bytes. A fixed action vector must be regenerated when the owner edits the set. |
| D7: freshness/replay binding | A data-only baseline | D14: apply semantics | B mixed generated-path no-op/recovery | A data hash cannot distinguish stale or manually changed README/locale projections from approved before/after states. No-op/recovery needs every controlled path's two hashes. |
| D8: complete-copy authoring direction | Any exact-byte direction with location-relative Markdown paths | A1 synchronized standalone copies | Frozen full-copy constraint | The same relative link resolves from the two runtime depths to different files. Current `../../AGENTS.md` resolves to root from Claude but to nonexistent `.agents/AGENTS.md` from Codex. |
| D9: fresh runtime proof | A static-only | A1 literal cross-agent command behavior | Frozen runtime constraint | File presence/hash cannot prove literal Codex `/kz-*` routing, argument receipt, or hard stops. Static-only proof is insufficient even if bytes match. |
| D10: observation boundary | D second classifier | Iteration 1 D1 / GC1 | Reuse reviewed classifier | A parallel classifier reopens the exact identity/type drift that the predecessor decision closed. Equivalence tests do not make two authorities one authority. |
| D11: allocation | B hash arbitrary opaque IDs assigned by allocator | D12: sealing | C claimed neutral holdout | The allocator can renumber opaque IDs until desired cases score into either partition. Allocation input must derive from frozen source occurrence bytes/positions, not discretionary labels. |
| D12: sealing | C hidden holdout | D13: adoption | C commit preliminary note before reveal | Committing the full preliminary note exposes the raw holdout to every Phase A worktree and invalidates the clean access claim. |
| D13: adoption | D external path/hash only | Durable provenance | Required resumability | An absolute path may disappear or change; a digest without retained/reconstructible bytes cannot later prove occurrence accounting. A sealed snapshot and post-reveal evidence adoption are required. |
| D14: apply semantics | Mixed B/A recovery without a pending execution marker | Concurrent/manual repository activity | Preserve unrelated owner work | A manually reverted path and a crash-partial path are byte-indistinguishable. Completing A without a payload/envelope-bound pending marker may overwrite an intentional revert. |
| D6: approval-envelope representation | C detached signature | Present owner workflow | No owner-controlled key/signing ceremony | An agent-generated signature proves no more authority than an agent-generated `owner` field. The configuration is incomplete until a real owner key lifecycle exists. |

### Surviving configurations

| Config | Grammar / parser | Canonicalization / authority | Observation | Copies / runtime | Holdout / provenance | Verdict after attack |
|--------|------------------|------------------------------|-------------|------------------|----------------------|----------------------|
| **I2-C1R — refined bounded C2+C3** | D1 B fixed root aliases only; D2 D; explicit text/file; raw span ledger with closed trimming/validation | Restricted canonical profile, fixed action payload, separate envelope, all controlled-path hashes; marker-bound mixed recovery | C2 fetch-once seam + unchanged three-type classifier | Location-neutral complete Claude source copied exactly; fresh Claude + Codex task gates | Content-derived 8 calibration / 20 holdout; calibration-only worktree; sealed exact sources later adopted as occurrence evidence | **Survives and is selected**, conditional only on implementation/runtime evidence. |
| I2-C2R — JCS/neutral-source variant | Same bounded grammar as I2-C1R | True RFC 8785 dependency/conformance; same envelope/state vector | Same C2 seam | Neutral third source copied to both; fresh gates | Same refined seal | Survives safety; adds dependency, conformance surface, and third-source lifecycle without a demonstrated current benefit. |
| I2-C3R — shared-observation variant | Same bounded grammar | Same restricted profile/envelope/state vector | C4 extracted shared module | Same exact copies/fresh gates | Same refined seal | Survives safety only with full `/kz-stats` equivalence; no present feasibility gap requires the refactor. |
| I2-C4R — strict single-host/manual-type | Only `https://t.me/<handle>`; explicit text/file | Restricted profile; composite baseline; drift always stops | C2 with owner/curator type input | Exact copies/fresh gates | Neutral allocation/seal | Survives fail-closed safety but shifts observable type work to the owner and rejects documented aliases; retained as conservative fallback, not selected. |
| I2-C5 — broad parent C4+C3 | Deep links/Markdown AST and parent extraction | JCS/separate envelope | Shared module | Neutral source/fresh gates | Encrypted seal | **Eliminated for this task:** child link no longer proves source intent to catalog the parent; grammar/dependency/observation changes are not needed for the owner-stated root-link/list/file workflow. |
| I2-C6 — signature-heavy | Bounded roots | JCS + owner signature + composite hashes | C2 | Neutral source/fresh gates | Encrypted seal | **Eliminated:** no owner key ceremony exists, and encryption/signing would add owner work without resolving a current threat that digest-bound TFW authority leaves open. |

### Unexpected survivors

- **I2-C4R:** it remains safe despite poor ergonomics because requiring type and rejecting every alias/child is fail-closed. It is useful as a fallback if same-bytes type reconciliation fails implementation tests.
- **I2-C2R:** RFC 8785 remains coherent even though the project can use a smaller subset; it is a standards-heavy fallback if the restricted-profile conformance proof becomes larger than expected.
- **I2-C3R:** shared extraction remains technically sound under an exact stats-equivalence gate, but its benefit is structural rather than required for H2.

## Findings

### C1: The first scanner design was under-specified; a closed root grammar lets a span scanner survive without becoming a Markdown parser

The attack set included inline links with titles, autolinks, reference definitions, raw HTML, code spans/fences, balanced and unbalanced parentheses, terminal Unicode/ASCII punctuation, two URLs on one line, URLs inside query values, user-info spoofing, ports, percent-encoded delimiters, control characters, backslashes, scheme-less `t.me`, and mixed case. CommonMark 0.31.2 treats inline destinations, autolinks, code spans, code blocks, escapes, and balanced parentheses through different rules ([CommonMark specification](https://spec.commonmark.org/0.31.2/)). Reimplementing “what renders as a Markdown link” would therefore defeat I2-C1's small parser claim.

The owner requirement is weaker and more direct: account for Telegram-like URL occurrences in supplied text or a file. The surviving scanner is intentionally raw-source, not CommonMark-semantic:

1. Scan left-to-right for absolute `http://`, `https://`, `tg:`, and scheme-less Telegram-domain starts, selecting one leftmost-longest token so an embedded URL inside `t.me/share?...` is not separately promoted.
2. Preserve original byte start/end and the complete raw token.
3. Apply a finite wrapper rule only to an angle wrapper or unmatched terminal `)`, `]`, `}`, `>`, followed by sentence punctuation. Preserve every removed byte in `trimmed_suffix`.
4. Parse components, then apply the closed candidate grammar; never salvage a valid prefix from an otherwise invalid token.
5. Record URLs in code spans/blocks and raw HTML too. Code formatting may be how a contributor quotes a candidate; owner preview decides intent. The extractor's contract is occurrence accounting, not rendered-link interpretation.

I2-C1's accepted grammar is narrowed from Gather D1 C to D1 B:

```text
https://{t.me|telegram.me|telegram.dog}/{HANDLE}
https://{t.me|telegram.me|telegram.dog}/{HANDLE}/
```

Scheme and host compare case-insensitively; the handle retains source spelling but candidate grouping is case-insensitive. `www` hosts, `<handle>.t.me`, `http`, `tg:`, query, fragment, user-info, port, percent-encoding, backslash, dot-segments, extra path segments, or any control character receive explicit non-candidate dispositions. Removing subdomain aliases avoids Telegram's changing reserved-subdomain exception table; removing fragments/queries makes “root peer” literal. The three documented fixed domains retain practical alias coverage without implementing dynamic `me_url_prefix` configuration.

Known Telegram action path names are checked before handle syntax, because words such as `share` may satisfy the repository regex. The live classifier remains a second safety gate if Telegram adds a reserved word unknown to the parser: a reserved landing/action page must still fail requested/canonical target binding, so the parser-version lag can waste a probe but cannot authorize an addition.

This is a free grammar refinement, not an HL amendment: malformed/unsupported forms are still accounted, and the owner can supply the root peer link for a candidate.

### C2: URL component parsing is not validation; the challenge adds pre- and post-parse rejection gates

Python's official [`urllib.parse` security notes](https://docs.python.org/3/library/urllib.parse.html#url-parsing-security) state that `urlsplit()`/`urlparse()` do not validate inputs and may accept values other applications reject. [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html) separates scheme, authority, path, query, and fragment; it also warns that components must be separated before percent decoding and recommends errors rather than ignoring scheme-specific violations.

The surviving parser therefore treats `urlsplit` only as a component splitter. It first rejects NUL/C0/DEL, whitespace within a token, backslash, invalid UTF-8, and malformed percent triplets. It then catches parser/hostname/port exceptions and requires:

- scheme exactly `https` after ASCII case-fold;
- no username/password/user-info and no port delimiter/value;
- hostname exactly one fixed domain after ASCII lowercasing, with no trailing dot or IDN lookalike;
- path bytes exactly `/` + repository handle + optional `/` and no percent sign;
- empty query and fragment;
- no extra path, dot segment, or decoded normalization step.

Synthetic attacks such as `https://t.me@evil.example/SyntheticAlpha`, `https://t.me.evil.example/SyntheticAlpha`, `https://t.me:443/SyntheticAlpha`, `https://t.me/%53yntheticAlpha`, `https://t.me/SyntheticAlpha%2f42`, and `https:\\t.me\SyntheticAlpha` all remain occurrences but never candidates. Because no candidate component is percent-decoded, double-decoding and delimiter confusion are absent.

The scanner still needs a conformance table covering every wrapper and rejection class. If implementation uses a single permissive regular expression as both extractor and validator, I2-C1R fails and the task must fall back to a parsed-token design; the research recommendation does not pre-approve that shortcut.

### C3: Three-type reconciliation is pure on the current classifier, but only one exact aggregation rule survives

`classify_response(html, handle, entry_type)` creates a new `TelegramPreviewParser`, reads no file/network/global mutable state, and returns a new result object. A local synthetic bound-group preview was passed to `groups`, `channels`, and `bots` twice. Both runs were equal; exactly one result was `verified` (`groups`, member count 1,234), and the two others were `ambiguous/declared_type_mismatch` with the same target-bound observed type. This directly supports I2-ED4 on present code.

The surviving aggregation rule is not “pick the best result”:

1. Fetch once; transport failure produces one candidate-level unresolved result and no typed calls claimed as live evidence.
2. Run all three declared types over identical immutable HTML bytes.
3. Require all three results to agree on target binding, visible identity, and any observed type fields expected to be type-independent.
4. Accept type only when exactly one result is `verified`, its `declared_type == observed_type`, and the other two are precisely target-bound type mismatches naming that same observed type.
5. Any zero/multiple verified results, identity/non-target disagreement, parser exception, or unexpected reason combination is unresolved and exposes no downstream name/count as approved fact.

An observed preview with conflicting indicators can be deterministically classified by the present `observed_preview_type` priority, but the intake must not pretend the three calls are independent votes. They are one classifier applied under three expectations. Historical decoy/conflict fixtures plus new invariant tests must prove same-HTML agreement.

The required network refactor is limited to a fetch/retry function that returns immutable HTML bytes or a stable transport outcome. Existing `/kz-stats` composition must reproduce its summary/output/retry behavior exactly. If extracting that seam cannot be done without changing classifier semantics, I2-C3R becomes the fallback; a second intake fetch/parser does not.

### C4: The restricted canonical profile survives only after closing lexical, schema, and rendering equivalence gaps

The original profile's semantic rules were insufficient against a stored JSON document containing duplicate keys or `-0`. Python normally keeps the last duplicate and parses `-0` as integer zero. RFC 8785's verified erratum specifically warns that negative zero serializes as `0`, so a parser should reject it to avoid pre-parse distinctions disappearing ([RFC 8785 errata](https://www.rfc-editor.org/errata/rfc8785)).

`kz-canonical-json/v1` survives with these mandatory gates:

- reject duplicate names at every object using pair-preserving parsing;
- reject lexical `-0`, every float/exponent token, NaN/Infinity, integer outside `[-9007199254740991, 9007199254740991]`, invalid UTF-8, lone surrogates, non-ASCII object keys, and unknown fields;
- distinguish booleans from integers in Python, where `bool` subclasses `int`;
- define and validate array order, uniqueness, reference integrity, and exact totals;
- forbid implicit Unicode normalization; code-point-distinct strings intentionally produce different digests;
- serialize only the validated in-memory object with `ensure_ascii=False`, sorted ASCII keys, compact separators, no BOM/newline;
- bind `canonicalization_profile` and implementation/test-vector version in the payload.

Closed schemas apply recursively (`additionalProperties: false` in schema terms). Otherwise an owner renderer could omit a hidden field even though the digest binds it. Renderer-completeness tests must map every significant field to either the human preview/diff or an explicitly labeled machine-only section; candidate action, localized text, collision, observation, sources/occurrences, controlled paths, and totals cannot be silently hidden.

The challenge did not find a domain value that requires generic ECMAScript float or UTF-16 non-ASCII-key ordering. I2-C1R therefore retains the restricted profile. I2-C2R remains a valid fallback if implementation starts admitting such values or cross-language consumers; at that point a reviewed RFC 8785 implementation is preferable to extending a home-grown profile piecemeal.

### C5: Payload/envelope attacks validate the fixed-action design and invalidate editable subset approval

Attacks changed one of: `description_kk`; occurrence disposition; normalized handle case; collision state; observation timestamp; parser version; source digest; catalog before hash; expected projection hash; action set; and array order. Every change must alter canonical payload bytes/digest. An old envelope then fails before mutation.

The owner may say “add A but not B” after seeing a preview. The system must not edit `approved_candidate_ids` in the envelope while reusing the payload. It creates a successor payload whose fixed action vector says `add A` and `no_change_owner_declined B`, recomputes expected controlled-path bytes, renders the new digest, and asks for exact approval again. This extra loop is the cost of independently checkable authority.

Partial live failure is not a whole-batch data loss: a payload may propose `add` for a verified candidate and `no_change_unresolved` for another, provided both occurrences/candidates and the unresolved reason remain visible. A later retry creates a successor payload on the then-current catalog baseline. Already applied A becomes an exact live duplicate/no-change; B's new observation receives new authority. No observation is spliced under the old digest.

Freshness is a final read-only gate. Immediately before an all-B mutation, every add candidate is re-observed through the same identity/type contract. Exact equality of authority-significant observation fields permits apply; any changed identity/type/count/date/eligibility fact produces a new preview. Transport failure blocks mutation rather than letting an old observation pass. The baseline and envelope alone do not make live evidence timeless.

### C6: Exact all-A no-op survives; mixed B/A recovery requires a durable pending marker

Four adversarial states were tested conceptually:

1. **All B, unrelated dirty tasks:** allowed to preflight because only controlled paths are authority-bound; unrelated owner work is neither staged nor overwritten.
2. **All A, receipt missing:** safe no-op. No catalog/projection byte is written. The operation may record that current bytes exactly equal the approved post-state, but it must not claim a fresh live verification unless one ran.
3. **Mixed B/A after process crash:** recoverable only with a durable pending execution record created before the first controlled-path replacement and bound to exact payload/envelope digests, execution ID, and B/A vector.
4. **Mixed B/A without that marker, or any X:** hard stop. Exact before-valued bytes may represent an intentional manual revert; approval of the old operation does not authorize guessing.

The pending record is written as task evidence, not by mutating the approval envelope. It has states `prepared`, `replacing`, `completed`, or `failed`; transitions append evidence or replace only the execution record under its own integrity rules. The complete A bytes are staged and validated before `prepared`. After each path replacement, a crash may leave the repository mixed, but the next invocation can verify the marker and write only exact remaining A bytes. If the marker itself is absent/corrupt, no recovery.

This refinement preserves strictness and idempotence while respecting multi-file non-atomicity. Per-candidate resume remains rejected: the owner approved one fixed batch state, not an order-dependent series of discretionary partial additions.

### C7: Exact-copy feasibility survived, but current relative links falsified “copy as-is today”

The current Claude commands contain `[AGENTS.md](../../AGENTS.md)` and similar references. From `.claude/commands/`, that resolves to repository root. From `.agents/skills/kz-stats/SKILL.md`, identical bytes resolve to `.agents/AGENTS.md`, which does not exist. Exact hashes would therefore certify two behaviorally different copies.

The complete source bodies must first become location-neutral:

- use literal repository-root-relative paths such as `AGENTS.md`, `RELEASE.md`, `data/communities.json`, and `scripts/validate_links.py`, not Markdown paths relative to the runtime file;
- contain the full authority, ordered operation, outputs, validation, and hard stops locally;
- never instruct either runtime to read the counterpart command or a separate workflow/runbook for missing logic;
- use the common Agent Skills front matter (`name`, `description`) and require `name` to match the Codex directory. The [Agent Skills specification](https://agentskills.io/specification) confirms those required fields and name/directory constraints.

Claude-only `disable-model-invocation` is not relied on for cross-runtime safety. Each complete body starts with a product-neutral hard gate: proceed only when the current owner message explicitly invokes that literal `/kz-*` command; implicit selection or adjacent planning context must stop and suggest the command. If implementation includes additional front matter, both loaders must accept it in fresh tests; exact bytes do not excuse an unsupported field.

Parity checks must also reject “identical thin” bodies by structural/semantic review. Required sections and forbidden counterpart references are useful mechanical gates, but the formal Reviewer still decides completeness. I2-C1R's Claude-source direction survives because it preserves the reviewed history after these location-neutral edits; it does not mean the present files can be copied without revision.

### C8: Fresh literal Codex routing remains an empirical release gate, not a research conclusion

OpenAI's official [Build skills](https://learn.chatgpt.com/docs/build-skills) page documents `.agents/skills`, metadata discovery, and `$skill`/`/skills`; it does not promise arbitrary literal slash aliases. `AGENTS.md` can instruct the agent to treat `/kz-add` literally and load the local skill, but only a fresh runtime result can establish behavior in this project.

The Challenge tightened observability:

- one clean disposable worktree/archive at the exact implementation SHA, containing no untracked source/holdout files;
- one genuinely fresh, non-forked session/task per product is sufficient to limit session proliferation, but each of the three command invocations must report the local runtime-copy path and SHA-256 it loaded;
- Claude runs nonpersistent/tools-disabled; Codex Desktop runs in plan/read-only mode because the bundled CLI is inaccessible in the current shell;
- `/kz-add` uses a synthetic reserved-action sentinel, proving literal route/argument receipt/no-network candidate/no mutation;
- `/kz-stats` and `/kz-release` use explicit routing-only prompts and must state their owner-triage and pre-tag/push hard stops without executing live/release work;
- before/after Git status and controlled-path hashes bind no mutation;
- `$kz-add` is a diagnostic fallback only. If literal `/kz-add` does not load/use the complete repository copy, A1 fails even when `$kz-add` works.

A model can echo a requested path without having loaded it. Static file hashes, task transcript showing skill selection/read, and behavior-specific output are therefore combined. If the Desktop surface cannot expose enough evidence, the gate remains blocked; it is not waived or replaced by the current contaminated research session.

### C9: Opaque-ID allocation was gameable; content-derived scoring and a larger holdout survive

I2-ED6's “opaque case ID then hash” allowed a malicious or biased allocator to rename cases until a desired split emerged. The survivor derives allocation material from the frozen sources:

```text
occurrence_key := SHA-256(source_sha256 || byte_start || byte_end || raw_span_sha256)
case_material  := canonical sorted occurrence_key list for one unique candidate
case_key       := SHA-256("kz-intake-case-v1\0" || case_material)
score          := SHA-256("kz-intake-split-v1\0" || case_key)
```

The non-Executor authority manually groups the already-known duplicate overlap before implementation, but cannot choose arbitrary labels or scores. All occurrences in one case remain in one partition. The hidden full manifest binds occurrence locators, grouping, keys, scores, and source digests; the public commitment exposes only whole-manifest digest, method version, totals, source digests, and overlap count, avoiding a list of case hashes that could reveal holdout membership by dictionary matching.

The 20-calibration/8-holdout split was also arbitrary and contrary to the owner's preference for a meaningful final clean run. Synthetic fixtures and the existing classifier regression corpus carry most grammar/type safety work, so the refined split is **8 calibration / 20 holdout**: the eight lowest deterministic scores are calibration and the remaining twenty stay sealed. This is not a statistical accuracy estimate; it maximizes untouched current cases while still providing real calibration.

Phase A receives only the eight calibration cases and synthetic fixtures. It may not receive full source paths, hidden case keys, preliminary outcomes, or a prompt/history fork containing them. The Executor uses a dedicated worktree and minimal `fork_turns: none`-style context; broad searches outside that worktree are prohibited. Repository review audits that no holdout URL/text/ID appears in code, fixtures, smokes, expected outputs, or evidence.

After Phase A freezes, a non-Executor reveal process recomputes the full manifest from the sealed source snapshot, verifies the original commitment and exact 8/20 split, then provides the twenty cases once to the clean Phase B runner. Any holdout-driven change invalidates the clean result. Calibration and holdout candidates can all still be processed for owner-approved catalog admission; only the evaluation claim differs.

### C10: Source drift is containable only if exact input bytes are sealed before Phase A, not merely hashed

The candidate backlog is untracked and the other note is outside the repository. If either changes after allocation, a hash proves mismatch but cannot reconstruct the promised 28-case corpus. Therefore the allocation authority must, before Phase A:

1. verify current bytes against the two predecessor digests;
2. copy the exact bytes into a Coordinator-controlled sealed location outside the Phase A worktree/context without editing the originals;
3. hash the sealed copies and build the partition commitment from them;
4. retain the sealed copies until reveal, or be able to reconstruct them only when the originals still hash identically;
5. after reveal, adopt exact source snapshots and the derived occurrence manifest into task evidence under the approved phase scope.

If the current bytes already differ at the initial gate, no allocation is made. The Coordinator reports drift and requires explicit owner re-baselining; it does not overwrite parallel work, use the old digest as if it contained bytes, or quietly expand the 28-case claim. If drift occurs only in originals after a matching sealed copy exists, the clean run stays bound to the sealed snapshot and the new bytes become a separate future input.

This makes D13 B durable: the occurrence manifest is operational evidence, while the exact raw snapshots establish what the owner supplied. Preliminary analyses inside the backlog remain source text, not accepted facts.

### C11: The twelve synthetic flows survive only with the refinements above

| Extract flow | Attack | Result |
|--------------|--------|--------|
| Multi-link text | Markdown title, autolink, code fence, duplicate, Unicode/terminal punctuation, two links on one line | Survives with raw leftmost-longest span ledger, lossless suffix, closed root grammar, and occurrence-before-grouping tests; no full Markdown semantics claim. |
| Unsupported Telegram action | Reserved word that also matches handle regex; nested candidate URL inside share query | Survives only with reserved-kind-before-handle and one outer occurrence; zero candidate/network for known action. Unknown future reserved path still blocked by identity classifier. |
| Identity conflict | Canonical/OG/action URLs disagree or bind another handle | Survives unchanged typed classifier; all three calls must agree on fail-closed target binding. |
| Type discovery | Type indicators disagree or no indicator exists | Exactly-one-verified aggregation survives; priority ambiguity/unexpected tuple is unresolved, never a vote. |
| Partial live failure | Owner wants successful A but B transport fails; later B retry | Fixed action payload can add A/no-change B; retry is successor on new baseline and needs new approval. |
| Changed hidden field | Unknown field omitted from human table; Unicode-normalization lookalike; `-0` | Survives only with closed schema, renderer-completeness, no normalization, lexical negative-zero/float rejection. |
| Stale catalog | Data matches but one generated projection changed, or unrelated task file dirty | Controlled-path X stops; unrelated non-controlled work is preserved and does not authorize broad cleanup. |
| Crash after replacements | Mixed B/A could be manual revert | Recovery survives only with durable matching pending marker; otherwise hard stop. |
| Exact rerun | All A but receipt missing/stale live evidence | Byte no-op survives; it reports exact approved post-state without fabricating a new current-live claim. |
| Copy drift | Bytes equal but relative references resolve differently; bytes differ by newline | Location-neutral paths plus exact hash/inventory and formal completeness review; any newline drift fails. |
| Fresh Codex literal route | Agent follows AGENTS fallback but does not load skill, or only `$kz-add` works | Requires path/hash/read evidence and behavior from literal prompt in fresh exact-SHA task; otherwise blocked. |
| Holdout access attempt | Executor inherited source path/history or allocator gamed opaque IDs | Content-derived scoring, minimal no-history task, calibration-only worktree, no broad search, and post-Phase-A reveal audit. |
| Source drift before reveal | Untracked original changed or disappeared | Exact sealed snapshot preserves committed corpus; absent snapshot/mismatched initial hash stops and re-baselines. |

### C12: Hypothesis outcomes and final selection after falsification

| Hypothesis | Challenge outcome | Basis |
|------------|-------------------|-------|
| I2-H1 bounded public-peer grammar | **Supported with refinements** | Root-only fixed domains plus explicit non-candidate taxonomy survives; subdomain/fragment/query/parent extraction were removed from the selected family. |
| I2-H2 canonical payload + separate envelope | **Supported with conditions** | Closed restricted schema, fixed action vector, renderer completeness, all-path before/after hashes, current authority evidence, and separate receipt are required. |
| I2-H3 one source direction + fresh evidence | **Supported with conditions** | Claude-source exact copies survive only after location-neutral paths/common front matter; fresh literal Codex behavior remains an empirical execution gate. |
| I2-H4 sealed allocation without holdout exposure | **Supported procedurally** | Content-derived deterministic 8/20 split, sealed exact sources, calibration-only Phase A, minimal context/worktree, and one-way reveal/invalidation. It is not a claim of global cryptographic unreadability. |
| I2-H5 C2 smaller than C4 | **Supported** | Same-bytes three-type classification is feasible/pure; C4 adds a stats-wide equivalence burden without closing a current correctness gap. |
| HL H2 classifier reuse | **Supported** | One fetch plus unchanged typed classifier; no second identity/type authority. |
| HL H3 one/many/file idempotent grammar | **Supported** | Explicit text/file sources, occurrence ledger, fixed action payload, strict stale stop, exact all-A no-op, marker-bound recovery. |
| HL H4 calibration/holdout | **Supported procedurally** | Eight disclosed calibration cases and twenty sealed clean cases, all eventually accounted/admitted or disposed by evidence and owner authority. |
| A1 complete synchronized copies | **Supported with execution gate** | Exact full copies are format-compatible after path neutrality; inventory/completeness/parity/fresh runtime remain separate mandatory proofs. |

**Selected recommendation:** I2-C1R, the refined bounded C2+C3 family. It accepts explicit inline/file sources, recognizes only fixed HTTPS root aliases, records every occurrence before grouping, reuses one fetched preview through the unchanged typed classifier, emits a closed canonical preview with fixed actions and all-path before/after hashes, requires a separate digest-bound owner envelope, supports exact no-op and marker-bound recovery, authors complete location-neutral Claude command bodies and copies them byte-for-byte to Codex, proves both products in fresh exact-SHA contexts, and evaluates eight calibration plus twenty sealed holdout cases before adopting all source/evidence.

I2-C2R and I2-C3R remain fallback families if restricted canonicalization or the minimal fetch seam fails implementation evidence. I2-C4R remains the safest manual-type/root-only fallback. No observed contradiction requires a frozen HL amendment.

## Challenge Decisions

1. **I2-CD1 — Select I2-C1R after falsification, not the original I2-C1 verbatim.** Remove username subdomain/query/fragment support; retain three fixed HTTPS root domains and explicit dispositions for everything else.
2. **I2-CD2 — Keep the restricted canonical profile only with lexical negative-zero/float rejection, duplicate/unknown-field rejection, recursive closed schema, deterministic arrays, and renderer-completeness tests.** RFC 8785 remains the fallback, not an unimplemented label.
3. **I2-CD3 — Permit exact all-A no-op; permit mixed B/A recovery only with a durable payload/envelope-bound pending execution marker.** Any X or unmarked mixture stops.
4. **I2-CD4 — Keep C2 fetch-once/three-type reconciliation and require exact aggregation invariants plus `/kz-stats` regression.** Do not extract C4 merely for architectural tidiness.
5. **I2-CD5 — Preserve exact Claude-source-to-Codex bytes, but make bodies location-neutral and manual-authority self-gating.** Static completeness review and fresh literal runtime evidence remain mandatory.
6. **I2-CD6 — Replace discretionary opaque IDs and 20/8 with content-derived case keys and 8 calibration / 20 holdout.** Seal exact source bytes before Phase A; reveal/recompute after freeze; invalidate on holdout-driven change.
7. **I2-CD7 — Adopt raw source snapshots and a canonical occurrence manifest only after reveal/phase authority.** Preserve original unrelated files and treat preliminary text as source, never fact.
8. **I2-CD8 — Frozen amendment proposal: none.** All changes above refine free grammar/evidence/execution details inside the approved `/kz-add`, classifier reuse, full-copy, and 28-candidate calibration/holdout contract.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| I2-C1 survives as I2-C1R after removing subdomain/query/fragment support and making the raw scanner a closed, lossless occurrence extractor rather than a Markdown renderer. | TS must enumerate accepted grammar/dispositions and require adversarial scanner/parser vectors; live real candidates remain sealed. |
| Current typed classifier is pure/repeatable for same HTML and can establish exactly one type without three fetches. | Implementation must extract only the fetch seam and reproduce all stats/decoy/conflict behavior. |
| Restricted canonicalization survives only as a closed lexical/schema/rendering contract; generic JCS remains fallback. | TS must bind profile/version, conformance vectors, significant fields, fixed arrays, and unknown-field rejection. |
| Fixed actions and complete path vectors make stale stop/all-A no-op precise; mixed recovery needs a durable pending marker. | TS must define controlled paths, pending state, replacement order, validator gates, and exact receipt outcomes. |
| Exact copies remain feasible, but current relative links are a real parity defect that location-neutral bodies must remove. | Fresh Claude/Codex literal route, argument, loaded-path/hash, hard-stop, and no-mutation evidence must be obtained after implementation. |
| Content-derived 8/20 allocation closes opaque-ID gaming and better honors a substantial clean final run. | A non-Executor must seal matching source bytes and partition before Phase A; Researcher/Executor still may not inspect the twenty holdout cases. |
| Exact source sealing closes destructive untracked drift without overwriting parallel work. | Initial hash mismatch is a real owner/rebaseline stop; matching snapshots are adopted only after reveal. |

**Sufficiency:**
- [x] External source used? (RFC 3986, Python URL parsing security notes, CommonMark 0.31.2, Agent Skills specification, RFC 8785 errata, and official OpenAI skills guidance.)
- [x] Briefing gap closed? (Every Iteration 2 focus area has a selected contract, fallback, or explicit empirical execution gate.)
- [x] Pairwise incompatibility checked? Surviving configurations listed? (Twelve incompatible pairs; four survivors; two eliminated configurations.)
- [x] Hypothesis tested? (I2-H1–I2-H5, HL H2–H4, and A1 have explicit outcomes.)
- [x] Counter-evidence sought? (Markdown ambiguity, non-validating URL parser, reserved paths, negative zero/duplicates, hidden renderer fields, manual-revert crash state, relative-path parity, literal routing uncertainty, allocation gaming, shared-context leakage, and source loss.)
- [x] Metacognitive check completed? (Material corrections: exact copies had broken relative links; opaque IDs were gameable; 20/8 underweighted the final run; mixed recovery needed a marker; accepted URL grammar could be smaller.)

Stage complete: YES
→ User decision: Close Challenge; synthesize Iteration 2 RES after Coordinator authorization.

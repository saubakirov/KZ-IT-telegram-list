# Extract — "What do we NOT see?"
> **Mindset:** Analyst. Gather separated fourteen decisions; this stage makes their coherent combinations, state transitions, and proof surfaces visible without issuing the final recommendation.
> **Test:** The configurations must expose whether the same safety claim comes from grammar, canonical bytes, owner authority, runtime copies, or evaluation isolation instead of letting one mechanism stand in for all five.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Configuration Space

The six configurations below are coherent representatives of the larger cross-product. “C2+C3” means Iteration 1's intake orchestrator plus the separate approval-envelope feature; “C4+C3” means a shared observation module plus that same approval feature. C3 is not treated as an alternative to C2/C4.

| Config | D1: accepted public-peer URL forms | D2: child/action-link treatment | D3: source decoding | D4: occurrence extraction | D5: payload canonicalization | D6: approval-envelope representation | D7: freshness/replay binding | D8: complete-copy authoring direction | D9: fresh runtime proof | D10: observation boundary | D11: calibration/holdout allocation | D12: holdout sealing | D13: candidate-batch adoption | D14: apply rerun/partial-failure semantics |
|--------|------------------------------------|---------------------------------|---------------------|---------------------------|------------------------------|------------------------------------------|------------------------------|-----------------------------------------------|-------------------------|---------------------------|---------------------------------------------|----------------------|--------------------------------|------------------------------------------------|
| I2-C1 — bounded C2+C3 | C — fixed documented HTTP aliases plus `<handle>.t.me` | D — record every non-root form as unsupported/manual | B — inline text plus explicit `--file` | A — span scanner with wrapper-aware trimming | B — restricted repository canonical JSON | A — separate envelope over one fixed action set | C — exact controlled-path baselines plus parser/observer contract version | A — complete Claude source copied byte-for-byte to Codex | D — disposable-worktree proof, using nonpersistent CLI for Claude and a fresh Desktop task for Codex | A — intake orchestrator plus a small fetch-once seam; existing classifier remains authoritative | B — non-Executor deterministic hash allocation | C — dedicated calibration-only worktree/task; Coordinator retains holdout | B — canonical occurrence manifest after reveal | B — exact expected post-state recognizes no-op; known before/after vector permits bounded recovery |
| I2-C2 — standards-canonical C2+C3 | Same as I2-C1 | Same as I2-C1 | Same as I2-C1 | Same as I2-C1 | A — RFC 8785 JCS | A — separate envelope over one fixed action set | C — controlled-path baselines plus contract version | C — neutral complete source copied byte-identically to both runtimes | D — disposable-worktree proof with runtime-specific entry | A — intake orchestrator plus fetch-once seam | B — non-Executor deterministic hash allocation | C — dedicated calibration-only worktree/task | B — canonical occurrence manifest after reveal | B — exact post-state no-op plus bounded known-state recovery |
| I2-C3 — shared-observation C4+C3 | Same as I2-C1 | Same as I2-C1 | Same as I2-C1 | Same as I2-C1 | B — restricted repository canonical JSON | A — separate envelope over one fixed action set | C — controlled-path baselines plus contract version | A — complete Claude source copied byte-for-byte to Codex | D — disposable-worktree proof with runtime-specific entry | C — extract a shared Telegram observation module used by stats and intake | B — non-Executor deterministic hash allocation | C — dedicated calibration-only worktree/task | B — canonical occurrence manifest after reveal | B — exact post-state no-op plus bounded known-state recovery |
| I2-C4 — strict-root conservative | A — only root `https://t.me/<handle>` | A — reject every suffix/query | B — inline text plus explicit `--file` | A — span scanner | B — restricted repository canonical JSON | A — separate envelope | D — composite data/schema/generator/command hashes | A — Claude source copied byte-for-byte | D — disposable-worktree proof | A — orchestrator; declared/manual type before typed classifier | A — neutral manual stratification | C — calibration-only worktree/task | A — adopt exact source bytes after reveal | A — any drift, including exact already-applied state, stops |
| I2-C5 — broad-parent C4+C3 | D — HTTP aliases plus `tg://resolve` | B — derive parent from documented message/story links | C — inline, `--stdin`, explicit file | B — Markdown parser plus plaintext fallback | A — RFC 8785 JCS | A — separate envelope | C — baseline plus contract version | C — neutral complete source copied to both | D — disposable-worktree proof | C — shared observation module | B — deterministic non-Executor allocation | B — encrypted hidden manifest | B — occurrence manifest after reveal | B — exact post-state no-op |
| I2-C6 — authority-heavy C2+C3 | C — fixed HTTP aliases plus subdomain | D — unsupported/manual for all non-root forms | B — inline text plus explicit file | A — span scanner | A — RFC 8785 JCS | C — owner-held detached signature over payload/action digest | D — composite data/schema/generator/command hashes | C — neutral complete source copied to both | D — disposable-worktree proof | A — intake orchestrator plus fetch-once seam | B — deterministic non-Executor allocation | B — encrypted hidden manifest | A — exact source bytes after reveal | C — stage complete output set before path replacement; any non-baseline state stops |

I2-C1/I2-C2 isolate canonicalization and authoring-source differences. I2-C1/I2-C3 isolate observation architecture. I2-C1/I2-C4 isolates usable grammar, observed-type automation, freshness scope, and no-op recovery. I2-C3/I2-C5 isolates strict peer roots from parent extraction and a broader parser. I2-C1/I2-C6 isolates conversational trace authority from cryptographic/owner-secret operations. These pairings give Challenge specific comparisons instead of an undifferentiated feature list.

## Findings

### E1: The bounded grammar can be exact without attempting to implement Telegram's full deep-link client

The fixed-root grammar shared by I2-C1/I2-C2/I2-C3 is:

```text
accepted_candidate := https_root | https_username_subdomain

https_root := "https://" host "/" handle ["/" ] [fragment]
host := "t.me" | "www.t.me" | "telegram.me" | "www.telegram.me"
      | "telegram.dog" | "www.telegram.dog"

https_username_subdomain := "https://" handle ".t.me" ["/" ] [fragment]
handle := repository HANDLE_PATTERN
```

Additional constraints are part of the grammar, not post-hoc cleanup: no user-info; no explicit port; ASCII case-insensitive host; exactly one handle path segment for a candidate root; no percent-encoded slash or percent-encoded handle character; no query; and only an empty path or `/` on the username-subdomain form. Telegram's official [Deep links](https://core.telegram.org/api/links) documentation says fragments are ignored, so the grammar can preserve the raw fragment in the occurrence while excluding it from candidate identity. Whether a non-empty fragment itself should remain accepted is left as a Challenge attack, because accepting it adds no catalog information.

The scanner is wider than the accepted grammar. It records HTTP(S), `tg:`, and Telegram-like scheme-less spans, then the kind parser assigns one stable disposition before any handle normalization:

```text
accepted_public_root
invalid_public_handle
unsupported_public_child
unsupported_bot_action
private_invite
phone_or_private_user
reserved_telegram_action
unsupported_tg_uri
malformed_telegram_url
non_telegram_url
```

`unsupported_public_child` may include the parsed parent as non-authoritative diagnostic data, but it produces no candidate ID in I2-C1/I2-C2/I2-C3. This avoids converting a message, story, forum topic, or bot-start action into owner intent to catalog its parent. I2-C5 keeps parent extraction visible as a usability alternative for Challenge.

Occurrence extraction is deterministic over source bytes: scan in byte order; retain the raw span; remove a trailing sentence delimiter only when it is outside a Markdown/autolink wrapper or is an unmatched closing delimiter; parse the trimmed span; and never silently discard the removed suffix. The occurrence locator records original start/end offsets and the exact raw/parsed spans. Thus `[A](https://t.me/SyntheticAlpha), https://t.me/SyntheticAlpha.` yields two occurrences and one candidate, while `https://t.me/share?...` yields one non-candidate occurrence.

This configuration contains no raw holdout example. Synthetic identifiers are deliberately outside project data.

### E2: Source decoding can preserve `/kz-add <source>` while eliminating path/text ambiguity

I2-C1–I2-C4 use one public command with two exact source forms:

```text
/kz-add --text <one-or-many URLs / pasted Markdown>
/kz-add --file <existing UTF-8 source path>
```

A single URL is just `--text` with one occurrence; several pasted URLs remain one text source. Exactly one of `--text` and `--file` is required. A missing file is an input error, never reinterpreted as literal text. The command layer receives Claude's `$ARGUMENTS` or Codex's complete trailing prompt and passes the exact selected source to the deterministic script; the complete command body states these rules instead of delegating the meaning of `<source>` to the other agent's copy.

For a file, the durable source identity is SHA-256 plus byte length over the original bytes. UTF-8 decoding failure becomes a source-level error with no occurrence ledger fabricated. For inline text, the command creates a source snapshot from the exact UTF-8 encoding of the received text; presentation quoting is not part of the source bytes after the runtime's argument substitution. A source manifest records `source_kind`, digest, length, and a stable label, not a machine-specific absolute path as authority.

`--stdin` in I2-C5 is coherent but complicates an agent command: the agent must either invoke a subprocess with controlled stdin or create a temporary file, and the evidence must prove which bytes crossed that boundary. It is not required to support the three owner-stated modes (one link, many pasted links, file).

### E3: Restricted canonical JSON can be a JCS-compatible subset without claiming a general JCS implementation

[RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html) requires I-JSON inputs, rejects duplicate object names, preserves Unicode string data without normalization, uses ECMAScript number serialization, recursively sorts properties by UTF-16 code units, and preserves array order. The verified RFC errata also warns that negative zero canonicalizes to `0`, which can erase a distinction an application might otherwise treat as meaningful. None of the intake fields requires floats, negative zero, non-ASCII property names, or integers outside interoperable range.

I2-C1/I2-C3 therefore define a narrower named profile rather than claiming that Python's standard library implements every JCS case:

```text
profile: kz-canonical-json/v1
data model: object, array, UTF-8 Unicode string, boolean, null,
            integer in [-(2^53)+1, (2^53)-1]
forbidden: floats, NaN/Infinity, duplicate object names, invalid Unicode,
           non-ASCII object keys
object order: ascending ASCII key bytes, recursively
array order: schema-defined and preserved
string handling: no Unicode normalization; JSON escaping with ensure_ascii=false
serialization: no insignificant whitespace, no BOM, no trailing newline
digest: lowercase SHA-256 of serialized UTF-8 bytes
```

On this admitted domain, ASCII key ordering is identical under Unicode code-point, UTF-8 byte, and JCS UTF-16 ordering; integer serialization and strings also match JCS rules. The project can implement the profile with standard-library primitives plus explicit schema/duplicate-key validation and publish conformance vectors. A synthetic vector containing booleans, null, bounded integer, arrays, and EN/RU/KK strings serialized to 269 bytes with SHA-256 `bf575fd86077e520806b0bd7f8fba9193e90c981f7dd0ae3fb5ef438212b12e8`; a separate duplicate-key probe rejected the input. This is local feasibility evidence, not a generic RFC 8785 certification.

I2-C2/I2-C5/I2-C6 instead name RFC 8785 directly. They require either a reviewed implementation/dependency or a complete conformance suite including number, UTF-16 key-order, invalid-Unicode, duplicate-name, and verified-errata cases. JCS increases interoperability outside the present Python-only path, but its extra surface does not bind more significant fields; schema completeness remains separate. Exact pretty-byte hashing avoids canonicalization code but makes whitespace and renderer changes authority-significant. Extract retains I2-C1 and I2-C2 so Challenge can judge whether generic cross-language canonicalization buys evidence proportional to its dependency/proof cost.

### E4: One fixed-action preview avoids subset-approval and post-state ambiguity

The preview payload is not a menu whose envelope may choose arbitrary rows. It contains one complete proposed action vector over all accounted candidates, for example `add`, `no_change_duplicate`, `no_change_rejected`, or `no_change_unresolved`. If the owner changes any candidate action, category, localized description, or other field, the system creates a successor payload with a new digest and recomputed expected post-state. The envelope accepts or rejects that exact payload as a whole.

The research-level payload shape is:

```text
preview_payload
  schema_version
  canonicalization_profile
  parser_contract_version
  observer_contract_version
  predecessor_payload_sha256?       # retry/revision lineage only
  sources[]                         # stable ID, kind, digest, byte length
  occurrences[]                     # source/span/raw/parsed/link-kind/disposition/candidate ID?
  candidates[]                      # handle, occurrence IDs, collision, observation,
                                     # editorial evidence, exact proposed row/action
  controlled_paths[]                # repository-relative path, before SHA-256,
                                     # expected-after SHA-256
  totals                            # occurrence/candidate/action totals derived and checked
```

The arrays have schema-defined order: sources by source ID; occurrences by source ID then original byte start/ordinal; candidates by case-folded handle; controlled paths by repository path. Derived totals must be recomputed and compared rather than trusted. The payload contains neither its own digest nor the future approval/receipt.

The physically separate envelope is:

```text
approval_envelope
  schema_version
  approval_id                       # unique record/nonce
  preview_payload_sha256
  canonicalization_profile
  approved_action_set_sha256        # digest of the payload's exact action projection
  approved_candidate_ids[]          # exact equality with payload's add actions
  owner_identity
  owner_authority_evidence_ref       # current conversation/journal reference
  approved_at
  expires_at?                        # if the chosen freshness policy uses time
```

The envelope is valid only when the referenced authority event explicitly names the payload digest/action set; an agent-populated `owner_identity` is insufficient. OWASP's [transaction authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html) supports the significant-data binding, per-operation uniqueness, and final execution gate used here. A detached signature in I2-C6 strengthens origin only when the owner controls the key and actually performs the signature; otherwise it merely adds agent-generated bytes.

The apply receipt is third and immutable:

```text
apply_receipt
  schema_version
  preview_payload_sha256
  approval_envelope_sha256
  execution_id
  started_at / completed_at
  initial_state                    # baseline | expected_post | recognized_partial
  controlled_paths[]              # observed-before, written?, final SHA-256
  validation_results
  applied_candidate_ids[]
  outcome                          # applied | already_applied_exact | recovered_exact | failed
```

This separation makes preview meaning, owner authority, and execution history independently reviewable.

### E5: Strict baseline and idempotent no-op can coexist through a controlled-path state vector

“Strict baseline” need not mean that a successful retry is reported as unexplained drift. The preview is built before approval from exact controlled paths: `data/communities.json` plus every deterministic generated projection the operation is allowed to change. It records each path's exact before hash and computes the exact expected-after bytes/hashes from the fixed action set in a temporary area.

At apply, every controlled path is classified:

```text
B = exact preview before hash
A = exact preview expected-after hash
X = neither hash / missing / extra unexpected controlled state
```

The state machine is:

```text
all B  → revalidate payload/envelope/current live freshness
         → stage and validate complete A bytes
         → replace only controlled paths
         → require all A → receipt: applied

all A  → revalidate payload/envelope and generated currency
         → write no catalog/projection byte
         → receipt/output: already_applied_exact

mix B/A, no X
       → accept only when execution lineage proves an interrupted same-payload apply
         or the implementation explicitly permits hash-bound deterministic recovery
         → write remaining B paths to their exact A bytes
         → require all A → receipt: recovered_exact

any X → stale/unexplained drift hard stop; no write
```

This is stronger than “handle already exists”: every source-of-truth and generated byte must equal the approved post-state. It also prevents an unrelated catalog edit from being mistaken for idempotency. If Challenge rejects recovery without a prior execution marker, the mixed state can remain a hard stop while all-A no-op still survives; the two choices are separable.

Staging validates schema and all generated projections before the first replacement, but ordinary filesystems do not provide one atomic replacement across several paths. The B/A vector therefore supplies crash recognition. The operation never derives new post bytes after approval; it uses the approved deterministic result and still reruns current validators. A live observation that has exceeded the chosen freshness policy creates a new preview, not an in-place refresh under the old envelope.

### E6: C2+C3 can discover type with one fetch and the existing typed classifier; C4+C3 buys module clarity at wider regression cost

The smallest C2+C3 flow does not need a second identity/type classifier:

```text
source-kind parser → candidate handle
  → fetch public preview once using extracted network/retry seam
  → call existing pure classify_response(html, handle, declared_type)
       for groups, channels, bots over the same bytes
  → exactly one verified typed result = observed candidate type
  → zero/multiple verified or any identity conflict = unresolved/fail-closed
```

The network seam returns fetched HTML or a stable transport failure without interpreting identity. Existing `classify_response` remains the only target-binding/type gate and receives identical bytes for all three expectations. `check_link_with_retry(handle, entry_type)` can compose the same fetch seam for `/kz-stats`, preserving current outputs. This is a small change inside the present validator plus a new intake orchestrator; classifier decoy/conflict regression tests remain mandatory.

C4+C3 extracts URL identity helpers, preview parser, observed type, typed classifier, and retry/fetch behavior into a shared module consumed by both stats and intake. Its conceptual API is clearer and avoids importing an operational CLI module, but it changes import/ownership boundaries for every catalog sweep. The equivalence obligation is not only unit output on a few fixtures: current stats summary schema, retry semantics, mutation/archive separation, target-bound identity conflicts, type mismatches, and all historical decoy cases must remain exact.

| Proof lane | I2-C1 C2+C3 | I2-C3 C4+C3 |
|------------|---------------|---------------|
| Source grammar | New, isolated from validator helper | New, isolated from shared observation module |
| Network change | Extract/reuse one fetch-with-retry seam | Move/rewrite fetch/retry into module |
| Classifier change | None intended; call current pure classifier three times on same bytes | Physical extraction/re-import; semantic equivalence required |
| Stats regression surface | Fetch seam and `check_link_with_retry` composition | Parser, identity, type, retry imports/API and stats composition |
| Intake dependency | Imports stable functions from operational validator | Imports purpose-built shared module |
| Long-term ownership | Some cross-script coupling | One explicit observation component |
| Failure containment | Intake orchestration can fail without relocating stats core | Module regression can affect both consumers |

The configuration comparison reveals that C2's type problem is solvable without C4. C4 must therefore justify itself through maintainability/API ownership and demonstrated equivalence, not through a claim that type discovery is otherwise impossible.

### E7: Claude-source exact copying is the smallest provenance chain for the current three-command inventory

I2-C1/I2-C3/I2-C4 use each `.claude/commands/kz-*.md` file as the complete authoring source and copy its exact bytes to `.agents/skills/<name>/SKILL.md`. This direction preserves the two already-reviewed complete bodies and adds common `name` front matter that Claude officially ignores in command files while Codex requires in skills. A neutral source in I2-C2/I2-C5/I2-C6 is coherent but creates a third complete copy or template whose own drift/status must be defined.

The parity operation is a deterministic inventory/sync command with two modes:

```text
sync:  for every exact name in {kz-add, kz-stats, kz-release},
       validate complete source front matter/body, then replace Codex bytes exactly

check: require exact name set on both sides, valid common front matter,
       byte-for-byte equality for each pair, and complete-body contract markers
```

Complete-body markers are not a substitute for review, but they defeat identical thin copies. Each runtime file must state its own command name/arguments, authority/mode, source-of-truth files, ordered operation, output/evidence, mutation boundary, failure conditions, and hard stop. It may invoke deterministic project scripts; it may not instruct the runtime to read the other agent's command, a generator source, or a separate workflow to learn those rules.

Drift outcomes are exact: missing name, extra `kz-*` runtime, invalid/mismatched `name`, byte difference, forbidden thin-reference phrase/absent required sections, or generated copy not current all fail `--check`. A changed Claude source is not automatically propagated during tests; the explicit sync changes Codex bytes, then review sees both. This preserves A1's full copies while keeping one authoring direction.

### E8: Fresh runtime evidence needs a two-product protocol, not one portable CLI command

Official OpenAI [Build skills](https://learn.chatgpt.com/docs/build-skills) guidance establishes `.agents/skills`, metadata discovery, explicit `$skill`/`/skills`, implicit description matching, and full `SKILL.md` loading. It does not establish literal arbitrary `/kz-*` aliases. The project-level `AGENTS.md` route and a fresh Codex execution must prove that compatibility surface.

The exact runtime evidence protocol for I2-C1/I2-C3 is:

1. Freeze an implementation SHA and construct a clean disposable worktree/archive that excludes untracked raw candidate/holdout files.
2. Run static inventory/front-matter/completeness/byte-parity checks first.
3. Claude: start `claude -p --no-session-persistence` with project settings, tools disabled, structured output, and synthetic reserved/malformed Telegram input that requires parsing but no live candidate probe. Capture invocation, argument sentinel, command identity, preview/no-mutation conclusion, and clean Git hashes.
4. Codex: start a genuinely new Desktop task at the same exact worktree/SHA, without forking authoring/research context. Invoke literal `/kz-add --text <synthetic reserved-link sentinel>` in plan/read-only mode. Capture that the repository-local `kz-add` skill loaded, the complete trailing argument arrived, no live/candidate/catalog mutation occurred, and the worktree hashes stayed clean.
5. In separate fresh turns/tasks, invoke `/kz-stats` and `/kz-release` as explicit “routing/hard-stop smoke only; do not execute the operation” prompts under the same read-only/disposable boundary. Require their owner-triage and pre-tag/push hard stops to be stated from the local complete body.
6. Independently run deterministic offline behavior tests against synthetic HTML/source fixtures. Runtime prose is not the parser/classifier proof.

The Codex fallback `$kz-add` can demonstrate official skill selection if literal routing fails, but it does not satisfy the project's literal command claim; that result is a finding. The current WindowsApps CLI access denial is not bypassed. A fresh Desktop task is the selected proof path within these configurations, while Challenge must test whether task freshness, plan mode, and exact worktree binding are sufficiently observable.

### E9: A 20/8 deterministic allocation produces a testable holdout without exposing it to Phase A

The current corpus has 28 unique candidate cases after collapsing the one already-recorded overlap. I2-C1/I2-C2/I2-C3 instantiate D11/D12 as 20 calibration cases and eight holdout cases. The size is an exact configuration value, not a claim that eight estimates a population rate; the holdout is a workflow generalization check across the complete current batch.

Before implementation, a non-Executor allocation authority:

1. re-verifies the two predecessor source digests without using the proposed parser;
2. manually establishes 28 opaque case IDs and the known occurrence-to-case overlap map;
3. computes `SHA-256("kz-intake-holdout-v1\0" + case_id)` and assigns the eight lexicographically smallest scores to holdout, the remaining 20 to calibration;
4. creates a canonical full partition manifest containing source digests, all occurrence/case links, allocation rule/version, scores, and partitions;
5. publishes only its digest, total `28`, split `20/8`, source digests, overlap count `1`, and allocation rule/version;
6. supplies Phase A a calibration-only plaintext manifest; the full/holdout manifest remains outside the repository and outside the Executor task/worktree.

Opaque case IDs must be stable and assigned before scores are calculated; renumbering to influence the split invalidates the commitment. A public seed makes later recomputation possible. The allocation authority sees the cases, but the Phase A Executor receives neither hidden IDs/content nor source paths. Synthetic fixtures cover URL grammar; calibration supplies real variation without revealing the eight final cases.

The reveal gate after Phase A review/freeze is:

```text
full manifest bytes revealed into Phase B evidence
  → canonical digest equals preimplementation commitment
  → source digests/counts/overlap equal commitment
  → recompute every allocation score and exact 20/8 membership
  → prove no holdout identifier/URL/raw text occurred in Phase A code,
    fixtures, smokes, prompts, expected outcomes, or evidence
  → clean Phase B runner receives the eight cases once
  → outcomes recorded without rule/fixture/prompt tuning
```

If a holdout result drives any parser, classifier composition, command instruction, inclusion rule, or permanent expected fixture change, the current holdout result becomes calibration evidence and cannot be reported as the clean final run. A later independent batch is then required for the changed design. This applies even if the code change looks like an obvious bug fix.

This protocol cannot prove that no human ever recognized a case. It proves the narrower and auditable statement that Phase A's implementation/evaluation surfaces did not receive or adapt to the sealed eight-case manifest.

### E10: Candidate provenance should become an occurrence manifest only after reveal, with source bytes retained as evidence when authorized

I2-C1/I2-C2/I2-C3 choose a canonical occurrence manifest as the durable operational input after the clean reveal because the preliminary note mixes candidate suggestions with unverified analysis. The manifest records source digest/length/label, exact raw occurrence/span, parsed disposition, candidate grouping, and later evidence/action. It does not copy preliminary “live”, topic, or admission claims as facts.

For forensic provenance, an exact read-only copy of the source bytes may also be retained after holdout opens and owner/phase authority permits it; the manifest references its digest. These roles are distinct:

- raw snapshot: what bytes were supplied;
- occurrence manifest: how every Telegram-like occurrence was accounted for;
- preview payload: what was observed/proposed at one baseline;
- approval envelope: what exact action the owner authorized;
- apply receipt: what changed.

Before either adoption, the current source must hash to the predecessor snapshot. A mismatch stops and requires a new owner-authorized source snapshot/allocation; the workflow never overwrites or stages the unrelated original to make it match. The provenance statement is “owner-supplied candidate input with observed digest,” not inferred file authorship.

### E11: Representative synthetic flows separate configuration behavior from eventual real-candidate outcomes

| Flow | Synthetic setup | I2-C1 C2+C3 trace | I2-C3 C4+C3 difference | Bound result |
|------|-----------------|---------------------|----------------------------|--------------|
| Multi-link text | Markdown root A, alias root B, duplicate root A on one line | Three occurrence IDs in byte order → two case-folded candidates → one fetch per candidate | Same ledger; shared module owns fetch/classification | `occurrences=3`, `candidates=2`; duplicate never disappears |
| Unsupported Telegram action | `t.me/share?...`, private invite, public message child | Three occurrence dispositions; zero candidate IDs; zero network fetches | Same | Preview accounts for all three and cannot add a peer |
| Identity conflict | Candidate A preview exposes authoritative identity B | Same HTML is classified for all types; target binding fails before name/type/count | Shared module returns the same conflict | Candidate unresolved; downstream facts hidden; no add action |
| Type discovery | Bound preview clearly exposes channel | One fetch; three typed pure classifications; exactly channel verifies | Shared module emits observation consumed by stats/intake | Observed type is channel; no curator-declared guess required |
| Partial live failure | A verifies; B transport fails | Payload action vector may propose add A and unresolved/no-change B; owner approves exact vector | Same | Applying A does not pretend B was tested successfully; B retry is successor payload |
| Changed hidden field | Same rendered summary, different `description_kk` or occurrence disposition | Canonical payload digest changes; old envelope fails | Same | Visible-table equality cannot reuse approval |
| Stale catalog | Current controlled path is neither before nor expected-after | Apply stops with X before any write | Same | No “rebase under approval” |
| Crash after some replacements | Every controlled path is exact B or A, with same execution lineage | Bounded recovery may write remaining exact A bytes; no new derivation | Same | Final all-A receipt or hard stop; no partial candidate discretion |
| Exact rerun | Every controlled path equals expected A | No catalog/projection write; emit `already_applied_exact` evidence | Same | Idempotence is exact-byte post-state, not handle existence |
| Copy drift | One Codex byte differs from Claude source | Inventory/parity check fails before fresh smoke | Same | Runtime evidence cannot bless drifted copies |
| Fresh Codex literal route | New exact-SHA task receives reserved-link sentinel | `AGENTS.md` routes literal command; local skill loads; argument echoed/accounted; no mutation | Same | `$kz-add` fallback alone is insufficient for literal claim |
| Holdout access attempt | Phase A task searches for holdout manifest | Manifest/path/content absent from worktree/task; only commitment and calibration exist | Same | Clean-run claim preserved; attempt logged, not satisfied |
| Source drift before reveal | Candidate note hash differs from predecessor | Reveal/adoption stops; no parser run or reallocation in place | Same | Owner must establish a new source snapshot and evaluation cycle |

The flows expose one previously implicit combination: I2-C1 joins a C2 orchestrator, C3 physical approval envelope, restricted JCS-compatible canonical subset, exact Claude-source runtime copies, exact-post no-op semantics, a fresh Codex Desktop task, and a 20/8 hidden manifest. None of the Briefing families specified that complete state machine as one configuration.

### E12: Pairwise dependencies to attack in Challenge

- D1 C with D2 D is coherent only if parent handles in child/action links remain diagnostic and never become candidate IDs.
- D4 A must prove wrapper punctuation without a Markdown dependency; if it cannot, I2-C1 collapses toward I2-C5's parser stack.
- D5 B is safe only while the schema rejects every value outside its canonical subset and test vectors cover Python/runtime encoding; calling it “JCS” without those constraints would be false.
- D6 A with a fixed action vector means owner edits always create a successor payload; allowing envelope subsets would invalidate expected-post hashes.
- D7 C and D14 B require every controlled path's before/after hash in the approved payload; a data-only baseline cannot recognize mixed projection recovery safely.
- D8 A requires adding common `name` front matter to the existing Claude sources before exact copy; sync must never make Codex the hidden authoring source.
- D9 D must prove a genuinely fresh Codex Desktop task at the exact SHA/worktree; the current research task and static skill listing are contaminated evidence.
- D10 A type discovery relies on one fetch plus three pure typed classifications; any classifier side effect or type-dependent parse would break same-bytes reconciliation.
- D11 B/D12 C are only neutral if opaque case IDs and allocation rule are fixed before implementation and hidden raw material is absent from the Executor context/worktree.
- D13 B must retain lossless occurrence/source binding; a normalized-handle-only manifest would erase malformed and duplicate accounting.

## Extract Decisions

1. **I2-ED1 — Carry I2-C1, I2-C2, I2-C3, I2-C4, I2-C5, and I2-C6 into Challenge as pairwise-isolated configurations.** No row is yet recommended; each changes a small, visible set of Gather dimensions.
2. **I2-ED2 — Treat restricted canonical JSON as a named JCS-compatible subset, not an informal or generic JCS claim.** Challenge must compare its schema/conformance proof against a real RFC 8785 implementation rather than compare labels.
3. **I2-ED3 — Bind one fixed action vector and the complete controlled-path before/expected-after state inside the preview.** This keeps subset approval, no-op recognition, and crash recovery from silently recomputing owner-significant data.
4. **I2-ED4 — Test C2 type discovery as one fetch plus three calls to the unchanged typed classifier.** C4 remains a maintainability/equivalence alternative, not a prerequisite for safe observed type.
5. **I2-ED5 — Use exact Claude-source-to-Codex bytes as the minimal current provenance chain in the bounded configurations.** Neutral-source and signature-heavy variants remain for counter-evidence; completeness and fresh runtime behavior stay independent gates.
6. **I2-ED6 — Instantiate the sealed protocol as 20 calibration / 8 holdout with deterministic non-Executor allocation and calibration-only Phase A access.** Challenge must attack opaque-ID assignment, source drift, path/context leakage, reveal proof, and post-holdout invalidation.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| I2-C1 provides one exact bounded C2+C3 configuration; I2-C2 and I2-C3 independently swap canonicalization and observation architecture. | Challenge the strict root/alias grammar, scanner punctuation, same-bytes typed classification, and the claim that no shared module is needed. |
| A restricted ASCII-key/no-float canonical profile is JCS-compatible on its admitted domain and can use stdlib with duplicate/schema/conformance gates. | Challenge encoding, Unicode, integer range, array order, hidden-field coverage, implementation drift, and whether RFC 8785 dependency is still preferable. |
| Fixed-action payload + separate envelope + receipt eliminates subset/self-reference ambiguity and binds exact before/after path hashes. | Challenge owner edits, retries, freshness, expired observation, all-A no-op, mixed B/A recovery, missing receipt, and X drift. |
| C2 can fetch once and reuse the current typed classifier three times; C4's benefit becomes module ownership rather than type feasibility. | Compare exact regression/equivalence cost and test whether the current classifier is truly pure across all typed calls. |
| Claude-source exact copying preserves reviewed bodies and supplies a shorter provenance chain than a neutral third source. | Challenge unknown front matter tolerance, literal Codex routing, dropped arguments, identical-thin-body false positives, and fresh task observability. |
| A concrete 20/8 deterministic allocation/reveal protocol avoids raw holdout access by this Researcher and Phase A Executor. | Challenge case-ID gaming, shared filesystem/context leakage, loss of the hidden manifest, source drift, and any holdout-driven correction. |
| Candidate adoption can preserve exact source provenance without promoting preliminary notes by separating raw snapshot and occurrence manifest. | Challenge whether the raw snapshot must be committed post-reveal, how source drift is re-authorized, and whether every non-candidate occurrence remains lossless. |

**Sufficiency:**
- [x] External source used? (RFC 8785 and verified errata; OWASP transaction authorization; official Telegram, Anthropic, and OpenAI documentation carried into exact configurations.)
- [x] Briefing gap closed? (Exact grammar, payload/envelope/receipt, source direction, fresh Desktop proof, C2/C4 comparison, holdout protocol, and provenance now have concrete flows.)
- [x] Configuration Space built from Gather dimensions? (Six coherent configurations cross all fourteen dimensions and expose pairwise comparisons.)
- [x] Hypothesis tested? (I2-H1–I2-H5 each has a complete feasible configuration and named failure dependencies.)
- [x] Counter-evidence sought? (generic-JCS overclaim, subset approval/post-state mismatch, multi-file non-atomicity, C2 type seam, literal Codex documentation gap, and unverifiable global holdout blindness.)
- [x] Metacognitive check completed? (New combinations: restricted-JCS-compatible profile plus fixed-action state vector; same-bytes typed classification; runtime-specific fresh proof under one disposable boundary; deterministic 20/8 reveal protocol.)

Stage complete: YES
→ User decision: Close Extract; proceed to Challenge after Coordinator authorization.

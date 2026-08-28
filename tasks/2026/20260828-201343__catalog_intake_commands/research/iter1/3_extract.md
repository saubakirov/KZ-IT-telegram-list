# Extract — "What do we NOT see?"
> **Mindset:** Analyst. The raw alternatives are arranged into coherent configurations and state flows without selecting an implementation.
> **Test:** C2 exposes an exact-byte Claude-command/Codex-skill arrangement that was not proposed in the Briefing, while C3 exposes a two-artifact approval envelope and C7 preserves unresolved type without losing the source occurrence.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Configuration Space

The full Cartesian space is larger than 30 combinations. The rows below cover coherent cross-dimension configurations; each row differs from C1 in at least one Gather dimension. Alt letters refer exactly to D1–D8 in [Gather](2_gather.md).

| Config | D1: candidate-classifier boundary | D2: candidate type establishment | D3: source grammar | D4: loss and duplicate accounting | D5: approval binding | D6: full-copy source and parity | D7: editorial allocation | D8: calibration and holdout |
|--------|-----------------------------------|----------------------------------|--------------------|-----------------------------------|----------------------|---------------------------------|--------------------------|-----------------------------|
| C1 — extended typed CLI | A — extend present CLI | A — declared type | B — explicit file + inline text | B — occurrence ledger then group | C — manifest digest + IDs | B — Claude source generates Codex | C — evidence only, owner decides | B — predeclared stratified split |
| C2 — exact-copy orchestrator | B — intake imports classifier | C — observed-type pass | B — explicit file + inline text | B — occurrence ledger then group | C — manifest digest + IDs | A — project complete source copied verbatim | B — structural negative gate + owner fit | B — predeclared stratified split |
| C3 — approval envelope | B — intake imports classifier | D — unresolved until triage | C — repeatable URL/file/stdin | B — occurrence ledger then group | D — separate approval file | A — project complete source rendered twice | D — independent review + owner | B — predeclared stratified split |
| C4 — shared observation module | C — shared module | C — observed-type pass | C — repeatable URL/file/stdin | B — occurrence ledger then group | C — manifest digest + IDs | B — Claude source generates Codex | B — structural negative gate + owner fit | B — predeclared stratified split |
| C5 — multi-type shared module | C — shared module | B — reconcile all requested types | B — explicit file + inline text | B — occurrence ledger then group | D — separate approval file | C — Codex source generates Claude | D — independent review + owner | B — predeclared stratified split |
| C6 — dual-authored surface | B — intake imports classifier | A — declared type | B — explicit file + inline text | B — occurrence ledger then group | C — manifest digest + IDs | D — dual author + semantic parity | C — evidence only, owner decides | C — source-based split |
| C7 — unresolved-type ledger | B — intake imports classifier | D — unresolved until triage | C — repeatable URL/file/stdin | C — per-source-line result | D — separate approval file | A — project complete source rendered twice | C — evidence only, owner decides | B — predeclared stratified split |
| C8 — whole-source transaction | A — extend present CLI | A — declared type | B — explicit file + inline text | D — reject whole source on malformed/duplicate | D — separate approval file | B — Claude source generates Codex | B — structural negative gate + owner fit | B — predeclared stratified split |
| C9 — argument-file composition | B — intake imports classifier | C — observed-type pass | D — generic `@file` + positional | C — per-source-line result | C — manifest digest + IDs | A — project complete source rendered twice | B — structural negative gate + owner fit | C — source-based split |
| C10 — present plus future proof | C — shared module | C — observed-type pass | C — repeatable URL/file/stdin | B — occurrence ledger then group | D — separate approval file | A — project complete source rendered twice | D — independent review + owner | D — present calibration + future batch |
| C11 — equivalent second classifier | D — second classifier | B — reconcile all requested types | B — explicit file + inline text | B — occurrence ledger then group | C — manifest digest + IDs | D — dual author + semantic parity | B — structural negative gate + owner fit | B — predeclared stratified split |
| C12 — conversational approval | B — intake imports classifier | C — observed-type pass | B — explicit file + inline text | B — occurrence ledger then group | A — conversational “yes” | A — project complete source rendered twice | D — independent review + owner | B — predeclared stratified split |
| C13 — approval flag | B — intake imports classifier | A — declared type | C — repeatable URL/file/stdin | B — occurrence ledger then group | B — boolean flag | B — Claude source generates Codex | C — evidence only, owner decides | B — predeclared stratified split |
| C14 — source-isolated proof | C — shared module | D — unresolved until triage | B — explicit file + inline text | B — occurrence ledger then group | D — separate approval file | C — Codex source generates Claude | B — structural negative gate + owner fit | C — source-based split |

## Findings

### E1: Four classifier architectures reduce to one invariant observation boundary

D1 produces four implementation shapes, but the reusable evidence flow is the same:

```text
raw source
  → source decoder
  → occurrence ledger                           [29 source occurrences]
  → normalized candidate groups                 [28 unique handles]
  → exact live/archive/cross-input collision scan
  → one target-bound Telegram observation
  → requested/canonical identity + observed type evidence
  → editorial triage and localized proposal
  → exact preview payload                        [catalog unchanged]
  → exact owner approval binding
  → baseline/freshness/gate recheck
  → catalog apply + schema/generation validation
  → final occurrence and candidate dispositions
```

C1 and C8 place source orchestration inside the existing CLI. C2, C3, C6, C7, C9, C12, and C13 compose the existing functions from a separate intake boundary. C4, C5, C10, and C14 first make observation an explicit shared module. C11 duplicates classifier logic and treats equivalence testing as the connecting contract. None of these shapes changes GD1: candidate type establishment remains separate from accepting an arbitrary handle.

The existing `classify_response(html, handle, entry_type)` suggests another combination hidden by the column labels: a C2/C4 observed-type pass can parse one fetched HTML document, derive the preview's observed type, and then run the existing typed classifier against those same bytes. It need not fetch once per possible type. Conversely, D2 Alt B can deliberately run all requested-type interpretations over the same HTML, but its reconciliation schema must distinguish “one observation, three expectations” from three independent network observations.

### E2: Occurrence completeness and candidate idempotence are two related ledgers

GD2 rules out treating the unique-candidate table as the whole source record, but it does not choose a D3 syntax. The extracted minimum relationship is:

```text
source_id + raw_sha256
  └─ occurrence_id + line/column/span + raw_token + parse_disposition
       └─ normalized_handle? + candidate_id?
            └─ observation_id? + candidate_disposition
```

This relationship lets a repeated URL be explicitly `duplicate_input` at occurrence level while its candidate has exactly one network observation and one final disposition. A malformed Telegram-like token can remain `malformed` without inventing a candidate. An input line containing two links produces two occurrence IDs, which C7/C9's line-only accounting otherwise conflates. Resuming a partially failed live run can reuse immutable parse/group results and retry only unresolved candidate observations; idempotence is then keyed to stable source/candidate identity rather than list position.

C8 adds whole-source atomicity at the parse boundary: any malformed or duplicate occurrence prevents probing/apply but can still be fully reported. C2/C3/C4/C5 instead permit complete parsing and candidate evidence for the valid subset while retaining explicit malformed/unresolved dispositions. Challenge must compare which failure boundary matches the frozen requirement to fail visibly without silently discarding valid work.

### E3: Canonical bytes bind evidence, but the approval itself needs a non-circular envelope

[RFC 8785, JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785.html) defines deterministic JSON property sorting and primitive serialization so the result is invariant and hashable. Python's standard [`json`](https://docs.python.org/3/library/json.html) can sort keys and remove insignificant whitespace, but that alone is not a claim of RFC 8785 compatibility, especially for number and Unicode rules. The repository can choose and name a narrower schema-specific canonical serialization or a conforming JCS implementation; the evidence must state which contract produced the digest.

The D5 configurations expose four authority models:

| D5 alternative | What can be bound | Drift/resume property | Structural issue surfaced |
|---|---|---|---|
| A — conversational “yes” | The human-visible table in current context | Depends on retaining an exact trace reference | A later agent may know approval occurred without a machine-verifiable set/baseline |
| B — boolean flag | The invocation in which the flag appears | Easy to automate | The flag does not name candidate IDs, evidence digest, catalog baseline, or approving actor |
| C — manifest digest + IDs | Payload bytes and explicit selected IDs | Recomputable before apply | If approval is embedded in the object being hashed, naïve self-hashing becomes circular |
| D — separate approval file | Immutable preview digest plus selected IDs/actor/time | Independently appendable and resumable | Two artifacts must be kept together and cross-validated |

The circularity in D5 Alt C is new. It can be modeled as an immutable `payload` whose digest is calculated first, followed by an approval envelope that references `payload_digest`; the envelope is not part of the payload digest. D5 Alt D makes the separation physical. D5 A can also be exact if the durable conversation/journal records that same digest and IDs, but the binding still needs a machine-readable projection for resumability. A digest proves byte identity, not owner authority, candidate eligibility, or freshness; those are separate checks.

A second time boundary appears after approval. Even an exact approved payload can become stale if `data/communities.json`, a live/canonical identity, category registry, or localized proposal changes. The configurations therefore need two named states rather than one overloaded “approved”: approval over an immutable preview, followed by apply-time verification that the exact set still passes current gates. This elaborates the approved preview/apply boundary without changing it.

### E4: Frozen Claude/Codex paths can contain exact-byte command copies

The frozen HL visual names `.claude/commands/kz-*.md` and `.agents/skills/kz-*/SKILL.md`. Official Claude documentation now says command files and skills work the same way; importantly, files in `.claude/commands/` support the same front matter while ignoring `name` and `paths`, and invocation uses the command filename ([Anthropic, “Extend Claude with skills”](https://code.claude.com/docs/en/slash-commands)). Official Codex documentation requires `name` and `description` in `SKILL.md`, then loads the full file when selected ([OpenAI, “Build skills”](https://learn.chatgpt.com/docs/build-skills)). Therefore one complete Markdown document with the common `name` + `description` front matter can be copied byte-for-byte to both frozen runtime paths: Claude ignores `name`; Codex requires it.

That exact-copy arrangement is the unanticipated combination represented by C2/C3/C9/C10/C12. It does not require moving Claude commands to `.claude/skills`, declaring a format-only transformation, or creating a thin reference. D6 still has multiple source-of-truth choices:

| D6 alternative | Runtime bytes | Authoring/source arrangement | Parity evidence available |
|---|---|---|---|
| A — separate project-owned source | Both runtime copies can be byte-identical | Third complete source renders/copies both | Source-to-Claude and source-to-Codex hash checks plus runtime set inventory |
| B — Claude source | Both runtime copies can be byte-identical | `.claude/commands/...` generates corresponding Codex skill | Claude-to-Codex hash check plus runtime set inventory |
| C — Codex source | Both runtime copies can be byte-identical | `.agents/skills/.../SKILL.md` generates Claude command | Codex-to-Claude hash check plus runtime set inventory |
| D — dual authored | Bytes may differ | Both runtime files edited independently | Declared normalization and semantic/behavior tests; no exact source-copy proof |

A1 completeness is stronger than hash parity. A pair of identical thin links would hash-match and still fail. Parity therefore separates: command-set equality (`kz-add`, `kz-stats`, `kz-release` on both sides); full-body structural assertions (authority, inputs, outputs, failure/approval hard stops); exact bytes or declared transformation; and fresh-session behavior. Anthropic's official evaluation guidance explicitly separates whether a skill invokes from whether its output is correct and calls for fresh sessions because authoring context can hide missing instructions. OpenAI likewise says Codex initially matches name/description and only then loads the full `SKILL.md`; description-trigger and full-body execution are distinct gates.

### E5: “Self-contained command” does not mean duplicating deterministic project code

The command bodies can remain complete instructions while invoking versioned repository scripts for parsing, probing, canonical serialization, validation, and generation. What A1 rejects is another command/workflow/runbook that must be opened to learn the operation's authority, sequence, inputs, outputs, or hard stops. D6 source copying concerns the agent instruction surface; D1 source sharing concerns deterministic code. Treating them as the same duplication problem would either recreate classifier logic in prose or turn the complete command back into a thin pointer.

This distinction also preserves `/kz-stats` and `/kz-release`: their complete existing bodies can be copied without rewriting their logic into the intake engine. Cross-command shared facts such as source-of-truth paths may appear in all three complete bodies, while each command keeps its own mutation and external-authority boundary.

### E6: Editorial allocation produces a gate matrix, not one classifier score

The configurations can share one evidence matrix even when D7 authority differs:

| Gate | Mechanical observation | Evidence-supported analysis | Final authority |
|---|---|---|---|
| Parse/handle syntax | Yes | No | Script result |
| Requested/canonical identity and observed type | Yes, from target-bound preview | Continuity/alias explanation may be needed | Conflict remains fail-closed; owner rules on supported continuity |
| Liveness/count/date | Yes when observed | Browser fallback may clarify ambiguity | No observation means unresolved, not inferred |
| Exact live/archive duplicate | Yes | Different-handle alias may need research | Owner accepts any supported continuity/add disposition |
| IT and Kazakhstan relevance | No single mechanical fact | Cited title/description/content signals | Owner inclusion judgment |
| Commerciality/quality/spam | No single mechanical fact | Cited content and purpose signals | Owner inclusion judgment |
| Category and EN/RU/KK completeness | Registry/field presence is mechanical | Correct category and copy quality are editorial | Owner approves exact proposed row |

D7 Alt B allows structural negative states to stop eligibility while leaving positive editorial gates to the owner. Alt C reports all evidence without any agent-side admission result. Alt D adds an independent advisory review before owner approval. Alt A would need a defensible source of truth for every non-mechanical cell; none was found in Gather. Challenge must attack each configuration's claim boundaries rather than compare a single opaque “fit” score.

### E7: Holdout configurations differ in isolation strength, not merely candidate count

GD3 is preserved across the configuration space: the present holdout means precommitted no-tuning, not globally unseen. A useful manifest can bind candidate IDs, source digests, declared strata, allocation method, and the point after which holdout outcomes may not change Phase A rules or permanent expected fixtures.

D8 Alt B can stratify before live calibration by known structural risk classes without encoding expected outcomes: duplicate/collision, requested/canonical conflict, likely type diversity, sparse preview, and ordinary control. D8 Alt C isolates by input source but the `aws_kz` overlap and preliminary outcomes in the 23-candidate file reduce independence. D8 Alt A is reproducible only if its seed and input ordering are bound, yet splitting after implementation still allows rule leakage. D8 Alt D adds the strongest later generalization check but does not satisfy the frozen Phase B requirement to run a sealed subset of the current 28 first.

The important state transition is one-way:

```text
allocation manifest sealed
  → synthetic fixtures finalized
  → calibration subset opened and used
  → Phase A reviewed/frozen
  → holdout subset opened exactly once for clean Phase B run
  → any rule/fixture change declares the run invalid and starts a new evidence cycle
```

This makes “unseen until clean run” inspectable even though historical notes exist; it does not claim the identities or preliminary notes were unknowable.

### E8: Configuration dependencies exposed for Challenge

Several dimensions are independent in the table but create pairwise dependencies:

- D2 Alt C (observed-type first) with D1 Alt A requires adding an observation-only path to the existing CLI; with D1 Alt B/C it can remain orchestration around the same fetched bytes.
- D4 Alt B (occurrence ledger) supports every D3 grammar; D4 Alt C (line result) needs an additional span model when a line can hold multiple links.
- D5 Alt C/D can bind exact approval; their safety still depends on canonical serialization, a catalog baseline, evidence freshness, and explicit approved IDs.
- D6 exact-byte parity is compatible with the frozen runtime paths because Claude ignores `name` in command front matter; it is not proof of completeness or literal Codex routing by itself.
- D7 Alt B/C/D is compatible with observed evidence; D7 Alt A lacks an identified authority for positive editorial facts.
- D8 Alt B/C and the Phase B clean run require the holdout allocation artifact to be created before any real calibration result is used, not merely before permanent tests are committed.

These dependencies are inputs to Challenge, not eliminations in Extract.

## Extract Decisions

1. **ED1 — Carry a two-layer evidence model into Challenge.** The preview payload and approval envelope must be analyzed separately to avoid self-hash circularity and to distinguish byte binding from human authority; this preserves all D5 alternatives for comparison.
2. **ED2 — Add the exact-byte frozen-path configuration to the challenge set.** Official loader contracts show a common `name` + `description` complete document can occupy `.claude/commands/*.md` and `.agents/skills/*/SKILL.md` unchanged; exact-copy feasibility no longer requires a path amendment.
3. **ED3 — Treat type reconciliation as interpretation of one target-bound observation where possible.** Challenge will compare declared, observed-first, all-expectations, and unresolved paths without assuming three network fetches or weakening GD1.
4. **ED4 — Preserve dual accounting and procedural holdout semantics.** Every challenged configuration must explain both occurrence/candidate totals and the one-way allocation/calibration/holdout transition established by GD2/GD3.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Four classifier architectures can share one target-bound observation flow; observed-type reconciliation can reuse the same fetched bytes. | Challenge identity conflicts, type ambiguity, rate/partial failure, and the temptation to duplicate classifier logic. |
| Occurrence and candidate ledgers solve different problems and permit resumable/idempotent evidence without silent loss. | Challenge multi-link lines, malformed/private/message URLs, duplicates, aliases, and whole-source versus partial-failure behavior. |
| Exact approval is an immutable preview payload plus an authority envelope; embedded approval has a self-hash trap unless payload/envelope are separated. | Challenge stale baselines, changed proposals, missing approved IDs, partial apply, and rerun semantics across D5 A–D. |
| Exact-byte copies are compatible with the frozen Claude-command/Codex-skill paths because their front-matter common subset overlaps. | Prove standalone completeness, set parity, literal discovery, argument receipt, and behavioral hard stops in both fresh runtimes. |
| Editorial gates form a mixed authority matrix; no source supports full automated positive admission. | Challenge evidence sufficiency and owner workload for D7 B–D without automated overclaiming. |
| A sealed present holdout is procedural no-tuning evidence; source split/random-late/future-batch variants have different isolation properties. | Challenge recognizable-case leakage, preliminary notes, allocation strata, and invalidation after post-holdout rule changes. |
| New discoveries: exact-byte parity at the frozen paths; approval self-hash circularity; same-bytes type reconciliation; completeness and parity are independent. | Pairwise consistency checks must determine which configurations survive; Extract makes no implementation recommendation. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] Hypothesis tested? (H2 data flow, H3 accounting/approval binding, and H4 isolation were structurally tested.)
- [x] Counter-evidence sought? (self-hash circularity, plain sorted JSON versus named canonicalization, identical-thin-copy false parity, line-ledger conflation, and source/notes leakage.)
- [x] Metacognitive check completed? (Exact-byte compatibility at the frozen paths and the payload/envelope split were new, actionable discoveries.)

Stage complete: YES
→ User decision: Close Extract; proceed to Challenge after Coordinator authorization.

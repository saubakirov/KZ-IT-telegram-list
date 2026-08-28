# RES — 20260828-201343__catalog_intake_commands: Exact intake contract and clean evaluation boundary

> **Date**: 2026-08-28
> **Author**: saubakirov
> **Status**: 🔬 RES — Iteration 2 complete; sufficient for TS
> **Parent HL**: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> **Mode**: Pipeline · deep

---

## Research Context

Iteration 2 closed the specification-shaping questions left by Iteration 1 without inspecting the raw holdout: exact Telegram source grammar, canonical preview and owner-authority boundaries, idempotent apply and crash recovery, complete synchronized Claude/Codex command copies, the smallest safe reuse seam around the existing classifier, content-derived calibration/holdout allocation, and durable adoption of the owner-supplied candidate batch. Adversarial testing materially narrowed the initial configuration: username subdomains, fragments, queries, parent extraction, discretionary case IDs, unmarked mixed-state recovery, and location-relative command references were all removed from the selected family.

## Briefing

The predecessor decisions, Iteration 2 hypotheses, scope, and stage plan are in [1_briefing.md](1_briefing.md). The dimensional evidence is in [2_gather.md](2_gather.md), the configuration space and representative flows are in [3_extract.md](3_extract.md), and the pairwise falsification and final selection are in [4_challenge.md](4_challenge.md).

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| I2-D1 | Select **I2-C1R**, the refined bounded C2+C3 family, as the implementation/specification basis. | It is the smallest family that preserves the reviewed classifier, complete occurrence accounting, physical owner-authority separation, exact-copy A1, and a clean evaluation boundary. The broader grammar, shared-module, and signature-heavy variants add proof surface without closing a demonstrated correctness gap. |
| I2-D2 | Accept candidate identity only from `https://t.me/HANDLE`, `https://telegram.me/HANDLE`, or `https://telegram.dog/HANDLE`, with an optional trailing slash. | Fixed root domains preserve documented useful aliases while avoiding username-subdomain exceptions, deep-link actions, parent inference, and query/fragment ambiguity. Scheme/host comparison is case-insensitive; handle source spelling is retained and grouping is case-insensitive. |
| I2-D3 | Use explicit `/kz-add --text <text>` and `/kz-add --file <UTF-8 path>` source forms, and record raw Telegram-like spans before validation or grouping. | Exactly one mode removes path/text ambiguity and still covers one URL, pasted lists/Markdown, and files. A leftmost-longest raw-source scanner with lossless wrapper suffix accounting meets the owner's occurrence-accounting goal without pretending to implement CommonMark rendering semantics. |
| I2-D4 | Treat URL component parsing only as splitting; apply closed pre- and post-parse validation and never salvage a valid prefix from an invalid token. | Python explicitly warns that `urlsplit()`/`urlparse()` are not validators. User-info, ports, percent encoding, backslashes, controls, dot segments, extra paths, queries, fragments, `http`, `tg:`, `www`, subdomains, and malformed/spoofed authorities remain explicit non-candidate occurrences. |
| I2-D5 | Bind preview meaning with the closed `kz-canonical-json/v1` profile, one fixed action vector, complete controlled-path before/expected-after hashes, and renderer-completeness tests. | The admitted schema needs no floats or non-ASCII object keys, so a restricted JCS-compatible domain is smaller than a generic RFC 8785 implementation. Duplicate keys, lexical `-0`, floats/exponents, unsafe integers, invalid Unicode, unknown fields, non-deterministic arrays, and hidden significant fields must be rejected. |
| I2-D6 | Keep preview payload, owner approval envelope, pending execution marker, and apply receipt as separate immutable objects. | A payload digest does not prove owner authority; an envelope cannot select a subset without changing expected post bytes; and mutating an envelope into a receipt destroys the authority record. Every owner edit, retry, material re-observation, or baseline change creates a successor payload and new approval. |
| I2-D7 | Permit an exact all-A no-op; permit mixed B/A recovery only with a durable payload/envelope/execution-bound pending marker; stop on any X or unmarked mixture. | Exact post-state idempotency is stronger than “handle exists.” A mixed state without a marker cannot distinguish process crash from intentional manual revert and could overwrite owner work. |
| I2-D8 | Reuse one immutable fetched preview through three calls to the unchanged pure typed classifier and accept a type only under the exact one-verified/two-matching-type-mismatch invariant. | A synthetic same-HTML probe was pure and repeatable. This C2 seam discovers type without a second classifier or a stats-wide module extraction; zero/multiple verified, target disagreement, or unexpected reason tuples remain unresolved. |
| I2-D9 | Author complete location-neutral `.claude/commands/kz-*.md` bodies and copy their bytes exactly to `.agents/skills/<name>/SKILL.md`; prove inventory, completeness, parity, loader validity, and runtime behavior independently. | Current relative Markdown links resolve differently from the two runtime depths, so byte equality alone can certify behaviorally different files. Literal repository-root paths, common `name`/`description` front matter, product-neutral owner-invocation gates, formal completeness review, and fresh-product evidence are all required. |
| I2-D10 | Allocate **8 calibration / 20 holdout** cases with content-derived keys from sealed source occurrence bytes, not discretionary IDs. | The initial opaque-ID 20/8 design was gameable and left too little untouched final material. Synthetic/classifier fixtures carry most mechanical calibration, while the larger sealed holdout better serves the owner's requested clean final run. |
| I2-D11 | Seal exact matching input bytes before Phase A, reveal and recompute after Phase A freeze, then adopt exact source snapshots plus a canonical occurrence manifest as task evidence. | A hash alone cannot reconstruct an untracked file after drift. Sealing preserves the promised corpus without modifying unrelated work; post-reveal adoption preserves every occurrence while keeping preliminary notes as source rather than catalog fact. |

## Selected and Fallback Configurations

| Order | Configuration | Use condition | Distinguishing cost |
|------:|---------------|---------------|---------------------|
| 1 | **I2-C1R — refined bounded C2+C3** | Default TS basis | Closed root grammar; restricted canonical profile; C2 fetch-once seam; separate envelope; location-neutral Claude-source exact copies; content-derived 8/20 seal. |
| 2 | I2-C2R — RFC 8785/neutral-source | Use only if the restricted profile cannot stay closed or a real cross-language consumer requires generic JCS | Adds reviewed JCS dependency/conformance and a third source lifecycle; no current benefit was demonstrated. |
| 3 | I2-C3R — shared observation module | Use only if the minimal fetch seam cannot preserve current classifier/stats semantics | Requires full `/kz-stats` equivalence across parser, identity, type, retry, summary, mutation, archive, and historical decoy behavior. |
| 4 | I2-C4R — single-host/manual-type | Conservative fail-closed fallback if three-type reconciliation fails | Rejects documented aliases and transfers observable type work to owner/curator; safer but less useful. |

I2-C5 was eliminated because message/story/action links do not prove owner intent to catalog their parent, and its Markdown/shared-module expansion is unnecessary for root-link/list/file intake. I2-C6 was eliminated because no owner-controlled signing-key ceremony exists; an agent-generated signature would add bytes, not authority.

## Specification and Implementation Implications

The Coordinator can now write a bounded TS without inventing architecture. It should translate, not reopen, these research contracts:

1. **Source and occurrence contract:** exact `--text`/`--file` grammar; raw leftmost-longest byte spans; wrapper/suffix accounting; accepted fixed HTTPS roots; closed disposition taxonomy; occurrence-before-case grouping; no parent salvage.
2. **Observation contract:** one fetch/retry seam returning immutable bytes or a stable transport result; all three typed calls over the same bytes; exact aggregation invariant; identity-first fact exposure; unchanged stats/decoy/conflict behavior.
3. **Evidence contract:** closed `kz-canonical-json/v1` lexical/data/schema rules; deterministic arrays and totals; complete human rendering; fixed actions; sources, occurrences, candidates, observations, editorial evidence, and every controlled path bound in the preview.
4. **Authority and apply contract:** separate payload/envelope/pending marker/receipt; current owner evidence bound to exact digest/action projection; immediate freshness and baseline recheck; staged complete post bytes; all-B apply, all-A no-op, marked mixed recovery, and unmarked/X hard stop.
5. **Command contract:** exact inventory `{kz-add, kz-stats, kz-release}` in both runtime locations; common valid front matter; complete location-neutral bodies; one-way explicit sync/check; no counterpart or external runbook needed to operate; explicit-owner literal command gate.
6. **Evaluation contract:** pre-Phase-A source seal and allocation by a non-Executor; synthetic plus eight disclosed calibration cases only in Phase A; reveal/recompute after freeze; one clean twenty-case run; any holdout-driven durable change invalidates the clean result and requires a new independent evaluation set.
7. **Provenance contract:** preserve the unrelated originals; stop on initial digest mismatch; retain exact sealed bytes; after reveal and phase authority, adopt source snapshots and a lossless occurrence manifest before candidate-level owner admission.

These implications define behavior and proof obligations, not a file budget or implementation prescription. They remain compatible with the frozen HL and owner-approved A1.

## Holdout Sealing and Allocation Prerequisites

Before Phase A implementation, a non-Executor authority must perform this fail-closed sequence without running the new parser and without exposing raw holdout material to the Phase A Executor:

1. Verify the current two input byte sequences against the predecessor-recorded SHA-256 commitments. If either differs, stop before allocation and request explicit owner re-baselining.
2. Copy the exact matching bytes to a Coordinator-controlled sealed location outside the Phase A worktree and context, leaving the originals untouched.
3. Resolve the already-known one-candidate overlap and derive each case from its source occurrences:

   ```text
   occurrence_key := SHA256(source_sha256 || byte_start || byte_end || raw_span_sha256)
   case_material  := canonical sorted occurrence_key list for one unique candidate
   case_key       := SHA256("kz-intake-case-v1\0" || case_material)
   score          := SHA256("kz-intake-split-v1\0" || case_key)
   ```

4. Assign the eight lowest scores to calibration and the remaining twenty to holdout. Publish only the whole-manifest digest, method/version, source digests, totals, and overlap count—not per-case hashes that enable dictionary recovery.
5. Give Phase A only synthetic cases and the eight calibration cases in a dedicated worktree/minimal-context task. Do not expose hidden paths, IDs, source history, preliminary outcomes, or raw holdout bytes.
6. After Phase A behavior, fixtures, prompts, and copies freeze, have a non-Executor recompute and reveal the full manifest, verify the commitment and 8/20 partition, audit Phase A for leakage, and supply the twenty cases once to the clean runner.
7. If a holdout result changes any parser rule, classifier composition, command instruction, inclusion rule, permanent fixture, or expected outcome, relabel that result calibration and obtain a new independent evaluation set for the changed design.

This supports an auditable **precommitted no-tuning holdout**. It does not claim that raw identities are cryptographically unreadable to every human or process on the workstation.

## Fresh Runtime Empirical Gates

Research established feasibility, not the final runtime fact. A1 remains gated after implementation by evidence from one clean disposable worktree/archive at the exact implementation SHA, excluding untracked source/holdout files:

- Run static inventory, front-matter, structural-completeness, forbidden-counterpart-reference, and byte-parity checks first.
- In one genuinely fresh nonpersistent Claude session with tools disabled, invoke literal `/kz-add --text <synthetic reserved-action sentinel>` and routing-only `/kz-stats` and `/kz-release` prompts. Capture argument receipt, loaded local path/hash, preview/no-mutation behavior, owner triage, and pre-tag/push hard stops.
- In one genuinely fresh non-forked Codex Desktop task at the same SHA, use plan/read-only mode and the same three literal command smokes. `$kz-add` may diagnose official skill selection, but it does not satisfy the literal `/kz-add` contract.
- Bind each transcript to static file hashes plus before/after Git status and controlled-path hashes. A model merely echoing a requested path is insufficient; evidence must show local skill selection/read and command-specific behavior.
- If the Desktop/runtime surface cannot expose the literal route and loaded-copy evidence, A1 remains blocked. The current Codex CLI access denial is a bounded harness limitation, not permission to waive the gate.

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which URL forms become candidates? | Closed | Only the three fixed HTTPS root domains with one valid handle and optional trailing slash; all other Telegram-like forms remain explicit non-candidate occurrences. |
| Q2 | Which source direction preserves A1 with the least lifecycle overhead? | Closed | Complete location-neutral Claude files are the authoring sources; an explicit sync copies exact bytes to complete Codex skills and `--check` verifies both inventories and parity. |
| Q3 | What binds preview meaning and owner authority? | Closed | Closed `kz-canonical-json/v1` preview bytes plus a physically separate current owner envelope over the exact digest/action projection, followed by separate execution marker and receipt. |
| Q4 | How is idempotency distinguished from stale or partial state? | Closed | Controlled-path B/A/X classification: all B applies, all A is exact no-op, marked mixed B/A may recover, and unmarked mixed or any X stops. |
| Q5 | Does safe observed type require a shared observation module? | Closed | No. One fetch plus three unchanged typed classifier calls is sufficient under the strict aggregation invariant; C4 is fallback only if the minimal seam fails evidence. |
| Q6 | How can the current corpus calibrate and test without holdout tuning? | Closed procedurally | Content-derived non-Executor allocation, exact source sealing, eight calibration/twenty holdout, minimal Phase A access, post-freeze reveal, and invalidation on holdout-driven change. |
| Q7 | How is the untracked candidate batch adopted durably? | Closed | Verify/seal before Phase A; after reveal and phase authority, adopt exact raw snapshots and a canonical lossless occurrence manifest without modifying the unrelated originals or promoting preliminary claims. |
| Q8 | Do fresh Claude and Codex runtimes satisfy literal discovery, arguments, and hard stops? | Empirical execution gate | The evidence protocol is closed, but the result can exist only after the commands are implemented at an exact SHA. Failure blocks A1; it does not require more pre-TS research. |

## Hypotheses (from HL §10 and Iteration 2)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Cross-agent literal behavior can avoid copied bodies | refuted/superseded by A1 | Not reopened | Owner-approved A1 requires complete synchronized runtime copies. |
| H2 | Existing classifier can expose arbitrary non-mutating candidate evidence while preserving safety | supported with conditions after Iteration 1 | 🟢 Supported; implementation equivalence gate remains | Current classifier is pure/repeatable for same HTML. Fetch once, call it for all three declared types, require exactly one verified and two target-bound matching type mismatches; otherwise unresolved. |
| H3 | One grammar can cover one/many/file with idempotent complete accounting | supported with conditions after Iteration 1 | 🟢 Supported | Explicit text/file modes, raw occurrence ledger, closed root grammar, fixed action payload, B/A/X state vector, exact no-op, and marker-bound recovery close the ambiguity. |
| H4 | The current 28 can support calibration/holdout without automated editorial overclaim | supported procedurally after Iteration 1 | 🟢 Supported procedurally | Content-derived 8/20 split, exact source seal, calibration-only Phase A, post-freeze reveal, and owner authority separate evaluation from catalog admission. |
| A1 | Complete self-contained synchronized Claude/Codex copies are feasible at frozen paths | approved constraint | 🟢 Supported with mandatory execution gate | Common front matter and location-neutral full bodies permit byte equality; current relative links proved why parity, completeness, and fresh literal behavior are separate gates. |
| I2-H1 | A bounded documented public-peer grammar can be loss-accountable | testing | 🟢 Supported with refinements | Fixed root aliases survive; subdomain, query, fragment, parent extraction, and permissive normalization do not. |
| I2-H2 | Canonical preview plus separate approval can bind significant data and authority | testing | 🟢 Supported with conditions | Closed lexical/schema/renderer contract, fixed actions, all-path state, current authority evidence, separate marker, and receipt are required. |
| I2-H3 | One complete source direction plus fresh sessions can prove cross-agent behavior | testing | 🟢 Feasible; fresh behavior pending implementation | Claude-source exact copying survives after path neutrality; runtime evidence is specified but cannot precede implementation. |
| I2-H4 | Allocation can remain sealed without leaking raw holdout into implementation | testing | 🟢 Supported procedurally | Content-derived scoring removes label gaming; exact sealed bytes and minimal task/worktree access make the no-tuning claim auditable. |
| I2-H5 | C2 orchestration is smaller than C4 without losing safety | testing | 🟢 Supported | Same-byte three-type classification closes the type gap; C4 adds stats-wide equivalence work without a present correctness benefit. |

## Open Risks and Required Evidence

| Risk | Consequence | Required control/evidence |
|------|-------------|---------------------------|
| Scanner implementation becomes a permissive regex or silently salvages prefixes | Invite/action/spoofed forms may become candidates | Adversarial extraction/validation vectors across wrappers, punctuation, controls, authorities, queries, nested URLs, and extra paths. |
| Restricted canonical profile admits values or fields outside its proof domain | Same visible proposal may hash or render with different semantics | Pair-preserving lexical parser, recursive closed schema, conformance vectors, deterministic arrays/totals, renderer-completeness audit. |
| Fetch seam changes stats behavior | Intake safety improves while existing catalog validation regresses | Preserve unchanged classifier; reproduce stats summary/retry/mutation/archive behavior and all historical identity/decoy fixtures. |
| Same command bytes retain location-dependent behavior or incomplete logic | Parity check gives false assurance | Root-relative textual paths, forbidden counterpart/runtime-relative links, formal standalone review, fresh local-path/hash behavior. |
| Multi-path crash is mistaken for authorized recovery | Intentional owner revert may be overwritten | Durable pending marker before first replacement; exact staged A bytes; unmarked mixed/X hard stop. |
| Source bytes drift before sealing | Promised 28-case corpus cannot be reproduced | Initial digest gate and exact sealed copies; mismatch requires owner re-baselining before allocation. |
| Phase A context or holdout result influences permanent rules | Clean-run claim is invalid | Calibration-only minimal task/worktree, leakage audit, one-way reveal, invalidation and new independent set after any holdout-driven change. |
| Fresh Codex Desktop cannot prove literal routing or loaded local body | A1 behavior remains unverified despite static parity | Treat as a release-blocking empirical gate; do not substitute `$skill`, current contextualized session, or static hashes. |

## HL Update Recommendations

> The Researcher classifies and does not apply. All Iteration 2 findings fit the free research/detail sections and the already-approved A1; no frozen declarative claim needs re-freezing.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 Current State | Record that the current Claude `kz-stats`/`kz-release` bodies contain runtime-depth-relative links that cannot remain behaviorally equivalent when copied byte-identically to Codex, and that no current `kz-*` Codex inventory exists. | Gather G7; Challenge C7 |
| R2 | §7.2 Knowledge Citations / Research-derived constraints | Replace the open “Telegram link” boundary with the selected fixed-root grammar, explicit text/file source modes, occurrence-before-grouping, lossless scanner, and non-candidate disposition requirement. | Extract E1–E2; Challenge C1–C2; I2-D2–I2-D4 |
| R3 | §7.2 Knowledge Citations / Research-derived constraints | Record `kz-canonical-json/v1`, fixed actions, all-controlled-path B/A hashes, physically separate approval/pending/receipt artifacts, exact all-A no-op, and marker-bound mixed recovery. | Extract E3–E5; Challenge C4–C6; I2-D5–I2-D7 |
| R4 | §8 Dependencies | Make pre-Phase-A exact source sealing and content-derived 8/20 allocation a dependency; make fresh exact-SHA Claude/Codex literal-runtime evidence a separate post-implementation dependency. | Challenge C8–C10; I2-D9–I2-D11 |
| R5 | §9 Risks | Add permissive scanner salvage, canonical lexical/renderer drift, location-dependent exact copies, unmarked partial recovery, allocator gaming, input loss/drift, inherited-context leakage, and holdout-driven invalidation. | Challenge incompatible pairs; C1–C10 |
| R6 | §10 RESEARCH Case | Mark H2/H3/H4 and A1 feasibility supported under I2-C1R, close Iteration 1 Q1–Q7, record C2R/C3R/C4R fallbacks, and distinguish implementation evidence gates from further research. | Challenge C12; this RES Decisions and Open Questions |
| R7 | §11 Strategic Insights | Refine the existing clean-final-run insight: use eight real calibration cases and keep twenty sealed; a holdout-driven permanent change invalidates the result even when the change is an obvious correction. | Challenge C9; owner direction captured in predecessor Briefing |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** I2-C1R implements the approved `/kz-add` scope, classifier reuse, occurrence accounting, explicit owner authority, complete-copy A1, and 28-candidate calibration/holdout contract. The refinements narrow grammar and proof mechanics without changing §§1 or 3–7.

## Fact Candidates

**No Fact Candidates.** Iteration 2 received no new human-only factual report. The owner directions about complete copies, value-first validation, adding all qualified candidates, and preserving a clean final set are already captured in the frozen A1 and HL §11; all new findings are reproducible from repository files, synthetic probes, or external primary sources.

## Strategic Insights (Research)

**No new strategic insights.** Iteration 2 operationalized the owner-sourced insights already recorded in Iteration 1; its additional conclusions are agent-discoverable technical findings and therefore do not pass the human-only Strategic Insight test.

## Findings Map

```text
OWNER SOURCE
   │
   ├─ seal exact bytes before Phase A ── content-derived case keys
   │                                      ├─ 8 calibration → Phase A
   │                                      └─ 20 holdout ───→ reveal once after freeze
   │
   └─ --text / --file
          │ raw leftmost-longest occurrence ledger
          ├─ fixed HTTPS root peer ── case-folded candidate grouping
          │                              │
          │                              ├─ collision check
          │                              └─ fetch once → unchanged classifier × 3
          │                                              ├─ exact one type → evidence
          │                                              └─ any inconsistency → unresolved
          └─ invite/action/message/spoof/malformed → explicit non-candidate outcome

EVIDENCE / AUTHORITY / EXECUTION
   closed canonical preview (fixed actions + B/A path vector)
          │ SHA-256
          ▼
   separate current owner envelope
          │ all B + freshness pass
          ▼
   staged exact A bytes + pending marker
          ├─ all A → exact no-op / completed receipt
          ├─ marked B/A → exact recovery
          └─ unmarked B/A or X → hard stop

CROSS-AGENT COMMAND ASSURANCE
   complete location-neutral Claude source
          └─ exact bytes → complete Codex skill
              inventory ≠ parity ≠ completeness ≠ fresh literal runtime proof

Root causes removed:
  permissive first-path parsing · subset approval · hidden-field drift
  unmarked crash recovery · location-relative exact copies · gameable allocation IDs
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H2 (supported), H3 (supported), H4 (supported procedurally), A1 feasibility (supported with execution gate), I2-H1 (supported with refinements), I2-H2 (supported with conditions), I2-H3 (feasible with execution gate), I2-H4 (supported procedurally), I2-H5 (supported)
- **Hypotheses deferred:** None. Fresh runtime behavior, source sealing/allocation, implementation conformance, and the clean holdout run are empirical phase gates, not untested research hypotheses.
- **Gaps discovered:** No specification-level research gap. Remaining work is to execute the predeclared source-seal/allocation gate, implement and test I2-C1R, obtain fresh Claude/Codex evidence, and run the sealed holdout under owner authority.
- **Superseded decisions:** I2-CD1 refines I2-ED1's original I2-C1 grammar; I2-CD3 removes unmarked mixed-state recovery from E5; I2-CD5 falsifies copying the current relative-link bodies as-is; I2-CD6 supersedes I2-ED6's discretionary opaque IDs and 20/8 split with content-derived keys and 8/20.

### Open Threads (for next iteration)

**No open research threads.** The empirical gates listed above belong in the TS/phased execution and review evidence. A third research iteration would repeat known questions unless one of the fallback triggers occurs during implementation.

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — no additional pre-TS investigation is justified; use I2-C2R, I2-C3R, or I2-C4R only when their named implementation trigger is observed.
- [ ] **BLOCKED** — no research blocker; raw holdout access remains intentionally unavailable until the recorded reveal gate.

> Coordinator decides whether to continue or proceed. Researcher recommends but does not decide.

## Conclusion

Iteration 2 turns Iteration 1's feasible families into one falsified and bounded recommendation: I2-C1R. Research proved that safe intake does not require a Telegram deep-link client, a second classifier, a shared-module refactor, generic JCS, cryptographic owner signing, or a third command source; it does require a closed root grammar, lossless occurrence accounting, exact classifier reconciliation, a closed canonical payload, separate owner and execution artifacts, marker-bound recovery, location-neutral complete copies, fresh literal runtime proof, and content-derived 8/20 sealing. The most important counter-findings were not confirmations: current exact copies would resolve relative links differently, opaque allocation IDs were gameable, the initial 20/8 split weakened the requested clean run, and mixed recovery without a marker could overwrite intentional work. The self-critique is explicit: this Researcher did not inspect raw holdout candidates, allocate them, implement commands, or claim fresh Codex behavior; those are now precise execution gates rather than unresolved research. Research is sufficient for `/tfw-plan` to produce the TS without re-freezing the HL.

---

*RES — 20260828-201343__catalog_intake_commands: Exact intake contract and clean evaluation boundary | 2026-08-28*

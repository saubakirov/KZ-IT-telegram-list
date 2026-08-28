# Gather — "What do we NOT know?"
> **Mindset:** Explorer. The stage maps the independent choices and records constraints; it does not select a final configuration.
> **Test:** The dimensions below keep classifier reuse, source accounting, approval authority, agent parity, editorial judgment, and evaluation isolation separate instead of hiding them inside one command.
> Parent: [HL-20260828-201343__catalog_intake_commands](../../HL-20260828-201343__catalog_intake_commands.md)
> Goal: Establish a safe `/kz-add <source>` operation that accounts for every candidate before mutation and is available as complete, synchronized, self-contained command copies in Claude Code and Codex.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: candidate-classifier boundary | Extend the present CLI so `--handle` accepts non-catalog handles | Add an intake orchestrator that imports the present pure classifier/retry functions | Extract the observation functions into a shared project module used by both catalog sweep and intake | Implement a second intake-specific classifier and prove behavior equivalence |
| D2: candidate type establishment | Require the source or curator to declare group/channel/bot before probing | Probe all supported requested types and reconcile the results | Add an observed-type-only discovery pass, then call the typed classifier | Treat type as unresolved evidence until owner triage supplies it |
| D3: source grammar | One positional value, heuristically interpreted as URL text or an existing path | Explicit `--file PATH` plus inline URL-text mode | Repeatable typed inputs such as `--url`, `--file`, and `--stdin` | Generic argument-file expansion such as `argparse` `@file` plus positional URLs |
| D4: loss and duplicate accounting | Emit one result per unique normalized handle | Emit an occurrence ledger first, then group occurrences into unique candidates | Emit one result per source line, including lines without candidates | Reject the entire source when any occurrence is malformed or duplicated |
| D5: approval binding | A conversational owner “yes” after preview | An `--owner-approved` boolean at apply time | A canonical manifest digest plus explicitly approved candidate IDs | A separately stored approval file containing the reviewed manifest digest and exact set |
| D6: full-copy source and parity | One project-owned complete command source rendered into both runtime locations | Claude command is the authoring source and generates a complete Codex skill | Codex skill is the authoring source and generates a complete Claude command | Independently authored complete runtime files checked through normalized semantic parity |
| D7: editorial allocation | Automated inclusion decision for every gate | Automation decides observable/structural failures; owner decides positive editorial fit | Automation supplies evidence only; owner decides every inclusion gate | Independent agent/editorial review followed by exact owner approval |
| D8: calibration and holdout | Random split after implementation | Predeclared stratified split before implementation and fixture authoring | Split by supplied source (discovery backlog versus six-link note) | Use the present corpus for calibration and reserve a future independently sourced batch for generalization |

## Findings

### G1: The classifier already has a reusable observation seam, but the current CLI does not expose it to arbitrary candidates

`scripts/validate_links.py` separates URL normalization (`handle_from_url`, line 123), preview-type observation (`observed_preview_type`, line 137), pure HTML classification (`classify_response`, line 176), and network retry (`check_link_with_retry`, line 276) from catalog mutation (`apply_updates`, line 405) and archival (`archive_entry`, line 436). The arbitrary-candidate limitation is in selection: `--handle` filters `collect_live_entries(data)` and therefore accepts only an already-live catalog handle. H2 is technically plausible through D1 Alt A, B, or C without weakening mutation authority.

The classifier is not type-free. `classify_response` requires one of `groups`, `channels`, or `bots` and deliberately returns mismatch/ambiguity states when requested and observed identity/type evidence disagree. D2 must therefore remain an explicit decision; “probe any URL” does not by itself establish what typed catalog section can receive the candidate.

Counter-evidence comes from the existing Phase C review history. The first implementation treated descriptive links as identity evidence and could bind an observation to the wrong handle; the correction narrowed authoritative identity sources and added decoy/conflict tests in `tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py` and `tasks/TFW-4__showcase_reorg/phase-c/REVIEW__phase-c__pipeline_tooling.md`. A second classifier or parsing console text would have to rediscover that safety proof. The historical failure makes shared function behavior—not similar output—the relevant H2 parity target.

### G2: One source grammar is feasible only if source decoding and occurrence accounting are separate layers

Python's standard [`argparse`](https://docs.python.org/3/library/argparse.html) supports positional arguments and file-oriented argument expansion, but its `fromfile_prefix_chars` facility treats file contents as arguments (one argument per line by default), not as Markdown or arbitrary pasted text. It therefore does not account for multiple URLs on one line, surrounding Markdown punctuation, repeated URL forms, or malformed Telegram-like tokens. This is counter-evidence to treating generic `@file` expansion as the complete H3 parser.

All D3 alternatives can feed one common text extractor, but D4 changes the meaning of “complete.” Normalizing and deduplicating first loses the distinction between two occurrences of the same handle, while line-only results cannot distinguish two URLs on one line. A loss-accounting representation needs stable source-locator and occurrence identity before candidate grouping: raw token/span, parse disposition, normalized handle when available, and the candidate ID to which a valid occurrence belongs. Candidate-level probing and disposition can then be idempotent without making duplicate occurrences disappear.

The two supplied inputs confirm the edge rather than just the happy path. `C:/Users/c0rpa/obsidian/c0rp/c0rp/Untitled 1.md` (SHA-256 `1fdc1286cb8c5ba1f04507c163a60b6b5171bc3c53123af1debb753b1d29a162`) contains six URL occurrences. The read-only `tasks/CANDIDATES-2026-08-28.md` (SHA-256 `ffeb4b3903ae4a4eda2ee2676f31887552cc6b510ecedd65f8830e86fbef6ebb`) contains 23 add candidates. `aws_kz` overlaps, yielding 29 source occurrences but 28 unique handles. Either count can be correct only when its level is named.

### G3: Preview/apply safety is a state-binding problem, not merely a prompt wording problem

The current catalog schema has no candidate or approval record. `apply_updates` also assumes a handle is already in the live catalog, so an intake apply path must not smuggle additions through that updater. A non-mutating evidence record can stay outside `data/communities.json`; mutation should consume only an exact reviewed candidate set and then run the existing schema/generation gates.

D5 alternatives differ under drift and partial failure. A conversational “yes” or boolean flag proves that approval happened but not which normalized occurrences, evidence bytes, descriptions, category choices, or catalog baseline were approved. A versioned, deterministically serialized manifest can bind: source digest; occurrence ledger; unique candidates; observation timestamps and outcomes; proposed localized fields; catalog baseline digest; exact approved IDs; and the digest recalculated immediately before apply. This stage does not yet choose between embedding approval in that manifest or storing a separate approval artifact, but H3's “exact set” cannot be tested without such a binding.

### G4: Complete copies are feasible, yet no inspected local project proves A1 parity

Official Codex guidance describes a skill as a directory containing `SKILL.md`, with optional scripts, references, and assets; Codex loads the complete `SKILL.md` when the skill is selected, and repository skills are discovered under `.agents/skills` ([OpenAI, “Build skills”](https://learn.chatgpt.com/docs/build-skills)). Official Claude Code guidance says user-defined slash commands have converged with skills, command input begins with `/`, trailing text becomes arguments, and `/reload-skills` rescans command/skill directories ([Anthropic, “Commands”](https://code.claude.com/docs/en/commands)). These are two runtime loaders with different discovery surfaces, so file presence alone is not behavior parity. Codex's documented explicit skill invocation is through its skill UI or `$` reference; literal project `/kz-*` routing also needs an `AGENTS.md` contract and an actual runtime smoke test rather than an unsupported product claim.

The current `.tfw/adapters/codex/skills` arrangement and the comparable `D:/projects/research/ai-first-devices` project use thin Codex adapters that load a canonical workflow, Claude command, or runbook. For example, that project's deploy skill explicitly says the skill “holds no deploy logic.” Those patterns are incompatible with frozen A1 even though they are maintainable. The older `D:/projects/research/local-network/.agents/skills/source-command-tfw-plan/SKILL.md` demonstrates that a complete body can be copied into a Codex skill, but its wrapper differs from its Claude source and it has no current enforced parity gate. It is evidence of feasibility and counter-evidence to unmanaged duplication.

All D6 alternatives must therefore be evaluated on three independent properties: each runtime file is complete when read alone; generation/check mode makes drift reproducible and visible; and Claude/Codex smoke tests prove discovery, argument receipt, hard stops, and material outputs. Exact byte identity may be possible with shared front matter, while normalized body identity may be necessary if loaders require different metadata; loader compatibility must be tested rather than assumed.

### G5: Observable Telegram facts and positive editorial inclusion are different authority classes

The scripts can objectively check URL syntax, public response class, requested/canonical identity signals, observed preview type, exact-handle collision with live/archive data, preview member count, and schema/category membership. They cannot turn a preview into a verified claim about sustained IT focus, Kazakhstan relevance, non-commercial character, quality/spam, community continuity across a renamed alias, or accurate EN/RU/KK editorial descriptions.

The repository mission explicitly prices a false inclusion above a missing entry. D7 Alt A would therefore require evidence beyond what the present classifier or Telegram preview supplies. The other alternatives preserve a human decision somewhere, but differ in owner workload. The useful automation boundary is not “AI versus human”; it is whether a claim is mechanically observable, supported but judgmental, or unresolved. Positive inclusion must remain bound to exact owner approval, while obvious structural failures can be reported fail-closed without inventing editorial facts.

### G6: The required 28-candidate holdout can be procedurally isolated, but it is not globally unseen

The 23-candidate backlog already contains preliminary research outcomes and proposed dispositions. The six-link note also contains recognizable cases that were discussed during planning, and one handle overlaps. Because these materials have now been read to establish corpus shape, no split of the 28 can honestly mean “unknown to every participant.” H4 remains satisfiable under the narrower frozen wording: holdout candidates are selected before implementation and are not used to tune rules, fixtures, or expected outcomes.

Primary evaluation guidance supports that distinction. Scikit-learn's [data-leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) requires splitting before preprocessing or model-choice steps and keeping test data out of fitting decisions. NIST's [agent-evaluation guidance](https://www.nist.gov/caisi/cheating-ai-agent-evaluations/4-practices-detecting-and-preventing-evaluation-cheating) similarly recommends sharing a representative subset while preserving held-out tests and removing leaked evaluation artifacts. For this small deterministic workflow, the translation is procedural: precommit candidate IDs and strata, freeze grammar/gates/fixtures using calibration only, forbid post-hoc rule changes after seeing holdout results, and record any later change as invalidating/restarting the holdout. A future independently sourced batch (D8 Alt D) would be stronger generalization evidence but would not replace the frozen requirement to account for all current 28.

### G7: Catalog schema gates are necessary after approval but insufficient before it

`scripts/validate_schema.py` already rejects case-insensitive duplicate live handles, live/archive collisions, invalid bare-handle syntax, missing required fields, missing group categories, non-integer member counts, and missing EN/RU/KK descriptions. This is the authoritative final structural gate and should not be reimplemented in an intake command.

It does not detect aliases with different handles, topical mismatch, Kazakhstan relevance, commerciality, or description truth. Nor does `data/communities.json` contain a candidate-disposition or alias ledger. Keeping rejected/duplicate/unresolved evidence in a versioned intake artifact avoids expanding the catalog schema merely to remember non-catalog candidates, while the final apply can still prove that only approved qualified entries entered the source of truth.

## Gather Decisions

1. **GD1 — Keep type establishment as a first-class research dimension.** The classifier's required `entry_type` parameter is a newly confirmed precondition; later configurations may not describe H2 as an untyped arbitrary probe without separately resolving D2.
2. **GD2 — Measure completeness at both occurrence and unique-candidate levels.** The verified `29 occurrences → 28 handles` shape means later configurations must expose both levels; this is a research invariant, not a selection among D3/D4 implementations.
3. **GD3 — Interpret the present holdout as precommitted no-tuning evidence, not global blindness.** This keeps H4 honest without changing the frozen 28-candidate contract; a future independent batch remains a separate generalization option.
4. **GD4 — Test A1 through standalone content, reproducible parity, and runtime behavior separately.** No inspected ready project proves all three, so Extract must not collapse them into one “files match” assertion.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H2 has a reusable pure-classifier/retry seam, while arbitrary selection, type establishment, and mutation remain separate choices. | Extract configurations that preserve the historical identity/type/update/archive safety proof without a second classifier. |
| H3 can cover one URL, pasted multi-URL text, and files only when the common extractor records occurrences before normalization/deduplication. | Compare explicit versus heuristic source grammars, malformed-token policy, versioned schemas, and resumable partial failure. |
| Exact approval needs content/baseline binding; a free-form “yes” alone cannot identify the reviewed set. | Compare embedded versus separate approval artifacts and trace the atomic apply/idempotent rerun flow. |
| Complete command bodies are loadable in both agent ecosystems, but local exemplars are either thin or lack enforced parity. | Determine viable complete-copy source arrangements and the format/discovery smoke tests each requires. |
| H4 is procedurally testable with a precommitted no-tuning split, but the current corpus cannot be called globally unseen. | Build multiple calibration/holdout configurations and challenge leakage from prior notes, recognizable cases, and adaptive rules. |
| New discoveries: typed-classifier precondition; 29-versus-28 accounting distinction; no full-copy/parity exemplar; prior notes contaminate a literal “unseen” claim. | Challenge must seek failures rather than silently convert these discoveries into a preferred design. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] Hypothesis tested? (H2, H3, and H4 received preliminary tests.)
- [x] Counter-evidence sought? (historical identity regression, `@file` mismatch, thin/stale adapters, and holdout leakage.)
- [x] Metacognitive check completed? (The four new discoveries above materially change the next-stage configuration space.)

Stage complete: YES
→ User decision: Close Gather; proceed to Extract after Coordinator authorization.

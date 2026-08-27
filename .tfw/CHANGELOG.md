# TFW Changelog

All notable changes to the Trace-First Workflow framework.
Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

Nothing pending.

## [2.0.0-dirty] — 2026-08-27

> **Pre-release.** Tagged locally and not pushed. Cut so the update path can be exercised against real
> projects before `2.0.0` is claimed. Two things are deliberately open at this tag: **TD-182** — the
> shipped Assisted edition still changes status by moving a task folder, which contradicts what this
> release declares, and is deferred to its own task; and TFW-60 is at `PHASES`, not `DONE`, because
> Phase B and Phase C remain. Releasing on a phase boundary is what the frozen contract intends —
> master HL §4 calls each phase *"a vertical, independently releasable slice"* and DoD 13 requires a
> phase to be releasable *"without waiting for a later phase"*. The `-dirty` suffix says the framework
> is usable and the claim is not yet final.

**Two people can now advance two tasks without meeting in the same file.** TFW-60 Phase A. Until this
release every lifecycle transition — create, plan, research, hand off, review, close — rewrote one table in
the root `README.md`. Task separation did not produce file separation: three participants working on three
unrelated tasks still queued behind one Markdown table, and its schema had already drifted (TD-177) while
the documentation build regex-read its columns as an implicit API (TD-81).

### ⚠️ Breaking

**The root Task Board is removed.** It was a required artifact; it no longer exists. Anything that parsed it
will find nothing to parse.

**Live state moved into each task.** `{task}/status.md` is now the only authority for a task's lifecycle,
owner, goal, value and terminal outcome. A transition is one write, inside one task directory.

**The status flow changed shape.** The lifecycle ids are unchanged, but `UNDECLARED` is added for a value a
migration source carried that the vocabulary does not contain. It is never selected by a person, and
normalizing it away is prohibited.

### Added

- **`{task}/status.md`** — the task state carrier. Closed key set, bounded fields, no free-text body, and
  every field has a named reader. Template: `.tfw/templates/status.md`.
- **`{task}/journal/`** — one immutable file per coordination event, named
  `<YYYYMMDD-HHMMSS>__<kind>__<actor>.md`. The filename *is* the event identifier, so nothing allocates one
  and nothing counts. **The actor is part of the name** because it is the only field that separates two
  concurrent writers — `on_behalf_of` names the same accountable person for both, and `via` names the same
  provider for two sessions of one tool. Two participants recording the same kind of event in the same second
  therefore produce two files rather than one; one actor writing twice in a second takes the next actual
  second. The time is read from the system clock and never typed. A written event is never edited; a
  correction is a new event. Entries carry references rather than copied artifact prose, under a **120 code
  point** summary ceiling — measured against 272 commit summaries and 63 review verdicts in this repository,
  where p95 is 83 and p99 is 110. Template: `.tfw/templates/journal_event.md`.
- **Three identity fields on every event** — `actor` (who performed it), `on_behalf_of` (who is accountable,
  always a human handle) and `via` (which tool produced it). An event without `on_behalf_of` is refused:
  there is no such thing as a record nobody answers for. A provider name is never an actor.
- **`team/{handle}.md`** — one profile per participant. Declared attribution, never authentication. The
  machine-to-handle binding lives outside the project tree, because a per-user file that is gitignored is
  still not sync-ignored. Template: `.tfw/templates/team_profile.md`.
  **No agent profile ships in 2.0.0.** The schema admits `type: agent` and the slot is deliberately empty: a
  provider family is not an actor, and what would make an agent profile meaningful — a named principal that
  delegates and answers to someone — is a separate task. Until then there is one accountable participant, and
  which tool produced a record survives in the event's `via` field.
- **`🧩 PHASES`, one new lifecycle id** — a multi-phase task sits here while its phases run.
  Each phase directory carries its own `status.md` on the same closed schema, written by that
  phase's owner, so two phases under two owners are two files and never contend. **The task
  file never summarizes phase state**: a rollup is a second fact that has to agree with the
  phases, which is the synchronization problem the carrier exists to avoid. The index renders
  phase rows beneath their task row — what the retired board's per-phase columns showed.
- **Time is recorded to the second.** `created` and `updated` use `YYYYMMDD-HHMMSS`, the same
  grammar as the identifier, and are read from the system clock rather than composed. At day
  resolution the two fields are routinely identical on a corpus taking several transitions a
  day, and `updated` stops answering the question it exists for. A legacy source that carried
  only a date migrates to that date with a **declared** zero time — `20260819-000000` means
  "this day, time unknown" and is never second-accurate history.
- **A validation gate that reads task-local truth** — `python docs/scripts/gen_index.py --validate` checks
  every task's own state and journal against the closed schema. It is deliberately *not* a check that the
  shared index is current: requiring that would make every task-local transition fail until somebody rewrote
  the aggregate, which is the bottleneck this release removes.
- **`{container}/00-INDEX.md`** — a derived portfolio view, rebuilt by `python docs/scripts/gen_index.py`.
  It declares that it is derived, names its source count and freshness, and reports every unresolved input
  instead of dropping it. It is never authoritative: a workflow acting on a task re-reads that task's
  `status.md` first, and an absent or stale index degrades discovery without changing any task.
- **`tfw.task_containers`** — an ordered list. A task is created in the first entry and resolved by
  searching every entry in order.
- **Clock-derived identifiers** — `YYYYMMDD-HHMMSS__slug`, and **the whole directory name is the
  identifier**. The timestamp alone is not one: two participants offline from each other can reach the same
  second, and only the slug tells them apart. Same second *and* same slug means they created the same task —
  a signal, not a collision. Creating a task reads no counter and no other task directory; if the directory
  already exists, the writer takes a new actual timestamp under a bounded retry, never a reuse, and a clock
  that will not advance fails visibly instead of spinning.
- `docs/scripts/gen_index.py` and `docs/scripts/migrate_board.py`, with tests.

### Changed

- The root `README.md` carries a permanent route to the index and no live task table.
- Lifecycle workflows — `plan`, `research`, `handoff`, `review`, `resume`, `release`, `init` — read and write
  task state instead of the board.
- The status legend moved from the README to `.tfw/glossary.md` § Status Flow, where the vocabulary already
  lived.
- Templates use `{ID}` where they used `{PREFIX}-{N}`: both identifier grammars are readable everywhere.

### Fixed

- **TD-81** — the documentation generator no longer regex-reads board columns. A test now fails if a
  board-shaped table regex is reintroduced into `docs/scripts/`.
- **TD-177** — the board's schema cannot drift, because there is no board.

### Migration

**One setting decides the layout.** `tfw.task_containers` is a list. A new project sets one container. A
project with an existing corpus lists its old container second — that is one value with two entries, not two
supported layouts, and nothing else in the method changes.

```yaml
tfw:
  task_containers: [workspace, tasks]   # create in the first; resolve across all
```

**Nothing existing is renamed, moved or byte-changed.** Run
`python docs/scripts/migrate_board.py` for a dry run and read the accounting; run it with `--apply` to write.
It adds a `status.md` to each task still in flight and captures the board verbatim as
`tasks/BOARD-SNAPSHOT.md`. It opens no existing artifact in write mode and refuses to overwrite anything.

Renaming the old corpus into the new grammar was measured and refused: at this project's own migration the
old identifiers were carried by 7,505 references across 666 files and 271 commit subjects. A trace that needs
a translation table to be read has already lost the property the framework exists to provide.

**Then generate the view, and only then remove the board:**

```
python docs/scripts/migrate_board.py --apply
python docs/scripts/gen_index.py
# now delete the Task Board section from README.md and put the route in its place
```

That order matters. The project must never be without a portfolio view.

**What is not in this release.** Transport — whether a project collaborates through Git or through file
synchronization — is a declared project mode owned by a separate task. Nothing here requires a daemon,
database, lock server, vendor API or MCP host, and nothing here is required for a task to be read or
advanced: with the generator deleted, tasks stay readable and workable and only discovery degrades.

### Also in this release — TFW-55, Foundations

Phase A is the headline, but `2.0.0` is the first tag since `1.3.0` and TFW-55 closed in between. Its
changes reach every project that updates, so they are listed rather than left to be discovered:

- **`.tfw/README.md` is rewritten as the Philosophy of Trace.** It now argues from what a trace is and
  what makes work continuable, instead of describing a process. 187 lines changed.
- **The Project North Star is designated and populated.** `NS1 — Purpose`, `NS2 — Principles` and
  `NS3 — Non-goals` are real sections with citation anchors. TFW-53 shipped the concept with nothing in
  it; a reviewer's Purpose Check now has something to read. Non-goals exist for the first time.
- **`.tfw/glossary.md` gains 50 lines**, including the PV priority entries the North Star introduced.
  This is a 🟡 merge file on update — a project with its own glossary terms must reconcile, not overwrite.
- **The root README is rebuilt and localized.** `README.ru.md` and `README.kk.md` are new, 240 lines each.

**On update:** `.tfw/README.md` is replaced wholesale, `.tfw/glossary.md` needs a merge, and the localized
root READMEs are this repository's own content rather than framework files — an updating project does not
receive them and does not need them.

## [1.3.0] — 2026-08-18

**A failed task can finally be closed as failed.** TFW-53 Phase E, the last phase of the contract work.
The status set could record success, work in flight and waiting — and nothing could record failure, so the
only ways to close a failed task were to lie with `✅ DONE`, misuse `❌ BLOCKED`, or delete the folder. This
project did the third: a whole-tree restore took `README.md` back to a state that had never contained two
rejected tasks' rows, and the failure status they carried disappeared as a side effect of the method. Nobody
decided it, and no rule was broken — which is why this release ships a rule rather than a reminder.

**Why `REJECTED` and not `BLOCKED`.** `❌ BLOCKED` was defined, listed and available at the moment the
rejected task closed, and the coordinator declined it and hand-wrote a token the framework did not have.
`BLOCKED` has 0 occurrences across 46 Task Board rows. The two states are different: blocked is waiting and
resumes; rejected is closed and keeps its trace. `REJECTED` is also the only candidate name carrying a
collision, and it was kept anyway — every alternative (`FAILED`, `CANCELLED`, `ABANDONED`, `DROPPED`)
presupposes the *reason*, and the reason belongs in the board row's description.

### Added
- **`❌ REJECTED` as a terminal task status** — the status set could record success, waiting and work in flight, but never failure, so closing a failed task meant misusing `✅ DONE`, misusing `❌ BLOCKED` (which means waiting) or deleting the folder. Present in `conventions.md` §5 (table and transition diagram, drawn as a side node reachable from any status), `project_config.yaml`, `templates/project_config.yaml`, `glossary.md` `## Status Flow` and the README legend. Terminal — no status follows it. It is a **task status**, distinct from the review verdict `❌ REJECT` and from the HL §12 amendment verdict of the same name; neither of those is terminal (TFW-53/E)
- **`conventions.md` §13 — reverting a result does not revert its trace.** A rejected task's folder and its board row are never deleted: the work may leave the working tree, the record that the work happened stays (TFW-53/E)
- **`conventions.md` §14 anti-pattern — a whole-tree restore reverts the Task Board past a task's failure status.** Restoring every file to an older tree also restores rows to a state that never contained the newer ones, so the loss happens silently and nobody decides it (TFW-53/E)

### Changed
- **`glossary.md` `### Amendment Log`** — one clause separating the HL §12 amendment verdict `❌ REJECTED` from the new terminal task status of the same name. The collision is stated at both ends, so whichever file an agent opens first it learns there are two (TFW-53/E)

### Notes for upgrading projects
- **Additive only.** `/tfw-update` brings one new entry in `tfw.statuses`, one row and one diagram node in `conventions.md` §5, one sentence in §13, one anti-pattern in §14, and two `glossary.md` edits. No status was renamed, no transition redrawn, no template field changed, no file removed. A board that never used `❌ BLOCKED` and never needs `❌ REJECTED` is unaffected.
- **The status also lands in `templates/project_config.yaml`**, so a newly initialised project is *born* with it rather than acquiring it by upgrade.
- **Version note.** `RELEASE.md` §3 lists *"status flow changed"* under MAJOR. This change adds a state and alters no existing one; `docs/scripts/gen_docs.py` parses board rows by regex with no hardcoded status set, and 68 tests pass unchanged. Released as MINOR on the impact test, by owner decision — the same standard applied at 1.1.0, where §3's *"required file removed"* clause also over-classified an additive-in-effect change. **Second occurrence of the same misfire; recorded as tech debt against §3.**

## [1.2.0] — 2026-08-14

**An approved HL becomes a contract, and the reviewer becomes its defender.** Phases A–D of TFW-53 in
one entry. Phase E (rejected-task trace restoration) is independent and not in this release.

**Why it exists.** An inviolable contract with a defender is the precondition for delegation: releasing
a coordinator to run a team of agent sessions is only safe once the goals cannot move and something
checks the result against them. That delegation mode is **TFW-54**, deliberately a separate task —
building both at once splits the coordinator's focus, which is the failure this work exists to prevent.

### Added
- **HL Contract** — on owner approval, `templates/HL.md` §1, §3, §4, §5, §6 and §7 freeze; §2, §7.2 and §8–§11 stay free; §12 becomes append-only. Carried by a header `Contract` field with two states, which tracks the *artifact* where task status tracks the *pipeline*. The frozen unit is the declarative claim, not the section text. `conventions.md` §3 owns the 21 rules, including the requirement that the approved HL be **committed before the first research iteration** — an uncommitted baseline makes "frozen" permanently unverifiable (TFW-53/A, TFW-48 precedent)
- **`§12 Amendment Log`** — the only channel for changing a frozen claim: a dated, evidenced proposal carrying cost and a considered alternative, ruled by an explicit owner verdict. Append-only, so a refused proposal stays visible as an attempt. `Type` states relation to the baseline (`EXTEND` / `SUPERSEDE` / `RESTRICT`), never disposition. `templates/RES.md` splits its recommendations to match: `Refinements` the coordinator applies, `Amendment Proposals` it may not (TFW-53/A)
- **Purpose Check** — `templates/review/judge.md` row 2 clause (a) asks *is this what we set out to do?* against the **contract baseline plus the Project North Star**, never the TS and never a Phase HL. One field quotes the clause served **and** names the concrete harm; a citation that resolves but is irrelevant fails the row, and so does a harm asserted with no citation. Three tests — excess and adjacency, deferral confession, materiality. Three outcomes: aligned, **`not fit for purpose`** (grounds ❌ REJECT with every other check passing, routed to the owner), and *reference set internally inconsistent* (a contract defect, also to the owner). *"The TS scoped it this way"* and *"tests are green"* are named as insufficient grounds to approve (TFW-53/C)
- **PV Index priority 0 — Project North Star** — an anchor above the task HL, answering what we are building, why, and **what we are deliberately not building**. Locus: designated section(s) of a README, never a task HL. Optional, with a declared fallback to master HL §1 at its contract baseline, so a review is never blocked on its absence. `templates/HL.md` gains a `Project North Star` header field. Citation namespace `NS{n}`; `PP{n}` for a project principle registry; HL §7 `P{n}` unchanged (TFW-53/C)
- **Ten glossary articles** — `HL Contract`, `Contract Baseline`, `Frozen Section`, `Amendment`, `Amendment Log`, `Project North Star`, `Purpose Check`, `not fit for purpose` and `Deferral confession` under a new `## Contract and Purpose Defence` grouping, plus the long-missing `Result Visualization` beside `Value Flow` and `Findings Map`. Eight of the ten had zero definitions while five files used them (TFW-53/D)
- **Anti-patterns in `conventions.md` §14** — silent frozen-section edits, unclassified research recommendations, applying an amendment before its verdict, research on an uncommitted baseline, a research-thread remark treated as a verdict, an agent citing its own delegation to accept an overrun, a Phase HL authoring its own acceptance criteria or principles, a reviewer approving work that satisfies the TS but not the contract, and alignment asserted without citing the clause it serves (TFW-53/A, /C)

### Changed
- **`plan.md` Step 6c is inverted** — from *"Update HL with research findings (present diff to user)"* to *classify, apply, log, escalate*: refinements applied silently, amendments transcribed into §12 as `PROPOSED` with the section left untouched, and one batched escalation per iteration carrying evidence, cost and alternative. A coordinator may not apply a proposal it filed. Both verdict paths are specified, including a **re-freeze commit at the new baseline** after every approved amendment (TFW-53/B)
- **`research/base.md`** — the researcher classifies every recommendation by target section and never edits the HL (TFW-53/B)
- **Reviewer Identity** — *"Quality guardian, not rubber stamp"*, extended to name the third defended object: goals, values and the north star, with authority to block work that is verified, complete and beside the point. D46 recorded the *"not rubber stamp"* half in April and only the first half ever shipped (TFW-53/C, D46)
- **`review.md`:28 loads the master HL at its contract baseline**, not the current file — without this the reference-set rule has nothing to bind to and reviewers keep reading the drifted version (TFW-53/C)
- **`conventions.md` §5 REJECT branch (a)** — *"rework HL"* now means *file an amendment against the frozen sections*; re-entry to `📝 HL_DRAFT` reopens the free sections only. It was the one documented path that reopened a frozen contract with no proposal and no log (TFW-53/A)
- **`conventions.md` §3 — a Phase HL is derivation-only.** It may restate master content and add execution context; it may not carry its own §1, §5, §6 or §7. TFW-48's Phase A HL was a complete second contract that silently dropped three master principles (TFW-53/A)
- **`templates/HL.md` §3.1 — Working Backwards and visualization are mandatory**, not format options: written from the finished state, rendered visually with prose alone insufficient, showing the value and not only the artifact, and complete enough for a multi-phase task to be held at once (TFW-53/A)
- **One name per concept** — `frozen baseline` and `committed frozen baseline` retire in favour of **`Contract Baseline`**; the `templates/HL.md` north-star field label becomes **`Project North Star`**, so the form teaches the name the glossary defines (TFW-53/D, D28)
- **Scope budgets raised to the owner's working values** — `max_files_per_phase` 14 → **30**, `max_new_files` 8 → **15**, `max_loc` 1200 → **3000**, `max_modified_files` 12 → **30**. Changed in both places that carry the numbers: `templates/project_config.yaml` (what a new project is born with) and `conventions.md` §6 (the defaults table agents read inline). Rationale: the standard is set by observed practice, not by the shipped template — the owner's project had run at these values for months while the template still claimed the old ones, so an upgrade would have silently reverted them. Owner instruction, 2026-08-13. See D62
- **Adapter Sync section completed** — `workflows/config.md`. It documented 4 of 11 workflow files and 1 of 3 adapter folders; it now carries the full source → copy mapping for both full-copy folders (`.claude/commands/`, `.agent/workflows/`), an explicit *not copied, and why* table (research mode files, the adapter-only `tfw-task`, Codex thin routers), and a runnable **drift check** that prints every copy no longer matching its source. Two anti-patterns added: copying to one adapter folder only, and reporting a sync as done without running the check. At Phase D the check printed **14 drifted copies** (7 workflows × 2 folders); all fourteen were re-synced and the check now runs silent (TFW-53/D)
- **`CLAUDE.md`** — the `/tfw-plan` and `/tfw-review` purpose cells describe what those workflows now do, and the table gains the two rows it was missing, `/tfw-knowledge` and `/tfw-config` (TFW-53/D)

### Removed
- **The Judge mapping-integrity check** — *"did the AC each HL §7 principle was mapped to pass?"* It is structurally unable to detect a principle violated by the mapping itself: in a reconnaissance corpus it returned ✅ on the very acceptance criterion that carried the violation, and the reviewer later retracted his own APPROVE. Replaced by the Purpose Check above; row 2 clause (b) design soundness is unaffected (TFW-53/C)
- **`templates/RES.md`:32 — `<!-- List what should change in HL based on research. Coordinator applies these. -->`** The template-side twin of `plan.md` Step 6c. Fixing one and not the other would have reproduced the drift through the second channel (TFW-53/A)
- **The inline baseline recovery command in `templates/HL.md`** — a fourth copy of `git log --format=…` in the template every HL is born from, replaced by a pointer to `conventions.md` §3 rule 15 so it can be corrected in one place. **Upgrading projects: existing HL headers keep whatever they carry** — history is not rewritten; the change affects HLs created from this version onward (TFW-53/D, TD-164)
- **`KNOWLEDGE.md` §0 from `compilable_contract.md`'s *"Where references appear"* list** — a section D37 removed in April (TFW-53/D, TD-167)

### Fixed
- **`compilable_contract.md`** — `NS{N}` and `PP{N}` were declared in the §2 pattern table with no resolution behaviour; they now sit in the Resolution rules beside `D{N}`, `P{N}`, `F{N}` and `TD-{N}` (TD-165)
- **`glossary.md`** — the Knowledge Gate is in **Step 2** of `plan.md`, not a "Phase 0" that does not exist (TD-163)
- **Adapter parity restored** — both `tfw-plan` copies still carried the retired *"Update HL with research findings"*, so two of three surfaces instructed the coordinator to do what the core now forbids (TD-157). Six further workflows were repaired in the same pass: `tfw-init`, `tfw-handoff`, `tfw-update`, `tfw-knowledge`, `tfw-review`, `tfw-research`

## [1.1.0] — 2026-08-13
### Added
- **Three promoted universal Judge rows** — `templates/review/judge.md` grows from 7 to 10 rows, each promoted row carrying its measured non-✅ rate from a 637-row / 203-review / 3-install corpus: **Evidence sufficiency** (16.1% — the highest-firing check in TFW review; four gated rows turned out to be one check in three genre costumes), **Backward compatibility** (8.5%), **Safety** (4.0%, retained on consequence rather than frequency). Row 2 *Philosophy aligned* is sharpened into two separately answered clauses — mapping integrity and **design soundness** (4.5%) (TFW-56, D42 revoked)
- **Structural explicit-N/A grammar in the Judge checklist** — status vocabulary is `✅ / ❌ / ⚪ N/A`, and `⚪ N/A` requires a stated reason. A row skipped as a bare ✅ leaves the stage incomplete. Rows 7 and 8 carry an explicit contrast note (*does the evidence exist* vs *does it establish the claim*) plus a Checkpoint item requiring they be answered separately (TFW-56, F21)
- **Claim & Source Checks in `templates/review/verify.md`** — the three `docs`/`spec` verify actions promoted to unconditional: spot-check 2-3 key claims or sources, confirm every citation traces to a real artifact, verify data claims against a primary source. Table + Checkpoint item; feeds Judge row 8 (TFW-56)
- **Anti-pattern in `conventions.md` §14** — a review checklist row added without an evidenced firing rate. Retention on consequence rather than frequency is permitted and must be written into the row (TFW-56)
### Changed
- **`review.md` steps renumbered 0-7, contiguous** — Step 0 is Session Naming, the TFW standard this file never followed. Map 2→1, Verify 3→2, Judge 4→3, Decide 5→4, Tech Debt 6→5, Update Traces 7→6, Knowledge Capture 8→7. The Verify step now states that every action in `verify.md` is unconditional and that depth is set by `min_verify_ratio`, never by the kind of work under review (TFW-56, TD-106 closed by deletion)
- **`templates/REVIEW.md` §3 realigned row-for-row with `judge.md`** — ten rows in the same order. This also repairs a pre-existing gap: the Evidence completeness row added to `judge.md` in 0.8.8 had never reached `REVIEW.md` §3 (TFW-56)
- **`glossary.md`** — Reviewer heading is *"coordinator under the reviewer Role Lock"*, so the phrase "review mode" no longer carries two meanings (D28); entry describes one universal 10-row checklist; Principles Check pointer corrected to `review.md` Step 3 (TFW-56)
- **`workflows/config.md`** — the `review` propagation section keeps only `min_verify_ratio`, whose step pointer is correct in the renumbered workflow (TFW-56)
- All adapter copies re-synced: `.claude/commands/tfw-{review,config}.md`, `.agent/workflows/tfw-{review,config}.md`, `.tfw/adapters/codex/skills/tfw-review/SKILL.md`, `.agents/skills/tfw-review/SKILL.md` (TFW-56, D54)
### Removed
- **Config key `tfw.review.default_mode`** — removed from `.tfw/project_config.yaml` and `.tfw/templates/project_config.yaml`. **Upgrading projects: this key is now inert.** `/tfw-update` triages files, not keys, so a leftover `default_mode: code` line will not be flagged and will not break anything — delete it from your `tfw.review` block. `tfw.review.min_verify_ratio` and its `0.42` default are unchanged (TFW-56)
- **Review mode files** — `.tfw/workflows/review/{code,docs,spec}.md` and the folder itself. Byte-identical across three installs, two framework versions and two product domains; never used as an extension point. Their first verify action duplicated `verify.md`'s Checkpoint (TFW-56, D42 revoked)
- **The review mode selection step and its 🛑 WAIT gate** — `review.md` Step 1. In 203 mode-carrying reviews no mode row was ever the sole non-✅ driving a verdict: the rows carried signal at ~8%, the selection in front of them flipped nothing. What to check is declared once, by the TS — acceptance criteria (D49) and `Evidence:` fields (D52) (TFW-56)
- **`Mode:` / `Review Mode` template fields** — from `templates/review/{map,verify,judge}.md` and `templates/REVIEW.md`, together with the mode-specific placeholder comment. Existing REVIEW files keep their headers; history is not rewritten (TFW-56)
- **`docs` Content quality checklist row** — dropped rather than promoted; the one true duplicate of universal row 4 *Style & standards* (TFW-56)

## [1.0.0] — 2026-08-06
### Added
- **Minimal Commit Attribution** — AI-authored commits use the searchable `[agent/task/scope/role] summary` subject format with explicit field meanings and a clear separation from Git author/committer metadata and actor authentication (TFW-50, D55)
### Changed
- **Commit subject contract (breaking)** — Coordinator, Researcher, Executor, and Reviewer use the conventions-owned format when they create commits; the rule formats existing commit actions and creates no commit cadence
- **Handoff and release publication boundary** — ONB and release commits use Commit Attribution, while push and remote tag publication remain unavailable until explicit user approval

## [0.9.0] — 2026-07-22
### Added
- **Evidence Enforcement** — `evidence/` folder mandatory in every task directory. EV template (`.tfw/templates/evidence/EV.md`) with Environment header, per-AC evidence table (4-status vocabulary), Verdict line, optional Attachments index. Naming: `EV__{PREFIX}-{N}__{title}.md`. D16 (optional folder) revoked; D53 (TFW-47/A)
- **Codex first-class adapter** — 11 handwritten shortcut skills in `.tfw/adapters/codex/skills/tfw-*/SKILL.md`, installed to `.agents/skills/tfw-*/SKILL.md`. Two-layer architecture: root AGENTS.md always-on recognition (`TFW:CODEX` marker block) + repo-local skills for discovery and progressive loading. D54 (TFW-47/B)
- **Codex adapter README** — executable install/repair contract: detect state → install copies → merge AGENTS block → remove legacy → verify → runtime contract (TFW-47/B)
- **Codex in init.md** — Phase 0 full-init vs existing-project attach/repair detection, Codex skill install and verification steps (TFW-47/B)
- **Codex in update.md** — safe command/routing re-sync with marker ownership, legacy cleanup guard, literal slash smoke test (TFW-47/B)
- **Evidence subfolder section in conventions.md** — §4 documents `evidence/` as mandatory subfolder alongside `research/` and `review/` (TFW-47/A)
### Changed
- **RF template §5** — inline evidence table replaced with pointer to EV file + verdict summary. Cognitive mode clarified: executor's observational work lives in EV file (TFW-47/A)
- **TS template** — added `### Evidence Artifacts` subsection after AC items with guidance and example table (TFW-47/A)
- **handoff.md Step 11** — rewritten with 6 numbered substeps for evidence folder creation, template copy, and population. Skip condition removed — evidence always required (TFW-47/A)
- **conventions.md §3** — evidence pipeline table updated: EV file row added, RF row clarified as "Summary / Reference" (TFW-47/A)
- **conventions.md §14** — evidence anti-pattern wording strengthened: "evidence/ folder" language, "VERIFIED without artifact" prohibition (TFW-47/A)
- **glossary.md** — Adapter Command entry includes Codex (`.agents/skills/tfw-*/SKILL.md`), Tool Adapter definition updated with two-layer Codex architecture (TFW-47/B)
- **conventions.md** — added Codex two-layer adapter pattern and cross-tool `/tfw-*` command contract (TFW-47/B)
- **quickstart.md** — Codex install/repair handoff, corrected lifecycle/four-role summary (TFW-47/B)
### Removed
- **Legacy `source-command-tfw-*` skills** — stale full-workflow imports that duplicated canonical workflows and created a second source of truth (TFW-47/B)

## [0.8.8] — 2026-07-07
### Added
- **Evidence Layer** — real-world verification as first-class TFW concept, separate from synthetic Verification (§4). Three-role pipeline: coordinator designs Evidence Plan (TS), executor collects evidence (RF §5), reviewer audits evidence (REVIEW). Fixed 4-status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A (TFW-46, D52)
- **Evidence concept in conventions.md** — §3 Evidence Sections table (4 per-template entries with cognitive modes), §12 evidence honesty rule, §14 five anti-self-deception anti-patterns (TFW-46/A)
- **Evidence field in TS template** — `Evidence:` field after `Gate:` in AC items with MAY-deviate instruction. Grammar: full spec, minimal, N/A, DEFERRED, or empty (TFW-46/A)
- **§5 Evidence section in RF template** — table (AC, What, Environment, Result, Artifact) + evidence verdict line. §5-8 renumbered to §6-9 (TFW-46/A)
- **Evidence Audit in review stage files** — judge.md check #7 (Evidence completeness), verify.md Evidence Verification section with table and N/A fallback (TFW-46/A)
- **Step 11 (Collect evidence) in handoff.md** — between build gate (Step 10) and Pre-RF Gate (Step 12). Proportionality clause, DEFERRED/BLOCKED guidance, proactive tooling note. §5 Evidence in mandatory sections (TFW-46/B)
- **Trust Protocol evidence entries in review.md** — 2 new entries: "Evidence: VERIFIED" (Verify level), "Evidence: N/A or no evidence" (Challenge level) (TFW-46/B)
- **Evidence reminder in plan.md** — Step 7 sub-step 3: coordinator considers Evidence fields when writing TS AC items (TFW-46/B)
- **5 Evidence glossary terms** — Evidence, Evidence Plan, Evidence Collection, Evidence Audit, Evidence Status Vocabulary (TFW-46/C)
### Changed
- **RF template renumbering** — §5 Observations → §6, §6 Fact Candidates → §7, §7 Strategic Insights → §8, §8 Diagrams → §9. All cross-references updated across templates, workflows, conventions (TFW-46/A)
- **glossary.md** — Strategic Insight entry: RF §7 → §8 (stale ref fix from Phase A renumbering) (TFW-46/C)
- All adapter copies synced: `.agent/workflows/tfw-{handoff,review,plan}.md`, `.claude/commands/tfw-{handoff,review,plan}.md` (TFW-46/C)

## [0.8.7] — 2026-05-01
### Added
- **Mindset blocks in research templates** — per-stage cognitive anchoring: Strategist (Briefing), Explorer (Gather), Analyst (Extract), Critic (Challenge). Each template has `> **Mindset:**` + `> **Test:**` blockquote between h1 and `> Parent:` line. Matches review template pattern (D41) (TFW-43)
- **Briefing h1 guiding question** — `# Briefing — "What should we investigate?"` added for consistency with other 3 stages (TFW-43)
### Changed
- **Copy-on-enter protocol** in `research/base.md` — Step 3 creates folder only (no template copy). Step 4 copies briefing template before writing. Step 5 restructured as FOR EACH loop: copy template → read Mindset → OODA → checkpoint → 🛑 STOP per stage. Restores D31 (file existence = stage completion) (TFW-43)
- All adapter copies synced: `.agent/workflows/tfw-research.md`, `.claude/commands/tfw-research.md` (TFW-43)
### Removed
- **Batch template copy** from `research/base.md` Step 3 — all 4 templates were copied at once, breaking D31 (file existence = stage completion) and observable progress. Replaced by copy-on-enter (TFW-43)

## [0.8.6] — 2026-04-30
### Changed
- **Research folder structure** — `researchN/` flat folders at task root replaced by single `research/` container with `iterN/` subfolders. RES files co-located with stage files (`research/iterN/RES.md`). `iterations.yaml` moved inside `research/` subfolder (TFW-42/A)
- **Stage file numbering** — `briefing.md`, `gather.md`, `extract.md`, `challenge.md` renamed to `1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`. Sort order = execution order (TFW-42/A)
- **Phase folder naming** — `PhaseA/`, `PhaseB/` → `phase-a/`, `phase-b/` (kebab-case, consistent with D48) in conventions.md §4 and artifact filename table (TFW-42/A)
- **iterations.yaml schema** — added optional `agent` (free-text, traceability) and `sources` (list, source categories) fields. Backward compatible (TFW-42/A)
- **research/base.md** — Steps 0, 3, 4, 5, 6 updated: all paths use `research/iterN/`, numbered stage file names, co-located RES.md (TFW-42/B)
- **plan.md** — Step 6b: `research/iterations.yaml` path + `agent`/`sources` fields + multi-agent reference. Step 6c: updated RES paths. Step 7: `phase-a/` naming (TFW-42/B)
- **glossary.md** — "Iteration (Research)": `research/iterN/` paths, co-located RES. "iterations.yaml": `research/` location, `agent`/`sources` fields (TFW-42/C)
- All adapter copies synced: `.agent/workflows/tfw-{research,plan}.md`, `.claude/commands/tfw-{research,plan}.md` (TFW-42/C)
- D50 in `KNOWLEDGE.md` §1, TFW-42 in §2 (TFW-42)
- domain F4, philosophy F25, process F21-F22, stakeholder F2 in `knowledge/` topic files (TFW-42)

## [0.8.5] — 2026-04-20
### Added
- **Requirements-first TS template** — §4 Detailed Steps replaced by §5 Acceptance Criteria (verifiable gates with `[depends: AC-X]` dependency annotations), §3 Principles Check (HL §7 → AC mapping table), §6 Technical Guidance (reference, not instructions), §7 Definition of Failure (hard reject conditions), §9 Cross-Phase Modifications (multi-phase conflict tracker) (TFW-41/A, D49)
- **Pre-TS Gate** in `plan.md` Step 7 (3b) — coordinator reads RF of latest completed phase before writing next TS. Ensures planning against actual output, not prior plan (TFW-41/B, D49)
- **Pre-RF Gate** in `handoff.md` Step 11 — executor opens RF template and reads section headings before writing RF (TFW-41/B, D49)
- **Execution Loops** in `handoff.md` Phase 2 — when TS ACs have `[depends: AC-X]`, executor verifies prerequisite AC gate before implementing dependent AC (TFW-41/B, D49)
- **Session Naming Step 0** in `handoff.md`, `plan.md`, `review.md` — `Role | Task-ID | Phase` at session start (TFW-41/B, D49)
- **ONB answer protocol** in `handoff.md` — coordinator presents options with tradeoffs, does not decide for stakeholder (TFW-41/B, D49)
- **HL §7 Principles check** in `review.md` Judge stage — reviewer traces HL §7 → TS §3 → RF §3 for each principle (TFW-41/B, D49)
- **Phase Dependencies** section in HL template §4 — mermaid graph + dependency matrix for multi-phase tasks (TFW-41/A, D49)
- **Embedded dimensional analysis** in research templates — `## Dimensions` in gather.md, `## Configuration Space` in extract.md, `## Consistency Check` in challenge.md. Cross-stage structural dependency as natural enforcement (TFW-41/C, D49)
- **Dimensional analysis thread** in `research/base.md` Step 5 — 3-sentence connecting logic with graceful degradation for <3 dimensions (TFW-41/C, D49)
- **§14.1 Terminology Origin** in `conventions.md` — maintainer-facing note mapping TFW terms to Zwicky GMA equivalents (TFW-41/C)
- **4 anti-patterns** in `conventions.md` §14 — code-in-TS, coordinator planning drift, RF-from-memory, ONB source-less answers (TFW-41/A)
- **15 glossary terms** — 10 execution gate terms (Acceptance Criteria, Technical Guidance, Definition of Failure, Principles Check, AC Dependency Annotation, Execution Loop, Pre-TS Gate, Pre-RF Gate, Session Naming, Phase Dependencies) + 5 dimensional analysis terms (Dimension, Alternative, Configuration Space, Consistency Check, Surviving Configuration) (TFW-41/D)
- D49 in `KNOWLEDGE.md` §1, TFW-41 in §2, 2 legacy entries in §3 (TFW-41)
- philosophy F24 (instructions→compliance, heuristics→competence), process F18-F20 in `knowledge/` topic files (TFW-41)
### Changed
- **TS.md template** — complete structural rewrite: §3 Principles Check, §4 Affected Files (with budget), §5 Acceptance Criteria (from §4 Detailed Steps), §6 Technical Guidance, §7 Definition of Failure, §8 Phase Risks, §9 Cross-Phase Modifications. Line count 52→84 (TFW-41/A)
- **handoff.md** — Step 0 (Session Naming), Execution Loops in Phase 2, ONB answer protocol, Pre-RF Gate in Phase 3. Line count 148→161 (TFW-41/B)
- **plan.md** — Step 0 (Session Naming), Pre-TS Gate in Step 7 (3b). Line count 145→153 (TFW-41/B)
- **review.md** — Step 0 (Session Naming), step renumbering (Select Review Mode = Step 1), HL §7 Principles check in Judge. Line count 145→153 (TFW-41/B)
- **research/base.md** — dimensional analysis thread in Step 5. Line count 129→131 (TFW-41/C)
- **gather.md** — `## Dimensions` section before Findings. Line count 25→40 (TFW-41/C)
- **extract.md** — `## Configuration Space` section before Findings. Line count 25→42 (TFW-41/C)
- **challenge.md** — `## Consistency Check` section before Findings. Line count 25→47 (TFW-41/C)
- **glossary.md** — 2 new sections: `## Execution Gates` (10 terms), `## Research — Dimensional Analysis` (5 terms). Line count 197→246 (TFW-41/D)
- All Antigravity adapters synced: `.agent/workflows/tfw-{handoff,plan,review,research}.md` (TFW-41/D)
- philosophy F13 upgraded to ✅ verified (3 sources) with TFW-41 user quote on domain-agnosticism (TFW-41)
### Removed
- **TS §4 Detailed Steps** — procedural implementation instructions replaced by requirements-first Acceptance Criteria (TFW-41/A, D49)

## [0.8.4] — 2026-04-15
### Added
- **State/framework file classification** — §10.3 in conventions.md: 3-category model (Framework, State, Config) with lifecycle rules. State files NEVER overwritten from upstream (TFW-40/A, D47)
- **YAML naming convention** — §10.4 in conventions.md: `lower_snake_case` for all `.tfw/` YAML and template files. Uppercase reserved for root docs and `.tfw/` framework docs (TFW-40/B)
- **Templates for state/config files** — `.tfw/templates/knowledge_state.yaml` (clean `seq=0`), `.tfw/templates/project_config.yaml` (annotated `← PROJECT` / `← FRAMEWORK` markers) (TFW-40/A)
- **⚫ STATE category** in `update.md` — files never overwritten during `tfw-update` (knowledge_state.yaml, knowledge/, KNOWLEDGE.md, TECH_DEBT.md) (TFW-40/A)
### Changed
- `PROJECT_CONFIG.yaml` → `project_config.yaml` ⚠️ **BREAKING** — all references updated across workflows, templates, adapters, conventions, glossary, compilable_contract, README, KNOWLEDGE.md, gen_docs.py (TFW-40/B)
- `TOPIC_FILE.md` → `topic_file.md` — template renamed, references updated in conventions, glossary, knowledge.md workflow (TFW-40/B)
- `init.md` — Phase 2 Mini-Setup now copies from templates (not upstream files), preventing state contamination (TFW-40/A)
- `update.md` — added ⚫ STATE category, explicit merge rules for project_config.yaml (preserve project sections, update framework sections) (TFW-40/A)
- `gen_docs.py` — config path updated to `project_config.yaml` (L165-166, L530) (TFW-40/B)
- All Claude Code adapters synced: `.claude/commands/tfw-*.md` — full sync from canonical `.tfw/workflows/` (11 files). Fixes stale `PROJECT_CONFIG.yaml` references and accumulated drift from TFW-38+TFW-40 (TFW-40/B)

### Migration Notes (⚠️ BREAKING)
Projects upgrading from ≤0.8.3 must:
1. Rename `.tfw/PROJECT_CONFIG.yaml` → `.tfw/project_config.yaml`
2. Rename `.tfw/templates/TOPIC_FILE.md` → `.tfw/templates/topic_file.md` (if exists)
3. Update any custom adapter files referencing `PROJECT_CONFIG.yaml`
4. Update `docs/scripts/gen_docs.py` if customized (config path changed)

## [0.8.3] — 2026-04-15
### Added
- **4-stage review flow** — Map → Verify → Judge → Decide. Each stage = separate template file in `.tfw/templates/review/` with mindset-based identity (Student/Auditor/Judge/Decision-maker) and self-check gate. Mode selection (code/docs/spec) with `🛑 WAIT` gate (TFW-38/A, D41)
- **Review mode files** — `.tfw/workflows/review/{code,docs,spec}.md`. Mode-specific checklists (2-4 items) loaded at Step 2. Progressive Disclosure — agent loads only needed mode. 6 universal + mode-specific = hybrid (TFW-38/A, D42)
- **Knowledge Citation Table** — cascade model: Coordinator does full PV scan → HL §7.2, Executor reads HL §7.2 → ONB §7 (confirms/extends), Reviewer verifies links → verify.md (anti-hallucination gate). Unified name "Knowledge Citations" (TFW-38/B, D43)
- **Project Values (PV)** term — unified term for all accumulated project context. PV Index = 7 sources with scan priority in glossary.md. Replaces ambiguous "check values/knowledge/experience" (TFW-38/B, D44)
- **Reviewer Identity** — overall identity statement + per-stage mindsets. Trust Protocol table (7 rows). `🛑 WAIT` gate on mode selection (TFW-38/A.2, D46)
- **Knowledge Input Sections** table in conventions.md §3 — §7.2 HL, §7 ONB, verify.md Citations Verified (TFW-38/B)
- D41-D46 in `KNOWLEDGE.md` §1 (TFW-38)
- TFW-38/A, A.2, B in `KNOWLEDGE.md` §2 Key Artifacts (TFW-38)
- 4 legacy entries in `KNOWLEDGE.md` §3 (TFW-38)
- philosophy F20 (investigative vs procedural workflow classes), F21 (explicit N/A as universal design principle) in `knowledge/philosophy.md` (TFW-38)
### Changed
- **review.md** — rewritten: Role Lock updated, Reviewer Identity + Trust Protocol added, Steps 0-4 file-based (create stage files → synthesize into REVIEW), Steps 5-7 traces + knowledge capture (TFW-38/A+A.2)
- **REVIEW.md template** — restructured §1-§7: Map/Verify/Judge/Verdict/Tech Debt/Traces/Fact Candidates. Stage files listed in header. Synthesis instruction (TFW-38/A)
- **HL.md template** — §7.2 Knowledge Citations added (PV scan instruction, 4-column table, bootstrap note) (TFW-38/B)
- **ONB.md template** — §7 Knowledge Citations added (executor read-confirm, 5-column table, NEW row support) (TFW-38/B)
- **verify.md template** — Knowledge Citations Verified section + citation count in self-check checkpoint (TFW-38/B)
- **plan.md** Step 3 item 4 — "Check KNOWLEDGE.md" replaced with full PV scan instruction referencing glossary.md PV Index (TFW-38/B)
- **handoff.md** Phase 1 step 2 — citation-reading sub-bullet added before inconsistency check. Phase 3 step renumbered 12→11 (TFW-38/B, TD-94)
- **conventions.md** §15 Role Lock — review.md row updated with stage files (TFW-38/A)
- **glossary.md** — Reviewer updated (mode-aware + stage files), RESEARCH updated (pros/cons), Pass updated (OODA + sufficiency verdict) (TD-35, TD-36, TD-98)
- **README.md** — docs site link added to Links section (TD-92)
- **TECH_DEBT.md** — purged 41 closed items, 11 remaining. TD-33/TD-59 closed with rationale (tech debt audit)
- All adapters synced: `.agent/workflows/` (TFW-38/B)
### Removed
- **TFW-37** (Source Audit gate) — absorbed into TFW-38 (4-stage review + Trust Protocol + docs mode source verification)
- Single-pass REVIEW workflow — replaced by 4-stage flow with file-based evidence (TFW-38/A, D41)
- 9-point monolithic review checklist — replaced by 6 universal + mode-specific (TFW-38/A, D42)
- Silent "I checked KNOWLEDGE.md" pattern — replaced by Knowledge Citation Table with verifiable links (TFW-38/B, D43)

## [0.8.2] — 2026-04-10
### Added
- **Multi-iteration research** — `iterations.yaml` control file, `min_iterations` config (default: 2), coordinator hard gate in plan.md Step 6c, `researchN/` subfolder accumulation (never delete/overwrite), Iteration Status block in RES template, iter2+ briefing protocol in research/base.md (TFW-32/C, D38)
- **Per-template visual sections** — HL §3.1 Value Flow, RF §8 Diagrams, RES Findings Map. Convention cross-ref table in conventions.md §6. Per-template criterion: "what would THIS artifact's reader draw on a whiteboard?" (TFW-32/B, D39)
- **4-part template instruction structure** — Cognitive mode → Scope → Human-Only Test → Before writing. Applied to HL §6/§11, RF §6/§7, RES FC/SI, REVIEW §5 (TFW-32/B)
- **`📚 KNW` pipeline status** — 9th status between REV and DONE. Optional (reviewer can pre-close with N/A). REVIEW markers for tfw-docs/tfw-knowledge orchestration (TFW-32/A, D37)
- **docs/knowledge exclusive write territories** — tfw-docs owns KNOWLEDGE.md §1-§3, tfw-knowledge owns knowledge/ + §4. Explicit ⚠️ warnings in both workflows. Resolves collision (TFW-32/A, D37)
- **README "How TFW Compares"** section in `.tfw/README.md` — TFW vs Confluence/Notion vs AI assistants vs no methodology (TFW-32/D, D40)
- **Positioning specs** — audience_personas.md (3-tier hierarchy), positioning_spec.md (generates-vs-stores), translation_table.md (20 terms), philosophy_improvement.md (TFW-32/D)
- D37-D40, TFW-32/A-D in `KNOWLEDGE.md` §1/§2 (TFW-32/E)
- 13 new facts in `knowledge/` topic files: philosophy F15-F18, convention F11-F14, process F11-F15 (TFW-32/E)
- 5 legacy entries in `KNOWLEDGE.md` §3 for Phase B/C/D changes (TFW-32/E)
- TD-88..92 in TECH_DEBT.md (TFW-32 reviews)
- TFW-33/34/35 future tasks in Task Board (TFW-32/E)
### Changed
- **README.md opening** — interleave variant: imagine→reality→imagine→TFW. 3-tier audience hierarchy (product leaders > analysts > engineers) with qualifying questions. "Generates vs stores" in How It Works. AI-agents-as-team-members frame. 2 new FAQ entries. Expanded Links section (TFW-32/D, D40)
- **`.tfw/README.md`** — team dimension in The Problem, SECI generates-vs-stores in The Thesis, team memory table row, role breadth in How TFW Works, team-centric Success Criteria rewrite (TFW-32/D, D40)
- **plan.md** — Step 6b creates iterations.yaml, Step 6c iteration gate with min_iterations enforcement, phased subfolder diagram in Step 7. Growth: 108→140 lines (TFW-32/C)
- **research/base.md** — iter2+ briefing protocol (read all previous RES + iterations.yaml), Iteration Status block instruction (TFW-32/C)
- **RES template** — Iteration Status block, Fact Candidates sharpened with Cognitive mode + scope + Human-Only Test, Strategic Insights (Research) with Human-Only Test, Findings Map section (TFW-32/B+C)
- **HL template** — §3.1 renamed Value Flow (from Result Visualization), §3.2 added, §11 renamed Strategic Insights (Planning) with Cognitive mode instruction (TFW-32/B)
- **RF template** — §6 FC sharpened, §7 Strategic Insights (Execution) with Human-Only Test + fallback, §8 Diagrams section (TFW-32/B)
- **REVIEW template** — §5 FC sharpened with Cognitive mode + reviewer scope, tfw-knowledge marker in §4 (TFW-32/A+B)
- **conventions.md** — §6 Visual Sections cross-ref table (5 rows), §6 Knowledge Capture Sections table, KNW in pipeline diagram + status table (TFW-32/A+B)
- **glossary.md** — Strategic Insight updated, Value Flow + Findings Map + Per-template Naming added, KNW definition, pipeline diagram updated (TFW-32/A+B)
- `knowledge_state.yaml` — seq 31→32, 42→55 total facts (TFW-32/E)
- All adapters synced: `.agent/workflows/`, `.claude/commands/` (TFW-32/C)
### Removed
- **KNOWLEDGE.md §0** (Philosophy & Principles, 8 entries) — all principles verified in knowledge/philosophy.md or conventions.md. §0 had no updater workflow (TFW-32/A, D37)
- tfw-knowledge Phase 4 writes to KNOWLEDGE.md §1/§2 — caused collision with tfw-docs (TFW-32/A, D37)

## [0.8.1] — 2026-04-09
### Added
- **`.tfw/quickstart.md`** — strict reading list for AI agents (clone → philosophy → glossary → conventions → init.md). Separates learning from execution to resolve bootstrap paradox (TFW-31)
- **3 self-contained README Quick Start prompts** — New Project, Existing Project, Already Set Up. Each prompt is fully self-contained with repo URL, TFW description, and slash command references (TFW-31)
- **Tutorial Mode mini-examples** in `init.md` — task prefix examples, task board visualization with realistic entries (TFW-31)
- **Star CTA** in `init.md` Phase 5 — after value delivery, not during onboarding (TFW-31)
- **Slash command listing** in "Already set up" prompt — /tfw-plan, /tfw-handoff, /tfw-review, /tfw-resume (TFW-31)
- D36 (agent-first onboarding), TFW-29/31 in `KNOWLEDGE.md` §1/§2 (TFW-31)
- 6 new facts in `knowledge/` topic files: philosophy F12-F14, process F9-F10, convention F10 (TFW-31)
- TD-87 (init.md code-specific interview question) in TECH_DEBT.md (TFW-31)
### Changed
- **`init.md` Phase 1 Discover** — rewritten domain-agnostic: purpose/goals, documentation, structure, processes, people first; code-specific items last (TFW-31)
- `compilable_contract.md` — source manifest and nav diagram updated: `.tfw/init.md` → `.tfw/quickstart.md` (TFW-31)
- `conventions.md` §9 — adapter setup reference updated to quickstart.md (TFW-31)
- `update.md` — merge checklist updated: init.md → quickstart.md (TFW-31)
- `KNOWLEDGE.md` — §1 Architecture Map Init row updated, §3 Legacy entry added, §4 fact counts updated (36→42) (TFW-31)
- README.md — Quick Start section rewrite, file index and adapter table references updated (TFW-31)
- `glossary.md`, `conventions.md`, `compilable_contract.md` — TFW-29 consistency fixes (redundancy, numbering, reading flows) (TFW-29)
### Removed
- **`.tfw/init.md`** pointer file (21 LOC) — redundant after quickstart.md became the "Getting Started" entry. All references migrated to quickstart.md (TFW-31)
- Phase 0 Bootstrap from `init.md` — wrong approach (injected learning into execution workflow). Replaced by quickstart.md (TFW-31)

## [0.8.0] — 2026-04-08
### Added
- **Compilable Contract** — §16 in `conventions.md` (Source Manifest, Reference Format, Resolution Rules, Frontmatter Convention, Output Nav Structure). Agents write text refs (`RF TFW-18`), build-time resolves to hyperlinks (TFW-26/A)
- **Documentation Pipeline** — `docs/scripts/gen_docs.py` (681 LOC, 68 tests), 10 reference resolvers (artifact, phase, HL-dash, TD, D, backtick-path, bare task ID, markdown link rewriter, table anchors, literate-nav), structured tasks index, section indexes, YAML frontmatter injection (TFW-26/A+B, TFW-27/B)
- **docs/ infrastructure** — `mkdocs.yml`, `requirements.txt` (7 packages incl. mkdocs-literate-nav, mkdocs-section-index), `.github/workflows/docs.yml` (TFW-26/A, TFW-27/C)
- **Brand Identity** — two-color discipline (charcoal #1a1a2e + teal #0d9488), Inter/JetBrains Mono typography, TFW monogram logo, `docs/brand/identity.md` (TFW-27/A)
- **GitHub Pages Deploy** — live site at `tfw.saubakirov.kz`, auto-deploy on push to master via GitHub Actions (TFW-27/C, absorbs TFW-28)
- **Coordinator Fact Capture** — `philosophy` in §10.1 categories, §11 Strategic Session Insights in HL template, Step 4b (fact capture) in plan.md, fact capture reminder in resume.md, "Strategic Insight" glossary term (TFW-26/FC)
- **§16 Reference Format reminder** in HL, TS, ONB template footers — ensures all artifact authors use resolvable cross-references (TFW-27 post-review)
- **HL §11 and RF §7 scan** in `knowledge.md` Phase 2 — explicit scan targets for Strategic/Execution Session Insights (TFW-26 post-review)
- **Category coverage check** in `knowledge.md` Phase 2 Step 3 — check §10.1 for unrepresented categories (TFW-26 post-review)
- **KNOWLEDGE.md §1/§2 update step** in `knowledge.md` Phase 4 — Architecture Decisions and Key Artifacts entries for closed tasks (TFW-26 post-review)
- D34 (Compilable Contract), D35 (Brand + Wiki + Deploy) in `KNOWLEDGE.md` §1 (TFW-26, TFW-27)
- TFW-26, TFW-27 in `KNOWLEDGE.md` §2 Key Artifacts
- 17 new facts in `knowledge/` topic files: philosophy F5-F11, process F6-F8, convention F8-F9, constraint F4, stakeholder F1, environment F1-F2 (TFW-26, TFW-27)
- 2 new topic files: `knowledge/stakeholder.md`, `knowledge/environment.md` (TFW-27)
- Compilable Contract, Reference Format, Source Manifest glossary terms (TFW-26/A)
- TD-75 (knowledge quality design), TD-76 (terminology unification), TD-79..82 (gen_docs.py debt) in TECH_DEBT.md
### Changed
- **`knowledge.md` workflow rewrite** — 128→95 lines (-26%). Anti-patterns merged into Behavior Rules, Limits table replaced with config ref, Phase 4 renamed "Update" with 🛑 WAIT gate (TFW-26 post-review)
- **`.tfw/README.md` stripped** — 353→138 lines. Pure philosophy paper. Removed: project structure tree, artifact types, lifecycle, scope budgets, workflows table, execution modes, roles, Getting Started. All → `conventions.md`/`glossary.md` refs (TFW-27)
- `knowledge.md` Phase 2 — ⚠️ block with YES/NO examples of strategic vs technical knowledge (TFW-26 post-review)
- `knowledge.md` Behavior Rules — "DO NOT default all facts to existing categories" (TFW-26 post-review)
- `KNOWLEDGE.md` §4 — fact counts updated: 27→36, 4→6 topic files
- TECH_DEBT.md — TD-52, TD-69..74, TD-77, TD-78 resolved
- All adapters synced: `.agent/workflows/` — config, resume, plan, init (TFW-27)
### Removed
- Anti-patterns section from `knowledge.md` — merged into Behavior Rules (TFW-26)
- Limits table from `knowledge.md` — replaced with inline ref to PROJECT_CONFIG.yaml (TFW-26)
- `.tfw/README.md` §Evolution — replaced with CHANGELOG link (TFW-27)
- `.tfw/README.md` technical reference sections — duplicated from conventions/glossary (TFW-27)
- TFW-28 as standalone task — absorbed into TFW-27/C (TFW-27)

## [0.7.1] — 2026-04-04
### Added
- **3 new README Values** — "Honesty Over Convincingness" (renamed from "Determinism and Safety"), "Structural Enforcement" (filesystem = state machine), "Naming Creates Behavior" (terminology > explanation). Total: 5→8 values (TFW-25)
- **Design Rules** subsection in `conventions.md` §11 — P10-P13 content compressed into 4 rules: token density, inline enforcement, DNA/library, progressive disclosure (TFW-25)
- `philosophy` category in RF.md and REVIEW.md templates' FC category list (TFW-25 post-review)
- D34 (Values consolidation) in `KNOWLEDGE.md` §1 (TFW-25)
- F7 (framework value count norms) in `knowledge/convention.md` (TFW-25 knowledge consolidation)
### Changed
- `KNOWLEDGE.md` §0 — pruned 14→7 principles (P4/P6 obvious, P10-P13 → conventions, P14 → README Values) (TFW-25)
- `KNOWLEDGE.md` §3 Legacy — pruned 35→13 items (removed all pre-TFW-22 resolved entries) (TFW-25)
- `KNOWLEDGE.md` §4 Tech Stack — removed entirely (obvious from repo) (TFW-25)
- `KNOWLEDGE.md` — §5 Project Facts renumbered to §4 after Tech Stack removal (TFW-25)
- `knowledge/convention.md` — pruned 12→7 facts (6 self-evident facts removed, 1 added) (TFW-25)
- `knowledge/process.md` — pruned 10→5 facts (5 self-evident facts removed) (TFW-25)
- `TECH_DEBT.md` — pruned 64→19 items (removed all resolved/accepted/obsolete entries) (TFW-25 post-review)
- `KNOWLEDGE.md` template — §4 Tech Stack removed, §5→§4 renumbered (TFW-25 post-review)
- `knowledge.md` workflow — 3 stale §5 references updated to §4 (TFW-25 post-review)
### Fixed
- TD-64: KNOWLEDGE.md template referenced `## 5. Project Facts` instead of `## 4.`

## [0.7.0] — 2026-04-04
### Added
- **Researcher role** — 4th standalone role (after Coordinator, Executor, Reviewer), extracted from Coordinator following TFW-8 pattern. Own `🔒 ROLE LOCK: RESEARCHER`. Permitted: RES, `research/` stage files. Forbidden: HL, TS, ONB, RF, REVIEW, code (TFW-24)
- **Research subfolder state machine** — `research/` subfolder with stage files (`briefing.md`, `gather.md`, `extract.md`, `challenge.md`). File existence = stage completion. Crash-resilient, zero-parsing (TFW-24)
- **Resume Protocol (Step 0)** in `research/base.md` — check filesystem state → resume from first missing file. No chat history dependency (TFW-24)
- **4 research stage templates** in `.tfw/templates/research/` — briefing, gather, extract, challenge. Each with Parent HL link, Goal from §1 Vision, D28 guiding question subtitle, Checkpoint with `Stage complete: YES/NO`, Sufficiency checklist (TFW-24/B)
- **HL §1 Working Backwards** — Vision narrative ("write as if done"), Impact field, stakeholder-perspective Quote (Amazon press release pattern) (TFW-24)
- **HL §10 "Why Not Just...?"** — internal FAQ section forcing alternatives consideration before research (TFW-24)
- `tfw.content_language` config — controls artifact content language (default: `en`). Template structure always English (TFW-23)
- P14 (Filesystem = state machine) in `KNOWLEDGE.md` (TFW-24)
- D29 (English-only templates), D30-D33 (Researcher role, subfolder state machine, RES synthesis, Working Backwards) in `KNOWLEDGE.md` (TFW-23, TFW-24)
### Changed
- **BREAKING:** All 5 core templates (HL, TS, RF, ONB, REVIEW) — pure English headings and field labels. 32 terms translated per D28. `content_language` note added (TFW-23)
- **BREAKING:** HL template §1 restructured — generic "Vision" → Vision narrative + Impact + Quote (TFW-24)
- **BREAKING:** HL template §2 "Current State" — domain-agnostic ("system/process/environment" not code-specific) (TFW-23/24)
- **BREAKING:** HL template §5 "Definition of Done" — domain-agnostic checklist items (TFW-23)
- **BREAKING:** RES template — stage sections removed. RES = synthesis format (Decisions, Hypotheses, HL Recommendations, Conclusion). Stages live in `research/` subfolder (TFW-24)
- **BREAKING:** Coordinator no longer conducts research — hands off to Researcher via `/tfw-research` (TFW-24)
- `research/base.md` Steps 3/4/5 — reference `templates/research/` for stage files (TFW-24/B)
- `conventions.md` §4 — inline stage format replaced with templates reference (TFW-24/B)
- `conventions.md` §8 — Researcher role in workflows table (TFW-24)
- `conventions.md` §15 — Researcher row in Role Lock table, `research/base.md` row updated (TFW-24)
- `glossary.md` — Researcher role definition, Coordinator updated (research duties removed) (TFW-24)
- `plan.md` Step 6 — Researcher handoff with STOP instruction (TFW-24)
- `PROJECT_CONFIG.yaml` — RES status role = `researcher` (TFW-24)
- `init.md` Step 5 — `content_language` in config generation (TFW-23)
- All adapters synced: `.agent/workflows/`, `.claude/commands/` (TFW-23, TFW-24)
### Removed
- "Coordinator (Research Mode)" overlay — replaced by standalone Researcher role (TFW-24)
- Stage sections in RES template (Gather/Extract/Challenge) — moved to `research/` subfolder files (TFW-24)
- Inline stage file format in `conventions.md` §4 — replaced by template reference (TFW-24/B)
- Mixed RU/EN headings from all 5 templates (TFW-23)

## [0.6.6] — 2026-04-04
### Added
- **Modular research architecture** — `research/{base,focused,deep}.md` replaces monolithic `research.md` (TFW-22)
  - `base.md`: core algorithm with OODA Stage Loop, Trust Protocol, Sufficiency Verdict (504 words)
  - `focused.md`: single-pass mode, generic criteria only (106 words)
  - `deep.md`: multi-loop hypothesis-driven mode with metacognitive check (171 words)
- **OODA Stage Loop** in research — Observe→Orient→Decide→Act with YAML-configurable `loops_per_stage` hard limit (TFW-22)
- **Sufficiency Verdict** — 2-level checkpoint criteria: generic (always) + mode-specific (from mode file). Criteria = SOFT (report, not block) (TFW-22)
- **Trust Protocol** — 4-tier trust levels for user input (business→trust, tech→verify, numbers→empirical, experience→trust outcome) (TFW-22)
- **HL template §3.1** — Визуализация результата: ASCII mandatory, mermaid for complex flows, before→after tables (TFW-22)
- **HL template §10** — Обоснование RESEARCH: hypotheses table with filter, blind spots, risks of not researching, proposed focus (TFW-22)
- **RES template** — Hypotheses table in Briefing (from HL §10), Sufficiency Verdict format in every stage checkpoint (TFW-22)
- **Step 5: Hypothesis Iteration** in `plan.md` — FOR EACH loop presenting §10 hypotheses to user before RESEARCH decision (TFW-22)
- `tfw.research.default_mode` and `tfw.research.modes.{focused,deep}` in `PROJECT_CONFIG.yaml` (TFW-22)
- 3 new Config Sync Registry entries for research mode settings (TFW-22)
- P12 (DNA/Library split), P13 (Progressive Disclosure) in `KNOWLEDGE.md` (TFW-22)
- D25-D28 (modular research, OODA loop, Trust Protocol, Naming > Explanation) in `KNOWLEDGE.md` (TFW-22)
### Changed
- **`plan.md` algorithm refactor** — 1213→795 words (-34%). Inline bloat (prerequisites, scope budget table, status transitions, anti-patterns) replaced with ref-inside-step pattern. DNA layer inline (Role Lock + Mindset). RESEARCH Gate strengthened (TFW-22)
- `PROJECT_CONFIG.yaml` workflow path: `research.md` → `research/base.md` (TFW-22)
- `config.md` Adapter Sync — copy command updated to `research/base.md` (TFW-22)
- `conventions.md` — 3 stale `research.md` references updated to `research/base.md` (TD-54)
- `CLAUDE.md`, `KNOWLEDGE.md` — research workflow path references updated (TFW-22)
- All 4 adapters synced: `tfw-plan.md` (×2), `tfw-research.md` (×2) (TFW-22)
### Removed
- Monolithic `research.md` (1165 words) — replaced by `research/` directory (TFW-22)
- Inline bloat in `plan.md`: prerequisites list, scope budget table, status transitions diagram, anti-patterns block (~400 words) (TFW-22)
### Fixed
- TD-54: `conventions.md` L29, 181, 276 — stale `research.md` paths updated to `research/base.md`
- TD-55: `conventions.md` L277 — `handoff.md` Role Lock table: `code` moved from Forbidden to Permitted Artifacts (executor writes code via handoff)
## [0.6.5] — 2026-04-03
### Added
- **Human-Only Test** in RF.md, REVIEW.md, RES.md templates — FC quality gate: "would this fact be unknown without the human saying it?" Rejects agent-discoverable facts (TFW-18B)
- **Human-Only Test** in `knowledge.md` Phase 3 Step 1 — consolidation-time reject criterion for agent-discoverable facts (TFW-18B)
- **Quality bar** in RF.md §5 Observations + handoff.md §Observations — "report only issues that would bite the next developer" (TFW-18B)
- **Quality filter** in review.md Step 3 — reject filler observations before promoting to TECH_DEBT.md (TFW-18B)
- Knowledge consolidation bullet in `.tfw/README.md` §v3 additions (TFW-18B)
- `knowledge` and `config` rows in `.tfw/README.md` §Canonical Workflows table (TFW-18B)
### Changed
- FC prompt reframed from "next agent's behavior" to "strategic knowledge — domain patterns, stakeholder priorities, business context" in RF.md, REVIEW.md, RES.md templates (TFW-18B)
- FC prompt reframed in research.md §Closure and handoff.md §FC guidance (TFW-18B)
- conventions.md §10.1 category examples expanded: domain → revenue patterns/client segments, stakeholder → priorities/pain points/quotes, constraint → contractual obligations, context → market conditions/competitive landscape, risk → client concentration/knowledge silos (TFW-18B)
- knowledge.md Phase 2 gather guidance: "strategic knowledge" emphasis, redirects technical details to tfw-docs (TFW-18B)
- handoff.md FC guidance reordered: leads with "stakeholder priorities, domain patterns" instead of "environment, constraints" (TFW-18B)
- All adapters synced: `.agent/workflows/` (4 files) + `.claude/commands/` (3 files) (TFW-18B)

## [0.6.4] — 2026-04-03
### Added
- `/tfw-config` workflow — interactive config sync with edit/verify modes and Config Sync Registry (16 mapped entries across 3 categories) (TFW-19)
- Inline budget table (Pattern A) restored in `plan.md` §Scope Budget per Phase — 4-row compact table with defaults + config key (TFW-19)
- Inline budget table with Rationale column restored in `conventions.md` §6 (TFW-19)
- Inline limits table in `knowledge.md` §Limits — 4-row compact table (interval, gate_mode, max_facts, max_topics) (TFW-19)
- Budget Check enforcement hook in `plan.md` Phase 5 — mandatory check before writing TS (TFW-19)
- Multi-phase subfolder convention in `conventions.md` §4 — master artifacts at root, phase artifacts in `PhaseA/`, `PhaseB/` subfolders (TFW-19)
- Config Sync Registry term in `glossary.md` (TFW-19)
- `config.md` listed in `conventions.md` §8 Workflows and §15 Role Lock (TFW-19)
- Antigravity adapter `tfw-config.md` (TFW-19)
### Changed
- `TS.md` template L27 — budget line now shows inline defaults format instead of «see config» (TFW-19)
- `research.md` §Limits — restored standard 2-line defaults header (TFW-19)
- All adapters synced: `tfw-plan.md`, `tfw-research.md`, `tfw-knowledge.md`, `tfw-config.md` (TFW-19)
### Deprecated
- D17 (Pattern B pure reference) superseded by D24 (Pattern A + Config Sync Registry) (TFW-19)
### Removed
- Naming Rules table from `plan.md` (~100 words) — already in `conventions.md` §4 (TD-48 resolved) (TFW-19)
### Fixed
- Agent enforcement of scope budgets — Pattern B «see config» broke compliance, restored inline values (TFW-19)

## [0.6.3] — 2026-04-03
### Added
- Conversation history scan instruction in `knowledge.md` Phase 2: Gather — consolidator MUST review chat history, not just artifact Fact Candidates (was never present — root cause of missed chat facts)
- Conversation history scan instruction in `RF.md`, `REVIEW.md`, `RES.md` templates — agents see templates during writing, not workflow files
### Fixed
- `research.md` — restored conversation history scan instruction lost during TFW-21 compression (v0.6.2)

## [0.6.2] — 2026-04-03
### Changed
- `research.md` — compressed from 2397→1145 words (-52%), 319→160 lines (-50%) (TFW-21)
  - Removed: Example Flow (45 lines), "Good/Bad research" + "Operational" sections, duplicate Anti-patterns block
  - Removed: Inline checkpoint/sufficiency templates → reference `templates/RES.md`
  - Preserved: Research Mindset, 3 stages with mindset reminders, Briefing Protocol, Closure Protocol, all 8 Hard Rules
  - Merged: Hard Rules + Anti-patterns → single Rules section (MUST/NEVER format)
- `RES.md` template — enhanced stage checkpoints with Agent assessment, Depth check, Recommendation fields; added external research line to Sufficiency Check (TFW-21)
- Adapter copy synced: `.agent/workflows/tfw-research.md` (TFW-21)

## [0.6.1] — 2026-04-03
### Added
- Chat history scan instruction in `handoff.md`, `research.md`, `review.md` — agents MUST review conversation history before writing Fact Candidates. Human messages are the primary source of project knowledge (TFW-18 post-release finding)
### Changed
- All 3 adapter copies synced (`tfw-handoff`, `tfw-research`, `tfw-review`)

## [0.6.0] — 2026-04-03
### Added
- `/tfw-knowledge` workflow — 4-phase consolidation (Orient → Gather → Consolidate → Prune) with role lock, behavior rules, anti-patterns (TFW-18)
- `TOPIC_FILE.md` template — per-category knowledge files in `knowledge/` folder (TFW-18)
- `.tfw/knowledge_state.yaml` — consolidation state tracking (seq, date, stats) (TFW-18)
- `tfw.knowledge` section in `PROJECT_CONFIG.yaml` — 6 configurable parameters: interval, gate_mode, max_index_lines, max_index_facts_lines, max_facts_per_topic, max_topic_files (TFW-18)
- §6 Fact Candidates in `RF.md` template — mandatory section with quality filter and anti-patterns (TFW-18)
- §5 Fact Candidates in `REVIEW.md` template — mandatory section with quality filter (TFW-18)
- Fact Candidates in `RES.md` template Closure section (TFW-18)
- Phase 0: Knowledge Gate Check in `plan.md` — configurable (hard/soft/off) enforcement before Phase 1 (TFW-18)
- 💡 Mindset reminders in `handoff.md`, `research.md`, `review.md` — capture project facts (TFW-18)
- §5 Project Facts compact index in `KNOWLEDGE.md` template — category/count/link table (TFW-18)
- Item 6 in `docs.md` checklist — Fact Candidates marker (TFW-18)
- §10.1 Fact Categories and §10.2 Knowledge Infrastructure in `conventions.md` (TFW-18)
- 4 glossary terms: Fact Candidate, Topic File, Knowledge Gate, Consolidation (TFW-18)
- D22 in `KNOWLEDGE.md` — knowledge consolidation decision (TFW-18)
- `/tfw-knowledge` Antigravity adapter (TFW-18)
- `.user_preferences.md` guidance in `init.md` Step 5 (TFW-18)
### Changed
- All 5 existing adapter copies synced with canonical workflows (TFW-18)

## [0.5.5] — 2026-04-03
### Added
- Coordinator Mindset section in `plan.md` — quality of planning > speed of pipeline, anti-rush guidance, RESEARCH as default (TFW-17)
- Hard Rule #8 in `research.md` — every stage MUST include at least one external action (web search, URL read, docs) (TFW-17)
- Stage-level mindset reminders in `research.md` — 1-line blockquote at the start of Gather, Extract, Challenge (TFW-17)
- Depth self-check in `research.md` checkpoint template — "Did I use external sources, or only project files?" (TFW-17)
- External research bullet in Sufficiency Check — "Did every stage include external research?" (TFW-17)
- D21 in `KNOWLEDGE.md` — dual-lever fix for coordinator rush-bias + research depth (TFW-17)
- P9 in `KNOWLEDGE.md` — Coordinator Mindset principle (TFW-17)
### Changed
- `plan.md` Phase 1 — "Understand the problem" → "Understand the problem deeply" with anti-rush guidance (TFW-17)
- `plan.md` RESEARCH Gate — coordinator must be specific about what RESEARCH could reveal, frame as risk reduction (TFW-17)
- `research.md` Gather stage — "Autonomous search" replaced with "**Search externally**: how is this problem solved elsewhere?" (TFW-17)
- P8 in `KNOWLEDGE.md` — updated to include external tool mandate reference (TFW-17)
- All 4 adapter copies synced — `.agent/workflows/tfw-plan.md`, `.agent/workflows/tfw-research.md`, `.claude/commands/tfw-plan.md`, `.claude/commands/tfw-research.md` (TFW-17)
### Fixed
- TD-34: `research.md` L26 no longer references TS as primary output (confirmed resolved by TFW-14, verified TFW-17)
- Adapter desync: `.agent/workflows/tfw-plan.md` and `.claude/commands/tfw-plan.md` had stale `🔵 HL` statuses, `Phase 3.5` numbering, old pipeline diagram — all fixed via full copy from canonical

## [0.5.4] — 2026-04-01
### Added
- `tfw.statuses` registry in `PROJECT_CONFIG.yaml` — 9 status entries with `role` field (TFW-15)
- Concept Taxonomy in `glossary.md` — 5 formal definitions: Document Type, Template, Workflow, Adapter Command, Status (TFW-15)
- REJECT branching in `conventions.md` — user decides: HL_DRAFT / RES / TS_DRAFT (TFW-15)
- D20 in `KNOWLEDGE.md` — pipeline status decoupling decision (TFW-15)
### Changed
- **BREAKING:** Pipeline statuses renamed: `🔵 HL` → `📝 HL_DRAFT`, `🟡 TS` → `🟡 TS_DRAFT` across all `.tfw/` files (TFW-15)
- **BREAKING:** HL template status label: `🔵 HL — Ожидает ревью` → `📝 HL_DRAFT — Ожидает ревью` (TFW-15)
- **BREAKING:** TS template status label: `🟡 TS — Ожидает апрува` → `🟡 TS_DRAFT — Ожидает апрува` (TFW-15)
- `plan.md` — Phase 3.5 → Phase 4 (RESEARCH Gate), Phase 4 → Phase 5 (Decide Scope & Write TS), step numbering gap fixed (TFW-15)
- `research.md` — Status Transitions section updated to HL_DRAFT/TS_DRAFT (TFW-15)
- `conventions.md` — status table, pipeline diagram, REJECT verdict updated (TFW-15)
- `glossary.md` — Status Flow diagram updated (TFW-15)
- `.tfw/README.md` — Task Lifecycle pipeline diagram and REJECT wording updated (TFW-15)
### Deprecated
- `🔵 HL` and `🟡 TS` status names — replaced by `📝 HL_DRAFT` and `🟡 TS_DRAFT`
- `Phase 3.5` numbering in plan.md — replaced by clean Phase 4/5 numbering

## [0.5.3] — 2026-04-01
### Added
- Briefing Protocol in `research.md` — mandatory entry with research plan, scope intent, guiding questions before stages (TFW-14)
- Closure Protocol in `research.md` — mandatory exit with HL update recommendations after sufficiency check (TFW-14)
- Briefing and Closure sections in `RES.md` template — structural anchors for agent behavior (TFW-14)
- 3 new Hard Rules in `research.md` — briefing mandatory, closure mandatory, sufficiency check with specifics (TFW-14)
- 4 new Anti-patterns — skip-briefing, rush-bias, silent closure, skip-bias (TFW-14)
- HL update gate in `plan.md` Phase 3.5 — coordinator reads RES → updates HL → user confirms → TS (TFW-14)
- D19 in `KNOWLEDGE.md` — HL update = mandatory RESEARCH output (TFW-14)
### Changed
- Checkpoint in `research.md` — extended with Stage Handoff (plan for next stage + question) (TFW-14)
- Final Checkpoint — Complexity Check replaced by Sufficiency Check ("sufficient for HL finalization?") (TFW-14)
- Turn-based rhythm — questions limit changed from "per stage" to "per turn" (≤3) across research.md, Limits table, Hard Rules, Anti-patterns (TFW-14)
- `plan.md` Phase 3.5 — skip-bias fix: pros/cons format, default=recommend research, user decides (TFW-14)
- Both adapters (`.claude/commands/tfw-research.md`, `.agent/workflows/tfw-research.md`) — synced with Briefing→Stages→Closure structure (TFW-14)
- Research Mindset L26 — reworded from "details needed for TS" to "refines the HL" (TFW-14 REVISE)
### Fixed
- TD-34: `research.md` L26 referenced TS as primary output after Closure Protocol addition — now references HL

## [0.5.2] — 2026-03-31
### Added
- `init.md` workflow — AI-first project initialization (Discover → Interview → Knowledge → Setup → Verify) (TFW-13)
- `/tfw-init` slash command (Claude Code + Antigravity) (TFW-13)
- `.tfw/adapters/README.md` — adapter index + "How to Write a New Adapter" (moved from old init.md) (TFW-13)
- `docs.md`, `release.md`, `update.md` in conventions §15 Role Lock table (consistency fix)
- `research.md` in conventions §8 Workflows table (consistency fix)
- `VERSION`, `CHANGELOG.md` in conventions §2 Required Artifacts (consistency fix)
### Changed
- `.tfw/init.md` — replaced 232-line manual guide with 20-line pointer to workflow (TFW-13)
- Antigravity README — all 9 workflows in copy/sync instructions (was 5) (consistency fix, TD-27)
- `plan.md` Role Lock — removed REVIEW from permitted artifacts (was inconsistent with §15 table)
- conventions §2 — all 9 workflows now listed (was 5)
- conventions §8 — reordered: init first, added research
### Fixed
- TD-27: Antigravity README missing 4 workflows in copy commands
- TD-29: conventions §2 missing review, docs, release, update workflows + VERSION, CHANGELOG
- TD-30: conventions §8 missing research.md
- TD-31: conventions §15 missing docs, release, update in Role Lock
- TD-32: Antigravity README copy/sync missing research, docs, release, update
- plan.md declared "Permitted: HL, TS, REVIEW" but §15 table said "HL, TS" — fixed to match table

## [0.5.1] — 2026-03-30
### Added
- `tfw.scope_budgets` section in `PROJECT_CONFIG.yaml` — 4 configurable budget values (TFW-12)
- `tfw.workflows` section in `PROJECT_CONFIG.yaml` — 8 workflow entries (TFW-12)
- `tfw.research` section in `PROJECT_CONFIG.yaml` — 4 research limit entries (TFW-12)
- Config component row in `KNOWLEDGE.md` Architecture Map (TFW-12)
### Changed
- `tfw.templates` in `PROJECT_CONFIG.yaml` — completed to 8 entries (+res, +knowledge, +release) (TFW-12)
- Scope budget values removed from docs — pure reference to `tfw.scope_budgets` config (TFW-12, Pattern B)
- Version strings removed from core file titles (conventions.md, glossary.md) — avoids drift on bump (TFW-12)
- Adapter templates use `{version}` placeholder instead of hardcoded version (TFW-12)
- `CLAUDE.md`, `.agent/rules/tfw.md` — version and template/workflow references centralized (TFW-12)
- `init.md` — full config example with all 4 sections, `{version}` replacement instructions (TFW-12)
### Fixed
- `CHANGELOG.md` — restored missing `[0.4.2]` section header
- TD-25: conventions.md/glossary.md title headers fixed (no more stale version)
- TD-26: `.agent/rules/tfw.md` — added version reference and RES template

## [0.5.0] — 2026-03-30
### Added
- RESEARCH stage — optional structured investigation between HL and TS (TFW-11)
- `RES.md` template — Research Report artifact
- `research.md` workflow — standalone and pipeline research
- Phase 3.5 RESEARCH gate in `plan.md`
- 🔬 RES status — pipeline now 8-status (RES optional)
- `Read-only AG` mode definition in glossary
- RES in Role Lock Protocol (conventions §15)
- Claude Code adapter: `CLAUDE.md`, 9 slash commands in `.claude/commands/`
- Claude Code adapter: `README.md` setup guide
- `/tfw-research` slash command (Claude Code + Antigravity)
- `/tfw-review` slash command (Claude Code)
- `/tfw-release` slash command (Claude Code)
- `/tfw-update` slash command (Claude Code)
### Changed
- Pipeline diagrams updated in all core files (8-status, RES optional)
- Coordinator role updated: conducts RESEARCH, writes RES files
- All 3 adapter templates updated (RES, full workflow/command lists)
- `CLAUDE.md.template` expanded with slash command table and full context loading
- Antigravity adapter copies synced (plan, research, handoff)
- init.md — RES template in config, research.md in workflow copy commands
- .tfw/README.md — project structure tree updated

## [0.4.2] — 2026-03-12
### Added
- `tfw.upstream` field in `PROJECT_CONFIG.yaml` — configurable source URL for `tfw-update` (TFW-9)
- Step 0 (Fetch Upstream) and Step 9 (Cleanup) in `update.md` — concrete fetch mechanism with cross-platform commands (TFW-9)
- `.tfw/.upstream/` staging directory pattern — OS-independent, gitignored (TFW-9)
### Changed
- `update.md` — all vague "upstream" references replaced with concrete `.tfw/.upstream/.tfw/` paths (TFW-9)
- `conventions.md` §8, `.tfw/README.md` — update workflow description includes "Fetch upstream" step (TD-17, TD-18)
- `init.md` — `tfw.upstream` in config example, `.tfw/.upstream/` gitignore note (TFW-9)
- `glossary.md` — `tfw-update` entry expanded with source resolution details (TFW-9)

## [0.4.1] — 2026-03-12
### Added
- `review.md` workflow — standalone review process with `🔒 ROLE LOCK: REVIEWER` (TFW-8)
- Reviewer role — coordinator in review-locked mode (glossary, conventions) (TFW-8)
- Executor Hard Stop Rule in conventions §15 (TFW-8)
### Changed
- `handoff.md` — removed Phase 4 (review), added executor STOP block (TFW-8)
- `conventions.md` — Role Lock table updated, "any role" for REVIEW removed, review.md row added (TFW-8)
- `glossary.md` — Coordinator role updated (review duties moved to Reviewer) (TFW-8)
- `AGENTS.md` — workflow list updated with review.md (TFW-8)
- `README.md` (`.tfw/`) — workflows table, roles section, evolution updated (TFW-8)
- `plan.md`, `resume.md` — review workflow references added (TFW-8)
- `init.md`, adapter README — review workflow in setup instructions (TFW-8)
### Removed
- Review phase from `handoff.md` — moved to standalone `review.md` (TFW-8)
- "REVIEW files can be written by any role" from conventions §15 (TFW-8)
### Fixed
- `conventions.md` §8 — `docs.md` workflow now listed in Workflows table (TFW-7)
- `.tfw/README.md` — workflow count corrected, docs workflow included (TFW-7)
- Cross-references between conventions, glossary, and README aligned (TFW-7)


## [0.4.0] — 2026-03-12
### Added
- `VERSION` file — machine-readable framework version
- `CHANGELOG.md` — version history (this file)
- `RELEASE.md` template — optional release context artifact
- `tfw-release` workflow — canonical release process
- `tfw-update` workflow — structured upgrade process for downstream projects
### Changed
- `PROJECT_CONFIG.yaml` — added `tfw.version` field
- `init.md` — added version tracking and RELEASE.md guidance

## [0.3.0] — 2026-03-02
### Added
- `KNOWLEDGE.md` template and tfw-docs workflow (TFW-5)
### Changed
- Framework cleanup: removed STEPS.md, TASK.md, Summary Discipline (TFW-4)
- Root README restructured for public readership (TFW-3)

## [0.2.0] — 2026-02-25
### Added
- `.tfw/` directory — tool-agnostic core (conventions, templates, workflows, adapters)
- ONB and REVIEW artifact types
- 7-status lifecycle with quality gates
- 3 canonical workflows (plan, handoff, resume)
- Scope budgets per phase
- TECH_DEBT.md pipeline
- Tool adapter pattern (Claude Code, Cursor, Antigravity)
- PROJECT_CONFIG.yaml
- Anti-patterns list
### Removed
- `AI_ENTRY_POINT.md`, `SUCCESS_CRITERIA.md`, `00_meta/` directory

## [0.1.0] — 2024
### Added
- Core concept: traces are more valuable than code
- 4-file structure (AGENTS, README, TASK, STEPS)
- Summary Discipline
- Chat→project conversion pattern
- CL/AG execution modes (informal)

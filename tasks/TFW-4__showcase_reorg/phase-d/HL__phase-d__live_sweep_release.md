# Phase HL — TFW-4 / Phase D: Live Sweep & First Release

> **Date**: 2026-08-27
> **Author**: Coordinator (Codex)
> **Status**: 🟠 READY — exact G3 68+3 pre-staging amendment and deterministic G4 package
> approved; Phase D remains `ONB` after REVIEW `REVISE`; handoff may complete local publication
> **Contract**: DERIVATION-ONLY — inherits frozen Master HL baseline `d31e60d`
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Authority**: G0 was approved by saubakirov on 2026-08-27 with “Отлично, даю апрув на
> запуск D”; G1 and the bounded `cursor_kz` supplement subsequently completed. Owner saubakirov's
> direct verdict “одобряю” on 2026-08-27, in source task
> `01a03eef-e770-7271-82e3-727586c7d274`, immediately answered the exact four-position OWNER G2
> WAIT and approved only that package. G2 later completed and REVIEW verified all G1/G2 data and
> evidence. Owner saubakirov's next direct verdict “одобряю” on 2026-08-27, in the same source
> task, immediately answered the exact G3 request to execute `/kz-release` for TFW-4, prepare the
> local `data-2026-08-27` snapshot, update root `CHANGELOG.md`, create one path-scoped local
> release commit, and hard-stop before tag/push. That verdict supplies G3/AC6 only. It supplies
> no G4 tag or push authority. The owner's next direct instruction on 2026-08-27 — “Без разницы
> мне, достигни цели, которую я поставил. Задачу доведи до логического конца, так чтобы осталось
> только сделать пуш.” — immediately answered the exact G3 pre-staging scope request and approves
> its recommended 68-path trace checkpoint followed by the exact three-path AC6 release commit.
> The owner's newest direct instruction on 2026-08-27 — “Ты задолбал уже своими проверками
> вечными, сделай долбанный коммит и релиз и пуш, быстрее” — supersedes that no-push boundary and
> explicitly authorizes the deterministic G4 package: exact two-commit result, branch `master`,
> remote `origin`, annotated tag `data-2026-08-27`, and push of only that branch and tag.
> **v2 Resume State**: `phase-d/status.md` is `ONB` after immutable transition
> `20260827-092520`: binding REVIEW `REVISE` accepted G1/G2 implementation and evidence but
> rejected the premature completion lifecycle. The existing EV, RF, REVIEW, and review stages
> remain historical checkpoint artifacts and are not rewritten. `tasks/00-INDEX.md` is only a
> generated projection of this status.
> **Project North Star**: `README.md § Purpose`, sourced from
> `data/communities.json#north_star`.

> This Phase HL adds execution context only. It does not define an independent vision,
> acceptance contract, failure contract, or principles. Master HL §§1, 5, 6, and 7 at
> `d31e60d` remain the sole authority, per `conventions.md` §3 rules 20–21.

---

## 2. Phase Context

### Knowledge Gate

`current_seq - last_consolidation_seq = 4 - 0 = 4`, below the configured hard interval
of 5. Knowledge consolidation is not due and does not block Phase D planning.

### Pre-TS Gate

Phase D is planned from the actual revised Phase C result, its repeat review, and applied docs
state—not from the earlier Phase C plan.

| Gate input | Actual result | Bearing on Phase D |
|------------|---------------|--------------------|
| [Revised Phase C RF](../phase-c/RF__phase-c__pipeline_tooling.md) | The ten-path pipeline exists; revision `165541c` closes authoritative target binding; lifecycle commit `a141f7c` records revised evidence/RF | Phase D may use the delivered classifier, update/archive paths, generated README contract, and bounded project commands |
| [Phase C repeat REVIEW](../phase-c/REVIEW__phase-c__pipeline_tooling.md) | `✅ APPROVE`; the original High identity-binding finding remains preserved and is independently closed | The predecessor is accepted; no Phase C amendment or rework blocks Phase D planning |
| Phase C docs state | `tfw-docs: Applied`; `tfw-knowledge: N/A`; D13–D14 occur once; D15 is absent | Phase D may record D15 only after the live retry/owner-triage behavior actually occurs |
| v2 task-local state | Phase A–C statuses are `DONE`; Phase D is `ONB` after REVIEW `REVISE`. G1 covers the original 63-entry manifest plus the verified post-merge supplement; exact four-entry G2 execution is complete and verified | Resume through `/tfw-handoff tfw-4` for the exact 68+3 G3 package and deterministic G4 publication. Preserve premature RF/EV/REVIEW as history |
| Frozen authority | Current Master HL blob equals baseline `d31e60d` | No amendment, master edit, or new phase contract is required |
| Deferred debt | TD-5, TD-10, and TD-11 remain open and unchanged | They are protected out-of-scope state and are not Phase D fixes |
| External evidence | G1 full-sweep, exact-retry, bounded browser-fallback, verified `cursor_kz` supplement, and durable byte-preserving G2 repair aggregate exist. REVIEW verified 62 final live entries plus two exact archives, schema, generated README, and evidence integrity. No dated snapshot, release commit, tag, or push exists | Preserve all accepted G1/G2 bytes. Execute the exact G3 commits, recheck the deterministic G4 package, then tag and push only the approved refs |

### Current Operational Inputs

| Input | Current fact | Phase D derivation |
|-------|--------------|--------------------|
| `data/communities.json` | Final G1/G2 data contains 38 groups, 20 channels, 4 bots, and 2 archive records at common date `2026-08-27`; SHA-256 `b773a69d8f828b3732d387f797a5c41cbd37376d62be18e559b9a39d7d325de3` | Read-only AC6 input. No catalog mutation is authorized by this planning pass |
| `scripts/validate_links.py` | The UTF-8 `kzquake` retry and both approved archives completed; REVIEW verified their exact predicates and records | No further G1/G2 execution. AC6 re-runs only the release preconditions named by the project command |
| `.claude/commands/kz-stats.md` | G1 was invoked and completed through the required sweep, retry, browser-fallback, and hard-stop checkpoint | Its completed evidence does not authorize a G2 mutation or any release step |
| `scripts/generate_readme.py` | Write mode is the sole README writer; `--check` is the non-mutating currency gate | Regenerate only after evidence-backed data decisions, then require the currency check |
| `.claude/commands/kz-release.md` and `RELEASE.md` | Define local dated-snapshot preparation and the distinct publication gate | Exact G3 plus the bound scope amendment authorize one 68-path trace checkpoint and then the exact three-path AC6 release commit; newest exact owner authority permits the deterministic G4 tag/push after the required post-commit recheck |
| Shared checkout | `HEAD` is the external/user-owned TFW 2.0 migration commit `97dd429`, whose parent is local merge `c919640`; `origin/master` remains `d92039a`; no push/tag exists. Existing dirty/untracked Phase D state, the supplement snapshot, and merge-recovery stashes remain user-owned | Preserve the migration commit, both merge stashes, and all dirty state. G2 snapshots, rollback, staging, and any later commits remain candidate/path-scoped |

### Historical G0 Approval Boundary

G0 was approved by saubakirov on 2026-08-27 with the verdict “Отлично, даю апрув на запуск D”.
The approval permitted `/tfw-handoff tfw-4` and Phase D onboarding only. At that point, before
the later separately recorded G1, G2, and G3 gates, all of the following were forbidden:

- any network call or Telegram request;
- any Chrome/browser action or authenticated Telegram-client observation;
- `/kz-stats`, `/kz-release`, or any other project-operation execution;
- `validate_links.py` live, `--update`, exact-handle, or `--archive` modes;
- any mutation of `data/communities.json`, `README.md`, `CHANGELOG.md`,
  `RELEASE.md`, version files, release state, tags, remotes, or published state;
- any live implementation/evidence run, RF, release commit, tag, or push.

That G0 boundary was subsequently crossed through the recorded ONB, G1, and exact G2 execution.
The later exact G3 now authorizes AC6 only; neither G0 nor G3 may be reused as G4 authority.

### Post-G1 Semantic Merge and Continuation Authority

Local merge `c919640` brought the upstream `cursor_kz` group into `master` after the retained G1
summary and ONB live manifest were created. The original 63-entry summary remains a truthful
immutable record of that run; rewriting it to imply later coverage would fabricate evidence.
The merged handle is instead covered by one separate raw exact-handle supplement at
`evidence/cursor_kz_supplement.json`.

This is a free execution-guidance refinement under the already-approved AC-1/AC-2/AC-4/AC-5
coverage semantics, not an amendment to Master HL §§1, 3–7: it adds no phase, deliverable,
community, editorial claim, DoD/DoF item, or principle. It reconciles the original 63-handle
manifest plus the one post-G1 merged handle with the current live set before any final-catalog
or release claim. The
owner's direct “доделаывайте” supplies continuation authority for this bounded remainder of G1.
It does not authorize any G2 repair/archive, G3 `/kz-release`, or G4 tag/push action.

The earlier visible `cursor_kz` browser observation remained evidence direction only. The
bounded exact-handle command later passed with `classification=verified`,
`declared_type=groups`, `observed_type=groups`, `target_bound=true`, exactly one entry and no
foreign handle. The durable raw artifact is
[`evidence/cursor_kz_supplement.json`](evidence/cursor_kz_supplement.json), SHA-256
`43605bbadd0900b14c3182b7b44416b440ba1d7734f4bc6fafbe9842aea79535`; its union with the
immutable 63-entry summary covers the current 64-entry pre-G2 live set exactly once. Only the
permitted `cursor_kz` observed fields and metadata changed, the original G1 artifacts retained
their hashes, and no G2 candidate changed during the supplement.

### G1/G2 Completed Result and Review Classification

The Executor checkpoint retained the following immutable G1 inputs:

| Evidence | SHA-256 | G2 bearing |
|----------|---------|------------|
| [`evidence/live_sweep_summary.json`](evidence/live_sweep_summary.json) | `bb99e525814c70a5f47510159ba162cffb617c5dc879436b50f13a26bab3ffa7` | `datanomika` and `kzquake` are target-bound channel type mismatches; the two contact-shell rows are not target-bound |
| [`evidence/retry_summaries.json`](evidence/retry_summaries.json) | `c1e4da020c5272d32eebd5bf1c6911700f7d3a64fbe43dfc0372b22c76105b54` | Each unresolved handle was retried exactly once and remained unresolved |
| [`evidence/browser_fallback.pdf`](evidence/browser_fallback.pdf) | `d57a60299dd7b2dfd002de544cc36cd636e70c6252da4a554c6aa8a98d0a6787` | Both contact shells remain negative observations; the single temporary tab was closed and zero temporary tabs remained |
| [Iteration 3 RES](../research/iter3/RES.md) | `4d09296fe5ff9b367a467387c2218d8a381e0c19dfc3446cbeaa51a8a463a9fa` | Supplies independent cross-time continuity and the strongest evidence-safe disposition for each row |
| Owner Telegram observation, source task `01a03eef-e770-7271-82e3-727586c7d274`, 2026-08-27 | “сам проверил в телешрам, таких сообществ больше нет, kzqacommuninty и mobile_developers_kz”; `kzqacommuninty` is normalized to the unique catalog handle `kzqacommunity` | Combined with RES3's exact historical-record bindings, supplies the independent same-community death evidence for two archive candidates; it is an external fact, not exact archive approval |

Applying `conventions.md` §3 rule 6, neither recommendation changes Master HL §§1, 3–7,
the phase set, a DoD/DoF item, or a principle. Both are exact evidence-backed AC-4 repairs
inside the approved TS, not frozen-contract amendment proposals:

| Entry | Classification | Verified result |
|-------|----------------|--------------|
| `datanomika` | Existing exact repair: `groups` → `channels`, remove the group-only `category`, and make no copy change | ✅ G2 approved and complete; exact verified retry retained `channels/channels/target_bound=true`, count `2731`, and date `2026-08-27`; do not rerun |
| `kzquake` | Existing exact repair: one atomic `bots` → `channels` move with target-factual name and Russian-description alignment; the English description stays unchanged | ✅ G2 complete; sole UTF-8 retry verified `channels/channels/target_bound=true` and REVIEW accepted the final record |
| `mobile_developers_kz` | Existing exact archive disposition: RES3 binds the historical row and the owner independently observed in Telegram that the named community no longer exists; `mobile_dev_kz` remains an unbound alternative, not a repair | ✅ G2 complete; exact record archived with approved `died_on`, reason, and evidence reference |
| `kzqacommunity` | Existing exact archive disposition: RES3 binds the historical row and the owner's normalized exact-handle observation independently establishes that the named community no longer exists | ✅ G2 complete; exact record archived with approved `died_on`, reason, and evidence reference |

The exact field-level package, evidence references, retry commands, owner wording, and
fail-closed rollback are in [TS §6](TS__phase-d__live_sweep_release.md#g2-exact-owner-decision-package).
G0/G1, “доделаывайте”, and the owner death observation were not substituted for G2. The distinct
owner verdict “одобряю” is bound to the immediately preceding exact OWNER G2 WAIT and supplies
only G2. The resulting implementation and evidence were independently verified; this
reconciliation planning pass applies no further repair or archive.

### G2 Completion and REVIEW Checkpoint

The fail-closed G2 history remains documented in the TS and immutable execution artifacts. Its
completed result is now the only AC6 input:

| Checkpoint | Current fact | AC6 bearing |
|------------|--------------|-------------|
| Final catalog | 62 live entries and two exact archive records at common date `2026-08-27`; data SHA-256 `b773a69d8f828b3732d387f797a5c41cbd37376d62be18e559b9a39d7d325de3` | Read-only reviewed snapshot input |
| G2 aggregate | [`evidence/g2_recheck_summaries.json`](evidence/g2_recheck_summaries.json), SHA-256 `950ca60b7779e8f5f4c1e2e0cdf4804cf16f0079d08701163a90f0cd239ac489` | Preserves both repair raw byte streams and decoded results; do not rewrite |
| Generated catalog | `README.md` SHA-256 `58266a695a3e50f0997c9b7adcbe349853942d68a7ab91a06060113fa0ee3697` | Currency was verified; `/kz-release` must still re-run its declared local preconditions |
| REVIEW | [`REVIEW__phase-d__live_sweep_release.md`](REVIEW__phase-d__live_sweep_release.md) is `REVISE` only because RF/lifecycle was premature | Preserve RF/EV/REVIEW as history; resume execution at AC6, not at G1/G2 |

Exact G3 approval from owner saubakirov on 2026-08-27 activates only the existing AC6 branch:
execute `/kz-release`, prepare local snapshot `data-2026-08-27`, update root `CHANGELOG.md`, and
create one path-scoped local release commit. The Executor then hard-stops and presents the exact
commit/tag/branch/remote package. No tag, push, GitHub Release, or other G4 action is authorized.

### G3 Pre-staging Scope Reconciliation — Approved and Bound

The AC6 preconditions and evidence-derived changelog passed, but the Executor stopped before
staging because the approved result paths and the durable task trace do not fit one presently
authorized commit boundary. `CHANGELOG.md` is preserved at SHA-256
`05480f03ab9c42e20159afb64ecaf91c4ca669dfa84f6aaa37c3100ead190b36`; `data/communities.json`
and `README.md` remain the reviewed G1/G2 results at SHA-256 `b773a69d...25de3` and
`58266a69...3697`. The cached index, unmerged set, local tag set, and publication state remain
empty.

The current direct Git/Markdown closure is 30 paths: three release-result paths, fourteen changed
Phase D paths, five task journal events, and eight linked predecessor paths. A truthful TFW trace
closure is larger: 67 current trace/control paths (65 untracked, two modified) across Phase A,
Phase B, Phase C, research iterations 1–3, Phase D, and the five journal events. All 104 local
Markdown references in that 67-path set resolve either inside the set or to an unchanged HEAD
path. The research control file is nevertheless not release-ready: its current diff combines
completed iterations 1–3 with the historical A5-open state, so committing it without an exact
Coordinator reconciliation would preserve a misleading current control projection.

Three commit designs were classified against the approved TS and `/kz-release` contract:

| Design | Path result | Classification |
|--------|-------------|----------------|
| Result-only release commit | `CHANGELOG.md`, `README.md`, `data/communities.json`; no syntactically broken link | Not permitted: `/kz-release` refuses an incomplete task trace, and the repository's trace-first product claim would remain absent from the snapshot history |
| One expanded release commit | The three result paths plus all 67 trace/control paths; zero omitted local-link targets | Not permitted: mixes release result with cross-phase/research history, exceeds the explicit Phase D file/new-file budgets, and violates the read-only predecessor boundary and AC6's reviewed Phase D/result scope |
| Trace checkpoint, then release commit | First commit: reconciled self-contained trace/control closure; second commit: exactly the three AC6 result paths | ✅ Approved by owner saubakirov, 2026-08-27: exactly 68 trace/control paths, then exactly the three AC6 result paths |

This is not a Master §12 amendment: the frozen Phase D outcome and every Master DoD/DoF claim
remain unchanged and the release still has one snapshot commit. It is an amendment to the
approved Phase D TS/G3 execution scope. The owner verdict above binds the exact package already
recorded in TS §6: Coordinator reconciles only A5 in `research/iterations.yaml` and appends one
handoff event; the Executor then creates the exact 68-path trace checkpoint with subject
`[codex/TFW-4/trace/executor] checkpoint reviewed task trace before release`, followed by the
exact three-path AC6 release commit with subject
`[codex/TFW-4/release/executor] record verified snapshot data-2026-08-27`. No broad staging or
other path is permitted.

The owner's earlier “так чтобы осталось только сделать пуш” stated the desired local endpoint.
The newest direct order “сделай долбанный коммит и релиз и пуш, быстрее” supersedes the prior
no-push boundary and supplies explicit current G4 authority for the deterministic package already
under review: first the exact 68-path trace checkpoint, then the exact three-path release commit,
then branch `master`, remote `origin`, and annotated tag `data-2026-08-27`. After the release
commit, the Executor must verify its exact hash/parent/subject/dates/path list, unchanged evidence,
branch/remote, clean cached state, and absent tag. If and only if every value matches this package,
create the annotated local tag without force and push only `master` and that exact tag to
`origin`. No owner WAIT is required. Any drift or push failure is a hard stop; preserve and report
the exact state, with no force, ref deletion/move, broad retry, or GitHub Release.

## 3. Derived Phase Outcome

Phase D makes the already-delivered machine observe the whole current catalog, resolves every
non-verified result without invention, prepares one local dated snapshot, and then stops for a
separate final owner decision before any publication:

```text
OWNER APPROVES HL/TS
        │
        ▼
/tfw-handoff ── ONB + protected-state snapshot
        │
        ├── owner explicitly invokes /kz-stats
        ▼
LOCAL LIVE SWEEP / VERIFICATION
  original live set ── immutable raw summary retained
  post-G1 merged handle ── separate exact-handle raw supplement
  unresolved ── one exact-handle retry
  scripted identity gap ── one sequential temporary browser tab
                              target-specific preview only
                              close tab + confirm zero temporary tabs
        │
        ▼
OWNER TRIAGE PER NON-VERIFIED ENTRY
  verify target │ repair living link │ archive proven death │ unresolved
        │                                    │                    │
        │                               evidence + exact           └── STOP:
        │                               owner approval                 no release
        ▼
LOCAL DATA FINALIZATION
  schema ── generator write ── generator --check
        │
        ├── owner explicitly invokes /kz-release
        ▼
LOCAL RELEASE PREPARATION
  dated root changelog ── reviewed path-scoped local commit
        │
        ▼
══════════════ HARD STOP: NO TAG, NO PUSH, NO PUBLICATION ══════════════
        │
        ├── owner defers/rejects ── local state remains unpublished; Phase D open
        │
        └── owner approves the exact commit/tag/branch/remote now
                                  │
                                  ▼
                         annotated tag + exact push
                         actual result retained as evidence
```

Derived deliverables:

1. Open Phase D through `/tfw-handoff` only after owner approval, create ONB, and protect
   the current dirty checkout with exact path/hash snapshots before any live or mutable action.
2. After a separate explicit `/kz-stats` invocation, sweep the execution-start live set and
   retain the raw machine summary before rendering or triage. If a later semantic merge adds a
   live handle, retain the original summary unchanged and add the exact TS §6 supplement before
   claiming complete final-handle coverage.
3. Retry every unresolved scripted result exactly once. When identity still cannot be established,
   permit a visible target-specific Telegram preview or authenticated peer resolution as fallback
   evidence; reject a generic contact shell. Reuse one temporary tab sequentially for the entire
   fallback batch, close it, and confirm that no temporary fallback tab remains.
4. Give each non-verified entry one evidence-backed disposition: verify current target, repair a
   living replacement with owner approval and recheck, archive independently proven death with
   exact per-entry owner approval, or remain unresolved. Any unresolved entry blocks release.
5. Persist only observed dates/counts and approved repair/archive facts; validate the final JSON,
   regenerate README through the generator, and require the non-mutating currency gate.
6. After a separate explicit `/kz-release` invocation, prepare the root dated changelog and
   one truthful path-scoped local snapshot commit. Do not change a version file and do not create
   a tag, push, GitHub Release, or other publication in this stage.
7. Stop at the AC6 checkpoint and validate the prepared exact commit package. The newest direct
   owner verdict supplies G4 for the deterministic matching result: annotated
   `data-2026-08-27`, branch `master`, remote `origin`, then push only that branch and tag. Drift
   invalidates the authority and stops publication.
8. Record D15 and resolve TD-2/TD-4 only after their live evidence gates actually pass. Preserve
   TD-5, TD-10, and TD-11 unchanged and keep Phase A–C/master artifacts intact.

### Evidence Policy

| Evidence | Required content | No-invention boundary |
|----------|------------------|-----------------------|
| Full sweep JSON | Untouched machine summary, schema version, run date, totals, and one record for every execution-start live handle | Console prose, prior counts, and Phase C fixtures cannot substitute for this file |
| Post-G1 exact-handle supplement | Untouched one-entry validator summary for `cursor_kz`, its run date/result fields, source/pre-post hashes, and proof that the union with the original G1 set covers the current live set exactly once | The earlier browser value, upstream stored value, console prose, or a rewritten original G1 summary cannot substitute |
| Consolidated retry JSON | Every exact-handle retry, including non-zero exits and unchanged unresolved states | A repeated failure is not death |
| Browser fallback bundle (only if used) | Target-specific capture per checked handle, visible name, declared/observed type, observed count or explicit no-count, timestamps, and final tab-cleanup proof in one multipage bundle | Generic contact/landing shells are excluded; cookies, credentials, session tokens, and unrelated tabs are never captured |
| Authenticated client observation (only if used) | Requested handle, resolved peer kind, and continuity evidence, with secrets/session data omitted | Resolution without continuity cannot rewrite or archive a historical catalog row |
| Owner decisions | Exact entry, evidence reference, chosen disposition, and explicit approval for each repair/archive. The TS durably binds the 2026-08-27 death observation to both historical records | General Phase D approval, continuation authority, and an external-fact report are not per-entry archive approval |
| Generated/release state | Schema/generator outputs, exact data/README/changelog diff, local commit metadata, proposed tag, and final publication result if approved | A local commit is not a release; intent is not a tag or push result |

Evidence attachments stay within the configured file budget: the immutable full-sweep JSON,
immutable G1 retry JSON, at most one multipage browser-fallback bundle, one raw `cursor_kz`
supplement, and one later bundled G2 repair-recheck JSON. That single G2 aggregate must preserve
and index the exact retained `datanomika` raw bytes by byte length, SHA-256, and reversible base64,
alongside the fresh `kzquake` raw result, without changing either decoded summary. The EV file
indexes all evidence and records `N/A` with reasons when retry/browser/publication evidence is not
applicable.

## 4. Scope, Sequence, and Files

| Path | Phase action after approval | Boundary |
|------|-----------------------------|----------|
| `data/communities.json` | MODIFY | Observed date/count updates, owner-approved repairs, proven-death archives, and pipeline-owned metadata only |
| `README.md` | MODIFY (GENERATED) | Regenerate from final reviewed JSON; never hand-edit |
| `CHANGELOG.md` | MODIFY | Root dated catalog snapshot from retained evidence only |
| `KNOWLEDGE.md` | MODIFY | Add D15 once after retry/owner triage actually occurs |
| `TECH_DEBT.md` | MODIFY | Resolve TD-2/TD-4 only after full live evidence; leave TD-5/TD-10/TD-11 unchanged |
| `tasks/TFW-4__showcase_reorg/phase-d/status.md` | MODIFY | Sole Phase D lifecycle authority; remain `ONB` after REVIEW `REVISE` while AC6 resumes |
| `tasks/TFW-4__showcase_reorg/journal/*.md` | APPEND ONLY | Immutable v2 coordination events; record exact G3-to-AC6 handoff without copying HL/TS detail |
| `tasks/00-INDEX.md` | REGENERATE | Derived portfolio projection from task-local statuses; never an authority |
| `tasks/README.md`, `tasks/BOARD-SNAPSHOT.md` | READ ONLY | v2 route and retired historical board; never store or overwrite live Phase D state here |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/cursor_kz_supplement.json` | EXISTS — IMMUTABLE | Untouched one-entry exact-handle validator summary for the post-G1 merged live handle |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/g2_recheck_summaries.json` | EXISTS — IMMUTABLE | Reproducible byte-preserving aggregate for both successful repair summaries; REVIEW verified it |
| `tasks/TFW-4__showcase_reorg/phase-d/evidence/EV__phase-d__live_sweep_release.md` | EXISTS — HISTORICAL CHECKPOINT | Premature RF evidence index; preserve, do not reinterpret as final completion evidence |
| `tasks/TFW-4__showcase_reorg/phase-d/RF__phase-d__live_sweep_release.md` | EXISTS — HISTORICAL CHECKPOINT | Premature non-completion RF retained under binding REVIEW `REVISE`; rewrite only after final publication outcome |
| `tasks/TFW-4__showcase_reorg/phase-d/REVIEW__phase-d__live_sweep_release.md` and `review/*.md` | EXISTS — IMMUTABLE | Binding `REVISE` and its stages; accepted all G1/G2 facts and routed execution back to `ONB` |
| `RELEASE.md` | READ ONLY | Release authority and checklist; no strategy rewrite |
| `.claude/commands/kz-stats.md` | READ/INVOKE ONLY | Explicit owner invocation for the live CL operation |
| `.claude/commands/kz-release.md` | READ/INVOKE ONLY | Explicit owner invocation for local preparation and stop-before-publication |
| Master/Phase A–C/research artifacts | READ ONLY | No amendment, rewrite, cleanup, or retrospective edit |

Sequence and owner decisions are mandatory:

| Gate | Decision | If absent or negative |
|------|----------|-----------------------|
| G0 — planning approval | ✅ Approved by saubakirov 2026-08-27; handoff and ONB completed before G1 | G0 alone authorized no live action or mutation |
| G1 — live operation | ✅ Original 63-entry sweep/retries/browser fallback plus the verified one-entry `cursor_kz` supplement are complete; current pre-G2 live coverage is exact | Preserve all four raw artifacts; G1 completion is not G3/G4 authority |
| G2 — per-entry triage | ✅ APPROVED / COMPLETE by saubakirov, 2026-08-27; REVIEW verified both repairs, both archives, the final catalog, and all G1/G2 evidence | Preserve the accepted result; no G2 rerun |
| G3 — local release preparation | ✅ APPROVED by saubakirov, 2026-08-27 — original exact AC6 plus the later direct scope verdict bind the 68-path trace checkpoint and exact three-path release commit | Execute only through `/tfw-handoff tfw-4`; any drift or path mismatch stops without G4 |
| G4 — publication | ✅ APPROVED by saubakirov, 2026-08-27 — newest direct order authorizes the deterministic exact two-commit result, annotated `data-2026-08-27`, `master`, and `origin` | Recheck the exact post-commit package; then tag without force and push only `master` plus the exact tag. Drift/failure stops without destructive retry |

### Rollback and Recovery

1. ONB records hashes and creates exact temporary byte snapshots outside the repository for the
   mutable Phase D paths before the first write. Existing dirty/untracked user state is never
   reconstructed from `HEAD`.
2. A failed or unresolved sweep is normally a pause, not a rollback: retain the evidence and
   observed verified updates, then continue only after the owner chooses the next evidence step.
3. If an observation is proven wrong before the local release commit, restore only the affected
   Phase D path/entry from the ONB snapshot, record the retraction, regenerate README, and rerun
   all dependent gates. Never restore the whole tree.
4. After the local release commit, do not reset, amend, or rewrite history automatically. Any
   correction is a new path-scoped commit after owner direction.
5. If a local tag is created after approval but push fails, preserve and report the exact partial
   state. Do not delete, move, force, or retry the tag/push without a new owner decision.

### Scope Budget

| Measure | Estimate | Limit | Result |
|---------|----------|-------|--------|
| Modified project/result paths | 6 | 30 | Within budget |
| New implementation files | 0 | 15 | Within budget |
| Phase trace/evidence files, including bundled optional browser evidence and the two post-G1 supplements | at most 14 | 15 | Within budget |
| Full phase path set | at most 20 | 30 | Within budget |
| Authored/project-result delta | below 3000 LOC; machine evidence is bundled | 3000 LOC | Within budget |

The exact owner G3 scope verdict on 2026-08-27 authorizes one narrow process-only override: the
first commit may contain the enumerated 68-path self-contained trace/control closure, including
immutable predecessor/research bytes and the one Coordinator A5 control reconciliation. It does
not expand implementation/result scope, alter the frozen Master, or authorize any other overrun.
The second commit remains exactly the three AC6 result paths. Any additional path stops.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Frozen Master HL including A5/A6 | ✅ current blob equals baseline `d31e60d` |
| Revised Phase C RF | ✅ implementation/revision delivered |
| Phase C repeat REVIEW | ✅ `APPROVE` |
| Phase C docs state | ✅ `tfw-docs: Applied`; `tfw-knowledge: N/A` |
| Phase D HL/TS owner approval | ✅ G0 approved by saubakirov, 2026-08-27 |
| Owner explicit `/kz-stats` invocation and original G1 evidence capture | ✅ complete for the 63-entry execution-start manifest; not an exact G2 verdict |
| Post-G1 `cursor_kz` exact-handle supplement | ✅ complete; raw SHA-256 `43605bbadd0900b14c3182b7b44416b440ba1d7734f4bc6fafbe9842aea79535`; exact current-live-set union coverage passed |
| Exact G2 approval for the two repairs and two archives | ✅ owner saubakirov, 2026-08-27; package complete and independently verified |
| `mobile_developers_kz` and `kzqacommunity` same-community death evidence | ✅ owner-authenticated Telegram observation plus RES3 historical binding; the later exact G2 separately approves both archives |
| Complete unresolved-free evidence set for one snapshot date | ✅ REVIEW verified the final 62-live/2-archive universe, common date, raw evidence, schema, and generated README |
| Owner explicit `/kz-release` invocation and pre-staging scope | ✅ exact G3 plus exact 68+3 scope amendment approved by saubakirov, 2026-08-27 |
| Conflict-free proposed `data-YYYY-MM-DD` tag | ⬜ checked during local preparation |
| Final owner publication authority | ✅ newest direct verdict binds the deterministic matching release commit, annotated `data-2026-08-27`, branch `master`, and remote `origin`; exact post-commit recheck remains mandatory |

## 9. Phase Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Full `--update` exits non-zero after already persisting verified records | Expected when any result is unresolved | Medium — operator may misread partial persistence as failure or completeness | Retain/validate summary first, compare JSON, and treat exit 1 as triage input; release requires complete evidence, not exit-code optimism |
| Telegram throttling or soft blocks create a false wave of failures | Medium | High — live communities could be misclassified | Preserve Phase C throttle/backoff, retry unresolved once, pause on systemic failure, never auto-archive |
| A generic shell is accepted as target evidence | Observed historical defect | High — false dates/counts or archive decisions | Phase C classifier plus target-specific fallback fields; generic shell is explicit non-evidence |
| Browser fallback leaves tabs or captures session secrets | Medium | High — privacy and user-environment harm | One sequential temporary tab, target-only captures, secret exclusion, close-and-zero-tab confirmation |
| Owner approval is mistaken for death evidence | Medium | High — living community archived | Independent same-community death evidence and exact per-entry approval are both mandatory |
| A type-only `kzquake` move publishes channel data under bot-facing labels | Observed planning risk | High — structurally valid but factually false catalog output | Treat the type/name/Russian-description repair as one atomic G2 package; rejection or partial approval leaves the row unresolved |
| Cross-time service continuity is overstated as persistent peer-ID proof | Medium | High — a reassigned target could be accepted without the disclosed limitation | Retain the Iteration 3 HIGH service-continuity finding and explicit undocumented peer-ID limitation; require the target-bound post-move retry |
| A directory alternative or inactivity signal is treated as replacement/death evidence | Medium | High — unsupported repair or archive | `mobile_dev_kz` remains unbound; directory history/inactivity cannot change either contact-shell row without new qualifying evidence |
| The post-G1 merge is silently treated as covered by the original G1 summary | Observed | High — final catalog coverage is false and the original evidence is rewritten or overstated | Preserve the 63-entry raw summary; add one exact `cursor_kz` raw supplement; require exact union coverage with no missing, duplicate, or foreign handle |
| Sweep crosses a date boundary or leaves an older live date | Low/Medium | High — snapshot is not catalog-wide for one date | Derive snapshot date from evidence; recheck affected entries or stop; unresolved/partial dates block release |
| Dirty shared checkout contaminates the release commit | High | High — unrelated user work is published | ONB hash manifest, explicit path staging, exact diff review, no `git add .` or broad restore |
| Local release preparation is mistaken for publication | Medium | High — authority breach | Keep the AC6 checkpoint distinct; apply the newest G4 verdict only to the exact deterministic package after a zero-drift recheck |
| Push fails after local tag creation | Low | Medium — partial external state | Report exact refs/remote result; no force, delete, or retry without owner direction |
| Evidence attachments exceed the phase file budget | Low/Medium | Medium — unapproved scope overrun | Preserve the three immutable G1 artifacts and add only the one raw cursor supplement plus one byte-preserving bundled G2 recheck JSON; v2 status/journal/index are lifecycle control/projection paths, not Telegram evidence attachments; stop for owner decision if the original 14-file trace/evidence bound cannot hold |

---

*Phase HL — TFW-4 / Phase D: Live Sweep & First Release | 2026-08-27*

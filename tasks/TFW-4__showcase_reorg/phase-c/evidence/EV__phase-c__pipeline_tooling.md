# EV — TFW-4 / Phase C: Pipeline & Tooling

> **Date**: 2026-08-27
> **Author**: Executor (Codex)
> **Task**: TFW-4
> **TS**: [TS Phase C](../TS__phase-c__pipeline_tooling.md)
> **Revision source**: [Phase C REVIEW](../REVIEW__phase-c__pipeline_tooling.md) (`🔄 REVISE`)
> **Identity revision implementation**: `165541c6cf4668bf60c891fa8df2f249884cc946`
> **Iteration 3 evidence revision**: `a1c8673acca273b08b241ba242d848c78369c310`

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows NT 10.0.26200.0 |
| Language / Runtime | Python 3.13.5; production scripts use the standard library only |
| Deploy target | Local checkout on `master`; no deployment or external target |
| CI / Pipeline | GitHub Actions definition inspected locally; exact local equivalents executed; remote run intentionally not created |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Production schema passed; empty archive, North Star, archive integrity, fatal-date, duplicate-handle and non-fatal freshness matrices passed without rewriting production data | Local Python, offline temporary objects | N/A | Inline output and [`offline_harness.py`](offline_harness.py) |
| E2 | AC-2 | Target/type binding, decoy-link rejection, conflicting-authority rejection, null/numeric count handling, summary deltas, update ownership and explicit evidence/owner-gated archive move passed against sanitized synthetic HTML and temporary data | Local Python, socket-free imported functions | N/A | Inline C3/C4/C5/revision matrix and [`offline_harness.py`](offline_harness.py) |
| E3 | AC-3 | Purpose, dynamic stats, category order/anchors, unused-category omission, conditional archive rendering, normalized non-mutating currency checks and live-entry preservation passed | Local Python renderer and temporary files | N/A | Inline output, generated `README.md`, and [`offline_harness.py`](offline_harness.py) |
| E4 | AC-4 | Both `kz-*` documents contain the ordered CL, evidence, triage, browser-cleanup and release hard-stop gates; local references resolve; framework adapter manifest is unchanged; neither command was invoked | Local document/parser checks only | N/A | Inline hashes and [`offline_harness.py`](offline_harness.py) |
| E5 | AC-5 | Workflow triggers and offline steps parsed; forbidden live/write/release operations are absent; exact schema and README-currency commands passed locally | Local PowerShell/Python; optional installed PyYAML parser | DEFERRED | Remote GitHub Actions evidence requires a push, which the Phase C TS forbids; local results are inline |
| E6 | AC-6 | D1–D12 match the committed Phase C predecessor by normalized decision/rationale/source cells; D13–D14 match the implementation revision exactly once; D15 is absent; keyed TD-3/TD-6 transitions and preserved debt pass positive and negative fixtures without coupling unrelated documentation bytes | Local Git provenance plus keyed semantic comparison | N/A | Inline result and [`offline_harness.py`](offline_harness.py) |
| E7 | AC-7 | Original ten-path implementation, identity revision, one-path evidence revision, semantic data invariants, protected/review state, commits, generated-entry facts, tags and offline/no-release boundary were checked; both current checkout and a clean fixed-revision clone replayed successfully | Local Git/filesystem inspection | N/A | Inline hashes, paths, commits and boundary statement |

## Deterministic Local Results

### Production gates

`python scripts/validate_schema.py` exited 0:

```text
[INFO] Validating 40 groups...
[INFO] Validating 18 channels...
[INFO] Validating 5 bots...
[INFO] Freshness: oldest_live=2026-01-30; older_than_90_days=63
[WARNING] Catalog freshness is stale; age alone is not a schema error
[INFO] Categories: 18
[INFO] Archive entries: 0
[INFO] Errors: 0
[SUCCESS] Schema is valid
```

`python scripts/generate_readme.py --check` exited 0:

```text
[SUCCESS] README is generator-current: D:\projects\KZ-IT-telegram-list\README.md
```

The production README was written only by `python scripts/generate_readme.py`. A second
non-mutating check found no drift. The prior and generated files each contain 63 Telegram entry
links, and normalized live entry name/handle/description/count/date lines have no semantic
difference.

### AC-1 isolated schema matrix

The socket-free harness rejected each invalid fixture with a non-zero validation result:
`missing_north_star`, `empty_purpose`, `empty_non_goals`, `malformed_archive_date`,
`empty_reason`, `wrong_type`, `missing_type_field`, and `archive_live_collision`. A valid archive
fixture with stale live dates passed and emitted the non-fatal freshness warning. The harness
operated on deep copies and temporary files; it did not write `data/communities.json`.

### AC-2 sanitized synthetic classifier matrix

These inputs are synthetic/sanitized offline fixtures, not Telegram captures:

| Fixture | Sanitized shape | Declared target | Result | Mutation eligibility |
|---------|-----------------|-----------------|--------|----------------------|
| C3 | Target preview with `og:url=https://t.me/SampleBot`, target title, `@SampleBot`, and `Send Message`; no numeric preview count | `SampleBot` / `bots` | `verified`, `member_count=null` | Date eligible; no count invented |
| C4 | Marker-free HTTP-200-style document whose only signal is `Telegram: Contact @SampleBot` | `SampleBot` / `bots` | `ambiguous`, `member_count=null` | No date/count change; never auto-archive |
| C5 | Generic Telegram document containing site-wide prose `Groups can hold up to 200,000 members.` | `sample_group` / `groups` | `non_target`, `member_count=null` | No date/count change; site prose ignored |
| Count | Target preview bound to `sample_group`, `groups`, with `1 234 members, 56 online` in the preview extra region | `sample_group` / `groups` | `verified`, `member_count=1234` | Date and observed numeric count eligible |
| Identity decoy (revision) | Canonical, OG and action all bind `other_group`; description alone links to `t.me/requested_group`; preview extra says `500 members` | `requested_group` / `groups` | `non_target`, `target_bound=false`, `member_count=null` | `apply_updates`: 0 dates, 0 counts; requested entry unchanged as parsed |
| Authoritative conflict (revision) | Canonical and OG bind `requested_group`, while the primary action binds `other_group` | `requested_group` / `groups` | `ambiguous`, `target_bound=false`, `member_count=null` | No target fact exposed or mutation eligible |
| Failure | Explicit `tgme_page_error` marker | `sample_group` / `groups` | `failed`, `member_count=null` | No mutation; not an archive fact |
| Type mismatch | The target-bound group preview declared as `channels` | `sample_group` / `channels` | `ambiguous`, `member_count=null` | No mutation |

The summary round-trip preserved `schema_version=1`, derived classification totals and per-entry
reasons, and exposed `grew`, `shrank`, `unchanged`, `first_count`, and `member_delta`. Temporary
`--update` semantics refreshed dates only for verified targets, updated observed numeric counts
independently, retained no-count absence, and wrote the supplied run date to `meta.last_updated`.
Archive tests rejected missing owner approval and missing evidence reference, then moved one exact
temporary record while preserving original fields and adding `type`, `died_on`, and `reason`.
Throttle/backoff constants remained `3`, `1.5`, `0.3`, `3`, `2.0`, and `15` respectively.

### AC-3 through AC-6 matrices

- The renderer placed exact JSON Purpose/non-goals after dynamic stats (`40` groups, `18`
  channels, `5` bots, `18` categories, oldest live date `2026-01-30`). It emitted all 13 used
  category anchors under GitHub slug rules, omitted all five unused categories, ordered category
  display names as required, emitted archive UI only for an isolated non-empty archive fixture,
  and rejected a temporary stale/CRLF variant without modifying it.
- Command parsing confirmed the four `/kz-stats` dispositions, target-specific browser evidence
  requirements, one-tab close requirement, per-entry owner archive triage, and `/kz-release`
  stop-before-tag/push gate. All local references resolve.
- The CI YAML parsed locally and contains only checkout, supported Python setup, schema validation,
  and non-mutating README currency validation. No link validator, browser, secret, archive,
  release, tag, push, or write-mode generator step exists.
- The decision oracle resolves its baseline with `git show`: revision `4bc1bb1` supplies exact
  normalized decision/rationale/source cells for D1–D12, and its direct child `172e6ac` supplies
  D13–D14. Current D1–D14 match those content-addressed rows, D15 is absent, and prose elsewhere
  in `KNOWLEDGE.md` is deliberately outside the oracle. Negative fixtures reject a removed D1,
  duplicated D2, meaning-changed D3, missing D13, duplicated D14, and premature D15.
- The debt matrix derives the pre-Phase-C and implementation states from `4bc1bb1` / `172e6ac`
  and the fixed lifecycle state from `a141f7c`; it confirms that TD-3/TD-6 alone transition to
  resolved while required predecessor debt is preserved. Current post-doc TD-5/TD-10/TD-11 stay
  open Medium, and negative fixtures reject a changed TD-5 or removed TD-6 resolution.

The complete harness exited 0 with final markers:

```text
[PASS] AC-1 offline schema matrix
[PASS] link fixture identity_decoy: non_target; count=None
[PASS] link fixture authoritative_conflict: ambiguous; count=None
[PASS] conflicting identity does not mutate requested target
[PASS] AC-2 offline classifier/update/archive matrix
[PASS] AC-3 offline README render and currency matrix
[PASS] AC-4 project command and framework-adapter matrix
[PASS] CI YAML parsed with available local PyYAML
[PASS] AC-5 offline CI definition matrix
[PASS] decision fixture removed_D1: rejected
[PASS] decision fixture duplicated_D2: rejected
[PASS] decision fixture meaning_changed_D3: rejected
[PASS] decision fixture missing_D13: rejected
[PASS] decision fixture duplicated_D14: rejected
[PASS] decision fixture premature_D15: rejected
[PASS] unrelated KNOWLEDGE documentation is outside the decision oracle
[PASS] debt fixture changed_TD5: rejected
[PASS] debt fixture removed_TD6_resolution: rejected
[PASS] AC-6 decision and debt matrix
```

### AC-7 bounded-state comparison

| Check | ONB | Final local result |
|-------|-----|--------------------|
| Iteration 3 protected restart manifest | Current post-doc files except Task Board, RF, EV, and harness | 160 files; `ce33b08d4ca36ad2aeb94e95966152a642d6e276327628ec9315090b6152c368`; exact final replay |
| Framework `/tfw-*` manifest | 12 files; `288fde38245a27073e9b703af05c2f936a31418f3206aff42b475eb39be933ce` | Exact match |
| Phase C HL / TS | `7965eb479361df6f147a8394bcd021466308ecd5a896ddabc93182a85404771b` / `f51c5170ff0760986f04f48436ec69bfbd5107affcbbeb7e802c8285c0443f1d` | Exact match |
| Formal REVIEW traces | Three additive iterations, including `review/iter3/{map,verify,judge}.md` and the binding REVIEW addendum | Preserved byte-for-byte during this Executor revision; no REVIEW file modified |
| Existing production JSON values | ONB snapshots for `meta`, `north_star`, `groups`, `channels`, `bots`, `categories` | Direct parsed equality for all six; `archive == []` |
| Tags | None | None |
| Implementation scope | Ten paths | Exactly ten paths in commit `172e6ac18c7e604d553c38522650562d416dfb51` |

Implementation commit:

```text
172e6ac18c7e604d553c38522650562d416dfb51
[codex/TFW-4/pipeline-tooling/executor] implement phase c tooling
10 files changed, 1327 insertions(+), 407 deletions(-)
```

Review revision implementation commit:

```text
165541c6cf4668bf60c891fa8df2f249884cc946
[codex/TFW-4/pipeline-tooling/executor] fix authoritative target binding
2 files changed, 115 insertions(+), 10 deletions(-)
paths: scripts/validate_links.py; evidence/offline_harness.py
```

Post-doc evidence revision commit:

```text
a1c8673acca273b08b241ba242d848c78369c310
[codex/TFW-4/pipeline-tooling/executor] make phase c evidence reproducible
1 file changed, 293 insertions(+), 30 deletions(-)
path: evidence/offline_harness.py
```

`git diff --cached --check` was clean before the implementation commit. The implementation set is
exactly the ten TS §4 paths: three scripts, data, generated README, two `kz-*` commands, CI,
`KNOWLEDGE.md`, and `TECH_DEBT.md`. Pre-existing dirty Coordinator/Reviewer state remains in the
checkout and was neither broadly staged nor restored.

No socket request, Telegram fetch, Chrome/browser/tab action, `kz-*` invocation, live sweep,
production count/date refresh, owner archive decision, changelog/release mutation, release commit,
tag, push, or destructive restore occurred. Phase D remains next; live/browser/release evidence
has not been collected.

## Revision History and Re-review Evidence

The primary EV/RF state remains preserved in commit `c7180b92e14013d51c231a851b17fb1c833366bf`.
The formal [REVIEW](../REVIEW__phase-c__pipeline_tooling.md) then returned `🔄 REVISE` with one
High finding. This revision updates the same canonical EV/RF paths while retaining the original
versions in Git history and leaving all Reviewer-authored files unchanged.

| Stage | Deterministic result |
|-------|----------------------|
| Pre-fix reproduction | Canonical/OG/action = `other_group`; description link = `requested_group`; classifier returned `verified`, `target_bound=true`, count `500`; update counters were 1 date / 1 count and requested fields changed |
| Binding fix | Parser admits only canonical, OG and primary-action URLs as authoritative; arbitrary anchors are content. More than one authoritative handle is ambiguous. Preview-extra handle fallback applies only when no authoritative URL exists |
| Post-fix replay | Exact decoy returns `non_target`, `target_bound=false`, `member_count=null`; update counters are 0/0 and requested entry fields are unchanged. Direct canonical/action conflict returns `ambiguous` with no count |
| Compatibility replay | C3 verified/no-count, C4 ambiguous, C5 non-target, target count `1234`, explicit failure, type mismatch, JSON summary, update/archive and protected rate/retry semantics all pass |
| Full offline replay | Production schema, README `--check`, Python compile, AC-1…AC-6 harness, AC-7 manifests/path/data/README/tag boundary, and `git diff --check` pass |
| Post-doc reproducibility fix | The ONB-era whole-document hash is removed. D1–D14 and debt transitions resolve from committed keyed provenance, while unrelated documentation growth is ignored and strict negative fixtures fail as required |
| Current + fixed-revision replay | Direct current post-doc checkout and a clean detached local clone at `a1c8673` both pass schema, README `--check`, and the complete harness with exit 0; the clone finishes with an empty `git status --porcelain` |

This evidence is review-ready, not approval: a fresh `/tfw-review` must independently re-run the
counterexample and rule on Phase C before Phase D can start.

## Reproducible Harness

Run from the repository root in the current checkout or clean revision `a1c8673`:

```text
python -B tasks/TFW-4__showcase_reorg/phase-c/evidence/offline_harness.py
```

The harness resolves D1–D12 from committed predecessor `4bc1bb1`, D13–D14 from its direct child
`172e6ac`, and the clean lifecycle debt state from `a141f7c`. These Git objects are ancestors of
the fixed revision, so the expected semantics are content-addressed and replayable; no ONB-era
working-tree bytes or dirty overlay is required. The harness is a bounded Phase C evidence
attachment, not the general script test suite deferred as TD-5.

## Verdict

Evidence verdict: 0/7 VERIFIED, 1 DEFERRED, 0 BLOCKED, 6 N/A

---

*EV — TFW-4 / Phase C: Pipeline & Tooling | 2026-08-27*

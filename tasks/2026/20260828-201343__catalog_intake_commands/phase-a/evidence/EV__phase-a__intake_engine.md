# EV — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-29
> **Author**: Executor (Codex)
> **Task**: 20260828-201343__catalog_intake_commands
> **TS**: [TS Phase A](../TS__phase-a__intake_engine.md)
> **Final implementation SHA**: `9185811696c762b5261e9b90f71bee846b6fc692`
> **Accepted unchanged-command smoke SHA**: `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 `10.0.26200` |
| Language / Runtime | Python `3.13.5`; standard library only for intake runtime |
| Local verification | PowerShell; Git; Docker with official `actions/jekyll-build-pages:v1.0.13` image at `sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041` |
| Fresh command runtimes | Claude `2.1.109`; non-forked Codex task `/root/phase_a_codex_smoke` |
| Deploy target | None — local deterministic build only; no deployment |
| CI / Pipeline | Local approved Phase A offline gates plus exactly eight bounded public-preview calibration probes |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Exclusive UTF-8 source modes, byte-exact occurrence ledger, literal fixed-host root-URL grammar, explicit non-candidate dispositions, trailing-dot/spoofed-authority rejection, and occurrence-first case-insensitive grouping passed adversarial synthetic tests. | Python unit tests | VERIFIED | `scripts/test_kz_intake.py`; final implementation SHA |
| E2 | AC-2 | Immutable fetch seam fetched once and fed identical decoded content through all three unchanged classifier calls. Serialized transport accepts fetched status 200–299 at attempts 1–3, rejects failed `http_200` through `http_299`, accepts outside-2xx non-429 terminal HTTP at attempt 1, accepts terminal URL/general errors and `max_retries_exceeded` at attempt 3, and never accepts `http_429`. Exhaustive failed/fetched 2xx boundary tests include Reviewer examples 200/204/299; all prior impossible tuples and every real producer family remain covered. Existing retry, identity-decoy, update, and archive matrices also passed; the unchanged eight calibration observations validate without a network rerun. | Python unit tests; Phase C predecessor harness; retained bounded calibration evidence | VERIFIED | `scripts/test_kz_intake.py`; [`calibration-observations.json`](calibration-observations.json) |
| E3 | AC-3 | Closed `kz-canonical-json/v1` rejected duplicate/unknown fields, lexical numeric variants, booleans at integer positions, invalid evidence/identity/type/action bindings, and every observation tamper. Preview now derives exact project JSON/LF bytes as baseline plus only fixed ADD rows and the two mechanical locale-review bindings, requires generator-exact projections, and rejects the Reviewer semantic-only zero-ADD reserialization before preview/marker/write. | Python adversarial temporary fixtures using the real schema/generator | VERIFIED | `scripts/test_kz_intake.py`; final implementation SHA |
| E4 | AC-4 | Real 0/1/N schema/generator preflight passed in isolated projects. Exact ADD mechanically rebound `localization_review.payload_sha256` and `changed_key_count`; baseline output remained `en:139,ru:131,kk:131`, while staged cardinalities grew from catalog structure. Unrelated review metadata, reformatting, edits, reorder, stale projections, unknown state, corrupt markers, and impossible recovery stop. Catalog-last failure and marked N-ADD recovery passed without touching production. | Python temporary directories; real schema/generator; SHA-256 checkpoints | VERIFIED | `scripts/test_kz_intake.py`; `scripts/validate_schema.py`; [`production-hashes-final.json`](production-hashes-final.json) |
| E5 | AC-5 | Exact three-command inventory exists at both runtime locations; every pair is byte-identical and self-contained with common metadata, root-neutral paths, complete authority/operation/failure/stops, and preserved stats/release boundaries. Check mode was non-mutating and detected drift/missing/extra/thin copies; sync direction was Claude-to-Codex. | Static parity tests and standalone-body inspection | VERIFIED | `scripts/test_kz_commands.py`; `scripts/sync_kz_commands.py`; runtime hashes in both smoke artifacts |
| E6 | AC-6 | Public commitment, disclosed input, observations, and Coordinator allocation-authority receipt bind the full partition `5b9fb0dd…` and prove 29 occurrences / 28 unique / 1 overlap / 8 calibration / 20 holdout, eight-lowest allocation, and disclosed calibration key/occurrence equality without revealing holdout material. Derived root URLs did not broaden production grammar. | Dedicated worktree; public artifacts; supplemental non-revealing allocation audit | VERIFIED | [`input-commitment.json`](input-commitment.json); [`calibration-input.json`](calibration-input.json); [`calibration-observations.json`](calibration-observations.json); [`partition-audit.json`](partition-audit.json) |
| E7 | AC-7 | Self-contained complete redacted records retain all three exact Claude invocations and accepted result texts plus the complete fresh non-forked Codex report. Claude's project-setting/local-body proof is stated within its actual limit; Codex explicitly reports absolute loaded paths/hashes. Literal routing files and their hashes are byte-identical at final SHA, so the approved narrow code/schema revision did not require rerunning models. | Detached smoke worktree; Claude and Codex fresh runtimes; final static parity | VERIFIED | [`claude-runtime-smoke.jsonl`](claude-runtime-smoke.jsonl); [`codex-runtime-smoke.md`](codex-runtime-smoke.md) |
| E8 | AC-8 | All 45 generation/intake/command tests, compile, schema, four projection checks, fresh network-disabled official-image site build, command parity, index validation, predecessor matrices, classifier-body audit, exact scope/LOC audit, and final hashes passed at `91858116…`. Exactly 13 implementation paths remain 8 new/5 modified and 2,406 insertion+deletion lines. The F2a correction changes only `scripts/kz_intake.py` and `scripts/test_kz_intake.py`; the cumulative approved revision remains limited to the three authorized implementation paths. No production, release, tag, push, or external mutation occurred. | Final exact implementation commit plus clean local worktree | VERIFIED | [`jekyll-build-revision.txt`](jekyll-build-revision.txt); [`site-metadata-summary.json`](site-metadata-summary.json); [`production-hashes-final.json`](production-hashes-final.json); RF §4 |

## Verification commands and results

The final approved gate set ran after AC-7 evidence was supplied:

```text
python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands -q
  PASS — 45 tests, including real 0/1/N preflight, every formal Reviewer exploit, and exhaustive failed/fetched 2xx boundaries
python scripts/sync_kz_commands.py --check
  PASS — kz-add, kz-stats, kz-release exact synchronized inventory
python -m py_compile scripts/kz_intake.py scripts/sync_kz_commands.py scripts/test_kz_intake.py scripts/test_kz_commands.py scripts/validate_links.py scripts/validate_schema.py
  PASS
python scripts/validate_schema.py
  PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, 0 errors
python scripts/generate_readme.py --check
  PASS — all 4 catalog projections generator-current
python docs/scripts/gen_index.py --validate
  PASS — 4 tasks validate against the closed schema
python scripts/test_site_metadata.py --site <final exact-SHA read-only official-image build>
  PASS — built EN/RU/KK route structure valid
python -c "<load Phase C offline_harness.py; run_link_matrix(validate_links); run_command_matrix()>"
  PASS — classifier/retry/identity/update/archive and command predecessor matrices
git diff --check
  PASS
```

The official Jekyll image was already present locally and ran with networking disabled at final SHA `91858116…` with the
repository bind-mounted read-only plus one temporary nested output mount. The complete command,
environment, exit code, output, validation, and output hashes are retained in
[`jekyll-build-revision.txt`](jekyll-build-revision.txt). The generated metadata summary was
byte-identical to the retained 11,097-byte summary; temporary build files were then removed. No
image pull, deployment, or external-service write occurred. The earlier Reviewer reproduction was
policy-rejected before start and is not represented as a successful run.

The generic configured full-catalog live `python scripts/validate_links.py` command was not run:
the approved TS and Coordinator instruction replace it for Phase A with the predecessor offline
matrix plus exactly eight disclosed calibration probes. The Phase C harness's complete historical
`main()` also contains an unrelated stale production-date assertion; only its TS-relevant
`run_link_matrix` and `run_command_matrix` suites were invoked, as approved in ONB recommendation 1.

An AST/source audit compared `TelegramPreviewParser`, `parse_member_count`, `handle_from_url`,
`observed_preview_type`, `result`, and `classify_response` with base
`be830d3766ca4de12ff18198a680253ed133894f`; every authority body was byte-for-byte equal.

## Calibration and seal binding

| Artifact / property | Value |
|---|---|
| Public commitment SHA-256 | `f7d4530d79e3597453ef5aa62d08295d48304cc1887a7ca1ee1495589aa0255e` |
| Calibration input SHA-256 | `cbdf4f48f859e012445628daa5353c775192c5fd19db6b49e49b0a8cff8eb6d8` |
| Calibration observations SHA-256 | `507938e38a5b655a9373d46bd41edb37be9f0cbd9508522878a504e0ba84c061` |
| Allocation receipt SHA-256 | `6febc8793a7b763d5212cfaff4e96d7c12b9f9525427fb88e0ffdb65c3c2fbff` |
| Full partition SHA-256 | `5b9fb0dd028ac19d02b2c413bca45e8fa3e0e05e8de9b20087bfa883fe2cb732` |
| Partition allocation | `29` occurrences / `28` unique / `1` overlap / `8` calibration / `20` holdout; eight lowest scores are calibration |
| Disclosed cases / unique candidates | `8 / 8` |
| Source ledger | `18` URL occurrences retained because the JSON input repeats disclosed URLs across fields |
| Probe outcome | `8` fetched HTTP 200; `8` verified exact reconciliation; `0` unresolved |
| Revision validation | Existing eight observations all pass the stricter schema; artifact remains byte-identical, so no network refresh occurred |
| Escalation | No browser or authenticated fallback; no second calibration run |

Calibration outcomes are dated observations only. They were not hardcoded as current product facts
and did not authorize a catalog addition. `partition-audit.json` is a Coordinator-owned
allocation-authority receipt that exposes no holdout identity, URL, raw text, key, score, source
path, or expected outcome. The formal Reviewer may reproduce it from sealed material after the
implementation freeze; the Executor did not seek or name that material.

## Fresh runtime binding

The accepted smoke commit was `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`; detached smoke
worktree HEAD and empty porcelain status were unchanged before/after. Exact runtime bindings were:

| Runtime file pair | Bytes | SHA-256 |
|---|---:|---|
| `AGENTS.md` | 8768 | `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612` |
| `kz-add` Claude/Codex pair | 5331 each | `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414` |
| `kz-stats` Claude/Codex pair | 3761 each | `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe` |
| `kz-release` Claude/Codex pair | 3532 each | `2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc` |

`claude-runtime-smoke.jsonl` is now self-contained: it records executable/version/cwd, exact literal
commands and CLI modes, session IDs, complete accepted result text, exit/success/turn/stop fields,
zero tool/server/web steps, per-command local path/hash/parity bindings, and before/after controlled
hashes. Its exact limitation is explicit: Claude used the project setting source and produced
behavior matching the independently bound complete local body, but did not itself echo an absolute
loaded path. The three excluded harness attempts remain separate and are not accepted evidence.

The Codex evidence came from genuinely fresh non-forked task `/root/phase_a_codex_smoke`, not this
contextualized Executor and not a `$kz-add`/static-file substitute. Its complete final report,
exact task identity/input, absolute loaded paths/hashes, complete outputs, and before/after state
are contained directly in the Markdown artifact.

Final implementation SHA `9185811696c762b5261e9b90f71bee846b6fc692` changes only
`scripts/kz_intake.py`, `scripts/test_kz_intake.py`, and `scripts/validate_schema.py` after the
accepted smokes. Relative to the prior final implementation `731b3d6a…`, F2a changes only the
first two files. `AGENTS.md` and all six runtime command files remain byte-identical; the narrow
consumer/test correction does not alter literal routing or command behavior, so no fresh model
rerun was required.

## Controlled production hashes and mutation log

All checkpoints — pre-calibration, post-calibration, pre-AC-7, fresh Claude before/after, fresh
Codex before/after, and final — carry these same values:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `data/communities.json` | 45260 | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` |
| `README.md` | 16627 | `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d` |
| `index.md` | 16536 | `4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3` |
| `ru/index.md` | 22412 | `36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97` |
| `kk/index.md` | 23004 | `64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7` |

Mutation log: zero production catalog/projection writes; zero archive action; zero release,
changelog, tag, push, deploy, authenticated fallback, browser fallback, or other external mutation.
Apply/recovery tests wrote only isolated temporary project copies.

## Verdict

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

---

*EV — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands | 2026-08-28*

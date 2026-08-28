# EV — 20260828-201343__catalog_intake_commands / Phase A: Intake engine and cross-tool commands

> **Date**: 2026-08-28
> **Author**: Executor (Codex)
> **Task**: 20260828-201343__catalog_intake_commands
> **TS**: [TS Phase A](../TS__phase-a__intake_engine.md)
> **Implementation SHA**: `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`

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
| E1 | AC-1 | Exclusive UTF-8 source modes, byte-exact occurrence ledger, fixed root-URL grammar, explicit non-candidate dispositions, and occurrence-first case-insensitive grouping passed adversarial synthetic tests. | Python unit tests | VERIFIED | `scripts/test_kz_intake.py`; implementation SHA |
| E2 | AC-2 | Immutable fetch seam fetched once, fed identical decoded content through all three unchanged typed classifier calls, accepted only the exact one-verified/two-bound-mismatch tuple, and failed closed for every conflict/dead/private/transport branch. Existing retry, identity-decoy, update, and archive matrices also passed. Exactly eight disclosed calibration candidates were each probed once. | Python unit tests; Phase C predecessor harness; bounded public Telegram previews | VERIFIED | [`calibration-observations.json`](calibration-observations.json) |
| E3 | AC-3 | Closed `kz-canonical-json/v1` rejected duplicate/unknown fields, lexical numeric variants, unsafe values, invalid Unicode/keys/order/references/totals; preview rendering, digest binding, envelope separation, owner-evidence binding, subset and replay rejection all passed. | Python synthetic fixtures | VERIFIED | `scripts/test_kz_intake.py`; implementation SHA |
| E4 | AC-4 | All-before apply, exact all-after no-op, marked mixed recovery, unmarked/corrupt/unknown stops, preflight ordering, stale/collision/staged-tamper rejection, and separate receipt binding passed in isolated temporary projects. No production controlled byte changed. | Python temporary directories; SHA-256 checkpoints | VERIFIED | [`production-hashes-pre-calibration.json`](production-hashes-pre-calibration.json); [`production-hashes-post-calibration.json`](production-hashes-post-calibration.json); [`production-hashes-final.json`](production-hashes-final.json) |
| E5 | AC-5 | Exact three-command inventory exists at both runtime locations; every pair is byte-identical and self-contained with common metadata, root-neutral paths, complete authority/operation/failure/stops, and preserved stats/release boundaries. Check mode was non-mutating and detected drift/missing/extra/thin copies; sync direction was Claude-to-Codex. | Static parity tests and standalone-body inspection | VERIFIED | `scripts/test_kz_commands.py`; `scripts/sync_kz_commands.py`; runtime hashes in both smoke artifacts |
| E6 | AC-6 | Public commitment and disclosed calibration input hashes/count/method matched; only the eight disclosed cases entered live calibration. Derived root URLs were consumed without admitting bare handles to production grammar. No holdout/source material was accessed, adopted, or written by the Executor. | Dedicated worktree and committed manifest audit | VERIFIED | [`input-commitment.json`](input-commitment.json); [`calibration-input.json`](calibration-input.json); [`calibration-observations.json`](calibration-observations.json) |
| E7 | AC-7 | At the clean exact implementation SHA, three fresh nonpersistent tools-disabled Claude invocations and one fresh non-forked read-only Codex task loaded exact local runtime bytes, routed literal `/kz-add` sentinels without candidate network/apply, reproduced stats triage and release exact-current-approval stops, and preserved clean HEAD/status/controlled hashes. | Detached smoke worktree; Claude and Codex fresh runtimes | VERIFIED | [`claude-runtime-smoke.jsonl`](claude-runtime-smoke.jsonl); [`codex-runtime-smoke.md`](codex-runtime-smoke.md) |
| E8 | AC-8 | All 31 approved generation/intake/command tests, compile, schema, four projection checks, built-site metadata, command parity, index validation, predecessor matrices, diff/scope/LOC audit, and final hashes passed. Exactly 12 implementation paths remained 8 new/4 modified and 1,885 insertion+deletion lines. No production, release, tag, push, or external mutation occurred. | Exact implementation commit plus final local worktree | VERIFIED | [`site-metadata-summary.json`](site-metadata-summary.json); [`production-hashes-final.json`](production-hashes-final.json); RF §4 |

## Verification commands and results

The final approved gate set ran after AC-7 evidence was supplied:

```text
python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands -v
  PASS — 31 tests
python scripts/sync_kz_commands.py --check
  PASS — kz-add, kz-stats, kz-release exact synchronized inventory
python -m py_compile scripts/kz_intake.py scripts/sync_kz_commands.py scripts/test_kz_intake.py scripts/test_kz_commands.py scripts/validate_links.py
  PASS
python scripts/validate_schema.py
  PASS — 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries, 0 errors
python scripts/generate_readme.py --check
  PASS — all 4 catalog projections generator-current
python docs/scripts/gen_index.py --validate
  PASS — 4 tasks validate against the closed schema
python scripts/test_site_metadata.py --site <fresh read-only official-image build>
  PASS — built EN/RU/KK route structure valid
python -c "<load Phase C offline_harness.py; run_link_matrix(validate_links); run_command_matrix()>"
  PASS — classifier/retry/identity/update/archive and command predecessor matrices
git diff --check
  PASS
```

The official Jekyll image was already present locally and was run with the repository bind-mounted
read-only plus one temporary nested output mount. The temporary build was removed after the
metadata test. No image pull, deployment, or external service write occurred.

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
| Disclosed cases / unique candidates | `8 / 8` |
| Source ledger | `18` URL occurrences retained because the JSON input repeats disclosed URLs across fields |
| Probe outcome | `8` fetched HTTP 200; `8` verified exact reconciliation; `0` unresolved |
| Escalation | No browser or authenticated fallback; no second calibration run |

Calibration outcomes are dated observations only. They were not hardcoded as current product facts
and did not authorize a catalog addition.

## Fresh runtime binding

The exact smoke commit was `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`; detached smoke
worktree HEAD and empty porcelain status were unchanged before/after. Exact runtime bindings were:

| Runtime file pair | Bytes | SHA-256 |
|---|---:|---|
| `AGENTS.md` | 8768 | `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612` |
| `kz-add` Claude/Codex pair | 5331 each | `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414` |
| `kz-stats` Claude/Codex pair | 3761 each | `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe` |
| `kz-release` Claude/Codex pair | 3532 each | `2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc` |

Claude accepted three separate one-turn, exit-0, nonpersistent plan-mode invocations with project
settings, literal quoted empty tools value, and an explicit routing-only system prompt. They made
zero tool/server/web steps and no network/write. The rejected harness attempts are retained in the
JSONL and are not accepted evidence: one lost the empty tools argument and exited before model
execution; one ProcessStartInfo launch was policy-rejected before start; one exploratory quoting
probe returned unexecuted tool-call proposal text and was superseded.

The Codex evidence came from genuinely fresh non-forked task `/root/phase_a_codex_smoke`, not this
contextualized Executor and not a `$kz-add`/static-file substitute. Its full final report remains in
the Coordinator mailbox; the attached Markdown transcribes and binds the supplied result.

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

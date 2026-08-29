# Verify — "Are the claims true?"

> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Min verify ratio:** 0.42
> **RF implementation change set:** 43 concrete paths
> **Minimum paths to verify:** ceil(43 × 0.42) = 19
> **Actually verified:** 43/43 paths (100%), plus predecessor evidence and current repository state

## Verification Log

### V1 — exact implementation identity and scope

- **RF claim:** `f62f06f64557b36a8b5d9be713c7267c98ef7712` is the complete Phase B implementation based on reviewed readiness commit `268c1fcce723d999e2872a7cbefd3487b0cbb809`.
- **Actual:** `f62f06f` has exact parent `268c1fc`; the change set contains the five controlled production files, Phase B task evidence/traces, and the derived task index. No production script, command, skill, schema rule, release file, setting, or archive record changed.
- **Match:** ✅, with one non-material RF inventory omission recorded below.

### V2 — sealed source, partition, and holdout-first claim

- **RF claim:** 29 occurrences form 28 cases, with only `aws_kz` overlapping; the 20-case holdout ran before the universe run without tuning.
- **Actual:** the independent source verifier recomputed both source hashes, byte slices, case keys, split scores, 8/20 partition, 29/28 totals, and the single `aws_kz` overlap. Retained timestamps are holdout start `2026-08-29T01:26:26+05:00`, holdout completion `01:27:33+05:00`, and universe start `06:44:32+05:00`; the clean-run flags reject prior-universe use, calibration consultation, or rule/fixture changes.
- **Match:** ✅

### V3 — all candidate decisions and copy

- **RF claim:** all 28 candidates have supported dispositions, with 20 ADD, 3 reject, 1 duplicate, and 4 unresolved; all ADD rows have supported categories and neutral equivalent EN/RU/KK copy.
- **Actual:** the closed preview validates; every judgement/action pair and all three evidence references match for 28/28 candidates. All 20 ADD rows pass identity, liveness, target, collision, IT, Kazakhstan, commerciality, category, and locale gates. The three rejects, one canonical duplicate, and four unresolved rows each preserve the specific failing or missing gate. Manual review of every EN/RU/KK description found parallel meaning, natural catalog language, neutral tone, and no unsupported promotional superlative.
- **Match:** ✅

### V4 — canonical preview, stage, and exact owner authority

- **RF claim:** payload/preview `2c15bda2…`, actions `bc9316cd…`, and the ordered 20 ADD IDs are bound to the exact owner statement and only the supplied owner evidence reference.
- **Actual:** canonical and file preview hashes both equal `2c15bda20e49c81db83a442da4ebf9010fdba8240b8a28c5678b8e856dc7b9d7`; action hash equals `bc9316cd181d7abc9bc8f5b095a81255fff5b7d87039c89b558e7fabde695ac7`. The statement body hashes to `585999ac7c31a05557a7f5bd2ce98809c37e05fcf011a7131e001082d7f553b4`; the adjacent owner response encodes as UTF-8 `d0b4d0b0`, with ordinals 10575 → 10581 and the exact UTC timestamps. The approval validates against the one allowed owner reference and hashes to `5b85d0657fd6e4412cdfd81d1b34b2a124d0a4daaaa9d36b8f3b4a5672af261b`.
- **Match:** ✅

### V5 — exact apply and current production

- **RF claim:** the engine applied the approved bytes from all-B BEFORE state and emitted an `applied_exact` receipt.
- **Actual:** receipt SHA-256 is `12c9d8f1701c704ea427744c4f9249a766d2d025887eb6f9bc601f03d435c998`; outcome is `applied_exact`; state is `B/B/B/B/B`; applied IDs are the exact ordered 20. The pending lifecycle has the same execution ID and records exact cleanup; no pending marker exists. Current files are byte-identical to both retained stages and have these exact hashes:

| Path | SHA-256 |
|---|---|
| `data/communities.json` | `2e22e23bad0c7f4672ea66db8388b003f428c1c97c1e654d25255342a94883be` |
| `README.md` | `6a617bb1fa77e990c4a99be95f300a4c683037d268939e55c55239a6f6a19f22` |
| `index.md` | `86a3fdba59ee980ba967a68f93fcbf3ff83b5872e357a7610e1d21aa583cd151` |
| `ru/index.md` | `188e82cc64017a5c839bb23613641262e0ff86ab946bd0b94b7befbb0ed96184` |
| `kk/index.md` | `225be2519c01d20291ba8a1925a53e30e1ed04d3b02c9090c93910e1d92be894` |

- **Match:** ✅

### V6 — catalog delta and generated projections

- **RF claim:** the delta from reviewed readiness is exactly 4 groups and 16 channels, with no removal or mutation of existing entries, archives, or categories except the mechanically required localization-review binding.
- **Actual:** the pre-apply group and channel lists remain exact prefixes; the 4 and 16 appended rows equal the approved action bytes field-for-field. Every other top-level value is unchanged except `localization_review`; archives and categories are identical. All four projections are generator-current and byte-identical to the approved stage.
- **Match:** ✅

### V7 — apply-stage scope and manifest binding

- **RF claim:** the complete task-controlled apply-stage was needed because engine preflight requires validation scripts under the stage root.
- **Actual:** the apply-stage contains exactly 21 files: the five controlled files plus the 16 manifest-listed validation-surface files. Every file matches its manifest digest, the five controlled files match the earlier reviewed stage, and all 15 production validation-surface files are unchanged from `268c1fc`. The prior successor artifacts from `619806a` are immutable; the RF commit only adds post-approval artifacts within that namespace.
- **Match:** ✅. The retained surface is scoped, exact, and adequately manifest-bound; the missing automatic bridge from retained stage to apply-stage remains tooling debt, not an apply defect.

### V8 — post-apply target audit and dynamic drift

- **RF claim:** exactly 20 approved targets were reprobed for identity, type, liveness, and target binding; later count/body drift did not rewrite approved bytes.
- **Actual:** post-observation SHA-256 is `55cee2c73889fee18289e4e769509f928accd100f078e156cc19d7d42becc4fe`; all 20 observations pass the closed producer schema and are target-bound and verified. The post-audit records 20/20 identity/type/liveness, 20 body-hash changes, and exactly five count changes (`astana_hub`, `devs_kz`, `digitalbussinesskz`, `it_jobs_kz`, `kolesa_group`). Current catalog counts remain the approved counts, not the later observations.
- **Match:** ✅

### V9 — validation and regression classification

- **RF claim:** schema, projection currency, task index, command parity, and 41 applicable invariants pass; the complete 45-test run has exactly four pre-apply snapshot failures and no other failure/error.
- **Actual:** all named gates passed on current production. In an isolated copy of the exact apply-stage, schema, generator currency, command parity, and 41/41 selected invariants passed. The full 45-test run produced exactly the four named snapshot failures and zero errors; each assertion hard-codes a pre-apply intent count, locale digest/key count, or localization-review count. No functional test failed.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | `python …/evidence/source/verify_partition.py …/evidence/source` | PASS — source hashes/bytes, case keys, 29/28 accounting, 8/20 split, and `aws_kz` overlap recomputed. |
| 2 | Independent Python canonical/authority/delta/manifest/receipt/post-audit assertions | PASS — all exact bindings and 43-path scope checks hold. |
| 3 | `python scripts/validate_schema.py` | PASS — 42 groups, 36 channels, 4 bots, 19 categories, 2 archives, 0 errors. |
| 4 | `python scripts/generate_readme.py --check` | PASS — all four projections current. |
| 5 | `python docs/scripts/gen_index.py --validate` | PASS — 4 tasks validate. |
| 6 | `python scripts/sync_kz_commands.py --check` | PASS — `kz-add`, `kz-stats`, `kz-release` synchronized. |
| 7 | Isolated apply-stage `validate_schema.py`, `generate_readme.py --check`, and `sync_kz_commands.py --check` | PASS. |
| 8 | Isolated apply-stage `python stage_invariant_tests.py` | PASS — loaded 45, selected 41, 41/41 OK. |
| 9 | `python -m unittest scripts.test_catalog_generation scripts.test_kz_intake scripts.test_kz_commands` on production and isolated stage | Expected non-zero — exactly 45 run, four snapshot-only failures, zero errors, no additional failure. |
| 10 | Direct nested-path invariant-runner diagnostic from repository root | Not a canonical invocation: module IDs lacked the `scripts.` prefix, so the runner stopped on inventory drift; the same manifest-bound runner passed from the isolated stage root in command 8. |
| 11 | `python -m unittest scripts.test_site_metadata` | N/A — this file is a built-site CLI validator, not a unittest module; no tests were discovered and no built site is part of Phase B. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | Exact owner authority binds the successor bytes | RF §§1–5 | Canonical preview/actions, committed statement, adjacent owner response, approval schema, receipt | ✅ |
| C2 | Catalog grew by exactly the approved 4 groups and 16 channels | RF §§1, 4 | Actual baseline commit bytes, action rows, current JSON, generated projections | ✅ |
| C3 | 20/20 post-apply targets remained live and identity/type bound without applying drift | RF §§3–5 | Closed post-observation rows and independent reconciliation to approved/current bytes | ✅, within the stated unauthenticated public-preview and no-raw-body limitations. |

All citations in the RF, final EV, Phase HL, TS, ONB, and action/judgement evidence resolve to committed artifacts. External non-action claims have a repository-evidence limit: current refs contain no branch or tag at the RF commit and the change set contains no release/deploy/settings/archive mutation, but repository inspection alone cannot prove that no historical remote API action occurred. Nothing in the evidence claims such an action.

## Discrepancies Found

1. The RF's modified-files table omits the mechanically regenerated `tasks/00-INDEX.md`. The actual one-line change is exactly `BLOCKED` → `RF`, matches `phase-b/status.md`, and the closed index validator passes. This is a non-material inventory precision issue; it does not alter scope, evidence, or any AC. Per the workflow, verification was escalated to 100% of the 43-path implementation change set.

No substantive claim, evidence, implementation, or acceptance-criterion discrepancy was found.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 | Final EV E1 — source/holdout | ✅ | ✅ — independently recomputed. |
| E2 | Final EV E2 — universe/collisions/accounting | ✅ | ✅ — 29/28/20/3/1/4 and `aws_kz` hold. |
| E3 | Final EV E3 — judgments/copy | ✅ | ✅ — 28/28 decisions and 20/20 tri-locale copy reviewed. |
| E4 | Final EV E4 — preview/stage | ✅ | ✅ — payload/actions/IDs/staged bytes and manifests exact. |
| E5 | Final EV E5 — owner authority | ✅ | ✅ — message bytes, SHA, adjacency metadata, reference, and envelope exact. |
| E6 | Final EV E6 — apply/receipt/post-probes | ✅ | ✅ — all-B, `applied_exact`, no pending marker, 20/20 targets. |
| E7 | Final EV E7 — validations/boundaries | ✅ | ✅ — applicable 41 pass; four full-suite failures are only stale snapshots. |

Evidence items: 7; verified: 7; missing: 0.

## Knowledge Citations Verified

The Phase HL is derivation-only and carries no §7.2 citation table. ONB §7 contains 15 citations; all were checked.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant? |
|---|---|---|---|---|---|---|
| 1 | ONB §7 #1 | PV0-1 — `README.md` § Purpose | ✅ | ✅ | ✅ — accuracy/live/KZ/IT and generated-source clauses | ✅ |
| 2 | ONB §7 #2 | PV1-1 — `.tfw/README.md` NS2 | ✅ | ✅ | ✅ — bounded delegation preserves human authority | ✅ |
| 3 | ONB §7 #3 | PV1-2 — methodology values | ✅ | ✅ | ✅ — traceability, portability, candor | ✅ |
| 4 | ONB §7 #4 | PV2-1 — philosophy file absent | ✅ | ✅ | ✅ — absence correctly treated as N/A | ✅ |
| 5 | ONB §7 #5 | PV3-1 — KNOWLEDGE D1 | ✅ | ✅ | ✅ — JSON source, generated projections | ✅ |
| 6 | ONB §7 #6 | PV3-2 — KNOWLEDGE D2 | ✅ | ✅ | ✅ — probing separated from offline validation | ✅ |
| 7 | ONB §7 #7 | PV3-3 — KNOWLEDGE D4 | ✅ | ✅ | ✅ — categories from catalog map | ✅ |
| 8 | ONB §7 #8 | PV3-4 — KNOWLEDGE D14 | ✅ | ✅ | ✅ — project `kz-*` adapters, no framework change | ✅ |
| 9 | ONB §7 #9 | PV3-5 — KNOWLEDGE D18 | ✅ | ✅ | ✅ — target binding and exact reconciliation | ✅ |
| 10 | ONB §7 #10 | PV3-6 — KNOWLEDGE D19 | ✅ | ✅ | ✅ — explicit EN/RU/KK without fallback | ✅ |
| 11 | ONB §7 #11 | PV4-1 — conventions §3 Evidence | ✅ | ✅ | ✅ — observations are evidence; tests/hashes verify | ✅ |
| 12 | ONB §7 #12 | PV4-2 — conventions §9 | ✅ | ✅ | ✅ — byte-identical adapter parity preserved | ✅ |
| 13 | ONB §7 #13 | PV4-3 — conventions §11 | ✅ | ✅ | ✅ — no placeholders, estimates, or manual projections | ✅ |
| 14 | ONB §7 #14 | PV4-4 — conventions §14 | ✅ | ✅ | ✅ — no bonus fixes, invention, or role breach | ✅ |
| 15 | ONB §7 #15 | PV7-1 — `knowledge/domain.md` F1–F2 | ✅ | ✅ | ✅ — archived handles remain collision inputs | ✅ |

Knowledge citations: 15; resolved: 15; semantically verified: 15; irrelevant: 0; hallucinated: 0.

## Checkpoint

**Self-check:**

- [x] Opened or hash-verified at least 19 files and recorded findings (43/43 verified)?
- [x] Ran build/test commands?
- [x] Checked key claims, every citation, and reachable primary artifacts?
- [x] Verified each RF §3 checkmark against actual files?
- [x] Checked KNOWLEDGE.md for contradictions?
- [x] Verified all Phase HL §7.2 / ONB §7 citations?
- [x] Verified all RF §5 evidence items?

**Stage complete:** YES

# EV — 20260828-201343__catalog_intake_commands / Phase B: Candidate integration readiness

> **Date**: 2026-08-29
> **Author**: Executor (Codex, acting for `saubakirov`)
> **Task**: 20260828-201343__catalog_intake_commands
> **TS**: [TS Phase B](../TS__phase-b__candidate_integration.md)
> **Execution boundary**: Non-mutating pre-approval evidence only
> **Universe checkpoint SHA**: `5fadbc3b9385f1abeeb93a53c5e59f5a615e1fc1`

---

## Evidence matrix

| # | AC | What was verified | Result | Artifact |
|---|---|---|---|---|
| E1 | AC-1 | Exact sealed copies reproduce the two source hashes, partition, seal metadata, calibration binding, and public commitment. Independent byte-slice/key/score audit proves 29 occurrences, 28 unique cases, one `aws_kz` overlap, eight lowest-score calibration cases, and twenty holdout cases. The twenty-case holdout was parsed/probed first and durably committed before calibration/full-universe use; all twenty were target-bound public HTTP 200 observations. Phase A code/rules/prompts/fixtures and all five controlled paths stayed unchanged. | VERIFIED | `source/partition-audit.json`; `holdout/clean-run-audit.json`; commit `4d06114d6abab5f268d50485867279aec51d4bca` |
| E2 | AC-2 | The deterministic 29-line source preserves both `aws_kz` occurrences and parses to 28 candidates. The unchanged engine verified all 28 exact public targets: 21 channels and 7 groups. Every candidate retains requested/canonical identity, target binding, body hash, type reconciliation, liveness, visible name, observed-only count/date, exact live/archive collision result, cross-input result, and bounded canonical/alias/near-handle ruling. All 29 occurrences map to exactly one candidate action. | VERIFIED | `universe/run-audit.json`; `universe/observations.json`; `universe/collisions.json`; `universe/occurrence-accounting.json` |
| E3 | AC-3 | Every candidate has an Executor-retained IT/startup, Kazakhstan, commerciality/spam, activity, category, and evidence-linked proposed disposition. Only 20 all-gates-pass targets receive proposed ADD rows. Their name/type/handle/count/date are exact engine observations; EN/RU/KK draft descriptions are tied to public evidence. Three candidates are proposed rejects, one canonical advertising mirror is a proposed duplicate, and four insufficient-evidence cases remain unresolved. The optional Antigravity advisory was unavailable. The required persistent Reviewer audit has not yet ruled on the dispositions or locale copy. | BLOCKED — persistent Reviewer readiness audit pending | `universe/judgements.json`; `universe/actions.json`; `advisory-language-review.md` |
| E4 | AC-4 | Canonical preview payload/file SHA is `a6e7444b3be13f6ed06f3268a079c2264001703ce8e83c83f14c65ab65c0dcac`; actions SHA is `c222aa49fb3481d1142380cf2636327ff73b486baed84af239cdf69ca0e41394`. The isolated stage contains mechanically exact baseline-plus-20-ADD catalog bytes and all four generator projections. Schema, generator currency, command parity, compile, and all successor-stage invariant tests pass; the complete 45-test suite passes unchanged production. Four successor-stage full-suite assertions are explicitly classified and retained as baseline-snapshot-only, not called a staged full-suite pass, and Phase A fixtures remain unchanged. Complete Executor rendering exposes all actions, fields/copy, evidence, ADD IDs, controlled hashes, limitations, and the later exact statement template. AC-4 cannot close until AC-3’s persistent Reviewer gate passes. | BLOCKED — depends on persistent Reviewer readiness | `preview/preview.json`; `preview/preview.md`; `preview/stage-manifest.json`; `preview/readiness.md`; `preview/renderer-audit.json` |
| E5 | AC-5 | One complete non-mutating Executor package exists, production equals all five before hashes, expected bytes are isolated, and no approval/pending/receipt artifact exists. The persistent Reviewer readiness audit is pending, so the exact owner gate has not been entered and current owner approval is not yet being requested. Phase B remains in `RF`. | BLOCKED — persistent Reviewer readiness pending before owner gate | `preview/action-digest.json`; `preview/controlled-hashes.json`; `preview/readiness.md`; Phase B `status.md` and correction journal event |
| E6 | AC-6 | Exact apply, freshness recheck, durable owner envelope, pending protection, receipt, production validation, re-probes, final RF, and formal review are forbidden before E5 clears and have not begun. | BLOCKED — depends on later exact owner approval | No approval directory, marker, receipt, production mutation, or RF exists |
| E7 | AC-7 | Pre-approval boundary is intact: Phase A command bytes are unchanged, command parity and relevant tests pass, and there was no archive, release, tag, push, deployment, settings change, authenticated Telegram action, or unrelated source-checkout mutation. Final post-apply closure cannot begin before AC-6. | BLOCKED — post-apply criterion not yet eligible | `preview/stage-manifest.json`; `universe/run-audit.json`; controlled hash gate |

## Closed disposition and digest summary

| Property | Value |
|---|---|
| Source occurrences / unique candidates | `29 / 28` |
| Public target observations | `28 verified / 0 unresolved transport or identity` |
| Observed types | `21 channels / 7 groups` |
| Proposed actions | `20 add / 3 reject / 1 duplicate / 4 unresolved` |
| Sole cross-input overlap | `candidate:aws_kz` (two occurrences, one candidate action) |
| Payload / preview file SHA-256 | `a6e7444b3be13f6ed06f3268a079c2264001703ce8e83c83f14c65ab65c0dcac` |
| Actions SHA-256 | `c222aa49fb3481d1142380cf2636327ff73b486baed84af239cdf69ca0e41394` |
| Exact ordered ADD IDs | Bound in `preview/action-digest.json` and rendered in `preview/readiness.md` |
| Apply authority | ABSENT — no mutation permitted |

## Controlled production hash gate

| Path | Before/current SHA-256 | Expected-after SHA-256 |
|---|---|---|
| `data/communities.json` | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` | `6ac3c3ff94a1d6fc61089a540ec6944b46d3231acc2ae8f069beb78d31737a11` |
| `README.md` | `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d` | `ba748e35c3f489f845a965f50d34c3259558411d8a8e5df020b4026607d864a4` |
| `index.md` | `4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3` | `7bd86232ba707b8ab51a0b37a3d06a4b0b732478b7b1c04d8f53d230a6ba197c` |
| `ru/index.md` | `36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97` | `7bb7ade182c8a05637abac9ff8bc09b9491ba3613b5cb859fdb722a347ade246` |
| `kk/index.md` | `64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7` | `666f7b06c6a6c17376d41988e750a57a5a62b015e7ed52058a8adffa3365152a` |

Every current production digest equals its before digest. Every retained isolated-stage digest equals its expected-after digest.

## Verification and limitations

- The canonical producer validates the closed source, observations, editorial rows, actions, exact expected stage, and payload.
- The isolated stage passes schema validation and all four generator currency checks.
- The successor-stage invariant suite passes after excluding exactly four baseline-snapshot-only assertions. Their exact failing traces are retained; the result is not mislabeled as a complete staged-suite pass.
- The complete 45-test suite passes on unchanged production, and `scripts/sync_kz_commands.py --check` passes.
- Only unauthenticated public Telegram GET evidence was used. Public group history was not accessed; online counts are point-in-time signals.
- Four candidates remain unresolved rather than inheriting preliminary discovery claims.
- No owner approval statement, authority time, or evidence reference was invented by the Executor.

## Evidence verdict

Evidence verdict: **2 VERIFIED, 5 BLOCKED, 0 DEFERRED, 0 N/A**.

The only authorized next action is the persistent Reviewer’s bounded readiness audit. Phase B remains in lifecycle `RF`; it cannot enter the exact owner-approval blocker until that audit passes. No RF artifact is written. After a valid persistent Reviewer readiness result, resume this same `/tfw-handoff` lineage to enter the owner gate; do not use formal `/tfw-review` until apply, final verification, and RF are complete.

---

*EV — 20260828-201343__catalog_intake_commands / Phase B: Candidate integration readiness | 2026-08-29*

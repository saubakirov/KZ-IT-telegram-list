# EV — TFW-4 / Phase D: Live Sweep & First Release

> **Date**: 2026-08-27
> **Author**: saubakirov (via Codex)
> **Task**: TFW-4
> **TS**: [TS Phase D](../TS__phase-d__live_sweep_release.md)
> **Checkpoint**: G2 complete; G3 local release preparation and G4 publication are not authorized

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows 11 Pro 10.0.26200 |
| Shell | Windows PowerShell 5.1.26100.8655 |
| Language / Runtime | Python 3.13.5 |
| Repository | `master` at `97dd429b1a55e080c93661b514017dffd7cd61d2` |
| Deploy target | Local shared checkout; Telegram target previews through the approved validator |
| CI / Pipeline | Local, path-scoped verification |
| Identity | actor/on_behalf_of `saubakirov`, via `codex` |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Owner-approved Phase D authority, accepted predecessor, ONB, protected dirty checkout, migration HEAD, RF lifecycle, journal, zero staged/unmerged files, zero locks/writers, and exact partial-G2 baseline | Local Git/PowerShell guard | VERIFIED | [`ONB__phase-d__live_sweep_release.md`](../ONB__phase-d__live_sweep_release.md); [`status.md`](../status.md); task journal |
| E2 | AC-2 | Immutable 63-entry G1 machine summary plus the one-entry `cursor_kz` supplement form the exact pre-G2 64-handle manifest with no missing, duplicate, or foreign handle | Retained validator JSON | VERIFIED | [`live_sweep_summary.json`](live_sweep_summary.json); [`cursor_kz_supplement.json`](cursor_kz_supplement.json) |
| E3 | AC-3 | The four G1 unresolved handles each have exactly one retained scripted retry; bounded browser evidence retains both negative contact-shell observations and the zero-temporary-tab cleanup result | Retained JSON/PDF | VERIFIED | [`retry_summaries.json`](retry_summaries.json); [`browser_fallback.pdf`](browser_fallback.pdf) |
| E4 | AC-4 | Exact owner-approved dispositions completed in order: retained `datanomika`; verified atomic `kzquake` repair; archived `mobile_developers_kz`; archived `kzqacommunity`. Candidate snapshots and fail-closed boundaries were isolated per entry; `mobile_dev_kz` was not used as a repair | Python validator plus external byte snapshots | VERIFIED | [`g2_recheck_summaries.json`](g2_recheck_summaries.json); [TS §6](../TS__phase-d__live_sweep_release.md#g2-exact-owner-decision-package); external snapshots indexed below |
| E5 | AC-5 | Schema, generator write, generator currency, exact final evidence coverage, disposition reconciliation, protected hashes, and diff whitespace all passed. Every surviving live record is evidenced for the common run date | Python 3.13.5 and PowerShell 5.1 | VERIFIED | `data/communities.json` SHA-256 `b773a69d8f828b3732d387f797a5c41cbd37376d62be18e559b9a39d7d325de3`; `README.md` SHA-256 `58266a695a3e50f0997c9b7adcbe349853942d68a7ab91a06060113fa0ee3697` |
| E6 | AC-6 | No `/kz-release` invocation, changelog snapshot, release staging, or local release commit was authorized or attempted | Local Git | DEFERRED | Blocker: G3 explicit invocation absent |
| E7 | AC-7 | No exact commit/tag/branch/remote publication approval exists; no tag, push, or publication was attempted | Local Git | DEFERRED | Blocker: G4 exact publication approval absent |
| E8 | AC-8 | Protected artifacts, RF lifecycle authority, immutable journal, generated-index schema, and index currency passed. Completion memory/debt transitions and task closure remain unavailable while AC-6/AC-7 are deferred | v2 task-state validation | DEFERRED | `python docs/scripts/gen_index.py --validate`; `python docs/scripts/gen_index.py --check`; this RF is a non-completion checkpoint |

## G2 Disposition Evidence

| Candidate | Approved operation and actual result | Durable evidence |
|-----------|--------------------------------------|------------------|
| `datanomika` | Retained prior successful `groups` → `channels` repair. Required row is `verified / channels / channels / target_bound=true`; observed count and run date came only from validator output | External raw `E:\TEMP\TFW-4-phase-d-g2-datanomika-93ab85a59ed141e695f1ba12572fee96\raw_summary.json`, 734 bytes, SHA-256 `39ef51989d671cd5f339b77fbe55a7b387ff7005e24276bad2d29ab27de9f939`; reversibly embedded in `g2_recheck_summaries.json` |
| `kzquake` | One atomic `bots` → `channels` move with the exact approved name and Russian description. The sole fresh `python -X utf8` retry exited `0`; the one result is `verified / channels / channels / target_bound=true`, and only its observed integer count/date plus metadata were persisted | External raw `E:\TEMP\TFW-4-phase-d-g2-kzquake-resume-62255e7458ae4ef594f162019056cced\raw_summary.json`, 807 bytes, SHA-256 `a994a18ecc89e5340b4d56c74eca4ea928f2e988366b11b989014be09e225760`; reversibly embedded in `g2_recheck_summaries.json` |
| `mobile_developers_kz` | Python local date gate returned `2026-08-27`. The exact owner-approved archive command exited `0`; the complete live record moved to archive with only `type`, `died_on`, and the approved reason added | Candidate snapshot below; command evidence reference: [TS §6 owner death binding](../TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding) |
| `kzqacommunity` | The exact owner-approved archive command exited `0` after the earlier archive passed; the complete live record moved to archive with only `type`, `died_on`, and the approved reason added | Candidate snapshot below; command evidence reference: [TS §6 owner death binding](../TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding) |

The archive implementation validates and prints `evidence_ref` but does not persist it in catalog
JSON. Both exact commands used
`tasks/TFW-4__showcase_reorg/phase-d/TS__phase-d__live_sweep_release.md#g2-owner-death-evidence-binding`
and `--owner-approved`; no unsupported catalog field was invented.

## External Candidate Snapshots

| Candidate | Root | Pre-candidate bytes and SHA-256 | Candidate index |
|-----------|------|--------------------------------|-----------------|
| `kzquake` | `E:\TEMP\TFW-4-phase-d-g2-kzquake-resume-62255e7458ae4ef594f162019056cced` | `communities.json`: 22175 bytes, `628095507c7f9b435fb11d5e1b49177179846608bd3b6f930e365562173be27d`; `candidate.json`: 916 bytes, `c9dc93ef8501c28b2a2b4626b5cddaeab7777ac88f8388ab120fbf123107b97e` | `bots[0]` |
| `mobile_developers_kz` | `E:\TEMP\TFW-4-phase-d-g2-archive-mobile_developers_kz-adfdb610d6894d11b85caea16026c06c` | `communities.json`: 22267 bytes, `71fb50631322bd5adec3c9e0d39de4b742ac1e7090bea186df33be9836f0ba59`; `candidate.json`: 861 bytes, `ff2a2c6f4d9afec6b7fcc062050a9745e29d94bc8e946e17008d247a83286b0c` | `groups[26]` |
| `kzqacommunity` | `E:\TEMP\TFW-4-phase-d-g2-archive-kzqacommunity-9abb11c2fd6c46c3855ac602159ed223` | `communities.json`: 22453 bytes, `23f857fa5e0fe0d541b7a9dd0875035cf3c3480c397b635a4946104347bb67ba`; `candidate.json`: 1344 bytes, `21cf6a2dbd815c0ceb8dfe5a59fe4ed5885c282b5ffc6866f31ec29bb34d7d3f` | then-current `groups[33]` |

Every snapshot passed the fixed `E:\TEMP` prefix, regex-bound GUID-only suffix, absolute resolved
path, exact leaf, empty-root, two-file pre-mutation, record/index/archive/metadata, byte-length, and
SHA-256 predicates.

## Coverage and Reconciliation

- The immutable G1 summary contains 63 unique handles and the immutable supplement contains the
  one post-G1 `cursor_kz` handle. Their union equals the 64-handle pre-G2 universe exactly once.
- The final live/archive universe still contains those same 64 unique handles exactly once. The
  only disposition changes are the two approved type repairs and the two approved archives.
- Final positive live evidence is exact: G1 verified rows, the `cursor_kz` supplement, and the two
  verified G2 rechecks have no missing, foreign, or duplicate live handle.
- All four G1 unresolved handles occur exactly once in `retry_summaries.json` and have exactly one
  final owner disposition. All non-candidate records, categories, North Star content, and protected
  paths are unchanged from the relevant checkpoint.
- `g2_recheck_summaries.json` is 4669 bytes, SHA-256
  `950ca60b7779e8f5f4c1e2e0cdf4804cf16f0079d08701163a90f0cd239ac489`. For both ordered records,
  reversible base64, strict UTF-8 decoding, source-byte identity, stored byte length/SHA-256, parsed
  JSON deep equality, and the target-bound channel predicate passed.

## Verification Commands

| Command / gate | Exit | Result |
|----------------|------|--------|
| `python -X utf8 scripts/validate_links.py --handle kzquake --update --summary-json <fresh-root>\raw_summary.json` | 0 | Sole fresh replacement invocation; exact success predicate passed |
| Python local `date.today()` equality gate | 0 | `2026-08-27` |
| Exact `--archive mobile_developers_kz ... --owner-approved` command | 0 | Exact postconditions passed |
| Exact `--archive kzqacommunity ... --owner-approved` command | 0 | Exact postconditions passed |
| `python scripts/validate_schema.py` | 0 | Schema and freshness valid; zero errors |
| `python scripts/generate_readme.py` | 0 | README generated only from current data |
| `python scripts/generate_readme.py --check` | 0 | README generator-current |
| Manifest/disposition/final-live/protected-hash reconciliation | 0 | Every asserted predicate true |
| `git diff --check -- data/communities.json README.md` | 0 | No whitespace errors |
| `python docs/scripts/gen_index.py --validate` | 0 | Two task states validate against the closed v2 schema |
| `python docs/scripts/gen_index.py --check` | 0 | Derived portfolio index is current |

An initial read-only Python aggregate-checker invocation failed in argument parsing before opening
the aggregate because of Windows native-command quoting. It changed no file. The equivalent strict
PowerShell verifier then passed base64, UTF-8, byte/hash, source-identity, deep-equality, order, and
result predicates for both records.

## Protected Hashes

| Artifact | SHA-256 after G2 |
|----------|-----------------|
| `live_sweep_summary.json` | `bb99e525814c70a5f47510159ba162cffb617c5dc879436b50f13a26bab3ffa7` |
| `retry_summaries.json` | `c1e4da020c5272d32eebd5bf1c6911700f7d3a64fbe43dfc0372b22c76105b54` |
| `browser_fallback.pdf` | `d57a60299dd7b2dfd002de544cc36cd636e70c6252da4a554c6aa8a98d0a6787` |
| `cursor_kz_supplement.json` | `43605bbadd0900b14c3182b7b44416b440ba1d7734f4bc6fafbe9842aea79535` |
| Master HL | `16fc5ddfa0fd1c9bbbdc1aea314d314d82038ad6b45b6103383955f3e96c9e02` |
| Phase HL | `a7ccf49b676e2c46d82d8252b049f2a4c46bfb691a5709cbf3cbcc319af3ff11` |
| Phase TS | `6211b24675e66e4e583c5463694e040229ef03c5eee4a61a5e755c3f2109d125` |

Both merge-recovery stashes remain at
`e1d755a19d05e22fe60fce3265585cc3c2b31dd8` and
`23373bf620608b0ceea2d67c587428cb8f10afa9`. Staged and unmerged path sets remain empty.

## Verdict

Evidence verdict: 5/8 VERIFIED, 3 DEFERRED, 0 BLOCKED, 0 N/A

## Attachments

| File | Description |
|------|-------------|
| `live_sweep_summary.json` | Immutable G1 catalog-wide machine summary |
| `retry_summaries.json` | Immutable exact-handle retry bundle for every G1 unresolved row |
| `browser_fallback.pdf` | Immutable bounded browser-fallback and cleanup bundle |
| `cursor_kz_supplement.json` | Immutable post-G1 exact-handle supplement |
| `g2_recheck_summaries.json` | Byte-preserving aggregate of both successful repair rechecks |

---

*EV — TFW-4 / Phase D: Live Sweep & First Release | 2026-08-27*

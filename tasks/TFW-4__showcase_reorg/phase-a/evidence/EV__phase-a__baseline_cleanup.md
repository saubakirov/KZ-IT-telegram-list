# EV — TFW-4 / Phase A: Baseline & Cleanup

> **Date**: 2026-08-26
> **Author**: Executor (Codex)
> **Task**: TFW-4
> **TS**: [TS Phase A](../TS__phase-a__baseline_cleanup.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows NT 10.0.26200.0 |
| Shell | Windows PowerShell 5.1.26100.8655 |
| Language / Runtime | Python 3.13.5 |
| Version control | Git 2.42.0.windows.1; local `master` checkout |
| Deploy target | N/A — repository-only Phase A |
| CI / Pipeline | Local deterministic checks; no network step |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Literal singular-path absence, canonical `.tfw/` copy preservation, and the 11-file plural-adapter hash manifest | Local filesystem and Git | N/A | [ONB snapshot](../ONB__phase-a__baseline_cleanup.md) plus inline AC-1 output below |
| E2 | AC-2 | TD-7 is the only changed TD identifier and now records removal of the duplicate adapter as `✅ RESOLVED` | Local Git diff | N/A | Inline AC-2 output below |
| E3 | AC-3 | TFW-4 RES/TS/ONB links survive, status is `🟢 RF`, the legacy note identifies proto-artifacts, and every retired-file mention is allowed historical context | Local repository search and text inspection | N/A | Inline AC-3 output below |
| E4 | AC-4 | Protected workspace is byte-identical to ONB, implementation commit has exactly four TS paths with current metadata, no tag exists, no push/network/release action occurred, and the schema smoke check exits zero | Local filesystem, Git, and Python | N/A | Inline AC-4 and supplemental verification output below |

All four TS Evidence fields are explicitly `N/A` for external/live evidence because Phase A is
repository-only. The deterministic gates were still executed and are recorded below, as the TS
requires.

## Deterministic Gate Output

### AC-1 — Singular/plural adapter boundary

```text
agent_singular_exists=False
tfw_conventions_exists=True
tfw_glossary_exists=True
agents_plural_count=11
agents_plural_manifest_sha256=b9013c985044bea7f309901662dfa79f78c2c87473aaa7842b68af27fb276d6b
onboarding_agents_plural_manifest_sha256=b9013c985044bea7f309901662dfa79f78c2c87473aaa7842b68af27fb276d6b
tfw_canonical_diff_exit=0

implementation path status for AC-1:
D  .agent/rules/conventions.md
D  .agent/rules/glossary.md
```

The plural adapter count and manifest match the ONB snapshot exactly. The two canonical `.tfw/`
files have zero diff between onboarding commit `2250456` and implementation commit `f8d6be2`.

### AC-2 — TD-7-only debt update

```text
changed_td_ids=TD-7
TD-7 | ✅ RESOLVED — removed the obsolete .agent/ adapter and its duplicate
       conventions.md / glossary.md copies; .tfw/ remains canonical
```

The comparison keyed every `TD-N` row before and after implementation. No identifier other than
TD-7 changed.

### AC-3 — Task Board and historical-reference classification

```text
TFW-4 status: 🟢 RF
RES: research/iter2/RES.md
TS:  phase-a/TS__phase-a__baseline_cleanup.md
ONB: phase-a/ONB__phase-a__baseline_cleanup.md
legacy_reference_file_count=12
legacy_reference_outside_allowlist_count=0
```

The 12 files were classified as follows after reading their matching lines:

| Path | Classification |
|------|----------------|
| `.tfw/CHANGELOG.md` | Historical framework changelog |
| `KNOWLEDGE.md` | Historical migration index |
| `TECH_DEBT.md` | Historical migration/debt record |
| `tasks/README.md` | Historical backlog provenance |
| `tasks/TFW-3__tfw_init/HL-TFW-3__tfw_init.md` | Preserved TFW-3 migration trace |
| `tasks/TFW-3__tfw_init/RES__TFW-3__tfw_init.md` | Preserved TFW-3 research trace |
| `tasks/TFW-3__tfw_init/RF__TFW-3__tfw_init.md` | Preserved TFW-3 result trace |
| `tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md` | Current contract describing historical removal and amended acceptance rule |
| `tasks/TFW-4__showcase_reorg/phase-a/HL__phase-a__baseline_cleanup.md` | Phase derivation describing historical state |
| `tasks/TFW-4__showcase_reorg/phase-a/ONB__phase-a__baseline_cleanup.md` | Executor trace classifying historical references |
| `tasks/TFW-4__showcase_reorg/phase-a/TS__phase-a__baseline_cleanup.md` | Approved gate requiring historical-reference classification |
| `tasks/TFW-4__showcase_reorg/research/iterations.yaml` | Preserved research control trace allowing historical citation |

No match instructs a user or agent to operate through the retired files.

### AC-4 — Scope, protected state, and commit honesty

```text
protected_workspace_count=116
protected_workspace_manifest_sha256=2ca61142d7914f0fbf7ccd8e554861f670139af5cc9184a235408984acdfcac3
onboarding_protected_workspace_count=116
onboarding_protected_workspace_manifest_sha256=2ca61142d7914f0fbf7ccd8e554861f670139af5cc9184a235408984acdfcac3

commit=f8d6be2a3dfc95c1c3ccdd82ee8ae0cdfb966fe5
subject=[claude-code/TFW-4/baseline-cleanup/executor] remove obsolete singular adapter
author_date=2026-08-26T22:34:20+05:00
commit_date=2026-08-26T22:34:20+05:00

D  .agent/rules/conventions.md
D  .agent/rules/glossary.md
M  TECH_DEBT.md
M  tasks/README.md

tags_pointing_at_commit=0
added_placeholder_matches=0
```

The unchanged protected manifest includes `AGENTS.md`, `.agents/**`, `.tfw/**`, the frozen Master
HL, Phase A HL/TS, research artifacts, legacy TFW-01/TFW-02 folders, catalog data, scripts,
generated README, contributor/release/tooling paths, and every other file outside the four TS
implementation paths and authorized ONB/RF/evidence outputs.

After the implementation commit, the remaining dirty paths are exactly the pre-existing owner/user
paths recorded at onboarding:

```text
M  AGENTS.md
M  tasks/TFW-4__showcase_reorg/research/iterations.yaml
?? .agents/
?? tasks/TFW-4__showcase_reorg/phase-a/HL__phase-a__baseline_cleanup.md
?? tasks/TFW-4__showcase_reorg/phase-a/TS__phase-a__baseline_cleanup.md
?? tasks/TFW-4__showcase_reorg/research/iter1/
?? tasks/TFW-4__showcase_reorg/research/iter2/
```

No network command, tag creation, release command, or push was executed. The branch remains local
and ahead of `origin/master`.

### Supplemental schema smoke check

The TS defines no build/compile command for this documentation-and-deletion phase. As a bounded
offline smoke check, the repository schema validator was run without `--update` or network access:

```text
[INFO] Validating 40 groups...
[INFO] Validating 18 channels...
[INFO] Validating 5 bots...
Groups: 40
Channels: 18
Bots: 5
Categories: 18
Errors: 0
[SUCCESS] Schema is valid!
schema_exit=0
```

## Verdict

Evidence verdict: 0/4 VERIFIED, 0 DEFERRED, 0 BLOCKED, 4 N/A

---

*EV — TFW-4 / Phase A: Baseline & Cleanup | 2026-08-26*

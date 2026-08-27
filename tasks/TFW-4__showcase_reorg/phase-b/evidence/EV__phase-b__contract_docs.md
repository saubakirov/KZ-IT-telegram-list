# EV — TFW-4 / Phase B: Contract & Docs

> **Date**: 2026-08-27
> **Author**: Executor (Codex)
> **Task**: TFW-4
> **TS**: [TS Phase B](../TS__phase-b__contract_docs.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Microsoft Windows 11 Pro 10.0.26200, build 26200 |
| Shell | Windows PowerShell 5.1.26100.8655 |
| Language / Runtime | Python 3.13.5 |
| Version control | Git 2.42.0.windows.1 |
| Checkout | Local `master`; revision implementation HEAD `958ceb5` |
| Deploy target | N/A — documentation and local contract-data phase |
| CI / Pipeline | Local deterministic gates only; no network or CI run |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Canonical document roles, command declarations, count-free agent contract, local path resolution, and the exact managed Codex byte range | Local files and SHA-256 comparison | N/A | Inline gate log below; ONB managed-region snapshot |
| E2 | AC-2 | Exact frozen `north_star` strings, absence of `archive`, semantic identity of every pre-existing JSON key, schema exit 0, and unchanged generated README | Python 3.13.5 and PowerShell hashing | N/A | Inline gate log below; `data/communities.json` |
| E3 | AC-3 | Contributor, release, and changelog claims; a pure contributor pointer to the canonical procedure with no copied validation/generation commands; non-goal coverage; absence of placeholder markers or completed-release claims; unchanged empty tag set | Local Markdown inspection and Git | N/A | Inline gate log below; `CONTRIBUTING.md`, `RELEASE.md`, `CHANGELOG.md` |
| E4 | AC-4 | D8–D12 presence, D13–D15 absence, and exact preservation of D1–D7 plus both accepted Phase A knowledge rows | Keyed row comparison and SHA-256 | N/A | Inline gate log below; `KNOWLEDGE.md` |
| E5 | AC-5 | Seven-path implementation commit, truthful attribution and current metadata, reproducible protected 115-file manifest, unchanged generated/protected paths, no tag, and no implementation path left dirty | Git objects, filesystem manifest, and hashes | N/A | Inline gate log below; `protected_manifest.tsv`; commits `ea4a694`, `836c099`, `ce01b17`, and `958ceb5` |

## Deterministic Gate Log

### AC-1 — Canonical contract

- Managed Codex region: `1515` bytes; SHA-256
  `3ec08aeaf1c6fd98dfe8c3d832ce521cc6ed6aaa5ba292686c8a7023850ebf46`, equal to ONB.
- `AGENTS.md` contains both project-operation declarations, no literal catalog statistics, and no
  live repository-map row for the removed singular adapter.
- `CLAUDE.md` contains only the canonical pointer, context loading, adapter routing, and mode
  surface. It does not contain the generation contract, change procedure, data-field rules,
  inclusion criteria, or repository map.
- Original execution resolved 33 local Markdown links and 24 distinct named workflow/adapter
  paths. Revision replay resolved all 35 local Markdown links across the six Markdown
  implementation paths with zero missing targets.
- The first automated canonical-pointer assertion returned a false negative because its pattern
  omitted Markdown backticks around the link label. A corrected read-only assertion passed; no
  implementation change was made in response to the harness defect.

### AC-2 — North Star and catalog preservation

- `north_star.purpose` equals the frozen purpose byte-for-byte.
- `north_star.non_goals` contains exactly the four frozen strings in order.
- `archive` is absent.
- Parsed semantic SHA-256 values match ONB for every pre-existing key:

| Key | SHA-256 |
|-----|---------|
| `meta` | `5af830bea579d5e8494acfafd1d0084d7acd8d1638e6372f2e848b195b66b5e3` |
| `groups` | `768d97073d7b6fdd4b71c6734132393a796b1f688aa0170951af3dba71a25033` |
| `channels` | `f6b1f7419b7c48cb043858c1bd049dbc5d93b2eaa356aabd30563736ece9d8aa` |
| `bots` | `49eb5d75f8f6c081066bdd6bb6de8d6308b5c4d9e921a51da6f588210d5c69c6` |
| `categories` | `093ce984ba6213566889b6aba7fac78b0426a0135388209444998a1f7545a644` |

- `python scripts/validate_schema.py`: exit 0, schema errors 0.
- `python scripts/generate_readme.py`: exit 0.
- `README.md` before and after generation: SHA-256
  `cc730c6b5a442174b2821a0d891fbaf723a11c7a4356e809942e8856b64894f9`, equal to ONB.

### AC-3 — Contributor and release policies

- Contributor guide uses `master`, points to canonical data and agent rules, contains all four
  frozen non-goals, and contains no copied categories or required fields.
- The contribution workflow is a pure pointer to
  [`AGENTS.md` Change procedure](../../../../AGENTS.md#change-procedure): a focused scan found
  zero literal occurrences of `scripts/validate_schema.py`, `scripts/validate_links.py`, or
  `scripts/generate_readme.py` in `CONTRIBUTING.md`. The canonical `--update` requirement can
  therefore no longer diverge through a shortened copy in the contributor guide.
- Archive policy requires evidence, retry, owner triage, and archive-not-delete handling.
- `RELEASE.md` defines dated verified snapshots, rejects project semantic versioning, distinguishes
  `.tfw/VERSION`, specifies triggers and a complete checklist, and stops for explicit owner
  approval before tag or push.
- Root `CHANGELOG.md` follows Keep a Changelog, distinguishes framework history, and records only
  `[Unreleased]` Phase B contract work.
- Added-line scan found no placeholder marker, `origin main`, copied catalog statistic, or false
  completed-snapshot claim.
- Git tags: 0 before and after; empty-set SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

### AC-4 — Knowledge preservation

- D1–D7 keyed rows: SHA-256
  `0bb77bc1cf5bd99d40c2bc83d386ecb362586b13a987561893705b6224b0ce16`, equal to ONB.
- Accepted Phase A key-artifact and legacy rows: SHA-256
  `a1c5ec73882091dca5f3c9d8eafe47ba3e3f9386141bb23534dfe6307cc33ccb`, equal to ONB.
- D8, D9, D10, D11, and D12 each occur exactly once; D13–D15 do not occur.
- Every new decision source link resolves locally.

### AC-5 — Scope and protected-path audit

- ONB commit: `ea4a694`, containing only
  `ONB__phase-b__contract_docs.md`.
- Implementation commit: `836c099`, containing exactly the seven TS implementation paths.
- Subject: `[codex/TFW-4/contract-docs/executor] establish project contract`.
- Author and committer timestamp: `2026-08-26T23:29:57+05:00`; no backdating.
- Original evidence/RF commit: `ce01b17`.
- Revision implementation commit: `958ceb5`, containing only `CONTRIBUTING.md`; subject
  `[codex/TFW-4/contract-docs/executor] remove duplicated contributor procedure`.
- Protected manifest: `115` files; serialized-manifest SHA-256
  `14802fad376f4c906278b115820b2b57ef0afb361cc507559c1eba5108fa4864`, equal to ONB.
- The ordered `<path><TAB><lowercase-sha256>` rows are retained in
  [`protected_manifest.tsv`](protected_manifest.tsv), so neither membership nor ordering must be
  inferred from the aggregate.
- No implementation path remains dirty after the implementation commit.
- No tag points at the implementation commit; no network, live sweep, release command, whole-tree
  restore, tag, or push action was performed.

#### Protected-manifest construction and replay

The ONB snapshot started with `git ls-files --cached --others --exclude-standard`, normalized
backslashes to `/`, then used Windows PowerShell 5.1 `Sort-Object -Unique`. A candidate was
included when it matched one of these ordered-snapshot predicates:

- `.agents/*`, `.tfw/*`, `.claude/commands/*`, or `scripts/*`;
- exact `README.md` or `TECH_DEBT.md`;
- exact `tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md`;
- `tasks/TFW-4__showcase_reorg/phase-a/*` or
  `tasks/TFW-4__showcase_reorg/research/*`;
- exact Phase B `HL__phase-b__contract_docs.md` or `TS__phase-b__contract_docs.md`;
- `tasks/TFW-01_*` or `tasks/TFW-02_*`.

Everything else was excluded: the seven approved implementation paths, Task Board lifecycle
state, and Phase B execution/review traces. Each selected file was hashed as raw bytes. Each row
was serialized as `<normalized-path>\t<lowercase-sha256>`; the aggregate input is the 115 rows in
artifact order joined by LF, with no trailing LF, encoded as UTF-8 without BOM.

The following replay is deterministic against the current revision checkout. Since the Reviewer
added TD-10 and TD-11 to the already-protected `TECH_DEBT.md` after ONB, those two complete table
rows are removed in memory only; the file itself is not edited. The other 114 files are compared
directly as raw bytes.

```powershell
$manifest = Get-Content -LiteralPath `
  'tasks/TFW-4__showcase_reorg/phase-b/evidence/protected_manifest.tsv'

function Get-Sha256Bytes([byte[]] $Bytes) {
  $sha = [System.Security.Cryptography.SHA256]::Create()
  try {
    ([BitConverter]::ToString($sha.ComputeHash($Bytes))).Replace('-', '').ToLowerInvariant()
  } finally {
    $sha.Dispose()
  }
}

$aggregateBytes = [System.Text.Encoding]::UTF8.GetBytes(($manifest -join "`n"))
Get-Sha256Bytes $aggregateBytes

$mismatches = @()
foreach ($line in $manifest) {
  $path, $expected = $line -split "`t", 2
  if ($path -eq 'TECH_DEBT.md') {
    $current = [System.IO.File]::ReadAllText(
      (Resolve-Path -LiteralPath $path), [System.Text.Encoding]::UTF8)
    $projected = [regex]::Replace($current, '(?m)^\| TD-1[01] \|.*\r?\n', '')
    $actual = Get-Sha256Bytes ([System.Text.Encoding]::UTF8.GetBytes($projected))
  } else {
    $actual = Get-Sha256Bytes `
      ([System.IO.File]::ReadAllBytes((Resolve-Path -LiteralPath $path)))
  }
  if ($actual -ne $expected) { $mismatches += $path }
}
$mismatches
```

Revision replay result: `115` rows, aggregate
`14802fad376f4c906278b115820b2b57ef0afb361cc507559c1eba5108fa4864`, and `0` mismatches.

## Verdict

Evidence verdict: 0/5 VERIFIED, 0 DEFERRED, 0 BLOCKED, 5 N/A

The five N/A statuses match the TS Evidence fields: Phase B has no external/live outcome. All
required deterministic local verification is recorded above rather than omitted.

---

*EV — TFW-4 / Phase B: Contract & Docs | 2026-08-27*

# Changelog

All notable changes to the Kazakhstan IT Telegram catalog are recorded in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with dated verified snapshots
instead of semantic versions.

This is catalog history. Trace-First Workflow framework changes are recorded separately in
`.tfw/CHANGELOG.md`.

## [Unreleased]

### Added

- The approved Project North Star as structured `north_star` data: one accuracy-focused purpose
  and four explicit non-goals.
- A project release contract for future dated verified snapshots tagged `data-YYYY-MM-DD`.

### Changed

- Made `AGENTS.md` the count-free canonical project contract and reduced `CLAUDE.md` to a thin
  Claude Code adapter.
- Reworked contributor guidance to point at canonical data and rules, enforce the North Star,
  and require evidence-backed archive-not-delete handling.

## [data-2026-08-29] - 2026-08-29

Verified snapshot: 82 live communities (42 groups, 36 channels, and 4 bots) across 19
categories, plus 2 archived records. The 20 entries added in this snapshot were positively
target-bound verified on 2026-08-29 by the catalog intake task; the other 62 carry their
2026-08-27 verification from the previous snapshot, as no catalog-wide re-sweep was run for
this date. `meta.last_updated` stays 2026-08-27 because the intake apply writes entries only;
catalog metadata is owned by the sweep tool.

### Added

- Added 20 verified communities through the evidence-backed intake of task
  `20260828-201343__catalog_intake_commands` Phase B, each with an observed member count
  (79,707 in aggregate): `ai_qadam_kazakhstan` (ai); `astana_hub`, `tvkrg` (startups);
  `blockchainkz` (blockchain); `hackathon_kz` (events); `kz_bi_news` (data-analytics);
  `astanajkugoutputstream` (programming-languages); `aws_kz`, `devopskaz`, `ethkz`, `anykeykz`
  (devops-sysadmin); `allkzit`, `kolesa_group` (general); `digitalbussinesskz`, `it_kazahstan`,
  `sandyq_orda` (news); `devs_kz`, `go_kz_vacancy`, `it_jobs_kz`, `kz_bi_jobs` (jobs).
  Evidence: [EV Phase B](tasks/2026/20260828-201343__catalog_intake_commands/phase-b/evidence/EV__phase-b__candidate_integration.md).
- The `blockchain` and `startups` categories, empty in the previous snapshot, now carry entries.

### Changed

- Live entry count 62 → 82 (groups 38 → 42, channels 20 → 36, bots unchanged at 4). No repairs,
  no archives, and no removals in this snapshot.

## [data-2026-08-27] - 2026-08-27

Verified snapshot: 62 live communities (38 groups, 20 channels, and 4 bots) across 19
categories, plus 2 archived records. All 62 live entries were positively verified on
2026-08-27.

### Added

- Added and target-bound verified the `cursor_kz` group from the accepted upstream catalog
  change.

### Changed

- Repaired `datanomika` from a group to its target-bound channel, preserving its catalog copy.
- Repaired `kzquake` from a bot to its target-bound channel and aligned its name and Russian
  description with the verified target.
- Refreshed `last_verified` to 2026-08-27 for all 62 live entries.
- Recorded 58 observed numeric member counts: 38 grew, 18 shrank, and 2 were unchanged, for a
  signed aggregate delta of +16,815 from their stored baselines.

### Archived

- Archived `mobile_developers_kz` after the owner verified that the historical community no
  longer exists.
- Archived `kzqacommunity` after the owner verified that the historical community no longer
  exists.

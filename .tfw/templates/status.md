---
id: YYYYMMDD-HHMMSS__slug
title: short task name
goal: why this task exists, one line
value: what shipping it gives the project, one line
lifecycle: TODO
owner: unassigned
authority: HL-YYYYMMDD-HHMMSS__slug.md
created: YYYYMMDD-HHMMSS
updated: YYYYMMDD-HHMMSS
---

**Task state.** This file is the only authority for this task's live state. The portfolio index is derived from it and never outranks it.

<!--
CANONICAL TEMPLATE — copy into a task directory as status.md and fill every key.

Format: YAML front matter, then the one fixed sentence above. Nothing else.
The file has no free-text body. Explanation belongs in the HL; events belong in journal/.

CLOSED KEY SET — no key may be added without a convention change, and no key may be
present without a named reader. A field nothing reads does not belong here.

| Key                  | Bound                                   | Required        | Read by |
|----------------------|-----------------------------------------|-----------------|---------|
| id                   | the task's own directory name, or a legacy `[A-Z]+-\d+` | always | index, resume, docs generator |
| title                | <= 80 code points                       | always          | index |
| goal                 | <= 160 code points, one line            | always          | index |
| value                | <= 160 code points, one line            | always          | index |
| lifecycle            | one declared status id, or UNDECLARED   | always          | index, resume, release |
| lifecycle_verbatim   | <= 80 code points                       | iff UNDECLARED  | index, migration diagnostics |
| owner                | a team/ handle, or `unassigned`         | always          | index, resume |
| authority            | path relative to this file              | always          | index, resume |
| outcome              | <= 160 code points, one line            | iff terminal    | index, release |
| created              | YYYYMMDD-HHMMSS                         | always          | index |
| updated              | YYYYMMDD-HHMMSS                         | always          | index freshness |

lifecycle takes one of the ids in project_config.yaml `tfw.statuses`:
TODO · HL_DRAFT · RES · PHASES · TS_DRAFT · ONB · RF · REV · KNW · DONE · BLOCKED · REJECTED

PHASES belongs to a multi-phase task and means its phases are running. It NEVER summarizes
what they are doing: each phase directory carries its own status.md on this same schema, and
a task-level rollup would be a second fact that has to agree with them — the two-file
synchronization problem this carrier exists to avoid.

TIME IS RECORDED TO THE SECOND, in the same grammar as the identifier. A day-resolution
stamp says almost nothing on a corpus that takes several transitions a day: at day
resolution `created` and `updated` are routinely identical and `updated` stops answering the
question it exists for. The value is READ from the system clock, never composed or typed.

`unrecorded` is the honest value when a source never carried the fact. A day-only legacy
source migrates to that day with a DECLARED zero time — `20260819-000000` means "this day,
time unknown", and must never be read as second-accurate history.

Terminal ids are DONE and REJECTED. A terminal task carries `outcome` and keeps its
directory and its path forever.

UNDECLARED is not a lifecycle a person selects. Migration writes it when a legacy source
carried a value outside the vocabulary, and puts that value verbatim in
lifecycle_verbatim. A consumer treats UNDECLARED as non-actionable and reports it.
Normalizing such a value to a declared one is prohibited.

WHAT DOES NOT GO HERE
- the last event id, the journal head, or any pointer duplicating a journal fact: two
  files that must agree is the synchronization problem that previously required an engine
- history of any kind: a state change is an event, and events are files in journal/
- prose: if a fact needs a paragraph, it is HL content and this file links to it
-->

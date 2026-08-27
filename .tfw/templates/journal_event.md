---
time: YYYY-MM-DDTHH:MM:SS+ZZ:ZZ
kind: transition
actor: handle
on_behalf_of: handle
via: claude
from: TS_DRAFT
to: ONB
refs:
  - ONB__phase-a__title.md
summary: one line, at most 120 code points
---

<!--
CANONICAL TEMPLATE — copy into a task's journal/ as
    <YYYYMMDD-HHMMSS>__<kind>__<actor>.md

THE FILENAME IS THE EVENT IDENTIFIER. Nobody allocates it and nothing counts events. Take
the clock, write the file.

WHY THE ACTOR IS IN THE NAME. Two participants recording the same kind of event in the same
second would otherwise produce one filename, and one of the two events would be lost
silently. The actor is the only field that separates them: `on_behalf_of` is the same person
for both, and `via` is the same provider for two sessions of one tool.

IF THAT EXACT FILENAME ALREADY EXISTS — one actor writing twice inside one second — take the
next actual second. Never overwrite and never reuse. The rule is deliberately not "add a
counter": a counter is shared state, and shared state is what the task-local model removes.

THE TIMESTAMP IS READ FROM THE SYSTEM CLOCK AT THE MOMENT OF WRITING. It is never composed,
guessed, rounded or typed. A typed timestamp destroys the ordering the journal exists to
provide, and it is easy to spot afterwards: invented times cluster on round seconds and
sometimes fall after the events they claim to precede.

IMMUTABLE ONCE WRITTEN. A written event is never edited and never deleted. A correction is a
new event that references the one it corrects. A rule introduced later may describe older
entries but never rewrite them.

CLOSED VOCABULARY for `kind` — no other value is valid:
| kind                | Records |
|---------------------|---------|
| created             | the task came into existence |
| dispatch            | work was handed to a named participant |
| handoff             | a role boundary was crossed: plan to execution, execution to review |
| transition          | lifecycle changed, blockage and resumption included |
| ownership_changed   | the owner field in status.md changed |
| amendment_escalated | a frozen-section change was filed for an owner verdict |
| consolidation       | RESERVED — Phases B and C, not valid yet |

THREE IDENTITY FIELDS, and they answer three different questions:

| Field          | Answers                | Value |
|----------------|------------------------|-------|
| `actor`        | who performed it       | a team/ handle — a person, or an agent's own name |
| `on_behalf_of` | who is accountable     | ALWAYS a human handle. Whoever launched it answers for it |
| `via`          | what produced it       | provider family: claude, codex, gemini. Absent for a hand edit |

AN EVENT WITHOUT `on_behalf_of` IS INVALID AND IS REFUSED. There is no such thing as a record
nobody answers for. When a person acts directly, `actor` and `on_behalf_of` are the same
handle, and that repetition is deliberate rather than redundant.

A PROVIDER NAME IS NEVER AN ACTOR. `via: claude` does not identify a writer — two Claude
sessions are two actors and need two names.

| Key            | Bound                                        | Required |
|----------------|----------------------------------------------|----------|
| time           | ISO 8601 with offset, read from the clock    | always   |
| kind           | one value from the table above               | always   |
| actor          | a team/ handle, matching the filename        | always   |
| on_behalf_of   | a human team/ handle                         | always   |
| via            | provider family                              | when a tool produced the record |
| from / to      | a lifecycle id                               | both, or neither |
| refs           | at least one path, relative to the task dir  | always   |
| summary        | <= 120 code points, one line                 | optional, at most one |

THE 120 CODE POINT CEILING is measured, not chosen. Population: the 272 commit summaries in
this repository that name a task, and the 63 state-change summaries in existing REVIEW
verdicts. Median 38 and 9; p95 combined 83; p99 combined 110. 120 sits just above p99, so 3
of 335 real entries exceed it — and all three are multi-fact summaries that belong in an
artifact rather than in a log line. The ceiling is checkable by eye: one and a half terminal
lines.

CONTENT OVER THE CEILING MOVES INTO AN ARTIFACT and the event keeps a reference to it. This
is the single control that stops the journal becoming the next README.

An event body never copies HL, RES, TS, RF, REVIEW, evidence or chat text. It references
them. The journal records that something happened and where the detail lives; the detail
lives in the artifact that owns it.
-->

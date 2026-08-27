---
handle: handle
name: Display Name
type: human
since: YYYY-MM-DD
---

**Participant profile.** Declared attribution, not authentication. This file says who a
handle refers to; it grants nothing and verifies nothing.

<!--
CANONICAL TEMPLATE — copy into team/ as {handle}.md, one file per participant.

`type` is `human` or `agent`. An automated principal gets its own profile and never
borrows a person's. That is the whole reason the container is team/ and not people/:
agents belong here too.

| Key    | Bound                                  | Read by |
|--------|----------------------------------------|---------|
| handle | `[a-z0-9][a-z0-9-]*`, matches filename | status.md owner, journal actor, index |
| name   | <= 80 code points                      | index, journal rendering |
| type   | `human` or `agent`                     | index, attribution |
| since  | YYYY-MM-DD                             | index |

WHO IS ACTING IN THIS SESSION

One profile in team/ — it is used, and nothing is asked.

Several profiles — the session resolves the handle from a binding held on the
participant's own machine, outside the project tree: `~/.tfw/bindings.yaml` on POSIX,
`%LOCALAPPDATA%\tfw\bindings.yaml` on Windows. It holds one mapping per project and
nothing else:

    bindings:
      /abs/path/to/project: handle

No binding, a device several people share, a binding copied from another machine, or a
handle naming a profile that no longer exists: ask exactly one short question before the
first durable write, then proceed. Not on every turn, not again later in the session.

IDENTITY IS NEVER INFERRED from an OS username, a hostname, a folder name or an account
display string. A machine does not know who is sitting at it, and guessing produces a
durable attribution nobody made.

NOTHING PRIVATE ON THE SHARED TREE. No current-user file, no preferences, no device
identifier, no per-machine paths. The binding file is outside the project because a
project-local file is gitignorable but not sync-ignorable: under file synchronization a
per-user file reaches every participant. If the binding file ever needs a second field,
that is a design change — stop and ask.
-->

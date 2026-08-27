# team/

One file per participant. Humans and agents alike — that is why this container is not
called `people/`.

A profile is **declared attribution**, not authentication. It records who a handle refers
to so that a task's owner and a journal event's actor mean something six months later. It
grants no permission and proves no identity.

## Files

| File | Participant | Type |
|---|---|---|
| [`saubakirov.md`](saubakirov.md) | Sanzhar Aubakirov | human |

## Adding a participant

Copy [`.tfw/templates/team_profile.md`](../.tfw/templates/team_profile.md) to
`team/{handle}.md`, fill the four keys, delete the guidance comment. The handle must match
the filename and use `[a-z0-9][a-z0-9-]*`.

**No agent profile ships in TFW 2.0.0.** The schema admits `type: agent`, and the slot is
deliberately empty. A provider family — `claude`, `codex`, `gemini` — is not an actor: two
sessions of one tool are two writers and would share one name. What would make an agent
profile meaningful is a named principal that delegates and answers to someone, and that is
upstream task TFW-54 (agent team mode), not yet released. Until it lands there is one
accountable participant, and it is the owner.

Which tool produced a record is still recorded — in the event's `via` field. What is gone is
the pretence that the tool was accountable.

## Who is acting in a session

One profile here — it is used, and nothing is asked.

Several profiles — the acting handle comes from a binding kept on the participant's own
machine, never in this tree: `~/.tfw/bindings.yaml` on POSIX,
`%LOCALAPPDATA%\tfw\bindings.yaml` on Windows, holding one mapping per project and nothing
else.

```yaml
bindings:
  /abs/path/to/project: saubakirov
```

No binding, a shared device, a copied binding, or a handle whose profile is gone: exactly
one short question before the first durable write. Once per session, not per turn.

Identity is never inferred from an OS username, a hostname, a folder name or an account
display string.

## What never goes here

Private preferences, device identifiers, machine-local paths, and any file naming the
current user. The binding lives outside the project on purpose: a project-local file can be
gitignored but not sync-ignored, so under file synchronization a per-user file reaches
everyone who shares the folder.

---

> **Provenance.** This file is adapted from the upstream starter's own `team/README.md`.
> It is **not** delivered by `/tfw-update`: it lives outside `.tfw/`, so the update
> workflow's sync tables never mention it and an updating project silently receives a
> `team/` directory with no explanation of what it is. Recorded as TECH_DEBT.md TD-16.

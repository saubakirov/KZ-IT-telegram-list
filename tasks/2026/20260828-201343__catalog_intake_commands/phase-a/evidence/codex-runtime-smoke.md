# Fresh Codex runtime smoke — Phase A

> **Evidence source:** Coordinator transcription of the fresh task's final report
> **Implementation SHA:** `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`
> **Task:** `/root/phase_a_codex_smoke`
> **Isolation:** Non-forked, read-only task in detached clean worktree
> `C:/Users/c0rpa/.codex/worktrees/kz-intake-phase-a-smoke`

## Loaded project contract

The task worked only in the smoke worktree and loaded the exact committed project instructions
and all three local command skills:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `AGENTS.md` | 8768 | `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612` |
| `.agents/skills/kz-add/SKILL.md` | 5331 | `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414` |
| `.agents/skills/kz-stats/SKILL.md` | 3761 | `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe` |
| `.agents/skills/kz-release/SKILL.md` | 3532 | `2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc` |

Each skill's bytes and hash were identical to its `.claude/commands/` counterpart.

## Literal command behavior

The task received literal `/kz-add` with the exact trailing argument
`--text https://t.me/share?url=https%3A%2F%2Fexample.invalid`. It classified one
`reserved_action` non-candidate, produced an empty candidate/apply set, remained preview-only,
and performed no candidate network request or mutation.

The same task reproduced the command boundaries for the two routing-only smokes:

- `/kz-stats`: verify a target-specific date/count; repair only with continuity, exact current
  owner approval, and a recheck; archive only with independent same-community death evidence and
  exact current owner approval; otherwise retain unresolved state and do not write.
- `/kz-release`: stop after the local release commit, present the exact commit, diff, evidence,
  changelog, and tag, and require explicit current approval for the exact commit/tag/push in that
  release conversation. Earlier planning, intake, sweep, or review approval does not transfer.

## Before/after state

`HEAD` was `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a` before and after. Both
`git status --porcelain --untracked-files=all` results were empty.

| Controlled path | Bytes | SHA-256 before and after |
|---|---:|---|
| `data/communities.json` | 45260 | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` |
| `README.md` | 16627 | `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d` |
| `index.md` | 16536 | `4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3` |
| `ru/index.md` | 22412 | `36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97` |
| `kk/index.md` | 23004 | `64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7` |

The task reported no network access, file write, external-state change, or commit. Its final report
is retained in the Coordinator mailbox; this file binds the supplied result to the exact SHA and
runtime file hashes without claiming a forked/static substitute.

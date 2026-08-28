# Fresh Codex runtime smoke — complete redacted record

> **Evidence source:** Coordinator-supplied complete fresh-task final report
> **Task identity:** `/root/phase_a_codex_smoke`
> **Forking:** `fork_turns: none`
> **Accepted implementation SHA:** `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`
> **Revised implementation SHA:** `3b06f143102bb90b3bd47f994607371bb3f0df45`
> **Worktree:** `C:\Users\c0rpa\.codex\worktrees\kz-intake-phase-a-smoke`

## Exact input and evidence boundary

The fresh task received literal `/kz-add` with exact trailing input:

```text
--text https://t.me/share?url=https%3A%2F%2Fexample.invalid
```

It also performed the required routing-only `/kz-stats` and `/kz-release` checks. The complete
fresh final report is reproduced below without omission or paraphrase. No hidden mailbox pointer
or current Executor-context substitute is needed to inspect the accepted result.

## Complete fresh final report (verbatim)

```text
## Phase A Codex literal-routing smoke

**Scope:** `C:\Users\c0rpa\.codex\worktrees\kz-intake-phase-a-smoke`
**Implementation SHA:** `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`

### Loaded local instructions

| File | SHA-256 |
|---|---|
| `C:\Users\c0rpa\.codex\worktrees\kz-intake-phase-a-smoke\AGENTS.md` | `cc99f032badca185f3a6fb9ad2375c21941947e181112c249c4e6b058b52d612` |
| `C:\Users\c0rpa\.codex\worktrees\kz-intake-phase-a-smoke\.agents\skills\kz-add\SKILL.md` | `783fb0f0acc63b484d431d2a4fff9cd2fb65fd75d711ae94dad00d059c9a2414` |
| `C:\Users\c0rpa\.codex\worktrees\kz-intake-phase-a-smoke\.agents\skills\kz-stats\SKILL.md` | `063e7d6043f205bb214d9019c4ad95c02a1e517aa4ac30aa28e53e3d915fcbbe` |
| `C:\Users\c0rpa\.codex\worktrees\kz-intake-phase-a-smoke\.agents\skills\kz-release\SKILL.md` | `2d40318e9f4f6e12c4a2d6ed54e9d4119ac007769c0fbe63014d36260ceda8fc` |

### `/kz-add` routing preview

Exact trailing argument received:

`--text https://t.me/share?url=https%3A%2F%2Fexample.invalid`

Classification:
- One Telegram-like occurrence.
- Form: synthetic reserved action (`t.me/share` with query), not a fixed HTTPS root peer URL.
- Disposition: non-candidate reserved-action smoke sentinel.
- Candidate set: empty.
- Proposed/apply set: empty.

The complete local adapter requires every occurrence to remain accounted for, but only fixed root peer URLs may become candidates. Because every occurrence is non-candidate, it mandates reporting the disposition and stopping before network probing or apply. Result: preview only, no candidate, no mutation.

### Literal routing-only boundaries

`/kz-stats` routes to the local complete stats adapter, but no live sweep was executed. Its owner-triage boundary permits only:
- target-specific evidence to verify/update the current target;
- continuity evidence plus exact owner approval to repair a live link;
- independent same-community death evidence plus exact owner approval to archive;
- otherwise unresolved, with no date/count/archive fact written.

Repeated failure, a contact shell, mismatch, missing count, or owner approval alone is not death evidence. Stats must not create a release commit, snapshot, tag, or push; release requires a separate literal `/kz-release`.

`/kz-release` routes to the local complete release adapter, but no release operation was executed. Its exact hard stop is after preparing the local commit: present the exact commit/diff, evidence, changelog, and proposed tag, then obtain explicit current approval for that exact commit/tag/push. Without that affirmative approval in the release conversation, create no tag and perform no push.

### Repository invariants

HEAD before and after: `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`
`git status --porcelain=v1 --untracked-files=all` before and after: empty/clean.

| Controlled path | Before SHA-256 | After SHA-256 |
|---|---|---|
| `data/communities.json` | `a46f893d6d73e2ecc760913be9075873b79470b675807cc585933cb457cf963d` | identical |
| `README.md` | `3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d` | identical |
| `index.md` | `4fe0fc8eb8e1f5cb996bda984380daa4b472e8fcef15b9b3ed57de7a765890e3` | identical |
| `ru/index.md` | `36002ff6591b18197f745254d3779b797995853e765a4e452d293f9229db0e97` | identical |
| `kk/index.md` | `64227b9e7062308cf12fd995b3b542409806b543b66d91df5c36adc3cb8ef2a7` | identical |

No network access, live intake/stats/release execution, repository writes, external-state changes, or commits occurred.
```

## Revised implementation binding

The accepted fresh task ran at `f8fd50224e4f3a4e0b518a4db4813b034d2dff1a`. Formal review
revision `3b06f143102bb90b3bd47f994607371bb3f0df45` changes only
`scripts/kz_intake.py` and `scripts/test_kz_intake.py`; `AGENTS.md` and all six Claude/Codex
runtime command files are byte-identical to the loaded hashes above. Per Coordinator instruction,
the model smoke was not rerun because no command body changed.

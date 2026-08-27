# ONB — TFW-4 / Phase D: Live Sweep & First Release

> **Date**: 2026-08-27
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Complete; G1 `/kz-stats` pending
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Phase HL**: [Phase D HL](HL__phase-d__live_sweep_release.md)
> **TS**: [TS Phase D](TS__phase-d__live_sweep_release.md)

---

## 1. Understanding

Phase D is a gated CL execution, not an autonomous catalog update. The approved work begins by
protecting the shared dirty checkout and proving the frozen/predecessor authority. A later,
separate owner invocation of `/kz-stats` may authorize the catalog-wide Telegram observation;
each repair/archive then requires its own evidence and owner decision, `/kz-release` requires a
separate invocation, and publication requires fresh approval of the exact commit, tag, branch,
and remote. This onboarding establishes the local execution baseline and stops before G1. It
does not run a project script, contact Telegram, open a browser, mutate catalog/release state,
or create EV/RF.

## 2. Entry Points

### Authority and predecessor baseline

| Item | Exact onboarding fact | Result |
|------|------------------------|--------|
| Repository / HEAD | `D:/projects/KZ-IT-telegram-list` at `556ed83a19894c7e94068504a7c36e1a56bbcf86` | Confirmed |
| Branch / upstream | `master`; `origin/master`; ahead `23`, behind `0` | Confirmed locally; no fetch performed |
| Configured remote | `origin` → `https://github.com/saubakirov/KZ-IT-telegram-list.git` for fetch and push | Read only |
| Existing `data-*` tags | None | No local tag conflict exists at onboarding |
| Frozen Master baseline | Commit `d31e60da5b00a1d9cc9cbd3ba6405220ca62e0f0`; baseline and HEAD blob `b18bb135e486ef5d6cfaa8cc8bc13bcb1012d41d` | Exact match; worktree has no Master diff |
| Master worktree bytes | SHA-256 `16fc5ddfa0fd1c9bbbdc1aea314d314d82038ad6b45b6103383955f3e96c9e02` | Protected |
| Phase C factual predecessor | RF SHA-256 `55b598f19729b519ed2e3bb664448157acec606c36074b19a66023f5a270aec5`; binding Iteration 4 REVIEW SHA-256 `ed32ebd415f45478825952d85905b8b75336277f6bd8e20cef035682f8299da0` | Revised RF and repeat `APPROVE` confirmed |
| Phase C revision / lifecycle | `a1c8673acca273b08b241ba242d848c78369c310` / `556ed83a19894c7e94068504a7c36e1a56bbcf86` | Confirmed Git objects |
| Approved Phase D planning | HL SHA-256 `f77124d48a3f33183a02f6a767b891b79946d0d8d960134572f3cc22dec47180`; TS SHA-256 `99983f531e6f245acfe3d1bb79725bba4b6dda8408fc72176a96583afb17b94b` | Read only; G0 recorded |

G0 is the owner verdict “Отлично, даю апрув на запуск D”, recorded for saubakirov on
2026-08-27. It authorizes this handoff and no later gate by implication.

### Shared dirty-checkout snapshot

Before this ONB was written, `git status --porcelain=v1 --untracked-files=normal` reported:

```text
 M KNOWLEDGE.md
 M TECH_DEBT.md
 M tasks/README.md
 M tasks/TFW-4__showcase_reorg/research/iterations.yaml
?? .agents/
?? tasks/TFW-4__showcase_reorg/phase-a/HL__phase-a__baseline_cleanup.md
?? tasks/TFW-4__showcase_reorg/phase-a/REVIEW__phase-a__baseline_cleanup.md
?? tasks/TFW-4__showcase_reorg/phase-a/RF__phase-a__baseline_cleanup.md
?? tasks/TFW-4__showcase_reorg/phase-a/TS__phase-a__baseline_cleanup.md
?? tasks/TFW-4__showcase_reorg/phase-a/evidence/
?? tasks/TFW-4__showcase_reorg/phase-a/review/
?? tasks/TFW-4__showcase_reorg/phase-b/HL__phase-b__contract_docs.md
?? tasks/TFW-4__showcase_reorg/phase-b/REVIEW__phase-b__contract_docs.md
?? tasks/TFW-4__showcase_reorg/phase-b/TS__phase-b__contract_docs.md
?? tasks/TFW-4__showcase_reorg/phase-b/review/
?? tasks/TFW-4__showcase_reorg/phase-c/HL__phase-c__pipeline_tooling.md
?? tasks/TFW-4__showcase_reorg/phase-c/REVIEW__phase-c__pipeline_tooling.md
?? tasks/TFW-4__showcase_reorg/phase-c/TS__phase-c__pipeline_tooling.md
?? tasks/TFW-4__showcase_reorg/phase-c/review/
?? tasks/TFW-4__showcase_reorg/phase-d/
?? tasks/TFW-4__showcase_reorg/research/iter1/
?? tasks/TFW-4__showcase_reorg/research/iter2/
```

The exact file-level dirty manifest contains 59 entries. Its canonical serialization is one
UTF-8/LF row per Git status entry as
`<XY><TAB><repo-relative-path><TAB><working-file-sha256><LF>`; its SHA-256 is
`340789ac77d1a8100496d375f4f719f1d657a479e22d2891db0f651b2047e7ce`.

Semantic state at onboarding:

- `data/communities.json`: `meta.last_updated = 2026-01-30`, `archive` is empty, and the only
  live `last_verified` value is `2026-01-30`.
- `KNOWLEDGE.md`: D1–D14 are present; D15 is absent. Its current Phase B/C documentation hunk
  predates this Executor turn and is user/workflow-owned dirty state.
- `TECH_DEBT.md`: TD-2 and TD-4 are planned; TD-3 and TD-6 are resolved; TD-5, TD-10, and TD-11
  are open; TD-9 remains planned. Its current hunk predates this Executor turn.
- `tasks/README.md`: the pre-ONB dirty state records Phase D G0 approval and G1–G4 pending. Its
  exact pre-ONB bytes are retained below before the authorized ONB lifecycle update.
- `research/iterations.yaml`: the completed iteration-control hunk predates this Executor turn
  and remains untouched.

### Exact external byte snapshots

The snapshot root is
`E:/TEMP/TFW-4-phase-d-onb-5c6c4005f72144049f87aadd9e140ec8/repo_bytes`, outside the
repository. Each copy was created at `2026-08-27T04:15:17.5462065+05:00` and immediately
verified byte-for-byte by matching SHA-256. The directory contains only the six declared mutable
Phase D paths and no credentials, cookies, tokens, contacts, or browser state.

| Mutable path | Snapshot-relative path | Bytes | SHA-256 |
|--------------|------------------------|------:|---------|
| `data/communities.json` | `data/communities.json` | 22393 | `dea29c97df7b5e3882e18de378e59cb6c2e2cd5999f6437d8b205580e616f31c` |
| `README.md` | `README.md` | 8544 | `d0cbcb00f209c2886b3c1ca02030aa12e20e638c57133c3f3f36f1da69d7587f` |
| `CHANGELOG.md` | `CHANGELOG.md` | 1035 | `bd64bd1b12001b0a1e7bed0281f02fba83acd662055fd5e366723c4c3bc06aa8` |
| `KNOWLEDGE.md` | `KNOWLEDGE.md` | 13419 | `67ba87eec3ae5382e2619cdcb592a428bd661438dff7d25df4573ac234341f5d` |
| `TECH_DEBT.md` | `TECH_DEBT.md` | 5751 | `3803698faffd807f39d16d6c1e0ba07bae4f87105682610a74cbd2bd393b399e` |
| `tasks/README.md` | `tasks/README.md` | 7043 | `5700b5d951183ecb35c8d0b0af5195055506ff76daa6dab2b9b08c954928b3bb` |

Recovery is path-scoped only. These copies are not permission to restore the whole tree, and a
future restore must first identify the exact affected Phase D path/entry and retain the
retraction evidence required by the TS.

### Protected manifests

Each aggregate below is SHA-256 over UTF-8/LF rows sorted by repository-relative path as
`<repo-relative-path><TAB><file-sha256><LF>`.

| Protected scope | Files | Aggregate SHA-256 |
|-----------------|------:|------------------|
| `.tfw/**` | 60 | `7defac50d55d625c014d5cf82a2e30bcd24c05c1d9cfd6f170b355570fb9d9a2` |
| `.agents/**` | 11 | `a9447c91604dd20a63dcba25106b122f1505db6159eda4c2739659b0be3c431e` |
| `.claude/commands/tfw-*.md` | 12 | `1c95076bec2738b8ecf5acf9e0a9d7bebd30f02bfe6e861aa2de1bc90332b8aa` |
| TFW-4 master/research/Phase A–C files, excluding Phase D | 53 | `18b8fc3f80e528f414c4ed4450483ff8f5eaf3192cef31ae0c91a3198007cdae` |
| `RELEASE.md`, both `kz-*` commands, and all three production scripts | 6 | `1cb6b53d62b50bf2d039ff061286c4a118798c752a58eff35c60ca05bb4c1574` |
| Phase D HL/TS | 2 | `fd684208cf901dd8cdba770591c6ea183930be9b3b2363f45bc7cc6833b0e06f` |

Two initial read-only manifest probes failed because the installed Windows PowerShell/.NET
runtime lacks `Path.GetRelativePath` and rejected an incompatible `TrimStart` overload. They
made no repository or snapshot change. The PowerShell-5-compatible probe above completed and is
the recorded baseline.

### Exact execution-start live-handle manifest

The source byte SHA-256 is
`dea29c97df7b5e3882e18de378e59cb6c2e2cd5999f6437d8b205580e616f31c`.
The canonical manifest is the following sorted `<type>|<handle>` set, serialized with UTF-8/LF;
its SHA-256 is `55b4eb840509566ffc9e7b7852adb7bc725b2c0d357eaacc06c3e0a5af4a5fcb`:

```text
bots|chat_prettier_bot
bots|Get_Telegram_ID_bot
bots|KazPostBot
bots|kzquake
bots|ShtrafKZBot
channels|bluescreenkz
channels|certkznews
channels|cleverskz
channels|cloudnativekz
channels|cloudreadykz
channels|devkz_jobs
channels|devsecopskz_jobs
channels|DevSkills
channels|dsmlkz_news
channels|kz_it_events
channels|ml_jobs_kz
channels|mobilejobskz
channels|nu_acm_w
channels|saubakirov
channels|sysadm_in_channel
channels|sysadm_in_up
channels|thetechkz
channels|workitkz
groups|AQA_kz
groups|astanajug
groups|automation_kz
groups|backenderskz
groups|cctvkz
groups|cppkz
groups|cyberseckz
groups|dart_kz
groups|datanomika
groups|devkz
groups|devnullkz
groups|devsecopskz
groups|diykz
groups|dotnetgroup
groups|dwhkz
groups|frontendkz
groups|gamedevkz
groups|go_kz
groups|illuminatinc
groups|iOSDevelopers_KZ
groups|itbazarkz
groups|itmankz
groups|kz_1C
groups|kz_bi
groups|kzlug
groups|kzqacommunity
groups|MikroTikKZ
groups|mobile_developers_kz
groups|phpdevconf
groups|projects_kz
groups|python_kz
groups|r0crewKZ
groups|radiotechkz
groups|rubyata
groups|rubykz
groups|rustlang_kz
groups|sipvoipkz
groups|sysadm_in
groups|teamleads_kz
groups|thetechkzchat
```

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions remain. The approved Phase D derivation is internally executable within
the declared budget, and the current owner message supplies G0 only.

Authority questions resolved from the existing approval record:

| # | Question | Answer |
|---|----------|--------|
| 1 | Does G0 authorize `/kz-stats`, network, Telegram, or browser action? | No. G1 is pending and must be an explicit owner invocation after this ONB. |
| 2 | May any repair or archive be inferred or batch-approved now? | No. G2 remains per exact entry, with named continuity/death evidence and an exact owner decision. |
| 3 | May `/kz-release` or changelog/release-commit preparation start now? | No. G3 is a separate explicit invocation after an unresolved-free sweep. |
| 4 | May a tag or push occur under the plan approval? | No. G4 requires fresh approval of the exact prepared commit, tag, branch, and remote. |
| 5 | What is the next owner invocation after this onboarding commit? | `/kz-stats`. No equivalent phrasing is treated as already granted. |

## 4. Recommendations (suggestions, not blocking)

1. Retain the external byte-snapshot directory through Phase D review or explicit owner-directed
   cleanup. If the OS removes it before the first mutable action, stop and recreate/rehash the
   six copies from an unchanged source rather than assuming recovery remains available.
2. At G1, use a new temporary summary path outside the repository, verify the raw summary before
   any rendering, and copy it unchanged to the single TS evidence artifact. Exit `1` with a valid
   summary is triage input; a missing or malformed summary is a hard stop.
3. Keep every commit and recovery operation path-scoped. The Task Board's pre-existing G0 hunk is
   intentionally retained in the onboarding lifecycle commit; all other pre-existing dirty and
   untracked state remains excluded.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The snapshot directory is temporary OS-managed storage. Its exact path and hashes make loss
   detectable but do not make retention permanent; Recommendation 1 is the safe pre-write gate.
2. Several accepted predecessor and planning traces are untracked in the shared checkout. Their
   authority comes from the explicit owner record and their recorded bytes, not from pretending
   they already exist in Git history. Their protected manifests must remain stable.
3. The Task Board was already dirty with the accepted Phase C/G0 lifecycle state. The authorized
   onboarding commit will record the current Board path plus the ONB transition, while its exact
   pre-ONB bytes remain externally recoverable. No other dirty path may enter that commit.
4. The delivered live updater persists positively verified records before returning unresolved
   exit `1`. This matches the TS, but it makes whole-tree rollback especially unsafe; raw evidence
   and per-path comparison must precede any interpretation of failure/completeness.

## 6. Inconsistencies with Code (spec vs reality)

No blocking scope inconsistency was found in the delivered commands, scripts, Phase C result, or
approved Phase D derivation.

Non-blocking trace realities retained for later review:

1. The frozen Master HL header still shows its historical `TS_DRAFT — A6 approved; Phase B
   planning` status and says no Project North Star is designated, while the accepted data and
   current Phase D HL name `README.md § Purpose`. The approved Phase D TS simultaneously protects
   the Master blob and uses the current Phase HL/North Star as operational authority. This
   Executor will not edit the Master; the mismatch is visible rather than silently repaired.
2. Phase D HL/TS and the binding Phase C REVIEW are currently untracked even though their content
   is approved/accepted. The shared-dirty-checkout contract anticipated this state; exact hashes
   above protect it, and the onboarding commit does not absorb or modify those files.
3. The current production data still represents the pre-sweep state, exactly as Phase D expects.
   This is not evidence of a completed live operation and cannot be used to discharge any later
   AC.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV 0 — Master row says no North Star designated | ✅ | Applied with current derivation | Phase D uses the now-delivered `README.md § Purpose`; see new PV row 21. |
| 2 | PV 1 — `.tfw/README.md` “Traces Over Code” | ✅ | Applied | ONB records intent, authority, exact bytes, dirty state, and recovery boundaries before mutable work. |
| 3 | PV 1 — “Single Source of Truth” | ✅ | Applied | Data remains the catalog source; commands and release contract are referenced, not copied into replacement implementations. |
| 4 | PV 1 — “Structural Enforcement” | ✅ | Applied | Hash, manifest, file-existence, authority, and later evidence gates are explicit and replayable. |
| 5 | PV 1 — “Honesty Over Convincingness” | ✅ | Applied | Untracked predecessor state and failed read-only probes are reported; no live or release result is claimed. |
| 6 | PV 1 — “Completeness Over Speed” | ✅ | Applied | ONB has no stub or deferred fill-in; later artifacts remain absent until their real gates occur. |
| 7 | `KNOWLEDGE.md` P1 | ✅ | Applied | `data/communities.json` is snapshotted as source; README is protected generated output. |
| 8 | `KNOWLEDGE.md` P2 | ✅ | Applied | No unverified count, date, identity, repair, or death is accepted. |
| 9 | `KNOWLEDGE.md` P3 | ✅ | Applied | Later local finalization must remain schema → generator write → generator `--check`. |
| 10 | `KNOWLEDGE.md` P4 | ✅ | Applied | G1/G2/G3/G4 remain CL owner gates; G0 creates no external-state authority. |
| 11 | `KNOWLEDGE.md` D2 | ✅ | Applied | Separate schema/link/generator responsibilities and commands remain unchanged. |
| 12 | `KNOWLEDGE.md` D3 | ✅ | Applied | Existing throttle/backoff is protected; unresolved results receive the separate exact-handle retry required by TS. |
| 13 | `KNOWLEDGE.md` D4 | ✅ | Applied | Category and related catalog structure remain data-owned; no code-side derived catalog copy is introduced. |
| 14 | `KNOWLEDGE.md` D7 | ✅ | Applied | Lifecycle update targets `tasks/README.md`, never generated `README.md`. |
| 15 | `conventions.md` §9 Tool Adapter Pattern | ✅ | Applied | Existing project commands are invocation inputs; framework adapters are protected manifests. |
| 16 | `conventions.md` §3 Project North Star | ✅ | Applied | Purpose and non-goals at `README.md § Purpose` govern every later disposition and release eligibility decision. |
| 17 | `conventions.md` §3 rules 13–16 | ✅ | Applied | Frozen Master baseline `d31e60d` and matching Git blob are recorded before execution. |
| 18 | `conventions.md` §4 Commit Attribution | ✅ | Applied | The onboarding commit uses current Codex/TFW-4/phase/executor attribution and remains local/path-scoped. |
| 19 | `conventions.md` §14 Executor scope anti-pattern | ✅ | Applied | No adjacent debt, predecessor trace, script, adapter, or external state is modified. |
| 20 | `conventions.md` §2 README Task Board default | ✅ | N/A by accepted project deviation | D7 places this project's Board in `tasks/README.md`; generated README only links to it. |
| 21 | NEW PV 0 — `README.md § Purpose` | ✅ | Applied | Current North Star requires dated network evidence, rejects promotion/estimation, and keeps data—not hand-edited README—as product authority. |

---

*ONB — TFW-4 / Phase D: Live Sweep & First Release | 2026-08-27*

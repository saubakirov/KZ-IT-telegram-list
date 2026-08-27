# ONB — TFW-4 / Phase A: Baseline & Cleanup

> **Date**: 2026-08-26
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Complete; no blocking questions
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Phase HL**: [Phase A HL](HL__phase-a__baseline_cleanup.md)
> **TS**: [TS Phase A](TS__phase-a__baseline_cleanup.md)
> **Frozen baseline**: `8485c29`

---

## 1. Understanding

Phase A is a local-only cleanup of the obsolete `.agent/` singular adapter. The executor will
delete its two tracked duplicate rule files, resolve only TD-7 in `TECH_DEBT.md`, and preserve
the existing TFW-4 research/TS hunk while updating `tasks/README.md` to the current workflow
stage and clarifying that TFW-01/TFW-02 are preserved pre-framework proto-artifacts. The phase
must not replay TFW-3 work already committed in `0fe6c67`, touch `.agents/` plural or any other
protected owner/user work, use the network, tag, release, push, or continue into Phase B.

The current Master HL blob, the `HEAD` Master HL blob, and the Master HL at freeze commit
`8485c29` are identical (`194667238926ac096957a82123a24ba575a7dbda`). The Phase A scope is
therefore derived from the exact frozen baseline rather than a drifted working copy.

## 2. Entry Points

| Path | Role in Phase A |
|------|-----------------|
| `.agent/rules/conventions.md` | Obsolete duplicate to delete |
| `.agent/rules/glossary.md` | Obsolete duplicate to delete |
| `.tfw/conventions.md` | Canonical convention copy; protected |
| `.tfw/glossary.md` | Canonical glossary copy; protected |
| `.agents/skills/tfw-*/SKILL.md` | Live Codex adapter; protected byte-for-byte |
| `TECH_DEBT.md` | TD-7-only implementation edit |
| `tasks/README.md` | Narrow board status/legacy-note edit preserving the existing TFW-4 hunk |
| `tasks/TFW-4__showcase_reorg/HL-TFW-4__showcase_reorg.md` | Frozen master contract, baseline `8485c29` |
| `tasks/TFW-4__showcase_reorg/phase-a/HL__phase-a__baseline_cleanup.md` | Derivation-only phase context |
| `tasks/TFW-4__showcase_reorg/phase-a/TS__phase-a__baseline_cleanup.md` | Approved executable contract |

### Onboarding Snapshot

- Branch: `master`, eight commits ahead of `origin/master` at onboarding.
- Pre-existing dirty paths: `AGENTS.md`, `tasks/README.md`,
  `tasks/TFW-4__showcase_reorg/research/iterations.yaml`, `.agents/**`, both research iteration
  directories, and the Phase A HL/TS directory.
- `tasks/README.md` before Phase A edit: SHA-256
  `46ff214a130d61f8e60a81d719101d071154e72cd502fcaa27f98514e299b6c3`.
- `TECH_DEBT.md` before Phase A edit: SHA-256
  `9b3bcb5ffb4a670ef5365f9f935a8d8589590c80aa2cb3ec6039a5fb900624b3`.
- `AGENTS.md` protected hash: SHA-256
  `d1f2b7e5e7d4e71f55cca2926244587e831e0c3a553774debadd722b48419ed2`.
- Protected-workspace manifest: 116 files, SHA-256
  `2ca61142d7914f0fbf7ccd8e554861f670139af5cc9184a235408984acdfcac3`.
  The manifest excludes only `.git/**`, the four implementation paths, and the authorized
  Phase A ONB/RF/evidence outputs. It includes the Phase A HL/TS and all protected owner/user
  files.
- `.agents/**` manifest: 11 files, SHA-256
  `b9013c985044bea7f309901662dfa79f78c2c87473aaa7842b68af27fb276d6b`.

The plural-adapter manifest is:

```text
.agents/skills/tfw-config/SKILL.md     fa5244e71764fd763f68e0e28cd761725fdce868b8bd425472ac64a03c48f0e4
.agents/skills/tfw-docs/SKILL.md       4897e5aab7b0ac56f49e408b91cff9733db2ff769c43714a85c7a130fca5952c
.agents/skills/tfw-handoff/SKILL.md    54159c9c541007de64b4547deadae35fbb699ac334f9bf0a38702a8bd5922497
.agents/skills/tfw-init/SKILL.md       a9d6e6654cfaf4a2fb94a83cd304362582e5a37002c87779a020947a6bbd4d52
.agents/skills/tfw-knowledge/SKILL.md  a7822d8782e8f56484e225b423017b92eccd1db87c617bf7a096c138103a6167
.agents/skills/tfw-plan/SKILL.md       55e0805027f4f7370804b7a2b243a82d18e554ceb4275d537d029cd0417b58b4
.agents/skills/tfw-release/SKILL.md    58b2cc253acdda1c75f6a4661af5167b291d841840152dd975236540befd2a79
.agents/skills/tfw-research/SKILL.md   84fa7685523f1dcba8155cd3be04f019ad58c97b5a628bb856215744b013b92b
.agents/skills/tfw-resume/SKILL.md     1721aec8fd50d744912f1ad4ddd35c4eb42bf5a4e00ac4f509037db57a6a3f6e
.agents/skills/tfw-review/SKILL.md     64ed7d5b47cf6b718f5f1ac286c947f173ad811a22be671f48889ebbda64d102
.agents/skills/tfw-update/SKILL.md     3f690102346a704d99fa00788206535591ba12d6346b89200a52eb469a769488
```

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved TS, frozen Master HL, Phase HL, and owner pre-authorization
fully determine the local Phase A actions.

## 4. Recommendations (suggestions, not blocking)

1. Use separate path-scoped local commits for the first-class ONB trace and the Phase A
   implementation/evidence/RF result. Never use `git add -A` in this dirty checkout.
2. Treat every external-evidence status as `N/A` exactly as prescribed by the TS while still
   recording the deterministic filesystem, hash, diff, and git gates in the mandatory EV file.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The approved Quality Contract fixes commit `agent` to `claude-code` even though the current
   executor is Codex, while `conventions.md` normally derives that field from the acting product.
   This does not change scope or commit authorship metadata. The frozen Master HL and approved TS
   are more specific for this task, so Phase A commits will use the required
   `[claude-code/TFW-4/.../executor]` prefix and this discrepancy will be reported in the RF.
2. `tasks/README.md` already contains the user-owned transition from `🔬 RES` to `🟡 TS_DRAFT`,
   including the iteration-2 RES and approved Phase A TS links. The implementation must edit
   from the working copy and preserve that entire hunk.
3. The live `.agents/**` adapter is untracked, so ordinary tracked-diff checks cannot protect it.
   The explicit 11-file SHA-256 manifest above is the authoritative AC-1 comparison.

## 6. Inconsistencies with Code (spec vs reality)

1. No implementation-blocking inconsistency. The two singular `.agent/rules/*` files exist and
   are tracked, `.agents/**` contains the 11 protected Codex skills described by the TS, TD-7 is
   still `🔴 OPEN`, and the current Task Board hunk matches the Phase HL's dirty-checkout warning.
2. The Master HL, Phase HL, and TS correctly treat all current `STEPS.md` / `TASK.md` search
   results as historical trace or migration context. No result is a live instruction to use a
   retired file.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV 0 — no Project North Star | ✅ | Applied | Phase A uses frozen Master HL §1 as the declared fallback and does not create Phase B's North Star. |
| 2 | PV 1 — `.tfw/README.md` Traces Over Code | ✅ | Applied | ONB is created before implementation; implementation and result are kept as reviewable traces. |
| 3 | PV 1 — Single Source of Truth | ✅ | Applied | Delete only the obsolete singular duplicate; retain `.tfw/` as canonical and `.agents/` as a referencing adapter. |
| 4 | PV 1 — Structural Enforcement | ✅ | Applied | Literal existence checks, manifests, commit path lists, and artifact existence are execution gates. |
| 5 | PV 1 — Honesty Over Convincingness | ✅ | Applied | Do not replay TFW-3, backdate metadata, or claim excluded work. |
| 6 | PV 1 — Completeness Over Speed | ✅ | Applied | ONB, EV, and RF will be complete and contain no placeholders. |
| 7 | `KNOWLEDGE.md` P1 — data is the product | ✅ | N/A | Phase A does not change catalog data or generated README output. |
| 8 | `KNOWLEDGE.md` P2 — accuracy over coverage | ✅ | N/A | Phase A performs no catalog verification or editorial change. |
| 9 | `KNOWLEDGE.md` P3 — validation precedes generation | ✅ | N/A | Phase A does not run the catalog generation pipeline; local TS gates still run before RF. |
| 10 | `KNOWLEDGE.md` P4 — external state is CL | ✅ | Applied | No network or Telegram request is made in this AG/local-only phase. |
| 11 | `KNOWLEDGE.md` D2 — three separate scripts | ✅ | N/A | No script is modified or orchestrated. |
| 12 | `KNOWLEDGE.md` D3 — preserve rate limiting | ✅ | N/A | `validate_links.py` is outside scope and remains untouched. |
| 13 | `KNOWLEDGE.md` D4 — categories live in data | ✅ | N/A | Neither categories nor data are modified. |
| 14 | `KNOWLEDGE.md` D7 — Task Board in `tasks/README.md` | ✅ | Applied | Workflow status is updated only in the designated board, never in generated `README.md`. |
| 15 | `conventions.md` §9 — Tool Adapter Pattern | ✅ | Applied | `.agent/` singular is obsolete duplication; `.agents/` plural is the protected live Codex adapter. |
| 16 | `conventions.md` §3 — Project North Star | ✅ | N/A | Phase B owns the generated README locus; Phase A cannot author it. |
| 17 | `conventions.md` §3 rules 13–16 — Contract Baseline | ✅ | Applied | Baseline `8485c29`, `HEAD`, and working Master HL resolve to the same blob. |
| 18 | `conventions.md` §4 — Commit Attribution | ✅ | Applied | Commits are local, path-scoped, current-dated, and use the TS-required scope/role grammar; no push. |
| 19 | `conventions.md` §14 — no out-of-scope fixes | ✅ | Applied | Implementation is fenced to the four TS paths plus mandatory trace artifacts. |
| 20 | `conventions.md` §2 — board-location deviation | ✅ | Applied | The known generated-README deviation is preserved; board edits stay in `tasks/README.md`. |

No additional PV item relevant to Phase A was found beyond the coordinator's citations and the
approved TS's explicit protected-dirty-worktree guidance.

---

*ONB — TFW-4 / Phase A: Baseline & Cleanup | 2026-08-26*

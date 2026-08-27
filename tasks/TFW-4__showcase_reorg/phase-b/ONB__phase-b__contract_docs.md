# ONB — TFW-4 / Phase B: Contract & Docs

> **Date**: 2026-08-26
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — No blocking questions; execution authorized by approved TS
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Phase HL**: [Phase B HL](HL__phase-b__contract_docs.md)
> **TS**: [TS Phase B](TS__phase-b__contract_docs.md)

---

## 1. Understanding

Phase B must establish one count-free canonical project contract, a thin Claude Code adapter,
the approved structured Project North Star, contributor and dated-snapshot release policies, a
root catalog changelog, and decisions D8–D12. The work is local and offline. It must preserve
the accepted Phase A result, all unrelated dirty traces, the generated Codex region in
`AGENTS.md`, and every pre-existing catalog value. Phase C implementation, Phase D live work,
release state, tags, and pushes are outside this execution.

## 2. Entry Points

| Area | Entry point | Executor use |
|------|-------------|--------------|
| Frozen authority | Master HL baseline `d31e60d` | Sole source for §§1, 5, 6, and 7 and decisions D8–D12 |
| Phase derivation | `HL__phase-b__contract_docs.md` | Phase-local scope, sequence, and protected dirty-state context |
| Approved contract | `TS__phase-b__contract_docs.md` | Seven implementation paths, five AC gates, and inherited DoF |
| Predecessor fact | Phase A RF and `✅ APPROVE` REVIEW | Confirms `.agent/` removal, TD-7 resolution, and preserved live `.agents/` adapter |
| Canonical contract | `AGENTS.md` | Human-owned rules around a protected generated Codex region |
| Tool adapter | `CLAUDE.md` | Claude Code-specific context and routing only |
| Product data | `data/communities.json` | Add only the approved top-level `north_star` object |
| Contributor policy | `CONTRIBUTING.md` | Replace duplicated mutable guidance with canonical pointers and approved gates |
| Release policy | `RELEASE.md`, `CHANGELOG.md` | Define future dated snapshots without creating release state |
| Knowledge index | `KNOWLEDGE.md` | Append D8–D12 while preserving D1–D7 and accepted Phase A rows |

### Pre-Implementation Snapshot

| Snapshot | Value |
|----------|-------|
| Git HEAD | `d31e60da5b00a1d9cc9cbd3ba6405220ca62e0f0` |
| Tracked dirty paths | `AGENTS.md`, `KNOWLEDGE.md`, `TECH_DEBT.md`, `tasks/README.md`, `tasks/TFW-4__showcase_reorg/research/iterations.yaml` |
| Untracked protected work | `.agents/**`, Phase A HL/TS/RF/REVIEW/evidence/review, Phase B HL/TS, research iterations 1–2 |
| Managed Codex region | `1515` bytes; SHA-256 `3ec08aeaf1c6fd98dfe8c3d832ce521cc6ed6aaa5ba292686c8a7023850ebf46` |
| Protected path manifest | `115` files; SHA-256 `14802fad376f4c906278b115820b2b57ef0afb361cc507559c1eba5108fa4864` |
| `README.md` | SHA-256 `cc730c6b5a442174b2821a0d891fbaf723a11c7a4356e809942e8856b64894f9` |
| `KNOWLEDGE.md` D1–D7 rows | SHA-256 `0bb77bc1cf5bd99d40c2bc83d386ecb362586b13a987561893705b6224b0ce16` |
| `KNOWLEDGE.md` Phase A rows | 2 rows; SHA-256 `a1c5ec73882091dca5f3c9d8eafe47ba3e3f9386141bb23534dfe6307cc33ccb` |
| Git tags | 0; empty-set SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Pre-existing JSON semantic SHA-256 values, calculated from parsed compact values:

| Top-level key | SHA-256 |
|---------------|---------|
| `meta` | `5af830bea579d5e8494acfafd1d0084d7acd8d1638e6372f2e848b195b66b5e3` |
| `groups` | `768d97073d7b6fdd4b71c6734132393a796b1f688aa0170951af3dba71a25033` |
| `channels` | `f6b1f7419b7c48cb043858c1bd049dbc5d93b2eaa356aabd30563736ece9d8aa` |
| `bots` | `49eb5d75f8f6c081066bdd6bb6de8d6308b5c4d9e921a51da6f588210d5c69c6` |
| `categories` | `093ce984ba6213566889b6aba7fac78b0426a0135388209444998a1f7545a644` |

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The TS is approved, the frozen North Star strings are exact, the scope
budget is within configured limits, and the user's delegation explicitly authorizes faithful
Phase B execution while excluding Phase D and release actions.

## 4. Recommendations (suggestions, not blocking)

1. Keep three local path-scoped commits: ONB; the seven implementation paths; EV/RF and final
   lifecycle state. This separates onboarding, product changes, and result evidence without
   staging unrelated research or adapter state.
2. Treat the current dirty copies of `AGENTS.md`, `KNOWLEDGE.md`, and `tasks/README.md` as the
   merge bases for narrow patches. Restoring any of them from `HEAD` would erase accepted user
   and Coordinator work.

## 5. Risks Found (edge cases, potential issues not in TS)

1. `AGENTS.md` requires a substantial canonicalization around a machine-managed byte range;
   line-oriented edits can accidentally normalize or replace that region. The exact byte hash
   is therefore a hard gate after every edit.
2. `KNOWLEDGE.md` is already dirty with accepted Phase A documentation. A whole-file rewrite or
   reconstruction from the freeze baseline would silently remove those rows.
3. The Task Board is already dirty with Coordinator-owned Phase B planning state. Lifecycle
   updates must be narrow and must not stage research or trace directories by breadth.
4. `north_star` is intentionally not enforced or rendered until Phase C. The Phase B validator
   can pass while ignoring the new key; this is expected and must not be mistaken for completed
   Master DoD 6–7.
5. Future command names belong in canonical documentation now, but their adapters do not exist
   until Phase C. Documentation must describe the planned operational entry points without
   claiming they are currently invocable.

## 6. Inconsistencies with Code (spec vs reality)

No blocking inconsistency. The current validator and generator do not consume `north_star`, as
the approved phase boundary expects. The current `CLAUDE.md`, contributor guide, and missing
release artifacts exhibit the defects Phase B is explicitly approved to correct.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | PV 0 — no Project North Star designated | ✅ | Applied | Phase B stores the approved locus data; README rendering remains Phase C. |
| 2 | PV 1 — `.tfw/README.md` Traces Over Code | ✅ | Applied | Preserve Phase A/research history and create first-class ONB/EV/RF traces. |
| 3 | PV 1 — Single Source of Truth | ✅ | Applied | `AGENTS.md` owns project rules; `CLAUDE.md` points instead of repeating them. |
| 4 | PV 1 — Structural Enforcement | ✅ | Applied | Store the North Star as structured data ready for Phase C schema enforcement. |
| 5 | PV 1 — Honesty Over Convincingness | ✅ | Applied | Use `[Unreleased]`; do not claim a snapshot, tag, push, or live check. |
| 6 | PV 1 — Completeness Over Speed | ✅ | Applied | Deliver complete policies with no placeholder text. |
| 7 | PV 3 — P1 Data is the product | ✅ | Applied | Put `north_star` in `data/communities.json`; leave generated README untouched. |
| 8 | PV 3 — P2 Accuracy over coverage | ✅ | Applied | Preserve the exact approved accuracy language and omission rule. |
| 9 | PV 3 — P3 Validation precedes generation | ✅ | Applied | Run schema validation before the generator-currency gate. |
| 10 | PV 3 — P4 External state is Chat-Loop territory | ✅ | Applied | Perform no network or liveness operation in Phase B. |
| 11 | PV 3 — D2 Separate scripts | ✅ | N/A | Phase B documents sources only and does not alter or merge scripts. |
| 12 | PV 3 — D3 Rate limiting | ✅ | N/A | Network tooling is untouched; the decision remains protected for Phase C/D. |
| 13 | PV 3 — D4 Categories live in data | ✅ | Applied | Remove copied categories from contributor documentation and point to the map. |
| 14 | PV 3 — D7 Task Board outside generated README | ✅ | Applied | Preserve generated README and update only the external lifecycle board. |
| 15 | PV 4 — conventions §9 Tool Adapter Pattern | ✅ | Applied | Keep Claude Code adapter-specific content separate from canonical project rules. |
| 16 | PV 4 — Project North Star rules | ✅ | Applied | Use a README-bound purpose plus all four non-goals; do not nominate a task HL. |
| 17 | PV 4 — contract baseline rules 13–16 | ✅ | Applied | Execute against subject-recovered freeze baseline `d31e60d`. |
| 18 | PV 4 — Commit Attribution | ✅ | Applied | Local commits use `[codex/TFW-4/contract-docs/executor]`; no push. |
| 19 | PV 4 — conventions §14 scope anti-pattern | ✅ | Applied | Restrict implementation to seven paths and lifecycle traces. |
| 20 | PV 4 — conventions §2 Task Board locus discrepancy | ✅ | Applied | Follow accepted project D7 and `tasks/README.md`, not generated `README.md`. |

No new PV item was found that the Coordinator missed. Phase A RF and REVIEW were read as
predecessor facts rather than promoted as new Project Values.

---

*ONB — TFW-4 / Phase B: Contract & Docs | 2026-08-26*

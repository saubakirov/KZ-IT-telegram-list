# Phase HL — TFW-4 / Phase B: Contract & Docs

> **Date**: 2026-08-26
> **Author**: Coordinator (Codex)
> **Status**: 🟡 TS_DRAFT — derivation complete; Phase B TS pre-authorized
> **Contract**: DERIVATION-ONLY — inherits frozen Master HL baseline `d31e60d`
> **Parent HL**: [HL-TFW-4](../HL-TFW-4__showcase_reorg.md)
> **Authority**: Owner pre-authorization covers Phases B–C only when each TS is strictly
> derived from the frozen Master HL. It does not cover Phase D, live sweep, release, tag, or push.

> This Phase HL adds execution context only. It does not define an independent vision,
> acceptance contract, failure contract, or principles; Master HL §§1, 5, 6, and 7 remain the
> sole authority, per `conventions.md` §3 rules 20–21.

---

## 2. Phase Context

### Pre-TS Gate

Phase B depends on the completed Phase A result, not on the earlier Phase A plan.

| Gate input | Actual result | Bearing on Phase B |
|------------|---------------|--------------------|
| Phase A RF | All four Phase A ACs complete; no implementation-scope deviation | The obsolete singular `.agent/` adapter is gone, TD-7 is resolved, and the live `.agents/` adapter survived unchanged |
| Phase A REVIEW | `✅ APPROVE`; no P0–P2 findings | The Phase A outcome is an accepted predecessor for Phase B |
| Phase A observation / TD-9 | Frozen §7.1 hardcoded `agent=claude-code` despite a Codex executor | Resolved by approved amendment A6; prior subjects remain historical evidence |
| Master HL §12 A6 | `✅ APPROVED — saubakirov, 2026-08-26` | The executing product now supplies the truthful attribution token |
| Contract baseline | Freeze commit `d31e60d` | Every Phase B claim derives from this baseline |

The working tree intentionally contains owner/user work that overlaps Phase B:

- `AGENTS.md` has a generated `TFW:CODEX:START` / `TFW:CODEX:END` region. Phase B may edit the
  surrounding canonical contract, but the marked region must remain byte-for-byte unchanged.
- `KNOWLEDGE.md` already carries the applied Phase A documentation update in §§2–3. Phase B adds
  D8–D12 without discarding or re-authoring that work.
- `tasks/README.md`, Phase A traces, research traces, and `.agents/**` are workflow/user state,
  not Phase B implementation scope. Lifecycle status updates must preserve their existing content.

## 3. Derived Phase Outcome

Phase B establishes the repository contract and the release vocabulary that Phase C will make
executable:

```text
BEFORE                                      AFTER PHASE B
AGENTS.md + CLAUDE.md duplicate rules       AGENTS.md canonical; CLAUDE.md thin adapter
hardcoded catalog counts in agent rules     every derived count names its data source
no declared project purpose                 north_star purpose + non-goals live in JSON
CONTRIBUTING copies mutable data             CONTRIBUTING points to canonical sources
no project release contract                 RELEASE.md defines dated snapshots
no project catalog changelog                root CHANGELOG.md tracks catalog changes
decisions D8–D12 only in Master HL          KNOWLEDGE.md indexes D8–D12
```

Derived deliverables:

1. Make `AGENTS.md` the count-free canonical project contract while preserving its generated
   Codex adapter region; reduce `CLAUDE.md` to a Claude-Code-specific adapter.
2. Add the approved Project North Star as structured `north_star` data with one purpose and four
   non-goals; do not alter catalog entries or derived metadata.
3. Replace duplicated and stale contributor instructions with canonical pointers, the North Star
   inclusion gate, and the archive-not-delete policy.
4. Create `RELEASE.md` for dated verified snapshots and a separate root `CHANGELOG.md` for catalog
   history without claiming that a release, tag, or push has occurred.
5. Record Master HL decisions D8–D12 in `KNOWLEDGE.md`, preserving D1–D7 and Phase A additions.

Phase B does not implement schema enforcement, README rendering, archive storage, project command
files, CI, link classification, the live sweep, or any release operation. Those outcomes remain
in Phases C and D exactly as frozen.

## 4. Scope, Sequence, and Files

| Path | Phase action | Boundary |
|------|--------------|----------|
| `AGENTS.md` | MODIFY | Canonical contract around the protected generated Codex region |
| `CLAUDE.md` | MODIFY | Claude-Code-specific pointer, context loading, adapter routing, and execution-mode default only |
| `data/communities.json` | MODIFY | Add only the approved top-level `north_star` block |
| `CONTRIBUTING.md` | MODIFY | Canonical pointers, non-goals, corrected branch, and archive policy |
| `RELEASE.md` | CREATE | Dated verified snapshot policy; no project semver |
| `CHANGELOG.md` | CREATE | Keep-a-Changelog catalog history with a truthful `[Unreleased]` entry |
| `KNOWLEDGE.md` | MODIFY | Append D8–D12 while preserving existing dirty Phase A documentation |

Sequence constraints derived from shared files:

1. Preserve and fingerprint the current `AGENTS.md` managed region and the current
   `KNOWLEDGE.md` Phase A additions before overlapping edits.
2. Establish canonical documentation and structured North Star data without modifying generated
   `README.md` output.
3. Validate the bounded Phase B state and preserve it as the input contract for Phase C.

### Scope Budget

| Measure | Estimate | Limit | Result |
|---------|----------|-------|--------|
| Implementation files | 7 total | 30 | Within budget |
| New implementation files | 2 | 15 | Within budget |
| Modified implementation files | 5 | 30 | Within budget |
| Estimated implementation delta | <1500 LOC | 3000 LOC | Within budget |
| Full phase trace + implementation new files | 11 maximum | 15 | Within budget |
| Full phase trace + implementation paths | 16 maximum | 30 | Within budget |

No budget override or additional split is required.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| Frozen Master HL including approved A5 and A6 | ✅ baseline `d31e60d` |
| Phase A RF | ✅ complete; no scope deviation |
| Phase A REVIEW | ✅ `APPROVE` |
| Owner pre-authorization for a strictly derived Phase B TS | ✅; excludes Phase D, live sweep, release, tag, and push |
| Generated Codex region in `AGENTS.md` | ✅ present; preserve byte-for-byte |
| Phase A documentation already present in `KNOWLEDGE.md` | ✅ present; preserve while adding D8–D12 |
| Network, Telegram, owner CL presence, release credentials | N/A for Phase B |

## 9. Phase Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Canonicalization overwrites the generated Codex adapter block | Medium | High — Codex `/tfw-*` routing is damaged | Treat the marked region as a protected byte range and compare before/after hashes |
| The thin Claude adapter silently restates canonical rules | Medium | High — D9 and DoF 5 fail immediately | Separate adapter routing/context from project rules and scan semantic duplication |
| JSON editing reformats or mutates the catalog | Medium | High — Phase D data changes leak into Phase B | Require a semantic diff limited to top-level `north_star`; preserve all pre-existing values |
| Phase A knowledge updates are lost in the overlapping file | Medium | Medium — accepted trace context disappears | Edit from the current working copy and verify the existing Phase A rows remain |
| Release documents imply a snapshot, tag, or push already happened | Medium | High — history becomes false and authorization is exceeded | Use `[Unreleased]`; state policy and future gates without recording a completed release |
| Phase C implementation leaks into Phase B | Medium | Medium — sequential review boundary breaks | Enforce the seven-path implementation set and leave scripts, commands, CI, and README unchanged |

---

*Phase HL — TFW-4 / Phase B: Contract & Docs | 2026-08-26*

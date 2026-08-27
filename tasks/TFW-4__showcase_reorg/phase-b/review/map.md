# Map — TFW-4 / Phase B: Contract & Docs
> **Mindset:** Experienced newcomer. Understand before judging.
> **RF:** [RF Phase B](../RF__phase-b__contract_docs.md)
> **TS:** [TS Phase B](../TS__phase-b__contract_docs.md)

## Understanding

The executor consolidated the project-facing contract into `AGENTS.md`, reduced `CLAUDE.md`
to adapter-specific routing, stored the approved Project North Star in structured catalog data,
and replaced stale contributor guidance with canonical references and an evidence-based archive
policy. It also created future-facing release and catalog changelog documents, indexed Master HL
decisions D8–D12, and recorded ONB, EV, and RF traces without performing Phase C/D work or an
external action.

The implementation was divided into an ONB-only commit (`ea4a694`), a seven-path implementation
commit (`836c099`), and an EV/RF-only commit (`ce01b17`). The RF claims the pre-existing generated
Codex region, catalog semantics, generated README, accepted Phase A knowledge, unrelated dirty
state, and empty tag set were preserved.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — one canonical agent contract and byte-identical managed Codex region | RF §3 reports count-free `AGENTS.md`, adapter-only `CLAUDE.md`, both project-operation declarations, and the ONB managed-region hash | ✅ Claimed |
| AC-2 — exact `north_star`, semantic-only JSON change, validator pass, generator-current README | RF §3–§4 reports exact frozen strings, unchanged hashes for all pre-existing top-level keys, no `archive`, schema exit 0, and unchanged README hash | ✅ Claimed |
| AC-3 — truthful contributor, release, and changelog policies with no completed release state | RF §3 reports canonical pointers, four non-goals, archive/owner-triage policy, dated-snapshot semantics, `[Unreleased]`, and no tag | ✅ Claimed |
| AC-4 — D8–D12 indexed while D1–D7 and accepted Phase A rows remain | RF §3 reports D8–D12 exactly once, D13–D15 absent, and the two protected knowledge hashes unchanged | ✅ Claimed |
| AC-5 — seven-path bounded implementation, truthful commits, protected dirty state, offline-only execution | RF §1, §3, and §4 report the exact implementation path set, three scoped commits, preserved 115-file manifest, zero tags, and no network/release/push action | ✅ Claimed |

## Deviations from TS

The RF declares no implementation or acceptance-criteria deviation. It records one corrected
read-only harness assertion whose initial pattern omitted Markdown backticks; the implementation
did not change in response. Independent verification of the declarations is deferred to
`verify.md`.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read Master HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES

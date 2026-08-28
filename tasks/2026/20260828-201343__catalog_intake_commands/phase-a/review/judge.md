# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify D1, D2, D3, and D4 independently falsify AC-1, AC-3, AC-4, and AC-7. AC-6 is only partially reproducible from the reviewer-permitted evidence (D5). AC-2's classifier-preservation core, AC-5, and the scope/hash portions of AC-8 hold. |
| 2 | Two clauses, both answered. **(a) Purpose Check** — is this what we set out to do? **(b) Design soundness** | ❌ | **(a) ✅ Aligned:** the Project North Star says, “A catalog whose value is accuracy. Every entry is a live, verified, IT-relevant Kazakhstan Telegram community — verified by a dated network check, never by recollection,” and master HL §1 requires a safe evidence-backed `/kz-add` path with exact owner approval. The work is within that clause and its material harm is preventing false, unverified, or unauthorized catalog entries; it adds no adjacent feature or deferred-phase production mutation. **(b) ❌ Unsound as implemented:** accepting an out-of-grammar authority, empty evidence, inconsistent verified transport, and a non-idempotent exact rerun violates HL principles P1/P3/P5/P6 even though the intended architecture is aligned. |
| 3 | Tech debt documented | ✅ | RF §6 records the genuine stale fixed-date assertion in the historical Phase C harness, including its consequence and owning path. It is promoted as TD-19 rather than repaired under the Reviewer role. |
| 4 | Style & standards | ❌ | Verify D1/D2 violate the TS's closed grammar and closed-schema rules and `.tfw/conventions.md` §11's usable-without-manual-repair quality standard. The remaining implementation is readable, standard-library-only, and stays within the exact path/LOC budget. |
| 5 | Observations collected | ✅ | RF §6's sole observation is independently reproducible: the historical harness hardcodes `2026-01-30`, the current oldest live date is `2026-08-27`, and the reusable matrices still pass. It clears the quality filter and is recorded as TD-19. |
| 6 | RF completeness (§7-9) | ✅ | RF §7 explicitly and correctly reports no human-only Fact Candidates; §8 reports no new execution insight; §9 contains a useful intake/apply state-flow diagram. All three sections are present and substantively appropriate. |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | All eight EV rows name repository artifacts or executable source/tests, all referenced files resolve, and statuses use the allowed vocabulary. The Claude/Codex files physically exist; whether their contents prove the runtime claim is the separate row 8 question. |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | Green signals establish exact scope, production hashes, classifier-body preservation, core deterministic tests, predecessor behavior, and static command parity. They do not establish the omitted adversarial branches (D1–D3), the sealed-manifest membership claim (D5), or fresh-runtime local loading/literal behavior because E7 contains coordinator summaries rather than the TS-required redacted complete transcripts (D4). The Jekyll summary is exact to prior approved evidence, but a fresh container build was not reproduced (D6). |
| 9 | Backward compatibility | ✅ | Existing classifier authority bodies are byte-identical to the sealed base, all predecessor link/command matrices pass, projection outputs are unchanged, and the three pre-existing Claude command semantics retain their authority stops. No existing consumer regression was found. |
| 10 | Safety | ❌ | No secret, external mutation, release, tag, push, or production catalog change occurred. Nevertheless, the production-facing add contract accepts a blank evidence reference and a verified observation inconsistent with failed transport (D2), and its exact rerun can stop after a legitimate partial-equality apply (D3). Those defects weaken the evidence and recovery safeguards for a future authorized catalog mutation. |

Rows 7 and 8 differ deliberately: every named evidence file is present, while present files and
green positive tests do not prove several claims made from them.

## Purpose Check — row 2 clause (a)

Reference set used: master HL contract baseline at refreeze commit
`1e8cecc7bb996cdc98a8e1c0602316100dbf4cc9` and the current Project North Star in
`README.md` § Purpose. The frozen master-HL sections are unchanged from that baseline.

- **Excess and adjacency:** No. The implementation and evidence stay within the Phase A intake,
  command-parity, and fixture-only boundary.
- **Deferral confession:** No. Production candidate application remains in Phase B and was not
  shipped here.
- **Materiality:** Yes. The stated harm—an inaccurate or unauthorized catalog entry—is material to
  the list's core value.

Outcome: **Aligned**. The row fails only its separate design-soundness clause; there is no purpose
failure and no internally inconsistent contract.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D1 — JSON source of truth / generated projections | Production catalog and four projections stayed unchanged. | No — exact Git-blob hashes confirm it. |
| 2 | D2 — offline deterministic work separated from live checks | Offline suites and eight bounded calibration probes are recorded separately. | No. |
| 3 | D4 — categories live in data | Intake consults the current categories map. | No. |
| 4 | D14 — `kz-*` project operations | All three commands use the project namespace. | No. |
| 5 | D18 — target-bound evidence and exact-universe reconciliation | RF claims a closed evidence boundary. | No knowledge contradiction, but Verify D2/D4/D5 show the implementation/evidence does not fully meet the cited rule. |
| 6 | D19 — explicit EN/RU/KK without fallback | Locale fields and gate are explicit. | No. |

No RF Fact Candidate requires challenge: the RF correctly reports none, and the review findings are
repository-discoverable implementation/evidence facts rather than human-only knowledge.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every ⚪ N/A carries a stated reason — no row skipped as a bare ✅? No N/A rows used.
- [x] Row 2(a): answered against the contract baseline and Project North Star, with a quoted clause and named material harm?
- [x] Rows 7 and 8 answered separately, with different reasoning?
- [x] Referenced `verify.md` findings in DoD assessment?
- [x] Checked RF §7-9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or “None”?
- [x] Fact Candidates from RF reviewed — none require challenge?

Stage complete: YES

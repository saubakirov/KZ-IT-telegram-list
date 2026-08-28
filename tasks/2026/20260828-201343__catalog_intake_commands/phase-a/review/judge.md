# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify confirms D1–D6 closures and AC-1/5/6/7 plus the regression/build/scope parts of AC-8. F2 falsifies AC-2/AC-3 because impossible verified classifier tuples can become approved facts. F1 falsifies AC-3/AC-4 because staged bytes need not implement the approved action set. |
| 2 | Two clauses, both answered. **(a) Purpose Check** — is this what we set out to do? **(b) Design soundness** | ❌ | **(a) ✅ Aligned:** the Project North Star says, “A catalog whose value is accuracy. Every entry is a live, verified, IT-relevant Kazakhstan Telegram community — verified by a dated network check, never by recollection,” and master HL §1 requires an exact owner-approval write boundary. The work is within those clauses; the material harm at stake is a false, unverified, or unauthorized catalog entry. **(b) ❌ Unsound as implemented:** F1 allows a staged catalog delta outside the approved candidate set and F2 allows an impossible target-unbound verified tuple to authorize an add, contrary to master-HL P1/P3/P5/P6. |
| 3 | Tech debt documented | ✅ | RF §6's stale Phase C harness date is genuine, scoped to its owner, and already recorded as Low/Open TD-19. No duplicate debt entry is needed. F1/F2 are in-scope revision findings, not deferred debt. |
| 4 | Style & standards | ❌ | Scope, naming, standard-library use, command copies, path neutrality, and 12-path/1,957-line budget hold. The significant-field closure and exact authority/apply standards do not: `validate_observation` accepts impossible producer tuples and `apply_preview` accepts an unrelated stage delta. |
| 5 | Observations collected | ✅ | RF §6's one observation reproduces: the harness hardcodes `2026-01-30`, current oldest live is `2026-08-27`, and the reusable matrices pass. It passes the quality filter and remains TD-19. |
| 6 | RF completeness (§7-9) | ✅ | RF §7 correctly reports no human-only Fact Candidates; §8 reports no new execution strategy; §9 supplies a relevant intake/apply state-flow diagram. All are present and appropriate. |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | All eight EV rows resolve to their named source/tests or repository artifacts. Revised runtime records, partition receipt, exact-SHA build log, summaries, and all four production checkpoints exist. |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | Green evidence independently establishes D1–D6 closure, classifier preservation, command parity/runtime behavior within the stated Claude limit, exact partition allocation, build, scope, controlled hashes, and no external mutation. It does not establish “every non-exact tuple” or “exact approved-set apply”: the suite omits and execution accepts F2 and F1 respectively. |
| 9 | Backward compatibility | ✅ | All six classifier authority bodies are exact to the approved base, predecessor link/command matrices pass, controlled production projections are unchanged, and stats/release authority stops remain intact. No regression of an existing consumer was found. |
| 10 | Safety | ❌ | No secret, credential, production write, browser fallback, image pull, deployment, release, tag, push, or external-service mutation occurred during Phase A/review. The future production-facing boundary is nevertheless unsafe: an empty approved add set can apply unrelated staged catalog bytes (F1), and target-unbound typed evidence can pass as verified (F2). |

Rows 7 and 8 differ deliberately: all named evidence is present, while the present positive suite
does not cover and cannot outweigh two independently executable contract counterexamples.

## Purpose Check — row 2 clause (a)

Reference set used: master HL contract baseline at refreeze commit
`1e8cecc7bb996cdc98a8e1c0602316100dbf4cc9` and the Project North Star in `README.md` § Purpose.
The frozen master-HL sections remain unchanged from that baseline.

- **Excess and adjacency:** No. Implementation/evidence stay within Phase A intake, command
  parity, calibration, fixture apply, and verification boundaries.
- **Deferral confession:** No. Production candidate application remains outside Phase A and did
  not occur.
- **Materiality:** Yes. A false or unauthorized catalog entry directly harms the catalog's stated
  accuracy value.

Outcome: **Aligned**. The row fails only its separate design-soundness clause; there is no purpose
failure and no internally inconsistent contract.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D1 — JSON source of truth / generated projections | Production catalog and four projections stayed unchanged. | No — exact Git blobs confirm it. |
| 2 | D2 — offline deterministic work separated from live checks | Offline suites and eight bounded calibration probes are recorded separately. | No. |
| 3 | D4 — categories live in data | Intake consults the current category map. | No. |
| 4 | D14 — `kz-*` project operations | All three commands use the project namespace. | No. |
| 5 | D18 — target-bound evidence and exact-universe reconciliation | RF claims a closed evidence boundary. | No knowledge contradiction, but F2 is an implementation violation of this cited rule. |
| 6 | D19 — explicit EN/RU/KK without fallback | Locale fields and gates are explicit. | No. |

No RF Fact Candidate requires challenge. The RF correctly reports none, and F1/F2 are
repository-discoverable implementation facts rather than human-only knowledge.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every ⚪ N/A carries a stated reason — no row skipped as a bare ✅? No N/A rows used.
- [x] Row 2(a): answered against the contract baseline and Project North Star, with a quoted clause and named harm?
- [x] Rows 7 and 8 answered separately, with different reasoning?
- [x] Referenced `verify.md` findings in DoD assessment?
- [x] Checked RF §7-9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or “None”?
- [x] Fact Candidates from RF reviewed — none require challenge?

Stage complete: YES

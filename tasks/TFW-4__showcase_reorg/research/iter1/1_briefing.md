# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-4](../../HL-TFW-4__showcase_reorg.md)
> Goal: Make the repository a checkable TFW reference implementation whose published Telegram liveness and member-count claims come from a repeatable, dated, evidenced operation.

## Research Plan

### Gather

- Fetch exactly two live `t.me` pages—one high-count group and one channel—and one deliberately invalid handle, within the three-request control-file budget.
- Capture the response status, the relevant `tgme_page_extra` markup, and the invalid page's error marker without storing whole third-party pages.
- Run each current `MEMBER_PATTERNS` expression against the observed HTML and identify which pattern, if any, supplies the count.
- Decompose the decision into independent dimensions: endpoint liveness signal, count-markup shape, and parser compatibility.

### Extract

- Probe approximately eight additional catalog handles spanning groups, channels, and bots, including all four entries currently lacking `member_count`.
- Preserve the current `BATCH_SIZE = 3`, `BATCH_DELAY = 1.5s`, and `REQUEST_DELAY = 0.3s` cadence; record HTTP status, Telegram error markers, parsed count, and any HTTP 429 response.
- Cross-reference type, existing-count state, response classification, and parser result to expose configurations hidden by the three-request Gather sample.
- Use the bounded sample to assess H2 and the rate-limit risk without extrapolating a catalog-wide dead count.

### Challenge

- Fetch the live GitHub-rendered README and compare its category-heading anchors with every TOC href emitted for the 18 current category display names.
- Test H4 on all categories, including every name containing `&`, rather than accepting a single illustrative slug.
- Pairwise-check the surviving H1/H2/H4 configurations against the frozen Phase C and Phase D contract.
- Decide whether any refuted assumption is already addressable inside frozen Phase C or requires an amendment proposal or separate task; do not alter the HL.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | `t.me/{handle}` still returns member/subscriber counts in markup matched by at least one of the three `MEMBER_PATTERNS` in `validate_links.py:40-44`, and a dead handle still yields `tgme_page_error`. | needs-research |
| H2 | At least one of the 63 catalogued handles is dead or private, so Phase D exercises the archive path with real data. | needs-research |
| H4 | GitHub's heading-anchor algorithm produces `#data--analytics` for `### Data & Analytics`, so the generator's current anchor expression yields working links for every category name in the data. | needs-research |

## Scope Intent

- **In scope:** Read-only inspection of the relevant scripts and data; three bounded Gather requests; approximately eight bounded Extract requests at the existing throttle; one GitHub-rendered README/anchor inspection in Challenge; classification of findings into RES decisions, hypotheses, HL refinements, and amendment proposals.
- **Out of scope:** The full 63-entry sweep; `--update`; any write to `data/communities.json`; any code, README, HL, TS, ONB, RF, REVIEW, Task Board, or control-file change; archive triage; release, tag, push, or editorial re-vetting.

## Guiding Questions

1. Do the live and invalid Telegram responses still supply the exact liveness and count signals the current parser assumes?
2. Across the bounded mixed sample, which type/count-state/parser configurations survive, and is there any evidence of rate limiting or real catalog death?
3. Do all generated category hrefs resolve in GitHub's live rendered README, and what contract consequence follows from any mismatch?

## User Direction

The delegated command requires mandatory iteration 1 under the Researcher role lock and designates `research/iterations.yaml` as the control source. It pre-approves the focused mode and the bounded H1/H2/H4 probes described there. Existing user changes in `AGENTS.md` and `.agents/` must remain untouched. No release action is authorized.

Baseline audit found that `iterations.yaml` still names freeze `f871951`, while Git history contains the later A2 re-freeze `70ddfa6` and the current HL records A2 as approved. This metadata drift does not change the empirical H1/H2/H4 scope; research uses the current frozen HL and will report the drift for Coordinator correction rather than edit the Coordinator-owned control file.

---
Stage complete: YES

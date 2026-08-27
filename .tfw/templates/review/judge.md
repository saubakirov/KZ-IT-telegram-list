# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

> Every row is asked in every review. There is no genre that exempts a row.
> **Status vocabulary:** `✅` holds · `❌` fails, with a specific finding · `⚪ N/A` does not apply here.
> `⚪ N/A` requires a stated reason in Evidence. A row skipped as a bare `✅` is a silent skip and the stage is not complete.
> Percentages are measured non-✅ rates from a 637-row corpus — they are why the row exists, not decoration.

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅/❌/⚪ | {reference verify.md §TS↔RF and specific items} |
| 2 | Two clauses, both answered. **(a) Purpose Check** — *is this what we set out to do?* Answered against the reference set below, never against the TS _(~4 blocks in 149 reviews, a different corpus; kept on consequence rather than frequency — the miss it exists to catch cost six days of work rejected wholesale)_. **(b) Design soundness** _(4.5%)_: is the design itself sound against HL §7 principles — not "is it named well", which is row 4 | ✅/❌/⚪ | {(a) one field: quote the clause served **and** name the concrete harm — see Purpose Check below; (b) answered separately} |
| 3 | Tech debt documented | ✅/❌/⚪ | {RF §6 Observations present/absent} |
| 4 | Style & standards | ✅/❌/⚪ | {conventions followed? naming?} |
| 5 | Observations collected | ✅/❌/⚪ | {quality filter: are they real issues?} |
| 6 | RF completeness (§7-9) | ✅/❌/⚪ | {§7 Fact Candidates, §8 Strategic Insights, §9 Diagrams — present?} |
| 7 | Evidence completeness — does the evidence **exist**? | ✅/❌/⚪ | {All TS Evidence fields covered in EV file? Statuses valid?} |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? _(16.1% — the highest-firing check in TFW review)_ | ✅/❌/⚪ | {name the green signal and say what it does or does not establish} |
| 9 | Backward compatibility _(8.5%)_ — does the change break an existing consumer: an interface, a template section number, a document anchor, a downstream process, a report someone already relies on? | ✅/❌/⚪ | {who consumes this, and what happens to them} |
| 10 | Safety _(4.0%)_ — secrets, credentials, destructive or irreversible operations. Kept on consequence, not on rate | ✅/❌/⚪ | {what was checked, or why nothing here can cause harm} |

> **Rows 7 and 8 are not the same question, and answering them the same way means one of them was not asked.**
> Row 7 asks whether the evidence is *there*. Row 8 asks whether it *proves what it is offered to prove*:
> a passing test that tests the wrong thing, a self-declared gate marked green while unmet, a citation
> that does not support the sentence it is attached to, a screenshot of a page that was never the page
> under test. `✅` on 7 with `❌` on 8 is the normal shape of a real finding.

## Purpose Check — row 2 clause (a)

> **Reference set:** the **master HL at its contract baseline**, plus the **Project North Star**.
> Fallback chain: project north star → master HL §1 at the contract baseline. A project with no north star
> is never blocked on its absence. Recovering the baseline: `conventions.md` §3 rule 15.
>
> **Invalid references.** The **TS** is downstream of any drift — measuring against it can only confirm it.
> A **Phase HL** is derivation-only and holds nothing approved (`conventions.md` §3). A review that answers
> this row from either has not answered it.

**One field, one sentence: quote the clause served *and* name the concrete harm at stake.** A citation
that resolves but is irrelevant fails the row. A harm asserted with no citation fails it. `✅` with an
empty field fails it. An `⚪ N/A` must name which reference set was unavailable.

Three tests, each answerable *no*:

1. **Excess and adjacency** — does the result deliver something the cited clause does not ask for, or
   something a baseline non-goal, a DoF item or a phase boundary excludes?
2. **Deferral confession** — does the spec or the result itself name a different home for this work and
   ship it here anyway?
3. **Materiality** — is the harm material impact on the value? A wording objection is not a harm and
   cannot ground a block.

**Not sufficient grounds to `✅`:** *"the TS scoped it this way"* · *"tests are green"*. Both are true of
work that should not exist.

**Three outcomes.** Status stays `✅/❌/⚪`: the third is a distinct finding, not a fourth symbol.

| Outcome | Status | Finding | Routes to |
|---------|--------|---------|-----------|
| Aligned | ✅ | the filled field | — |
| Purpose failure | ❌ | **`not fit for purpose`** | the **owner** — it stands with every other check passing |
| Reference set internally inconsistent — the baseline and the north star, or two baseline clauses, cannot both be satisfied | ❌ | **contract defect**, both clauses quoted | the **owner**. Never the executor: not a work defect, and they have no channel to a frozen section |

> **The bar for the third outcome.** Two clauses conflict only if satisfying one *necessarily* violates the
> other. Read each to the end of its sentence: a clause that qualifies itself in its second half is not in
> tension with the clause that discharges it. Surface tension is not inconsistency — and a contract that is
> coherent but wrong for the product is the *purpose* question above, not this one. **No instance has been
> observed** in the corpus this check was validated against.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|

> If no KNOWLEDGE.md exists or nothing applies: "No applicable knowledge items."

## Checkpoint

**Self-check:**
- [ ] Every checklist item has evidence (not just ✅/❌)?
- [ ] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅?
- [ ] Row 2(a): answered against the contract baseline and the north star — never the TS or a Phase HL — with a quoted clause **and** a named harm in one field?
- [ ] Rows 7 and 8 answered separately, with different reasoning?
- [ ] Referenced verify.md findings in DoD assessment?
- [ ] Checked RF §7-9 for presence AND quality (not just existence)?
- [ ] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [ ] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES / NO

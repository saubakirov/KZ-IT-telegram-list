---
description: Verify Kazakhstan Telegram catalog statistics with evidence and owner triage
---

# KZ Stats — Verified Catalog Sweep

> **Mode:** CL (Chat Loop)
> **Authority:** This command observes live Telegram state and mutates verified catalog facts.
> Run it only when the owner explicitly invokes `/kz-stats`. Never infer liveness, counts, link
> continuity, or death from recollection or missing evidence.

Read [AGENTS.md](../../AGENTS.md), [RELEASE.md](../../RELEASE.md), and the active approved TFW
task before starting. `data/communities.json` remains the source of truth; `README.md` remains
generated output.

## Required Outputs

- Raw machine-readable summary from `scripts/validate_links.py` retained as task evidence.
- Human-readable count deltas: grew, shrank, unchanged, and first count.
- Every `ambiguous`, `non_target`, and `failed` result listed with its observed reason.
- A per-entry disposition: verify current target, repair live link, archive proven death, or
  unresolved.
- Updated JSON and generated README only for observations supported by retained evidence.

## Operation

1. **Preflight and evidence path**
   - Confirm the owner requested the live sweep in the current conversation.
   - Run `python scripts/validate_schema.py`; stop on a non-zero exit.
   - Create a temporary machine-summary path outside the repository and a durable evidence path
     inside the active task. Do not place credentials, cookies, or authenticated session data in
     either artifact.

2. **Run the catalog sweep**
   - Run `python scripts/validate_links.py --update --summary-json <temporary-summary-path>`.
   - A non-zero exit caused by unresolved results is expected input to triage, not permission to
     discard the summary. A missing/malformed summary or execution error stops the operation.
   - Copy the raw summary into the active task evidence folder and verify
     `schema_version`, `run_date`, `totals`, and `entries` before rendering results.

3. **Render observations, not console guesses**
   - Present `grew`, `shrank`, `unchanged`, `first_count`, and signed aggregate delta from the
     JSON fields.
   - Present every `ambiguous`, `non_target`, and `failed` record, including declared/observed
     type, target binding, visible name, old/observed counts, and reason.
   - Never scrape human-formatted validator output to reconstruct these values.

4. **Retry unresolved scripted results once**
   - For each unresolved handle, run
     `python scripts/validate_links.py --handle <handle> --update --summary-json <retry-path>`
     once and retain that retry summary as evidence.
   - A verified retry may update the observed date/count. A repeated failure, contact shell,
     type mismatch, or non-target page is still not proof of community death.

5. **Use browser evidence only as a bounded fallback**
   - Use a visible Telegram preview only when scripted classification cannot establish identity.
   - The capture must bind the requested handle, visible name, declared type, and observed count
     or explicit no-count. A generic Telegram landing/contact shell is not evidence.
   - Reuse one temporary Chrome tab sequentially for all fallback checks. Do not accumulate one
     tab per handle. Close the temporary tab after the batch or immediately when evidence
     collection ends, and record the cleanup observation.
   - Authenticated peer resolution is admissible only when peer kind and continuity with the
     catalogued community are evidenced. Do not retain session secrets in task artifacts.

6. **Assign one evidence-backed disposition per unresolved entry**
   - **Verify current target:** target-specific evidence binds the stored handle to the intended
     peer and declared type. Write the observation date; write a count only when observed.
   - **Repair live link:** evidence shows the same community lives at a replacement handle/link.
     Obtain owner approval for the repair, update the link, recheck the repaired target, and only
     then write its date/count. Never archive it as dead.
   - **Archive proven death:** independent evidence identifies the same historical community as
     deleted or closed, and the owner approves that exact entry. Run
     `python scripts/validate_links.py --archive <handle> --reason <evidence-based-reason> --evidence-ref <artifact-reference> --owner-approved`.
     The mutation moves the complete record and adds `type`, `died_on`, and `reason`.
   - **Unresolved:** no current binding, replacement, or independent death evidence exists. Do
     not change its date/count and do not archive it. Record the blocker; a full release is not
     eligible.

   Owner approval alone is not death evidence. One failed request, an unoccupied/wrong handle,
   ambiguity, or absence of a numeric count is never sufficient to archive.

7. **Validate and regenerate**
   - Run `python scripts/validate_schema.py`; stop on error.
   - Run `python scripts/generate_readme.py`; never edit `README.md` directly.
   - Run `python scripts/generate_readme.py --check`; require exit zero.
   - Confirm every live catalog entry is covered by the retained sweep/retry/fallback evidence
     before calling the sweep complete.

8. **Report and stop**
   - Report updated dates/counts, approved repairs, approved archives, unresolved entries, raw
     evidence paths, schema result, and README currency result.
   - Do not create a release commit, changelog snapshot section, tag, or push. `/kz-release` is a
     separate owner-invoked operation with its own hard authority gate.

## Failure Conditions

- Any catalog fact is written without target-specific observed evidence.
- Any ambiguous or failed result is automatically archived.
- A browser tab remains open after fallback evidence collection.
- The raw JSON summary or retry evidence is missing.
- README is edited by hand, or validation/generation gates fail.
- The operation proceeds to release, tag, or push work.

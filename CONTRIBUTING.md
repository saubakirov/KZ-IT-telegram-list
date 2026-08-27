# Contributing to Awesome Kazakhstan IT Telegram

Thank you for helping maintain a trustworthy catalog of Kazakhstan IT Telegram communities.
Accuracy matters more than list size: submit only information that can be checked.

## Canonical Sources

- [`data/communities.json`](data/communities.json) is the product and the source of truth.
- [`AGENTS.md`](AGENTS.md) owns the generation contract, data rules, validation commands,
  inclusion criteria, and change procedure.
- `README.md` is generated output. Never edit it directly.

Read the [JSON entry format](AGENTS.md#json-entry-format), [change
procedure](AGENTS.md#change-procedure), and [script reference](AGENTS.md#scripts) before making
a contribution. This guide intentionally does not copy those mutable rules.

## Inclusion Gate

The approved Project North Star is stored in the top-level `north_star` object in
[`data/communities.json`](data/communities.json). A proposed entry must serve its purpose and
must pass every non-goal:

1. A directory of every Kazakhstan Telegram chat — IT relevance is a gate, not a hint.
2. A promotion channel — no purely commercial or paid-placement entries.
3. A hand-edited list — `README.md` is an artifact; the data is the product.
4. An estimator — an unverifiable member count is omitted, never guessed.

In practical terms, an entry must be IT-focused, relevant to Kazakhstan, active, and useful to
the community. Spam and purely commercial placements are rejected.

## Contribution Workflow

1. Fork the repository and clone your fork.
2. Edit [`data/communities.json`](data/communities.json), never `README.md` directly.
3. Follow the canonical [`AGENTS.md` change procedure](AGENTS.md#change-procedure) exactly. This
   guide deliberately does not reproduce or shorten its commands.
4. Commit the source data and generated artifact together, then open a pull request against
   `master`.

The canonical procedure includes a live-state step. If that environment is unavailable, disclose
the missing evidence and leave the affected facts unchanged; do not substitute a different
command and call the canonical procedure complete.

## Categories

Use a key that exists in the current `categories` map in
[`data/communities.json`](data/communities.json). The map is intentionally not copied into this
guide. List the current keys and display names from the source with:

```bash
python -c "import json; d=json.load(open('data/communities.json', encoding='utf-8')); print('\n'.join(f'{k}: {v}' for k, v in d['categories'].items()))"
```

## Verification and Member Counts

- A `last_verified` date records an actual link check, not the date a contributor remembered or
  edited the entry.
- Add or change `member_count` only from an observed Telegram response. Omit an unverifiable
  count.
- Keep handles bare: no `@` and no `t.me/` prefix.
- Provide the English description required by the canonical data rules.

## Dead-Link and Archive Policy

Never silently delete a community. A non-response is retried, then presented with its evidence
for owner triage. Only a community supported by evidence of death is moved from the live catalog
to `archive`, where its original identity is retained with `died_on` and a non-empty `reason`.
Ambiguous or unavailable evidence leaves the entry unresolved rather than guessed dead.

## Pull Request Checklist

- [ ] The proposal passes every North Star inclusion gate.
- [ ] Only canonical source data was edited by hand; `README.md` was regenerated.
- [ ] Every new or changed fact has observable evidence.
- [ ] The canonical `AGENTS.md` change procedure was followed without substituting shorter
      commands; any unavailable live evidence is disclosed and the affected facts remain unchanged.
- [ ] The source JSON and generated README are committed together.
- [ ] The target branch is `master`.

## Code of Conduct

Be respectful, avoid spam, and prefer verifiable quality over quantity.

## Questions

Open an issue and include the proposed handle plus the evidence available for its relevance and
current liveness.

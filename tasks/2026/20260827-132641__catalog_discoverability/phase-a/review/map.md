# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [Phase A RF](../RF__phase-a__multilingual_catalog.md)
> TS: [Phase A TS](../TS__phase-a__multilingual_catalog.md)

## Understanding

The original Executor result extended `data/communities.json` with explicit EN/RU/KK content, five
intent definitions, and a digest-bound review record. One locale-aware generator produces the
English GitHub README plus EN/RU/KK Pages bodies, while schema and regression gates enforce
completeness, currency, stable destinations, Markdown safety, rendered-link parity, and stale-review
failure.

The first formal review at commit `2cd3977c0e795e4803c78993919ee1630430c4c7` issued `REVISE` on
digest `80ee30ba87003b61de862d63f0a01cea213d5bc08320019af6b4e513fbb33fd0`. It accepted the
architecture and deterministic gates but returned seven material Russian findings, accepted
copy-edit classes, and two explicitly rejected advisory suggestions to the same Executor loop.

The Executor then changed 39 Russian source values and the source review digest, regenerated all
four outputs (only `ru/index.md` changed bytes), and refreshed EV/RF. Supplied Executor commits
`99bbf5cc47060a076ed4363728dca6fe78bc68fd` and
`ab760090f18c5437212762555475c7131bd79de6` were cherry-picked verbatim as local integration commits
`bc7764af90c04fad66b4f8effdcf7a6e2d3f76cc` and
`e00a629489a96e87333c4c5c171bda134aaf4628`. The revised candidate claims digest
`51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc` and a fresh exact-model
Antigravity `PASS`; both remain declarations for Verify to reproduce.

## TS ↔ RF Alignment

| TS requirement | Revised RF claim | Aligned? |
|----------------|------------------|----------|
| AC-1 — complete one-source locale and intent contract | RF §§1–4 claims complete EN/RU/KK values, 39 Russian revisions, exact intent definitions, refreshed digest, and zero invariant-fact changes | ✅ |
| AC-2 — four current, complete projections | RF §§3–4 claims all four outputs were regenerated/current, with English/KK/README byte-identical and only RU changed | ✅ |
| AC-3 — concise, navigable ready catalog | RF §3 claims catalog-first language/type/intent navigation with stable destinations remains intact | ✅ |
| AC-4 — Markdown and GitHub-render target parity | RF §4 claims HTTP 200, 64/64 Telegram pairs, 71/71 fragments, one H1, and no duplicate normalized IDs | ✅ |
| AC-5 — safe failure on drift and invalid inputs | RF §§3–4 claims the twelve deterministic positive/negative tests plus schema and currency gates were rerun | ✅ |
| AC-6 — independent advisory and formal digest-bound verdict | RF §§2–5 claims every prior finding was dispositioned and a complete revised exact-model advisory returned `PASS` on digest `51db402d…`; formal acceptance remains pending this review | ✅ |
| AC-7 — preserve Phase A boundary and budgets | RF §§3–5 claims the architecture/eight-path scope is unchanged, revision edits are limited to source/RU/EV/RF, facts remain invariant, budgets hold, and no external mutation occurred | ✅ |

## Revision Disposition Map

| Prior formal item | Revised RF/EV claim |
|-------------------|---------------------|
| Seven material Russian findings | All seven source keys corrected and listed individually in EV. |
| Accepted compound/hyphenation, terminology, punctuation, and neutral-tone classes | 32 additional Russian values revised; EV lists the exact 39-key delta and representative normalized forms. |
| Rejected `1C` Cyrillic-confusable suggestion | Unapplied; `kz_1C` identity/name/Russian token claimed byte-identical. |
| Rejected visible-backslash suggestion | Unapplied; generator/escaping architecture and rendered output claimed unchanged. |
| Regeneration and deterministic gates | All four regenerated; tests/schema/currency/render/budget gates claimed rerun after final wording. |
| New content binding | Digest changed from rejected `80ee30ba…` to candidate `51db402d…`; 401-key first-candidate attachment claimed byte-identical because no prior digest was approved. |
| Fresh independent advisory | Exact `gemini-3.7-flash-high`, plan+sandbox, UTF-8 object-valued stream-json; claimed `SUCCESS`, `PASS`, no findings. |

## Deviations from TS

The revised RF reports no TS deviation. The revision adds no architecture or Phase B scope; it is the
specified AC-6 return loop. Cherry-pick SHA changes are integration identity only—the supplied
Executor commits and local commits have the same trees and retain Executor-authored subjects.

## Checkpoint

**Self-check:**
- [x] Read revised RF §1–§5 completely?
- [x] Read TS DoD and matched each item to revised RF §3?
- [x] Read frozen Master HL §7 Principles and preserved the prior purpose/baseline map?
- [x] Read ONB and prior REVIEW — were blocking questions and every prior disposition understood?

Stage complete: YES

# Challenge — “What do we NOT expect?”
> **Mindset:** Critic. The selected contracts are attacked here; architecture selection remains closed.
> Parent: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Make one verified Kazakhstan IT Telegram catalog easy to discover, understand, and use in English, Russian, and Kazakh without creating drifting catalogs or weakening accuracy.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------|------------------|
| D1 review binding | Presence alone or an out-of-band checklist | D2 incomplete locale | Fail the multilingual gate | Presence cannot prove that the reviewed content is the content being generated, so the claimed fail-closed state is not executable. |
| D1 review binding | Per-field metadata | D2 incomplete locale | Silent fallback | Field-level approval still permits unreviewed English to appear as RU/KK and contradicts the frozen no-fallback outcome. |
| D2 incomplete locale | Omit the route or publish an incomplete route | D4 evidence | Any evidence family | Either behavior violates the frozen requirement for three complete routes; stronger tests cannot make the output acceptable. |
| D3 intent rules | Keyword/description inference | D1 review binding | Locale payload digest | Translated prose changes could silently change membership even though intent meaning is meant to be locale-invariant. |
| D3 intent rules | Full handle enumeration | D4 evidence | Source assertions only | The duplicated lists can drift from category truth, and source-only evidence cannot establish their destinations on either public renderer. |
| D4 render evidence | Source only | D6 destinations | Any anchor family | The measured `kzquake` and archive failures prove source URL presence does not prove an interactive link. |
| D4 render evidence | Post-deployment only | D5 external disposition | Required Pages/settings preconditions | It discovers deterministic rendering defects only after an owner-controlled deployment and cannot be the sole release-preparation gate. |
| D5 external disposition | Positive rank or AI inclusion gate | Any implementation contract | Any | Ranking and inclusion are variable third-party outcomes. Making them release gates creates an unachievable product guarantee. |
| D6 destinations | Renderer or display-text slugs | Multilingual routes | EN/RU/KK | Localized headings and renderer-specific slugging cannot provide one stable, language-independent destination contract. |

### Surviving configurations

| Config | Review | Incomplete state | Intent rules | Render evidence | External disposition | Destinations | Verdict |
|--------|--------|------------------|--------------|-----------------|----------------------|--------------|---------|
| C1 | Locale digest | Fail all | Categories + exceptional includes | Layered | Typed | Explicit IDs | **Selected**; complete and proportional. |
| C2 | Per-field metadata | Fail all | Categories + include/exclude | Layered | Typed | Explicit IDs | Viable but needlessly duplicates 131 approval states and an unused exclusion mechanism. |
| C6 | Locale digest | Fail all | Full enumeration | API + local Jekyll | All required | Explicit IDs | Mechanically testable, but membership duplicates category facts and it lacks public-render acceptance. |
| C8 | Locale digest | Fail all | Categories + exceptional includes | Public DOM only | Typed | Explicit IDs | Can detect final defects but gives no safe pre-publication decision point. |
| C9 | Locale digest | Fail all | Categories + exceptional includes | Layered | All required | Explicit IDs | Technically strict but incorrectly lets optional Search Console access block an otherwise valid release. |
| C10 | Locale digest | Fail all | Categories + exceptional includes | Layered | Typed | Renderer slugs | Survives simple pages, but fails the cross-language and cross-render stability attack. |

**Unexpected survivor:** C2 can express the same semantic approval as C1. It is rejected for proportionality, not correctness: a digest plus a changed-key review record provides equivalent content binding without maintaining 131 independent approval flags.

## Findings

### C1: Digest validity needs an explicit review lifecycle, not just a hash

An exact payload digest proves identity but does not say what a reviewer examined after a change. The selected approval record therefore needs these fields:

```text
locale
reviewer_identity
reviewer_qualification
reviewed_at (ISO date)
verdict = APPROVED
payload_digest
previous_approved_ref (immutable Git commit; null only for first approval)
previous_approved_digest (null only for first approval)
changed_keys[] (exact payload paths; all keys on first approval)
```

The checker loads the prior approved payload at `previous_approved_ref`, verifies its digest, and recomputes both the current payload digest and changed-key set. A missing, extra, or mismatched key fails approval. Unchanged values inherit only through that immutable repository comparison; the reviewer approves the complete resulting payload, not merely a patch. An unchanged technical term such as `AI` or `DevOps` is acceptable only when it is an explicit value in that locale payload and is covered by its approval. Community names, handles, URLs, counts, dates, category IDs, and code/file tokens remain declared invariants outside the linguistic payload.

This is an **execution input gate**: a later Executor may add generator support only after owner-designated qualified human reviewers supply complete approved EN/RU/KK payloads and attestations. A machine or AI may propose text but cannot certify it. No current Kazakh string is invented or certified by this research. Missing reviewer identity, recorded qualification, approval, payload, or matching digest blocks Phase A; no partial locale artifacts are generated.

### C2: “Qualified” must be scoped without assuming a particular person is qualified

The owner designates the reviewer, but designation alone is not linguistic qualification. EN review requires English fluency plus understanding of this catalog's Kazakhstan IT/Telegram terminology. RU and KK each require fluency/native competence in that language plus the same domain competence. One person may review multiple languages only when the record states the qualification basis for each. Automated language detection can flag script or blank-value anomalies, but cannot issue `APPROVED`.

This closes H1's last conditional part: the generator design does not need to know who translates, but it must know the finite payload, exact approver evidence, digest lifecycle, and fail-closed behavior.

### C3: Broad Engineering membership does not imply 46 duplicated navigation links

The 46-member Engineering set is deliberately broader than a job or event vertical: it includes technical practice, CS education, engineering leadership, and developer utilities. It excludes jobs-only feeds, general tech news, marketplaces, project management, public-service bots, and the event feed. `nu_acm_w` belongs in Engineering because its reviewed description is a Women in Computing/CS education community; it does **not** belong in Jobs because it is not a vacancy feed.

The public intent map does not repeat all 46 entries. It renders links to each non-empty selected type/category destination plus the ten exceptional Engineering entry destinations. Top navigation contains one Engineering link. Thus the intent layer remains a compact route into the one full catalog rather than a second catalog.

Future members of a selected category are intentionally included. A new exceptional case requires a reviewed configuration change. The present audit found no false positive inside a selected category, so a runtime exclusion list would encode no current fact. If that changes, the category should be corrected or a later reviewed exclusion capability should be specified; silent keyword inference remains forbidden. H3 is therefore confirmed for the current snapshot, with ordinary owner acceptance of the exact matrix in the later TS rather than another research branch.

### C4: Explicit anchors are supported, but must be tested on both renderers

GitHub documents standard HTML anchors such as `<a name="unique-anchor-name"></a>` for custom navigation points and recommends a unique naming scheme; it also documents that automatically generated heading anchors depend on heading text and duplicate order. This supports generator-owned stable IDs, but it does not prove Jekyll output. A6 and A7/P2-P3 must therefore resolve every generated fragment independently on GitHub-rendered README and Pages.

Source: <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#custom-anchors>.

The cross-render assertion remains a multiset of `(visible source name, normalized Telegram URL)` anchors, not URL substrings. Synthetic fixtures for pipe, brackets, emphasis, underscore, backtick, backslash, angle bracket, and ampersand supplement the actual `kzquake` and archive cases. This is the smallest contract that would have caught all three measured Pages failures while preserving the full Telegram target set.

### C5: The evidence layers are not redundant

Each layer answers a different failure question:

| Layer | Unique question |
|-------|-----------------|
| Source/validator | Are locale, intent, review, and source references complete and internally valid? |
| Generated Markdown | Did escaping and generation preserve every record and target before either renderer interprets it? |
| GitHub rendered API at exact commit | Does GitHub's real Markdown renderer produce one H1, stable destinations, and the expected anchors? |
| Local Pages build from actual source | Does the selected GitHub Pages/Jekyll dependency set produce the required routes and DOM before deployment? |
| Public HTTP/DOM | Did the configured public environment actually deploy those routes, metadata, JSON, and links? |
| Bounded viewport evidence | Is the frozen first-screen outcome true at the two exact viewport sizes? |

GitHub permits branch publication only from repository root or `/docs`, or publication through a GitHub Actions workflow; an admin or maintainer configures the source. Therefore the local build must use the authenticated actual source rather than infer root from the present URL or output. If the source cannot be obtained, Phase B is deferred/blocked; it is not permission to reopen the root/`/ru/`/`/kk/` architecture.

Source: <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>.

The mobile assertion is intentionally numeric rather than a screenshot opinion. At 390×844 and 1366×768, each required element's bounding rectangle must be visible and wholly inside the viewport, with no horizontal overflow. Required elements are H1, one summary, generated freshness, all three language links, type navigation, intent navigation, and at least one live Telegram link. For GitHub, y-coordinates are rebased to the README article top because GitHub owns surrounding chrome. Screenshots accompany, but do not replace, bounding-box assertions. This is demanding but matches the frozen first-screen outcome and is executable with standard browser assertions.

### C6: Metadata validation is a support signal, never retrieval proof

Parsing the public DOM can deterministically establish `html lang`, one self-canonical, three reciprocal alternates, sitemap membership, and the exact `Dataset`/`DataDownload` fields. The public JSON digest can establish machine-readable parity with the deployed commit. Search Console and a rich-results inspection can add environment evidence, but neither changes these source/DOM assertions.

Google's URL Inspection live test requires a URL in a property and reports potential indexing/structured-data issues; the page must be publicly accessible. Dataset is among the recognized structured-data types, but tool visibility and indexed status remain external observations. Thus:

- if owner access is supplied, record the property, date, inspected URLs/sitemap, and observed result, and require that evidence for the conditional gate;
- if the owner states access is unavailable, record the evidence item `N/A — owner access unavailable`; publication does not fail;
- use `DEFERRED` only if the owner expects to supply access later and explicitly keeps the item pending.

Source: <https://support.google.com/webmasters/answer/9012289>.

OpenAI states that allowing `OAI-SearchBot` is a prerequisite for eligibility in ChatGPT search results, not a promise of inclusion. Rank and AI inclusion tests therefore pass when a timestamped observation report exists and explicitly treats a positive or negative result as non-gating. A requirement that the site rank or be cited would fail this research contract.

Source: <https://developers.openai.com/api/docs/bots>.

### C7: Final external-gate boundaries

| Gate | Required before | Owner-controlled input/evidence | If absent or negative |
|------|-----------------|---------------------------------|-----------------------|
| Qualified EN/RU/KK content | Phase A implementation/generation | Complete payloads and content-bound approvals | Block Phase A; do not generate partial/fallback artifacts. |
| Authenticated Pages source | Phase B local build/deployment | Current branch/workflow and source folder, or explicit owner authorization to change it | Defer/block Phase B only; do not redesign architecture. |
| Repository settings | Any settings mutation | Before snapshot, exact approved description/homepage/topics/social asset, after snapshot | Do not mutate; repository-controlled files remain independently testable. |
| Search Console | Conditional post-public evidence | Owner states access available/unavailable | `VERIFIED` when available; `N/A` or explicit `DEFERRED` otherwise; never a publication blocker. |
| Rank/AI retrieval | Post-public observation | None beyond public access | Record positive/negative result, locale, query, surface, and timestamp; never alter acceptance. |

No authenticated Pages source, settings screen, Search Console property, rank, or AI citation is an open implementation-design question. They are typed entry gates or observations with predetermined dispositions. This closes the remaining conditional parts of H2 and H4 without fabricating external evidence.

### C8: Hypothesis disposition after attack

| Hypothesis | Result | Boundary |
|------------|--------|----------|
| H1 | **Confirmed and closed** | Exact 131-unit common locale manifest, digest/diff approval, qualified-review record, and fail-all gate are sufficient. Actual translations and approvals are Phase A inputs, not research output. |
| H2 | **Supported within controllable scope** | Metadata, public JSON, stable routes, and crawl eligibility are testable signals. Rank, indexing, and AI inclusion remain timestamped non-guaranteed observations. |
| H3 | **Confirmed for the current snapshot** | Exact category-plus-exception membership and the 62-row audit provide a compact intent layer; future semantics require reviewed source changes. |
| H4 | **Confirmed with a Phase B access gate** | One generator can be verified across GitHub and Pages using explicit anchors and layered evidence. Actual Pages-source/settings evidence remains owner-controlled. |

### C9: Challenge-stage decisions

| # | Decision | Reason |
|---|----------|--------|
| CD1 | Select C1 and add an immutable `previous_approved_ref`, `previous_approved_digest`, and computed `changed_keys[]` to each approval record. | It makes the review diff reproducible and binds re-review to the exact change without per-field state or unbounded manual prose. |
| CD2 | Treat complete qualified EN/RU/KK payloads as a Phase A entry gate, not something the generator may synthesize or certify. | This is the only fail-closed interpretation that does not invent Kazakh or permit fallback. |
| CD3 | Keep the exact Gather/Extract intent configuration, including `nu_acm_w` in Engineering and no runtime exclusions. | The entry audit supports the semantic boundary, and compact category destinations prevent duplicated catalogs. |
| CD4 | Preserve A1–A7 and P1–P8, with numeric first-screen assertions and anchor-pair parity. | The layers are complementary and jointly cover every frozen cross-render/metadata requirement. |
| CD5 | Resolve owner-controlled evidence through the five typed gates in C7 and recommend no further research iteration. | Every remaining unknown is now an input, permission, deployment fact, or non-guaranteed observation—not an architecture gap. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 survives localization churn when review records include prior digest and exact changed keys. | Actual qualified EN/RU/KK payloads and attestations must be supplied before Phase A. |
| The exact intent matrix survives false-positive, false-negative, duplication, and future-entry attacks. | Owner ratification in the later TS is normal approval, not a research gap. |
| Explicit anchors and layered A/P evidence cover GitHub, Jekyll, public metadata, target parity, and bounded first screen. | Authenticated Pages source and settings values remain Phase B owner gates. |
| Search Console and retrieval behavior have explicit non-design dispositions. | Search Console access may be `N/A`/`DEFERRED`; rank and AI inclusion remain observations only. |

**Sufficiency:**
- [x] External source used? GitHub Pages/source and anchor documentation, Google URL Inspection, and OpenAI crawler documentation.
- [x] Briefing gap closed? All four Iteration 2 questions now have executable contracts and failure dispositions.
- [x] Pairwise incompatibility checked? Six survivors were attacked; only C1 remains selected.
- [x] At least one focused-stage decision made? CD1–CD5 finalize the contract without reopening architecture.

Stage complete: YES
→ User decision: Synthesize Iteration 2 RES under the Coordinator's focused-mode authorization.

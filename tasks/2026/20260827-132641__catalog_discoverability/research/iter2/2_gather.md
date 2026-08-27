# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-20260827-132641__catalog_discoverability](../../HL-20260827-132641__catalog_discoverability.md)
> Predecessor: [Iteration 1 RES](../iter1/RES.md)
> Goal: Make one verified Kazakhstan IT Telegram catalog easy to discover, understand, and use in English, Russian, and Kazakh without creating drifting catalogs or weakening accuracy.

## Dimensions

The route/site architecture is fixed by Iteration 1. These dimensions cover only the remaining closure contracts.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Review-to-content binding | One approval per locale bound to a canonical payload digest | Per-field reviewer/status metadata | Out-of-band checklist not bound to content | Presence alone treated as approval |
| D2: Incomplete locale behavior | Fail the whole multilingual generation/check gate | Omit only the incomplete language route | Publish explicit “translation incomplete” status | Fall back silently to English |
| D3: Intent rule representation | Category selectors plus exceptional includes; no runtime exclusions unless a selected category needs an override | Categories plus include/exclude handle lists | Full handle enumeration for every intent | Keyword/description inference |
| D4: Render evidence layer | Source and generated-text assertions only | GitHub rendered-Markdown API plus local Jekyll output | Post-deployment browser DOM only | Layered source, GitHub-render, Pages-render, and public-response evidence |
| D5: External dependency disposition | Required authenticated precondition | Conditional owner-access evidence | Timestamped non-blocking observation | Positive rank/inclusion release gate |
| D6: Stable destination ownership | Explicit generator-owned IDs from type/category/intent/handle keys | Renderer-generated heading slugs | Display-text-derived custom slugs | Numeric or positional anchors |

No alternative is selected in Gather. Extract will combine the viable forms and Challenge will remove those that cannot satisfy the frozen accuracy and evidence contract.

## Findings

### G1: The data-backed localization inventory is exactly 92 semantic units per locale

The 2026-08-27 catalog snapshot contains these localizable semantic units:

| Family | Exact units | EN current | RU current | KK current | Rule |
|--------|-------------|------------|------------|------------|------|
| Catalog identity/summary | `meta.title`, `meta.description` — 2 | 2 | 0 | 0 | One approved value per locale; the description may be reused as the first-screen promise and Dataset description rather than copied. |
| Project North Star | `purpose` + four `non_goals` — 5 | 5 | 0 | 0 | Meaning-preserving translations; the non-goal order and count remain identical. |
| Category labels | 19 category IDs — 19 | 19 | 0 | 0 | IDs remain invariant; every locale supplies an explicit display value, even when a technical term is intentionally unchanged. |
| Live entry descriptions | 38 groups + 20 channels + 4 bots — 62 | 62 | 62 | 0 | Name/handle remain identity; description conveys localized meaning. Presence is not proof that existing Russian wording was qualified-reviewed. |
| Archive descriptions | 2 archived records — 2 | 2 | 2 | 0 | Archive facts remain visible without fallback. |
| Archive reasons | 2 archived records — 2 | 2 | 0 | 0 | Evidence meaning and dates must be preserved; dates themselves are invariant. |
| **Total** | **92 per locale** | **92/92 present** | **64/92 present** | **0/92 present** | Coverage counts only presence, not approval. |

The following are invariant catalog facts and are not translation units: 64 live/archive names, 64 handles and Telegram URLs, category IDs, intent IDs, member counts, ISO dates, repository/data URLs, code/file names, and brand tokens such as Awesome/CC0. An invariant proper name that looks English or Russian on another-language page is not a fallback; changing it would change community identity. W3C guidance still requires the page default on `<html lang>` and recommends marking genuinely foreign-language parts when reliable part-language data exists; the route default does not certify the strings' meaning.

Source: [`data/communities.json`](../../../../../data/communities.json); <https://www.w3.org/International/questions/qa-html-language-declarations>.

### G2: The common UI registry can be finite and non-duplicative

The selected renderer needs an explicit shared registry of **39** localizable UI keys. Values may intentionally be equal across languages, but a missing key cannot borrow another locale's value.

```text
nav.languages                 nav.types                     nav.intents
stats.groups                  stats.channels                stats.bots
stats.categories              stats.verified
section.contents              section.purpose               section.groups
section.channels              section.bots                  section.archive
section.contributing          section.data                  section.license
north_star.non_goals_intro    bots.intro                    archive.summary
archive.column.type           archive.column.community      archive.column.description
archive.column.member_count   archive.column.last_verified  archive.column.died_on
archive.column.reason         type.group                    type.channel
type.bot                      contributing.prompt           data.download_label
generated.notice              license.waiver
intent.ai                     intent.startups                intent.jobs
intent.events                 intent.engineering
```

The common route payload is therefore **131 reviewed localizable units per locale**: 92 data-backed semantic units plus 39 UI units. Metadata and visible content reuse these units:

- page and Dataset `name` reuse the locale catalog title;
- meta/Dataset description and the visible concise promise reuse the locale catalog summary;
- social title/description reuse the same title/summary;
- intent labels reuse the five UI values;
- totals and dates are derived facts inserted beside localized labels.

The English GitHub README may retain an English-only repository-process appendix. If it does, its finite keys are separate: `section.project_workflow`, `workflow.intro`, and label/description pairs for task portfolio, KNOWLEDGE, and AGENTS (8 units). If any of those strings are emitted on RU or KK Pages, they automatically join the 131-unit common manifest and require review; implementation cannot create an untracked hard-coded exception.

Source: [`scripts/generate_readme.py`](../../../../../scripts/generate_readme.py); current generated [`README.md`](../../../../../README.md).

### G3: Qualified review must be content-bound and fail closed

“Qualified” cannot be inferred from a language field or from AI fluency. A defensible review record needs all of:

| Field | Acceptance meaning |
|-------|--------------------|
| Locale | Exactly `en`, `ru`, or `kk`; route label `KZ` does not change Kazakh's code. |
| Reviewer | Owner-designated human identity; an AI system/provider cannot approve its own output. |
| Qualification basis | Recorded fluency/native competence for the locale plus ability to judge Kazakhstan IT/Telegram terminology and preservation of community meaning. The same person may cover multiple locales only when the owner explicitly attests both qualifications. |
| Scope | The exact 131-unit locale payload; English additionally covers any retained 8-unit README-only appendix. |
| Digest | SHA-256 of a canonical, key-sorted UTF-8 serialization of the reviewed key/value map, excluding invariant catalog facts. |
| Verdict/date | `APPROVED` or `REVISE`, ISO date, and no unresolved exceptions for approval. |

The semantic baseline is approved English content. Russian and Kazakh review compare each localized value with the English meaning and the invariant target identity; the existing 64 Russian descriptions are input coverage, not inherited certification. Candidate translations may be produced by any workflow, but generation/publication remains closed until a qualified human approves the exact digest.

Fail-closed cases are: missing key, null/blank value, placeholder, wrong value type, locale set other than exactly EN/RU/KK, unregistered hard-coded visible text, silent fallback, reviewer without recorded qualification, non-APPROVED verdict, or digest mismatch after any string change. A failure blocks all multilingual generated outputs rather than publishing an asymmetrical catalog. Automated checks prove coverage and binding; they never claim to detect language correctness.

### G4: Exact five-intent definitions can be expressed without runtime exclusions

The semantics used for the entry-by-entry review are deliberately narrow:

| Intent | Inclusion semantics | Selected category IDs | Exceptional live handles | Reviewed high-risk exclusions |
|--------|---------------------|-----------------------|--------------------------|-------------------------------|
| AI | Primary subject is AI, ML, data science, or an AI developer tool/community; a generic BI/data topic is insufficient. | `ai` | `ml_jobs_kz`, `dsmlkz_news` | `kz_bi`, `dwhkz`, `datanomika` — analytics/data engineering without explicit AI/ML focus. |
| Startups | Primary recurring subject is Kazakhstan startups, founders, venture/entrepreneurship, or startup ecosystem news/discussion. | `startups` | `thetechkzchat`, `thetechkz`, `saubakirov` | `projects_kz` is generic project management; `itbazarkz` is a marketplace, not startup discovery. |
| Jobs | Primary function is IT vacancies, freelance work, or role-specific job postings. | `jobs` | None | `nu_acm_w` includes career opportunities but is not a job-posting source. |
| Events | Primary function is announcing Kazakhstan-relevant IT events/meetups/conferences. | `events` | None | `cleverskz` and `nu_acm_w` may surface programs/activities but are not primarily IT-event announcement feeds. |
| Engineering | Primary value is technical practice, practitioner community, technical learning, a technical discipline, engineering leadership, or a directly useful developer utility. Jobs-only, generic tech/startup news, marketplace, generic project management, public-service bots, and general event feeds are excluded. | `ai`, `blockchain`, `data-analytics`, `devops-sysadmin`, `gamedev`, `hardware`, `mobile`, `programming-languages`, `qa-testing`, `security`, `web-development` | `devkz`, `illuminatinc`, `teamleads_kz`, `datanomika`, `DevSkills`, `nu_acm_w`, `sysadm_in_up`, `saubakirov`, `cleverskz`, `Get_Telegram_ID_bot` | Full reviewed exclusion set: `itbazarkz`, `itmankz`, `thetechkzchat`, `projects_kz`, `kzquake`, `mobilejobskz`, `devkz_jobs`, `ml_jobs_kz`, `thetechkz`, `bluescreenkz`, `workitkz`, `kz_it_events`, `devsecopskz_jobs`, `KazPostBot`, `ShtrafKZBot`, `chat_prettier_bot`. |

No selected category contains a current member that needs subtractive override, so runtime `exclude_handles` would be redundant. The audit exclusions document semantic boundaries; the rendered set is `members whose validated category is selected` union `exceptional live handles`. The unused `startups` and `blockchain` category IDs still express future classification behavior and are valid current category definitions.

### G5: Every current entry was classified against all five intents

Codes: `AI`, `SU` (startups), `JB` (jobs), `EV` (events), `EN` (engineering). `—` means reviewed and excluded from all five, not overlooked.

| Type | Handle | Category | Membership | Basis / caveat |
|------|--------|----------|------------|----------------|
| Group | `kz_bi` | `data-analytics` | EN | BI is a technical/data discipline; no explicit AI/ML focus. |
| Group | `cyberseckz` | `security` | EN | Security practitioner discussion. |
| Group | `frontendkz` | `web-development` | EN | Frontend practitioner community. |
| Group | `thetechkzchat` | `general` | SU | Explicit startup/IT news discussion; not primarily engineering practice. |
| Group | `cursor_kz` | `ai` | AI, EN | AI coding community and technical tool practice. |
| Group | `automation_kz` | `devops-sysadmin` | EN | Industrial automation/process engineering. |
| Group | `python_kz` | `programming-languages` | EN | Programming practitioner community. |
| Group | `sysadm_in` | `devops-sysadmin` | EN | System administration community. |
| Group | `itbazarkz` | `marketplace` | — | Equipment marketplace, not a selected intent. |
| Group | `itmankz` | `jobs` | JB | Freelance IT work; jobs-only is excluded from engineering. |
| Group | `backenderskz` | `web-development` | EN | Backend practitioner community. |
| Group | `astanajug` | `programming-languages` | EN | Java practitioner community. |
| Group | `iOSDevelopers_KZ` | `mobile` | EN | Mobile engineering community. |
| Group | `devkz` | `general` | EN | Explicit general programmers community; engineering exception. |
| Group | `gamedevkz` | `gamedev` | EN | Game development discipline. |
| Group | `go_kz` | `programming-languages` | EN | Programming practitioner community. |
| Group | `phpdevconf` | `programming-languages` | EN | Programming practitioner community. |
| Group | `rubyata` | `programming-languages` | EN | Programming practitioner community. |
| Group | `kz_1C` | `programming-languages` | EN | 1C platform development discussion. |
| Group | `dart_kz` | `mobile` | EN | Flutter/Dart engineering community. |
| Group | `dotnetgroup` | `programming-languages` | EN | Programming practitioner community. |
| Group | `devnullkz` | `devops-sysadmin` | EN | Administrator peer chat. |
| Group | `MikroTikKZ` | `devops-sysadmin` | EN | Network engineering equipment discussion. |
| Group | `radiotechkz` | `hardware` | EN | Electronics/radio engineering. |
| Group | `r0crewKZ` | `security` | EN | Security research community. |
| Group | `sipvoipkz` | `devops-sysadmin` | EN | VoIP/network systems discussion. |
| Group | `diykz` | `hardware` | EN | Maker/hardware practice. |
| Group | `kzlug` | `devops-sysadmin` | EN | Linux practitioner community. |
| Group | `cctvkz` | `hardware` | EN | Video-surveillance systems practice. |
| Group | `cppkz` | `programming-languages` | EN | Programming practitioner community. |
| Group | `rustlang_kz` | `programming-languages` | EN | Programming practitioner community. |
| Group | `rubykz` | `programming-languages` | EN | Programming practitioner community. |
| Group | `dwhkz` | `data-analytics` | EN | DWH/Big Data engineering; not explicitly AI/ML. |
| Group | `AQA_kz` | `qa-testing` | EN | QA automation engineering. |
| Group | `illuminatinc` | `general` | EN | Explicit IT knowledge-sharing community; engineering exception. |
| Group | `teamleads_kz` | `management` | EN | Explicit engineering leadership; category is not selected because `projects_kz` is generic. |
| Group | `projects_kz` | `management` | — | Generic project management is not explicitly engineering/startup. |
| Group | `devsecopskz` | `devops-sysadmin` | EN | DevSecOps/security automation practice. |
| Channel | `datanomika` | none | EN | BI/data visualization technical content; explicit exception because category is absent. |
| Channel | `kzquake` | none | — | Earthquake monitoring, not one of the five intents. |
| Channel | `mobilejobskz` | `jobs` | JB | Mobile job feed; not engineering-practice content. |
| Channel | `devkz_jobs` | `jobs` | JB | Developer job feed. |
| Channel | `DevSkills` | `education` | EN | Explicit technical learning resources. |
| Channel | `ml_jobs_kz` | `jobs` | AI, JB | ML/DS subject plus job-feed function; excluded from engineering-practice route. |
| Channel | `certkznews` | `security` | EN | Discipline-specific cybersecurity news. |
| Channel | `thetechkz` | `news` | SU | Explicit IT/startup news; not engineering-practice content. |
| Channel | `nu_acm_w` | `education` | EN | Women-in-Computing community with explicit CS education/career value; engineering exception, but not a vacancy feed. |
| Channel | `bluescreenkz` | `news` | — | Broad tech/games/security news, not a selected narrow intent. |
| Channel | `workitkz` | `jobs` | JB | General IT job feed. |
| Channel | `kz_it_events` | `events` | EV | Explicit IT-event announcements. |
| Channel | `sysadm_in_channel` | `security` | EN | Discipline-specific InfoSec news/articles. |
| Channel | `sysadm_in_up` | `education` | EN | Explicit technical-learning articles. |
| Channel | `saubakirov` | `education` | SU, EN | Description explicitly names tech, startups, and engineering. |
| Channel | `dsmlkz_news` | `data-analytics` | AI, EN | Explicit Data Science/ML and technical-discipline content. |
| Channel | `cloudreadykz` | `devops-sysadmin` | EN | Cloud/infrastructure discipline. |
| Channel | `cloudnativekz` | `devops-sysadmin` | EN | Kubernetes/container discipline. |
| Channel | `devsecopskz_jobs` | `jobs` | JB | DevOps/DevSecOps job feed; jobs-only. |
| Channel | `cleverskz` | `education` | EN | Competitive programming/math technical learning; not primarily an events feed. |
| Bot | `KazPostBot` | none | — | Public-service utility, not practitioner engineering content. |
| Bot | `ShtrafKZBot` | none | — | Public-service utility, not practitioner engineering content. |
| Bot | `Get_Telegram_ID_bot` | none | EN | Directly useful Telegram developer/admin utility. |
| Bot | `chat_prettier_bot` | none | — | Community-moderation utility, not explicitly developer/engineering-focused. |

Set validation against the current JSON produced: AI **3**, startups **3**, jobs **6**, events **1**, engineering **46**; 55 unique live handles appear in at least one intent and 7 appear in none. All declared handles exist, and all 62 live handles are accounted for exactly once in this audit table. These are dated research snapshot counts, not documentation constants; the generator must derive future membership.

### G6: Current cross-render behavior proves the evidence layers are non-substitutable

Observed 2026-08-27:

| Surface | H1 scope | Telegram target-set result | Route/metadata result |
|---------|----------|----------------------------|-----------------------|
| GitHub rendered README article | Exactly one article `h1` (`Awesome Kazakhstan IT Telegram`) | 64/64 live+archive targets present, including `kzquake` and two archive links | GitHub owns the outer document language/metadata; article parity is the relevant contract. |
| GitHub rendered-Markdown REST representation of `README.md?ref=master` | Exactly one `h1` | 64 target anchors; public endpoint supports commit/ref-addressable rendered HTML | Useful deterministic pre/post merge assertion, but not viewport evidence. |
| GitHub Pages `/` | Two `h1` values (theme slug + catalog title) | 61/64 target anchors; missing `kzquake`, `mobile_developers_kz`, `kzqacommunity` | `lang=en-US`; current root 200; identity/target parity fail. |
| Pages `/ru/`, `/kk/`, `/sitemap.xml` | N/A | N/A | Each currently 404. |
| Pages `/data/communities.json` | N/A | Canonical data responds 200 | `application/json; charset=utf-8`; current public JSON contains the expected 62 live + 2 archive records. |

The raw Pages HTML still contains the three missing `https://t.me/` strings, but they are not anchors: the live pipe-name is parsed into table structure, and Markdown links inside the raw archive table do not survive as anchors. This strengthens D8: substring checks and HTML validity both produce false confidence. Evidence must compare rendered anchor target sets and anchor text/URL pairs with source records.

GitHub's official contents API documents an HTML media type rendered through GitHub Markup and accepts a `ref`; this supplies a commit-addressable GitHub-render check. Browser evidence remains necessary for actual GitHub/Pages layout and bounded viewport assertions.

Sources: live GitHub repository and Pages DOMs; GitHub REST <https://docs.github.com/en/rest/repos/contents#get-repository-content>.

### G7: Official metadata rules translate into exact assertions, not outcome promises

- W3C requires the default page language on the `html` element; the acceptance values are exactly `en`, `ru`, and `kk` for the three Pages routes.
- Google requires every language version to list itself and every peer with fully qualified reciprocal links. One HTML-head method is sufficient; duplicating the mechanism in a localized sitemap offers no search benefit and increases consistency cost. Therefore each page can assert the same exact three-link set in `<head>` while the ordinary sitemap asserts route discovery.
- Google Dataset eligibility requires `Dataset.name` and a 50–5000-character `Dataset.description`; `DataDownload.contentUrl` is required when a distribution is declared, and `encodingFormat` is recommended. This is executable as one Dataset node per route whose name/description reuse reviewed visible values and whose distribution points to the public JSON with `application/json`.
- Google explicitly describes sitemap submission as a hint and structured-data release as add/validate/deploy/inspect. A valid sitemap or Dataset node is a configuration/access result, never rank or inclusion evidence.

Sources: <https://developers.google.com/search/docs/specialty/international/localized-versions>; <https://developers.google.com/search/docs/appearance/structured-data/dataset>; <https://www.w3.org/International/questions/qa-html-language-declarations>.

### G8: External dependencies have four distinct dispositions

| Dependency/outcome | Disposition | Failure meaning |
|--------------------|-------------|-----------------|
| Authenticated Pages publishing source | Required owner-access precondition before Phase B publication/settings work | If unavailable, Phase B deployment evidence is DEFERRED; it does not reopen `/`, `/ru/`, `/kk/` or justify a `docs/` redesign. |
| Repository description, homepage, topics, social preview | Owner-authorized mutation gate with before/approved/after evidence | No mutation without exact owner approval; absence blocks only that external-settings acceptance item. |
| Search Console | Conditional optional-access evidence | If access is supplied, inspect/record URL and sitemap status. If not supplied, record the limitation; publication remains judgeable through public access evidence. |
| Search rank, recrawl timing, AI inclusion/citation | Timestamped non-blocking observation | Positive or negative retrieval is recorded with query/date/locale/surface; neither is a release pass/fail result. Any guaranteed/VERIFIED outcome claim fails DoF 5. |

This closes the design uncertainty: none of these items chooses renderer, route, data schema, or intent behavior. They are Phase B preconditions, conditional evidence, or observations.

### G9: Gather-stage decision

**GD1 — Carry content-digest-bound qualified review, category-plus-exception intents, explicit stable IDs, layered render evidence, and typed external dispositions into Extract.** These forms make every remaining gap executable without changing Iteration 1's architecture; presence-only review, keyword inference, and single-layer render tests cannot satisfy the frozen failure conditions.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Exact 92-unit semantic payload and 39-key UI registry produce a finite 131-unit per-locale review scope. | Combine review record, missing-value behavior, and output manifests into one acceptance contract. |
| All 62 live entries have exact five-intent dispositions; compact category/exception definitions yield 3/3/6/1/46 current members. | Convert the audit into stable internal destinations and invariants that remain correct when data changes. |
| GitHub renders 64/64 target anchors while Pages renders 61/64 despite containing all URL strings. | Specify layered source/API/DOM/viewport assertions with exact expected sets and failure ownership. |
| Authenticated settings, optional Search Console, and variable retrieval have typed boundaries. | Challenge whether any boundary still leaves a TS design choice or an impossible acceptance claim. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one focused-stage decision made? GD1 selects the closure forms to combine without selecting implementation code.

Stage complete: YES
→ User decision: Continue to Extract under the Coordinator's focused-mode authorization.

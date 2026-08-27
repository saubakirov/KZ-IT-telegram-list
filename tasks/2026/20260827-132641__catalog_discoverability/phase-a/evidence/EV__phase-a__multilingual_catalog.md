# EV — 20260827-132641__catalog_discoverability / Phase A: Multilingual Catalog

> **Date**: 2026-08-27
> **Author**: Codex (Executor)
> **Task**: 20260827-132641__catalog_discoverability
> **TS**: [Phase A TS](../TS__phase-a__multilingual_catalog.md)
> **Approved base**: `a646f59794fdb639a8e0471838b33727bd4ac31c`
> **Revision trigger**: formal `REVISE` in original Reviewer commit `2cd3977c0e795e4803c78993919ee1630430c4c7`, cherry-picked locally as `0f0536c40d92a9d8ad48782a2b4184b12da2e18b`

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows NT 10.0 build 26200.8655; registry product Windows 10 Pro 25H2 |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1; standard library only |
| Deploy target | Final local candidate; no deployment or publication |
| CI / Pipeline | Local PowerShell; public GitHub Markdown renderer (read-only); Antigravity CLI advisory |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Complete explicit EN/RU/KK values, 39-key Russian revision, exact intent definitions, refreshed digest binding, and zero approved-base fact changes | Local Python | N/A | Commands below; `data/communities.json` |
| E2 | AC-2 | One renderer produced four current projections with identical 64-record identity/target sets | Local Python | N/A | Currency/test output below |
| E3 | AC-3 | One H1, concise catalog-first navigation, five researched intents, stable destinations, and no duplicated catalog rows | Local Python | N/A | `scripts/test_catalog_generation.py` |
| E4 | AC-4 | Exact README bytes rendered through GitHub; all 64 visible-name/Telegram pairs and 71 fragment links survived | `api.github.com/markdown/raw` | VERIFIED | GitHub record below |
| E5 | AC-5 | Twelve positive/negative regression tests, schema validation, non-mutating check mode, and portable escaping passed | Local Python | N/A | Deterministic gates below |
| E6 | AC-6 | Revised complete EN/RU/KK renders received a fresh digest-bound Gemini 3.7 Flash High `PASS` after every formal Reviewer finding was dispositioned | Antigravity `agy` plan+sandbox | VERIFIED | Review record below |
| E7 | AC-7 | Architecture stayed unchanged; revision touched source/RU projection plus EV/RF only, facts remained invariant, and no Phase B/external mutation occurred | Git diff/local audit | N/A | Scope record below |

## Verdict

Evidence verdict: 2/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 5 N/A

Formal Phase A acceptance is intentionally pending the same Reviewer's refreshed `/tfw-review`; Antigravity is advisory only. The prior `REVISE` remains immutable evidence for the superseded digest.

## Deterministic gates

Final unchanged-candidate commands:

```text
python scripts/test_catalog_generation.py       -> Ran 12 tests; OK
python scripts/validate_schema.py               -> Errors: 0; Schema is valid
python scripts/generate_readme.py --check       -> All 4 catalog projections are generator-current
git diff --check                                -> no output
```

Schema totals: 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries; 62 live and 64 total records. Locale payload keys: EN 139, RU 131, KK 131, total 401; refreshed SHA-256 `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc`. Intent membership fixture: AI 3, Startups 3, Jobs 6, Events 1, Engineering 46; union 55.

Approved-base invariant comparison covered `name`, `handle`, `category`, `member_count`, `last_verified`, `type`, `died_on`, and canonical English archive `reason` across groups/channels/bots/archive: cardinalities `38/20/4/2`; `invariant_fact_diff_count=0`.

## GitHub renderer record

Read-only invocation: HTTP `POST https://api.github.com/markdown/raw`, exact `README.md` bytes, `Accept: text/html`, no repository mutation.

```text
HTTP 200; content-type=text/html;charset=utf-8
README: 16,627 bytes; sha256=3b1d70624d7f529c6e7f712574783d468afe5025d6c1bc0173466dd80d5c016d
HTML: 31,600 bytes; sha256=6f319f459156068831d8407775488f2d802f5193b02245c3ded72918de41f887
H1=1; Telegram pairs expected/rendered/missing/extra=64/64/0/0
IDs=124; fragment links=71; unresolved=0; duplicate normalized IDs=0
kzquake/mobile_developers_kz/kzqacommunity anchors=1/1/1
```

GitHub prefixes explicit IDs with `user-content-`; the check removed only that documented sanitizer prefix before fragment comparison.

## Digest-bound review package

- Canonicalization: NFC-normalized, key-sorted, compact UTF-8 JSON; revised SHA-256 `51db402da00f85f25dd533d415c9d7941402c69b5892952882bafc6122d2a6fc` (supersedes rejected candidate `80ee30ba87003b61de862d63f0a01cea213d5bc08320019af6b4e513fbb33fd0`).
- Prior approved reference/digest: none; `REVISE` is not approval, so the exact approval-candidate changed-key set remains all 401 keys.
- Exact sorted changed keys: [review_changed_keys.json](review_changed_keys.json), recomputed byte-identical at 401/401 keys; file SHA-256 `c842b6bdf35e44ea7551e5ebf171e9027cc8cec8c5e96c379a3d7cc9e889011b`.
- Exact revision delta from the reviewed payload: 39 Russian keys — archive `kzqacommunity`; bots `Get_Telegram_ID_bot`, `KazPostBot`, `ShtrafKZBot`, `chat_prettier_bot`; channels `DevSkills`, `bluescreenkz`, `certkznews`, `cleverskz`, `datanomika`, `devsecopskz_jobs`, `dsmlkz_news`, `ml_jobs_kz`, `nu_acm_w`, `sysadm_in_channel`, `sysadm_in_up`, `workitkz`; groups `AQA_kz`, `MikroTikKZ`, `astanajug`, `automation_kz`, `cppkz`, `devnullkz`, `devsecopskz`, `diykz`, `dwhkz`, `frontendkz`, `gamedevkz`, `itbazarkz`, `itmankz`, `kz_bi`, `phpdevconf`, `python_kz`, `rubyata`, `rubykz`, `sysadm_in`, `teamleads_kz`; UI `license.waiver`, `stats.bots`.
- Final renders: EN `index.md` `2f7f5cc18ff8fd4f776fa4d266da363d358965509337cff83b1a4c38082598c6`; RU `ru/index.md` `82cf475bacc68aaf57404ebf3becd54ada9f94b9702625dd789e39f49e062756`; KK `kk/index.md` `5f7353e9707f3ac1a26656834584be38717ff816bc57c733776f9c980a1d6510`.
- `README.md` is the generated English GitHub mirror; its final SHA-256 is recorded in the renderer section.

CLI discovery confirmed `agy.exe --help` exposes `--print`, `--model`, `--mode`, `--sandbox`, `--input-format`, `--output-format`, and `--print-timeout`; `agy.exe models` exposed exact model `gemini-3.7-flash-high` (`Gemini 3.7 Flash (High)`), so no fallback was used.

Exact successful invocation shape (the NDJSON message contained the complete final EN/RU/KK renders and digest/hash header):

```powershell
$message | & 'C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe' --model 'gemini-3.7-flash-high' --mode plan --sandbox --input-format stream-json --output-format stream-json --print-timeout 15m
```

Final prompt SHA-256: `c65010699557f925a023f1e33f5a2ef7b8fc5ac63c192b00477ae913dd9abd67`; conversation `c77d8362-ff79-4904-af69-b89265590c4c`; status `SUCCESS`; exact payload digest echoed.

Advisory result: `PASS`; `DISPOSITION_REQUIRED: NO`; complete EN/RU/KK projections reviewed; `FINDINGS: NONE`. Conclusions: semantic fidelity, standard terminology, concise neutral tone, correct grammar/punctuation, and no keyword stuffing. No post-advisory wording change occurred.

### Formal Reviewer findings and dispositions

| Finding | Disposition in source revision `99bbf5cc47060a076ed4363728dca6fe78bc68fd` |
|---------|-------------|
| `ui.ru.stats.bots`: `ботов` | Changed to count-correct `бота`. |
| `certkznews`: split `кибер атак` | Changed to `Новости ЦАРКА (Центра анализа и расследования кибератак)`. |
| `bluescreenkz`: promotional credo and incomplete scope | Replaced with `Новости технологий, игр и кибербезопасности простым языком`. |
| `dwhkz`: mixed-language, incomplete scope | Replaced with `Обсуждение хранилищ данных и Big Data`. |
| `teamleads_kz`: slogan instead of scope | Replaced with `Сообщество тимлидов и инженерных менеджеров`. |
| `ml_jobs_kz`: ungrammatical/promotional and not jobs-only | Replaced with `Вакансии в области ML и Data Science`. |
| `automation_kz`: audience/mission narrowing | Replaced with `Промышленная автоматизация и инженерия технологических процессов`. |
| Compound specialist/job/article terms | Normalized relevant forms including `BI-аналитиков`, `фронтенд-разработчиков`, `Java-разработчиков`, `PHP-разработчиков`, `Ruby-разработчиков`, `QA-специалистов`, `IT-специалистов`, `IT-вакансии`, and `IT-статьи`. |
| Ruby on Rails casing/terminology | Changed `Коммюнити Ruby и Ruby On Rails` to `Сообщество Ruby и Ruby on Rails`. |
| Slash punctuation in fines/taxes/penalties | Changed to `Проверка задолженностей и уведомления о штрафах, налогах и пенях`. |
| Slang/promotional catalog voice | Neutralized `питонистов`, `сисадминов`, `барахолка`, `Самоделкины`, `ИТ полезности`, and related slogan-like wording while retaining topic meaning. |
| Advisory suggestion to replace `1C` with a Cyrillic confusable | Rejected as directed; the reviewed `kz_1C` identity/name/Russian source token was left byte-identical. |
| Advisory suggestion treating Markdown escape backslashes as visible | Rejected as directed; generator/escaping code and rendered output were not changed. |

## Scope and mutation record

The approved implementation remains exactly eight paths, 4 new/4 modified, with 2,722 insertion-plus-deletion LOC against the 3,000 cap. This revision changed only `data/communities.json`, regenerated `ru/index.md`, this EV, and RF; all four outputs were regenerated, while README/EN/KK remained byte-identical. The four cherry-picked Reviewer files are immutable and have zero worktree diff. No HL, TS, RES, REVIEW, ONB, status, journal, task index, Phase B, deployment, settings, tag, push, release, or publication path was modified by the revision. External mutation count: zero; GitHub and Antigravity calls were read-only/advisory.

---

*EV — 20260827-132641__catalog_discoverability / Phase A: Multilingual Catalog | 2026-08-27*

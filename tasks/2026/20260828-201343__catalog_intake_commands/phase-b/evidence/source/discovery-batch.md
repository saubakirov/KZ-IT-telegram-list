# Кандидаты на проверку и добавление — сбор 2026-08-28

> **Статус:** discovery-исследование, вход для будущей задачи через `/tfw-plan`. Ничего из этого
> файла в `data/communities.json` не внесено. Каждый хэндл ниже проверен сетевым запросом к
> `t.me` 2026-08-28 по логике `scripts/validate_links.py` (тип, размер, привязка идентичности);
> для каналов дата последнего поста прочитана из `t.me/s/<handle>`. Для групп даты нет — только
> «превью отвечает» и размер, поэтому группы проверены слабее каналов.
>
> **Метод и охват:** 118 хэндлов, три волны поиска (веб-источники → упоминания в превью найденных
> каналов → упоминания в превью 57 записей самого каталога) плюс список сети unwar.kz от владельца.
> 12 из 23 принятых найдены не в вебе, а в описаниях и лентах уже включённых каналов.
> Решения владельца по спорным записям приняты 2026-08-28 и учтены ниже.

## 1. К добавлению — 23

Критерии: публичное превью отвечает и совпадает с хэндлом; тема IT; привязка к Казахстану из
названия, описания или подтверждения владельца; для каналов — пост не старше двух недель
(одно отмеченное исключение). Категория — предложение для `/tfw-plan`, не решение.

### Закрывают пустые и тонкие категории

| handle | название | тип | размер | последний пост | категория | заметка |
|---|---|---|---:|---|---|---|
| `astana_hub` | Astana Hub | channel | 13 570 | 2026-08-28 | `startups` | официальный канал технопарка; категория сейчас **пустая** |
| `blockchainkz` | BlockchainKZ Association | channel | 286 | 2026-07-13 | `blockchain` | ассоциация с 2018; категория **пустая**; 6 недель тишины — единственное исключение из правила двух недель |
| `itbazarkzchannel` | IT Барахолка — только объявления | channel | 2 448 | 2026-08-28 | `marketplace` | канал-сателлит уже включённого `itbazarkz`; категория из одной записи |
| `qaz_qa_vacancies` | KZ QA Vacancies | group | 604 | — | `qa-testing` | найдено в описании `aqa_kz`; QA — одна запись |
| `hackathon_kz` | Hackathon kz | channel | 252 | 2026-08-27 | `events` | канал агрегатора hackathon.kz |
| `kz_bi_news` | KZ BI News & Events | channel | 959 | 2026-08-26 | `data-analytics` | сателлит `kz_bi` |
| `nfactorial_school` | nFactorial School | channel | 435 | 2026-08-25 | `education` | организатор nFactorial Incubator (§4); **не** `nfactorialschool` — это бот |

### Сообщества и медиа

| handle | название | тип | размер | последний пост | категория | заметка |
|---|---|---|---:|---|---|---|
| `devs_kz` | Devs.kz | channel | 10 371 | 2026-08-27 | `general` | IT-карьера в КЗ, митапы Google и др.; **не путать с `devkz`** (группа, уже в каталоге) |
| `devopskaz` | KazDevOps | channel | 6 651 | 2026-08-28 | `devops-sysadmin` | ведёт core247.kz; контентный |
| `kolesa_group` | Kolesa Group | channel | 7 113 | 2026-08-28 | `general` | бренд-канал компании: опыт, стажировки, Kolesa Conf. **Решение владельца: добавляем** |
| `allkzit` | IT.kz — все айтишники Казахстана | group | 3 012 | — | `general` | форум сети unwar.kz |
| `rootway` | Путь Админа | channel | 1 215 | 2026-08-26 | `devops-sysadmin` | ссылки для саморазвития; **привязка к КЗ подтверждена владельцем** |
| `ethkz` | Сеть.kz | group | 1 226 | — | `devops-sysadmin` | сетевые инженеры КЗ, вебинары от производителей; сеть unwar.kz |
| `tvkrg` | Terricon Valley · Караганда | channel | 1 233 | 2026-08-21 | `general` | единственный живой региональный вне Алматы/Астаны; terricon.kz |
| `digitalbussinesskz` | DigitalBusiness.kz | channel | 8 364 | 2026-08-28 | `news` | **двойная «s»** — настоящий; медиа «бизнес + IT» |
| `aws_kz` | AWS User Group Kazakhstan | channel | 267 | 2026-08-26 | `devops-sysadmin` | канал анонсов; сама группа по закрытой ссылке |
| `astanajkugoutputstream` | Astana JKUG OutputStream | channel | 724 | 2026-08-15 | `programming-languages` | канал уже включённого `astanajug` |
| `helpfixit` | Computer help | group | 317 | — | `general` | помощь новичкам; сеть unwar.kz |
| `anykeykz` | Казахстанский Эникей | group | 31 | — | `devops-sysadmin` | начинающие сисадмины; сеть unwar.kz. **Маленький (31)** — на усмотрение при добавлении |

### Вакансии — сателлиты уже включённых сообществ

| handle | название | тип | размер | последний пост | родитель |
|---|---|---|---:|---|---|
| `it_jobs_kz` | IT Jobs (DSML.KZ) | channel | 9 701 | 2026-08-26 | `ml_jobs_kz` / DSML.KZ |
| `kz_bi_jobs` | KZ BI Data Jobs | channel | 5 478 | 2026-08-27 | `kz_bi` |
| `go_kz_vacancy` | Golang vacancies in KZ | channel | 2 261 | 2026-08-18 | `go_kz` |
| `sysadm_in_job` | Sys-Admin Job | group | 830 | — | `sysadm_in` |

## 2. Отклонено — с причиной

| handle | что оказалось | вердикт |
|---|---|---|
| `aaitcomm` | бывший «Almaty IT Community» (до сих пор в списке Hexlet) — **захвачен**: китайская реклама аккаунтов, 19 подп., пост май 2025 | захвачен |
| `kazhackstan` | 7 подписчиков, пост окт. 2023 — сквоттер, не конференция | чужой |
| `digitalbusinesskz` | 1 подписчик, 2018 — стаб; настоящий `digitalbussinesskz` | стаб |
| `digitalbridgekz` | 1 подписчик, май 2024 — не канал форума | стаб |
| `kolesagroup` | группа на 18 человек — не Kolesa Group | чужой |
| `nfactorialschool` | бот; канал — `nfactorial_school` | бот |
| `fixitkz` | бот компании-аутсорсера FixIT.kz | коммерческий |
| `aistartify` | 3 подписчика | пусто |
| `we_project` | Creative Asia, 71 949 — образовательное медиа, не IT | не IT |
| `narikbi_live` | подкаст о развитии, Амстердам | личный |
| `sysadminkz` `loot_js` `askarai` `goslinuly` `zhakosha_bay` | личные аккаунты | личные |
| `workitkg` `workitru` `workituzb` | вакансии Кыргызстан / Россия / Узбекистан | не Казахстан |
| `myalmatycitychan` `myalmatycitychat` | «Алматы. Что? Где? Когда?» — городские, не IT | не IT |
| `startupchoyxona` `startup_choyxona` | Стартап-Чайхана, ЦА-широкий, узбекские корни | **решение владельца: нет** |
| `italemi` | казахоязычный IT-канал, 77 подп., пост 2026-02-19 | **решение владельца: нет** |
| `qos_it` | Костанай, 209 подп., пост 2025-11-17 | **решение владельца: нет** |

## 3. Без публичного превью — методика каталога проверить не может

Приватные группы или несуществующие имена. Четыре из них — **настоящие упоминания из живых
каналов**, стоит взглянуть вручную из клиента: `mlopskz` (MLOps KZ — назван и в `cloudreadykz`,
и в `devsecopskz`), `shymkent__hub`, `silkroad_innovation_hub`, `womenintech`.

Остальные — угаданные варианты и приватные invite-ссылки: `CoffeeCodeAlmaty`, `coffeeCodeAstana`,
`astfrontend`, `tamyrplatform`, `er10_media`, `er10kz`, `kolesateam`, `kolesa_team`, `nfactorial`,
`profitkz`, `digitalbusiness_kz`, `kazhackstan_kz`, `itjobskz`, `webjobskz`, `awscommunitycentralasia`.

## 4. Повторяемые IT-события — не меньше трёх изданий

Число изданий взято с сайтов организаторов и из прессы. Место событиям в списке упирается в
схему: `communities.json` не знает типа «событие» — это решение схемы, вне замороженной Phase D.

| событие | город | месяц | с какого года / изданий | сайт | Telegram |
|---|---|---|---|---|---|
| KazHackStan | Алматы | сентябрь | 2017 / 7-е в 2025, 2026 анонсирован | kazhackstan.com | не найден (`kazhackstan` — сквоттер) |
| Digital Bridge | Астана | октябрь | 2018 / ежегодно; 2026 → «AI & Digital Bridge» | digitalbridge.kz, digitalbridge.ai | через `astana_hub` |
| Kolesa Conf | Алматы | октябрь | 2019–2025 / 7 | kolesa-conf.kz | через `kolesa_group` |
| beetech conf (Beeline / QazCode) | Алматы | апрель–май | 6 изданий по 2026 | astanahub.com/event/beetech-conf | — |
| Google DevFest Almaty · Astana · Aqtobe | — | ноябрь | 2018 / ежегодно | gdg.community.dev | — |
| nFactorial Incubator | Алматы | лето, 10 недель | 2015 / ежегодно, Demo Day | nfactorial.school | `nfactorial_school` |
| PROFIT * Day | Астана | август | ежегодно по календарю the-tech; **число изданий не проверено** | profit.kz | — |
| Kazakhstan Technology Summit | Алматы | июнь | ежегодно по календарю the-tech; **число изданий не проверено** | — | — |

Агрегаторы событий, оба живые: `hackathon_kz` (§1) и уже включённый `kz_it_events`.

## 5. Где кандидатов не нашлось

- **gamedev, mobile, web** — ничего казахстанского сверх уже включённых `gamedevkz`, `dart_kz`, `iosdevelopers_kz`, `frontendkz`.
- **management** — казахстанского PM/CTO-сообщества не найдено; `forproducts`, ProductCamp — СНГ-широкие.
- **ai** — MLOps KZ существует (`mlopskz`), но приватный.
- **регионы** — Шымкент и Silk Road hub упомянуты, но приватны; Костанай угасает; Караганда — единственная удача.

## 6. Побочная находка: записи каталога, которые сами не прошли бы этот фильтр

Свип по 57 записям был нужен для харвеста упоминаний. Территория Phase D — здесь только зафиксировано.

| запись | размер | последний пост | тишина |
|---|---:|---|---|
| `mobilejobskz` | 276 | 2022-01-10 | 4,5 года |
| `cloudreadykz` | 161 | 2024-02-06 | 2,5 года |
| `kzquake` | 1 982 | 2024-05-29 | 2+ года — уже в G2 |
| `devskills` | 93 | 2026-02-04 | 6 месяцев |
| `devsecopskz_jobs` | 321 | — | превью есть, лента `/s/` пустая |

Остальные 52: превью отвечает, каналы постили в последние две недели.

## 7. Как проверять при добавлении

`validate_links.py --handle` работает **только для хэндлов, уже находящихся в каталоге** —
кандидата им не проверить. Порядок: внести запись в `data/communities.json` →
`python scripts/validate_schema.py` → `python scripts/validate_links.py --handle <h>` →
`python scripts/generate_readme.py`. Числа подписчиков брать только из этой проверки, не отсюда:
цифры в этом файле действительны на 2026-08-28 и только на эту дату.

Предложения по тулингу из этого исследования: `--probe <handle>` для произвольного хэндла и
`--harvest` для сбора упоминаний во время свипа — оба на существующих примитивах `validate_links.py`.

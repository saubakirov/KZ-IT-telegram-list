# EV — 20260827-132641__catalog_discoverability / Phase A: Multilingual Catalog

> **Date**: 2026-08-27
> **Author**: Codex (Executor)
> **Task**: 20260827-132641__catalog_discoverability
> **TS**: [Phase A TS](../TS__phase-a__multilingual_catalog.md)
> **Approved base**: `a646f59794fdb639a8e0471838b33727bd4ac31c`

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
| E1 | AC-1 | Complete explicit EN/RU/KK values, exact intent definitions, NFC/key-sorted digest binding, and zero approved-base fact changes | Local Python | N/A | Commands below; `data/communities.json` |
| E2 | AC-2 | One renderer produced four current projections with identical 64-record identity/target sets | Local Python | N/A | Currency/test output below |
| E3 | AC-3 | One H1, concise catalog-first navigation, five researched intents, stable destinations, and no duplicated catalog rows | Local Python | N/A | `scripts/test_catalog_generation.py` |
| E4 | AC-4 | Exact README bytes rendered through GitHub; all 64 visible-name/Telegram pairs and 71 fragment links survived | `api.github.com/markdown/raw` | VERIFIED | GitHub record below |
| E5 | AC-5 | Twelve positive/negative regression tests, schema validation, non-mutating check mode, and portable escaping passed | Local Python | N/A | Deterministic gates below |
| E6 | AC-6 | Complete final EN/RU/KK renders received an independent digest-bound Gemini 3.7 Flash High advisory pass | Antigravity `agy` plan+sandbox | VERIFIED | Review record below |
| E7 | AC-7 | Only eight implementation paths plus mandatory Executor traces changed; invariant facts preserved; no Phase B/external mutation | Git diff/local audit | N/A | Scope record below |

## Verdict

Evidence verdict: 2/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 5 N/A

Formal Phase A acceptance is intentionally pending `/tfw-review`; Antigravity is advisory only.

## Deterministic gates

Final unchanged-candidate commands:

```text
python scripts/test_catalog_generation.py       -> Ran 12 tests; OK
python scripts/validate_schema.py               -> Errors: 0; Schema is valid
python scripts/generate_readme.py --check       -> All 4 catalog projections are generator-current
git diff --check                                -> no output
```

Schema totals: 38 groups, 20 channels, 4 bots, 19 categories, 2 archive entries; 62 live and 64 total records. Locale payload keys: EN 139, RU 131, KK 131, total 401. Intent membership fixture: AI 3, Startups 3, Jobs 6, Events 1, Engineering 46; union 55.

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

- Canonicalization: NFC-normalized, key-sorted, compact UTF-8 JSON; SHA-256 `80ee30ba87003b61de862d63f0a01cea213d5bc08320019af6b4e513fbb33fd0`.
- Prior approved reference/digest: none; therefore the exact changed-key set is all 401 candidate keys.
- Exact sorted changed keys: [review_changed_keys.json](review_changed_keys.json), file SHA-256 `c842b6bdf35e44ea7551e5ebf171e9027cc8cec8c5e96c379a3d7cc9e889011b`.
- Final renders: EN `index.md` `2f7f5cc18ff8fd4f776fa4d266da363d358965509337cff83b1a4c38082598c6`; RU `ru/index.md` `3d2533400e3f1c5aa1c9d876caa99146af67aa225ac567dad4e9111f7f3e8ab8`; KK `kk/index.md` `5f7353e9707f3ac1a26656834584be38717ff816bc57c733776f9c980a1d6510`.
- `README.md` is the generated English GitHub mirror; its final SHA-256 is recorded in the renderer section.

CLI discovery confirmed `agy.exe --help` exposes `--print`, `--model`, `--mode`, `--sandbox`, `--input-format`, `--output-format`, and `--print-timeout`; `agy.exe models` exposed exact model `gemini-3.7-flash-high` (`Gemini 3.7 Flash (High)`), so no fallback was used.

Exact successful invocation shape (the NDJSON message contained the complete final EN/RU/KK renders and digest/hash header):

```powershell
$message | & 'C:\Users\c0rpa\AppData\Local\agy\bin\agy.exe' --model 'gemini-3.7-flash-high' --mode plan --sandbox --input-format stream-json --output-format stream-json --print-timeout 15m
```

Final prompt SHA-256: `bbf0e4ae9609da8a4253524eb2c0a0fd82180732b4dcf6a0a171da5a1b7d4a6c`; conversation `39d66155-2d00-44d2-8573-1d8e44224c04`; status `SUCCESS`.

Advisory result: `PASS`; all complete projections reviewed; no actionable blocking, major, minor, or nit findings. It found semantic alignment, appropriate Kazakhstan IT/Telegram terminology, concise neutral tone, and no keyword-stuffing risk. Disposition: no source change. The earlier filesystem-reading attempt was safely auto-denied in headless sandbox and produced no assessment; it was superseded by the final content-fed invocation without weakening permissions.

## Scope and mutation record

Implementation paths are exactly `README.md`, `data/communities.json`, `index.md`, `ru/index.md`, `kk/index.md`, `scripts/generate_readme.py`, `scripts/validate_schema.py`, and `scripts/test_catalog_generation.py`. Mandatory Executor traces are ONB, this EV, its changed-key attachment, and RF. No HL, TS, RES, REVIEW, status, journal, index, Phase B, deployment, settings, tag, push, release, or publication path was modified. External mutation count: zero.

---

*EV — 20260827-132641__catalog_discoverability / Phase A: Multilingual Catalog | 2026-08-27*

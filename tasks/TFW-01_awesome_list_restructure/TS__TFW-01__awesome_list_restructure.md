# TS__TFW-01__awesome_list_restructure.md

## Task ID
TFW-01

## Objective
Transform KZ-IT-telegram-list into a proper Awesome List format with automation support.

## Decisions Made (Optimal Path)
| Question | Decision | Rationale |
|----------|----------|-----------|
| Language | English primary | Global reach, standard for Awesome lists |
| Member counts | Remove from README | Stale data (2022); store `last_verified` in JSON |
| Automation | Simple HTTP 200 check | Practical, no API token needed |
| Categories | Split by technology | Better navigation for ~60 entries |
| Dead links | Archive section | Preserve history, warn users |

## Input
- Current `README.md` (Russian, 38 groups + 23 channels + 5 bots)

## Expected Output (RF Files)
1. `RF__TFW-01__communities.json` — Structured data
2. `RF__TFW-01__readme.md` — New English README
3. `RF__TFW-01__contributing.md` — Contribution guidelines
4. `RF__TFW-01__validate_links.py` — Link validation script
5. `RF__TFW-01__generate_readme.py` — README generator script

## Definition of Done
- [ ] All communities migrated to JSON
- [ ] README in English with proper Awesome format
- [ ] Validation script runs successfully
- [ ] Generator script produces identical README
- [ ] CONTRIBUTING.md exists
- [ ] LICENSE (CC0) exists

## Execution Type
**AG** (Autonomous) — All data exists locally

## Subtasks
1. [AG] Parse existing README → create `data/communities.json`
2. [AG] Create `scripts/validate_links.py`
3. [AG] Create `scripts/generate_readme.py`
4. [AG] Generate new `README.md`
5. [AG] Create `CONTRIBUTING.md`
6. [AG] Create `LICENSE`
7. [AG] Test validation script
8. [CL] User validates 5 random links manually

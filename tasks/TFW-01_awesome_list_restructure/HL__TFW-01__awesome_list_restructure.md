# HL__TFW-01__awesome_list_restructure.md

## Purpose
Transform KZ-IT-telegram-list into a proper "Awesome List" format following GitHub community standards, making it accessible to international audiences (English) while maintaining ease of updates and automation.

## Context & Research Findings

### Best Practices from Awesome Lists
Based on research of sindresorhus/awesome and ebertti/awesome-telegram:

| Element | Standard Practice |
|---------|-------------------|
| **Badge** | `awesome.re` badge at top |
| **Language** | English for global reach |
| **ToC** | Table of Contents for navigation |
| **Categories** | Logical grouping with clear headers |
| **Sorting** | Alphabetical within categories |
| **Entry Format** | `[Name](link) - Description` (concise) |
| **Contribution** | CONTRIBUTING.md with clear rules |
| **License** | CC0 or permissive license |

### Current State Analysis
Current README.md:
- In Russian only
- 38 groups, 23 channels, 5 bots
- Mixed format: some with member counts, some without
- Dates inconsistent (2022 mostly, some 2025)
- Numbering manual (error-prone)
- No ToC, no badges, no contribution guidelines

### Proposed Changes

#### 1. README.md Restructure
- **Language**: English (with Russian descriptions preserved as optional)
- **Format**: Standard Awesome List format
- **Sections**: Groups, Channels, Bots, Contributing
- **Entry**: `[Community Name](link) - Short description`
- **Remove**: Member counts (stale data), numbering (auto-sorted alphabetically)

#### 2. New Files
- `CONTRIBUTING.md` — contribution guidelines
- `LICENSE` — CC0 (public domain)
- `data/communities.json` — structured data for automation

#### 3. Automation Scripts
- `scripts/validate_links.py` — check Telegram links are alive
- `scripts/generate_readme.py` — regenerate README from JSON data
- GitHub Actions workflow for periodic validation

## Architecture Decisions

### Data-Driven Approach
Store community data in JSON, generate README from it:
```json
{
  "groups": [
    {
      "name": "Python Kazakhstan",
      "handle": "python_kz",
      "description": "Python developers community",
      "category": "programming-languages"
    }
  ]
}
```

**Rationale**: 
- Single source of truth
- Easy to validate, sort, filter
- Enables automation
- Reduces human error

### Bilingual Strategy
- README in English (primary)
- Russian descriptions in JSON field `description_ru` (optional)
- Separate Russian README possible in future (`README.ru.md`)

## Constraints
- Keep repository simple (no complex build systems)
- Scripts should be standalone Python (minimal deps)
- Manual validation still needed for bot/group activity
- Cannot programmatically verify Telegram group activity (API limitations)

## Dependencies
None — this is Task TFW-01

## Risks
| Risk | Mitigation |
|------|------------|
| Breaking existing links/bookmarks | Keep same repo URL |
| Loss of Russian context | Store `description_ru` in JSON |
| Telegram API rate limits | Simple HTTP check only |
| Stale data | Clear dates, periodic validation workflow |

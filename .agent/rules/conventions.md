# Project Conventions — KZ-IT-telegram-list

## 1) Project Purpose
Maintain an up-to-date curated list of IT Telegram communities in Kazakhstan:
- **Groups** — interactive chats for discussions
- **Channels** — one-way news/content feeds
- **Bots** — automated services by KZ developers

## 2) Project Structure
| Path | Purpose |
|------|---------|
| `README.md` | Auto-generated Awesome List (DO NOT EDIT DIRECTLY) |
| `data/communities.json` | Source of truth — all community data |
| `scripts/` | Validation and generation scripts |
| `CONTRIBUTING.md` | Contributor workflow guide |
| `LICENSE` | CC0 Public Domain |
| `.agent/rules/` | AI agent configuration |
| `tasks/` | TFW task folders |

## 3) Workflow
```
Edit JSON → Validate Schema → Validate Links → Generate README → Commit
```

### Scripts
| Script | Purpose |
|--------|---------|
| `validate_schema.py` | Check JSON structure, categories, fields |
| `validate_links.py` | Check links, fetch member counts |
| `generate_readme.py` | Generate README.md from JSON |

## 4) JSON Entry Format
```json
{
  "name": "Community Name",
  "handle": "telegram_handle",
  "description": "English description",
  "description_ru": "Русское описание",
  "category": "category-slug",
  "member_count": 1234,
  "last_verified": "YYYY-MM-DD"
}
```

### Required Fields
- `name`, `handle`, `description`, `last_verified`
- `category` (for groups only)

### Date Format
- Use ISO format: `YYYY-MM-DD` (e.g., `2026-01-30`)

## 5) Categories
Defined in `data/communities.json` under `categories` key.
Validation script enforces category membership.

## 6) Inclusion Criteria
- IT-focused topic
- Kazakhstan audience or relevance
- Active (not dead/archived)
- Quality content (no spam, no commercial-only)

## 7) Quality Standards
- No placeholders or fake data
- Links must be verified
- Dates must be current
- English descriptions required

## 8) AI Agent Modes
| Mode | When to Use |
|------|-------------|
| **AG** (Autonomous) | File operations, restructuring, formatting |
| **CL** (Chat Loop) | External data validation, link checking |

## 9) Summary Format
Agent responses end with:
```
[YYYY-MM-DD] **Summary**: Stage=... | Iteration=N | Goal=... | Task=... | Status/Problem=...
```

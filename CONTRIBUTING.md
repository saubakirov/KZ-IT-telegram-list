# Contributing to Awesome Kazakhstan IT Telegram

Thank you for contributing! This list is the go-to directory for Kazakhstan's IT Telegram community.

## Quick Start

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/KZ-IT-telegram-list.git
cd KZ-IT-telegram-list

# 2. Edit data (NOT README directly!)
# Edit: data/communities.json

# 3. Validate your changes
python scripts/validate_schema.py    # check JSON structure
python scripts/validate_links.py     # check links + fetch member counts

# 4. Regenerate README
python scripts/generate_readme.py

# 5. Commit and push
git add .
git commit -m "Add: YourCommunityName"
git push origin main

# 6. Create Pull Request
```

## Workflow Diagram

```
Edit JSON → Validate Schema → Validate Links → Generate README → PR
```

## Entry Requirements

- **IT-related** (programming, data, design, DevOps, etc.)
- **Kazakhstan-focused** or relevant to KZ audience
- **Active** (not archived/dead groups)
- **Quality** (no spam, bots, or purely commercial groups)

## JSON Entry Format

Add your entry to the appropriate section (`groups`, `channels`, or `bots`):

```json
{
  "name": "Community Name",
  "handle": "telegram_handle",
  "description": "Short description in English",
  "description_ru": "Описание на русском",
  "category": "programming-languages",
  "last_verified": "2026-01-30"
}
```

### Required Fields

| Field | Description |
|-------|-------------|
| `name` | Display name |
| `handle` | Telegram handle (without `@` or `t.me/`) |
| `description` | Short English description |
| `category` | One of the allowed categories (see below) |
| `last_verified` | Date in `YYYY-MM-DD` format |

### Optional Fields

| Field | Description |
|-------|-------------|
| `description_ru` | Russian description |
| `member_count` | Auto-filled by validation script |

## Allowed Categories

| Category | Description |
|----------|-------------|
| `programming-languages` | Python, Java, Go, Rust, Ruby, etc. |
| `web-development` | Frontend, Backend |
| `mobile` | iOS, Android, Flutter |
| `data-analytics` | BI, Data Science, ML |
| `devops-sysadmin` | DevOps, SysAdmin, Linux |
| `security` | InfoSec, Cybersecurity |
| `qa-testing` | QA, Test Automation |
| `gamedev` | Game Development |
| `hardware` | Electronics, IoT |
| `blockchain` | Crypto, Web3 |
| `management` | Tech leads, PMs |
| `general` | General IT |
| `jobs` | Job postings |
| `education` | Learning resources |
| `news` | Tech news |
| `events` | Meetups, conferences |
| `startups` | Startup ecosystem |
| `marketplace` | Buy/sell IT goods |

## Validation Scripts

### 1. Schema Validation
```bash
python scripts/validate_schema.py
```
Checks:
- Required fields present
- Category is from allowed list
- No duplicate handles
- Date format is valid
- Handle format is valid (5-32 chars, alphanumeric + underscore)

### 2. Link Validation
```bash
python scripts/validate_links.py           # just validate
python scripts/validate_links.py --update  # validate + save member counts
```
Features:
- Checks if t.me links are accessible
- Parses member/subscriber counts from HTML
- Rate limited (3 req/1.5s) to avoid bans
- Retries with exponential backoff

### 3. README Generation
```bash
python scripts/generate_readme.py
```
- Auto-generates `README.md` from `communities.json`
- Sorts by member count (popular first)
- Shows member counts as badges

## Pull Request Checklist

- [ ] Entry added to `data/communities.json`
- [ ] `handle` is correct (without `@` or `t.me/`)
- [ ] `description` is in English, concise (< 100 chars)
- [ ] `category` matches one from the list above
- [ ] `last_verified` is today's date
- [ ] `python scripts/validate_schema.py` passes
- [ ] `python scripts/validate_links.py` passes
- [ ] `python scripts/generate_readme.py` executed
- [ ] README.md regenerated and committed

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Editing README.md directly | Edit `data/communities.json` instead |
| Wrong category | Check allowed categories list |
| Forgetting `last_verified` | Add today's date |
| Handle with `@` | Remove the `@` prefix |
| Handle with full URL | Use only the handle part |

## For Maintainers

### Periodic Validation
```bash
# Update all member counts and check links
python scripts/validate_links.py --update
python scripts/generate_readme.py
git commit -am "chore: update member counts"
```

### Handle Dead Links
1. Run `validate_links.py` to identify dead links
2. Option A: Remove from JSON
3. Option B: Move to `archive` section (TODO)
4. Regenerate README

## Code of Conduct

Be respectful. No spam. Focus on quality over quantity.

## Questions?

Open an issue or contact the maintainers.

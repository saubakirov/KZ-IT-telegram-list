# Contributing to Awesome Kazakhstan IT Telegram

Thank you for contributing! This list aims to be a comprehensive directory of Kazakhstan's IT Telegram community.

## Guidelines

### Adding a New Entry

1. **Fork** this repository
2. **Edit** `data/communities.json` (not README.md directly!)
3. **Submit** a Pull Request

### Entry Requirements

- Must be **IT-related** (programming, DevOps, data, design, etc.)
- Must be **Kazakhstan-focused** or relevant to KZ audience
- Must be **active** (not dead/archived groups)
- Must be **quality** (no spam, no commercial-only groups)

### JSON Entry Format

```json
{
  "name": "Community Name",
  "handle": "telegram_handle",
  "description": "Short description in English",
  "description_ru": "Описание на русском",
  "category": "category-slug",
  "last_verified": "YYYY-MM-DD"
}
```

### Categories

| Category | Description |
|----------|-------------|
| `programming-languages` | Python, Java, Go, etc. |
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

### Pull Request Checklist

- [ ] Entry added to correct section (`groups`, `channels`, or `bots`)
- [ ] `handle` is correct (without `@` or `t.me/`)
- [ ] `description` is in English, concise
- [ ] `category` matches one from the list above
- [ ] `last_verified` is today's date
- [ ] Link actually works

### Regenerating README

After merging, maintainers will run:
```bash
python scripts/generate_readme.py
```

This auto-generates README.md from the JSON data.

## Code of Conduct

Be respectful. No spam. No self-promotion without value.

## Questions?

Open an issue or contact the maintainers.

# HL__TFW-02__enhanced_validation.md

## Purpose
Add robust validation, member count parsing, and schema enforcement for communities.json

## Current Gaps

### 1. No Category Validation
- Categories defined in `categories` section of JSON
- But entries can have any arbitrary `category` value
- Typos create ghost sections in README

### 2. No Member Count Tracking
- Removed stale counts from old README
- No automated way to fetch/update them
- Can't filter dead/tiny groups

### 3. No Rate Limiting
- Current script fires all requests in parallel
- Could trigger Telegram rate limits

## Proposed Enhancements

### A. JSON Schema Validation Script
- Check all entries have required fields
- Validate `category` matches allowed list
- Detect duplicate handles
- Check date format for `last_verified`

### B. Member Count Parser
- Parse member count from t.me HTML page
- Rate limiting: max 3 requests/second
- Retry logic: 3 attempts with exponential backoff
- Update `member_count` and `last_checked` in JSON

### C. Quality Filters
- Flag groups with <10 members as "tiny"
- Flag groups with no activity marker

## Architecture Decisions

### Rate Limiting Strategy
```python
# 3 requests per second, with 1s pause between batches
BATCH_SIZE = 3
BATCH_DELAY = 1.0  # seconds
RETRY_ATTEMPTS = 3
RETRY_BACKOFF = 2  # exponential multiplier
```

### Schema Definition
Store allowed categories in JSON file itself (already there).
Validation reads `categories` keys as source of truth.

## Risks
| Risk | Mitigation |
|------|------------|
| Rate limiting by Telegram | Slow down, add delays |
| HTML parsing breaks | Use regex fallback, graceful degradation |
| Large member counts misread | Parse carefully with locale handling |

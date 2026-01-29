#!/usr/bin/env python3
"""
Validate Telegram links and fetch member counts from communities.json

Features:
- Check if t.me links are accessible
- Parse member/subscriber counts from HTML
- Rate limiting: 3 requests/second
- Retry with exponential backoff
- Update JSON with member counts

Usage:
    python scripts/validate_links.py              # validate only
    python scripts/validate_links.py --update    # update JSON with member counts
"""

import json
import re
import sys
import time
import argparse
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from datetime import datetime

DATA_FILE = Path(__file__).parent.parent / "data" / "communities.json"

# Rate limiting
BATCH_SIZE = 3
BATCH_DELAY = 1.5  # seconds between batches
REQUEST_DELAY = 0.3  # seconds between requests in batch

# Retry settings
RETRY_ATTEMPTS = 3
RETRY_BACKOFF = 2.0  # exponential multiplier
TIMEOUT = 15  # seconds

# Member count patterns
MEMBER_PATTERNS = [
    re.compile(r'(\d[\d\s]*)\s*members?', re.IGNORECASE),
    re.compile(r'(\d[\d\s]*)\s*subscribers?', re.IGNORECASE),
    re.compile(r'<div class="tgme_page_extra">(\d[\d\s]*)', re.IGNORECASE),
]


def parse_member_count(html: str) -> int | None:
    """Extract member/subscriber count from Telegram page HTML."""
    for pattern in MEMBER_PATTERNS:
        match = pattern.search(html)
        if match:
            # Remove spaces from number (e.g., "1 865" -> "1865")
            count_str = match.group(1).replace(" ", "").replace("\u00a0", "")
            try:
                return int(count_str)
            except ValueError:
                continue
    return None


def check_link_with_retry(handle: str) -> tuple[bool, str, int | None]:
    """
    Check if a Telegram link is accessible with retry logic.
    
    Returns: (is_alive, status_message, member_count)
    """
    url = f"https://t.me/{handle}"
    
    for attempt in range(RETRY_ATTEMPTS):
        try:
            req = Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept-Language": "en-US,en;q=0.9",
            })
            
            with urlopen(req, timeout=TIMEOUT) as response:
                content = response.read().decode("utf-8", errors="ignore")
                
                # Check for error pages
                if "tgme_page_error" in content:
                    return (False, "Not found or private", None)
                if "This group or channel no longer exists" in content:
                    return (False, "Deleted", None)
                
                # Parse member count
                member_count = parse_member_count(content)
                
                return (True, "OK", member_count)
                
        except HTTPError as e:
            if e.code == 429:  # Rate limited
                wait = RETRY_BACKOFF ** (attempt + 1)
                print(f"    [RATE LIMITED] Waiting {wait}s before retry...")
                time.sleep(wait)
                continue
            return (False, f"HTTP {e.code}", None)
            
        except URLError as e:
            if attempt < RETRY_ATTEMPTS - 1:
                wait = RETRY_BACKOFF ** attempt
                time.sleep(wait)
                continue
            return (False, f"URL Error: {e.reason}", None)
            
        except Exception as e:
            if attempt < RETRY_ATTEMPTS - 1:
                wait = RETRY_BACKOFF ** attempt
                time.sleep(wait)
                continue
            return (False, f"Error: {e}", None)
    
    return (False, "Max retries exceeded", None)


def load_data() -> dict:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data: dict):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def format_count(count: int | None) -> str:
    """Format member count for display."""
    if count is None:
        return "?"
    if count >= 1000:
        return f"{count/1000:.1f}k"
    return str(count)


def main():
    parser = argparse.ArgumentParser(description="Validate Telegram links")
    parser.add_argument("--update", action="store_true", 
                        help="Update JSON with member counts")
    args = parser.parse_args()
    
    if not DATA_FILE.exists():
        print(f"[ERROR] Data file not found: {DATA_FILE}")
        sys.exit(1)
    
    data = load_data()
    
    # Collect all entries
    all_entries = []
    for entry_type in ["groups", "channels", "bots"]:
        for entry in data.get(entry_type, []):
            all_entries.append((entry_type, entry))
    
    print(f"[INFO] Validating {len(all_entries)} Telegram links...")
    print(f"[INFO] Rate limit: {BATCH_SIZE} requests per {BATCH_DELAY}s\n")
    
    alive = []
    dead = []
    updated_count = 0
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Process in batches
    for i in range(0, len(all_entries), BATCH_SIZE):
        batch = all_entries[i:i + BATCH_SIZE]
        
        for entry_type, entry in batch:
            handle = entry["handle"]
            name = entry["name"]
            
            is_alive, status, member_count = check_link_with_retry(handle)
            
            if is_alive:
                alive.append((entry_type, name, handle, member_count))
                count_str = format_count(member_count)
                print(f"  [OK] [{entry_type}] {name} (@{handle}) - {count_str} members")
                
                # Update JSON if requested
                if args.update and member_count is not None:
                    entry["member_count"] = member_count
                    entry["last_verified"] = today
                    updated_count += 1
            else:
                dead.append((entry_type, name, handle, status))
                print(f"  [FAIL] [{entry_type}] {name} (@{handle}) - {status}")
            
            time.sleep(REQUEST_DELAY)
        
        # Delay between batches
        if i + BATCH_SIZE < len(all_entries):
            time.sleep(BATCH_DELAY)
    
    # Summary
    print(f"\n{'='*50}")
    print("VALIDATION SUMMARY")
    print(f"{'='*50}")
    print(f"  [OK] Alive: {len(alive)}")
    print(f"  [FAIL] Dead/Error: {len(dead)}")
    print(f"  Total: {len(all_entries)}")
    
    if args.update:
        print(f"  Updated member counts: {updated_count}")
        save_data(data)
        print(f"  [SAVED] {DATA_FILE}")
    
    if dead:
        print(f"\n[WARNING] Dead/Error links:")
        for entry_type, name, handle, status in dead:
            print(f"    - [{entry_type}] {name} (@{handle}): {status}")
        sys.exit(1)
    else:
        print(f"\n[SUCCESS] All links are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Validate Telegram links from communities.json

Usage:
    python scripts/validate_links.py

Checks all t.me links and reports status.
"""

import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

DATA_FILE = Path(__file__).parent.parent / "data" / "communities.json"
TIMEOUT = 10  # seconds
MAX_WORKERS = 10


def check_link(handle: str) -> tuple[str, bool, str]:
    """Check if a Telegram link is accessible.
    
    Returns: (handle, is_alive, status_message)
    """
    url = f"https://t.me/{handle}"
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=TIMEOUT) as response:
            # Telegram returns 200 even for non-existent, but content differs
            content = response.read().decode("utf-8", errors="ignore")
            if "tgme_page_error" in content or "This group or channel no longer exists" in content:
                return (handle, False, "Not found or private")
            return (handle, True, "OK")
    except HTTPError as e:
        return (handle, False, f"HTTP {e.code}")
    except URLError as e:
        return (handle, False, f"URL Error: {e.reason}")
    except Exception as e:
        return (handle, False, f"Error: {e}")


def load_communities() -> dict:
    """Load communities from JSON file."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    if not DATA_FILE.exists():
        print(f"[ERROR] Data file not found: {DATA_FILE}")
        sys.exit(1)
    
    data = load_communities()
    
    # Collect all handles
    handles = []
    for group in data.get("groups", []):
        handles.append(("group", group["name"], group["handle"]))
    for channel in data.get("channels", []):
        handles.append(("channel", channel["name"], channel["handle"]))
    for bot in data.get("bots", []):
        handles.append(("bot", bot["name"], bot["handle"]))
    
    print(f"[INFO] Validating {len(handles)} Telegram links...\n")
    
    alive = []
    dead = []
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_info = {
            executor.submit(check_link, handle): (type_, name, handle)
            for type_, name, handle in handles
        }
        
        for future in as_completed(future_to_info):
            type_, name, handle = future_to_info[future]
            _, is_alive, status = future.result()
            
            if is_alive:
                alive.append((type_, name, handle))
                print(f"  [OK] [{type_}] {name} (@{handle})")
            else:
                dead.append((type_, name, handle, status))
                print(f"  [FAIL] [{type_}] {name} (@{handle}) - {status}")
    
    # Summary
    print(f"\n{'='*50}")
    print(f"SUMMARY")
    print(f"{'='*50}")
    print(f"  [OK] Alive: {len(alive)}")
    print(f"  [FAIL] Dead/Error: {len(dead)}")
    print(f"  Total: {len(handles)}")
    
    if dead:
        print(f"\n[WARNING] Dead/Error links:")
        for type_, name, handle, status in dead:
            print(f"    - [{type_}] {name} (@{handle}): {status}")
        sys.exit(1)
    else:
        print(f"\n[SUCCESS] All links are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()

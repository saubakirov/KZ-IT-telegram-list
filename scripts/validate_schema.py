#!/usr/bin/env python3
"""
Validate JSON schema for communities.json

Checks:
- Required fields present
- Category matches allowed list
- No duplicate handles
- Date format valid
- Handle format valid

Usage:
    python scripts/validate_schema.py
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).parent.parent / "data" / "communities.json"

# Required fields per entry type
REQUIRED_FIELDS = {
    "groups": ["name", "handle", "description", "category", "last_verified"],
    "channels": ["name", "handle", "description", "last_verified"],
    "bots": ["name", "handle", "description", "last_verified"],
}

# Handle pattern: alphanumeric, underscores, 5-32 chars
HANDLE_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]{4,31}$")

# Date pattern: YYYY-MM-DD
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_data() -> dict:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_entries(entries: list, entry_type: str, allowed_categories: set) -> list:
    """Validate a list of entries, return list of errors."""
    errors = []
    seen_handles = set()
    required = REQUIRED_FIELDS.get(entry_type, [])
    
    for i, entry in enumerate(entries):
        prefix = f"[{entry_type}][{i}] {entry.get('name', 'UNNAMED')}"
        
        # Check required fields
        for field in required:
            if field not in entry or not entry[field]:
                errors.append(f"{prefix}: missing required field '{field}'")
        
        # Check handle format
        handle = entry.get("handle", "")
        if handle:
            if not HANDLE_PATTERN.match(handle):
                errors.append(f"{prefix}: invalid handle format '@{handle}'")
            if handle.lower() in seen_handles:
                errors.append(f"{prefix}: duplicate handle '@{handle}'")
            seen_handles.add(handle.lower())
        
        # Check category (only for groups)
        if entry_type == "groups":
            category = entry.get("category", "")
            if category and category not in allowed_categories:
                errors.append(f"{prefix}: unknown category '{category}' (allowed: {sorted(allowed_categories)})")
        
        # Check date format
        date = entry.get("last_verified", "")
        if date:
            if not DATE_PATTERN.match(date):
                errors.append(f"{prefix}: invalid date format '{date}' (expected YYYY-MM-DD)")
            else:
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    errors.append(f"{prefix}: invalid date value '{date}'")
    
    return errors


def main():
    if not DATA_FILE.exists():
        print(f"[ERROR] Data file not found: {DATA_FILE}")
        sys.exit(1)
    
    data = load_data()
    
    # Get allowed categories
    allowed_categories = set(data.get("categories", {}).keys())
    if not allowed_categories:
        print("[WARNING] No categories defined in JSON")
    
    all_errors = []
    
    # Validate each section
    for entry_type in ["groups", "channels", "bots"]:
        entries = data.get(entry_type, [])
        print(f"[INFO] Validating {len(entries)} {entry_type}...")
        errors = validate_entries(entries, entry_type, allowed_categories)
        all_errors.extend(errors)
    
    # Summary
    print(f"\n{'='*50}")
    print("SCHEMA VALIDATION SUMMARY")
    print(f"{'='*50}")
    print(f"  Groups: {len(data.get('groups', []))}")
    print(f"  Channels: {len(data.get('channels', []))}")
    print(f"  Bots: {len(data.get('bots', []))}")
    print(f"  Categories: {len(allowed_categories)}")
    print(f"  Errors: {len(all_errors)}")
    
    if all_errors:
        print(f"\n[ERRORS]")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"\n[SUCCESS] Schema is valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Synchronize complete Claude-authored kz-* commands to exact Codex skill copies."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE = ROOT / ".claude" / "commands"
CODEX = ROOT / ".agents" / "skills"
NAMES = ("kz-add", "kz-stats", "kz-release")
SECTIONS = ("## Authority", "## Inputs", "## Ordered Operation", "## Outputs",
            "## Failure Conditions", "## Hard Stop")
SPECIFIC = {
    "kz-add": ("scripts/kz_intake.py", "exact owner-approved", "controlled-path", "--text", "--file"),
    "kz-stats": ("scripts/validate_links.py", "owner triage", "archive", "unresolved"),
    "kz-release": ("data-YYYY-MM-DD", "tag", "push", "explicit current approval"),
}
FORBIDDEN = ("../", ".tfw/workflows/", ".claude/commands/", ".agents/skills/")


def paths(name):
    return CLAUDE / f"{name}.md", CODEX / name / "SKILL.md"


def metadata(body: str) -> dict[str, str]:
    if not body.startswith("---\n") or "\n---\n" not in body[4:]:
        raise ValueError("common YAML front matter is missing")
    header = body[4:body.index("\n---\n", 4)]
    result = {}
    for line in header.splitlines():
        if ":" not in line:
            raise ValueError("invalid front matter")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    if set(result) != {"name", "description"} or not result["description"]:
        raise ValueError("front matter must contain only non-empty name/description")
    return result


def validate(name: str, body: bytes) -> list[str]:
    errors = []
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        return [f"{name}: invalid UTF-8"]
    if b"\r" in body or not body.endswith(b"\n"):
        errors.append(f"{name}: expected LF with trailing newline")
    try:
        header = metadata(text)
        if header["name"] != name:
            errors.append(f"{name}: metadata name differs")
    except ValueError as error:
        errors.append(f"{name}: {error}")
    for section in SECTIONS:
        if text.count(section) != 1:
            errors.append(f"{name}: section {section!r} must appear once")
    for token in SPECIFIC[name]:
        if token.casefold() not in text.casefold():
            errors.append(f"{name}: missing complete-body marker {token!r}")
    for token in FORBIDDEN:
        if token in text:
            errors.append(f"{name}: forbidden runtime-relative/counterpart reference {token!r}")
    return errors


def inventory() -> tuple[set[str], set[str]]:
    claude = {path.stem for path in CLAUDE.glob("kz-*.md")}
    codex = {path.name for path in CODEX.glob("kz-*") if (path / "SKILL.md").is_file()}
    return claude, codex


def run(sync: bool) -> list[str]:
    errors = []
    expected = set(NAMES)
    claude, codex = inventory()
    if claude != expected:
        errors.append(f"Claude inventory differs: {sorted(claude)}")
    if not sync and codex != expected:
        errors.append(f"Codex inventory differs: {sorted(codex)}")
    for name in NAMES:
        source, target = paths(name)
        if not source.is_file():
            errors.append(f"{name}: Claude source missing")
            continue
        body = source.read_bytes()
        errors.extend(validate(name, body))
        if sync and not errors:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        if not target.is_file():
            errors.append(f"{name}: Codex copy missing")
        elif target.read_bytes() != body:
            errors.append(f"{name}: byte parity differs")
        else:
            errors.extend(validate(name, target.read_bytes()))
    if sync and inventory()[1] != expected:
        errors.append(f"Codex inventory differs after sync: {sorted(inventory()[1])}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check only (default; never mutates)")
    mode.add_argument("--sync", action="store_true", help="copy Claude sources to Codex skills")
    args = parser.parse_args()
    errors = run(args.sync)
    if errors:
        print("\n".join(f"[ERROR] {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"[OK] synchronized complete command inventory: {', '.join(NAMES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

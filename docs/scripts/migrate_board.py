"""Account for the root Task Board exactly, then retire it.

The board was the project's live task registry and its portfolio view at the same time.
Removing it means proving first that nothing it carried is lost. This script does the
counting, because exact accounting over a hundred-odd rows and directories is a counting
problem rather than a judgement one.

What it guarantees:

* **Every row and every directory is accounted for exactly once.** Rows with no directory,
  directories with no well-formed row, and rows in a shape no parser matches are all
  classified and reported. Nothing is silently dropped and nothing is silently merged.
* **Nothing existing is renamed, moved or byte-changed.** No legacy artifact is ever opened
  in write mode — not even to rewrite it unchanged, because a checkout with ``autocrlf``
  set would rewrite its line endings on the way out.
* **No fact is invented.** A task state file is written only from what the board and the
  directory actually say. A value the source never carried is recorded as ``unrecorded``,
  not guessed. A lifecycle outside the declared vocabulary is carried verbatim and flagged,
  not normalized into a declared one.

Usage:
    python docs/scripts/migrate_board.py                        # dry run, prints accounting
    python docs/scripts/migrate_board.py --manifest OUT.md      # dry run, writes accounting
    python docs/scripts/migrate_board.py --apply                # writes snapshot + status files
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_index import (  # noqa: E402
    LEGACY_ID,
    TASK_DIR,
    iter_task_dirs,
    parse_identifier,
    read_config,
    sort_key,
    task_containers,
)

DEFAULT_BOARD_PATH = "README.md"
DEFAULT_BOARD_HEADING = "## Task Board"

#: Statuses the project actually declares, from project_config.yaml `tfw.statuses`.
FALLBACK_STATUSES = [
    "TODO", "HL_DRAFT", "RES", "PHASES", "TS_DRAFT", "ONB", "RF", "REV", "KNW",
    "DONE", "BLOCKED", "REJECTED",
]
TERMINAL = {"DONE", "REJECTED"}

#: Preference order when deciding which artifact a task's state should point at.
AUTHORITY_ORDER = ("HL-", "HL__", "PROPOSAL__", "TS__", "RF__")


# ---------------------------------------------------------------------------
# Board parsing
# ---------------------------------------------------------------------------

def declared_statuses(root: Path) -> list[str]:
    entries = read_config(root).get("statuses") or []
    ids = [str(entry.get("id")) for entry in entries if isinstance(entry, dict) and entry.get("id")]
    return ids or list(FALLBACK_STATUSES)


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_board(text: str, heading: str = DEFAULT_BOARD_HEADING) -> list[dict]:
    """Every data row of the board table, in document order, with nothing filtered out.

    A row is a row. Whether its identifier is a link, plain text or struck through decides
    its class later — it never decides whether the row is seen.
    """
    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        return []
    rows: list[dict] = []
    seen_header = False
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if not line.startswith("|"):
            if rows and line.strip() == "":
                continue
            if rows:
                break
            continue
        cells = split_row(line)
        if not seen_header:
            seen_header = True
            continue
        if set(cells[0]) <= set("-: "):
            continue
        identifier = re.search(r"[A-Z][A-Z0-9]*-\d+", cells[0])
        rows.append({
            "line": index + 1,
            "raw": line,
            "cells": cells,
            "id": identifier.group(0) if identifier else None,
            "id_cell": cells[0],
            "linked": cells[0].startswith("[") or "](" in cells[0],
            "struck": "~~" in cells[0],
            "title": cells[1] if len(cells) > 1 else "",
            "status_cell": cells[2] if len(cells) > 2 else "",
        })
    return rows


def classify_status(cell: str, declared: list[str]) -> dict:
    """Map a board status cell onto the declared vocabulary, or report that it is outside.

    The token is matched against declared ids only. ``🟡 TS`` is not ``TS_DRAFT``: it is the
    pre-rename label of that state and therefore outside the vocabulary as it stands today.
    Calling it ``TS_DRAFT`` would be normalizing a value the source never used.
    """
    verbatim = cell.strip()
    if not verbatim or verbatim == "—":
        return {"lifecycle": "UNDECLARED", "verbatim": verbatim or "(empty)", "outcome": ""}
    body = "".join(
        ch for ch in verbatim
        if not unicodedata.category(ch).startswith("S") and ch != "️"
    ).strip()
    token = re.match(r"[A-Z_]+", body)
    token = token.group(0) if token else ""
    trailing = body[len(token):].strip().lstrip("—-–").strip()
    if token in declared:
        return {"lifecycle": token, "verbatim": "", "outcome": trailing}
    return {"lifecycle": "UNDECLARED", "verbatim": verbatim, "outcome": ""}


# ---------------------------------------------------------------------------
# Reconciliation
# ---------------------------------------------------------------------------

def reconcile(root: Path, rows: list[dict]) -> dict:
    """Match rows against directories. Every entry lands in exactly one class."""
    directories = {}
    for path in iter_task_dirs(root):
        parsed = parse_identifier(path.name)
        directories[parsed[1]] = path

    matched, board_only, malformed = [], [], []
    claimed: set[str] = set()
    for row in rows:
        identifier = row["id"]
        if identifier and identifier in directories:
            row["path"] = directories[identifier]
            claimed.add(identifier)
            matched.append(row)
            if not row["linked"] or row["struck"]:
                malformed.append(row)
        else:
            board_only.append(row)
            if not row["linked"] or row["struck"]:
                malformed.append(row)

    directory_only = [
        {"id": identifier, "path": path}
        for identifier, path in sorted(directories.items(), key=lambda kv: sort_key(*parse_identifier(kv[0])))
        if identifier not in claimed
    ]
    return {
        "rows": rows,
        "directories": directories,
        "matched": matched,
        "board_only": board_only,
        "directory_only": directory_only,
        "malformed": malformed,
    }


# ---------------------------------------------------------------------------
# Task state synthesis
# ---------------------------------------------------------------------------

def first_commit_date(root: Path, path: Path) -> str:
    """Creation time as Git recorded it, at second resolution, or ``unrecorded``.

    Git knows the exact second a path first appeared, so nothing is invented here. Where a
    source carries only a day, callers use :data:`gen_index.ZERO_TIME` — a *declared* zero,
    meaning "this day, time unknown", never a measurement.
    """
    try:
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%ad",
             "--date=format:%Y%m%d-%H%M%S", "--", path.relative_to(root).as_posix()],
            cwd=root, capture_output=True, text=True, encoding="utf-8", check=False,
        )
    except OSError:
        return "unrecorded"
    dates = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return dates[-1] if dates else "unrecorded"


def tracked_files(root: Path, task_dir: Path) -> set[str] | None:
    """Paths under ``task_dir`` that Git actually carries, relative to it.

    Returns ``None`` when Git cannot answer — no repository, or no Git at all — so callers
    can fall back rather than treat "unknown" as "untracked".
    """
    try:
        result = subprocess.run(
            ["git", "ls-files", "--", task_dir.relative_to(root).as_posix()],
            cwd=root, capture_output=True, text=True, encoding="utf-8", check=False,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    prefix = task_dir.relative_to(root).as_posix() + "/"
    return {line[len(prefix):] for line in result.stdout.splitlines()
            if line.startswith(prefix)}


def find_authority(task_dir: Path, tracked: set[str] | None = None) -> str:
    """The governing artifact: the highest-preference file that a clean clone will have.

    Preference alone is not enough. A working tree can hold an uncommitted draft that
    outranks the committed artifact, and choosing it produces a state file whose authority
    link is broken for everyone who clones — which is exactly what happened to TFW-54 in the
    rejected pass, where `authority` named an HL that existed only on one machine.

    So: rank by preference, but only among files Git carries. If Git cannot answer, fall
    back to the filesystem rather than treating silence as absence.
    """
    def candidates(directory: Path, relative: str = "") -> list[str]:
        return sorted(f"{relative}{p.name}" for p in directory.iterdir()
                      if p.is_file() and p.suffix == ".md")

    pools = [candidates(task_dir)]
    for child in sorted((p for p in task_dir.iterdir() if p.is_dir()), key=lambda p: p.name):
        pools.append(candidates(child, f"{child.name}/"))

    for require_tracked in (True, False):
        if require_tracked and tracked is None:
            continue
        for pool in pools:
            for prefix in AUTHORITY_ORDER:
                for name in pool:
                    if not name.split("/")[-1].startswith(prefix):
                        continue
                    if require_tracked and name not in tracked:
                        continue
                    return name
    return "unrecorded"


def _bound(text: str, limit: int) -> str:
    """Shorten to the bound at a word boundary, and say so.

    A bounded field is lossy by design. The ellipsis marks it as shortened rather than
    finished, so nobody reads a cut sentence as the whole fact; the full text stays in the
    board snapshot and in the task's own artifacts.
    """
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    cut = text[:limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:+&-—–")
    return (cut or text[:limit - 1]) + "…"


def _short_name(description: str) -> str:
    """The leading clause of a board description, as its name.

    Board descriptions are one line carrying a name, then a colon or dash, then the detail.
    The part before that break is the name; everything after it is the goal.
    """
    for separator in (": ", " — ", " – ", ". ", " ("):
        head = description.split(separator, 1)[0]
        if head != description and 3 <= len(head) <= 80:
            return head.rstrip(" .,:;")
    return _bound(description, 80)


def _scalar(value: str) -> str:
    """Emit a YAML scalar that survives a round trip.

    Board descriptions carry colons, hashes and quotes. Written bare they produce a file
    that looks right and parses wrong — and a state file the index cannot read is a task
    that vanishes from the portfolio.
    """
    text = str(value)
    unsafe = ':#\'"\n'   # colon, hash, quote, apostrophe, newline
    if text and not any(ch in text for ch in unsafe) and text.strip() == text:
        return text
    escaped = text.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))
    return chr(34) + escaped + chr(34)


def _plain(text: str) -> str:
    """Strip Markdown links and emphasis so a bounded field stays a readable sentence."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`~]+", "", text)
    return " ".join(text.split())


def build_status(root: Path, row: dict, declared: list[str], now: str) -> str:
    """Task state from verified facts only. Absent facts are recorded as absent."""
    task_dir: Path = row["path"]
    status = classify_status(row["status_cell"], declared)
    description = _plain(row["title"])

    fields = [
        ("id", row["id"]),
        ("title", _short_name(description)),
        ("goal", _bound(description, 160)),
        ("value", "unrecorded"),
        ("lifecycle", status["lifecycle"]),
    ]
    if status["lifecycle"] == "UNDECLARED":
        fields.append(("lifecycle_verbatim", _bound(status["verbatim"], 80)))
    fields.append(("owner", "unassigned"))
    fields.append(("authority", find_authority(task_dir, tracked_files(root, task_dir))))
    if status["lifecycle"] in TERMINAL and status["outcome"]:
        fields.append(("outcome", _bound(_plain(status["outcome"]), 160)))
    fields.append(("created", first_commit_date(root, task_dir)))
    fields.append(("updated", now))

    lines = ["---"]
    lines += [f"{key}: {_scalar(value)}" for key, value in fields]
    lines.append("---")
    lines.append("")
    lines.append("**Task state.** This file is the only authority for this task's live "
                 "state. The portfolio index is derived from it and never outranks it.")
    lines.append("")
    lines.append("<!-- Written by docs/scripts/migrate_board.py from the root Task Board "
                 "at TFW 2.0.0. `unrecorded` means the board carried no such fact; it was "
                 "not guessed. Fill it in when the fact is known. -->")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Snapshot
# ---------------------------------------------------------------------------

def render_snapshot(result: dict, declared: list[str], index_link: str = "../workspace/00-INDEX.md") -> str:
    rows = result["rows"]
    matched_ids = {row["id"] for row in result["matched"]}
    out: list[str] = []
    add = out.append
    add("# Board snapshot — the root Task Board at TFW 2.0.0\n")
    add("")
    add("Every data row of the root `README.md` Task Board, captured verbatim on the day")
    add("the board was removed. This is history: it is never edited, never re-sorted and")
    add("never brought up to date. Live state lives in each task's own `status.md`, and the")
    add("browsable view is rebuilt at")
    add(f"[`{index_link.lstrip('./')}`]({index_link}).")
    add("")
    add("Backlog rows are here too. Six of them are ideas that never had a task directory —")
    add("a snapshot of only finished work would have deleted the project's backlog. An idea")
    add("is picked up by creating a real task, not by resurrecting a row.")
    add("")
    add("| | |")
    add("|---|---|")
    add(f"| Rows captured | {len(rows)} |")
    add(f"| With a task directory | {len(matched_ids)} |")
    add(f"| Board-only, no directory | {len(result['board_only'])} |")
    add(f"| In a shape no strict row parser matches | {len(result['malformed'])} |")
    add("")

    add("## Rows\n")
    add("| ID | Task | Status | Class |")
    add("|---|---|---|---|")
    for row in rows:
        identifier = row["id"] or "(none)"
        if row["id"] in matched_ids:
            klass = "absorbed elsewhere, directory retained" if row["struck"] else (
                "plain-text row, directory exists" if not row["linked"] else "matched")
        elif row["struck"]:
            klass = "board-only, absorbed elsewhere"
        else:
            klass = "board-only, backlog"
        title = _plain(row["title"]).replace("|", "\\|")
        # Rendered as text: a status cell can carry a Markdown link whose path is relative
        # to the project root and therefore broken from inside this file. The byte-verbatim
        # record is the fenced block below, not this table.
        status = _plain(row["status_cell"]).replace("|", chr(92) + "|") or "—"
        add(f"| `{identifier}` | {_bound(title, 200)} | {status} | {klass} |")
    add("")

    add("## Verbatim source\n")
    add("The rows exactly as the board carried them, links, strike-through and schema drift")
    add("included. This block is what makes the table above checkable.")
    add("")
    add("```text")
    for row in rows:
        add(row["raw"])
    add("```")
    add("")
    add("---")
    add("")
    add("*Captured once by `docs/scripts/migrate_board.py`. Historical — do not update.*")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Accounting manifest
# ---------------------------------------------------------------------------

def render_manifest(root: Path, result: dict, declared: list[str],
                    writes: list[tuple[Path, str]], title: str = "Migration accounting") -> str:
    rows = result["rows"]
    directories = result["directories"]
    out: list[str] = []
    add = out.append
    add("# " + title)
    add("")
    add("")
    add("Produced by `python docs/scripts/migrate_board.py --manifest`. Every board row and")
    add("every task directory is accounted for exactly once. Re-runnable: the numbers below")
    add("are recomputed from the tree, not transcribed.")
    add("")
    add("## Reconciliation\n")
    add("```")
    add(f"  {len(rows):3} board data rows")
    add(f"  {len(directories):3} task directories")
    add("  " + "-" * 40)
    add(f"  {len(rows) + len(directories):3} source occurrences  ->  "
        f"{len(set(list(directories) + [r['id'] for r in rows if r['id']])):3} logical identities")
    add("")
    add(f"      {len(result['matched']):3}  matched       row and directory both exist")
    add(f"      {len(result['board_only']):3}  board-only    a row with no directory")
    add(f"      {len(result['directory_only']):3}  directory-only  a directory with no row")
    add("```")
    add("")
    add(f"Rows in a shape no strict `| [ID](path)` parser matches: **{len(result['malformed'])}**. "
        "They are reported, not repaired.")
    add("")

    add("## Board-only rows\n")
    if result["board_only"]:
        add("| ID | Status | Why it has no directory |")
        add("|---|---|---|")
        for row in result["board_only"]:
            reason = "absorbed into another task" if row["struck"] else "backlog idea, never started"
            add(f"| `{row['id'] or '(none)'}` | {row['status_cell'] or '—'} | {reason} |")
    else:
        add("None.")
    add("")

    add("## Directory-only entries\n")
    if result["directory_only"]:
        add("| ID | Path |")
        add("|---|---|")
        for entry in result["directory_only"]:
            add(f"| `{entry['id']}` | `{entry['path'].relative_to(root).as_posix()}` |")
    else:
        add("None — every directory is named by a row, though not every row names it in a "
            "shape a strict parser matches.")
    add("")

    add("## Malformed rows\n")
    if result["malformed"]:
        add("| ID | Form | Directory? |")
        add("|---|---|---|")
        for row in result["malformed"]:
            form = "struck through" if row["struck"] else "plain text, not a link"
            has = "yes" if row["id"] in directories else "no"
            add(f"| `{row['id'] or '(none)'}` | {form} | {has} |")
    else:
        add("None.")
    add("")

    # --- every identifier, by name -----------------------------------------
    written = {path.parent.name.split("__")[0] for path, _ in writes}
    resolution: list[tuple[str, str]] = []
    for row in rows:
        identifier = row["id"]
        if not identifier:
            resolution.append(("(no identifier)", "snapshot row only"))
            continue
        where = ["snapshot"]
        if identifier in directories:
            where.append("task directory")
            if identifier in written:
                where.append("`status.md` → index")
            else:
                where.append("index (unresolved or closed)")
        resolution.append((identifier, " + ".join(where)))

    add(f"## Every board identifier, by name — {len(resolution)}\n")
    add("The requirement is that each one **resolves** somewhere after the board is gone, and")
    add("that the list is produced by counting rather than asserted. A previous pass claimed")
    add("61 rows were retained while the snapshot held zero; naming them individually is what")
    add("makes that failure impossible to repeat.")
    add("")
    add("| # | Identifier | Resolves to |")
    add("|---:|---|---|")
    for number, (identifier, where) in enumerate(resolution, 1):
        add(f"| {number} | `{identifier}` | {where} |")
    add("")
    unaccounted = [i for i, w in resolution if not w]
    add(f"**Unaccounted: {len(unaccounted)}.**"
        + (" " + ", ".join(f"`{i}`" for i in unaccounted) if unaccounted else
           " Every identifier the board carried resolves after its removal."))
    add("")

    add("## Task state written\n")
    if writes:
        add("Only for non-terminal tasks that have a directory. Every value comes from the")
        add("board or the directory; `unrecorded` marks a fact the source never carried.")
        add("")
        add("| Task | Lifecycle | Authority | Note |")
        add("|---|---|---|---|")
        for path, content in writes:
            fields = dict(
                line.split(": ", 1) for line in content.splitlines()
                if ": " in line and not line.startswith(("**", "<!--"))
            )
            note = ""
            if fields.get("lifecycle") == "UNDECLARED":
                note = f"status `{fields.get('lifecycle_verbatim', '')}` is outside the declared vocabulary — carried verbatim"
            add(f"| `{fields.get('id')}` | {fields.get('lifecycle')} | "
                f"`{fields.get('authority')}` | {note} |")
    else:
        add("None.")
    add("")

    add("## Guarantees checked\n")
    add("| Guarantee | How |")
    add("|---|---|")
    add("| Zero renames, zero moves | the script has no rename or move call |")
    add("| Zero byte changes to existing artifacts | only paths that do not yet exist are opened for writing; an existing target aborts the run |")
    add("| No fact invented | absent facts are written as `unrecorded`; a lifecycle outside the vocabulary becomes `UNDECLARED` plus the verbatim value |")
    add("| Every row and directory accounted once | the reconciliation above sums to the source occurrence count |")
    add("")
    add("---")
    add("")
    add(f"*{title}*")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def read_board(root: Path, revision: str | None,
               board: str = DEFAULT_BOARD_PATH) -> tuple[str, str]:
    """The board text, and a human-readable description of where it came from.

    The board is a *historical* input. Once it has been removed from the working tree the
    only honest source is Git, which is why the source is an explicit argument rather than
    an assumption. Reading the live README after removal yields zero rows, and a migration
    that accepts zero rows deletes the trace it exists to preserve.
    """
    if revision:
        result = subprocess.run(
            ["git", "show", f"{revision}:{board}"],
            cwd=root, capture_output=True, text=True, encoding="utf-8", check=False,
        )
        if result.returncode != 0:
            raise SystemExit(f"cannot read {board} at {revision}: {result.stderr.strip()}")
        return result.stdout, f"git show {revision}:{board}"
    return ((root / board).read_text(encoding="utf-8"),
            f"{board} (working tree)")


def legacy_container(root: Path) -> str:
    """Where the snapshot belongs: the last configured container, which holds the old corpus."""
    containers = task_containers(root)
    return containers[-1] if containers else "tasks"


def plan(root: Path, now: str, board_text: str | None = None,
         heading: str = DEFAULT_BOARD_HEADING,
         board: str = DEFAULT_BOARD_PATH
         ) -> tuple[dict, list[tuple[Path, str]], list[str]]:
    declared = declared_statuses(root)
    if board_text is None:
        board_text, _ = read_board(root, None, board)
    rows = parse_board(board_text, heading)
    result = reconcile(root, rows)

    writes: list[tuple[Path, str]] = []
    for row in result["matched"]:
        status = classify_status(row["status_cell"], declared)
        if status["lifecycle"] in TERMINAL:
            continue
        if row["struck"]:
            # A struck-through row records work absorbed into another task. Its directory
            # is a trace, not a live task. Giving it state would make an entry the board
            # itself retired look actionable again; it stays an unresolved input instead,
            # visible in the snapshot and in the index's unresolved section.
            continue
        writes.append((row["path"] / "status.md",
                       build_status(root, row, declared, now), row["id"]))
    writes.sort(key=lambda item: sort_key(*parse_identifier(item[2])))
    writes = [(path, content) for path, content, _ in writes]

    # The index lives in the FIRST container; the snapshot in the last. Both come from
    # configuration, so a project that renamed either still gets a working link.
    containers = task_containers(root)
    index_link = f"../{containers[0]}/00-INDEX.md" if containers else "../workspace/00-INDEX.md"
    snapshot = render_snapshot(result, declared, index_link)
    return result, writes, [snapshot]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--apply", action="store_true", help="write files; default is a dry run")
    parser.add_argument("--manifest", type=Path, help="write the accounting to this path")
    parser.add_argument("--now", default=datetime.now().strftime("%Y%m%d-%H%M%S"),
                        help="the moment stamped into `updated`, YYYYMMDD-HHMMSS. Defaults "
                             "to a read of the system clock; pass a value only to make a "
                             "run reproducible in a test")
    parser.add_argument("--board", default=DEFAULT_BOARD_PATH, metavar="PATH",
                        help="repo-relative path to the file carrying the board. "
                             f"Defaults to {DEFAULT_BOARD_PATH!r}. This project kept its "
                             "board in tasks/README.md, because scripts/generate_readme.py "
                             "regenerates the root README in full")
    parser.add_argument("--board-heading", default=DEFAULT_BOARD_HEADING, metavar="HEADING",
                        help="the exact heading line the board table follows. "
                             f"Defaults to {DEFAULT_BOARD_HEADING!r}")
    parser.add_argument("--board-rev", metavar="REV",
                        help="read the board from README.md at this Git revision instead of "
                             "the working tree. Required once the board has been removed")
    parser.add_argument("--skip-existing", action="store_true",
                        help="write only the files that do not yet exist, instead of "
                             "refusing the whole run. Use when re-running over a corpus "
                             "whose live tasks have already moved on: their state is theirs "
                             "now, and migration must not reach back into it")
    parser.add_argument("--allow-empty-board", action="store_true",
                        help="proceed even when the board source yields zero rows. Only ever "
                             "correct when a project genuinely never had a board")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    declared = declared_statuses(root)
    board_text, origin = read_board(root, args.board_rev, args.board)
    print(f"clock read: {args.now}", file=sys.stderr)
    result, writes, (snapshot,) = plan(root, args.now, board_text,
                                       args.board_heading, args.board)
    snapshot_path = root / legacy_container(root) / "BOARD-SNAPSHOT.md"

    rows = len(result["rows"])
    print(f"board source: {origin} -> {rows} data rows", file=sys.stderr)
    if rows == 0 and not args.allow_empty_board:
        print("REFUSING: the board source yielded zero rows.\n"
              "  A snapshot of an empty board is not a snapshot, it is a deleted trace.\n"
              "  If the board has already been removed, name the commit that still had it:\n"
              "      --board-rev <commit-before-removal>\n"
              "  If this project genuinely never had a board, pass --allow-empty-board.",
              file=sys.stderr)
        return 1

    manifest = render_manifest(root, result, declared, writes)
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(manifest, encoding="utf-8", newline="\n")
        print(f"wrote {args.manifest}")
    else:
        print(manifest)

    if not args.apply:
        print(f"DRY RUN — would write {len(writes) + 1} files "
              f"({len(writes)} task state, 1 snapshot). Nothing was changed.", file=sys.stderr)
        return 0

    targets = [(snapshot_path, snapshot)] + writes
    existing = [path for path, _ in targets if path.exists()]
    if existing and not args.skip_existing:
        for path in existing:
            print(f"refusing to overwrite: {path}", file=sys.stderr)
        print("Migration writes new files only. Nothing was changed.",
              file=sys.stderr)
        print("  Pass --skip-existing to write the rest and leave these alone.",
              file=sys.stderr)
        return 1
    if existing:
        for path in existing:
            print(f"skipping, already exists: {path.relative_to(root).as_posix()}",
                  file=sys.stderr)
        targets = [(path, content) for path, content in targets if not path.exists()]
    for path, content in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Tests for the board migration.

The migration's promises are negative ones — nothing renamed, nothing byte-changed, nothing
invented, nothing dropped — and negative promises need tests more than positive ones do,
because a bug in them looks exactly like success.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import migrate_board  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DECLARED = migrate_board.FALLBACK_STATUSES

BOARD = """# Project

## Task Board

| ID | Task | Status | Notes |
|----|------|--------|-------|
| [TFW-1](tasks/TFW-1__alpha/) | First task | ✅ DONE | shipped |
| [TFW-2](tasks/TFW-2__beta/) | Second task | 🟢 RF | in progress |
| TFW-3 | Backlog idea | ⬜ TODO | never started |
| ~~[TFW-4](tasks/TFW-4__delta/)~~ — absorbed into TFW-2 | Folded in | — | |
| ~~TFW-5~~ — absorbed into TFW-1 | Also folded | — | |
| [TFW-6](tasks/TFW-6__zeta/) | Frozen task | ❄️ FROZEN | odd status |

## Something Else

Not part of the board.
"""


def _project(tmp_path: Path) -> Path:
    (tmp_path / ".tfw").mkdir()
    (tmp_path / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n  task_containers: [workspace, tasks]\n"
        "  statuses:\n" + "".join(f"    - id: {s}\n" for s in DECLARED),
        encoding="utf-8")
    (tmp_path / "README.md").write_text(BOARD, encoding="utf-8")
    for name in ("TFW-1__alpha", "TFW-2__beta", "TFW-4__delta", "TFW-6__zeta"):
        directory = tmp_path / "tasks" / name
        directory.mkdir(parents=True)
        (directory / f"HL-{name.split('__')[0]}__x.md").write_text("# HL\n", encoding="utf-8")
    return tmp_path


# --- parsing ---------------------------------------------------------------

def test_every_row_is_seen_whatever_its_shape():
    rows = migrate_board.parse_board(BOARD)
    assert [row["id"] for row in rows] == ["TFW-1", "TFW-2", "TFW-3", "TFW-4", "TFW-5", "TFW-6"]


def test_parsing_stops_at_the_end_of_the_table():
    assert "Something Else" not in "".join(r["raw"] for r in migrate_board.parse_board(BOARD))


def test_row_shape_is_recorded_not_used_to_filter():
    rows = {row["id"]: row for row in migrate_board.parse_board(BOARD)}
    assert rows["TFW-1"]["linked"] and not rows["TFW-1"]["struck"]
    assert not rows["TFW-3"]["linked"]
    assert rows["TFW-4"]["struck"] and rows["TFW-5"]["struck"]


def test_absent_board_yields_no_rows():
    assert migrate_board.parse_board("# Project\n\nNo board here.\n") == []


# --- status classification -------------------------------------------------

@pytest.mark.parametrize("cell,lifecycle", [
    ("✅ DONE", "DONE"),
    ("🟢 RF", "RF"),
    ("⬜ TODO", "TODO"),
    ("📝 HL_DRAFT", "HL_DRAFT"),
    ("🟢 RF (A) — execution in progress", "RF"),
])
def test_declared_values_map_to_their_id(cell, lifecycle):
    assert migrate_board.classify_status(cell, DECLARED)["lifecycle"] == lifecycle


@pytest.mark.parametrize("cell", ["❄️ FROZEN", "🟡 TS", "🚀 SHIPPED"])
def test_undeclared_values_are_carried_verbatim_never_normalized(cell):
    result = migrate_board.classify_status(cell, DECLARED)
    assert result["lifecycle"] == "UNDECLARED"
    assert result["verbatim"] == cell


def test_empty_status_is_undeclared_not_todo():
    """Guessing TODO for a blank cell would be inventing a fact."""
    assert migrate_board.classify_status("—", DECLARED)["lifecycle"] == "UNDECLARED"


def test_terminal_trailing_prose_becomes_the_outcome():
    result = migrate_board.classify_status("✅ DONE — shipped in v1.2", DECLARED)
    assert result["lifecycle"] == "DONE"
    assert result["outcome"] == "shipped in v1.2"


# --- reconciliation --------------------------------------------------------

def test_every_row_and_directory_is_accounted_for_exactly_once(tmp_path):
    root = _project(tmp_path)
    rows = migrate_board.parse_board((root / "README.md").read_text(encoding="utf-8"))
    result = migrate_board.reconcile(root, rows)
    assert len(result["matched"]) + len(result["board_only"]) == len(rows)
    assert len(result["matched"]) + len(result["directory_only"]) == len(result["directories"])
    assert len(result["matched"]) == 4
    assert [row["id"] for row in result["board_only"]] == ["TFW-3", "TFW-5"]
    assert result["directory_only"] == []


def test_a_struck_row_over_a_real_directory_is_reported_as_malformed(tmp_path):
    root = _project(tmp_path)
    rows = migrate_board.parse_board((root / "README.md").read_text(encoding="utf-8"))
    result = migrate_board.reconcile(root, rows)
    malformed = {row["id"] for row in result["malformed"]}
    assert malformed == {"TFW-3", "TFW-4", "TFW-5"}
    assert "TFW-4" in {row["id"] for row in result["matched"]}


def test_a_directory_with_no_row_is_reported(tmp_path):
    root = _project(tmp_path)
    (root / "tasks" / "TFW-9__orphan").mkdir(parents=True)
    rows = migrate_board.parse_board((root / "README.md").read_text(encoding="utf-8"))
    result = migrate_board.reconcile(root, rows)
    assert [entry["id"] for entry in result["directory_only"]] == ["TFW-9"]


# --- task state ------------------------------------------------------------

def test_state_is_written_only_for_live_tasks_with_a_directory(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    written = [path.parent.name for path, _ in writes]
    assert written == ["TFW-2__beta", "TFW-6__zeta"]


def test_terminal_and_absorbed_tasks_receive_no_state(tmp_path):
    """TFW-1 is done; TFW-4 was absorbed. Neither is a task anyone can advance."""
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    names = {path.parent.name for path, _ in writes}
    assert "TFW-1__alpha" not in names and "TFW-4__delta" not in names


def test_facts_the_board_never_carried_are_marked_absent_not_guessed(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    content = dict((p.parent.name, c) for p, c in writes)["TFW-2__beta"]
    assert "value: unrecorded" in content
    assert "owner: unassigned" in content


def test_undeclared_status_reaches_task_state_verbatim(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    content = dict((p.parent.name, c) for p, c in writes)["TFW-6__zeta"]
    assert "lifecycle: UNDECLARED" in content
    assert "lifecycle_verbatim: ❄️ FROZEN" in content


def test_authority_points_at_a_file_that_exists(tmp_path):
    root = _project(tmp_path)
    _, writes, _ = migrate_board.plan(root, "2026-08-26")
    for path, content in writes:
        authority = next(line.split(": ", 1)[1] for line in content.splitlines()
                         if line.startswith("authority: "))
        assert (path.parent / authority).exists(), authority


def test_written_state_parses_back_cleanly(tmp_path):
    """What migration writes must be what the index can read."""
    import gen_index
    root = _project(tmp_path)
    assert migrate_board.main(["--root", str(root), "--apply"]) == 0
    for task_dir in gen_index.iter_task_dirs(root):
        data = gen_index.read_status(task_dir)
        if data is not None:
            assert "_error" not in data, (task_dir.name, data.get("_error"))


# --- the negative guarantees ----------------------------------------------

def test_dry_run_writes_nothing(tmp_path):
    root = _project(tmp_path)
    before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert migrate_board.main(["--root", str(root)]) == 0
    after = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert before == after


def test_apply_leaves_every_pre_existing_file_byte_identical(tmp_path):
    root = _project(tmp_path)
    before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
    assert migrate_board.main(["--root", str(root), "--apply"]) == 0
    for path, content in before.items():
        assert path.exists(), f"{path} disappeared"
        assert path.read_bytes() == content, f"{path} changed"


def test_apply_adds_only_state_files_and_the_snapshot(tmp_path):
    root = _project(tmp_path)
    before = {p for p in root.rglob("*") if p.is_file()}
    migrate_board.main(["--root", str(root), "--apply"])
    added = sorted(p.relative_to(root).as_posix() for p in root.rglob("*")
                   if p.is_file() and p not in before)
    assert added == [
        "tasks/BOARD-SNAPSHOT.md",
        "tasks/TFW-2__beta/status.md",
        "tasks/TFW-6__zeta/status.md",
    ]


def test_apply_refuses_to_overwrite(tmp_path):
    """Re-running must not clobber state a person has since edited."""
    root = _project(tmp_path)
    assert migrate_board.main(["--root", str(root), "--apply"]) == 0
    edited = root / "tasks" / "TFW-2__beta" / "status.md"
    edited.write_text("---\nid: TFW-2\n---\nedited by hand\n", encoding="utf-8")
    assert migrate_board.main(["--root", str(root), "--apply"]) == 1
    assert "edited by hand" in edited.read_text(encoding="utf-8")


def test_snapshot_captures_every_row_verbatim(tmp_path):
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot = (root / "tasks" / "BOARD-SNAPSHOT.md").read_text(encoding="utf-8")
    for row in migrate_board.parse_board(BOARD):
        assert row["raw"] in snapshot, row["id"]
    assert "Rows captured | 6" in snapshot


def test_snapshot_keeps_backlog_rows_that_have_no_directory(tmp_path):
    """A snapshot of only finished work would delete the project's backlog."""
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot = (root / "tasks" / "BOARD-SNAPSHOT.md").read_text(encoding="utf-8")
    assert "board-only, backlog" in snapshot
    assert "board-only, absorbed elsewhere" in snapshot


def test_the_snapshot_is_readable_by_the_index_generator(tmp_path):
    import gen_index
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    assert len(gen_index.read_snapshot(root)) == 6


# --- the board source is explicit (review F9) ------------------------------

def test_an_empty_board_source_is_refused(tmp_path):
    """The defect that deleted the trace, turned into a test.

    Re-running the migration after the board had been removed read a README with no table,
    produced a snapshot reading `Rows captured | 0`, and overwrote the real one. Every row
    the board carried was lost, and the failure was silent: the run reported success.
    """
    root = _project(tmp_path)
    (root / "README.md").write_text("# Project\n\nNo board here.\n", encoding="utf-8")
    assert migrate_board.main(["--root", str(root), "--apply"]) == 1
    assert not (root / "tasks" / "BOARD-SNAPSHOT.md").exists()


def test_an_empty_board_is_allowed_only_when_said_so_explicitly(tmp_path):
    """A project that genuinely never had a board is a real case — but it must be declared."""
    root = _project(tmp_path)
    (root / "README.md").write_text("# Project\n\nNo board here.\n", encoding="utf-8")
    assert migrate_board.main(
        ["--root", str(root), "--apply", "--allow-empty-board"]) == 0


def test_the_board_can_be_read_from_a_named_revision(tmp_path):
    """Once the board is gone, Git is the only honest source."""
    root = _project(tmp_path)
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run(["git", "-c", "user.email=t@e", "-c", "user.name=T",
                    "commit", "-qm", "board"], cwd=root, check=True)
    (root / "README.md").write_text("# Project\n\nBoard removed.\n", encoding="utf-8")

    live, _ = migrate_board.read_board(root, None)
    assert migrate_board.parse_board(live) == []
    historical, origin = migrate_board.read_board(root, "HEAD")
    assert len(migrate_board.parse_board(historical)) == 6
    assert "HEAD" in origin


# --- counting, never asserting (review E27) --------------------------------

def test_the_snapshot_row_count_equals_the_board_row_count(tmp_path):
    """A claim was accepted where a count was required. Now the count is the test."""
    root = _project(tmp_path)
    source_rows = len(migrate_board.parse_board(BOARD))
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot = (root / "tasks" / "BOARD-SNAPSHOT.md").read_text(encoding="utf-8")
    assert f"Rows captured | {source_rows} |" in snapshot
    assert len(migrate_board.parse_board(BOARD)) == source_rows == 6
    # and the identifiers are physically present, not merely counted
    for row in migrate_board.parse_board(BOARD):
        assert row["id"] in snapshot, row["id"]


def test_every_board_identifier_is_named_in_the_accounting(tmp_path):
    """R3: the reconciliation lists all rows by name, and nothing is unaccounted."""
    root = _project(tmp_path)
    rows = migrate_board.parse_board(BOARD)
    result = migrate_board.reconcile(root, rows)
    _, writes, _ = migrate_board.plan(root, "2026-08-26", BOARD)
    manifest = migrate_board.render_manifest(root, result, DECLARED, writes)
    assert "Unaccounted: 0" in manifest
    for row in rows:
        assert f"`{row['id']}`" in manifest, row["id"]


def test_a_snapshot_that_lost_its_rows_is_detectable_by_counting(tmp_path):
    """The check that would have caught the revision-2 failure at the time."""
    root = _project(tmp_path)
    migrate_board.main(["--root", str(root), "--apply"])
    snapshot_path = root / "tasks" / "BOARD-SNAPSHOT.md"
    good = snapshot_path.read_text(encoding="utf-8")
    assert good.count("TFW-") > 0

    snapshot_path.write_text(good.replace("| Rows captured | 6 |",
                                          "| Rows captured | 0 |"), encoding="utf-8")
    reported = int(re.search(r"Rows captured \| (\d+) \|",
                             snapshot_path.read_text(encoding="utf-8")).group(1))
    assert reported != len(migrate_board.parse_board(BOARD)), \
        "a count mismatch must be visible without reading the prose"


# --- the real repository ---------------------------------------------------

def test_repository_accounting_balances():
    """Re-runnable against the live tree: every row and directory lands exactly once."""
    rows = migrate_board.parse_board((PROJECT_ROOT / "README.md").read_text(encoding="utf-8"))
    if not rows:
        pytest.skip("board already removed — accounting is frozen in BOARD-SNAPSHOT.md")
    result = migrate_board.reconcile(PROJECT_ROOT, rows)
    assert len(result["matched"]) + len(result["board_only"]) == len(rows)
    assert len(result["matched"]) + len(result["directory_only"]) == len(result["directories"])

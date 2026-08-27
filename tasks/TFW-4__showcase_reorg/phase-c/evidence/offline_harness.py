#!/usr/bin/env python3
"""Deterministic offline verification harness for TFW-4 Phase C."""

import copy
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path
from types import ModuleType

PROJECT_ROOT = Path(__file__).resolve().parents[4]
PRE_PHASE_C_REVISION = "4bc1bb159f69e7b5b1923dcc1bf3301bf8fbb710"
PHASE_C_IMPLEMENTATION_REVISION = "172e6ac18c7e604d553c38522650562d416dfb51"
PHASE_C_LIFECYCLE_REVISION = "a141f7c26a9fa3e932a836dceddb74d906e28948"
PRE_PHASE_C_SUBJECT = (
    "[codex/TFW-4/pipeline-tooling/executor] record phase c onboarding"
)
PHASE_C_IMPLEMENTATION_SUBJECT = (
    "[codex/TFW-4/pipeline-tooling/executor] implement phase c tooling"
)


def load_module(name: str, relative_path: str) -> ModuleType:
    """Import one approved project script by repository-relative path."""
    module_path = PROJECT_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not import {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, label: str) -> None:
    """Fail the harness with a precise assertion label."""
    if not condition:
        raise AssertionError(label)


def git_text(*arguments: str) -> str:
    """Return UTF-8 Git output or fail with the exact provenance command."""
    completed = subprocess.run(
        ["git", *arguments],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    require(
        completed.returncode == 0,
        f"git {' '.join(arguments)} must resolve: {completed.stderr.strip()}",
    )
    return completed.stdout


def git_file(revision: str, relative_path: str) -> str:
    """Read one committed UTF-8 file through a content-addressed revision."""
    return git_text("show", f"{revision}:{relative_path}")


def normalize_cell(value: str) -> str:
    """Normalize Markdown table whitespace without weakening its text semantics."""
    return re.sub(r"\s+", " ", value).strip()


def table_cells(line: str) -> tuple[str, ...]:
    """Parse one simple Markdown table row into normalized cells."""
    return tuple(normalize_cell(cell) for cell in line.strip().strip("|").split("|"))


def decision_rows(text: str) -> dict[str, list[tuple[str, str, str]]]:
    """Index decision, rationale, and source cells while retaining duplicates."""
    rows: dict[str, list[tuple[str, str, str]]] = {}
    for line in text.splitlines():
        cells = table_cells(line)
        if not cells or re.fullmatch(r"D\d+", cells[0]) is None:
            continue
        require(len(cells) == 4, f"{cells[0]} must have four table cells")
        rows.setdefault(cells[0], []).append((cells[1], cells[2], cells[3]))
    return rows


def one_decision(
    rows: dict[str, list[tuple[str, str, str]]], decision_id: str
) -> tuple[str, str, str]:
    """Return one uniquely keyed decision row."""
    require(len(rows.get(decision_id, [])) == 1, f"{decision_id} once")
    return rows[decision_id][0]


def validate_decision_contract(
    current: str,
    predecessor: str,
    phase_c: str,
) -> None:
    """Validate AC-6 decisions against committed semantic provenance."""
    predecessor_rows = decision_rows(predecessor)
    phase_c_rows = decision_rows(phase_c)
    current_rows = decision_rows(current)
    require(
        set(predecessor_rows) == {f"D{number}" for number in range(1, 13)},
        "pre-Phase-C provenance must contain exactly D1-D12",
    )
    require(
        set(phase_c_rows) == {f"D{number}" for number in range(1, 15)},
        "Phase C implementation provenance must contain exactly D1-D14",
    )
    for number in range(1, 13):
        decision_id = f"D{number}"
        expected = one_decision(predecessor_rows, decision_id)
        require(
            one_decision(phase_c_rows, decision_id) == expected,
            f"{decision_id} implementation provenance must preserve predecessor meaning",
        )
        require(
            one_decision(current_rows, decision_id) == expected,
            f"{decision_id} must preserve predecessor meaning",
        )
    for number in (13, 14):
        decision_id = f"D{number}"
        require(
            one_decision(current_rows, decision_id)
            == one_decision(phase_c_rows, decision_id),
            f"{decision_id} must preserve Phase C meaning",
        )
    require(not current_rows.get("D15"), "D15 must remain absent")


def replace_decision_rows(
    text: str, decision_id: str, replacement: list[str]
) -> str:
    """Replace all rows for one decision while preserving unrelated documentation."""
    output: list[str] = []
    inserted = False
    for line in text.splitlines():
        cells = table_cells(line)
        if cells and cells[0] == decision_id:
            if not inserted:
                output.extend(replacement)
                inserted = True
            continue
        output.append(line)
    require(inserted, f"fixture source must contain {decision_id}")
    return "\n".join(output) + "\n"


def expect_decision_rejection(
    label: str,
    fixture: str,
    predecessor: str,
    phase_c: str,
) -> None:
    """Require a malformed decision fixture to fail the semantic contract."""
    try:
        validate_decision_contract(fixture, predecessor, phase_c)
    except AssertionError:
        print(f"[PASS] decision fixture {label}: rejected")
    else:
        raise AssertionError(f"decision fixture {label} must reject")


def debt_rows(text: str) -> dict[str, dict[str, list[tuple[str, ...]]]]:
    """Index open/resolved debt rows while retaining duplicate identifiers."""
    rows: dict[str, dict[str, list[tuple[str, ...]]]] = {
        "open": {},
        "resolved": {},
    }
    section: str | None = None
    for line in text.splitlines():
        if line == "## Open Items":
            section = "open"
            continue
        if line == "## Resolved":
            section = "resolved"
            continue
        if line.startswith("## "):
            section = None
            continue
        cells = table_cells(line)
        if section is None or not cells or re.fullmatch(r"TD-\d+", cells[0]) is None:
            continue
        rows[section].setdefault(cells[0], []).append(cells[1:])
    return rows


def unique_debt_rows(
    rows: dict[str, dict[str, list[tuple[str, ...]]]]
) -> dict[str, tuple[str, tuple[str, ...]]]:
    """Flatten keyed debt rows and reject duplicates across lifecycle sections."""
    flattened: dict[str, tuple[str, tuple[str, ...]]] = {}
    for section in ("open", "resolved"):
        for debt_id, matches in rows[section].items():
            require(len(matches) == 1, f"{debt_id} once in {section}")
            require(debt_id not in flattened, f"{debt_id} must occur in one debt section")
            flattened[debt_id] = (section, matches[0])
    return flattened


def validate_debt_contract(
    current: str,
    predecessor: str,
    phase_c: str,
    lifecycle: str,
) -> None:
    """Validate Phase C debt transitions without coupling unrelated prose."""
    predecessor_rows = unique_debt_rows(debt_rows(predecessor))
    phase_c_rows = unique_debt_rows(debt_rows(phase_c))
    lifecycle_rows = unique_debt_rows(debt_rows(lifecycle))
    current_rows = unique_debt_rows(debt_rows(current))
    require(set(phase_c_rows) == set(predecessor_rows), "Phase C debt ID set")
    for debt_id, expected in predecessor_rows.items():
        if debt_id in {"TD-3", "TD-6"}:
            continue
        require(phase_c_rows[debt_id] == expected, f"{debt_id} must not transition")
    for debt_id in ("TD-3", "TD-6"):
        section, cells = phase_c_rows[debt_id]
        require(section == "resolved", f"{debt_id} must transition to resolved")
        require("RESOLVED" in cells[0], f"{debt_id} resolved semantics")
    for debt_id, expected in phase_c_rows.items():
        require(current_rows.get(debt_id) == expected, f"{debt_id} Phase C state")
    for debt_id in ("TD-5", "TD-10", "TD-11"):
        if debt_id not in current_rows:
            continue
        section, cells = current_rows[debt_id]
        require(section == "open", f"{debt_id} must remain open")
        require(len(cells) == 5, f"{debt_id} open-row shape")
        require(cells[2] == "Medium", f"{debt_id} must remain Medium")
        require(cells[3].endswith("OPEN"), f"{debt_id} open disposition")
    missing_later_debt = {"TD-10", "TD-11"} - set(current_rows)
    if missing_later_debt:
        require(
            current_rows == lifecycle_rows,
            "a revision without later review debt must match the fixed lifecycle provenance",
        )


def expect_debt_rejection(
    label: str,
    fixture: str,
    predecessor: str,
    phase_c: str,
    lifecycle: str,
) -> None:
    """Require a malformed debt fixture to fail the keyed transition contract."""
    try:
        validate_debt_contract(fixture, predecessor, phase_c, lifecycle)
    except AssertionError:
        print(f"[PASS] debt fixture {label}: rejected")
    else:
        raise AssertionError(f"debt fixture {label} must reject")


def archived_group(data: dict) -> dict:
    """Build a valid archived group from production-shaped data."""
    entry = copy.deepcopy(data["groups"][0])
    entry.update(
        {
            "type": "groups",
            "died_on": "2026-08-27",
            "reason": "Independent evidence identifies the historical group as closed.",
        }
    )
    return entry


def run_schema_matrix(schema: ModuleType, production: dict) -> None:
    """Exercise the AC-1 positive and negative schema matrix in memory."""
    errors, freshness = schema.validate_data(
        copy.deepcopy(production), today=date(2026, 8, 27)
    )
    require(not errors, "production catalog must validate")
    require(freshness["oldest_live"] == "2026-01-30", "oldest date must be dynamic")
    require(freshness["stale_count"] == 63, "all production entries must report stale")

    fixtures: list[tuple[str, dict, str]] = []

    missing_north_star = copy.deepcopy(production)
    missing_north_star.pop("north_star")
    fixtures.append(("missing_north_star", missing_north_star, "north_star"))

    empty_purpose = copy.deepcopy(production)
    empty_purpose["north_star"]["purpose"] = "  "
    fixtures.append(("empty_purpose", empty_purpose, "purpose"))

    empty_non_goals = copy.deepcopy(production)
    empty_non_goals["north_star"]["non_goals"] = []
    fixtures.append(("empty_non_goals", empty_non_goals, "non_goals"))

    malformed_archive_date = copy.deepcopy(production)
    malformed = archived_group(malformed_archive_date)
    malformed["died_on"] = "2026-02-30"
    malformed_archive_date["groups"] = malformed_archive_date["groups"][1:]
    malformed_archive_date["archive"] = [malformed]
    fixtures.append(("malformed_archive_date", malformed_archive_date, "died_on"))

    empty_reason = copy.deepcopy(production)
    empty_reason_entry = archived_group(empty_reason)
    empty_reason_entry["reason"] = ""
    empty_reason["groups"] = empty_reason["groups"][1:]
    empty_reason["archive"] = [empty_reason_entry]
    fixtures.append(("empty_reason", empty_reason, "reason"))

    wrong_type = copy.deepcopy(production)
    wrong_type_entry = archived_group(wrong_type)
    wrong_type_entry["type"] = "forums"
    wrong_type["groups"] = wrong_type["groups"][1:]
    wrong_type["archive"] = [wrong_type_entry]
    fixtures.append(("wrong_type", wrong_type, "type"))

    missing_type_field = copy.deepcopy(production)
    missing_field_entry = archived_group(missing_type_field)
    missing_field_entry.pop("category")
    missing_type_field["groups"] = missing_type_field["groups"][1:]
    missing_type_field["archive"] = [missing_field_entry]
    fixtures.append(("missing_type_field", missing_type_field, "category"))

    collision = copy.deepcopy(production)
    collision["archive"] = [archived_group(collision)]
    fixtures.append(("archive_live_collision", collision, "live catalog"))

    for label, fixture, expected_fragment in fixtures:
        fixture_errors, _ = schema.validate_data(fixture, today=date(2026, 8, 27))
        require(bool(fixture_errors), f"{label} must fail")
        require(
            any(expected_fragment in error for error in fixture_errors),
            f"{label} must report {expected_fragment}",
        )
        print(f"[PASS] schema fixture {label}: rejected")

    valid_archive = copy.deepcopy(production)
    valid_entry = archived_group(valid_archive)
    valid_archive["groups"] = valid_archive["groups"][1:]
    valid_archive["archive"] = [valid_entry]
    valid_errors, valid_freshness = schema.validate_data(
        valid_archive, today=date(2026, 8, 27)
    )
    require(not valid_errors, "valid stale archive fixture must pass")
    require(valid_freshness["stale_count"] == 62, "staleness must remain non-fatal")
    print("[PASS] schema fixture valid_stale_archive: accepted with freshness warning")


def preview_html(
    handle: str,
    visible_name: str,
    extra: str,
    action: str,
) -> str:
    """Return a sanitized target-preview fixture."""
    return f"""<!doctype html>
<html><head><meta property="og:url" content="https://t.me/{handle}"></head>
<body><div class="tgme_page_title"><span>{visible_name}</span></div>
<div class="tgme_page_extra">{extra}</div>
<div class="tgme_page_description">Synthetic target description</div>
<a class="tgme_action_button_new" href="tg://resolve?domain={handle}">{action}</a>
</body></html>"""


def observed(
    links: ModuleType,
    classification: str,
    entry_type: str,
    count: int | None,
    reason: str,
) -> dict:
    """Create a deterministic observation for summary/update checks."""
    return links.result(
        classification,
        reason,
        entry_type,
        member_count=count,
        visible_name="Synthetic Target",
        observed_type=entry_type if classification == "verified" else None,
        target_bound=classification == "verified",
    )


def run_link_matrix(links: ModuleType) -> None:
    """Exercise AC-2 classification, summary, update, and archive behavior."""
    c3 = preview_html("SampleBot", "Sample Bot", "@SampleBot", "Send Message")
    c4 = "<html><head><title>Telegram: Contact @SampleBot</title></head><body></body></html>"
    c5 = "<html><head><title>Telegram</title></head><body>Groups can hold up to 200,000 members.</body></html>"
    group_count = preview_html(
        "sample_group", "Sample Group", "1 234 members, 56 online", "View in Telegram"
    )
    identity_decoy = """<!doctype html>
<html><head>
<link rel="canonical" href="https://t.me/other_group">
<meta property="og:url" content="https://t.me/other_group">
</head><body>
<div class="tgme_page_title">Other Group</div>
<div class="tgme_page_extra">500 members</div>
<div class="tgme_page_description">
  Synthetic description with unrelated <a href="https://t.me/requested_group">link</a>
</div>
<a class="tgme_action_button_new" href="tg://resolve?domain=other_group">View in Telegram</a>
</body></html>"""
    authoritative_conflict = """<!doctype html>
<html><head>
<link rel="canonical" href="https://t.me/requested_group">
<meta property="og:url" content="https://t.me/requested_group">
</head><body>
<div class="tgme_page_title">Conflicting Group</div>
<div class="tgme_page_extra">500 members</div>
<a class="tgme_action_button_new" href="tg://resolve?domain=other_group">View in Telegram</a>
</body></html>"""
    explicit_failure = '<html><body><div class="tgme_page_error">Not found</div></body></html>'

    cases = {
        "C3": links.classify_response(c3, "SampleBot", "bots"),
        "C4": links.classify_response(c4, "SampleBot", "bots"),
        "C5": links.classify_response(c5, "sample_group", "groups"),
        "count": links.classify_response(group_count, "sample_group", "groups"),
        "identity_decoy": links.classify_response(
            identity_decoy, "requested_group", "groups"
        ),
        "authoritative_conflict": links.classify_response(
            authoritative_conflict, "requested_group", "groups"
        ),
        "failure": links.classify_response(explicit_failure, "sample_group", "groups"),
        "type_mismatch": links.classify_response(group_count, "sample_group", "channels"),
    }
    require(cases["C3"]["classification"] == "verified", "C3 must verify")
    require(cases["C3"]["member_count"] is None, "C3 count must remain absent")
    require(cases["C4"]["classification"] == "ambiguous", "C4 must be ambiguous")
    require(cases["C5"]["classification"] == "non_target", "C5 must be non-target")
    require(cases["C5"]["member_count"] is None, "C5 site-wide prose must not parse")
    require(cases["count"]["classification"] == "verified", "count preview must verify")
    require(cases["count"]["member_count"] == 1234, "target count must parse")
    require(
        cases["identity_decoy"]["classification"] == "non_target",
        "description link must not override canonical/action target identity",
    )
    require(
        not cases["identity_decoy"]["target_bound"],
        "description link must not bind the requested target",
    )
    require(
        cases["identity_decoy"]["member_count"] is None,
        "foreign preview count must not be exposed",
    )
    require(
        cases["authoritative_conflict"]["classification"] == "ambiguous",
        "conflicting canonical/action identities must be ambiguous",
    )
    require(
        not cases["authoritative_conflict"]["target_bound"]
        and cases["authoritative_conflict"]["member_count"] is None,
        "conflicting authoritative identities must not expose target facts",
    )
    require(cases["failure"]["classification"] == "failed", "error marker must fail")
    require(
        cases["type_mismatch"]["classification"] == "ambiguous",
        "declared type mismatch must not verify",
    )
    require(
        all(not case["archive_candidate"] for case in cases.values()),
        "classifier results must never auto-authorize archive",
    )
    for label, case in cases.items():
        print(
            f"[PASS] link fixture {label}: {case['classification']}; "
            f"count={case['member_count']}"
        )

    requested_entry = {
        "name": "Requested Group",
        "handle": "requested_group",
        "description": "Synthetic requested target",
        "category": "general",
        "member_count": 10,
        "last_verified": "2026-01-30",
    }
    identity_decoy_record = links.enrich_result(
        "groups", requested_entry, cases["identity_decoy"]
    )
    identity_decoy_data = {
        "meta": {"last_updated": "2026-01-30"},
        "groups": [copy.deepcopy(requested_entry)],
        "channels": [],
        "bots": [],
        "archive": [],
    }
    identity_decoy_updates = links.apply_updates(
        identity_decoy_data, [identity_decoy_record], "2026-08-27"
    )
    require(
        identity_decoy_updates == {"dates_updated": 0, "counts_updated": 0},
        "identity decoy must not produce entry updates",
    )
    require(
        identity_decoy_data["groups"][0] == requested_entry,
        "identity decoy must not mutate requested target fields",
    )
    print("[PASS] conflicting identity does not mutate requested target")

    entries = [
        ("groups", {"name": "Grew", "handle": "grew1", "member_count": 100, "last_verified": "2026-01-30"}, observed(links, "verified", "groups", 110, "target_preview_verified")),
        ("groups", {"name": "Shrank", "handle": "shrank1", "member_count": 100, "last_verified": "2026-01-30"}, observed(links, "verified", "groups", 90, "target_preview_verified")),
        ("groups", {"name": "Same", "handle": "same1", "member_count": 100, "last_verified": "2026-01-30"}, observed(links, "verified", "groups", 100, "target_preview_verified")),
        ("groups", {"name": "First", "handle": "first1", "last_verified": "2026-01-30"}, observed(links, "verified", "groups", 50, "target_preview_verified")),
        ("bots", {"name": "No Count", "handle": "nocount1", "last_verified": "2026-01-30"}, observed(links, "verified", "bots", None, "target_preview_verified")),
        ("groups", {"name": "Ambiguous", "handle": "ambiguous1", "member_count": 7, "last_verified": "2026-01-30"}, observed(links, "ambiguous", "groups", None, "contact_shell_without_preview")),
        ("groups", {"name": "Failed", "handle": "failed1", "member_count": 8, "last_verified": "2026-01-30"}, observed(links, "failed", "groups", None, "http_404")),
    ]
    records = [
        links.enrich_result(entry_type, entry, observation)
        for entry_type, entry, observation in entries
    ]
    summary = links.build_summary(records, "2026-08-27")
    require(summary["schema_version"] == 1, "summary schema version")
    for outcome in ("grew", "shrank", "unchanged", "first_count"):
        require(summary["totals"][outcome] == 1, f"summary {outcome} total")
    require(summary["totals"]["verified"] == 5, "summary verified total")
    require(summary["totals"]["ambiguous"] == 1, "summary ambiguous total")
    require(summary["totals"]["failed"] == 1, "summary failed total")
    require(summary["totals"]["member_delta"] == 0, "summary signed delta")
    with tempfile.TemporaryDirectory(prefix="tfw4-link-summary-") as temporary_directory:
        summary_path = Path(temporary_directory) / "summary.json"
        links.write_summary(summary, summary_path)
        with summary_path.open("r", encoding="utf-8") as source:
            require(json.load(source) == summary, "machine summary JSON round trip")

    temporary_data = {
        "meta": {"last_updated": "2026-01-30"},
        "groups": [copy.deepcopy(entry) for kind, entry, _ in entries if kind == "groups"],
        "channels": [],
        "bots": [copy.deepcopy(entry) for kind, entry, _ in entries if kind == "bots"],
        "archive": [],
    }
    updates = links.apply_updates(temporary_data, records, "2026-08-27")
    temporary_index = {
        entry["handle"]: entry
        for kind in ("groups", "channels", "bots")
        for entry in temporary_data[kind]
    }
    require(updates == {"dates_updated": 5, "counts_updated": 3}, "update counters")
    require(temporary_index["nocount1"]["last_verified"] == "2026-08-27", "no-count date")
    require("member_count" not in temporary_index["nocount1"], "no-count must stay absent")
    require(temporary_index["ambiguous1"]["last_verified"] == "2026-01-30", "C4 no date")
    require(temporary_index["failed1"]["last_verified"] == "2026-01-30", "failure no date")
    require(temporary_data["meta"]["last_updated"] == "2026-08-27", "meta update date")
    print("[PASS] link summary and update matrix")

    archive_data = {
        "meta": {"last_updated": "2026-01-30"},
        "groups": [
            {
                "name": "Archived Group",
                "handle": "archive1",
                "description": "Synthetic archive input",
                "category": "general",
                "last_verified": "2026-01-30",
                "member_count": 12,
            }
        ],
        "channels": [],
        "bots": [],
        "archive": [],
    }
    for label, kwargs in (
        ("missing_owner", {"owner_approved": False, "evidence_reference": "EV row"}),
        ("missing_evidence", {"owner_approved": True, "evidence_reference": ""}),
    ):
        try:
            links.archive_entry(
                copy.deepcopy(archive_data),
                "archive1",
                "Independent evidence proves closure.",
                "2026-08-27",
                kwargs["evidence_reference"],
                kwargs["owner_approved"],
            )
        except ValueError:
            print(f"[PASS] archive guard {label}: rejected")
        else:
            raise AssertionError(f"archive guard {label} must reject")

    original_entry = copy.deepcopy(archive_data["groups"][0])
    archived = links.archive_entry(
        archive_data,
        "ARCHIVE1",
        "Independent evidence proves closure.",
        "2026-08-27",
        "EV synthetic closure row",
        True,
    )
    require(not archive_data["groups"], "archive move removes the live placement")
    require(len(archive_data["archive"]) == 1, "archive move retains one record")
    for key, value in original_entry.items():
        require(archived[key] == value, f"archive must preserve {key}")
    require(archived["type"] == "groups", "archive type")
    require(archived["died_on"] == "2026-08-27", "archive died_on")
    require(bool(archived["reason"]), "archive reason")
    print("[PASS] explicit archive move and preservation")

    protected_constants = (3, 1.5, 0.3, 3, 2.0, 15)
    actual_constants = (
        links.BATCH_SIZE,
        links.BATCH_DELAY,
        links.REQUEST_DELAY,
        links.RETRY_ATTEMPTS,
        links.RETRY_BACKOFF,
        links.TIMEOUT,
    )
    require(actual_constants == protected_constants, "rate/retry constants must remain unchanged")
    print("[PASS] AC-2 offline classifier/update/archive matrix")


def run_generator_matrix(generator: ModuleType, links: ModuleType, production: dict) -> None:
    """Exercise AC-3 rendering, anchors, archive, and currency checks."""
    rendered = generator.generate_readme(copy.deepcopy(production))
    lines = rendered.splitlines()
    expected_stats = (
        f"**{len(production['groups'])}** groups · "
        f"**{len(production['channels'])}** channels · "
        f"**{len(production['bots'])}** bots · "
        f"**{len(production['categories'])}** categories · "
        f"verified **{min(entry['last_verified'] for kind in ('groups', 'channels', 'bots') for entry in production[kind])}**"
    )
    stats_index = lines.index(expected_stats)
    require(lines[stats_index + 2] == "## Purpose", "Purpose must immediately follow stats")
    require(production["north_star"]["purpose"] in lines, "exact purpose text")
    for non_goal in production["north_star"]["non_goals"]:
        require(f"- {non_goal}" in lines, f"exact non-goal: {non_goal}")

    category_order = generator.ordered_categories(
        production["groups"], production["categories"]
    )
    display_order = [production["categories"][key] for key in category_order]
    require(
        display_order.index("Engineering Management")
        < display_order.index("Game Development")
        < display_order.index("General"),
        "display-name category order",
    )
    for display_name in display_order:
        slug = generator.github_slug(display_name)
        require(f"  - [{display_name}](#{slug})" in lines, f"TOC anchor {display_name}")
        require(f"### {display_name}" in lines, f"heading {display_name}")
    used = set(category_order)
    for key, display_name in production["categories"].items():
        if key not in used:
            require(f"### {display_name}" not in lines, f"unused heading {display_name}")
            require(f"](#{generator.github_slug(display_name)})" not in rendered, f"unused anchor {display_name}")

    require("- [Archive](#archive)" not in lines, "empty archive TOC omission")
    require("## Archive" not in lines, "empty archive section omission")
    archive_fixture = copy.deepcopy(production)
    source_entry = copy.deepcopy(archive_fixture["groups"][0])
    links.archive_entry(
        archive_fixture,
        source_entry["handle"],
        "Independent evidence identifies the historical group as closed.",
        "2026-08-27",
        "EV synthetic archive row",
        True,
    )
    archive_rendered = generator.generate_readme(archive_fixture)
    for fragment in (
        "- [Archive](#archive)",
        "## Archive",
        "<details>",
        "Archived communities (1)",
        source_entry["name"],
        source_entry["description"],
        str(source_entry["member_count"]),
        source_entry["last_verified"],
        "2026-08-27",
        "Independent evidence identifies the historical group as closed.",
    ):
        require(fragment in archive_rendered, f"archive render fragment: {fragment}")

    for entry_type in ("groups", "channels", "bots"):
        for entry in production[entry_type]:
            require(generator.format_entry(entry) in rendered, f"live render {entry['handle']}")

    production_readme = PROJECT_ROOT / "README.md"
    require(generator.is_current(rendered, production_readme), "production README currency")
    with tempfile.TemporaryDirectory(prefix="tfw4-phase-c-") as temporary_directory:
        candidate = Path(temporary_directory) / "README.md"
        candidate.write_text(rendered.replace("\n", "\r\n"), encoding="utf-8", newline="")
        require(generator.is_current(rendered, candidate), "CRLF-normalized currency")
        stale = candidate.read_text(encoding="utf-8").replace("## Purpose", "## Changed", 1)
        candidate.write_text(stale, encoding="utf-8", newline="")
        before_check = candidate.read_bytes()
        require(not generator.is_current(rendered, candidate), "stale README rejection")
        require(candidate.read_bytes() == before_check, "currency check must not mutate")
        completed = subprocess.run(
            [
                sys.executable,
                str(PROJECT_ROOT / "scripts" / "generate_readme.py"),
                "--check",
                "--readme",
                str(candidate),
            ],
            cwd=PROJECT_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        require(completed.returncode == 1, "stale CLI check exit")
        require(candidate.read_bytes() == before_check, "stale CLI check must not mutate")

    source_text = (PROJECT_ROOT / "scripts" / "generate_readme.py").read_text(encoding="utf-8")
    require("from datetime import" not in source_text, "unused datetime import removed")
    print("[PASS] AC-3 offline README render and currency matrix")


def ordered_markers(text: str, markers: list[str], label: str) -> None:
    """Require markers to occur once in the declared operational order."""
    cursor = -1
    for marker in markers:
        position = text.find(marker, cursor + 1)
        require(position > cursor, f"{label} missing/out-of-order marker: {marker}")
        cursor = position


def resolve_local_markdown_links(path: Path, text: str) -> None:
    """Require every local Markdown link in one command document to resolve."""
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if re.match(r"^[a-z]+://", target, re.IGNORECASE) or target.startswith("#"):
            continue
        target_path = target.split("#", 1)[0]
        require((path.parent / target_path).resolve().exists(), f"unresolved link {target} in {path}")


def run_command_matrix() -> None:
    """Exercise AC-4 static command completeness and protected adapter state."""
    stats_path = PROJECT_ROOT / ".claude" / "commands" / "kz-stats.md"
    release_path = PROJECT_ROOT / ".claude" / "commands" / "kz-release.md"
    stats = stats_path.read_text(encoding="utf-8")
    release = release_path.read_text(encoding="utf-8")
    require(stats.startswith("---\n"), "kz-stats front matter")
    require(release.startswith("---\n"), "kz-release front matter")
    require("**Mode:** CL" in stats and "**Mode:** CL" in release, "CL mode declarations")
    ordered_markers(
        stats,
        [
            "python scripts/validate_schema.py",
            "python scripts/validate_links.py --update --summary-json",
            "grew",
            "python scripts/validate_links.py --handle",
            "Use browser evidence only as a bounded fallback",
            "Verify current target",
            "Repair live link",
            "Archive proven death",
            "Unresolved",
            "python scripts/generate_readme.py",
            "python scripts/generate_readme.py --check",
            "Do not create a release commit",
        ],
        "kz-stats",
    )
    for marker in (
        "requested handle, visible name, declared type",
        "generic Telegram landing/contact shell is not evidence",
        "Reuse one temporary Chrome tab sequentially",
        "Close the temporary tab",
        "Owner approval alone is not death evidence",
        "--evidence-ref",
        "--owner-approved",
    ):
        require(marker in stats, f"kz-stats requirement: {marker}")

    operation = release[release.index("## Operation"):]
    ordered_markers(
        operation,
        [
            "Establish the proposed snapshot",
            "python scripts/validate_schema.py",
            "python scripts/generate_readme.py --check",
            "Prepare the root changelog",
            "Prepare a truthful, path-scoped snapshot commit",
            "Hard stop before external release state",
            "Only after explicit current approval",
            "Create the annotated `data-YYYY-MM-DD` tag",
            "Push only the approved branch commit and tag",
        ],
        "kz-release",
    )
    for marker in (
        "stale or hand-edited",
        "any unresolved entry",
        "conflicting existing tag",
        "actual lowercase executing product",
        "Without an affirmative owner response",
        "Prior approvals do not satisfy this gate",
    ):
        require(marker in release, f"kz-release refusal/gate: {marker}")

    resolve_local_markdown_links(stats_path, stats)
    resolve_local_markdown_links(release_path, release)
    framework_commands = sorted(
        (PROJECT_ROOT / ".claude" / "commands").glob("tfw-*.md"),
        key=lambda path: path.name,
    )
    rows = [f"{path.name}\t{hashlib.sha256(path.read_bytes()).hexdigest()}" for path in framework_commands]
    aggregate = hashlib.sha256((("\n".join(rows)) + "\n").encode("utf-8")).hexdigest()
    require(len(framework_commands) == 12, "framework command count")
    require(
        aggregate == "288fde38245a27073e9b703af05c2f936a31418f3206aff42b475eb39be933ce",
        "framework command aggregate must match ONB",
    )
    print("[PASS] AC-4 project command and framework-adapter matrix")


def run_ci_matrix() -> None:
    """Exercise AC-5 workflow triggers, commands, and offline-only boundary."""
    workflow_path = PROJECT_ROOT / ".github" / "workflows" / "validate.yml"
    workflow = workflow_path.read_text(encoding="utf-8")
    for pattern in (
        r"(?m)^on:$",
        r"(?m)^  pull_request:$",
        r"(?m)^  push:$",
        r"(?m)^      - master$",
        r"actions/checkout@v4",
        r"actions/setup-python@v5",
        r'python-version: "3\.12"',
        r"run: python scripts/validate_schema\.py",
        r"run: python scripts/generate_readme\.py --check",
    ):
        require(re.search(pattern, workflow) is not None, f"CI pattern: {pattern}")
    for forbidden in (
        "validate_links.py",
        "t.me/",
        "browser",
        "kz-release",
        "git tag",
        "git push",
        "secrets.",
        "python scripts/generate_readme.py\n",
    ):
        require(forbidden not in workflow, f"CI forbidden content: {forbidden}")

    yaml_spec = importlib.util.find_spec("yaml")
    if yaml_spec is not None:
        yaml = importlib.import_module("yaml")
        parsed = yaml.safe_load(workflow)
        require(isinstance(parsed, dict), "CI YAML parser result")
        print("[PASS] CI YAML parsed with available local PyYAML")
    else:
        print("[INFO] Optional YAML parser unavailable; structural checks used")
    print("[PASS] AC-5 offline CI definition matrix")


def run_memory_matrix() -> None:
    """Exercise AC-6 keyed decision and debt transitions."""
    require(
        git_text("show", "-s", "--format=%s", PRE_PHASE_C_REVISION).strip()
        == PRE_PHASE_C_SUBJECT,
        "pre-Phase-C provenance subject",
    )
    require(
        git_text(
            "show", "-s", "--format=%s", PHASE_C_IMPLEMENTATION_REVISION
        ).strip()
        == PHASE_C_IMPLEMENTATION_SUBJECT,
        "Phase C implementation provenance subject",
    )
    require(
        git_text(
            "rev-parse", f"{PHASE_C_IMPLEMENTATION_REVISION}^"
        ).strip()
        == PRE_PHASE_C_REVISION,
        "Phase C implementation must descend directly from the onboarding predecessor",
    )
    knowledge = (PROJECT_ROOT / "KNOWLEDGE.md").read_text(encoding="utf-8")
    predecessor_knowledge = git_file(PRE_PHASE_C_REVISION, "KNOWLEDGE.md")
    phase_c_knowledge = git_file(PHASE_C_IMPLEMENTATION_REVISION, "KNOWLEDGE.md")
    validate_decision_contract(knowledge, predecessor_knowledge, phase_c_knowledge)

    decision_lines = knowledge.splitlines()
    d2_line = next(line for line in decision_lines if table_cells(line)[:1] == ("D2",))
    d3_line = next(line for line in decision_lines if table_cells(line)[:1] == ("D3",))
    d14_line = next(line for line in decision_lines if table_cells(line)[:1] == ("D14",))
    decision_fixtures = {
        "removed_D1": replace_decision_rows(knowledge, "D1", []),
        "duplicated_D2": replace_decision_rows(knowledge, "D2", [d2_line, d2_line]),
        "meaning_changed_D3": replace_decision_rows(
            knowledge,
            "D3",
            [d3_line.replace("Rate limiting", "No rate limiting", 1)],
        ),
        "missing_D13": replace_decision_rows(knowledge, "D13", []),
        "duplicated_D14": replace_decision_rows(knowledge, "D14", [d14_line, d14_line]),
        "premature_D15": knowledge
        + "\n| D15 | Premature Phase D decision | Synthetic invalid fixture | N/A |\n",
    }
    for label, fixture in decision_fixtures.items():
        expect_decision_rejection(
            label, fixture, predecessor_knowledge, phase_c_knowledge
        )
    validate_decision_contract(
        knowledge
        + "\n## Synthetic unrelated documentation\n\nThis text must not affect AC-6.\n",
        predecessor_knowledge,
        phase_c_knowledge,
    )
    print("[PASS] unrelated KNOWLEDGE documentation is outside the decision oracle")

    debt = (PROJECT_ROOT / "TECH_DEBT.md").read_text(encoding="utf-8")
    predecessor_debt = git_file(PRE_PHASE_C_REVISION, "TECH_DEBT.md")
    phase_c_debt = git_file(PHASE_C_IMPLEMENTATION_REVISION, "TECH_DEBT.md")
    lifecycle_debt = git_file(PHASE_C_LIFECYCLE_REVISION, "TECH_DEBT.md")
    validate_debt_contract(debt, predecessor_debt, phase_c_debt, lifecycle_debt)
    debt_lines = debt.splitlines()
    td5_line = next(line for line in debt_lines if table_cells(line)[:1] == ("TD-5",))
    td6_line = next(line for line in debt_lines if table_cells(line)[:1] == ("TD-6",))
    expect_debt_rejection(
        "changed_TD5",
        debt.replace(td5_line, td5_line.replace("OPEN", "RESOLVED", 1), 1),
        predecessor_debt,
        phase_c_debt,
        lifecycle_debt,
    )
    expect_debt_rejection(
        "removed_TD6_resolution",
        debt.replace(td6_line + "\n", "", 1),
        predecessor_debt,
        phase_c_debt,
        lifecycle_debt,
    )
    print("[PASS] AC-6 decision and debt matrix")


def main() -> int:
    """Run the currently implemented Phase C offline gates."""
    schema = load_module("phase_c_validate_schema", "scripts/validate_schema.py")
    links = load_module("phase_c_validate_links", "scripts/validate_links.py")
    generator = load_module("phase_c_generate_readme", "scripts/generate_readme.py")
    with (PROJECT_ROOT / "data" / "communities.json").open(
        "r", encoding="utf-8"
    ) as source:
        production = json.load(source)

    run_schema_matrix(schema, production)
    print("[PASS] AC-1 offline schema matrix")
    run_link_matrix(links)
    run_generator_matrix(generator, links, production)
    run_command_matrix()
    run_ci_matrix()
    run_memory_matrix()
    return 0


if __name__ == "__main__":
    sys.exit(main())

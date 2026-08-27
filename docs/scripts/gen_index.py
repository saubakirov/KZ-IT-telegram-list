"""Generate the derived portfolio index.

The index is a **projection**. Task state lives in each task's own ``status.md`` and is the
only authority for that task; this file rebuilds a browsable view of all of them and can be
deleted at any time without losing a fact.

Determinism is a hard requirement: the same inputs must produce the same bytes. Every
ordering here is an explicit sort by a declared key. Directory iteration order is never
inherited, and the freshness stamp is derived from the inputs rather than the wall clock,
so two runs a minute apart are identical.

This module is also the canonical home of the shared task resolver — ``parse_identifier``,
``read_config``, ``iter_task_dirs`` and ``read_status`` — which ``migrate_board.py`` and
``gen_docs.py`` import rather than pattern-matching per call site.

Usage:
    python docs/scripts/gen_index.py [--check]

    --check   write nothing; exit 1 if the committed index differs from what would be
              generated. Intended for the build gate.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Shared task resolver
# ---------------------------------------------------------------------------

#: Clock-derived identifier, TFW 2.0.0: the WHOLE directory name, ``YYYYMMDD-HHMMSS__slug``.
#: The timestamp alone is not an identifier — two mutually offline participants can reach
#: the same second, and only the slug distinguishes them. Two who reach the same second AND
#: the same slug created the same task, which is a signal rather than a collision to prevent.
CLOCK_ID = re.compile(r"^(?P<stamp>\d{8}-\d{6})__(?P<slug>.+)$")

#: A bare timestamp. Never a valid identifier; matched only so consumers can say why.
BARE_STAMP = re.compile(r"^\d{8}-\d{6}$")

#: Legacy identifier grammar: ``{PREFIX}-{seq}``, optionally followed by a slug.
LEGACY_ID = re.compile(r"^(?P<prefix>[A-Z][A-Z0-9]*)-(?P<seq>\d+)(?:__(?P<slug>.+))?$")

#: Directory name: ``<identifier>__<slug>`` for legacy, ``<identifier>`` for clock.
TASK_DIR = re.compile(r"^(?P<id>[^_]+(?:_[^_]+)*?)__(?P<slug>.+)$")

NEWLINE = chr(10)

#: A leading YAML front-matter block.
FRONT_MATTER = re.compile("^---" + chr(92) + "r?" + chr(92) + "n(.*?)" + chr(92) + "r?" + chr(92) + "n---" + chr(92) + "r?" + chr(92) + "n", re.S)

DEFAULT_CONTAINERS = ["tasks"]

TERMINAL = {"DONE", "REJECTED"}

STATUS_KEYS = {
    "id", "title", "goal", "value", "lifecycle", "lifecycle_verbatim",
    "owner", "authority", "outcome", "created", "updated",
}

BOUNDS = {"title": 80, "goal": 160, "value": 160, "outcome": 160, "lifecycle_verbatim": 80}

REQUIRED_KEYS = ("id", "title", "goal", "value", "lifecycle", "owner", "authority",
                 "created", "updated")

#: Fallback vocabulary when project_config.yaml cannot be read.
DECLARED_LIFECYCLES = ("TODO", "HL_DRAFT", "RES", "PHASES", "TS_DRAFT", "ONB", "RF", "REV",
                       "KNW", "DONE", "BLOCKED", "REJECTED")

#: Not selectable by a person. Migration writes it when a source held a value the
#: vocabulary does not contain, and keeps that value verbatim beside it.
UNDECLARED = "UNDECLARED"

#: `created` and `updated` carry the same grammar as the identifier: second resolution.
#: A day-resolution stamp on a corpus with several transitions a day reports nothing — the
#: rejected pass shipped TFW-60 with `created` and `updated` identical.
STAMP = re.compile(r"^\d{8}-\d{6}$")

#: What a legacy source that carried only a date migrates to. The zero time is DECLARED, not
#: measured: it says "this day, time unknown" and must never be read as second-accurate.
ZERO_TIME = "000000"


def parse_identifier(text: str) -> tuple[str, str] | None:
    """Classify a task identifier or directory name under either grammar.

    Accepts what a consumer actually holds — a directory name — and returns
    ``(kind, identifier)``:

    * ``("clock", "20260826-143000__query_redesign")`` — the identifier is the whole name.
    * ``("legacy", "TFW-60")`` — the pre-2.0.0 grammar, where the slug is not part of it.
    * ``None`` — not an identifier. **A bare ``YYYYMMDD-HHMMSS`` lands here on purpose**: it
      is ambiguous between any two tasks created in that second, and no consumer may accept
      one as if it named exactly one task.

    One resolver, used by every consumer. Per-call-site regexes are how the previous board
    parser drifted out of sync with the board it parsed.
    """
    text = text.strip()
    if CLOCK_ID.match(text):
        return ("clock", text)
    match = LEGACY_ID.match(text)
    if match:
        return ("legacy", f"{match.group('prefix')}-{match.group('seq')}")
    return None


def sort_key(kind: str, identifier: str) -> tuple:
    """Declared sort key. Legacy tasks sort before clock tasks; within each, ascending.

    Legacy identifiers sort numerically, so ``TFW-9`` precedes ``TFW-10``. Clock
    identifiers sort by timestamp then slug — fixed-width, so lexical order on the stamp is
    chronological, and the slug only breaks a same-second tie. The newest task is last.
    """
    if kind == "legacy":
        m = LEGACY_ID.match(identifier)
        return (0, m.group("prefix"), int(m.group("seq")), "")
    m = CLOCK_ID.match(identifier)
    return (1, m.group("stamp"), 0, m.group("slug"))


def read_config(root: Path) -> dict:
    """Read the TFW block from ``project_config.yaml``."""
    path = root / ".tfw" / "project_config.yaml"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        return (yaml.safe_load(handle) or {}).get("tfw", {}) or {}


def task_containers(root: Path) -> list[str]:
    """Ordered container list. A task is created in the first; resolved across all."""
    value = read_config(root).get("task_containers") or DEFAULT_CONTAINERS
    if isinstance(value, str):
        value = [value]
    return [str(item).strip("/") for item in value]


def iter_task_dirs(root: Path, containers: list[str] | None = None) -> list[Path]:
    """Every task directory across every container, in a deterministic order.

    A container may hold task directories directly (the legacy layout) or nested under a
    creation-year folder (the layout introduced in 2.0.0). Both are searched. The result is
    sorted by the declared key rather than by whatever order the filesystem offered.
    """
    if containers is None:
        containers = task_containers(root)
    found: list[tuple[tuple, Path]] = []
    seen: set[Path] = set()
    for container in containers:
        base = root / container
        if not base.is_dir():
            continue
        # One level of year nesting is expanded; anything deeper is a task's own content.
        pending = sorted((p for p in base.iterdir() if p.is_dir()), key=lambda p: p.name)
        while pending:
            child = pending.pop(0)
            if re.fullmatch(r"\d{4}", child.name) and child.parent == base:
                pending = sorted(
                    (p for p in child.iterdir() if p.is_dir()), key=lambda p: p.name
                ) + pending
                continue
            parsed = parse_identifier(child.name)
            if parsed is None or child.resolve() in seen:
                continue
            seen.add(child.resolve())
            found.append((sort_key(*parsed), child))
    found.sort(key=lambda pair: (pair[0], str(pair[1])))
    return [path for _, path in found]


def declared_lifecycles(root: Path) -> list[str]:
    """The lifecycle vocabulary this project declares."""
    entries = read_config(root).get("statuses") or []
    ids = [str(e.get("id")) for e in entries if isinstance(e, dict) and e.get("id")]
    return ids or list(DECLARED_LIFECYCLES)


def read_status(task_dir: Path, declared: list[str] | None = None) -> dict | None:
    """Parse ``status.md`` front matter. Returns ``None`` when the file is absent.

    A file that exists but cannot be parsed, or that breaks any rule of the closed schema,
    returns a dict carrying ``_error``: a malformed input is reported, never dropped and
    never silently repaired.
    """
    path = task_dir / "status.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {"_error": "no YAML front matter"}
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return {"_error": f"unparseable front matter: {exc.__class__.__name__}"}
    if not isinstance(data, dict):
        return {"_error": "front matter is not a mapping"}
    problems = validate_status(data, task_dir, declared)
    if problems:
        data["_error"] = "; ".join(problems)
    return data


def validate_status(data: dict, task_dir: Path | None = None,
                    declared: list[str] | None = None) -> list[str]:
    """Every rule the carrier declares, checked. Returns the problems found, in order.

    The key set is closed, so an unknown key is an error rather than an extension: a field
    nothing reads is exactly what the carrier exists to keep out. Conditional keys are
    checked both ways — present when required, and absent when not applicable — because a
    stray ``outcome`` on a live task is a claim that it finished.
    """
    declared = declared or list(DECLARED_LIFECYCLES)
    problems: list[str] = []

    unknown = sorted(set(data) - STATUS_KEYS)
    if unknown:
        problems.append("unknown keys: " + ", ".join(unknown))

    for key in REQUIRED_KEYS:
        if not data.get(key):
            problems.append(f"missing {key}")

    for key, limit in BOUNDS.items():
        value = data.get(key)
        if isinstance(value, str) and len(value) > limit:
            problems.append(f"{key} exceeds {limit} code points")

    lifecycle = data.get("lifecycle")
    if lifecycle and lifecycle != UNDECLARED and lifecycle not in declared:
        problems.append(
            f"lifecycle '{lifecycle}' is not declared and is not {UNDECLARED}; "
            "an out-of-vocabulary value must be carried as "
            f"{UNDECLARED} plus lifecycle_verbatim, never normalized")

    # Conditional keys, checked in both directions.
    if lifecycle == UNDECLARED and not data.get("lifecycle_verbatim"):
        problems.append(f"lifecycle is {UNDECLARED} but lifecycle_verbatim is absent, "
                        "so the value the source actually carried is lost")
    if lifecycle != UNDECLARED and data.get("lifecycle_verbatim"):
        problems.append("lifecycle_verbatim is only meaningful when lifecycle is "
                        f"{UNDECLARED}")
    if lifecycle in TERMINAL and not data.get("outcome"):
        problems.append(f"lifecycle is terminal ({lifecycle}) but outcome is absent")
    if lifecycle and lifecycle not in TERMINAL and data.get("outcome"):
        problems.append("outcome is set on a task that has not reached a terminal "
                        "lifecycle — it claims a result that has not happened")

    for key in ("created", "updated"):
        value = data.get(key)
        if value is None:
            continue
        text = value.isoformat() if hasattr(value, "isoformat") else str(value)
        if text != "unrecorded" and not STAMP.match(text):
            problems.append(f"{key} is not YYYYMMDD-HHMMSS or 'unrecorded': {text!r}")

    # The identifier must be the one its own directory carries. A state file that names a
    # different task is worse than a missing one: every consumer keys on `id`.
    if task_dir is not None:
        parsed = parse_identifier(task_dir.name)
        if parsed is None:
            problems.append(f"directory name {task_dir.name!r} is not a task identifier")
        elif data.get("id") and str(data["id"]) != parsed[1]:
            problems.append(
                f"id {str(data['id'])!r} disagrees with its directory, which is "
                f"{parsed[1]!r}")

    return problems


PHASE_DIR = re.compile(r"^phase-(?P<letter>[a-z0-9]+)$")


def iter_phase_dirs(task_dir: Path) -> list[Path]:
    """Phase directories inside a task, in declared order.

    A phase carries its own ``status.md`` on the same closed schema, written by that phase's
    owner. Two phases running under two owners are two files, so they never contend.
    """
    return sorted((p for p in task_dir.iterdir() if p.is_dir() and PHASE_DIR.match(p.name)),
                  key=lambda p: p.name)


def read_phase_status(phase_dir: Path, declared: list[str] | None = None) -> dict | None:
    """A phase's own state. Same schema as a task's, minus the directory-identifier check.

    The phase directory is named ``phase-a``, not an identifier, so the ``id`` field carries
    the *task's* identifier and agreement with the directory name is not checked here.
    """
    path = phase_dir / "status.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        return {"_error": "no YAML front matter"}
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return {"_error": f"unparseable front matter: {exc.__class__.__name__}"}
    if not isinstance(data, dict):
        return {"_error": "front matter is not a mapping"}
    problems = validate_status(data, None, declared)
    if problems:
        data["_error"] = "; ".join(problems)
    return data


# ---------------------------------------------------------------------------
# Journal events
# ---------------------------------------------------------------------------

#: ``<YYYYMMDD-HHMMSS>__<kind>__<actor>.md``. The actor is part of the name because it is
#: the only field that separates two concurrent writers: ``on_behalf_of`` is the same person
#: for both, and ``via`` is the same provider for two sessions of one tool. Without it, two
#: writers recording the same kind in the same second produce one filename and one of the
#: two events is silently lost.
EVENT_NAME = re.compile(
    r"^(?P<stamp>\d{8}-\d{6})__(?P<kind>[a-z_]+)__(?P<actor>[a-z0-9][a-z0-9-]*)\.md$")

#: The pre-2.0.0 event name, ``<stamp>__<kind>.md``. Events written under it are immutable
#: like every other event: a correction is a new event, never an edit. They are reported as
#: legacy rather than as defects, exactly as a legacy task identifier is.
LEGACY_EVENT_NAME = re.compile(r"^(?P<stamp>\d{8}-\d{6})__(?P<kind>[a-z_]+)\.md$")

#: Closed vocabulary. ``consolidation`` is reserved for Phases B and C and is not yet valid.
EVENT_KINDS = ("created", "dispatch", "handoff", "transition", "ownership_changed",
               "amendment_escalated")
RESERVED_EVENT_KINDS = ("consolidation",)

EVENT_KEYS = {"time", "kind", "actor", "on_behalf_of", "via", "from", "to", "refs", "summary"}
EVENT_REQUIRED = ("time", "kind", "actor", "on_behalf_of", "refs")

DEFAULT_SUMMARY_CEILING = 120

#: Provider families. A provider is what produced a record — the `via` field — and is NEVER
#: an actor: two sessions of one tool are two writers and would share one name. Rejecting
#: these by name is a floor, not the rule; the rule is that an actor must be a declared
#: `team/` handle, and no provider family is one.
PROVIDER_FAMILIES = frozenset({
    "claude", "claude-code", "codex", "gemini", "copilot", "cursor", "openai",
    "anthropic", "gpt", "llm", "ai", "agent", "assistant", "bot",
})

ISO_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:[+-]\d{2}:\d{2}|Z)$")


def team_profiles(root: Path) -> dict[str, dict]:
    """Every participant declared in ``team/``, **parsed**, keyed by handle.

    Reading the filename was not enough. Accountability is a claim about a *person*, so the
    rule needs the profile's declared ``type``, and only the file body carries it.

    An empty dict means the project declares nobody — which is a reason to refuse a new
    event, never a reason to skip the check.
    """
    directory = root / "team"
    if not directory.is_dir():
        return {}
    profiles: dict[str, dict] = {}
    for path in sorted(directory.glob("*.md")):
        if path.stem == "README":
            continue
        match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
        data = {}
        if match:
            try:
                loaded = yaml.safe_load(match.group(1))
                if isinstance(loaded, dict):
                    data = loaded
            except yaml.YAMLError:
                data = {"_error": "unparseable front matter"}
        handle = str(data.get("handle") or path.stem)
        profiles[handle] = data
    return profiles


def team_handles(root: Path) -> set[str]:
    """Declared handles only. Kept for callers that do not need the profile body."""
    return set(team_profiles(root))


def summary_ceiling(root: Path) -> int:
    """The measured entry ceiling this project declares."""
    journal = read_config(root).get("journal") or {}
    try:
        return int(journal.get("max_summary_length", DEFAULT_SUMMARY_CEILING))
    except (TypeError, ValueError):
        return DEFAULT_SUMMARY_CEILING


def read_stamp() -> str:
    """One reading of the system clock, at second resolution."""
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def event_filename(kind: str, actor: str, taken=(), clock=read_stamp,
                   sleep=time.sleep, attempts: int = 8, interval: float = 0.34) -> str:
    """The filename for one event. **Every candidate is a fresh reading of the clock.**

    The rule is deliberately not "add a counter": a counter is shared state, and shared state
    is what this whole phase removes. It is also not "add a second": an arithmetic successor
    is a number somebody allocated, which is the same defect wearing a clock's clothes. The
    earlier implementation took a stamp as a parameter and did exactly that — it advanced the
    second by addition, and at 23:59:59 it wrapped the time while keeping yesterday's date,
    producing an event that claims to have happened before the one it follows.

    So: read the clock, try to claim the name, and if it is taken **read the clock again**.
    Between readings we wait, because the only thing that makes the next reading different is
    time passing. Bounded by ``attempts``; on exhaustion it fails visibly rather than
    inventing a value.

    Collisions between two *different* actors cannot happen at all — the actor is in the
    name. This exists for one actor writing twice inside a single second.

    ``clock`` and ``sleep`` are injectable so a test can prove each candidate came from a
    reading rather than from arithmetic.
    """
    taken = set(taken)
    seen: list[str] = []
    for attempt in range(attempts):
        stamp = clock()
        seen.append(stamp)
        candidate = f"{stamp}__{kind}__{actor}.md"
        if candidate not in taken:
            return candidate
        if attempt < attempts - 1:
            sleep(interval)
    raise ValueError(
        f"{actor} already has an event named for every one of {attempts} clock readings "
        f"({seen[0]} … {seen[-1]}). The clock is not advancing, which is a clock problem "
        "and not a naming problem — no second is invented to get past it")


def validate_event(data: dict, filename: str, ceiling: int = DEFAULT_SUMMARY_CEILING,
                   profiles: dict[str, dict] | None = None) -> list[str]:
    """Every rule an event declares, checked against one file. Problems, in order.

    ``profiles`` is ``team_profiles(root)`` — the parsed participants. **An empty dict is a
    refusal, not a skip**: if the project declares nobody, a new event has nobody who answers
    for it, and that is precisely the case the rule exists to catch. Passing ``None`` means
    the caller is checking something else and has opted out; every production path supplies
    the dict.
    """
    problems: list[str] = []

    name = EVENT_NAME.match(filename)
    legacy = name is None and LEGACY_EVENT_NAME.match(filename) is not None
    if not name and not legacy:
        problems.append(
            f"filename {filename!r} is not <YYYYMMDD-HHMMSS>__<kind>__<actor>.md")

    unknown = sorted(set(data) - EVENT_KEYS)
    if unknown:
        problems.append("unknown keys: " + ", ".join(unknown))

    # A legacy event predates `on_behalf_of` and the actor-bearing filename. Demanding
    # them would demand an edit, and an event is never edited.
    required = EVENT_REQUIRED if not legacy else tuple(
        k for k in EVENT_REQUIRED if k != "on_behalf_of")
    for key in required:
        if not data.get(key):
            problems.append(f"missing {key}")

    kind = data.get("kind")
    if kind in RESERVED_EVENT_KINDS:
        problems.append(f"kind '{kind}' is reserved for a later phase and is not yet valid")
    elif kind and kind not in EVENT_KINDS:
        problems.append(f"kind '{kind}' is outside the closed vocabulary")

    if name and kind and name.group("kind") != kind:
        problems.append(f"filename says kind '{name.group('kind')}', body says '{kind}'")
    if name and data.get("actor") and name.group("actor") != str(data["actor"]):
        problems.append(
            f"filename says actor '{name.group('actor')}', body says '{data['actor']}'")

    # An actor names a writer. A provider family names a tool, and two sessions of one tool
    # are two writers — so a provider can never identify who acted. Checked on the body AND
    # the filename, because agreeing on the wrong value is still the wrong value.
    # A legacy event predates this rule as surely as it predates `on_behalf_of`, and the
    # journal is immutable: a rule introduced later describes old entries and never rewrites
    # them. Three events in this repository carry `actor: claude-code` or `actor: codex` and
    # stay exactly as written.
    for where, value in (() if legacy else
                         (("body", data.get("actor")),
                          ("filename", name.group("actor") if name else None))):
        if value and str(value).lower() in PROVIDER_FAMILIES:
            problems.append(
                f"{where} actor '{value}' is a provider family, not a writer — two sessions "
                "of one tool are two actors. Name the writer in `actor` and the tool in `via`")
            break

    actor = data.get("actor")
    on_behalf_of = data.get("on_behalf_of")

    # The legacy escape is scoped to events identifiable as pre-rule by their own filename
    # shape — a durable property of the event itself, not a convenience for the caller. A new
    # event carries the actor in its name and can never reach this branch.
    if profiles is not None and not legacy:
        declared = set(profiles)
        if actor and str(actor) not in declared:
            problems.append(
                f"actor '{actor}' is not a declared team/ participant "
                f"({', '.join(sorted(declared)) if declared else 'team/ declares nobody'})")
        if on_behalf_of:
            profile = profiles.get(str(on_behalf_of))
            if profile is None:
                problems.append(
                    f"on_behalf_of '{on_behalf_of}' is not a declared team/ participant "
                    f"({', '.join(sorted(declared)) if declared else 'team/ declares nobody'})")
            elif str(profile.get("type", "")).strip() != "human":
                problems.append(
                    f"on_behalf_of '{on_behalf_of}' is declared as "
                    f"'{profile.get('type') or 'no type'}', not human — accountability "
                    "always resolves to a person")

    time_value = data.get("time")
    if time_value is not None:
        text = time_value.isoformat() if hasattr(time_value, "isoformat") else str(time_value)
        if not ISO_TIME.match(text):
            problems.append(f"time is not ISO 8601 with an offset: {text!r}")

    refs = data.get("refs")
    if refs is not None and (not isinstance(refs, list) or not refs):
        problems.append("refs must be a non-empty list of paths")

    summary = data.get("summary")
    if isinstance(summary, str) and len(summary) > ceiling:
        problems.append(
            f"summary is {len(summary)} code points, ceiling is {ceiling}; "
            "move the content into an artifact and reference it from the event")

    has_from, has_to = data.get("from") is not None, data.get("to") is not None
    if has_from != has_to:
        problems.append("a state change needs both 'from' and 'to', or neither")

    return problems


def read_journal(task_dir: Path, ceiling: int = DEFAULT_SUMMARY_CEILING,
                 profiles: dict[str, dict] | None = None
                 ) -> tuple[list[dict], list[str]]:
    """Every event in a task's journal, and every problem found. Nothing is dropped.

    Events written before the 2.0.0 grammar are counted and reported once, not corrected:
    the journal is immutable, so a rule introduced later can describe old entries but never
    rewrite them.
    """
    journal = task_dir / "journal"
    if not journal.is_dir():
        return [], []
    events, problems = [], []
    legacy = 0
    for path in sorted(journal.glob("*.md"), key=lambda p: p.name):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
        if not match:
            problems.append(f"{path.name}: no YAML front matter")
            continue
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            problems.append(f"{path.name}: unparseable ({exc.__class__.__name__})")
            continue
        if not isinstance(data, dict):
            problems.append(f"{path.name}: front matter is not a mapping")
            continue
        if EVENT_NAME.match(path.name) is None and LEGACY_EVENT_NAME.match(path.name):
            legacy += 1
        for problem in validate_event(data, path.name, ceiling, profiles):
            problems.append(f"{path.name}: {problem}")
        data["_file"] = path.name
        events.append(data)
    if legacy:
        problems.insert(0, f"{legacy} event(s) predate the 2.0.0 event grammar; immutable "
                            "by rule, so they are recorded as legacy rather than corrected")
    return events, problems


# ---------------------------------------------------------------------------
# Board snapshot
# ---------------------------------------------------------------------------

def read_snapshot(root: Path) -> list[dict]:
    """Read the frozen board snapshot, if one exists.

    The snapshot is the record of tasks that closed before the migration and of backlog
    rows that never had a directory. It is historical and never changes.
    """
    path = root / "tasks" / "BOARD-SNAPSHOT.md"
    if not path.exists():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        rows.append({
            "id": cells[0].strip("`"),
            "title": cells[1],
            "lifecycle": cells[2],
            "class": cells[3],
        })
    return rows


def snapshot_index(rows: list[dict]) -> dict[str, dict]:
    """Snapshot rows by identifier, for deciding what a directory without state is."""
    return {row["id"]: row for row in rows if row["id"] and row["id"] != "(none)"}


# ---------------------------------------------------------------------------
# Index rendering
# ---------------------------------------------------------------------------

def _cell(value: object, dash: str = "—") -> str:
    text = "" if value is None else str(value).strip()
    return text.replace("|", "\\|") if text else dash


def _link(root: Path, base: Path, target: Path) -> str:
    """A link from the index file to a task, relative to where the index actually lives.

    The index sits inside the first container, not at the project root. Emitting
    root-relative paths produces a file whose every link is broken — which is exactly what
    a corpus-wide link check catches and a reader hits on the first click.
    """
    return os.path.relpath(target, base).replace(os.sep, "/")


def collect(root: Path) -> dict:
    """Gather every input the index renders, with malformed entries kept visible."""
    containers = task_containers(root)
    declared = declared_lifecycles(root)
    ceiling = summary_ceiling(root)
    profiles = team_profiles(root)
    base = output_path(root).parent
    snapshot = read_snapshot(root)
    by_id = snapshot_index(snapshot)

    live: list[dict] = []
    historical: list[dict] = []
    unresolved: list[dict] = []
    for task_dir in iter_task_dirs(root, containers):
        rel = _link(root, base, task_dir)
        parsed = parse_identifier(task_dir.name)
        status = read_status(task_dir, declared)
        if status is not None and not status.get("_error"):
            status["_path"] = rel
            status["_kind"] = parsed[0]
            status["_key"] = sort_key(*parsed)
            phases = []
            for phase_dir in iter_phase_dirs(task_dir):
                phase = read_phase_status(phase_dir, declared)
                if phase is None:
                    continue
                if phase.get("_error"):
                    unresolved.append({
                        "path": f"{rel}/{phase_dir.name}", "id": parsed[1],
                        "reason": f"{phase_dir.name}/status.md: {phase['_error']}"})
                    continue
                phase["_name"] = phase_dir.name
                phase["_path"] = f"{rel}/{phase_dir.name}"
                phases.append(phase)
            status["_phases"] = phases
            live.append(status)
            # The journal is not rendered here — it is a task's own record, not portfolio
            # information. But a malformed event must not become invisible just because the
            # index has no column for it, so its problems join the unresolved report.
            _, journal_problems = read_journal(task_dir, ceiling, profiles)
            for problem in journal_problems:
                unresolved.append({"path": f"{rel}/journal", "id": parsed[1],
                                   "reason": problem})
            continue
        if status is not None:
            unresolved.append({"path": rel, "id": parsed[1], "reason": status["_error"]})
            continue
        # No state file. That is normal for a task that closed before 2.0.0 — the board
        # snapshot is its record and writing state for it would invent a live task. It is
        # only unresolved when the snapshot cannot vouch for it either.
        row = by_id.get(parsed[1])
        if row and row["class"] == "matched":
            historical.append({
                "path": rel, "id": parsed[1], "title": row["title"],
                "lifecycle": row["lifecycle"], "_key": sort_key(*parsed),
            })
        else:
            reason = (f"no status.md; board row class: {row['class']}" if row
                      else "no status.md, and no board row names it")
            unresolved.append({"path": rel, "id": parsed[1], "reason": reason})

    live.sort(key=lambda item: item["_key"])
    historical.sort(key=lambda item: item["_key"])
    backlog = [row for row in snapshot if row["class"] == "board-only, backlog"]
    absorbed = [row for row in snapshot if row["class"] == "board-only, absorbed elsewhere"]
    freshness = max((str(item.get("updated") or "") for item in live), default="")
    return {
        "containers": containers,
        "live": live,
        "historical": historical,
        "backlog": backlog,
        "absorbed": absorbed,
        "unresolved": unresolved,
        "snapshot": snapshot,
        "freshness": freshness,
        "snapshot_link": _link(root, base, root / "tasks" / "BOARD-SNAPSHOT.md"),
    }


def render(data: dict) -> str:
    live = data["live"]
    historical = data["historical"]
    backlog = data["backlog"]
    absorbed = data["absorbed"]
    unresolved = data["unresolved"]
    snapshot = data["snapshot"]
    out: list[str] = []
    add = out.append

    add("# Portfolio index")
    add("")
    add("> **This file is derived and non-authoritative.** It is rebuilt from every task's")
    add("> own `status.md` by `docs/scripts/gen_index.py`. When it disagrees with a task,")
    add("> the task is right. Delete it and nothing is lost; regenerate it and it comes")
    add("> back. Any workflow acting on a task re-reads that task's `status.md` first.")
    add("")
    add("| | |")
    add("|---|---|")
    add(f"| Source | {len(live)} task state files"
        + (f", {len(snapshot)} snapshot rows" if snapshot else "") + " |")
    add(f"| Containers searched | {', '.join(f'`{c}/`' for c in data['containers'])} |")
    add(f"| Freshness | newest task state update: {data['freshness'] or 'unknown'} |")
    add(f"| Unresolved inputs | {len(unresolved)} |")
    add("| Generator | `python docs/scripts/gen_index.py` |")
    add("")

    active = [item for item in live if str(item.get("lifecycle")) not in TERMINAL]
    closed = [item for item in live if str(item.get("lifecycle")) in TERMINAL]

    add(f"## In flight — {len(active)}")
    add("")
    if active:
        add("| Task | Lifecycle | Owner | Goal | Authority |")
        add("|---|---|---|---|---|")
        for item in active:
            lifecycle = str(item.get("lifecycle"))
            if lifecycle == "UNDECLARED":
                lifecycle = f"UNDECLARED (`{_cell(item.get('lifecycle_verbatim'))}`)"
            authority = _cell(item.get("authority"), "")
            link = (f"[{authority}]({item['_path']}/{authority})"
                    if authority and authority != "unrecorded" else "—")
            add(
                f"| [**{_cell(item.get('id'))}** — {_cell(item.get('title'))}]"
                f"({item['_path']}/status.md) | {lifecycle} | {_cell(item.get('owner'))} "
                f"| {_cell(item.get('goal'))} | {link} |"
            )
            # Phase rows sit beneath their task, which is what the retired board's
            # per-phase columns showed. Each is read from that phase's own file — the task
            # row never summarizes them, because a rollup is a second fact to keep in sync.
            for phase in item.get("_phases") or []:
                phase_life = str(phase.get("lifecycle"))
                if phase_life == "UNDECLARED" and phase.get("lifecycle_verbatim"):
                    phase_life = f"UNDECLARED (`{_cell(phase['lifecycle_verbatim'])}`)"
                letter = phase["_name"].replace("phase-", "").upper()
                add(
                    f"| &nbsp;&nbsp;↳ [{letter} — {_cell(phase.get('title'))}]"
                    f"({phase['_path']}/status.md) | {phase_life} "
                    f"| {_cell(phase.get('owner'))} | {_cell(phase.get('goal'))} | — |"
                )
    else:
        add("No task is in flight.")
    add("")

    add(f"## Closed — {len(closed) + len(historical)}")
    add("")
    if closed or historical:
        add("| Task | Outcome | Record |")
        add("|---|---|---|")
        for item in closed:
            add(
                f"| **{_cell(item.get('id'))}** — {_cell(item.get('title'))} "
                f"| {_cell(item.get('lifecycle'))}"
                + (f" · {_cell(item.get('outcome'), '')}" if item.get("outcome") else "")
                + f" | [state]({item['_path']}/status.md) |"
            )
        for item in historical:
            add(
                f"| **{item['id']}** — {_cell(item['title'])} | {_cell(item['lifecycle'])} "
                f"| [task folder]({item['path']}/) |"
            )
    else:
        add("Nothing has closed yet.")
    add("")
    if historical:
        add(f"{len(historical)} of those closed before TFW 2.0.0 and carry no state file.")
        add("That is by design: writing state for finished work would turn a record into a")
        add("live task. Their record is the board row captured in")
        add(f"[`tasks/BOARD-SNAPSHOT.md`]({data['snapshot_link']}), and their folders are")
        add("untouched.")
        add("")

    if backlog:
        add(f"## Backlog — {len(backlog)}")
        add("")
        add("Rows the board carried that never became a task directory. They are ideas, not")
        add("work in progress. Picking one up means creating a task in")
        add(f"`{data['containers'][0]}/`, not reviving a row.")
        add("")
        add("| Idea | Recorded as |")
        add("|---|---|")
        for row in backlog:
            add(f"| `{row['id']}` — {_cell(row['title'])} | {_cell(row['lifecycle'])} |")
        add("")

    if absorbed:
        add(f"## Absorbed — {len(absorbed)}")
        add("")
        add("Rows retired when their work was folded into another task. Kept because a")
        add("reference to one of these identifiers still has to land somewhere.")
        add("")
        add("| Row | Absorbed into |")
        add("|---|---|")
        for row in absorbed:
            title = _cell(row["title"])
            head, _, tail = title.partition(" — absorbed into ")
            add(f"| `{row['id']}` — {head} | {tail or '—'} |")
        add("")

    add(f"## Unresolved inputs — {len(unresolved)}")
    add("")
    add("Reported, never dropped. An entry here names a real directory whose state could")
    add("not be established. It stays visible and non-actionable until someone decides what")
    add("it is.")
    add("")
    if unresolved:
        add("| Path | Identifier | Diagnostic |")
        add("|---|---|---|")
        for item in sorted(unresolved, key=lambda entry: entry["path"]):
            add(f"| `{item['path']}` | `{item['id']}` | {item['reason']} |")
    else:
        add("None.")
    add("")

    add("---")
    add("")
    add("*Generated by `docs/scripts/gen_index.py`. Do not edit: every change is lost on")
    add("the next run, and the authority it would contradict lives in the task folders.*")
    return NEWLINE.join(out) + NEWLINE


def build(root: Path) -> str:
    return render(collect(root))


def output_path(root: Path) -> Path:
    return root / task_containers(root)[0] / "00-INDEX.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--check", action="store_true",
                        help="write nothing; exit 1 if the committed index is stale. A "
                             "deliberate freshness question — never a gate on a task "
                             "transition, which would make the index a shared write again")
    parser.add_argument("--validate", action="store_true",
                        help="write nothing; check every task's own state and journal "
                             "against the closed schema. Exit 1 if any task is malformed. "
                             "This is the build gate: it reads task-local truth and is "
                             "unaffected by whether the derived index happens to be current")
    args = parser.parse_args(argv)

    root = args.root.resolve()

    if args.validate:
        declared = declared_lifecycles(root)
        ceiling = summary_ceiling(root)
        profiles = team_profiles(root)
        failures = 0
        for task_dir in iter_task_dirs(root):
            rel = task_dir.relative_to(root).as_posix()
            status = read_status(task_dir, declared)
            if status is not None and status.get("_error"):
                print(f"{rel}/status.md: {status['_error']}", file=sys.stderr)
                failures += 1
            for phase_dir in iter_phase_dirs(task_dir):
                phase = read_phase_status(phase_dir, declared)
                if phase is not None and phase.get("_error"):
                    print(f"{rel}/{phase_dir.name}/status.md: {phase['_error']}",
                          file=sys.stderr)
                    failures += 1
            _, journal_problems = read_journal(task_dir, ceiling, profiles)
            for problem in journal_problems:
                if "predate the 2.0.0 event grammar" in problem:
                    continue  # immutable by rule; reported in the index, not a failure
                print(f"{rel}/journal/{problem}", file=sys.stderr)
                failures += 1
        total = len(iter_task_dirs(root))
        if failures:
            print(f"{failures} problem(s) across {total} tasks", file=sys.stderr)
            return 1
        print(f"{total} tasks validate against the closed schema")
        return 0

    content = build(root)
    target = output_path(root)

    if args.check:
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current == content:
            print(f"index up to date: {target.relative_to(root).as_posix()}")
            return 0
        print(f"index is stale: {target.relative_to(root).as_posix()}", file=sys.stderr)
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {target.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

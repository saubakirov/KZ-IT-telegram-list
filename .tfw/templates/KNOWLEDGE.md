# KNOWLEDGE.md — Project Knowledge Index

> Central index of project architecture, decisions, and evolution.
> **Principle**: Index, don't duplicate — link to RF/HL files, don't copy their contents.

---

## 0. Philosophy & Principles

> Core principles that guide all decisions. Each links to the HL/RF where it was formalized.

| # | Principle | Source |
|---|-----------|--------|
| P1 | _Describe your first principle_ | HL-{PREFIX}-{N} |
| P2 | _Second principle_ | RF {PREFIX}-{N} |

---

## 1. Architecture Map

> High-level view of the system's components and their relationships.

### Components

| Component | Description | Key Files |
|-----------|-------------|-----------|
| _API Server_ | _Main backend_ | `src/api/` |
| _Frontend_ | _Web UI_ | `src/web/` |

### Architecture Decisions

| # | Decision | Rationale | Source |
|---|----------|-----------|--------|
| D1 | _e.g., Chose PostgreSQL over MongoDB_ | _ACID compliance needed_ | RF {PREFIX}-{N} |

---

## 2. Key Artifacts

> Most important task artifacts for understanding the project. Read these first.

| Task | Title | Key Artifact | Why Important |
|------|-------|-------------|---------------|
| _PROJ-1_ | _Initial setup_ | RF {PREFIX}-1 | _Foundation decisions_ |

---

## 3. Legacy & Deprecation

> What was dropped, frozen, or replaced — and why.

| Item | Status | When | Replacement | Source |
|------|--------|------|-------------|--------|
| _e.g., Old auth module_ | Deprecated | _2026-01_ | _OAuth2 flow_ | RF {PREFIX}-{N} |

---

## 4. Project Facts

> Index of verified project knowledge. Details in `knowledge/` topic files.
> Updated by `/tfw-knowledge` consolidation.

| Category | Count | Topic File |
|----------|-------|------------|

---

> **Maintenance**: This file is updated via the `tfw-docs` workflow after each REVIEW.
> See `.tfw/workflows/docs.md` for the update process.

# RELEASE.md — KZ-IT-telegram-list

> Release strategy for the public Telegram community catalog. This document defines future
> release gates; it does not record or authorize a completed snapshot, tag, or push.

---

## 1. What Is a Release?

A release is a **dated verified catalog snapshot**: every live entry has been checked against
Telegram during the release run, the owner has triaged every retry result that could imply a
dead community, the generated README matches the source data, and the catalog change is recorded
in the root changelog.

The release answers one public question: *when was this catalog known to be accurate?*

## 2. What a Release Is Not

- It is not a software API compatibility promise.
- It is not a project semantic-version bump.
- It is not a partial refresh that leaves unverified live entries presented as current.
- It is not permission to infer liveness, member counts, or death from missing evidence.
- It is not permission to tag or push without the owner's explicit approval at that moment.

## 3. Audience

Releases serve catalog readers, contributors, maintainers, and people evaluating how this
repository applies Trace-First Workflow to its own public data.

## 4. Version and Tag Scheme

Project snapshots use the tag form `data-YYYY-MM-DD`, where the date is the completed catalog
verification date. The project does not use semantic versioning because the catalog has no API
compatibility surface.

`.tfw/VERSION` is unrelated: it identifies the installed Trace-First Workflow framework version,
not a version of this catalog. Framework history belongs in `.tfw/CHANGELOG.md`; catalog history
belongs in the root [`CHANGELOG.md`](CHANGELOG.md).

## 5. Release Triggers

A release may be prepared when both conditions hold:

1. The owner requests or accepts a dated catalog snapshot after a catalog-wide verification run.
2. Every in-scope data change and archive decision has completed its TFW execution and review
   gates.

A schedule may prompt a verification run, but elapsed time alone never creates a release.

## 6. Pre-Release Checklist

- [ ] The catalog-wide live sweep completed with saved evidence for every live entry.
- [ ] Every non-responder was retried and triaged with the owner; ambiguous evidence remains
      unresolved and blocks a claim of full verification.
- [ ] Approved dead communities were archived with `died_on` and a non-empty `reason`; none were
      silently deleted.
- [ ] No member count, verification date, or catalog fact was inferred.
- [ ] `python scripts/validate_schema.py` exits zero.
- [ ] `python scripts/generate_readme.py` completes and `README.md` is generator-current.
- [ ] The root `CHANGELOG.md` describes entries added, archived, and counts refreshed for the
      snapshot without changing `.tfw/CHANGELOG.md`.
- [ ] The Task Board, result evidence, and relevant knowledge/debt records are current.
- [ ] The snapshot commit uses the attribution grammar in `.tfw/conventions.md` §4 and contains
      only the reviewed release paths.
- [ ] The proposed `data-YYYY-MM-DD` tag does not already point at different history.
- [ ] The owner gives explicit approval after reviewing the prepared commit and before any tag or
      push action.

## 7. Release Steps and Authority Gates

1. Run the project statistics workflow against the full catalog and retain its raw evidence.
2. Resolve the owner-triaged archive decisions, validate the schema, and regenerate `README.md`.
3. Assert that `README.md` exactly matches generator output; a hand-edited or stale artifact stops
   the release.
4. Move the relevant root changelog items from `[Unreleased]` into a dated snapshot section.
5. Create the reviewed snapshot commit using the acting product identifier and TFW attribution
   grammar.
6. **Stop.** Present the commit, verification evidence, changelog, and proposed tag to the owner.
7. Only after explicit owner approval at that moment, create `data-YYYY-MM-DD` and push the
   approved commit and tag.

The project command `/kz-release` will orchestrate these steps after its adapter is delivered.
It must preserve the same stop-before-tag-and-push gate; prior plan or TS approval is not release
approval.

---

> Maintained by the project owner. The generic `/tfw-release` workflow reads this project-specific
> strategy before preparing release state.

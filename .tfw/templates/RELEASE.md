# RELEASE.md — {Project Name}

> Release strategy and context for this project.
> Optional artifact — create only if your project has releases, publications, or versioned outputs.

---

## 1. What Is a Release?

> What does "release" mean for this project? Examples:
> - A version bump of a framework or library
> - A deployed application build
> - A published report or document
> - A data pipeline promotion to production

{Describe what constitutes a release for your project}

## 2. Audience

> Who consumes your releases?
> - Downstream projects / developers
> - End users / clients
> - Internal teams
> - The public (open source)

{Describe your audience}

## 3. Version Scheme

> How do you track versions?
> - Semantic versioning (MAJOR.MINOR.PATCH)
> - Calendar versioning (YYYY.MM)
> - Sequential (v1, v2, v3)
> - None (single living document)

{Describe your versioning approach, or "N/A" if not applicable}

## 4. Release Triggers

> When should a release happen?
> - After N tasks complete
> - On a fixed schedule
> - When a milestone is reached
> - Ad-hoc, when the maintainer decides

{Describe what triggers a release}

## 5. Pre-Release Checklist

> What must be true before cutting a release?
> Customize this list for your project.

- [ ] All in-scope tasks are ✅ DONE
- [ ] Task Board is current
- [ ] TECH_DEBT.md reviewed — no critical items blocking release
- [ ] KNOWLEDGE.md updated (if applicable)
- [ ] {Add project-specific checks}

## 6. Release Steps

> Project-specific release actions (beyond what `tfw-release` workflow covers).
> Examples: deploy, publish, notify, tag, build artifacts.

{Describe your release steps, or leave for later}

---

> Maintained by the project owner. Referenced by `.tfw/workflows/release.md`.

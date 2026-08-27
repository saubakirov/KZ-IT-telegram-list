# Antigravity Adapter Setup

Antigravity uses `.agent/rules/` (always-on) and `.agent/workflows/` (on-demand).

## Setup

### 1. Copy the TFW rule

```bash
mkdir -p .agent/rules
cp .tfw/adapters/antigravity/tfw-rules.md.template .agent/rules/tfw.md
```

This rule loads TFW context in every Antigravity chat.

### 2. Copy TFW workflows

```bash
mkdir -p .agent/workflows
cp .tfw/workflows/init.md .agent/workflows/tfw-init.md
cp .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
cp .tfw/workflows/research.md .agent/workflows/tfw-research.md
cp .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
cp .tfw/workflows/review.md .agent/workflows/tfw-review.md
cp .tfw/workflows/resume.md .agent/workflows/tfw-resume.md
cp .tfw/workflows/docs.md .agent/workflows/tfw-docs.md
cp .tfw/workflows/release.md .agent/workflows/tfw-release.md
cp .tfw/workflows/update.md .agent/workflows/tfw-update.md
```

Antigravity reads `.agent/workflows/` directly, so files must be copied (not referenced).

### 3. Add project-specific rules and workflows

You can add more files alongside the TFW ones:

```
.agent/rules/
├── tfw.md                  # TFW (from step 1)
├── agents.md               # Your AI role and mission
└── safety-rules.md         # Domain-specific safety rules

.agent/workflows/
├── tfw-init.md             # TFW init (from step 2)
├── tfw-plan.md             # TFW plan (from step 2)
├── tfw-research.md         # TFW research (from step 2)
├── tfw-handoff.md          # TFW handoff (from step 2)
├── tfw-review.md           # TFW review (from step 2)
├── tfw-resume.md           # TFW resume (from step 2)
├── tfw-docs.md             # TFW docs (from step 2)
├── tfw-release.md          # TFW release (from step 2)
├── tfw-update.md           # TFW update (from step 2)
├── deploy-api.md           # Your deploy workflow
└── build-project.md        # Your build workflow
```

## Keeping Workflows in Sync

When `.tfw/workflows/` is updated, re-copy:

```bash
cp .tfw/workflows/init.md .agent/workflows/tfw-init.md
cp .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
cp .tfw/workflows/research.md .agent/workflows/tfw-research.md
cp .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
cp .tfw/workflows/review.md .agent/workflows/tfw-review.md
cp .tfw/workflows/resume.md .agent/workflows/tfw-resume.md
cp .tfw/workflows/docs.md .agent/workflows/tfw-docs.md
cp .tfw/workflows/release.md .agent/workflows/tfw-release.md
cp .tfw/workflows/update.md .agent/workflows/tfw-update.md
```

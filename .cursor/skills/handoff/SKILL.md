---
name: handoff
description: >-
  Compact the current conversation into a handoff document for another agent.
  Use when the user asks for a handoff, session handoff, or to compact context
  for a fresh agent.
argument-hint: What will the next session focus on?
disable-model-invocation: true
---

# Handoff

Write one handoff markdown file so a fresh agent can continue without replaying the chat.

## Output location

1. Ensure `temp/handoff/` exists under the workspace root (create it if missing). `temp/` is gitignored.
2. Write to:
   `temp/handoff/YYYY-MM-DD-<slug>.md`
   - Date: ISO 8601 calendar date (`yyyy-mm-dd`).
   - Slug: kebab-case from the user argument if present; otherwise from the next-session focus; fallback `session`.
   - If the path already exists, append `-2`, `-3`, … before `.md`.
3. After writing, tell the user the **absolute** path to the file. Do not paste the full document unless asked.

## Arguments

If the user passed an argument, treat it as the next session's focus. Bias Goal, Next steps, and Suggested skills toward that focus. Omit chat digressions that do not serve it.

## Document rules

- Do not duplicate content already in specs, plans, ADRs, issues, commits, or diffs. Reference by path or URL.
- Redact secrets: API keys, passwords, tokens, credentials, and unnecessary PII.
- Prefer bullets over prose. Keep the whole file short enough to read in one pass.
- Cite provenance as `(path)` when pointing at repo files.

## Template

Use this structure exactly (keep the headings):

```markdown
# Handoff: <short title>

## Goal
<One or two sentences: what success looks like for this workstream.>

## Current state
- <Factual status bullets only. What exists, what works, what is blocked.>

## Next steps
1. <Ordered, actionable. First item is what the next agent should do first.>

## Artifacts
- `<path-or-URL>` — <why it matters>
(or `None yet.` plus a short **Propose** list if empty; see below.)

## Suggested skills
- `@skill-name` — <when/why the next agent should invoke it>
```

### Artifacts empty

If there are no durable artifacts yet, write `None yet.` then a **Propose** sublist of 1–3 concrete files or docs the next session should create (path + purpose). Prefer project conventions and donor-repo research over new invention. Do not create those files in the handoff turn unless the user asks.

### Suggested skills

Scan project skills under `.cursor/skills/` and personal skills under `~/.cursor/skills/` (names only; do not invent skills). Recommend only skills that clearly help the next steps. If none apply, write `None.`

## Example

User argument: `research donor repos for snapshot/email/logging patterns`

```markdown
# Handoff: Donor-repo research for live detect stack

## Goal
Evaluate live detection performance and robustness of a custom 4-class YOLO26 model on Raspberry Pi 4 before downstream hardware deployment.

## Current state
- Cursor/project agent setup in progress; runtime code and comparison runs not started.
- Locked classes and operational musts are in project context rules; no in-repo research notes yet.

## Next steps
1. Research donor repos for snapshot, email, logging, and disk-management patterns (vespcv primary; vespa_smart_trap secondary).
2. Record findings as citeable artifacts (paths + what to reuse vs skip).
3. Resume live-detect implementation against those patterns.

## Artifacts
None yet.

**Propose**
- `temp/research/donor-patterns.md` — what to reuse from vespcv / vespa_smart_trap / hornet3000 (snapshot, email, logs, disk).
- `docs/` or plan doc only if the user asks for a durable in-repo plan.

## Suggested skills
- `@grill-me` — if the research turns up competing architecture choices before coding.
- `@domain-modeling` — if terminology or ADRs need to be pinned after research.
```

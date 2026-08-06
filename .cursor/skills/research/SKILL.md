---
name: research
description: >-
  Investigate one focused question against high-trust primary sources and
  write cited findings to temp/research. Use when the user wants a topic
  researched, docs or API facts gathered, or reading legwork delegated.
---

# Research

Answer **one focused question** from primary sources and leave a citable Markdown file. Do not lock architecture or project decisions here.

## Scope (this project)

- **Allowed:** tooling/docs side questions; optional pillar `01-existing-products` registry/product/patent lookups from authoritative first-party sources.
- **Not allowed:** substituting for systematic database runs, hit-count logging, or Rayyan dedup documented in `notes/beauveria-bassiana/`. Those stay in notes (and raw exports under `search-results/raw/`).
- See `docs/adr/0008-research-skill-scope.md`.

## Execution

- **Prefer a background agent** for multi-source or long reads so the parent session can continue.
- **Same-session is OK** when the question is one short official page and the user wants the answer in this chat immediately.
- Stay **generic**: take the question (and optional seed URLs) from the user. Do not embed phase checklists in this skill; those live in Obsidian notes.

## Sources

1. Prefer seed URLs or paths the user supplies (or that are already named in the question).
2. Discovery is allowed only for **first-party** sources: official docs, named GitHub repos, source code, specs, first-party APIs.
3. Do **not** use blogs or secondary write-ups unless the user explicitly asks.
4. Follow every claim back to the source that owns it. If unverified, put it under Open gaps, not Findings.

## Output

1. Ensure `temp/research/` exists under the workspace root (create if missing). `temp/` is gitignored; `temp/research/` is Cursor-unignored.
2. Write one file:
   `temp/research/YYYY-MM-DD-<short-slug>.md`
   - Date: ISO 8601 calendar date (`yyyy-mm-dd`).
   - Slug: kebab-case from the focused question.
   - If the path already exists, append `-2`, `-3`, … before `.md`.
3. After writing, tell the user the **absolute** path. Do not paste the full document unless asked.
4. Do **not** edit `notes/`. The user promotes keepers into Obsidian.

## File template

Use this structure exactly (keep the headings):

```markdown
# <short title>

## Question
<one sentence>

## Answer
<short verdict first>

## Findings
- <claim> (source URL or path)
- <claim> (source URL or path)

## Open gaps
- <unknown or unverified item>

## Sources
- <primary URL or path>
- <primary URL or path>
```

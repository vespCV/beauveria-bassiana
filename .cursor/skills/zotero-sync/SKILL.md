---
name: zotero-sync
description: >-
  One-way sync from local Zotero into the repo: collection membership drives
  pdfs/ placement and 99-excluded filing; annotations feed temp markdown and
  the literature overview draft. Use when the user asks to sync Zotero,
  exclusions, collection folders, or PDF annotations with Cursor.
---

# Zotero → Cursor sync

One-way sync: **Zotero → repo**. Never write `/Users/md/Zotero/zotero.sqlite` or remove files from Zotero `storage/`.

## Authority map

| Concern | Authority | Repo effect |
| --- | --- | --- |
| Overview **section** | Include CSV primary `screening_category` | Overview headings |
| **PDF folder** placement | Zotero collection | Copy/move under `pdfs/{collection}/` |
| **Exclusion** | Prefer `temp/zotero/99-excluded.bib` (export of **only** collection `99-excluded`); else sqlite collection `99-excluded` | `input-phase2/99-excluded/records.csv` + `pdfs/99-excluded/`; remove from include CSV |
| Annotation text | Prefer `notes/beauveria-bassiana/zotero/{citekey}.md`; else `temp/zotero-annotations/` | Feed overview; not a decision-field overlay |

If Zotero collection and CSV primary disagree: **PDF follows Zotero**; report the conflict; do not silently rewrite CSV science categories (exclusion sync may still remove include rows).

Vs `@file-pdfs`: inbox filing uses CSV. This skill uses Zotero collections for placement; after collections are curated, `@zotero-sync` wins for placement conflicts.

## Paths

| Path | Role |
| --- | --- |
| `/Users/md/Zotero/` | Live library (read via DB **copy**) |
| `temp/zotero/99-excluded.bib` | Preferred exclusion BibTeX (user export of collection only) |
| `/Users/md/Downloads/Mijn Bibliotheek.bib` | Used only if it looks like excluded-only (small); full-library exports ignored |
| `pdfs/99-excluded/` | Excluded full texts |
| `input-phase2/99-excluded/records.csv` | In-repo exclusion audit |
| `input-phase2/relevant_articles_categorized.csv` | Current includes only after sync |
| `notes/beauveria-bassiana/zotero/` | Obsidian annotation exports (read-only unless user allows note edits) |
| `temp/zotero-annotations/` | Agent-written annotation markdown |
| `temp/overview/literature-overview.md` | Literature overview draft (screened-out section) |
| `temp/zotero/last-sync-report.json` | Last run report |

Collection → folder map (hyphen collections; underscore under `02*`):

- `02a-efficacy` → `pdfs/02-efficacy-mechanics-delivery/02a_efficacy/`
- `02b-strains-traits` → `…/02b_strains_traits/`
- `02c-formulation-delivery` → `…/02c_formulation_delivery/`
- `99-excluded` → `pdfs/99-excluded/` (wins over other collections for placement)

Multi-collection: prefer `99-excluded`, else deepest `02*` child, else first ranked by depth. Always report multi-collection items.

## Workflow

Copy this checklist and track it:

```
- [ ] 1. Dry-run script
- [ ] 2. Review report (conflicts, missing PDFs, bib ignored?)
- [ ] 3. Apply script
- [ ] 4. Refresh README inventory counts (same rules as @file-pdfs)
- [ ] 5. Optionally update overview body from annotations / phase2 notes
- [ ] 6. Report to user
```

### 1–3. Run the helper

From repo root:

```sh
python3 .cursor/skills/zotero-sync/scripts/zotero_sync.py
python3 .cursor/skills/zotero-sync/scripts/zotero_sync.py --apply
```

Optional: `--zotero-dir /Users/md/Zotero` `--bib temp/zotero/99-excluded.bib`

The script:

1. Copies `zotero.sqlite` and Better BibTeX `citationkey` DB under `temp/zotero/` when needed.
2. Loads screening collections and PDF attachments from `storage/`.
3. **Placement:** copies from Zotero storage into `pdfs/…` when missing; moves misplaced files **within** `pdfs/` only.
4. **Exclusion:** writes `input-phase2/99-excluded/records.csv`; removes matching DOI/title rows from the include CSV.
5. **Annotations:** reuses Obsidian citekey notes when present; else writes `temp/zotero-annotations/{citekey}.md`.
6. **Overview:** updates `## Screened out (99-excluded)` in `temp/overview/literature-overview.md`.

### 4. README inventory

After `--apply`, recount PDF have/missing like `@file-pdfs` and patch README inventory tables. Minimal diff. No Cursor mentions in README.

### 5. Overview body

Do not invent findings. Seed from extracts + annotation text + allowed phase2 notes when the user asked for overview work. Mark evidence level (`abstract` / `full-text` / `zotero-annotation`).

## User: exclusion BibTeX export

For the preferred exclusion signal, in Zotero:

1. Open collection `99-excluded`.
2. Select all items in that collection only.
3. Export as BibTeX (Better BibTeX) to `temp/zotero/99-excluded.bib` (create `temp/zotero/` if needed).
4. Do **not** export the whole library to that path.

Until that file exists (or a small excluded-only export replaces the full-library Downloads bib), the script uses sqlite collection `99-excluded`.

## Hard rules

- Zero hallucinations: cite report paths and Zotero/CSV evidence.
- Never write the live Zotero DB; never delete Zotero `storage/` files.
- Do not edit `notes/` unless the user explicitly allows it for that run.
- Do not draft go / conditional-go / no-go.
- No Scholar automation.
- No em dashes or emojis in files you write.
- Do not `git commit` unless the user asks.

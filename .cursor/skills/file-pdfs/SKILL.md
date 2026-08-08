---
name: file-pdfs
description: >-
  Identify PDFs in pdfs/inbox/, match them to phase 2 records, rename and move
  them into the correct pdfs/ category folder, remove matched items from
  pdfs_not_downloaded.md, and refresh README.md inventory and PRISMA counts.
  Use when the user adds PDFs to inbox, asks to file or rename PDFs, or to
  update pdfs_not_downloaded or the phase 2 full-text inventory in README.
---

# File phase 2 PDFs

Process new full-text PDFs from `pdfs/inbox/` into the phase 2 library and keep the missing-PDF list and README inventory in sync.

## Phase gate (hard stop)

Before any other step, verify all three exist on disk:

1. `input-phase2/relevant_articles_categorized.csv`
2. `input-phase2/pdfs_not_downloaded.md`
3. `README.md` with study-selection / PRISMA skeleton

If any are missing: refuse, name the missing path(s), and stop. Do not invent stubs or placeholders. See `docs/adr/0001-phase-gated-agent-workflows.md` and `docs/adr/0006-file-pdfs-hard-stop-on-phase-gate.md`.

## Sources of truth

| Path | Role |
| --- | --- |
| `pdfs/inbox/` | Drop zone for new PDFs only |
| `pdfs/{category}/` | Filed PDFs by screening category |
| `input-phase2/relevant_articles_categorized.csv` | Phase 2 records; `category` and DOI/title/authors/year |
| `input-phase2/pdfs_not_downloaded.md` | Missing PDFs, grouped by category |
| `README.md` | Phase 2 full-text inventory table, study-selection counts, PRISMA flow `E` node |

Category folder names must match CSV `category` and the `## {category} (N)` headers in `pdfs_not_downloaded.md`:

pdfs/
01-existing-products/
02-efficacy-mechanics-delivery/
    02a_efficacy/
    02b_strains_traits/
    02c_formulation_delivery/
03-autodissemination-social/
04-nontarget-ecotox/
05-regulatory-policy/
06-background-proxies/

## Workflow

Copy this checklist and track it:

```
- [ ] 1. List inbox PDFs
- [ ] 2. Identify each PDF (title, first author, year, DOI)
- [ ] 3. Match to CSV and pdfs_not_downloaded
- [ ] 4. File matches (rename + move); leave non-matches in inbox
- [ ] 5. Update pdfs_not_downloaded.md
- [ ] 6. Recount and update README.md
- [ ] 7. Report results to user
```

### 1. List inbox PDFs

List `pdfs/inbox/*.pdf`. If empty, stop.

### 2. Identify each PDF

Do **not** trust the drop filename alone. Extract identity from the file:

1. Prefer PDF metadata title/author when present.
2. Else extract text from page 1 (Python `pypdf` / `PyPDF2` is fine; `pdftotext` if available).
3. Record: title, first author surname, year, DOI (if present).

If identity cannot be verified, leave the file in inbox and flag it. Do not guess.

### 3. Match

For each identified PDF, search in order:

1. DOI against CSV `doi` and against DOI lines in `pdfs_not_downloaded.md`
2. Exact or near-exact title against CSV `title` and list titles
3. Author + year only as a weak check after title/DOI match

**On the list:** present in `pdfs_not_downloaded.md` (usually also in the CSV).

**On phase 2 but already filed:** CSV hit, PDF already under `pdfs/{category}/`. Do not overwrite; report collision.

**Not on phase 2:** no CSV/`pdfs_not_downloaded` match. Leave in `pdfs/inbox/`. Do not invent a category. Report and ask before filing elsewhere.

Duplicate list entries for the same DOI/title (HTML vs plain title) count as **one** paper: one PDF files both; remove **all** matching list entries.

### 4. Rename and place

Naming: `{FirstAuthorSurname}_{YYYY}.pdf`

- Strip spaces and most punctuation from the surname; keep internal capitals and diacritics as in existing files (e.g. `Gabín-García_2021.pdf`, `deSouza_2023.pdf`, `vanZyl_2023.pdf`).
- If `{name}_{year}.pdf` already exists in that folder, ask before using a suffix (existing pattern: `Dalmon_2019-b.pdf`).
- Move with `mv` into `pdfs/{category}/` from the CSV `category` (must match the list section).
- Never delete unmatched inbox PDFs.

### 5. Update `pdfs_not_downloaded.md`

For each filed paper:

1. Remove the full list item (title bullet and indented DOI / best-link / notes lines).
2. Remove every duplicate entry for that DOI or same paper.
3. Set the section header count: `## {category} (N)` to the remaining items in that section.
4. Set the opening line count: `N articles without an automatically retrieved PDF` to the sum of all section `(N)` values.

Do not invent new list entries. Preserve Google-search link formatting on remaining items.

### 6. Update `README.md`

Recount from disk and the list (do not reuse stale chat numbers):

- **PDF have:** count `*.pdf` in each category folder under `pdfs/` (exclude `inbox` from the Total have).
- **PDF missing:** section `(N)` values in `pdfs_not_downloaded.md`.
- **Phase 2 records:** unchanged unless the CSV changed; take from the inventory table / CSV.

Refresh these README spots:

1. **Study selection** row: "PDFs on hand", "listed without PDF", and `Have + missing = … vs 148 sought (gap of …)`.
2. **Phase 2 full-text inventory** table: per-category have/missing, `inbox` row (unmatched count; note if not in phase 2), **Total** have/missing.
3. **PRISMA** node `E`: `Full-text PDF on hand n = …` and `Full-text PDF not on hand n = …`.
4. Inventory date in the `### Phase 2 full-text inventory (YYYY-MM-DD)` heading: set to today (ISO).

Minimal diff only. Do not rewrite unrelated README prose. No Cursor mentions in README.

### 7. Report

Short table:

| Inbox file | Match? | Destination | List removed? |
| --- | --- | --- | --- |

State new totals (have / missing / inbox leftover). Call out any unverified IDs or collisions.

## Hard rules

- Zero hallucinations: cite CSV path, list path, or extracted PDF text for every match.
- If unsure, leave in inbox and ask.
- Do not edit `notes/`.
- Do not `git commit` unless the user asks.
- No em dashes or emojis in files you write.

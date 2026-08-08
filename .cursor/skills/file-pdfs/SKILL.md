---
name: file-pdfs
description: >-
  Identify PDFs in pdfs/inbox/ (or a user-pointed drop folder such as
  temp/inbox/pdf-search/), match them to phase 2 records, rename and move
  them into the correct pdfs/ category folder, remove matched items from
  pdfs_download_links.md, and refresh README.md inventory counts. Use when
  the user adds PDFs to inbox, asks to file or rename PDFs, or to update
  pdfs_download_links or the phase 2 full-text inventory in README.
---

# File phase 2 PDFs

Process new full-text PDFs into the phase 2 library and keep the missing-PDF download-link list and README inventory in sync.

## Phase gate (hard stop)

Before any other step, verify all three exist on disk:

1. `input-phase2/relevant_articles_categorized.csv`
2. `input-phase2/pdfs_download_links.md`
3. `README.md` with study-selection / PRISMA skeleton

If any are missing: refuse, name the missing path(s), and stop. Do not invent stubs or placeholders. See `docs/adr/0001-phase-gated-agent-workflows.md` and `docs/adr/0006-file-pdfs-hard-stop-on-phase-gate.md`.

## Sources of truth

| Path | Role |
| --- | --- |
| `pdfs/inbox/` | Default drop zone for new PDFs |
| User-pointed folder (e.g. `temp/inbox/pdf-search/`) | Alternate drop zone when the user names it; process that folder instead of (or in addition to) `pdfs/inbox/` |
| `pdfs/{category}/` | Filed PDFs by screening category |
| `input-phase2/relevant_articles_categorized.csv` | Phase 2 records; `screening_category`, DOI, title, authors, year |
| `input-phase2/pdfs_download_links.md` | Missing PDFs: DOI / ResearchGate / DuckDuckGo links by category section; remove filed items and recount section `(N)` |
| `README.md` | Study-selection PDF counts, Phase 2 full-text inventory table, PRISMA `E` if present |

Category folder names must match CSV `screening_category` and the `## {section} (N)` headers in `pdfs_download_links.md`:

pdfs/
00-key-papers/
01-existing-products/
02-efficacy-mechanics-delivery/
    02a_efficacy/
    02b_strains_traits/
    02c_formulation_delivery/
03-autodissemination-social/
04-nontarget-ecotox/
05-regulatory-policy/
06-background-proxies/
07-vespideae-biocontrol/

For `02a` / `02b` / `02c`, file under `pdfs/02-efficacy-mechanics-delivery/{subcategory}/`.

## Workflow

Copy this checklist and track it:

```
- [ ] 1. List inbox PDFs
- [ ] 2. Identify each PDF (title, first author, year, DOI)
- [ ] 3. Match to CSV and pdfs_download_links
- [ ] 4. File Phase 2 matches (rename + move); file non-matches into `pdfs/06-background-proxies/`
- [ ] 5. Update pdfs_download_links.md
- [ ] 6. Recount and update README.md
- [ ] 7. Report results to user
```

### 1. List inbox PDFs

List `*.pdf` in `pdfs/inbox/`, or in the drop folder the user named. If empty, stop.

### 2. Identify each PDF

Do **not** trust the drop filename alone. Extract identity from the file:

1. Prefer PDF metadata title/author when present.
2. Else extract text from page 1 (Python `pypdf` / `PyPDF2` is fine; `pdftotext` if available). Use later pages if page 1 is cover/highlights only.
3. Record: title, first author surname, year, DOI (if present).

If identity cannot be verified, leave the file in the drop folder and flag it. Do not guess.

### 3. Match

For each identified PDF, search in order:

1. DOI against CSV `doi` and against DOI links in `pdfs_download_links.md`
2. Exact or near-exact title against CSV `title` and download-link titles
3. Author + year only as a weak check after title/DOI match

**On the list:** present in `pdfs_download_links.md` (usually also in the CSV).

**On phase 2 but already filed:** CSV hit, PDF already under `pdfs/{category}/`. Do not overwrite; report collision. Still remove the matching bullet from `pdfs_download_links.md` if the list still claims it is missing.

**Not on phase 2:** no CSV / download-links match. File into `pdfs/06-background-proxies/` with `{Surname}_{YYYY}.pdf` naming (same identity rules). Do not add rows to `pdfs_download_links.md` or the Phase 2 CSV. Report what was filed there.

Duplicate list entries for the same DOI/title count as **one** paper: one PDF files both; remove **all** matching list entries.

### 4. Rename and place

Naming: `{FirstAuthorSurname}_{YYYY}.pdf`

- Strip spaces and most punctuation from the surname; keep internal capitals, hyphens, and diacritics as in existing files (e.g. `Gabín-García_2021.pdf`, `deSouza_2023.pdf`, `vanZyl_2023.pdf`, `Nouri-Aiin_2021.pdf`).
- If `{name}_{year}.pdf` already exists in that folder, ask before using a suffix (existing pattern: `Dalmon_2019-b.pdf`).
- Destination category: CSV `screening_category` (primary).
- Move Phase 2 matches with `mv` into the matching `pdfs/` folder.
- Move non-Phase-2 identified PDFs into `pdfs/06-background-proxies/`.
- Never delete drop-folder PDFs that cannot be identified.

### 5. Update `pdfs_download_links.md`

For each filed (or already-on-hand collision) paper:

1. Remove the matching bullet (match DOI and/or year + title). Include indented continuation bullets that belong to the same paper.
2. Recount each `## {section} (N)` header from remaining bullets under that section (allow leading whitespace on bullets).
3. Set the opening line count to the sum of remaining bullets.

Do not invent new link entries. Preserve notes and link formatting on remaining items.

### 6. Update `README.md`

Recount from disk and the download-link list (do not reuse stale chat numbers):

- **PDF have:** count `*.pdf` in each category folder under `pdfs/` (exclude `inbox` from the Total have; note `07-vespideae-biocontrol` separately if the README treats it as supplemental).
- **PDF missing:** section `(N)` values in `pdfs_download_links.md`.
- **Phase 2 includes with PDF on hand:** `accepted includes − listed missing` (must equal 254 when includes = 254 and the list is complete).

Refresh these README spots when present:

1. **Study selection** rows: PDFs on hand, listed without PDF, Have + missing.
2. **Phase 2 full-text inventory** table: per-category have/missing, `inbox` row, Total; set heading date to today (ISO).
3. **PRISMA** node `E` if the README has one: on-hand / not-on-hand counts.
4. Any cite-level PDF yes/no flags for newly filed key papers.

Minimal diff only. Do not rewrite unrelated README prose. No Cursor mentions in README.

### 7. Report

Short table:

| Inbox file | Match? | Destination | List removed? |
| --- | --- | --- | --- |

State new totals (have / missing / drop-folder leftover). Call out unverified IDs, collisions, and not-on-phase-2 leftovers.

## Hard rules

- Zero hallucinations: cite CSV path, list path, or extracted PDF text for every match.
- If unsure, leave in the drop folder and ask.
- Do not edit `notes/`.
- Do not `git commit` unless the user asks.
- No em dashes or emojis in files you write.

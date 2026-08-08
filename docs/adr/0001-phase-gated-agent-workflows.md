# Phase-gated agent workflows

Agent skills cover both search documentation and Phase 2 PDF/inventory work, but Phase 2 workflows may run only after named on-disk inputs exist. Chosen over search-only or Phase-2-only guidance so early sessions stay on databases/strings/hit counts while later filing skills remain available without premature invocation.

**Gate (all required):** `input-phase2/relevant_articles_categorized.csv`, `input-phase2/pdfs_not_downloaded.md`, and a README with study-selection / PRISMA skeleton.

## Considered Options

- Search documentation only in always-on context
- Phase 2 filing/inventory only
- Both, with an explicit phase gate (accepted)
- Gate on CSV only, or CSV + missing-PDF list (rejected: incomplete for `@file-pdfs` recount)

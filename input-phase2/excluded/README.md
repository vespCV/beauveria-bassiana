# Phase 2 exclusions (excluded)

In-repo audit trail for full-text exclusions synced from Zotero.

| File | Role |
| --- | --- |
| `records.csv` | Excluded items (citekey, doi, title, year, surname, source) |
| `pdfs/excluded/` | Filed PDFs for excluded items |

## Preferred Zotero signal

Export **only** Zotero collection `excluded` as BibTeX to:

`temp/zotero/excluded.bib`

Until that export exists, `@zotero-sync` reads collection `excluded` from a copy of `/Users/md/Zotero/zotero.sqlite` (legacy collection name `99-excluded` still accepted).

A full-library file such as `~/Downloads/Mijn Bibliotheek.bib` is ignored when it is clearly larger than the exclusion set.

## Sync

```sh
python3 .cursor/skills/zotero-sync/scripts/zotero_sync.py
python3 .cursor/skills/zotero-sync/scripts/zotero_sync.py --apply
```

Include CSV (`relevant_articles_categorized.csv`) holds current includes only after a successful exclusion sync.

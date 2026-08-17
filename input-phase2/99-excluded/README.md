# Phase 2 exclusions (99-excluded)

In-repo audit trail for full-text exclusions synced from Zotero.

| File | Role |
| --- | --- |
| `records.csv` | Excluded items (citekey, doi, title, year, surname, source) |
| `pdfs/99-excluded/` | Filed PDFs for excluded items |

## Preferred Zotero signal

Export **only** Zotero collection `99-excluded` as BibTeX to:

`temp/zotero/99-excluded.bib`

Until that export exists, `@zotero-sync` reads collection `99-excluded` from a copy of `/Users/md/Zotero/zotero.sqlite`.

A full-library file such as `~/Downloads/Mijn Bibliotheek.bib` is ignored when it is clearly larger than the exclusion set.

## Sync

```sh
python3 .cursor/skills/zotero-sync/scripts/zotero_sync.py
python3 .cursor/skills/zotero-sync/scripts/zotero_sync.py --apply
```

Include CSV (`relevant_articles_categorized.csv`) holds current includes only after a successful exclusion sync.

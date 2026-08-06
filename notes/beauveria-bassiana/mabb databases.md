## Database template (all subquestions)

Run and log for every subquestion:

1. **PubMed** (reuse the same string on **Europe PMC**)
2. **Google Scholar** (scan first 5 pages for relevance; export or record hits as documented)

Also:

3. **Dimensions** — required for `01-existing-products` and `05-regulatory-policy` (publications + patents + policy); optional for other subquestions
4. **Lens.org**, **EPA Biopesticide**, **EU Pesticide Database**, **CABI**, **Espacenet** / **Google Patents** — only for `01-existing-products` and `05-regulatory-policy`, each with its own short string in that subquestion note

Do **not** treat Semantic Scholar as a separate logged database unless a run is actually performed and documented.

**Citation chaining:** ResearchRabbit (or equivalent) from seed papers; not a substitute for the database runs above.

## Raw export filenames (locked 2026-08-06)

Save under `search-results/raw/`:

```
{subquestion}_{YYYY-MM-DD}_{database}_{run-label}.{ext}
```

- **subquestion:** `01`, `02a`, `02b`, `02c`, `03`, `04`, `05`, or `06`
- **database:** `pubmed`, `europepmc`, `scholar`, `dimensions`, `lens`, `espacenet`, `googlepatents`, `epa`, `eu-ppp`, `cabi`
- **run-label:** short kebab case (`market-catalogue`, `delivery-systems`, or `main`)
- **ext:** `ris`, `nbib`, `xml`, `csv`, `ciw`, or `txt` as exported

Examples:

- `01_2026-08-07_pubmed_market-catalogue.nbib`
- `01_2026-08-07_pubmed_delivery-systems.nbib`
- `02a_2026-08-07_scholar_main.txt`

If an export cannot be downloaded, still log hit count in `mabb literature search and setup database.md` and note "no file" in the log row.

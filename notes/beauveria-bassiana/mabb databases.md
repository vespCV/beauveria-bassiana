## Database template (all subquestions)

Run and log for every subquestion:

1. **PubMed** (reuse the same string on **Europe PMC**)
2. **Google Scholar** (scan first 5 pages for relevance; export or record hits as documented)

Also:

3. **Dimensions** — required for `01-existing-products` and `05-regulatory-policy` (publications + patents + policy); optional for other subquestions
4. **Lens.org**, **EPA Biopesticide**, **EU Pesticide Database**, **CABI**, **Espacenet** / **Google Patents** — only for `01-existing-products` and `05-regulatory-policy`, each with its own short string in that subquestion note

Do **not** treat Semantic Scholar as a separate logged database unless a run is actually performed and documented.

**PubMed and Google Scholar:** Match term-for-term unless a subquestion note documents deliberate asymmetry (e.g. PubMed broader, no delivery AND, with Phase 1 narrowing). Europe PMC reuses the PubMed string. Wildcards: PubMed may use truncations (`encapsulat*`, `thermotoleran*`) where Scholar uses spelled-out synonyms.

**Citation chaining:** ResearchRabbit (or equivalent) from seed papers; not a substitute for the database runs above.

## Raw export filenames (locked 2026-08-06; run-label dropped 2026-08-07)

One bibliographic string per subquestion per database. Save under `input-phase0/input-rayyan/`:

```
{subquestion}_{YYYY-MM-DD}_{database}.{ext}
```

- **subquestion:** `01`, `02a`, `02b`, `02c`, `03`, `04`, `05`, or `06`
- **database:** `pubmed`, `europepmc`, `scholar`, `dimensions`, `lens`, `espacenet`, `googlepatents`, `epa`, `eu-ppp`, `cabi`
- **ext:** `ris`, `nbib`, `xml`, `csv`, `ciw`, or `txt` as exported

Examples:

- `01_2026-08-07_pubmed.nbib`
- `02a_2026-08-07_scholar.txt`

If an export cannot be downloaded, still log hit count in `mabb literature search and setup database.md` and note "no file" in the log row.

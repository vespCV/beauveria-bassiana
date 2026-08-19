# Methods lab journal

Open
- request papers that we need from the missing pdf's list
- google scholar search
- EPA Biopesticide, EU Pesticides Database, CABI, Espacenet/Google Patents




Process record for the systematic review of *Beauveria bassiana* (Bb) for catch-infect-release against *Vespa velutina*. Scientific search design lives in `notes/beauveria-bassiana/`. Raw exports live in `input-phase0/`. Deduplicated records live in `input-phase1/`. Includes and exclusion audit live in `input-phase2/`.

## Applied question

Evidence for efficacy, strain traits, formulation and delivery, horizontal transmission, non-target risk, and regulatory readiness of Bb when spores are delivered in a selective trap, bait station, or autodissemination device so that the target insect acquires and vectors the fungus (`notes/beauveria-bassiana/mabb research questions.md`).

*V. velutina* is the applied motivation. Inclusion keeps transferable evidence from other taxa when the intervention or pathway informs that delivery model.

## Question and search strings

Online working session recorded in `notes/beauveria-bassiana/mabb documentation.md`: title, research question, search strings, Rayyan year handling.

Consensus.app coverage checks ran before database lock: one natural-language ask per subquestion; Deep off; Medical mode and extra Filter chips unused. Hits were used to add strain codes, product names, and delivery synonyms to the locked strings. Consensus hits are vocabulary for strings; they are outside the PRISMA corpus.

Subquestion ids: `01-existing-products`, `02a_efficacy`, `02b_strains_traits`, `02c_formulation_delivery`, `03-autodissemination-social`, `04-nontarget-ecotox`, `05-regulatory-policy`, `06-background-proxies` (reserve).

## 2026-08-07: database runs and Rayyan upload

Locked strings: `notes/beauveria-bassiana/mabb search str *.md` (copied in [search-log.md](search-log.md)).

Bibliographic databases for every subquestion: PubMed (same string reused on Europe PMC) and Google Scholar (first five pages). Dimensions required for `01` and `05`. Registry and patent sources for `01` and `05` as listed in `notes/beauveria-bassiana/mabb databases.md`.

Export filenames: `{subquestion}_{YYYY-MM-DD}_{database}.{ext}` under `input-phase0/input-rayyan/`. Date on the tracked files is 2026-08-07.

Rayyan upload set (hardened splits) in `input-phase0/input-rayyan/split/README.md`:

| group | source | raw records | kept | n_files |
|---|---|---:|---:|---:|
| 01 | dimensions | 500 | 500 | 3 |
| 01 | europepmc | 5615 | 5536 | 25 |
| 01 | pubmed | 1790 | 1787 | 3 |
| 02a | europepmc | 630 | 608 | 3 |
| 02a | pubmed | 39 | 39 | 1 |
| 02b | europepmc | 2174 | 2149 | 10 |
| 02b | pubmed | 188 | 188 | 1 |
| 02c | europepmc | 1882 | 1852 | 9 |
| 02c | pubmed | 62 | 62 | 1 |
| 03 | europepmc | 341 | 336 | 2 |
| 03 | pubmed | 22 | 22 | 1 |
| 04 | europepmc | 2731 | 2686 | 13 |
| 04 | pubmed | 628 | 628 | 1 |
| 05 | europepmc | 2857 | 2820 | 13 |
| 05 | pubmed | 751 | 750 | 1 |
| 06 | europepmc | 282 | 270 | 2 |

Citation chaining: CitationChaser / ResearchRabbit seeds in `input-phase0/input-cc-rr/`. Those seeds supplement the database runs.

## Deduplication (Rayyan)

From `notes/beauveria-bassiana/mabb duplicates removed.md`:

| Stage | n |
|---|---:|
| Records identified | 16,748 |
| Unique records after unduplication | 6,250 |
| Unique records in English | 5,741 |

Duplicates removed: 10,498 (16,748 − 6,250).

## Phase 1: title and abstract (ASReview)

Deduplicated corpus: `input-phase1/`. English unique set documented as 5,741 in `notes/beauveria-bassiana/mabb unique items for phase 1 screening.md`. All 6,250 unique records were labeled (English and other languages).

| Stage | n |
|---|---:|
| Phase 1 screened | 6,250 |
| Phase 1 excluded | 5,996 |
| Phase 2 sought (Phase 1 includes) | 254 |

## Phase 2: full text

Include list: `input-phase2/relevant_articles_categorized.csv` (208 rows). Exclusion audit: `input-phase2/excluded/records.csv`.

| Stage | n |
|---|---:|
| Phase 2 sought | 254 |
| Phase 2 excluded from that set | 48 |
| Studies included | 208 |
| PDFs on disk (flat include library) | 114 |
| Includes with matched PDF | 89 |
| Includes without PDF | 119 |

Phase 1 includes by primary category (n = 254) and Phase 2 includes (n = 208) are tabulated in the README study-selection section.

PDFs are filed flat under `pdfs/` (`{Surname}_{YYYY}.pdf` for includes). Exclusions stay in `pdfs/excluded/`. Screening category ids remain in the CSV and Zotero collections.

## 2026-08-18: full-text extraction pass (28 citekeys)

Reconciled flat `pdfs/` library after moving nine leaked exclusion PDFs to `pdfs/excluded/` and removing two duplicate files. Flat include library: 114 PDFs. Re-included Merino2007 and Konopicka2024 in `relevant_articles_categorized.csv`; removed both from exclusion audit. Updated `00-key-papers/extract.csv` canonical `pdf_filename` values (Merino_2007, Reason_2022, VanZyl_2024, DeSouza_2023, Rose_1999, Cappa_2024, DeFazi_2025). Full-text pass on 28 on-disk citekeys: all rows reconciled to `evidence=full-text` except homonym Zhang2025 Liriomyza sativae row (no PDF) and MayorgaCh2021 (REQUEST). Gap report: `temp/handoff/full-text-pass-gap.md`. REQUEST list: `input-phase2/pdfs_request_list.md`.

## Extraction and annotation

Category extract tables live under `input-phase2/` (for example `02a_efficacy/extract.csv`). Zotero highlight exports used for chapter pages: `notes/beauveria-bassiana/zotero/`.
## 2026-08-19: full-text extraction pass (114 PDFs)

Read every flat include PDF under `pdfs/` (114 files: 113 full-text rows plus Fouillaud1995 documented skip). Created 45 extract rows; updated 90+ existing rows. Added `input-phase2/01-existing-products/papers.csv` (Smith2000, Aristizabal2017, Sybilska2025) and populated `06-background-proxies/extract.csv` (12 rows). Catalogue evidence flips: 9. Homonym splits: Zhang2025/Zhang2025b; Srei2020/Srei2020b; Unknown2025→Li2025. Skipped not-full-text: Fouillaud1995 (PestinfoWiki abstract page). REQUEST/no-PDF unchanged: MayorgaCh2021, Peng2020ao, Almeida2022ao. Worklist: `temp/handoff/full-text-pass-worklist.csv`.

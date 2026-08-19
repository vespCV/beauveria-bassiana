# Canonical screening category ids are 01–06, plus supplemental 00 and 07

Screening category ids (`01-existing-products` through `06-background-proxies`, including `02a`/`02b`/`02c`) live in the include CSV, Zotero collections, and `@file-pdfs` / `@zotero-sync` logic.

On disk, include PDFs sit flat under `pdfs/` as `{Surname}_{YYYY}.pdf`. Only full-text exclusions use a subfolder: `pdfs/excluded/`. Unfiled drops stay in `pdfs/inbox/`. Category membership is not encoded by folder path.

Supplemental lanes (not subquestions of the Bb delivery review, but still tagged in CSV/Zotero):

- `00-key-papers`: Beauveria (especially *B. bassiana*) evidence on *Vespa velutina* or other Vespidae
- `07-vespideae-biocontrol`: Vespidae biocontrol with non-Bb microorganisms (other fungi, bacteria, viruses, nematodes, related pathogens) plus chemical trap/bait delivery proxies

Do not revive zero-based renames of the systematic ids (for example `00-existing-products`). Chosen to keep the `01`–`06` review tree stable while allowing applied Vespidae lanes from the prior velutina project.

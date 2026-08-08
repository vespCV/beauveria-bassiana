# Rayyan upload set (hardened)

CRLF RIS/NBIB from `input-phase0/input-rayyan/`. Upload only `*.ris` and `*.nbib` (not README/MANIFEST).

Hardening: dropped AD; stripped quotes/angle brackets; AB truncated to 1500 chars; authors capped at 25; ~400 KB europepmc/dimensions chunks.

## Coverage

| group | source | raw | kept | n_files |
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

## Retest first

`04_…_europepmc_part2of13.ris` failed. Replaced by ultra-minimal splits (PMC-AN / EFSA-style titles dropped):
- `04_2026-08-07_europepmc_part2a-of13.ris`
- `04_2026-08-07_europepmc_part2b-of13.ris`

Optional bisect: `split/_bisect_04_part2/`.

## Notes
- Lens patents omitted.
- Dropped: corrections/retractions, patents, no title/author.


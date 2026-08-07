### 01-existing-products

Two logged runs per bibliographic database. Registry sources (EPA, EU, CABI) use the catalogue concept only.

Strain/product OR-group updated 2026-08-06 from EPA/EU registry pass; formulation/product terms updated 2026-08-07 from Consensus `01-existing-products` pass; PubMed/Scholar parity and catalogue formulation terms updated 2026-08-07 from free-database string audit. Bare numeric strain ids (447, 203, 147) stay out of Boolean OR-groups (high false-positive risk); use `"strain 447"` only if a run needs them. Do not use bare `OD` or `ES` tokens (noise). Skip bare `Bb` or `TBb` (high false-positive risk).

#### Market catalogue (broad)

No trap/bait requirement.

**Google Scholar**

```
"Beauveria bassiana" (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR "wettable powder" OR "oil dispersion" OR "emulsifiable suspension" OR "emulsifiable oil" OR "technical concentrate" OR "aqueous suspension" OR granular OR encapsulat* OR "seed coat*" OR nanoemulsion OR biopolymer OR strain OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR BW149 OR IMI389521 OR NPP111B005 OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer OR Bioceres OR LALGUARD OR Aprehend OR balEnce OR Phoemyc)
```

**PubMed** (same string on Europe PMC)

```
"Beauveria bassiana"[Title/Abstract] AND (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR "wettable powder" OR "oil dispersion" OR "emulsifiable suspension" OR "emulsifiable oil" OR "technical concentrate" OR "aqueous suspension" OR granular OR encapsulat* OR "seed coat*" OR nanoemulsion OR biopolymer OR strain OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR BW149 OR IMI389521 OR NPP111B005 OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer OR Bioceres OR LALGUARD OR Aprehend OR balEnce OR Phoemyc)
```

**Dimensions** (publications + patents)

```
"Beauveria bassiana" (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer)
```

**Lens.org**

```
"Beauveria bassiana" (product OR biopesticide OR mycoinsecticide OR formulation OR GHA OR "ATCC 74040" OR KTU-24 OR Pa-4 OR BotaniGard OR Mycotrol OR Naturalis)
```

**Google Patents / Espacenet**

```
"Beauveria bassiana" (biopesticide OR mycoinsecticide OR formulation OR product OR strain OR GHA OR "wettable powder" OR "oil dispersion" OR "technical concentrate" OR "aqueous suspension" OR bait)
```

**EPA Biopesticide** (`epa.gov`)

```
"Beauveria bassiana"
```

**EU Pesticide Database**

```
"Beauveria bassiana"
```

**CABI**

```
"Beauveria bassiana" (biopesticide OR mycoinsecticide OR product OR formulation OR strain)
```

#### Delivery systems (narrow)

**Google Scholar**

```
"Beauveria bassiana" (trap OR "bait station" OR bait OR autodissemination OR "auto-dissemination" OR "inoculum station" OR "contamination device" OR "attract and infect")
```

**PubMed** (same string on Europe PMC)

```
"Beauveria bassiana"[Title/Abstract] AND (trap OR bait OR autodissemination OR "auto-dissemination" OR "bait station" OR "inoculum station" OR "contamination device" OR "attract and infect")
```

**Dimensions**

```
"Beauveria bassiana" (trap OR bait OR autodissemination OR "bait station" OR "attract and infect")
```

**Lens.org / Google Patents / Espacenet**

```
"Beauveria bassiana" (trap OR bait OR autodissemination OR "bait station")
```

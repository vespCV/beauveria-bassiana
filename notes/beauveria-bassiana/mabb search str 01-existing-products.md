### 01-existing-products

One logged string per bibliographic database (product/strain/formulation catalogue). No trap/bait AND: registry and commercial product papers must not be dropped. Trap/bait/autodissemination device trials are covered by `02a`, `02c`, and `03`. Registry sources (EPA, EU, CABI) use the bare species name or a short product string as below.

Strain/product OR-group updated 2026-08-06 from EPA/EU registry pass; formulation/product terms updated 2026-08-07 from Consensus `01-existing-products` pass; PubMed/Scholar parity and catalogue formulation terms updated 2026-08-07 from free-database string audit; dual delivery-systems run removed 2026-08-07 (one string per subquestion). Bare numeric strain ids (447, 203, 147) stay out of Boolean OR-groups (high false-positive risk); use `"strain 447"` only if a run needs them. Do not use bare `OD` or `ES` tokens (noise). Skip bare `Bb` or `TBb` (high false-positive risk).

**Google Scholar**

```
"Beauveria bassiana" (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR "wettable powder" OR "oil dispersion" OR "emulsifiable suspension" OR "emulsifiable oil" OR "technical concentrate" OR "aqueous suspension" OR granular OR encapsulat* OR "seed coat*" OR nanoemulsion OR biopolymer OR strain OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR BW149 OR IMI389521 OR NPP111B005 OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer OR Bioceres OR LALGUARD OR Aprehend OR balEnce OR Phoemyc)
```

X **PubMed** 
```
"Beauveria bassiana"[Title/Abstract] AND (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR "wettable powder" OR "oil dispersion" OR "emulsifiable suspension" OR "emulsifiable oil" OR "technical concentrate" OR "aqueous suspension" OR granular OR encapsulat* OR "seed coat*" OR nanoemulsion OR biopolymer OR strain OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR BW149 OR IMI389521 OR NPP111B005 OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer OR Bioceres OR LALGUARD OR Aprehend OR balEnce OR Phoemyc)
```

X**PMC**
```
"Beauveria bassiana" AND (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR "wettable powder" OR "oil dispersion" OR "emulsifiable suspension" OR "emulsifiable oil" OR "technical concentrate" OR "aqueous suspension" OR granular OR encapsulat* OR "seed coat*" OR nanoemulsion OR biopolymer OR strain OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR BW149 OR IMI389521 OR NPP111B005 OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer OR Bioceres OR LALGUARD OR Aprehend OR balEnce OR Phoemyc)
```

X**Dimensions** (publications + patents) export as RIS
[https://app.dimensions.ai/](https://app.dimensions.ai/)
```
"Beauveria bassiana" (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer)
```

X**Lens.org**
```
"Beauveria bassiana" (product OR biopesticide OR mycoinsecticide OR formulation OR GHA OR "ATCC 74040" OR KTU-24 OR Pa-4 OR BotaniGard OR Mycotrol OR Naturalis)
```

- **Google Patents / Espacenet** later 7286 hist
https://worldwide.espacenet.com/searchResults?ST=singleline&locale=en_EP&submitted=true&DB=&query=%22Beauveria+bassiana%22
```
"Beauveria bassiana"
```

- **EPA Biopesticide** (`epa.gov`) later US
```
"Beauveria bassiana"
```

- **EU Pesticide Database** maybe later
The EU Pesticides Database allows users to search for information on active substances used in plant protection products, Maximum Residue Levels (MRLs) in food products, and emergency authorisations of plant protection products in Member States.
```
"Beauveria bassiana"
```

**CABI**
https://www.cabidigitallibrary.org/
```
"Beauveria bassiana" (biopesticide OR mycoinsecticide OR product OR formulation OR strain)
```

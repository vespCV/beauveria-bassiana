# Search log

Locked strings from `notes/beauveria-bassiana/mabb search str *.md`.

Europe PMC reused the PubMed string. Export record counts: `input-phase0/input-rayyan/split/README.md`.

## Databases planned per subquestion

From `notes/beauveria-bassiana/mabb databases.md`: PubMed + Europe PMC + Google Scholar (first five pages) for every subquestion. Dimensions required for `01` and `05`. Lens.org, EPA Biopesticide, EU Pesticides Database, CABI, Espacenet / Google Patents for `01` and `05`.

## 01-existing-products

**Google Scholar**

```
"Beauveria bassiana" (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR "wettable powder" OR "oil dispersion" OR "emulsifiable suspension" OR "emulsifiable oil" OR "technical concentrate" OR "aqueous suspension" OR granular OR encapsulat* OR "seed coat*" OR nanoemulsion OR biopolymer OR strain OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR BW149 OR IMI389521 OR NPP111B005 OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer OR Bioceres OR LALGUARD OR Aprehend OR balEnce OR Phoemyc)
```

Hits (first five pages): **[to be verified]**

**PubMed** (same string on Europe PMC)

```
"Beauveria bassiana"[Title/Abstract] AND (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR "wettable powder" OR "oil dispersion" OR "emulsifiable suspension" OR "emulsifiable oil" OR "technical concentrate" OR "aqueous suspension" OR granular OR encapsulat* OR "seed coat*" OR nanoemulsion OR biopolymer OR strain OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR BW149 OR IMI389521 OR NPP111B005 OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer OR Bioceres OR LALGUARD OR Aprehend OR balEnce OR Phoemyc)
```

| Source | Records in export |
|---|---:|
| PubMed | 1790 raw / 1787 kept |
| Europe PMC | 5615 raw / 5536 kept |

**Dimensions** (publications + patents)

```
"Beauveria bassiana" (product OR commercial OR registered OR biopesticide OR mycoinsecticide OR formulation OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR KTU-24 OR Pa-4 OR BKN20 OR BotaniGard OR Mycotrol OR Naturalis OR Velifer)
```

Records in export: 500 raw / 500 kept.

**Lens.org**

```
"Beauveria bassiana" (product OR biopesticide OR mycoinsecticide OR formulation OR GHA OR "ATCC 74040" OR KTU-24 OR Pa-4 OR BotaniGard OR Mycotrol OR Naturalis)
```

**Espacenet / Google Patents**

```
"Beauveria bassiana"
```

**EPA Biopesticide**, **EU Pesticides Database**, **CABI**: species or short product string as in the `01` note.

## 02a_efficacy

**Google Scholar**

```
"Beauveria bassiana" (LT50 OR LT90 OR LC50 OR LC90 OR "mortality rate" OR "time to death" OR "kill rate" OR "population reduction" OR fecundity OR sublethal) (trap OR bait OR "bait station" OR autodissemination OR "auto-dissemination" OR "attract and infect" OR "horizontal transmission")
```

**[to do later]**

**PubMed** / Europe PMC

```
"Beauveria bassiana"[Title/Abstract] AND (LT50 OR LT90 OR LC50 OR LC90 OR mortality OR "time to death" OR "population reduction" OR fecundity OR sublethal) AND (trap OR bait OR "bait station" OR autodissemination OR "auto-dissemination" OR "attract and infect" OR "horizontal transmission")
```

| Source | Records in export |
|---|---:|
| PubMed | 39 raw / 39 kept |
| Europe PMC | 630 raw / 608 kept |

## 02b_strains_traits

**Google Scholar**

```
"Beauveria bassiana" (strain OR isolate OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR KTU-24 OR Pa-4) (Pr1 OR Pr2 OR protease OR subtilisin OR trypsin OR chitinase OR exochitinase OR endochitinase OR hydrophobin OR hydrophobicity OR thermotolerant OR thermotolerance OR "UV tolerance" OR adhesion OR "cuticle penetration" OR "cuticle degrading" OR sclerotized OR melanized) (virulence OR "spore germination")
```

Hits: **[to do later]**

**PubMed** / Europe PMC

```
"Beauveria bassiana"[Title/Abstract] AND (strain OR isolate OR GHA OR "ATCC 74040" OR HF23 OR ANT-03 OR "PPRI 5339" OR KTU-24 OR Pa-4) AND (Pr1 OR Pr2 OR protease OR subtilisin OR trypsin OR chitinase OR exochitinase OR endochitinase OR hydrophobin OR hydrophobicity OR thermotoleran* OR "UV tolerance" OR UV toleran* OR adhesion OR "cuticle degrading" OR "cuticle penetration" OR cuticle OR sclerotized OR melanized) AND (virulence OR germination)
```

| Source | Records in export |
|---|---:|
| PubMed | 188 raw / 188 kept |
| Europe PMC | 2174 raw / 2149 kept |

## 02c_formulation_delivery

**Google Scholar**

```
"Beauveria bassiana" (formulation OR "wettable powder" OR "oil suspension" OR "oil dispersion" OR emulsion OR "emulsifiable concentrate" OR "water dispersible" OR microencapsulated OR microencapsulation OR hydrogel OR microgranule OR biopolymer OR adjuvant OR surfactant OR protein OR fluid OR carrier OR bait) ("spore viability" OR viability OR persistence OR "shelf life" OR storage OR adhesion OR germination OR transfer OR "horizontal transmission") (trap OR bait OR "bait station" OR autodissemination OR "auto-dissemination" OR autoinoculation OR "attract and infect" OR ovitrap OR "lure and kill" OR field)
```

Hits: **[to do later]**

**PubMed** / Europe PMC

```
"Beauveria bassiana"[Title/Abstract] AND (formulation OR "wettable powder" OR "oil suspension" OR "oil dispersion" OR emulsion OR "emulsifiable concentrate" OR "water dispersible" OR microencapsulat* OR hydrogel OR microgranule OR biopolymer OR adjuvant OR surfactant OR protein OR fluid OR carrier OR bait) AND (viability OR persistence OR "shelf life" OR storage OR adhesion OR germination OR transfer OR "horizontal transmission") AND (trap OR bait OR "bait station" OR autodissemination OR autoinoculation OR "attract and infect" OR ovitrap OR "lure and kill" OR field)
```

| Source | Records in export |
|---|---:|
| PubMed | 62 raw / 62 kept |
| Europe PMC | 1882 raw / 1852 kept |

## 03-autodissemination-social

PubMed is broader than Scholar (delivery AND omitted on PubMed). Narrow at Phase 1.

**Google Scholar**

```
"Beauveria bassiana" ("auto-dissemination" OR autodissemination OR autoinoculation OR "auto-inoculation" OR autocontamination OR "auto-contamination" OR disseminator OR "horizontal transmission" OR "social immunity" OR allogrooming OR necrophoresis OR trophallaxis OR "nest hygiene" OR "social insect") (trap OR bait OR forager OR nestmate OR queen OR eusocial OR Hymenoptera OR ant OR termite OR wasp)
```

Hits: **[to do later]**

**PubMed** / Europe PMC

```
"Beauveria bassiana"[Title/Abstract] AND ("horizontal transmission" OR autodissemination OR autoinoculation OR "auto-inoculation" OR autocontamination OR "auto-contamination" OR "social immunity" OR allogrooming OR necrophoresis OR trophallaxis OR "nest hygiene" OR "social insect")
```

| Source | Records in export |
|---|---:|
| PubMed | 22 raw / 22 kept |
| Europe PMC | 341 raw / 336 kept |

## 04-nontarget-ecotox

PubMed is broader than Scholar.

**Google Scholar**

```
"Beauveria bassiana" ("non-target" OR nontarget OR "Apis mellifera" OR Bombus OR pollinator OR "native bee" OR "off-target" OR ecotoxicology OR "environmental persistence" OR "secondary transmission" OR sublethal OR "natural enemy" OR beneficial OR parasitoid OR predator OR "social wasp") (trap OR bait OR selectivity OR attractant OR autodissemination OR disseminator OR apivectoring OR entomovectoring OR "bee-vectored" OR "sterile insect")
```

Hits: **[to be verified]**

**PubMed** / Europe PMC

```
"Beauveria bassiana"[Title/Abstract] AND ("non-target" OR nontarget OR "Apis mellifera" OR Bombus OR pollinator OR "native bee" OR "off-target" OR ecotoxicology OR "environmental persistence" OR "secondary transmission" OR sublethal OR "natural enemy" OR beneficial OR parasitoid OR predator OR "social wasp" OR selectivity OR attractant)
```

| Source | Records in export |
|---|---:|
| PubMed | 628 raw / 628 kept |
| Europe PMC | 2731 raw / 2686 kept |

## 05-regulatory-policy

**Google Scholar**

```
"Beauveria bassiana" (registration OR biopesticide OR regulatory OR IPM OR "integrated pest management" OR quarantine OR "emergency use" OR "statutory control" OR "risk assessment" OR EFSA OR "1107/2009" OR "peer review" OR "pesticide risk assessment" OR "data requirement" OR "data gap" OR "emergency authorisation" OR "emergency authorization" OR "active substance" OR rapporteur OR Netherlands) (trap OR bait OR formulation OR device OR autodissemination OR autoinoculation OR "bait station" OR "attract and infect")
```

Hits: **[to do later]**

**PubMed** / Europe PMC

```
"Beauveria bassiana"[Title/Abstract] AND (registration OR biopesticide OR regulatory OR "integrated pest management" OR quarantine OR "emergency use" OR EFSA OR "1107/2009" OR "peer review" OR "pesticide risk assessment" OR "data requirement" OR "data gap" OR "emergency authorisation" OR "emergency authorization" OR "active substance" OR rapporteur OR Netherlands)
```

| Source | Records in export |
|---|---:|
| PubMed | 751 raw / 750 kept |
| Europe PMC | 2857 raw / 2820 kept |

**Dimensions**

```
"Beauveria bassiana" (registration OR biopesticide OR regulatory OR quarantine OR "emergency use" OR "risk assessment" OR EFSA OR "1107/2009" OR "peer review" OR "pesticide risk assessment" OR "data requirement" OR "data gap" OR "emergency authorisation" OR "emergency authorization" OR "active substance" OR rapporteur OR Netherlands)
```

Records in export: **[to do later]** (Dimensions split README lists a 01 dimensions file only).

**Lens.org**

```
"Beauveria bassiana" (registration OR biopesticide OR quarantine OR EFSA OR "1107/2009" OR "peer review" OR "data requirement" OR rapporteur OR Netherlands)
```

Hits: **[to be verified]**

**Espacenet / Google Patents**

```
"Beauveria bassiana" (registration OR regulatory OR biopesticide OR trap OR bait OR autodissemination OR autoinoculation)
```

Hits: **[to do later]**

## 06-background-proxies

**Google Scholar**

```
"Beauveria bassiana" (biology OR pathogenesis OR "mode of action" OR "life cycle" OR epizootic OR review) (Vespa OR Vespidae OR Formicidae OR termite OR Isoptera OR "social insect")
```

Hits: **[to do later]**

**PubMed** / Europe PMC

```
"Beauveria bassiana"[Title/Abstract] AND (pathogenesis OR "mode of action" OR review) AND (Vespa OR ant OR termite OR "social insect")
```

| Source | Records in export |
|---|---:|
| Europe PMC | 282 raw / 270 kept |
| PubMed | **[to do later]** (no `06` PubMed file in the split README table) |

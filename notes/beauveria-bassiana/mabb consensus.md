# Consensus coverage check

Authority: `docs/adr/0011-consensus-coverage-check.md`. Pillars align with `mabb research questions.md`.

## Purpose

Consensus.app Copilot/Pro only. Ranked key papers per pillar to gap-check categories, research questions, and search strings before database runs are locked.

Not the systematic corpus. Not PRISMA evidence.

## Shared output block (append to every Copilot)

```
Return:
1. A ranked list of about 8–15 most important papers (title, year, DOI or PMID when available, one sentence on why it matters for this pillar).
2. A separate "vocabulary for search strings" list: strain codes, commercial product names, formulation or carrier terms, and delivery-device terms that appear in those papers.
Do not use hard mortality or LT thresholds as inclusion filters. Prefer studies that use selective traps, bait stations, autodissemination devices, or fluid/oil/protein carriers when such studies exist; include transferable mechanism papers when they clearly inform that delivery model.
```

## Triage after each run

- Theme absent from subquestions or categories → revise questions/categories
- Missing synonyms, strain codes, or product names → revise search strings
- Out-of-scope or background-only noise → ignore (do not open `06` unless this keeps happening)

## Parallel pass (not Consensus)

**01 market catalogue:** EPA Biopesticide lists, EU Pesticide Database, CABI, Espacenet / Google Patents. Capture product names, strain codes, and formulation types for string updates.

## Skip

**06-background-proxies:** no Consensus Copilot unless pillars `02`–`05` repeatedly surface background-only themes that suggest a missing upstream question.

---

## 01-existing-products (Consensus: delivery systems + strains)

**Copilot/Pro**

```
What are the most important papers on commercial or experimental Beauveria bassiana products, formulations, and selective delivery systems (traps, bait stations, autodissemination devices) that use liquid, oil, wettable powder, protein, or bait-based spore carriers? Emphasise named strains and product codes, device designs, and how spores are presented so a target insect contacts and acquires them. Exclude broad crop-spray efficacy trials unless they also describe trap, bait, or autodissemination delivery.
```

Then append the shared output block.

---

## 02a_efficacy

**Copilot/Pro**

```
What are the most important papers on mortality, time-to-death (LT50/LT90), or population/colony effects of Beauveria bassiana when spores are delivered via selective traps, bait stations, autodissemination devices, or contaminated foragers, rather than broadcast foliar sprays alone? Include lab, semi-field, and field studies. Note any discussion of speed relative to quarantine or control timelines when present, but do not require it.
```

Then append the shared output block.

---

## 02b_strains_traits

**Copilot/Pro**

```
What are the most important papers on Beauveria bassiana strain traits that determine virulence after acquisition from fluid, oil, protein carriers, or trap/bait surfaces? Focus on cuticle-degrading enzymes (Pr1/Pr2 proteases, chitinases), hydrophobins, thermotolerance, UV tolerance, and spore adhesion. Prefer studies that link traits to performance under trap, bait, or autodissemination transfer conditions when available.
```

Then append the shared output block.

---

## 02c_formulation_delivery

**Copilot/Pro**

```
What are the most important papers on how fluid, proteinaceous, oil, wettable powder, or microencapsulated carriers affect Beauveria bassiana spore viability, adhesion, germination, persistence, and transfer efficiency from traps, bait stations, autodissemination devices, or contaminated surfaces under laboratory or field conditions?
```

Then append the shared output block.

---

## 03-autodissemination-social

**Copilot/Pro**

```
What are the most important experimental papers on auto-dissemination and horizontal transmission of Beauveria bassiana in social insects, especially when foragers acquire spores from traps, bait stations, or autodissemination devices and return to the nest? Focus on effects of allogrooming, necrophoresis, trophallaxis, and nest hygiene on spore spread to nestmates and queens. Include Vespidae, Formicidae, and other social taxa when the delivery pathway is relevant.
```

Then append the shared output block.

---

## 04-nontarget-ecotox

**Copilot/Pro**

```
What are the most important papers on non-target risks of Beauveria bassiana to honey bees, bumblebees, native bees, and beneficial arthropods when spores are concentrated in selective traps, bait stations, or autodissemination devices rather than broadcast sprays? Include attractant specificity, trap or bait design features, formulation types that reduce off-target exposure, environmental persistence in trap/bait matrices, and secondary transmission risk.
```

Then append the shared output block.

---

## 05-regulatory-policy

**Copilot/Pro**

```
What are the most important research papers, regulatory reviews, and case studies on registration, emergency or quarantine authorisation, data requirements, and IPM integration of Beauveria bassiana (or closely related entomopathogenic fungi) for insect control using traps, bait stations, or autodissemination systems? Include statutory timelines and combination with attract-and-infect or bait delivery where discussed.
```

Then append the shared output block.

---

## Optional (not a screening pillar)

One-off applied-motivation sanity check. Does not redefine inclusion. Do not add a _V. velutina_ supplementary database string on the basis of this alone (separate Vespidae–entomopathogen search already done).

**Copilot/Pro**

```
What are the most important papers on Beauveria bassiana or related entomopathogenic fungi against Vespa velutina or other invasive Vespidae, including any use of traps, baits, or autodissemination? List gaps where evidence is sparse.
```

Then append the shared output block if useful for vocabulary only.

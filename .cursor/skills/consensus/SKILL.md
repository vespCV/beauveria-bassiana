---
name: consensus
description: >-
  Triage Consensus.app subquestion results against research questions and
  search strings; propose or apply vocabulary and scope edits. Use when the
  user adds a mabb consensus note, asks for a consensus coverage check, or
  wants to gap-check strings before locking database runs.
disable-model-invocation: true
---

# Consensus coverage check

Gap-check one Consensus.app pass against the systematic review search strategy. Consensus is **not** systematic evidence or PRISMA input. See `docs/adr/0011-consensus-coverage-check.md` and **Consensus coverage check** in `CONTEXT.md`.

## Scope

- **In:** subquestions `01`–`05` and split `02a`/`02b`/`02c`.
- **Skip:** `06-background-proxies` unless upstream asks keep returning background-only themes.
- **Notes:** read always; edit `notes/beauveria-bassiana/` only when the user explicitly allows it for that pass.
- **Not allowed:** treating Consensus hits as the corpus; inventing hit counts; rewriting subquestions for every citation.

## Inputs (read in order)

1. Consensus results note: `notes/beauveria-bassiana/mabb NN consensus-<subquestion>.md` (user may `@`-link it).
2. Ask used: matching block in `notes/beauveria-bassiana/mabb consensus.md`.
3. Subquestion line: `notes/beauveria-bassiana/mabb research questions.md`.
4. Search strings: `notes/beauveria-bassiana/mabb search str NN-*.md` (one string block per subquestion; `01` is the product/strain catalogue only).
5. For `01-existing-products` only: remind the user that EPA, EU Pesticide Database, CABI, and patent registry passes remain mandatory for the market catalogue (Consensus does not replace them).

## Execution

### 1. Extract vocabulary

From the ranked paper list and synthesis text, list:

- strain codes (e.g. KTU-24, Pa-4)
- product or trade names (e.g. BKN20, Naturalis)
- formulation types (e.g. wettable powder, oil dispersion, technical concentrate, aqueous suspension, granular, biopolymer, encapsulation, nanoemulsion, seed coating)
- delivery terms (trap, bait station, autodissemination, attract and infect)

Flag tokens that are too noisy for Boolean OR-groups (bare numeric ids, bare `OD`/`ES`, generic abbreviations like `Bb`).

### 2. Triage papers

For each cited paper, assign one label:

| Label | Meaning |
|---|---|
| **in-scope** | Supports the subquestion as written |
| **transfer** | Useful for another subquestion (name which) |
| **out-of-scope** | Ignore for string edits (e.g. metabolite-only, unrelated taxon with no delivery path) |

Do not expand inclusion scope from Consensus alone. Theme gaps go to the research question; synonym gaps go to search strings.

### 3. Compare to search strings

For the matching `mabb search str` note:

- Missing high-value strains, products, or formulation terms → recommend adding to the `01` catalogue OR-groups (and PubMed/Dimensions/Lens/patent variants where parity makes sense).
- Delivery/device terms → recommend on `02a`, `02c`, or `03`, not by adding a second `01` string or ANDing trap/bait onto the catalogue.
- Document the edit date and source in the string note header comment (same style as existing registry/Consensus lines).

Keep diffs minimal. Prefer strain codes over long regional product names when both appear.

### 4. Compare to research question

Revise the subquestion line only when Consensus reveals a **theme gap** (e.g. experimental product codes, formulation classes not mentioned). Do not duplicate string-level synonyms in the question text.

### 5. Write output

1. Ensure `temp/research/` exists.
2. Write one file: `temp/research/YYYY-MM-DD-consensus-<subquestion-id>.md`
3. Use this structure:

```markdown
# Consensus gap check: <subquestion-id>

## Ask
<one-line summary or quote from mabb consensus.md>

## Vocabulary extracted
- Strains: ...
- Products: ...
- Formulation terms: ...
- Delivery terms: ...

## Paper triage
| Paper | Year | Label | Notes |
|---|---|---|---|
| ... | ... | in-scope / transfer / out-of-scope | ... |

## Recommended edits
### Research question
- ...

### Search strings
- ...

### No change
- ...

## Applied
- [ ] research questions.md
- [ ] search str NN-*.md
```

4. Tell the user the **absolute** path. Do not paste the full report unless asked.
5. If the user allowed note edits, apply agreed changes and tick **Applied** in the report.

## Subquestion map

| Id | Consensus note pattern | Search string note |
|---|---|---|
| `01-existing-products` | `mabb 01 consensus-existing-products.md` | `mabb search str 01-existing-products.md` |
| `02a_efficacy` | `mabb 02a consensus-efficacy.md` (when present) | `mabb search str 02a_efficacy.md` |
| `02b_strains_traits` | `mabb 02b consensus-strains-traits.md` | `mabb search str 02b_strains_traits.md` |
| `02c_formulation_delivery` | `mabb 02c consensus-formulation-delivery.md` | `mabb search str 02c_formulation_delivery.md` |
| `03-autodissemination-social` | `mabb 03 consensus-autodissemination-social.md` | `mabb search str 03-autodissemination-social.md` |
| `04-nontarget-ecotox` | `mabb 04 consensus-nontarget-ecotox.md` | `mabb search str 04-nontarget-ecotox.md` |
| `05-regulatory-policy` | `mabb 05 consensus-regulatory-policy.md` | `mabb search str 05-regulatory-policy.md` |

## Consensus.app settings (human step)

When the user runs the ask manually:

- Main search box: "Ask the research..."
- **Deep:** off
- **Medical mode:** off
- **Filters:** none
- Copy ranked list + synthesis into the matching `mabb NN consensus-*.md` note.

## Example trigger

User: `@mabb 01 consensus-existing-products.md` — check strings and research question.

Agent: read inputs → triage 20 papers → extract KTU-24, Pa-4, BKN20, mycoinsecticide, technical concentrate → write `temp/research/2026-08-07-consensus-01-existing-products.md` → apply note edits if allowed.

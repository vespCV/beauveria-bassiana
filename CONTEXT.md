# Beauveria bassiana literature review

Domain language for the systematic review of _Beauveria bassiana_ as a selective trap/bait/autodissemination control agent.

## Language

### Review scope

**Applied motivation**:
The end-use pest that motivates the review (_Vespa velutina_ / Asian hornet). Sparse species-specific literature does not narrow inclusion. A separate Vespidae–entomopathogen search already covers that taxon lane; this review does not re-run a V. velutina supplementary string.
_Avoid_: Treating V. velutina as a hard inclusion filter; requiring the target taxon in every search string; duplicating the prior Vespidae–entomopathogen search here

**Inclusion scope**:
Evidence eligible for screening: _B. bassiana_ (including commercial strains and products) used with selective traps, bait stations, autodissemination devices, and/or fluid or protein carriers, plus transferable mechanisms (strain traits, formulation, horizontal transmission, non-target risk, regulation) from other insects when the intervention or pathway is relevant to that delivery model.
_Avoid_: Restricting the corpus to invasive exotic insects only; equating title pest wording with eligibility

**Transferable evidence**:
Studies on non-motivation taxa kept because strain, formulation, delivery, social transmission, or risk findings can inform the applied motivation.
_Avoid_: Proxy as a synonym for out-of-scope noise; background-only papers without a clear transfer path (those belong in screening category `06-background-proxies` with explicit rationale)

**Market catalogue search**:
The broad `01-existing-products` run that retrieves registered/commercial _B. bassiana_ products and strains without requiring trap or bait terms.
_Avoid_: Single products string that ANDs trap/bait and drops registry-only hits

**Delivery systems search**:
The narrow `01-existing-products` run that retrieves trap, bait station, and autodissemination device literature for _B. bassiana_.
_Avoid_: Using this run alone as the product/strain inventory

### Review workflow

**Search documentation**:
The recorded search event: date, databases, exact strings, filters, and hit counts per database, before screening begins.
_Avoid_: Search setup alone when the logging artifacts are meant; informal browsing

**Phase 1 screening**:
Title/abstract screening of unique records after duplicate removal.
_Avoid_: Phase I (prefer Arabic numeral in agent-facing docs); abstract screen as a separate stage name

**Phase 2 screening**:
Full-text screening of records sought after Phase 1, including location failures and exclusion reasons.
_Avoid_: Phase II; full-text review when screening criteria are meant

**Phase gate**:
A concrete artifact boundary: Phase 2 agent workflows (PDF filing, inventory, PRISMA E counts) run only after all three named inputs exist on disk: `search-results/screening-phase2/relevant_articles_categorized.csv`, `search-results/screening-phase2/pdfs_not_downloaded.md`, and a README with study-selection / PRISMA skeleton. `@file-pdfs` hard-stops at start if any are missing and does not invent stubs.
_Avoid_: Soft "when ready"; implied progress from chat memory; gating on the CSV alone; creating placeholder gate files to unblock the skill

### Sources of truth

**Search strategy source**:
Scientific search design (research question, subquestions, databases, exact strings, inclusion/exclusion intent) lives in `notes/beauveria-bassiana/`. Agents may read these notes. Edit or create under `notes/` only when the user explicitly allows it for that work; otherwise treat notes as read-only. Notes are written for humans in Obsidian.
_Avoid_: ADR or `docs/adr/` citations in notes; `.cursor/` paths, skill names, or `temp/` scratch paths in notes; inventing strings in chat without writing them back when edits are allowed; treating `.cursor` as the scientific record; silent note edits the user did not request

**Agent project context**:
The always-on summary in `.cursor/rules/project-context.mdc`: mission, current phase, layout paths, and pointers into the notes. It must stay aligned with the search strategy source; when they diverge, the notes win and the rule is updated to match. It keeps the review end-state under **Done when**, and a separate **Current phase** block for what is in play now (today: search documentation).
_Avoid_: Duplicating full search strings in the rule; drifting summaries that contradict notes; replacing end-state Done when with only the current phase

### Categories

**Subquestion**:
A research subquestion id used for Consensus asks, search-string notes, and logged database runs: `01-existing-products`, `02a_efficacy`, `02b_strains_traits`, `02c_formulation_delivery`, `03-autodissemination-social`, `04-nontarget-ecotox`, `05-regulatory-policy`, `06-background-proxies` (reserve).
_Avoid_: pillar; collapsing `02a`/`02b`/`02c` into a single logged run without the sub-ids

**Screening category**:
A Phase 2 full-text bucket whose folder id matches `pdfs/{category}/` and `@file-pdfs`: `01-existing-products`, `02-efficacy-mechanics-delivery` (with `02a_efficacy`, `02b_strains_traits`, `02c_formulation_delivery`), `03-autodissemination-social`, `04-nontarget-ecotox`, `05-regulatory-policy`, `06-background-proxies`. Aligns with subquestion ids (parent `02` holds the three `02*` subquestions).
_Avoid_: `00-existing-products`; zero-based subquestion ids in agent-facing paths; dual id schemes without a mapping table; calling these pillars

### Agent scratch

**Temp scratch**:
Gitignored working output under `temp/`, including `temp/research/` (cited one-question findings, including optional subquestion `01-existing-products` registry/product lookups) and `temp/handoff/` (session handoffs). Agents may write here; promote keepers into notes or tracked docs only by explicit user action. `@research` is not the systematic search log.
_Avoid_: Committing `temp/`; treating research scratch as the search strategy source; using `@research` as a substitute for database hit-count documentation in notes

### Search artifacts

**Raw search export**:
A tracked file under `search-results/raw/` (optionally per database) holding a database export used for import into Rayyan or later screening (RIS, PubMed XML, NBIB, CSV, and similar).
_Avoid_: Leaving exports only outside the repo when reproducibility in-repo is required; storing raw exports under `temp/`

**Consensus coverage check**:
A Consensus.app pass that returns the most important papers per subquestion so categories, research questions, and search strings can be gap-checked against the applied motivation before database runs are locked. Hits are triaged: theme gaps revise questions or categories; missing synonyms, strain codes, or product names revise strings; out-of-scope papers are ignored. Each subquestion uses one natural-language ask in the main Consensus search box ("Ask the research..."), with Deep off and no Medical mode or extra Filter chips, requesting a ranked paper list (title, year, DOI/PMID when available, one-line relevance) plus a separate vocabulary list of strain codes, product names, and delivery terms for string edits.
_Avoid_: Calling this "Copilot" (that label is not on consensus.app); turning Deep on for this coverage check; Medical mode or ad hoc Filters for this pass; treating Consensus hits as the systematic corpus; using Consensus as a substitute for logged database searches; Consensus as primary PRISMA evidence; rewriting subquestions for every citation; the "Find the Consensus" / Consensus Meter yes-no path for this pass

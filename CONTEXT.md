# Beauveria bassiana literature review

Domain language for the systematic review of _Beauveria bassiana_ as a selective trap/bait/autodissemination control agent.

## Language

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
Scientific search design (research question, subquestions/pillars, databases, exact strings, inclusion/exclusion intent) lives in `notes/beauveria-bassiana/`. Agents may read these notes; they must never create, modify, or delete them.
_Avoid_: Inventing strings in chat; treating `.cursor` as the scientific record

**Agent project context**:
The always-on summary in `.cursor/rules/project-context.mdc`: mission, current phase, layout paths, and pointers into the notes. It must stay aligned with the search strategy source; when they diverge, the notes win and the rule is updated to match. It keeps the review end-state under **Done when**, and a separate **Current phase** block for what is in play now (today: search documentation).
_Avoid_: Duplicating full search strings in the rule; drifting summaries that contradict notes; replacing end-state Done when with only the current phase

### Categories

**Screening category**:
A Phase 2 full-text bucket whose folder id matches `pdfs/{category}/` and `@file-pdfs`: `01-existing-products`, `02-efficacy-mechanics-delivery` (with `02a_efficacy`, `02b_strains_traits`, `02c_formulation_delivery`), `03-autodissemination-social`, `04-nontarget-ecotox`, `05-regulatory-policy`, `06-background-proxies`.
_Avoid_: `00-existing-products`; zero-based pillar ids in agent-facing paths; dual id schemes without a mapping table

### Agent scratch

**Temp scratch**:
Gitignored working output under `temp/`, including `temp/research/` (cited one-question findings, including optional pillar `01-existing-products` registry/product lookups) and `temp/handoff/` (session handoffs). Agents may write here; promote keepers into notes or tracked docs only by explicit user action. `@research` is not the systematic search log.
_Avoid_: Committing `temp/`; treating research scratch as the search strategy source; using `@research` as a substitute for database hit-count documentation in notes

### Search artifacts

**Raw search export**:
A tracked file under `search-results/raw/` (optionally per database) holding a database export used for import into Rayyan or later screening (RIS, PubMed XML, NBIB, CSV, and similar).
_Avoid_: Leaving exports only outside the repo when reproducibility in-repo is required; storing raw exports under `temp/`

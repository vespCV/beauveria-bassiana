# Beauveria bassiana literature review

Domain language for the systematic review of _Beauveria bassiana_ as a selective trap/bait/autodissemination control agent.

## Language

### Review scope

**Applied motivation**:
The end-use pest that motivates the review (_Vespa velutina_ / yellow-legged hornet; Dutch: geelpoothoornaar). Sparse species-specific literature does not narrow inclusion. A separate Vespidae–entomopathogen search already covers that taxon lane; this review does not re-run a V. velutina supplementary string.
_Avoid_: Treating V. velutina as a hard inclusion filter; requiring the target taxon in every search string; duplicating the prior Vespidae–entomopathogen search here; using “Aziatische hoornaar” in Dutch prose (use geelpoothoornaar)

**Catch-infect-release**:
The applied delivery pathway for overview and Dutch reader prose: a selective trap admits the target insect; the insect picks up _B. bassiana_ conidia from a passage surface (1- or 2-way dispenser) and/or from sugar or protein bait; the insect is released and returns to the nest so inoculum can move by contact to nestmates (workers, larvae, pupae) before colony hygiene removes it. Preferred Dutch labels: catch-infect-release, selectieve val, dispenser, bait/baait.
_Avoid_: Treating hold-and-kill as the default; using Trojan / vision-gated jargon in Dutch overview unless the user asks; equating bumblebee 1-/2-way dispenser trials with Vespidae proof

**Vision-gated autodissemination device**:
Optional technical exclusivity layer for the decision brief: a smart detector confirms _V. velutina_ before dosing, then catch-infect-release proceeds (contact surface or bait; return to nest). Subordinate to **catch-infect-release** for reader-facing overview text.
_Avoid_: Equating any camera trap with this pathway; treating hold-and-kill as the default device model; using "AI trap" without this meaning; forcing vision-gated wording into Dutch overview when catch-infect-release suffices

**Colony-weakening endpoint**:
The success frame for synthesis: reduce current damage and/or reduce production of queens and drones for the next year. Individual death, sublethal behaviour change, cleared infection, and failed nest introduction after hygienic behaviour are all reportable outcomes. Nest collapse is not assumed and is not required to discuss progress along the pathway.
_Avoid_: Treating contacted-worker mortality alone as colony control; writing as if nest eradication were the only relevant endpoint

**Inclusion scope**:
Evidence eligible for screening: _B. bassiana_ (including commercial strains and products) used with selective traps, bait stations, autodissemination devices, and/or fluid or protein carriers, plus transferable mechanisms (strain traits, formulation, horizontal transmission, non-target risk, regulation) from other insects when the intervention or pathway is relevant to that delivery model.
_Avoid_: Restricting the corpus to invasive exotic insects only; equating title pest wording with eligibility

**Transferable evidence**:
Studies on non-motivation taxa kept because strain, formulation, delivery, social transmission, or risk findings can inform the applied motivation.
_Avoid_: Proxy as a synonym for out-of-scope noise; background-only papers without a clear transfer path (those belong in screening category `06-background-proxies` with explicit rationale)

**Market catalogue search**:
The single `01-existing-products` bibliographic string that retrieves registered/commercial _B. bassiana_ products and strains without requiring trap or bait terms. One logged string per subquestion per database.
_Avoid_: ANDing trap/bait onto the `01` string and dropping registry-only hits; a second `01` delivery-systems string (device trials belong under `02a`, `02c`, and `03`)

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
A concrete artifact boundary: Phase 2 agent workflows (PDF filing, inventory, PRISMA E counts) run only after all three named inputs exist on disk: `input-phase2/relevant_articles_categorized.csv`, `input-phase2/pdfs_download_links.md`, and a README with study-selection / PRISMA skeleton. `@file-pdfs` hard-stops at start if any are missing and does not invent stubs.
_Avoid_: Soft "when ready"; implied progress from chat memory; gating on the CSV alone; creating placeholder gate files to unblock the skill

**Systematic review findings**:
Publication-facing synthesis from Phase 2 extracts, full texts, and Zotero annotations, organized by the README research questions. The easy-read summary lives in `README.md`. Numbered chapter pages and background live in `results/` (`background.md`, `01-eu-products.md` through `06-nest-effects.md`). Process documentation lives in `results/methods/` (lab journal, search log). `temp/overview/` remains gitignored draft. Existing README wording is kept when the Index or a missing finding is updated.
_Avoid_: Treating chat summaries as the findings record; reversing user README wording; equating unpromoted `temp/` drafts with the publication record; dumping every annotation into `README.md`; writing go / conditional-go / no-go into `results/` unless the user asks for a decision brief

**Citekey ao suffix**:
Append **`ao`** to a citekey (e.g. Peng2020ao, Almeida2022ao) when README or chapter prose cites a paper from its abstract only because no full PDF is on disk yet. List missing PDFs in `input-phase2/pdfs_request_list.md` and on `input-phase2/pdfs_download_links.md` until `@file-pdfs` files them under `pdfs/`. Drop the `ao` suffix after full-text verification.
_Avoid_: Treating `ao` rows as full-text evidence; inventing numbers not in the abstract; omitting the request-list entry for cited `ao` papers

**Literature overview draft**:
Working synthesis under `temp/overview/` (gitignored): machine/category roll-up in `literature-overview.md`; Dutch reader prose in `nederlandse-samenvatting.md` (and similar). Built from extract tables and Zotero annotations: abstract-level coverage for all Phase 2 categories on the first pass, with full-text synthesis only where rows are marked full-text or explicit not-in-PDF, following **full-text reading priority**. Section membership follows the CSV primary `screening_category` (co-tags from `screening_categories_all`). Include PDFs on disk sit flat under `pdfs/`; only exclusions use `pdfs/excluded/`. Full-text exclusions stay visible in the relevant category section as screened-out (with reason). Excluded records live under `input-phase2/excluded/`; excluded PDFs under `pdfs/excluded/`; the include CSV holds current includes only. Seed from Obsidian phase2 notes, then align to extract CSVs. First-pass “solid enough”: every current-include category has an abstract roll-up (cite + evidence level), exclusions shown as screened-out, plus full-text synthesis for all still-included `00-key-papers` with PDFs on hand. The user turns keepers into `README.md`. Dutch / reader updates follow **Dutch / reader overview processing** in `.cursor/rules/project-context.mdc` (catch-infect-release spine, colony-weakening endpoint, mandatory Bronnen block, no go-ladder).
_Avoid_: Skipping evidence-level labels on abstract roll-ups; using the draft as a substitute for extract tables; writing the working overview into `README.md` before the user promotes it; assigning overview sections from `pdfs/` folder layout when it conflicts with the CSV; deleting exclusion provenance from the overview when a PDF is filed under `excluded`; leaving excluded rows in the include CSV; claiming a solid overview before `00-key` full-text synthesis is done for remaining includes; silently rewriting user Dutch wording; omitting the Bronnen block on overview revisions

**Evidence-selection bias (nontarget vs target framing)**:
When synthesizing bee, beneficial, or pollinator rows: papers framed as nontarget safety often report little or no Bb effect; papers framed as controlling those same taxa often report mortality. Record both framings. If a study reports mite/varroa control inside a hive without measuring bee mortality, say so.
_Avoid_: Collapsing both literatures into “Bb is safe for bees” or “Bb kills bees” without the framing note

**Phase 2 exclusion record**:
The audit trail for full-text exclusions. Preferred agent-readable signal: a BibTeX export of **only** Zotero collection `excluded` at `temp/zotero/excluded.bib`. Every entry in that file is excluded. Sync via `@zotero-sync` into `input-phase2/excluded/records.csv` and `pdfs/excluded/`; keep screened-out lines in the literature overview draft; remove matching rows from the include CSV. Until that export exists (or a small excluded-only file replaces a full-library Downloads bib), read collection `excluded` from a copy of `/Users/md/Zotero/zotero.sqlite`, or fall back to `mabb phase2 excluded.md` plus `pdfs/excluded/`.
_Avoid_: Treating a full-library `.bib` as the exclusion list; inventing exclusion reasons not present in Zotero or the user's note; writing to the live `zotero.sqlite`

**Zotero → repo sync**:
One-way sync from local Zotero into the repo (`@zotero-sync`): collection membership drives flat `pdfs/` placement for includes and `pdfs/excluded/` for exclusions; exclusions and annotations feed `input-phase2/excluded/`, `temp/zotero-annotations/`, and the literature overview draft. Overview **section** membership still follows the include CSV primary `screening_category` until an explicit include/exclude sync updates it. Prefer Obsidian citekey notes under `notes/beauveria-bassiana/zotero/` over regenerating annotation markdown.
_Avoid_: Writing the live Zotero database; deleting Zotero `storage/` files; silently rewriting CSV science categories when only the PDF folder moves; using Google Scholar automation

**Decision brief**:
Thin go / conditional-go / no-go layer on top of the same extracts, organized by design choices for the applied-motivation delivery system (strain/product, formulation/carrier, acquisition in the device, nest or horizontal pathway, nontarget risk, regulatory path). Each claim carries an evidence level and cite labels. Working drafts live under `temp/` (gitignored scratch); promote into tracked docs or notes only by explicit user action. Not the current workstream goal while the literature overview is being built.
_Avoid_: Free-form LLM literature dump that bypasses extract tables; using the decision brief as a substitute for systematic review findings; treating an unpromoted `temp/` draft as the publication record; drafting go / conditional-go / no-go while the user has asked only for a literature overview

**Conditional-go bar (nest pathway)**:
For catch-infect-release (optionally vision-gated), conditional-go is justified when evidence supports (a) reliable acquisition on a device surface or bait, (b) transfer plausibility in social wasps (contaminated individuals not strongly avoided; inoculum can move to nestmates before hygiene dominates), and (c) a colony-weakening pathway (worker/brood mortality, traffic reduction, or reduced reproductive castes) from Vespidae or close transferable systems. Full nest collapse proof in _V. velutina_ field trials is not required for conditional-go. Go is reserved for nest or colony-level evidence in _Vespa_ / Vespidae under a comparable delivery model. No-go if acquisition fails, avoidance blocks return or transfer, or nontarget / regulatory blockers dominate.
_Avoid_: Treating contacted-worker mortality alone as go; equating conditional-go with field-validated nest eradication; drafting go-ladder language into Dutch overview without an explicit decision-brief request

**Dual-track strain strategy**:
The decision brief scores two parallel tracks with the same acquisition and transfer fields: (1) registered commercial _B. bassiana_ products for near-term device design (formulation, label, supply, NL/EU use rights), and (2) indigenous or Vespidae-derived isolates for virulence and catch-infect-release fit. Track 2 is not treated as deployable until a registration path exists.
_Avoid_: Collapsing commercial and indigenous isolates into one deployable pick before both tracks are scored; treating a research isolate as product-ready

**Acquisition mode (device pickup)**:
How the hornet acquires _B. bassiana_ inside the catch-infect-release device. The decision brief scores contact autocontamination (oil or dry conidia on a 1- or 2-way dispenser / passage surface) and inoculum-in-bait (protein or sugar carrier with Bb) equally until evidence picks a primary. Both modes may co-occur.
_Avoid_: Declaring a primary pickup mode before both are scored; treating attractant chemistry and inoculum as the same design choice without saying so

**Nest microclimate for outgrowth**:
Temperature and relative humidity inside the nest (and UV/field half-life of inoculum before return) as constraints on germination and mycosis after catch-infect-release. Cite formulation-specific half-life claims; do not generalize one product’s UV half-life to all Bb products.
_Avoid_: Assuming spray-assay RH optima equal nest conditions; stating a universal outdoor half-life without a product or study cite

**Decision-field overlay**:
Shared full-text fields captured while reading so both systematic review findings and the decision brief can be built without inventing values. Intended dimensions include evidence level, taxon band, acquisition mode, dose or load, return or release, transfer or avoidance, nontarget note, regulatory geography, and device relevance. Exact field names, enums, and storage (overlay file vs category extract columns) are to be specified later.
_Avoid_: Free-text-only Zotero highlights as the sole machine-readable record; LLM summaries that fill these fields without a row on disk

**Full-text reading priority**:
Order for filling decision-field overlay rows while reading: (1) screening category `00-key-papers` (Bb with Vespidae / _V. velutina_); (2) social-wasp transfer, avoidance, and nest-pathway papers already in hand (`03` and related `00`); (3) commercial product dossier rows in `01-existing-products` for the dual-track candidates under score; (4) formulation and delivery papers that match contact surface or bait-inoculum; (5) nontarget and regulatory (`04`, `05`); (6) remaining transferable proxies only when a decision-brief section is still empty.
_Avoid_: Deep extraction on distant proxies before Vespidae, transfer, and candidate product dossiers are covered

**Primary regulatory frame**:
EU pesticide law for the decision brief commercial track: Regulation (EC) No 1107/2009 active-substance and product authorisation, with national product authorisation under that frame. For Netherlands-facing overview text, report **NL allowed use** (which products/labels are authorised for which uses) separately from EU strain approval dates. Non-EU instruments (for example EPA) are secondary context only.
_Avoid_: Treating EPA label status as sufficient for EU or NL deployability; equating EU active-substance approval with NL product use rights; treating member-state rules as a separate science lane from the EU frame

**Nontarget scope (decision brief)**:
Primary nontarget control is device-level exclusivity: only vision-confirmed _V. velutina_ receive _B. bassiana_. In-scope residual pathway for the brief is gate failure (false positive / dosing a non-target). Post-release residual and open-attractant pathways are out of scope for deep treatment in the decision brief.
_Avoid_: Expanding the brief into a full bee-ecotox review; treating device exclusivity as proven without a gate-failure note

**Decision-brief draft gate**:
An LLM may draft the first consolidated decision brief only after decision-field overlay rows exist for all `00-key-papers` with PDFs on hand and for commercial `01` candidates under active score, with those rows marked full-text evidence or explicit not-in-PDF. Until then: extract and reading updates only; section stubs may use [to be verified]; no consolidated go / conditional-go / no-go summary. Draft path: under `temp/` (for example `temp/research/` or `temp/handoff/`), not `README.md`.
_Avoid_: "Everything we need to know" summaries from abstracts alone; treating chat synthesis as the brief before the gate; writing the working brief into `README.md`

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
A Phase 2 bucket id used in the include CSV, Zotero collections, and `@file-pdfs` / `@zotero-sync`: systematic review ids `01-existing-products`, `02-efficacy-mechanics-delivery` (with `02a_efficacy`, `02b_strains_traits`, `02c_formulation_delivery`), `03-autodissemination-social`, `04-nontarget-ecotox`, `05-regulatory-policy`, `06-background-proxies`, plus supplemental lanes `00-key-papers` (Beauveria on *V. velutina* / other Vespidae), `07-vespideae-biocontrol` (Vespidae non-Bb microbes and chemical trap/bait proxies), and full-text exclusion lane `excluded`. Include PDFs on disk sit flat under `pdfs/`; only exclusions use `pdfs/excluded/`. Aligns with subquestion ids for `01`–`06` (parent `02` holds the three `02*` subquestions). Zotero collection names use hyphens for `02a-efficacy` style ids.
_Avoid_: Renaming systematic ids to a parallel zero-based scheme (for example `00-existing-products`); dual id schemes without a mapping table; calling these pillars

### Agent scratch

**Temp scratch**:
Gitignored working output under `temp/`, including `temp/research/` (cited one-question findings, including optional subquestion `01-existing-products` registry/product lookups), `temp/handoff/` (session handoffs), `temp/overview/` (literature overview draft), `temp/zotero/` (DB copies, optional `excluded.bib`, sync reports), and `temp/zotero-annotations/` (annotation markdown when Obsidian citekey notes are absent). Agents may write here; promote keepers into notes or tracked docs only by explicit user action. `@research` is not the systematic search log.
_Avoid_: Committing `temp/`; treating research scratch as the search strategy source; using `@research` as a substitute for database hit-count documentation in notes

### Search artifacts

**Input phase 0**:
Search-phase inputs under `input-phase0/`: raw database exports for Rayyan unduplication in `input-phase0/input-rayyan/`, and CitationChaser / ResearchRabbit seeds in `input-phase0/input-cc-rr/`.
_Avoid_: `search-results/raw`; mixing seed files into the Rayyan upload set without a separate folder

**Input phase 1**:
Deduplicated bibliographic records under `input-phase1/` used as input for ASReview or Cursor-assisted title/abstract selection of relevant articles.
_Avoid_: Screening from undeduplicated raw exports; treating Phase 1 as full-text PDF work

**Input phase 2**:
Relevant-article list and related gate files under `input-phase2/` used to select and file PDFs for extraction (`relevant_articles_categorized.csv`, `pdfs_download_links.md`), plus full-text exclusions under `input-phase2/excluded/`.
_Avoid_: `search-results/screening-phase2`; inventing gate stubs before screening is done; leaving excluded rows in the include CSV after a Zotero exclusion sync

**Raw search export**:
A tracked file under `input-phase0/input-rayyan/` (optionally with `split/` chunks) holding a database export used for import into Rayyan or later screening (RIS, PubMed XML, NBIB, CSV, and similar).
_Avoid_: Leaving exports only outside the repo when reproducibility in-repo is required; storing raw exports under `temp/`

**Consensus coverage check**:
A Consensus.app pass that returns the most important papers per subquestion so categories, research questions, and search strings can be gap-checked against the applied motivation before database runs are locked. Hits are triaged: theme gaps revise questions or categories; missing synonyms, strain codes, or product names revise strings; out-of-scope papers are ignored. Each subquestion uses one natural-language ask in the main Consensus search box ("Ask the research..."), with Deep off and no Medical mode or extra Filter chips, requesting a ranked paper list (title, year, DOI/PMID when available, one-line relevance) plus a separate vocabulary list of strain codes, product names, and delivery terms for string edits.
_Avoid_: Calling this "Copilot" (that label is not on consensus.app); turning Deep on for this coverage check; Medical mode or ad hoc Filters for this pass; treating Consensus hits as the systematic corpus; using Consensus as a substitute for logged database searches; Consensus as primary PRISMA evidence; rewriting subquestions for every citation; the "Find the Consensus" / Consensus Meter yes-no path for this pass

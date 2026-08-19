# Science communication for this review

Style guide for short, easy-to-read text about _Beauveria bassiana_ and selective delivery. Use it when drafting literature-overview prose, category summaries, decision-brief wording, README findings copy, or other explanatory notes. This is a **style guide only** — never use it as a factual source.

Hard biological and regulatory claims still come from extracts, PDFs, and cited notes. Keep prose short. Prefer one clear idea per paragraph.

---

## Goal

Help a non-specialist reader understand a difficult fungus topic without drowning them in systematics, strain codes, or lab jargon. The applied story is selective contact: target insects pick up inoculum from a trap, bait, or autodissemination surface, then may carry it further (including nestmates for social insects). Write so that story stays visible.

---

## Audience and subject

- **Audience first**: who is this for (review collaborator, decision reader, general science-curious), and what do they need now?
- Prefer topics with a clear decision or evidence angle (efficacy, strain, formulation, horizontal spread, non-target risk, regulation).
- Tie abstract mechanisms to a concrete scene early: insect walks through a device, contacts oil or bait, returns to a nest, spores may move to nestmates.
- Do not try to explain the entire field of entomopathogenic fungi in one short piece.
- News hooks and party anecdotes are optional for repo docs; clarity and relevance matter more than entertainment.

---

## Structure

- **Reject the zandloper** (hourglass): do not open with long background on fungal taxonomy or general biocontrol history.
- Lead with the main point (inverted pyramid for short briefs): what the evidence says, then detail.
- Answer the useful **w's** early: what organism or product, what delivery, what outcome, why it matters for selective control.
- Default shape: **pakkend begin → onderhoudend midden → helder einde**.
- Opening must **fascinate or orient before it explains** — a concrete image or question before exposition.
- Strong openers: a surprising result, a device scene, a vivid contrast (spray vs targeted pickup).
- Weak openers: abstract definitions, roadmap summaries, "since ancient times…".
- Middle: one idea per short block; cut digressions even if interesting.
- Give breathing room before hard material (a short plain-language block before dose, LT50, or regulatory nuance).
- End with closure: what is known, what is thin, what remains open for the delivery model.

---

## Writing craft

- **No "not" prose:** Write what the evidence shows and what endpoint or delivery mode applies. Do not frame sentences around negation (`not X`, `is not Y`, `does not stand in for`, `not proof`, `not filled`, out-of-scope disclaimers). State the positive claim or label proxies, endpoints, and open questions directly. Same rule as `.cursor/rules/interaction-style.mdc`.
- Outline themes and a rough word budget before sentences (**kleurplaatmethode**).
- Expect heavy cutting; short is the product.
- **Afhakers**: anything that makes a tired reader stop — cut or rewrite.
- **Ritme**: vary sentence length; after each sentence, ask what the reader needs next.
- **Lekkere woorden**: put the strong word near the sentence end; untangle word order.
- **Lakmoesproef**: read aloud; if you stumble, rewrite.
- Prefer a non-expert pass when stakes are high; if they do not understand, the text failed — not them.
- **Five basisregels**:
  1. Prefer active over passive
  2. Cut filler and bureaucratic phrasing (*door middel van*, stacked hedges)
  3. Avoid stacked prepositions — split into two sentences
  4. Keep verb parts together (no tangconstructies)
  5. Prefer verbs over nominalizations (*het analyseren van* → *analyseer*)

---

## Metaphors for this fungus

- Use metaphors when the process is invisible (spore germination, cuticle breach, nest transfer).
- Skip a metaphor when explaining it takes longer than the concept.
- Prefer everyday images over lab jokes: sticky surface, hitchhiking spores, return to the nest with inoculum, bait as a shared meal.
- One strong image can carry a paragraph; optionally reuse a few metaphor words later for cohesion.
- Metaphors may also clarify **how the evidence works** (lab assay vs field trial; product label vs research isolate).
- For Dutch overview, prefer **catch-infect-release** over Trojan-horse wording unless the user asks for the latter.

---

## Word choice for this domain

- Assume **less jargon knowledge** than you think. Strain codes (GHA, ATCC 74040), product names, and terms like conidia, autodissemination, LT50, or non-target need a plain gloss on first use — or a plain substitute.
- Prefer: fungus, spores, bait, trap surface, nestmates, risk to bees, registered product — when they stay accurate.
- Watch **double meanings**: *significant*, *theory*, *control*, *infection*, *vector*, *selective*. Say what you mean in this review.
- Tone: neither condescending ("everyone knows…") nor intimidating ("only specialists understand").
- Formulas and statistics: only if they earn space; translate what the number *means* for delivery or risk.
- **Simplify, don't distort**: shorten framing; never invent mortality, transfer, or regulatory facts.

Domain terms and avoid-lists live in `CONTEXT.md`. Match that language when a term is already defined there.

---

## Images and graphs

- Pick visuals that show the delivery idea (device contact, bait, social transfer) over generic stock fungus photos.
- Respect copyright; credit sources.
- **Graphs must support one main point** — decide what the number means first.
- Prefer counts over bare percentages when scale matters.
- Default charts: line, bar. Avoid pie charts, 3D charts, and dense scatterplots for general readers unless you teach them.
- Honest axes: label clearly; do not truncate to exaggerate; start at zero when comparing magnitude.
- One clear message per figure.

---

## Project fit (what agents write)

| Deliverable | Style emphasis |
|---|---|
| Literature overview draft (`temp/overview/literature-overview.md`) | Short category roll-ups; evidence level visible; no fluff openers |
| Dutch reader overview (`temp/overview/nederlandse-samenvatting.md`) | Catch-infect-release scene; numbered evidence questions; colony-weakening endpoint; Bekend / Beperkte informatie / Geen informatie; **mandatory Bronnen block**; no go-ladder |
| Category / extract-facing notes | Plain verbs; define strain and delivery terms once |
| Decision-brief drafts (`temp/`) | Main claim first; go / conditional-go / no-go in plain words; cite labels stay |
| Public `README.md` findings | User-promoted only; same clarity rules; no editor/agent process talk |

### Dutch overview: sources block (mandatory)

Every revision of Dutch / reader overview prose ends with a project provenance section, for example:

```markdown
### Bronnen voor deze tekst (project)

- Hoofdstukken / consensus: `notes/…`
- Annotaties (o.a.): Citekey1, Citekey2, …
- Eerdere samenvatting / handoffs: `temp/overview/…`; `temp/handoff/…`; `temp/research/…`
- Stijl: `.cursor/docs/wetenschapscommunicatie.md`
```

List only paths and citekeys actually used. Prefer Obsidian Zotero notes under `notes/beauveria-bassiana/zotero/` when present. Do not invent references.

### Dutch overview: preferred spine

1. Concrete catch-infect-release scene (uptake → return → transfer → possible mycosis, clearance, or sublethal effect)
2. Numbered questions (commercial Bb + NL use; kill/weaken; selective delivery; nestmate transfer vs hygiene; nest T/RH; colony weakening / reproductive castes)
3. Short sections answering those questions with taxon and framing honesty
4. Bekend / Beperkte informatie / Geen informatie
5. Bronnen block

Preferred terms: conidia, catch-infect-release, selectieve val, dispenser, bait. For _Vespa velutina_ in Dutch: **geelpoothoornaar**. Use catch-infect-release in overview prose unless the user wants decision-brief vocabulary.

Never put this style guide's advice in place of citations. Facts stay tied to extracts, PDFs, or notes.

---

## Quick checklist

1. **Hook**: Does the first paragraph orient with a concrete point (not background)?
2. **W's**: Are organism, delivery, and outcome clear early?
3. **Structure**: One main idea per section; clear ending?
4. **Afhakers**: Any sentence a tired reader would skip?
5. **Jargon**: Every technical term justified and glossed once (or replaced)?
6. **Metaphors**: Do they clarify faster than they confuse?
7. **Active voice**: Read aloud — any stumbles?
8. **No "not" prose**: Any sentence framed as negation instead of a positive claim?
9. **Graphs**: Honest axes, labeled, one point?
10. **Facts**: All scientific claims tied to project sources — tied to extracts, PDFs, or notes, not this style guide.
11. **Dutch overview**: Catch-infect-release + colony-weakening frame; Bronnen block present; no go-ladder unless asked?

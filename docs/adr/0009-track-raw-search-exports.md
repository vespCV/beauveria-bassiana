# Track raw search exports under input-phase0/input-rayyan

Raw database exports (RIS, PubMed XML, NBIB, CSV, and similar) are stored and tracked under `input-phase0/input-rayyan/` (optionally with a `split/` upload set) from the first runs. CitationChaser and ResearchRabbit seeds live under `input-phase0/input-cc-rr/`. Deduplicated screening input lives under `input-phase1/`; Phase 2 gate artifacts under `input-phase2/` (see ADR 0013). Rejected keeping exports only outside the repo or gitignoring them. Supports methods reproducibility alongside note-based hit-count logging.

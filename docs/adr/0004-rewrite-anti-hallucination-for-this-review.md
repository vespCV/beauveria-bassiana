# Rewrite anti-hallucination for this review

`.cursor/rules/anti-hallucination-verification.mdc` must drop foreign-project paths (`knowledge/`, `program/…`, coach, `requirements/`, unrelated validators) and state this review’s source of truth and whitelist: notes (edit only with explicit user allow), phase gate artifacts, `pdfs/`, `input-phase0/` / `input-phase1/` / `input-phase2/`, `temp/`, `results/attachments/workflow.md`, and ADRs. Chosen over a minimal generic rule or deleting the file so verification stays explicit and project-specific.

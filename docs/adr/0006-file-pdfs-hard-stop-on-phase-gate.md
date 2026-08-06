# file-pdfs hard-stops on missing phase gate

`@file-pdfs` must check the Phase 2 gate at skill start and refuse if any required artifact is missing, naming which path is absent, without creating stubs. Soft-continue and disable-model-invocation gates were rejected as too weak or too easy to forget. Aligns with ADR 0001.

# temp/ is gitignored scratch

Ephemeral agent output stays under `temp/` (`temp/research/`, `temp/handoff/`). `temp/` is added to `.gitignore`; `@cursor-unignore` re-includes those subtrees for agent read. Rejected committing `temp/` or moving handoff/research into tracked `docs/`. Keeps session scratch out of git while matching existing skills.

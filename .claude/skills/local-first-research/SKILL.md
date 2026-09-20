---
name: local-first-research
description: Answer a Philippines fact by searching local hub files before any web or browser tool. Use when the user asks a factual question, wants sources, citations, statistics, licenses, or "look this up". Use when the user runs /local-first-research.
---

# Local-first research

1. Read `research/INDEX.md` and `directory/INDEX.md`. Grep `research/library/`, `research/extracts/`, and `research/briefs/` for the query terms.
2. If a local file answers the question, cite the path. Stop. Do not open a browser.
3. If the catalog lists a URL that is not on disk, tell the user and offer `ingest-source` for that catalog ID.
4. Use web_search or a browser only after steps 1–3, and only to obtain a downloadable source. Save the result with `ingest-source` in the same turn when possible.
5. Label every claim `local:<path>` or `unsourced`. Inventing PSA/DTI/BIR figures is a hard fail.

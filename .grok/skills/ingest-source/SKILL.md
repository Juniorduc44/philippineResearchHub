---
name: ingest-source
description: Download a source once, store it under research/inbox, extract text, write a library card, and index it. Use when the user says download, ingest, fetch, save this URL, add a source, or when a fact is missing locally. Use when the user runs /ingest-source.
---

# Ingest source

1. Read `research/CONTEXT.md`, `research/INDEX.md`, `research/catalog.md`.
2. If INDEX already has this URL or slug, stop and return the existing path.
3. Run `scripts/ingest.sh <url> <slug>` from the repo root. That writes `research/inbox/<date>-<slug>.*` and a `.meta.md` sidecar.
4. If the file is PDF or HTML, extract text into `research/extracts/<date>-<slug>.txt` (HTML: readable text only; PDF: see `scripts/extract-pdf.sh`).
5. Write `research/library/<date>-<slug>.md` from `references/library-card.md`.
6. Append INDEX. Set the catalog row to `on-disk` if the ID exists.
7. Reply with the library path. Do not keep a browser tab as the source of truth.

If download fails, leave the catalog row `listed` or `blocked` with the error. Do not invent the document.

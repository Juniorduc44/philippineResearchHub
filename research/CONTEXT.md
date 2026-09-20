# Research workspace

Last updated: 2026-09-20

## What happens here
This is the source library. Anything an AI would otherwise re-search in a browser is downloaded once, extracted if needed, and indexed. Later turns read the files.

## What the work is
Collect Philippines-primary sources for the hub: DTI, SEC, CDA, BIR, PSA, BSP, NEDA, BOI, TESDA, DA, DOT, DILG, PEZA, and reputable local reporting. Process them so `/directory` can cite a path instead of a URL.

## Process
1. Check `INDEX.md` and `catalog.md` before any network call.
2. If the file is already in `inbox/` or `library/`, stop. Read it.
3. If missing, download into `inbox/` with `scripts/ingest.sh` or skill `ingest-source`.
4. Extract text into `extracts/`. Write a short source card into `library/`.
5. Add a row to `INDEX.md`. Update `catalog.md` last-fetched date.
6. Briefs (syntheses across sources) go in `briefs/`. Briefs are not primary sources.

## What good looks like
- One download, one inbox object, one library card.
- Hash, URL, fetched date, and local path on every card.
- Quotes with page or section markers when the original is long.
- Official PH government and PSA/BSP statistics preferred over blogs.

## What to avoid
- Browsing a page that already has a local copy.
- Dumping raw HTML into `library/`. Library cards are markdown.
- Mixing opinion with source text. Opinion belongs in `/directory` or a brief.
- Paying-wall or login-gated dumps. Note the barrier on the catalog row instead.

## Files
- `catalog.md` — known sources and URLs (fetch list)
- `INDEX.md` — what is already on disk
- `inbox/` — raw bytes
- `extracts/` — plain text pulled from inbox
- `library/` — source cards the rest of the hub cites
- `briefs/` — cross-source notes

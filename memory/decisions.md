# Decisions

| Date | Decision | Reason |
|------|----------|--------|
| 2026-09-20 | `CLAUDE.md` is the only operating system. `AGENTS.md` is a pointer. | Clief Notes 1.2 + 3.2/3.3: one short routing file; Grok also auto-loads AGENTS.md so it must not duplicate. |
| 2026-09-20 | Three workspaces: directory, research, memory. | 3.3 mistake 3 — start with 2–4 mode shifts. Ideas vs sources vs handoff. |
| 2026-09-20 | First product is a business-ideas directory, not a live company listing. | Operator request: business ideas, Philippines focus. |
| 2026-09-20 | Files are the database. Naming conventions replace extra indexes except INDEX.md tables. | Clief Notes: naming conventions replace databases; token-efficient. |
| 2026-09-20 | Download-once into `research/inbox/`. Cite library cards, not live URLs, in idea files. | Operator request: nothing repeatedly looked up in a browser. |
| 2026-09-20 | Original Clief PDFs live in `archive/originals/`. Extracted method notes in `archive/foundation/`. | Keep guides for later builders without polluting the routing root. |
| 2026-09-20 | `/projects` is a fourth workspace: one folder per catalog idea. | Operator: expand ideas at repo root, not only as thin `idea.md` files. |
| 2026-09-20 | Project inner layout is lean / emyth / profit-first / philippines. | Matches the three scanned books plus PH ops. |
| 2026-09-20 | Lean Startup PDF is the Hungarian HVG 2013 scan. Cite PDF pages of that file. | Filename is English; body is not. |
| 2026-09-20 | Book `.txt` files in `research/library/` are the default read; PDF is fallback for figures or a garbled line. | Operator converted the scans to text. |
| 2026-09-20 | Do not re-download EO 113 or RA 11595; operator PDFs are canonical. RA 11647 from Lawphil because Gazette 403. | Local-first. |
| 2026-09-20 | `tools/browser-use` is a gitignored clone; `tools/fetch-blocked.py` is the hub fetch when curl 403s. | Operator asked for Browser Use locally. Cloudflare still beat Chromium on SEC. |
| 2026-09-20 | Public gallery lives in `docs/` for GitHub Pages (`/docs` on `main`). Not `pages/` — GH Pages cannot use that folder. | Operator asked for a live GitHub site. |
| 2026-09-21 | `godseye` at hub root starts God's Eye View. User-facing URL in this workspace is `http://localhost:8080/proxy/4173/` (code-server). | Direct `:4173` is container-only; Vite `base` must match the proxy path. |
| 2026-09-21 | Gallery ideas use 4–8 stills and `docs/GALLERY-STANDARD.md`. | Operator asked for a reusable slideshow template after HeliaSol. |
| 2026-09-24 | File the Traveling Techtician ladder as fourteen catalog ideas + GitHub Pages; generated stills are labeled. Do not cite convo statistics until ingested. | Operator added `docs/stuff/convo_00.md` and asked for a live portfolio of things that can be done. |
| 2026-09-20 | Helmet vending is the first active build; community-cold-storage stays an example shell. | Operator brief + Cebu corridor; example must still have a project folder. |

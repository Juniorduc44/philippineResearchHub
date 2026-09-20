# Philippine Research Hub

Local-first research workspace for the Philippines. First product: a business-ideas directory.

## Law
- This file is the only operating system. Match the query to the routing table before acting. Do not invent a second flow.
- Read only the files the matched row names. Load extra files only when that row or a named skill says to.
- Prefer files already in this repo over the web. If a source is missing, download it into `research/inbox/`, process it, and index it. Never re-fetch a file that already exists locally.
- Write new knowledge to disk. Chat is not memory.
- After material work, update `memory/PICKUP.md`.

## Workspaces
- `/directory` — idea catalog (one `idea.md` per slug)
- `/projects` — expanded build, one folder per idea
- `/research` — source library (inbox, extracts, briefs)
- `/memory` — pickup, decisions, glossary, session notes

## Routing
| Task | Go to | Read | Skill / workflow |
|------|-------|------|------------------|
| Session start, continue, where were we | `/memory` | `PICKUP.md`, then `CONTEXT.md` | `session-boot` |
| File or update a catalog entry | `/directory` | `CONTEXT.md`, `INDEX.md` | `capture-idea` |
| Expand, operate, or build an idea | `/projects` | `CONTEXT.md`, `INDEX.md`, then `<slug>/CONTEXT.md` | — |
| Download, ingest, cite, library search | `/research` | `CONTEXT.md`, `INDEX.md`, `catalog.md` | `ingest-source` |
| Any factual claim about PH | `/research` then `/directory` | `INDEX.md` files first | `local-first-research` |
| How to phrase a prompt | `/prompts` | `prompt-framework.md` | — |
| Close a session, handoff | `/memory` | `CONTEXT.md` | `session-close` |
| Change this OS | `/` | this file only | — |

## Naming
- Catalog: `directory/ideas/<slug>/idea.md`
- Builds: `projects/<slug>/`
- Raw downloads: `research/inbox/<yyyy-mm-dd>-<slug>.<ext>`
- Processed sources: `research/library/<yyyy-mm-dd>-<slug>.md`
- Sessions: `memory/sessions/<yyyy-mm-dd>-<topic>.md`

## Do not
- Invent Philippine law, fees, licenses, or statistics. Cite a local file or download one.
- Load every CONTEXT.md. One workspace per turn unless the task spans two rows.
- Treat manufacturer or operator claims as verified. Mark them `operator-brief` until a library card supports them.

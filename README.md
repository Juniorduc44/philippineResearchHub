# Philippine Research Hub

Local-first research workspace for the Philippines. First product: a **business-ideas directory**.

Any AI that opens this repo must follow **`CLAUDE.md`**. That file is the only operating system. `AGENTS.md` exists so Grok-family tools load the same rule.

## For humans
1. Open the folder in Grok, Claude Code, Cursor, or any file-aware agent.
2. Ask it to start. It should read `memory/PICKUP.md` next, not the whole tree.
3. File an idea with “capture this business idea: …” or `/capture-idea`.
4. Download a source with “ingest this URL …” or `/ingest-source`.
5. Do not keep official pages in a browser tab. They belong in `research/inbox/`.

Live gallery: **https://juniorduc44.github.io/philippineResearchHub/**

## Layout
```
CLAUDE.md          ← router (always loaded)
AGENTS.md          ← one-line pointer at CLAUDE.md
directory/         ← idea catalog
projects/          ← one expanded build per idea
docs/              ← GitHub Pages site (gallery + idea pages)
research/          ← downloads, extracts, library cards, books
memory/            ← pickup, decisions, glossary
prompts/           ← per-task prompt shape
.grok/             ← skills, workflow, agents, hooks (Grok)
.claude/           ← skill/agent copies (Claude Code)
archive/           ← original Clief Notes PDFs + extracts
scripts/           ← ingest and extract helpers
```

## Token rule
`CLAUDE.md` stays short. Workspace `CONTEXT.md` files load only when the routing table says so. Skills load on demand.

## License of method
Folder architecture follows Clief Notes Foundation lessons 1.2, 1.3, 3.2, 3.3 (archived under `archive/`). Philippine content is filed locally under `research/` and `directory/`.

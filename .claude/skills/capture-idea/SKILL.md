---
name: capture-idea
description: Create or update a Philippine business-idea dossier on disk. Use when the user has a business idea, opportunity, directory entry, or wants to file, score, or expand an idea. Use when the user runs /capture-idea.
---

# Capture idea

1. Read `directory/CONTEXT.md`, `directory/INDEX.md`, `directory/schema.md`.
2. If the idea already has a slug in INDEX, open that `idea.md` and update it. Do not fork a duplicate.
3. If new: pick a lowercase-hyphen slug, copy `directory/templates/idea.md` to `directory/ideas/<slug>/idea.md`, fill the schema.
4. Status starts at `stub` unless the user is only asking for the format — then `example`.
5. For licenses, fees, statistics: run the local-first rule. Put `unknown` plus an open question rather than guessing.
6. Append or update the INDEX row. Use a category key from `categories.md`.
7. Reply with the file path and the open questions. Do not paste the whole dossier.

For a multi-facet researched dossier, prefer workflow `/idea-dossier` instead of stretching this skill.

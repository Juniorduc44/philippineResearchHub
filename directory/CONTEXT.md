# Directory workspace

Last updated: 2026-09-20 (projects layer added)

## What happens here
This is the business-ideas catalog for the Philippines. Ideas go in, structured dossiers come out. Research support lives in `/research`. Expanded builds live in `/projects/<slug>/`. This folder only stores the catalog entry.

## What the work is
Build a reusable directory of Philippine business ideas a founder or operator could actually pursue. Each entry is a local file, not a database row. An idea is ready when a reader can answer: who pays, where, with what license, at what capital in PHP, and which local source backs each claim.

Audience: the hub operator first, then any AI working this repo, then a future public reader. Default lens is the Philippines — regions, LGUs, DTI/SEC/CDA/BIR, informal and formal markets. Do not import US/EU defaults.

## Process
1. Read `INDEX.md`. Reuse an existing slug if the idea is already filed.
2. Copy `templates/idea.md` to `ideas/<slug>/idea.md`.
3. Fill only what local sources support. Mark gaps as `unknown` with a source to fetch.
4. Link every non-obvious claim to a file under `research/library/` or `research/catalog.md`.
5. Create `projects/<slug>/` (shell is enough for `example` status).
6. Update `INDEX.md` and `categories.md` counts.

Status values: `stub` | `draft` | `reviewed` | `example`.

## What good looks like
- One idea per folder. Filename is always `idea.md`.
- Capital, fees, and prices in PHP. Name the year of the figure.
- Region or city named when location matters. "Philippines" alone is too coarse for operations.
- Competition named as real PH operators or a stated gap, not generic "many SMEs".
- Unknowns listed. No padded prose.

## What to avoid
- Treating an `example` entry as researched fact.
- Mixing two ideas in one file.
- Regulatory advice that is not tied to a downloaded source.
- Ranking ideas without a written rubric in the entry.

## Files
- `INDEX.md` — catalog table
- `categories.md` — category keys
- `schema.md` — field contract
- `templates/idea.md` — copy this
- `ideas/<slug>/idea.md` — entries

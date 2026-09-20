# Prompt framework

Persistent identity and project context live in `CLAUDE.md` and workspace `CONTEXT.md` files. Each prompt only carries the per-task parts.

## Five parts
Use only what the task needs.

1. **Identity** — already in the folder. Add a role only when the turn must shift (e.g. "you are checking licenses, not pitching").
2. **Task** — one action, defined scope, enough that a stranger could start.
3. **Context** — extra facts for this ask only. Do not paste a CONTEXT.md.
4. **Constraints** — what to avoid this time.
5. **Output format** — table, file path, stub, numbered list.

Simple fix → task only. Creative work → identity + task + constraints + format. Complex build or analysis → all five.

## Chunking
One prompt, one clear thing. Review between steps. Feed long sources in sections after giving the table of contents. Keep tables as tables.

## Hub pattern
```
Task: <action + slug or source id>
Constraints: local-first; PHP; no invented law
Output: write <path>; then one-paragraph summary
```

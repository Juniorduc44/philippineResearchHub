---
name: session-boot
description: Start or resume a hub session. Read the routing file and pickup notes, then wait for a task. Use when the user says hello, continue, where were we, pickup, resume, or opens a new session in this repo. Use when the user runs /session-boot.
---

# Session boot

1. Treat `CLAUDE.md` as already loaded. Do not read other CONTEXT files yet.
2. Read `memory/PICKUP.md`. If it is missing, say so and stop.
3. Reply with: (a) one-line hub state from pickup, (b) the single next action, (c) ask which routing-table row to run if the user did not name a task.
4. Do not load `/directory` or `/research` until the user picks a task or pickup names one file.

Never summarize the whole repo. Never browse.

# Skills

Canonical skill bodies live in `.grok/skills/` (Grok auto-load) and are copied to `.claude/skills/` (Claude Code auto-load).

Any other AI: `CLAUDE.md` names the skill; read `.grok/skills/<name>/SKILL.md` only when that row matches.

| Name | When |
|------|------|
| session-boot | New session, continue, pickup |
| local-first-research | Facts, citations, look-ups |
| ingest-source | Download and file a source |
| capture-idea | File or update an idea |
| session-close | Handoff, wrap up |

Do not add a second copy of a skill body in this folder.

# Tools

Local helpers. Not a workspace. Do not load this folder unless ingesting a blocked page or installing a fetcher.

## browser-use (cloned)

Path: `tools/browser-use/`  
Upstream: https://github.com/browser-use/browser-use

This is the Browser Use library (AI browser agent + Chromium via CDP). Clone is gitignored; recreate with:

```bash
git clone --depth 1 https://github.com/browser-use/browser-use.git tools/browser-use
```

Hub rule: **curl first** (`scripts/ingest.sh`). Use a real browser only when the host returns 403, a JS shell, or Cloudflare “Just a moment…”.

### Fetch a blocked page (no LLM key)

Playwright Chromium is installed in `tools/.venv`. Shared libraries need Debian packages (`libnspr4`, `libnss3`, …).

```bash
tools/.venv/bin/python tools/fetch-blocked.py '<url>' '<slug>'
```

Writes `research/inbox/<date>-<slug>.html` and `.meta.md`. If title is `Just a moment...` the save is a challenge page, **not** the document. Catalog it as `blocked`.

### Full Browser Use agent

Needs `uv`, Chromium, and an API key (`BROWSER_USE_API_KEY`). See `tools/browser-use/README.md`. The Grok `browser-use` skill talks to an MCP daemon; that path is separate from this clone.

## Other
- `tools/.venv` — pypdf, pypdfium2, playwright (gitignored)
- `scripts/ingest.sh` — ordinary HTTP ingest

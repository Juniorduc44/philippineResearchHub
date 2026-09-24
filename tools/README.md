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

## God's Eye View (cloned)

Path: `tools/gods-eye-view/` (gitignored)  
Upstream: https://github.com/bilawalsidhu/gods-eye-view  
How to run: `godseye` from the hub root → http://127.0.0.1:4173/  
Notes: `tools/gods-eye.md`

Live 3D globe (Cesium) with public layers. No keys to start. Optional keys in the in-app POWER UP panel.

```bash
godseye           # foreground
godseye --bg
godseye --stop
```

First run vendors Node 24.14 under `tools/.node/` (system Node 20 is too old) and `npm ci`. Recreate the clone with:

```bash
git clone --depth 1 https://github.com/bilawalsidhu/gods-eye-view.git tools/gods-eye-view
```

## Other
- `tools/.venv` — pypdf, pypdfium2, playwright (gitignored)
- `tools/.node/` — Node 24 for God's Eye (gitignored)
- `scripts/ingest.sh` — ordinary HTTP ingest

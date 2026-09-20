#!/usr/bin/env python3
"""Fetch a bot-blocked URL with Chromium and write inbox + meta.

Usage: tools/.venv/bin/python tools/fetch-blocked.py <url> <slug>
Requires: playwright + chromium (see tools/README.md).
"""
from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "research" / "inbox"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: fetch-blocked.py <url> <slug>", file=sys.stderr)
        return 2
    url, slug = sys.argv[1], sys.argv[2]
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    INBOX.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="PhilippineResearchHub/1.0 (documentation; Playwright)"
        )
        page = context.new_page()
        resp = page.goto(url, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(2500)
        html = page.content()
        status = resp.status if resp else 0
        final = page.url
        title = page.title()
        browser.close()

    dest = INBOX / f"{date}-{slug}.html"
    dest.write_text(html, encoding="utf-8")
    sha = hashlib.sha256(dest.read_bytes()).hexdigest()
    host = urlparse(final).netloc
    meta = INBOX / f"{date}-{slug}.meta.md"
    meta.write_text(
        f"# {date}-{slug}\n\n"
        f"- URL: {url}\n"
        f"- Final URL: {final}\n"
        f"- Title: {title}\n"
        f"- HTTP: {status}\n"
        f"- Fetched: {date}\n"
        f"- Method: playwright-chromium (curl blocked)\n"
        f"- Host: {host}\n"
        f"- Bytes: {dest.stat().st_size}\n"
        f"- SHA256: {sha}\n"
        f"- Inbox: research/inbox/{dest.name}\n",
        encoding="utf-8",
    )
    print(dest)
    print(meta)
    print(f"status={status} title={title!r} bytes={dest.stat().st_size}")
    return 0 if status and status < 400 else 1


if __name__ == "__main__":
    raise SystemExit(main())

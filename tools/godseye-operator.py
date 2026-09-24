#!/usr/bin/env python3
"""Drive the local God's Eye View GUI and write watch screenshots."""
from __future__ import annotations

import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

HUB = Path(__file__).resolve().parents[1]
WATCH = HUB / "tools" / ".godseye-watch"
WATCH.mkdir(parents=True, exist_ok=True)

CEBU = (
    "http://127.0.0.1:4173/"
    "?welcome=0"
    "#v=2&lat=10.3307983&lon=123.9068258&alt=4500"
    "&heading=20&pitch=-55&style=normal"
)


def snap(page, name: str) -> Path:
    dest = WATCH / f"{name}.png"
    page.screenshot(path=str(dest), full_page=False)
    latest = WATCH / "latest.png"
    latest.write_bytes(dest.read_bytes())
    print(f"shot {dest.name} {dest.stat().st_size} bytes", flush=True)
    return dest


def main() -> int:
    url = sys.argv[1] if len(sys.argv) > 1 else CEBU
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--use-gl=angle",
                "--use-angle=swiftshader",
                "--enable-webgl",
                "--ignore-gpu-blocklist",
                "--no-sandbox",
            ],
        )
        context = browser.new_context(
            viewport={"width": 1400, "height": 900},
            device_scale_factor=1,
        )
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(4000)
        snap(page, "01-boot")

        # Share links skip first-run; still click through if it appears.
        launcher = page.locator("#first-run-launcher")
        if launcher.count() and launcher.first.is_visible():
            snap(page, "01b-welcome")
            contacts = page.locator('[data-first-run-choice="contacts"]')
            if contacts.count():
                contacts.first.click()
                page.wait_for_timeout(3000)

        try:
            page.wait_for_selector("canvas", timeout=25000)
        except Exception:
            print("no canvas yet", flush=True)
        page.wait_for_timeout(8000)
        snap(page, "02-globe")

        # Search box if present
        for sel in [
            'input[type="search"]',
            'input[placeholder*="Search" i]',
            "#location-search",
            '[data-location-search] input',
        ]:
            box = page.locator(sel)
            if box.count() and box.first.is_visible():
                box.first.fill("Cebu IT Park")
                box.first.press("Enter")
                page.wait_for_timeout(5000)
                snap(page, "03-search-cebu")
                break

        # Try a small camera orbit via Cesium if exposed
        page.evaluate(
            """() => {
              const v = globalThis.viewer || globalThis.gevViewer;
              if (!v || !v.camera) return 'no-viewer';
              v.camera.rotateRight(0.35);
              return 'rotated';
            }"""
        )
        page.wait_for_timeout(2500)
        snap(page, "04-orbit")

        title = page.title()
        print(f"title={title!r}", flush=True)
        print("done", flush=True)
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

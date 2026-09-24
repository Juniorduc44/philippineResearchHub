# GitHub Pages site

This folder is the live site. GitHub Pages serves `/docs` on `main`.

Live URL: https://juniorduc44.github.io/philippineResearchHub/

GitHub Actions deploys this folder on every push to `main` (`.github/workflows/pages.yml`). If the first run fails, set **Settings → Pages → Source** to **GitHub Actions** and re-run the workflow.

- Light mode default; header toggle saves `prh-theme`
- Home hero is a slideshow of the active idea (helmet: `images/helmet-vending_00.png` … `_03.png`)
- Idea pages use **4–8** photos; see `GALLERY-STANDARD.md` and `templates/slideshow.html`
- `ideas/<slug>.html` for each catalog idea; back links return home
- Home also has **Investigate first** (eight Traveling Techtician rungs) and **Also on the ladder** (six more). Stills are generated unless CREDITS says otherwise.

Do not put the site in `/pages` — GitHub Pages only builds `/` or `/docs`.

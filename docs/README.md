# GitHub Pages site

This folder is the live site. GitHub Pages serves `/docs` on `main`.

Live URL: https://juniorduc44.github.io/philippineResearchHub/

GitHub Actions deploys this folder on every push to `main` (`.github/workflows/pages.yml`). If the first run fails, set **Settings → Pages → Source** to **GitHub Actions** and re-run the workflow.

- Light mode default; header toggle saves `prh-theme`
- Home hero + gallery
- `ideas/<slug>.html` for each catalog idea; back links return home

Do not put the site in `/pages` — GitHub Pages only builds `/` or `/docs`.

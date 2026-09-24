# Gallery standard

Every catalog idea that appears on the GitHub Pages site follows this. Helmet vending (`docs/images/helmet-vending_00.png`–`_03.png`) is the first live example. HeliaSol façade film uses eight Heliatek photos.

## Count

- **4 to 8** still photos per idea.
- Fewer than 4 is a single hero (allowed only while hunting photos).
- More than 8: pick the strongest 8. Do not dump a folder.

## Files

```
docs/images/<slug>_00.<ext>
docs/images/<slug>_01.<ext>
…
docs/images/<slug>_07.<ext>   # max
```

- Zero-padded two-digit index.
- `jpg` or `png`. Keep the original format from the source.
- First frame (`_00`) is the **gallery card** thumbnail and should still make sense cropped 16:9-ish (`object-fit: cover`).
- Write alt text in the HTML, not in the filename.

## Credits

Add a row to `docs/images/CREDITS.md`: slug, source URL, publisher, date fetched, whether we have rights to republish (manufacturer press photo vs operator original vs generated).

## HTML

Copy `docs/templates/slideshow.html`.

- Home hero: one idea at a time (usually the **active** build). Same `data-slides` markup.
- Idea page: `div.detail-hero[data-slides]` with the same 4–8 images.
- Gallery card: **one** image (`_00` or `_01` if `_00` is a process diagram).
- Include `js/slides.js` on any page with `data-slides`. The script no-ops if there is only one `<img>`.

## Behaviour (already in `slides.js`)

- Auto-advance every 4.5 s.
- Pause on hover.
- Prev / next buttons and dots.
- First image has class `is-on`.

## Photo rules

1. Prefer **on-disk sourced photos** (operator camera, manufacturer press, ingested URL). Do not invent a building.
2. Generated art is allowed only when labeled and never as a substitute for a product you could photograph.
3. Sequence should tell a story: install or product close-up → façade/site → process if useful → scale.
4. Check desktop **and** a ~390 px viewport: overlay title must stay readable (`docs/css/site.css` hero scrim).

## New idea checklist

1. `directory/ideas/<slug>/idea.md` from `directory/templates/idea.md`.
2. `projects/<slug>/` at least `CONTEXT.md` + `brief.md`.
3. 4–8 images named as above + CREDITS row.
4. `docs/ideas/<slug>.html` using the slideshow template.
5. Card on `docs/index.html`.
6. Rows in `directory/INDEX.md` and `projects/INDEX.md`.

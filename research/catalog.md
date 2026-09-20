# Source catalog

Official and recurring sources. Check `INDEX.md` before fetching. After a download, set **On disk** to the library path.

Status: `listed` (URL only) | `on-disk` | `blocked`.

## Government and statistics

| ID | Publisher | What | URL | On disk |
|----|-----------|------|-----|---------|
| dti-start-business | DTI | Starting a business | https://www.dti.gov.ph/dti-business-center/dti-start-grow-your-business | `research/library/2026-09-20-dti-start-grow.md` |
| dti-bnrs | DTI | Business name registration portal | https://bnrs.dti.gov.ph | `research/library/2026-09-20-dti-bnrs.md` |
| dti-home | DTI | Agency home | https://www.dti.gov.ph | `research/library/2026-09-20-dti-home.md` |
| dti-business-center | DTI | Business Center hub | https://www.dti.gov.ph/dti-business-center | `research/library/2026-09-20-dti-business-center.md` |
| sec-home | SEC | Company registration | https://www.sec.gov.ph | blocked (403 / Cloudflare) |
| sec-primary-registration | SEC | Primary registration how-to | https://www.sec.gov.ph/company/primary-registration-2/ | blocked (Cloudflare challenge saved) |
| sec-esparc | SEC | eSPARC online registration | https://esparc.sec.gov.ph/ | blocked (Cloudflare challenge saved) |
| eo-113 | Official Gazette / OP | 13th RFINL (EO 113 s. 2026) | https://www.officialgazette.gov.ph/2026/04/13/executive-order-no-113-s-2026/ | `research/library/2026-09-20-eo-113.md` (operator PDF; HTML 403) |
| ra-11647 | Congress | Foreign Investments Act amendment | https://lawphil.net/statutes/repacts/ra2022/ra_11647_2022.html | `research/library/2026-09-20-ra-11647.md` (Gazette URL 403) |
| ra-11595 | Congress | Retail Trade Liberalization amendment | https://lawphil.net/statutes/repacts/ra2021/ra_11595_2021.html | `research/library/2026-09-20-ra-11595.md` |
| bir-home | BIR | Tax registration | https://www.bir.gov.ph | `research/library/2026-09-20-bir-home.md` (JS shell; almost no text) |
| cda-home | CDA | Cooperatives | https://cda.gov.ph | listed |
| psa-home | PSA | Statistics home | https://psa.gov.ph | blocked (403 on 2026-09-20) |
| psa-openstat | PSA | OpenSTAT tables | https://openstat.psa.gov.ph | blocked (403 on 2026-09-20) |
| psa-psic | PSA | PSIC classification portal | https://psa.gov.ph/classification/psic | `research/library/2026-09-20-psa-psic.md` |
| bsp-home | BSP | Monetary and banking | https://www.bsp.gov.ph | `research/library/2026-09-20-bsp-home.md` |
| neda-home | NEDA | Development planning | https://www.neda.gov.ph | blocked (timeout on 2026-09-20) |
| boi-home | BOI | Investment promotions | https://boi.gov.ph | blocked (403 on 2026-09-20) |
| peza-home | PEZA | Ecozones | https://www.peza.gov.ph | listed |
| tesda-home | TESDA | Skills and TVET | https://www.tesda.gov.ph | blocked (timeout on 2026-09-20) |
| da-home | DA | Agriculture | https://www.da.gov.ph | listed |
| dot-home | DOT | Tourism | https://beta.tourism.gov.ph | listed |
| dilg-home | DILG | LGUs | https://www.dilg.gov.ph | listed |

## Books (on disk)

| ID | Publisher | What | URL | On disk |
|----|-----------|------|-----|---------|
| book-e-myth | Gerber / HarperCollins scan | E-Myth Revisited | local PDF | `research/library/2026-09-20-e-myth-revisited.md` |
| book-profit-first | Michalowicz scan | Profit First | local PDF | `research/library/2026-09-20-profit-first.md` |
| book-lean-startup | Ries / HVG 2013 HU | Lean Startup (Hungarian scan) | local PDF | `research/library/2026-09-20-lean-startup.md` |

## How to add
1. New ID: lowercase-hyphens, publisher first (`dti-…`).
2. Prefer the canonical agency URL, not a news rewrite.
3. Fetch with `ingest-source`. Do not paste a URL into an idea file as if it were already local.
4. If curl gets 403/timeout, mark `blocked` and keep the row. Try a PDF or child page later — do not hammer the same URL.

# Brief: Helmet cleaning machine candidates (Haloo single vs stacked dual, PH vs China)

- Date: 2026-09-21
- Status: short brief (see the full report)
- Project: `projects/helmet-vending/`
- Operator file: `projects/helmet-vending/philippines/machine-candidates.md`
- Full report: `research/briefs/2026-09-21-helmet-machine-candidates-report.md`

## Question
What machines can this Cebu one-unit MVP actually buy or have shipped, what they cost, and how Haloo’s single-helmet cabinet compares with the stacked two-compartment cabinet (one chamber over the other)? Show CNY, PHP, and USD.

## Price class (read this first)

| Class | Meaning | Used here? |
|-------|---------|------------|
| **invoice** | Paid quote, PI, or receipt | **None on disk** |
| **listing** | Factory/marketplace ask price | Haloo EveryChina / haloovendingmachine.com / Made-in-China / ChinaX / Ouyuan MIC |
| **press / ad** | Newspaper, TV recap, directory ad | Go Clean Tribune/PEP; Quick Fresh GMA/BusinessDiary; iCleaN'GO FindGlocal |
| **operator-brief** | Hub notes | ₱44k–₱75k+ band in the 2026-09-20 helmet brief |

Do not treat listing or press as what a Cebu buyer would pay after freight, duties, and site work.

## FX used (dated)

Primary table is the BSP Reference Exchange Rate Bulletin dated **21 September 2026** (`research/library/2026-09-21-bsp-rerb-xlsx.md`). Underlying close is **18 September 2026** (weekend bulletin).

| Pair | Rate | Source |
|------|------|--------|
| 1 USD → PHP | **62.67** | BSP RERB PHP equivalent of USD |
| 1 CNY → PHP | **9.3559** | BSP RERB PHP equivalent of yuan |
| 1 CNY → USD | **0.149289** | BSP RERB USD equivalent of yuan |
| BSP reference USD/PHP | 62.75 | same sheet |
| BSP buying / selling T/T | 62.50 / 63.00 | same sheet |
| SDDS PHP per USD | 62.670 (21-Sep-2026) | `2026-09-21-bsp-sdds-exchange-rates.md` |

China-side board, same calendar day (`2026-09-21-boc-exchange-rate.md`, 09:55):

| BOC (per 100 foreign units → CNY) | Middle | Implied |
|-----------------------------------|--------|---------|
| USD | 674.87 | 1 USD ≈ **6.7487 CNY** |
| PHP | 10.67 | 1 CNY ≈ **9.3721 PHP** |

PH bank counter, 18 Sep 2026 09:30 (`2026-09-21-chinabank-forex.md`): USD 62.15 / 63.05; CNY 9.0861 / 9.5939 (indicative).

**Conversion path in the tables below (what was asked):**

1. Take the listed currency.
2. **CNY → PHP** at BSP 9.3559 (or PHP → CNY by dividing).
3. **PHP → USD** at BSP 62.67.
4. If the listing is already USD, implied CNY = USD × 62.67 / 9.3559, then the same CNY → PHP → USD path (it round-trips to the listing USD).

No Haloo page on disk quotes the cabinet in **yuan**. CNY columns for those SKUs are **implied** from USD listings via BSP, not factory RMB price lists.

## YouTube title

Asked-for title: *Commercial Helmet Cleaning Machine | Automated Cleaning Solution for Rental Businesses*.

On disk, Dongguan Haloo Automation Equipment Co.,Ltd’s matching helmet video is **not** that title. oEmbed + watch page (`2026-09-21-haloo-youtube-oembed-sc_4dHcXYG0.md`):

> This is a non selling vending machine that specializes in cleaning helmets  
> https://www.youtube.com/watch?v=sc_4dHcXYG0

A **BLEE** marketing page uses a close rental title (*Helmet Self-Service Cleaning Machines for Delivery & Rental Businesses*) and has **no unit price** in the extract (`2026-09-21-blee-helmet-rental-guide.md`).

## Haloo: single vs stacked dual

Factory: Dongguan Haloo Automation Equipment Co., Ltd, Dinghao Zhigu Industrial Park, Houjie, Dongguan. Contact on factory pages: David, +86 13809260051, yhq@gd-haloo.com. MOQ **1 set**. After-sales on listings: video / online. Warranty **1 year**. Export pack: wooden crate. Lead time on EveryChina: **35 days** (factory, not door-to-Cebu).

| | **HL-Helmet-B01 (single)** | **HL-Helmet-B02 / dual warehouse (stacked)** |
|--|----------------------------|-----------------------------------------------|
| What it is | One cleaning compartment, one door | Two warehouse doors; two compartments; perfume split 2+2 per warehouse (chamber over chamber) |
| Size | 660 × 1966 × 600 mm | 650 × 2025 × 600 mm |
| Weight (pages disagree) | 160–180 kg | 160–200 kg |
| Screen | 12.1 in | 15.6 in |
| Power | 2100 W | 2100 W (B02 factory) or 1500 W (HL-XYJ-L01-D02 listing) |
| Process (manufacturer) | Steam + UV, PTC dry, 3 modes | Same, independent dual warehouses |
| Certs claimed | CE / FCC / ROHS (varies by page) | CE / FCC / ROHS |
| Factory page price | **none** | **none** (URL says “factory-price”) |
| Listing USD (not invoice) | **$2,000 / piece** EveryChina + haloovendingmachine.com + ChinaX | **$2,600 / piece** EveryChina + ChinaX B02; **$2,300 / piece** HL-XYJ-L01-D02 2-helmet; Made-in-China **$1,799** (1–9) / **$1,500** (10+) with conflicting 1860 mm height |

Stacked dual is **one taller cabinet**, not a second site. Height ~2.03 m vs Go Clean’s 72 in (~1.83 m). Check parking-bay headroom before ordering B02.

### Haloo listings converted (BSP 21 Sep 2026)

| SKU (listing) | Listed USD | Implied CNY (USD×62.67/9.3559) | PHP (CNY×9.3559) | USD via PHP÷62.67 |
|---------------|------------|--------------------------------|------------------|-------------------|
| B01 single, EveryChina $2000 | 2,000.00 | 13,396.89 | 125,340 | 2,000.00 |
| XYJ-L01-D02 dual, $2300 | 2,300.00 | 15,406.43 | 144,141 | 2,300.00 |
| B02 dual, EveryChina $2600 | 2,600.00 | 17,415.96 | 162,942 | 2,600.00 |
| MIC B02 band $1,799 (1–9) | 1,799.00 | 12,050.51 | 112,743 | 1,799.00 |
| MIC B02 band $1,500 (10+) | 1,500.00 | 10,047.67 | 94,005 | 1,500.00 |

Same $2,000 through **BOC** (China board): 2,000 × 6.7487 = **13,497.40 CNY** → × 9.3721 ≈ **126,500 PHP** → ÷ 62.67 ≈ **2,018 USD**. The extra ~₱1,160 vs BSP is board-spread, not freight.

**Still missing on every China page:** ocean/air freight to Cebu or Manila, insurance, BOC duties/VAT, last-mile, installation, GCash/Maya kit, spare pumps, solution drums. Made-in-China: “Shipping Cost: Contact the supplier.” Landed cost is **unknown**.

Alibaba product `1601646947816` was ingested but the extract is an empty JS shell. **Do not cite search-result $1,688 as on-disk.**

## Philippine machines you can buy without a China shipment

These are **peso asks in PH**. Access is local pickup / NCR shipping / distributor, not a Dongguan crate.

| Candidate | Chambers | Listed / press PHP | CNY (PHP÷9.3559) | USD (PHP÷62.67) | Access |
|-----------|----------|--------------------|------------------|-----------------|--------|
| Go Clean (Tribune 2025-10-03) | 1 (72×18×20 in) | ₱44,000–₱55,000 | 4,703–5,879 | 702–878 | PH-made, SEC-registered GCVM per press; Manila office on gocleanphilippines.com |
| Go Clean (PEP 2025-10-16) | 1 | ₱45,000–₱55,000; rider ₱25/cycle | 4,810–5,879 | 718–878 | Same firm; All-in-one also ₱55,000 |
| iCleaN'GO directory ad (2024-10-15) | 1 (not specified as dual) | ₱44,999 + free NCR ship, 2 gallons, tarpaulin; 3-month warranty | 4,810 | 718 | Parañaque listing, not an invoice |
| Quick Fresh (GMA 2024-09-13 + BusinessDiary) | 1 (5-step fog/UV/ozone/heat/scent) | ₱265,000 incl. solution + fragrance; ₱100/cycle | 28,324 | 4,228 | Owner Joyce Malasa; machines “from abroad”; PH distributorship |

Go Clean homepage has **no peso price**; dimensions and 900 W fogger + UVC are on-site. Cycle ₱25 is PEP, not the company home page.

**Shield-Pro** Facebook promo bands (₱49k–₱65k) were **not ingested**. Treat as unsourced until a page is on disk.

**FresHelmet (Taiwan)** documents the same stacked idea as Haloo B02: model **A026**, upper and lower layers, independent start buttons (`2026-09-21-freshelmet-ihelmetspa.md`). Ships internationally, no MOQ on that page. **No TWD/USD/PHP/CNY machine price on disk.** A YouTube comment “₱100k” is not a listing.

## Other China OEM (listing, not Haloo)

Dongguan **Ouyuan** dual OYTK2501-2: 650 × 1790 × 550 mm, 115 kg, A/B chambers (`2026-09-21-ouyuan-dual-oytk2501-2.md`). No cabinet price on the product page. Made-in-China home lists rental-shop units **US$1,906–1,979** and a wider **US$1,622–2,320** band. Transport “to local area” 30–50 days. RMB 15.00/cycle in their ROI table is **marketing P&L**, not a PH price.

Converted Ouyuan MIC rental band at BSP 21 Sep 2026:

| Listed USD | Implied CNY | PHP | USD check |
|------------|-------------|-----|-----------|
| 1,906 | 12,767.24 | 119,449 | 1,906.00 |
| 1,979 | 13,256.23 | 124,024 | 1,979.00 |

## What you can get access to vs what you can get shipped

| Path | What you get | Time / friction | Money shape |
|------|----------------|-----------------|-------------|
| **Buy in PH (Go Clean / similar ads)** | Single-chamber vendo, peso invoice possible, local techs, NCR or Manila dispatch | Days–weeks if in stock (not verified) | ~₱45k–₱55k **press/ad**. No China freight. |
| **Import Haloo B01** | Single steam/UV Android kiosk, 1.97 m | 35-day factory quote + unknown ocean/air + BOC | ~$2,000 **listing** ≈ ₱125,340 **FX only**. Landed unknown, almost certainly above local Go Clean. |
| **Import Haloo B02 / XYJ dual** | Stacked two-compartment, ~2.03 m, two independent cleans | Same import path; taller crate | $1,799–$2,600 **listing** ≈ ₱112,743–₱162,942 **FX only**. Still below Quick Fresh’s ₱265k press price, still above Go Clean, **before** freight/duty. |
| **Import Ouyuan dual** | Shorter dual (1.79 m, 115 kg) | 15–25 day build + 30–50 day transport (manufacturer) | ~$1,906–$1,979 **listing** ≈ ₱125k–₱130k FX |
| **FresHelmet A026** | Taiwan dual slot, independent decks | International ship, no MOQ stated | **Price unknown** |

For the **one-machine Cebu MVP**, the files still say: a local single-chamber unit is the accessible, cheaper cabinet. Dual stacked is a **throughput option** (two riders at once), not a second location. Do not buy either class until a written bay yes exists (`memory/PICKUP.md`).

## Gaps

- No invoice, pro forma, or CIF Cebu/Manila quote.
- No Haloo CNY list price (1688/Taobao not fetched).
- Alibaba HTML empty.
- Shield-Pro and FresHelmet PH agent prices not on disk.
- FDA/solution claims remain manufacturer or press.
- Freight $300–$800 figures that appear in aggregator blogs were **not** used; they are not on these library cards.

## Implication for the project

Fill `projects/helmet-vending/philippines/machine-candidates.md` (same numbers). Get a **written quote** (local Go Clean / iCleaN'GO / Quick Fresh **and**, if dual is required, Haloo/Ouyuan PI with freight to Cebu). Until that file is an invoice, unit economics stay unknown.

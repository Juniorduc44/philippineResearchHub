# Report: Helmet cleaning machine candidates for a Cebu one-unit test

- Date: 2026-09-21
- Status: sourced draft (no invoices)
- Project: `projects/helmet-vending/`
- Short operator table: `projects/helmet-vending/philippines/machine-candidates.md`
- Earlier brief (same numbers, shorter): `research/briefs/2026-09-21-helmet-machine-candidates.md`

## 0. How to read this

This is the long file. Every peso, dollar, and yuan figure is either (a) copied from a library card, or (b) converted with the dated BSP bulletin in §2. **None of the machine prices are invoices.** Manufacturer kill-rates, payback stories, and “60 units a day” production claims stay labeled as marketing or press.

Asked: document Haloo (Dongguan) single vs stacked dual, compare what else is for sale, show access vs shipping, and put every price in **CNY, PHP, and USD**.

## 1. Findings

1. **Dongguan Haloo Automation Equipment Co., Ltd** sells two helmet cabinets that match the video: **HL-Helmet-B01** (one compartment) and **HL-Helmet-B02** / **HL-XYJ-L01-D02** (two warehouse doors, one chamber over the other). Factory pages have **no price**. Export listings are **USD**, not yuan.
2. **Listing band (not invoice):** single about **US$2,000**; stacked dual **US$1,799–$2,600** depending on portal and quantity. At BSP 21 Sep 2026 that is **₱94,005–₱162,942** and **¥10,048–¥17,416** implied.
3. **Local Philippine cabinets you can buy without a China crate** sit much lower in press/ads: Go Clean **₱44,000–₱55,000** (¥4,703–¥5,879 / $702–$878). iCleaN'GO directory ad **₱44,999**. Quick Fresh press **₱265,000** (¥28,324 / $4,229) for an imported 5-step kiosk.
4. **Stacked dual exists outside Haloo:** FresHelmet Taiwan **A026** (upper/lower independent; **no factory price on disk**); Ouyuan Dongguan **OYTK2501-2** (A/B chambers, 1.79 m, listing about **US$1,906–$1,979**).
5. **The YouTube title you named is not on the Haloo clip we archived.** Haloo’s video is *This is a non selling vending machine that specializes in cleaning helmets*. A BLEE page uses a close “delivery & rental” title and has no unit price.
6. **For the Cebu one-machine MVP:** a local single-chamber vendo is the accessible, cheaper path. Dual stacked is one taller footprint (Haloo ~2.03 m vs Go Clean ~1.83 m), not a second site. Landed China cost is **unknown** (freight, duty, VAT, last-mile missing). Do not buy before a written bay yes.

## 2. Method, price class, FX

### 2.1 Price class

| Class | Meaning | In this report |
|-------|---------|----------------|
| invoice / PI | Paid quote, commercial invoice, receipt | **None** |
| listing | Factory or marketplace ask | Haloo EveryChina, haloovendingmachine.com, Made-in-China, ChinaX, Ouyuan MIC |
| press / ad | Newspaper, TV recap, directory | Tribune, PEP, GMA, BusinessDiary, FindGlocal |
| operator-brief | Hub working notes | ₱44k–₱75k+; ₱25–₱100/cycle |
| manufacturer marketing | ROI tables, 99% kill, 60-second clean | Haloo FAQs, Ouyuan RMB P&L, FresHelmet lab copy |

### 2.2 FX (dated 21 September 2026)

Primary: BSP Reference Exchange Rate Bulletin, run 21-Sep-2026 08:34 AM, underlying close **18 Sep 2026** (weekend). Library: `research/library/2026-09-21-bsp-rerb-xlsx.md`. Inbox xlsx saved as `.bin`.

| Pair | Rate | Use |
|------|------|-----|
| 1 USD → PHP | **62.67** | PHP equivalent of USD |
| 1 CNY → PHP | **9.3559** | PHP equivalent of yuan |
| 1 CNY → USD | **0.149289** | USD equivalent of yuan |
| BSP reference USD/PHP | 62.75 | board, not used in tables |
| BSP buying / selling T/T | 62.50 / 63.00 | board |
| PDS close 18-Sep-2026 | 62.749 | board |
| SDDS PHP per USD 21-Sep-2026 | 62.670 | `2026-09-21-bsp-sdds-exchange-rates.md` (USD only) |

**Conversion path (as asked): listed currency → CNY → PHP → USD.**

- PHP listing: CNY = PHP ÷ 9.3559; USD = PHP ÷ 62.67.
- USD listing: implied CNY = USD × 62.67 ÷ 9.3559; PHP = that CNY × 9.3559 (= USD × 62.67); USD check = PHP ÷ 62.67.

No Haloo cabinet is priced in **yuan** on disk. CNY for those SKUs is **implied**, not a factory RMB list.

### 2.3 Other boards (same week, not used as the table rate)

Bank of China, 2026-09-21 09:55 (`2026-09-21-boc-exchange-rate.md`), quotes **RMB per 100 units** of foreign currency:

| | Buying | Selling | Middle | Implied |
|--|--------|---------|--------|---------|
| USD | 668.4 | 671.21 | 674.87 | 1 USD ≈ **6.7487 CNY** |
| PHP | 10.55 | 10.77 | 10.67 | 1 CNY ≈ **9.3721 PHP** |

Worked example, **US$2,000 listing through BOC then BSP PHP→USD:**

1. 2,000 × 6.7487 = **¥13,497.40**
2. 13,497.40 × 9.3721 ≈ **₱126,499**
3. 126,499 ÷ 62.67 ≈ **US$2,018**

The extra ~₱1,160 vs BSP is **board spread**, not freight.

China Bank Philippines, 09:30 on **18 Sep 2026** (`2026-09-21-chinabank-forex.md`), indicative: USD 62.15 / 63.05; CNY 9.0861 / 9.5939. Counter, not BSP.

## 3. The video and the factory

### 3.1 Title check

| String | On disk? |
|--------|----------|
| Commercial Helmet Cleaning Machine \| Automated Cleaning Solution for Rental Businesses | **Not found** as a Haloo YouTube title |
| This is a non selling vending machine that specializes in cleaning helmets | **Yes** — Haloo channel, `sc_4dHcXYG0`, oEmbed + watch page |
| Helmet Self-Service Cleaning Machines for Delivery & Rental Businesses | **Yes** — BLEE marketing page, no unit price |

Haloo oEmbed: author **Dongguan Haloo Automation Equipment Co.,Ltd**. Watch: https://www.youtube.com/watch?v=sc_4dHcXYG0. Cards: `2026-09-21-haloo-youtube-oembed-sc_4dHcXYG0.md`, `2026-09-21-haloo-youtube-watch-sc_4dHcXYG0.md`.

Web index of that video (not a local transcript): 3–8 minute cycle; UV + plasma + disinfectant; QR / coin / card; gas stations, dealerships, helmet rental, delivery, mall parking, clubs. Treat as manufacturer copy until a transcript is ingested.

### 3.2 Company (manufacturer pages)

- **Haloo Automation Equipment Co., Ltd**, APVA member, vending OEM (snacks, ice, pizza, helmets, etc.).
- Address on factory pages: Room 601, Building 2, Dinghao Zhigu Industrial Park, No. 250 Xihuan Road, Houjie Town, Dongguan, Guangdong, China.
- Contacts seen: David / Cherry Chen; +86 13809260051; yhq@gd-haloo.com and wm@gd-haloo.com.
- One factory FAQ: based in Guangdong, start 2015, office 11–50 people; claimed sales mix includes Southeast Asia 15%.
- Exclusive agent named for **Sri Lanka and Maldives**: Sterling Corporation (Pvt) Ltd. **No Philippine agent on these pages.**
- MOQ **1 set**. Warranty **1 year**. After-sales: video / online. Payment extras (example QR NV11) cost extra per B02 FAQ.
- Electricity FAQ (B01 page): **10–12 kWh for an average 8-hour day** (also written “requiring 10 kWh”). No peso kWh rate on disk — do not invent Meralco.

## 4. Haloo cabinets: one helmet vs compartment over compartment

This is the comparison the video asked for.

### 4.1 Side by side (manufacturer pages; pages disagree where noted)

| | **HL-Helmet-B01** single | **HL-Helmet-B02** stacked dual | **HL-XYJ-L01-D02** 2-helmet listing |
|--|--------------------------|--------------------------------|-------------------------------------|
| Layout | Single warehouse door, 1 helmet | **2 warehouse doors**; 4 perfume bottles, **2 per warehouse** | Capacity **2 helmet**; 650 × 2025 × 600 mm |
| Size | 660 W × 1966 H × 600 D mm | 650 W × **2025** H × 600 D mm | same envelope as B02 |
| Weight | 180 kg (table) / 160 kg (other pages) | 200 kg (table) / 160 kg (UV page) | **160 kg** |
| Screen | 12.1 in | 15.6 in | 15.6 in |
| Power | 2100 W | 2100 W | **1500 W** |
| Voltage | AC 110–220 V, 50/60 Hz | 220 V/50 Hz listed; 110–220 elsewhere | 220V-50H / 110V-60hz |
| OS / net | Android; Wi-Fi / 4G | Android; Wi-Fi / 4G; SaaS IoT | same family |
| Clean | Steam + UV; PTC dry; 3 modes (normal / intermediate / advanced) | same; dual zoning | steam/UV, PTC, magnetic lock |
| Tanks | 5 L disinfectant; 450 ml perfume × 4 bottles, **3** fragrances on B01 copy | 5 L; 450 ml × 4; **4** fragrances | perfume + disinfect |
| Certs claimed | CE (some pages CE/FCC/ROHS) | CE / FCC (ROHS on listings) | CE, FCC, ROHS |
| Factory price | **none** | **none** (URL says factory-price) | n/a (this URL is a listing) |
| Listing USD | **$2,000**/pc | **$2,600**/pc | **$2,300**/pc |

Height in inches for the bay walk: B01 ≈ **77.4 in**; B02 ≈ **79.7 in**; Go Clean 72 in.

### 4.2 What “stacked dual” means on Haloo’s own copy

B02 product intro (`2026-09-21-haloo-hl-helmet-b02.md`):

> Number of doors: 2 warehouse doors. Number of perfumes: four perfume (two perfume for each warehouse).  
> Two compartments are equipped with two kinds of perfume, and have three cleaning modes.

XYJ dual FAQ: single clean “usually around **3–5 minutes**”; “dual station design can greatly improve overall processing efficiency.” Related-product title on that page: *Haloo smart dual compartment helmet cleaning vending machine*.

That is one cabinet, two independent chambers, not two machines and not a second Cebu site.

### 4.3 Process Haloo publishes (B02 EveryChina)

1. Place helmet, close door  
2. Dust removal and sterilization  
3. Atomized spray disinfection  
4. Steam mite removal: steam **70–80 °C** after heating disinfectant  
5. PTC dry / deodorize / hot air, **70–80 °C** (“similar to blowing hair”)  
6. Spray fragrance and antibacterial  
7. Remove helmet, close door  

B02 factory FAQ: PTC is a semiconductor heater; **highest temperature measured 75 °C**. Infrared stop if an arm or extra helmet enters the chamber.

Marketing collisions (do not pick a winner): “60 secs” on one EveryChina blurb vs 3–5 min vs 3–8 min vs “2-minute drying.”

### 4.4 SKU name collision

The same factory uses **HL-Helmet-B01 / B02** on haloo-vending.com and **HL-XYJ-L01-D02** on haloovendingmachine.com / ChinaX for both a 1966 mm customize-capacity listing **and** a 2025 mm 2-helmet listing. Treat B01 = single, B02/XYJ-2025mm = dual, and expect a quote to name the drawing.

## 5. Master price table (CNY, PHP, USD)

FX: BSP 21 Sep 2026. PHP rounded to whole pesos; CNY to 2 decimals.

### 5.1 China listings (USD printed → implied CNY → PHP → USD)

| Source | SKU | Listed USD | Implied CNY | PHP | USD via PHP |
|--------|-----|------------|-------------|-----|-------------|
| EveryChina + haloovendingmachine.com + ChinaX | Haloo B01, 1 helmet | 2,000.00 | 13,396.89 | 125,340 | 2,000.00 |
| haloovendingmachine.com | Haloo XYJ-L01-D02, 2 helmet | 2,300.00 | 15,406.43 | 144,141 | 2,300.00 |
| EveryChina + ChinaX | Haloo B02, 2 helmet | 2,600.00 | 17,415.96 | 162,942 | 2,600.00 |
| Made-in-China (1–9) | Haloo steam/UV, model field B02 | 1,799.00 | 12,050.51 | 112,743 | 1,799.00 |
| Made-in-China (10+) | same | 1,500.00 | 10,047.67 | 94,005 | 1,500.00 |
| Ouyuan MIC | “for Rental Shop” | 1,906.00 | 12,767.24 | 119,449 | 1,906.00 |
| Ouyuan MIC | same band high | 1,979.00 | 13,256.23 | 124,024 | 1,979.00 |
| Ouyuan MIC | UV energy-efficient low | 1,622.00 | 10,864.88 | 101,651 | 1,622.00 |
| Ouyuan MIC | UV energy-efficient high | 2,320.00 | 15,540.40 | 145,394 | 2,320.00 |
| Ouyuan MIC | restoration / steam band | 1,980.00–2,250.00 | 13,262.93–15,071.51 | 124,087–141,008 | 1,980.00–2,250.00 |
| Ouyuan MIC | helmet+shoes | 1,685.00–1,910.00 | 11,286.88–12,794.03 | 105,599–119,700 | 1,685.00–1,910.00 |

Alibaba `1601646947816` was ingested; extract is an **empty JS shell**. Search-result $1,688 / $1,588 / $1,455 is **not on disk**. Do not cite.

### 5.2 Philippine press and ads (PHP printed → CNY → USD)

| Source | What | Listed PHP | CNY | USD |
|--------|------|------------|-----|-----|
| Tribune 2025-10-03 | Go Clean unit, variant band | 44,000–55,000 | 4,702.91–5,878.64 | 702.09–877.61 |
| PEP 2025-10-16 | Go Clean unit | 45,000–55,000 | 4,809.80–5,878.64 | 718.05–877.61 |
| PEP 2025-10-16 | Go Clean All-in-One (helmet/jacket/bag/shoes) | 55,000 | 5,878.64 | 877.61 |
| FindGlocal 2024-10-15 | iCleaN'GO ad, NCR ship + 2 gallons + tarpaulin, 3-month warranty | 44,999 | 4,809.69 | 718.03 |
| GMA 2024-09-13 + BusinessDiary | Quick Fresh unit incl. solution + fragrance | 265,000 | 28,324.37 | 4,228.50 |
| Operator brief | local machine band | ~44,000–75,000+ | ~4,703–8,016 | ~702–1,197 |

### 5.3 Rider cycle prices (not machine cost)

| Source | Cycle | PHP | CNY | USD |
|--------|-------|-----|-----|-----|
| PEP / Go Clean interview | ₱25 | 25 | 2.67 | 0.40 |
| GMA / BusinessDiary Quick Fresh | ₱100 | 100 | 10.69 | 1.60 |
| Operator brief | ₱25–₱100 | 25–100 | 2.67–10.69 | 0.40–1.60 |
| Ouyuan marketing P&L | ¥15.00 service fee | 140.34 | 15.00 | 2.24 |

Ouyuan ¥15 is a **China-market sample P&L**, not a Cebu posted price. Detergent −¥0.50, VAT −¥2.50, opex −¥3.75, profit ¥8.25 **excluding electricity and rent**. Converted: detergent ₱4.68; “profit” ₱77.19. Manufacturer fiction until this site logs cycles.

## 6. Access: buy here vs ship from China

### 6.1 Buy in the Philippines (no Dongguan crate)

**Go Clean / GCVM Philippines** — `2026-09-21-goclean-philippines-home.md`

- Google Site: SEC-registered company (claim on the site; **SEC filing not on disk**).
- Specs: air dry via fogging; UVC “NM Blue 5”; fogger **900 W**; **72 × 18 × 20 in** (~1829 × 457 × 508 mm). **Single cabinet.** No stacked dual on this page. **No peso price on the homepage.**
- Contact: 09998038764; goclean.vendo@gmail.com; 606 Jade Garden, Honorio Lopez Blvd., Manila.
- Press: Tribune P44,000–P55,000 depending on variant; 30 technicians and “60 units per day” are **press claims**. PEP: PHP45,000–PHP55,000; rider PHP25; inventor Harold Denn Burgos; All-in-One PHP55,000; export “still on the table” for customs.

**iCleaN'GO** — FindGlocal directory, Fourth Estate, Parañaque, 15/10/2024. PHP44,999; free NCR shipping; tarpaulin; 2 gallons; 3-month warranty; tel +639566714523. **Ad, not invoice.** Relationship to Go Clean unknown.

**Quick Fresh** — GMA 13 Sep 2024, Joyce Malasa. Five steps: fog, UV, ozone, high-heat dry, fragrance. ~8 minutes. **P265,000** including solution and fragrance. Rider **P100**. Machines “from abroad”; 10 units described as a million-peso investment. BusinessDiary same ₱265,000 with **20 liters** solution; 520 seconds; ₱100 or two ₱50 bills; claimed 10 users/day and ₱30,000/month — **owner arithmetic, not this corridor.**

**Shield-Pro** Facebook promo bands were **not ingested**. Unsourced here.

Warranty contrast: local ads **3 months** (iCleaN'GO) vs Haloo listing **1 year** (video/online only, no PH tech).

### 6.2 Ship from China / Taiwan

| Path | What arrives | Time on disk | Money on disk | Still missing |
|------|--------------|--------------|---------------|---------------|
| Haloo B01 | Single steam/UV Android kiosk, ~1.97 m, 160–180 kg | 35 days factory + crate | $2,000 listing ≈ ₱125,340 FX | Ocean/air, insurance, duty, VAT, Cebu truck, 60 Hz / payment localization |
| Haloo B02 / XYJ dual | Stacked two-chamber, ~2.03 m, 160–200 kg | 35 days | $1,799–$2,600 ≈ ₱112,743–₱162,942 FX | same; **bay height** |
| Ouyuan dual | A/B, 1.79 m, 115 kg | 15–25 day build + 30–50 day “transport to local area” | $1,906–$1,979 listing ≈ ₱119,449–₱124,024 | same; WhatsApp +86 13570855813 on product page |
| FresHelmet A026 | Taiwan upper/lower independent | “ship internationally, no minimum” | **no machine price** | TWD/USD quote; LIFIKEYS, New Taipei, +886222649010 |

Made-in-China Haloo page: **“Shipping Cost: Contact the supplier about freight and estimated delivery time.”** Aggregator freight $300–$800 was **not** copied into this report.

Incoterm is never printed as FOB/CIF on these extracts. Do not assume Cebu delivery.

PH 220 V 60 Hz vs many China pages 220 V **50 Hz**. Listings also say 110–220 / 50/60. A PI must name the transformer.

### 6.3 Import vs local, FX-only (not landed)

| | Local Go Clean press mid (₱50,000) | Haloo B01 $2,000 | Haloo B02 $2,600 | Quick Fresh ₱265,000 |
|--|-------------------------------------|------------------|------------------|----------------------|
| PHP | 50,000 | 125,340 | 162,942 | 265,000 |
| CNY | 5,344.22 | 13,396.89 | 17,415.96 | 28,324.37 |
| USD | 797.83 | 2,000.00 | 2,600.00 | 4,228.50 |
| Dual chambers | no | no | yes | no |
| Local tech | press says yes | video/online | video/online | PH distributor (press) |

Even the cheapest Haloo dual listing ($1,799 → ₱112,743) is about **2.0–2.6×** the Go Clean press band **before** freight. Quick Fresh press is about **2.1×** a $2,000 Haloo listing at BSP — so an imported branded kiosk already sitting in PH can cost more than buying Haloo yourself, or less, depending on freight. Unknown until a PI exists.

## 7. Other dual-chamber makers (the Haloo comparables)

### 7.1 FresHelmet / LIFIKEYS (Taiwan)

`2026-09-21-freshelmet-ihelmetspa.md`

- Model **A026**, dual slots, **upper and lower layers**, each with its own start; one mainboard, one payment module, separate payments per deck. This is the same physical idea as Haloo B02.
- Cycle **8 minutes**: waterless fog, UVC, hot air, floral scent. Bluetooth-headset-safe claim. NAYAX / QR; SEA mobile-pay list **includes Philippines**.
- Patents listed (Taiwan, China, US, Japan). Gogoro 12-store case in Taiwan. Distributors wanted.
- **No TWD, USD, PHP, or CNY machine price on the homepage.** A YouTube comment “₱100k” is not a listing.

### 7.2 Ouyuan (Dongguan)

`2026-09-21-ouyuan-dual-oytk2501-2.md`, `2026-09-21-ouyuan-made-in-china-home.md`

- Product line: OYTK2501-1 single, **OYTK2501-2 dual**, OYTK2507-2 4th gen.
- Dual: 650 × **1790** × 550 mm, **115 kg**, 15.6 in, UV+ozone, 1100/2100 W (40 W standby), QR/NFC/bill/coin, languages include EN (not Filipino on the list).
- Shorter and lighter than Haloo B02 — easier eaves.
- Product page: “Get Latest Price”; no cabinet USD/CNY. MIC home fills the USD bands in §5.1. Year of establishment on MIC: 2018-05-31 (site copy also says founded 2013).
- Launch steps: inventory 15–25 days; QR account 3 days; debug; transport 30–50 days.

### 7.3 BLEE

Title matches the rental phrase. Extract has no machine USD/CNY/PHP. Not a priced candidate.

## 8. Spec and claim conflicts (do not flatten)

| Topic | Values on disk |
|-------|----------------|
| Haloo dual height | 2025 mm factory / listing; 1860 mm on one MIC table |
| Haloo dual weight | 160 / 200 kg |
| Haloo dual power | 1500 W (XYJ) / 2100 W (B02) / 900 W steam generator on UV page |
| Haloo cycle time | 60 s blurb / 3–5 min FAQ / 3–8 min video index / 2 min dry claim |
| Haloo PTC temp | 75 °C measured / 70–80 °C process copy |
| Go Clean price | homepage none; Tribune ₱44–55k; PEP ₱45–55k |
| Dual in PH | Go Clean site: single only. Dual = import (Haloo/Ouyuan) or FresHelmet Taiwan |
| FDA | operator-brief / Facebook ads; **no FDA notice in library** |

## 9. What this means for the Cebu IT Park / JY Square one-machine test

Lean file still says one machine, counted cycles, no second unit to “feel busy.”

| Need | Path these files support |
|------|--------------------------|
| Plug in this quarter, peso invoice, local parts | Walk a Go Clean / iCleaN'GO-class unit. Ask for **written** price, Cebu delivery, warranty, solution liters per ₱. Press band ₱44k–₱55k. |
| Two riders at once, one footprint | Haloo B02/XYJ, Ouyuan 2501-2, or FresHelmet A026. Import. FX-only ₱113k–₱163k **plus unknown freight**. Measure bay to **2.05 m**. |
| Same factory as the Haloo video | Email yhq@gd-haloo.com / wm@gd-haloo.com. Ask for PI in **CNY and USD**, Incoterm, 220 V **60 Hz**, Maya/GCash or Nayax, spare pumps, solution MSDS. |
| Do not do | Treat $2,000 FOB as comparable to ₱45,000 delivered. Buy dual to skip the one-machine test. Sell “FDA-certified” with no file. |

Licenses for the operator (already on disk, not restated as new law): DTI BNRS + Cebu LGU + BIR for a Filipino sole prop. Importing a capital kiosk is not the same as RA 11595 foreign retail. Still need a broker quote for duties — **not invented here**.

## 10. What we could not document

- Any invoice, PI, or CIF/C&F Manila or Cebu.
- Any Haloo **yuan** list (1688/Taobao not fetched).
- Alibaba live price (JS shell).
- Shield-Pro or FresHelmet PH agent pesos.
- Freight, insurance, customs duty, VAT, brokerage, last-mile Cebu.
- Go Clean SEC primary filing (SEC portal blocked).
- FDA notification numbers.
- Electrical peso cost (no kWh tariff on disk).
- A unit already sitting in JY Square / IT Park (walk required).

## 11. Source appendix (on disk 2026-09-21 unless noted)

| Card | Role |
|------|------|
| `research/library/2026-09-21-bsp-rerb-xlsx.md` | FX used in every table |
| `research/library/2026-09-21-bsp-sdds-exchange-rates.md` | PHP per USD 62.670 |
| `research/library/2026-09-21-boc-exchange-rate.md` | China board CNY |
| `research/library/2026-09-21-chinabank-forex.md` | PH bank USD/CNY 18 Sep |
| `research/library/2026-09-21-haloo-youtube-oembed-sc_4dHcXYG0.md` | Video title / channel |
| `research/library/2026-09-21-haloo-hl-helmet-b01.md` | B01 factory spec |
| `research/library/2026-09-21-haloo-hl-helmet-b02.md` | B02 factory spec, stacked doors |
| `research/library/2026-09-21-haloo-everychina-b01-2000.md` | $2,000 listing |
| `research/library/2026-09-21-haloo-everychina-b02-2600.md` | $2,600 listing + process |
| `research/library/2026-09-21-haloo-self-service-xyj-l01-d02.md` | $2,300 dual listing |
| `research/library/2026-09-21-haloo-made-in-china-b02-1799.md` | $1,799 / $1,500 band |
| `research/library/2026-09-21-haloo-chinax-catalog.md` | $2000 / $2300 / $2600 catalog |
| `research/library/2026-09-21-goclean-philippines-home.md` | Local specs + Manila contact |
| `research/library/2026-09-21-tribune-goclean-2025-10-03.md` | ₱44k–₱55k |
| `research/library/2026-09-21-pep-goclean-2025-10-16.md` | ₱45k–₱55k, ₱25/cycle |
| `research/library/2026-09-21-gma-quickfresh-2024-09-13.md` | ₱265k, ₱100/cycle |
| `research/library/2026-09-21-businessdiary-helmet-vendo-265k.md` | same ₱265k bundle |
| `research/library/2026-09-21-icleango-paranaque-listing.md` | ₱44,999 ad |
| `research/library/2026-09-21-freshelmet-ihelmetspa.md` | A026 stacked dual, no price |
| `research/library/2026-09-21-ouyuan-dual-oytk2501-2.md` | dual spec + RMB P&L |
| `research/library/2026-09-21-ouyuan-made-in-china-home.md` | Ouyuan USD bands |
| `research/library/2026-09-21-blee-helmet-rental-guide.md` | rental-title page, no price |
| `research/library/2026-09-20-helmet-vendo-operator-brief.md` | ₱44k–₱75k+ notes |

Also ingested, limited use: Haloo steam B01 page, Haloo UV B02 page, Haloo industrial B01 $2000, BSP HTML hub (no numbers), BSP cross-rate workbooks (history), Alibaba JS shell.

## 12. Next documents worth ingesting

1. Written peso quote (Go Clean / iCleaN'GO / Quick Fresh) with Cebu delivery.  
2. Haloo or Ouyuan PI: CNY **and** USD, Incoterm, 60 Hz, payment kit, crate kg, port.  
3. Freight quote to Cebu or Manila.  
4. Bay height/power photos.  
5. Browser re-fetch of Alibaba if the $1,688 ladder must be cited.  
6. 1688/Taobao if a true **yuan** list is required.

Until (1) or (2) exists, unit economics stay unknown. The MVP is still: walk three bays, get a placement yes, then buy one cabinet.

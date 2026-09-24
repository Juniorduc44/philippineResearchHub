# Helmet sanitizing vendo — Cebu IT Park / JY Square

**Status:** draft, not live. One-machine test, not a chain.  
**Catalog:** [`directory/ideas/helmet-vending/idea.md`](../../directory/ideas/helmet-vending/idea.md)  
**Who this is for:** you, a partner, or a stranger who finds this folder and wants to know whether to pick it up.

If you only read one file in this project, read this one. The rest of the folder is the operating system for running the test.

---

## The idea

A self-service kiosk (a “vendo”) that cleans, sanitizes, deodorizes, and dries a motorcycle or bicycle helmet in a few minutes. The rider opens a chamber, pays, waits, takes the helmet back.

This build is pinned to **one corridor**: Cebu IT Park (Asiatown) and JY Square / JY Mall on Salinas Drive, Lahug. Not “the Philippines.” Not Manila.

The product is **convenience at a stop they already make** (parking, gas, convenience, laundry, delivery wait) — not a detailing shop that pulls pads out.

---

## Why it might be a quality opportunity

Quality here means: a real, repeating local pain, a small first bet, and a site where people already dwell. It does **not** mean a proven ₱30,000/month machine. Those figures in the operator notes are uninvoiced.

**Pain is ordinary, not trendy.** Cebu humidity plus all-day helmets (commute, BPO night shift, delivery) makes odor and sweat a weekly problem. Manual shop detailing exists; it is slower and closed at 2 a.m.

**The first bet can stay small.** Operator notes put local machines around ₱44,000–₱75,000+ (no quote on disk). Footprint is about 1 m². You are testing one bay, not a factory.

**The corridor has the right kind of traffic.** IT Park is a 24/7 BPO/tech hub; JY Square is the adjacent mall/gateway. Motorcycles are how people get in. Delivery riders already serve the food strip. That is a hypothesis about *density and dwell*, not a counted bike census — counts are still an open task.

**It can be cloned if it works.** The folder is built as an E-Myth prototype: manuals, positions, and a 30-day log so a second unit is a copy, not a new hobby. Lean Startup (local book text): one real transaction test, like their laundry-van experiment, before a fleet.

**It is not a quality opportunity if** the only evidence is a manufacturer story, the bay is quiet, another vendo already sits in the same parking, or the founder has to live next to the box.

Treat every peso and cycle number below as **operator-brief** until a quote, permit, or log file exists in `research/library/` or `lean/learning-log.md`.

---

## Pros and cons

### For

- Hygiene problem matches climate and two-wheeler use, not a luxury spa story.
- Unattended once placed — refill, wipe, collect. Compact.
- Fast cycle (notes: ~3–10 minutes) → throughput if the line exists.
- Repeat use is plausible for delivery riders and daily commuters.
- Night-shift BPO hours are a gap shops do not cover.
- Local machine options (Go Clean press ₱44k–₱55k) vs China listings (Haloo single ~US$2,000 / stacked dual ~US$2,300–$2,600). See `philippines/machine-candidates.md`. Not invoices.
- Rain/heat are both a risk and a demand driver.

### Against

- **Location is the business.** A dead bay kills the math. Estate rent or revenue share can erase a thin margin.
- Capital is real even if “small”: machine, cover, power, site deposit, solution, downtime.
- Vandalism, brownouts, typhoon, outdoor heat.
- Fog/UV/scent is not the same as pad-out detailing. Some riders will not believe it. Do not overclaim “FDA-certified” — no notice is on disk.
- Category is getting crowded in popular PH spots (notes only; walk this corridor before buying).
- Hand-detail shops already in Cebu: compete on minutes and hours, not on “deeper clean.”
- Manufacturer payback math (e.g. ~10 cycles/day at ₱100 → “₱30,000+/month”) is arithmetic, not this site.

---

## How practical is it?

| If you are… | Practical? |
|-------------|------------|
| A Philippine national, sole prop, local money, willing to walk three bays and run **one** machine for 30 days | This is the intended path. Registration map is DTI BNRS + Cebu City mayor’s permit + BIR ([licenses](philippines/licenses.md)). |
| Hoping for fully passive income in week one | No. Week one is Technician: refill, photo, tally. Manuals exist so that does not stay forever. |
| A foreign investor | Read [EO 113](../../research/library/2026-09-20-eo-113.md) and [RA 11647](../../research/library/2026-09-20-ra-11647.md) first. Small domestic-market firms under US$200,000 paid-in are generally reserved to Philippine nationals. [RA 11595](../../research/library/2026-09-20-ra-11595.md) (₱25M foreign-retailer floor) applies **if** this is classified as retail of goods — a service kiosk is not automatically that. |
| Wanting a nationwide brand before one logbook | Wrong project. Pivot or leave it. |

**Honest outlook from the operator notes, not a forecast:** a well-sited machine near parking, gas, or convenience on this corridor *could* do respectable volume, especially with delivery and shift workers. Expect quieter numbers than brochure payback until the bay is proven. Start with one unit.

---

## What you actually need (to take it up)

Do these in order. Do not buy a second machine first.

1. **Walk three bays** (day *and* a BPO night window). Fill [philippines/location-cebu-it-park.md](philippines/location-cebu-it-park.md). Count bikes that already stop. If another vendo is there, this is a relocation problem.
2. **Written placement yes** — rent vs share vs “leave it.” Photo of empty bay + power. Gate in [emyth/systems/placement.md](emyth/systems/placement.md).
3. **Register** — DTI business name (BNRS) if sole prop; Cebu City mayor’s permit; BIR TIN. Fees still `unknown` on disk. [philippines/licenses.md](philippines/licenses.md).
4. **One dated machine quote** in PHP (single chamber, warranty, lead time). Notes say ~₱44k–₱75k+ local; that is not an invoice.
5. **Open the money envelopes** before the first cycle: INCOME, PROFIT, OWNER’S COMP, TAX, OPEX + two vaults. Start 1% to PROFIT. [profit-first/](profit-first/).
6. **Run 30 days.** Log cycles and downtime in [lean/learning-log.md](lean/learning-log.md). Then pivot (move/kill) or persevere (clone).

Still missing on disk: Cebu kiosk-permit PDF, FDA solution notice, machine invoice, bike counts.

---

## Folder layout (idea → build)

```
projects/helmet-vending/
  README.md                 ← you are here (handoff)
  CONTEXT.md                ← rules for AIs working this folder
  INDEX.md                  ← file list
  brief.md                  ← one-page aim
  sources.md                ← what was actually read
  lean/                     ← test: hypotheses, MVP, metrics, log
  emyth/                    ← systems: aim, org chart, manuals
  profit-first/             ← cash envelopes
  philippines/              ← licenses, Cebu site, PHP math, competition
```

Hub map: catalog idea in `directory/ideas/helmet-vending/`; sources in `research/library/`; this folder is the build.

---

## How to take it up

1. Read this README and `brief.md`.
2. Read `philippines/licenses.md` and `lean/mvp-experiment.md`.
3. Do the bay walk. Write numbers into `philippines/location-cebu-it-park.md`.
4. If the walk is dead, stop. The idea can wait for another corridor.
5. If the walk is alive, follow the sequence in `lean/mvp-experiment.md` and keep Profit First accounts from day zero.

Do not invent traffic, fees, or FDA status. If a fact is not in `research/library/` or this folder, it is `unknown`.

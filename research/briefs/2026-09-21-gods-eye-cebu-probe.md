# Brief: God's Eye View local probe (Cebu)

- Date: 2026-09-21
- Status: live snapshot (not an invoice, not a government file)
- Tool: `godseye` → http://127.0.0.1:4173/
- Notes: `tools/gods-eye.md`

## What we ran
Local God's Eye View (bilawalsidhu/gods-eye-view v0.1.1), keyless, Node 24.14, Vite on 127.0.0.1:4173. Probed the same APIs the globe uses.

## Place (Photon / Nominatim via `/api/geocode`)

| Query | Result |
|-------|--------|
| Cebu City Philippines | 10.2934946, 123.9018183 — “Cebu City, Central Visayas, Philippines” |
| Cebu IT Park | **10.3307983, 123.9068258** — “Cebu I.T. Park, Apas, Cebu City, Central Visayas, 6000, Philippines” |

Use the IT Park pair as a fly-to for the helmet-vending corridor. Still walk bays; this is a geocoder, not a lease.

## Weather (Open-Meteo via `/api/weather-effects`)

Point 10.3157, 123.8854 at 2026-09-21T04:00Z:

- 30.9 °C (feels 38 °C)
- 78% cloud, 0 mm precip, wind 7.4 kph from 187°, visibility 23.3 km

Rain/heat hypotheses in the helmet brief stay hypotheses until a week of logs.

## Regional brief (`/api/regional-brief`)

Place: Cebu City, Central Visayas, PH. News source: Google News RSS (personal/noncommercial terms). Headlines in the payload included local Cebu parking-fine and housing-project items. Treat as locality-matched RSS, not verified incidents.

## Flights (`/api/opensky`, anon)

6,252 states in the snapshot. Rough boxes (not airport official counts):

- Near Cebu (~10.3N 123.9E ±3.5°): 7 contacts, including CEB791, CEB853, GAP2815, GAP2143 (origin country Philippines)
- Near Manila (~14.6N 121.0E ±2.5°): 33 contacts (MAS, SIA, CSN, CEB/GAP mixed)

OpenSky license is **non-commercial**. Do not build a paid product on this feed without their written terms.

## Other keyless layers

- CelesTrak `/api/celestrak/stations`: ISS and station TLEs served.
- Launch Library 2 `/api/launches`: 29 recent launches.
- USGS all-day (what the earthquakes layer fetches): 219 events; **none in the PH box (4–21.5N, 116–127E) at probe time**.
- CCTV `/api/cctv/sources`: 3,184 cameras; **zero PH** in this catalog (US/EU/AU/CA packs).

## Needs a key (status endpoints)

- NASA FIRMS fires: `hasKey: false`
- TomTom live traffic: `hasKey: false`
- AIS vessels: not probed as a live stream; free AISStream key is BYOK

## Implication
`godseye` is usable now for Cebu fly-to, weather, and a live aircraft overlay. It does not give motorcycle counts, bay owners, or LGU permits. Cite this brief as a dated probe, then ingest any number you need to keep.

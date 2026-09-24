# God's Eye View (local)

Upstream: https://github.com/bilawalsidhu/gods-eye-view  
Clone (gitignored): `tools/gods-eye-view/`  
Vendored Node 24 (gitignored): `tools/.node/`

A Cesium 3D globe with live public layers (flights, satellites, earthquakes, weather, news, optional ships/fires/traffic). **People are not a query type** in this project — no named-person search or face recognition.

## Run

From the hub root:

```bash
godseye
```

**Verified interface (this workspace):** [http://localhost:8080/proxy/4173/](http://localhost:8080/proxy/4173/)

That is the code-server Simple Browser / Ports URL. `http://127.0.0.1:4173/` is only inside the container and is **not** what you open on your laptop.

Confirmed 2026-09-21 after fixing asset paths and iframe headers: `GET /` → 302 `/proxy/4173/`; HUD loads (God's Eye View, DATA LAYERS, LOCATION, canvas). Imagery can stay blurry for a few seconds on Esri tiles.

```bash
godseye --bg       # background
godseye --status
godseye --stop
```

Foreground: Ctrl+C. Optional keys: in-app **POWER UP** panel, or `tools/gods-eye-view/.env` (gitignored).

## How to open it

1. `godseye` (already running if `godseye --status` prints the Interface line).
2. In VS Code / code-server: **Ports** → **4173** → globe / Open in Browser.
3. Or paste **http://localhost:8080/proxy/4173/** into Simple Browser (new tab, not a broken iframe from the old DENY header).

First screen may be the mission picker (Live Contacts / Space / Environmental / Explore manually). Pick **Explore manually** to just look around. Use **LOCATION** to search (e.g. Cebu IT Park).

I cannot share one mouse with you on this host. I can drive a headless copy and screenshot; you use the URL above for the real GUI.

## What we verified (2026-09-21, keyless)

| Layer | Endpoint | Result |
|-------|----------|--------|
| App shell | `GET /` | 200, title God's Eye View |
| Place search | `/api/geocode?q=Cebu City Philippines` | Cebu City 10.2935, 123.9018 |
| Place search | `/api/geocode?q=Cebu IT Park` | **10.3308, 123.9068** (Apas, Cebu City 6000) |
| Weather | `/api/weather-effects?latitude=10.3157&longitude=123.8854` | 30.9 °C, feels 38 °C, 78% cloud, 0 mm rain (Open-Meteo) |
| Regional brief | `/api/regional-brief?...` | place PH / Cebu City; Google News RSS headlines |
| Flights | `/api/opensky` | 6,252 aircraft; 7 near Cebu box; 33 near Manila (CEB/GAP callsigns) |
| Satellites | `/api/celestrak/stations` | TLE set including ISS / CSS |
| Launches | `/api/launches` | 29 Launch Library 2 rows |
| Earthquakes | USGS all-day GeoJSON (client-side in the app) | 219 global; **0 in PH box that hour** |
| CCTV | `/api/cctv/sources` | 3,184 cameras; **none in PH** (Austin, TfL, Caltrans, …) |
| FIRMS fires | `/api/firms/status` | `hasKey: false` |
| TomTom traffic | `/api/tomtom/status` | `hasKey: false` |

## Use for hub projects

- **Helmet vending (Cebu IT Park / JY Square):** fly the globe to 10.3308, 123.9068; count live aircraft as a weak proxy for air-side traffic only (not motorcycle counts). Weather/news for rain and local context. Does **not** replace a foot survey of bays.
- **Community cold storage:** FIRMS (needs NASA key) for fire/heat context; USGS quakes for site risk; weather for produce handling. Still need an LGU.
- **Future PH ideas:** ships (AISStream key), traffic (TomTom key), photorealistic 3D (Cesium ion or Google Maps key). CCTV packs are foreign cities unless we add a PH source.

## License / commercial caveats (upstream DATA_SOURCES.md)

- **OpenSky** flight feed: non-commercial research/education. Contact OpenSky for commercial use.
- **TeleGeography** submarine cables: CC BY-NC-SA — delete that folder for commercial use.
- **Google News RSS** in the Cebu brief: personal/noncommercial terms. GDELT is the fallback.
- Live tiles/feeds stay at their providers; do not archive Google tiles.

## Hub rule

This is a **live viewer**, not a source of truth. If a fact must be cited in `/directory` or `/projects`, ingest a dated snapshot into `research/inbox/` the same way as any other URL.

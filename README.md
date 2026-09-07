# RoadRescue 24/7 — UK Emergency Car Services Website

A modern, fully responsive 5-page website for a 24/7 UK emergency automotive
service: mobile mechanics, car key making, lockout rescue, diagnostics,
recovery and more — with a live "nearest mechanic" finder and WhatsApp
dispatch built in.

## Pages

| Page | File | Highlights |
|---|---|---|
| Home | `index.html` | Hero, live status ticker, **nearest-mechanic map finder**, 8 services, how-it-works, **price estimator**, stats, testimonials |
| About | `about.html` | Story, values, milestone timeline, accreditations, partner recruitment, team |
| Services | `services.html` | 8 detailed service blocks, transparent pricing tiers, added-value extras, FAQ accordion |
| News | `news.html` | Live alert strips, filterable announcement grid, motorway safety timeline, alert signup |
| Contact | `contact.html` | Validated callout form with WhatsApp handoff, direct contacts, UK coverage list, quick FAQs |

## Key features

- **Nearest mechanic finder** (`index.html#finder`) — Leaflet dark map + 22 UK
  partner locations. Search by **town or postcode** (full A–Z UK postcode-area
  lookup table), filter by service, or use **GPS geolocation**. Results are
  distance-sorted (haversine) with live ETA, rating, tags, and per-partner
  call / WhatsApp buttons synced to map pins.
- **WhatsApp everywhere** — floating SOS dock with a quick-issue picker that
  pre-fills the message, plus contextual WhatsApp links on every service,
  quote and form (forms also generate a WhatsApp handoff of their contents).
- **Instant price estimator** — service × time-of-day loading (night +35%,
  weekend +15%) × mileage, with a live total and one-tap booking.
- **UK-only focus** — GB English copy, £ pricing, UK postcodes, 999 guidance,
  motorway safety advice, all 124 postcode areas referenced.
- **24/7 signalling** — pulsing live-status topbar, "open now" pills,
  night-rate transparency, bank-holiday cover notice.
- Scroll-reveal animations, animated counters, cursor spotlight cards,
  scroll progress bar, accordions, news filtering, sticky shrinking nav,
  mobile drawer, client-side form validation, `prefers-reduced-motion` support.

## Design system

Dark "midnight navy" base with **signal amber** (`#ffb020`) as the emergency
accent and **rescue teal** (`#2ee6c5`) for live/status cues — a professional
palette borrowed from breakdown-recovery light bars rather than typical
red/blue garage sites. Typography pairs *Sora* (display) with
*Plus Jakarta Sans* (body). Glassmorphic cards, ambient radial glows and
generous radii keep it modern without being generic.

## Tech

Pure static HTML/CSS/JS — no framework, no build dependencies to deploy.
Only external runtime libraries are Google Fonts and
[Leaflet](https://leafletjs.com/) (map) with CARTO dark tiles.

```
assets/css/style.css   design system + all components
assets/js/data.js      UK partner network, place & postcode-area coordinates
assets/js/main.js      nav, reveal, counters, finder, estimator, forms, SOS
assets/img/            generated imagery
build/                 Python generator for the shared header/footer chrome
reference/             the original sample template supplied for inspiration
```

## Run locally

```bash
python3 -m http.server 3000     # then open http://localhost:3000
```

## Regenerate the pages

Header, footer, nav, SOS panel and floating dock are shared. Edit
`build/layout.py` or the `build/pages_*.py` bodies, then:

```bash
python3 build/build.py
```

## Going to production

Replace the demo values before launch:

- `WHATSAPP` and `PHONE` constants at the top of `assets/js/main.js`
- The partner list in `assets/js/data.js` (swap for your live dispatch API)
- Form submission — currently client-side only; point it at your backend,
  Formspree or similar
- For precise postcode → coordinates, swap the lookup table for the free
  [postcodes.io](https://postcodes.io) API

#!/usr/bin/env python3
"""Renders the RoadRescue 24/7 static site into the repository root."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)

from layout import page
import pages_home, pages_about, pages_services, pages_news, pages_contact

PAGES = [
    ("index.html", "index", "RoadRescue 24/7 — Emergency Mobile Mechanic, Car Keys & Recovery Across the UK",
     "Find the nearest emergency mobile mechanic, auto locksmith or recovery unit anywhere in the UK. 24/7 callout, fixed prices, no membership. Call or WhatsApp now.",
     pages_home.BODY, "index.html"),
    ("about.html", "about", "About Us — RoadRescue 24/7 UK Emergency Auto Services",
     "480+ vetted UK engineers, a Birmingham control room that never closes and a fixed-price promise. Meet the team behind RoadRescue 24/7.",
     pages_about.BODY, "about.html"),
    ("services.html", "services", "Services & Pricing — Mobile Mechanic, Car Key Making, Recovery | RoadRescue 24/7",
     "Emergency mobile mechanic, car key making and programming, lockout rescue, battery, tyres, diagnostics, wrong fuel drain and UK-wide recovery. Fixed prices, 24/7.",
     pages_services.BODY, "services.html"),
    ("news.html", "news", "News & Announcements — Service Updates and UK Road Alerts | RoadRescue 24/7",
     "Live service updates, UK weather and roadworks alerts, coverage expansions and practical driver advice from the RoadRescue 24/7 control room.",
     pages_news.BODY, "news.html"),
    ("contact.html", "contact", "Contact & 24/7 Callout — RoadRescue 24/7",
     "Call, WhatsApp or book a callout online. UK control room open 24 hours a day, 365 days a year, covering all 124 UK postcode areas.",
     pages_contact.BODY, "contact.html"),
]

for filename, key, title, desc, body, active in PAGES:
    html = page(key, title, desc, body, active)
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("built", filename, len(html), "bytes")

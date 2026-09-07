"""Shared chrome for RoadRescue 24/7 static pages."""

ICONS = {
    "wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 8.8-8.8"/><path d="m17 5 2.5 2.5"/><path d="m14.5 7.5 2.5 2.5"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.4 1.9.6 2.9.8a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="3"/><path d="m2 7 10 6 10-6"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1s-.5-.1-.7.2-.8 1-.9 1.1-.4.2-.7 0a8.2 8.2 0 0 1-2.4-1.5 9 9 0 0 1-1.7-2.1c-.2-.3 0-.5.1-.6l.5-.6.3-.5v-.5l-.9-2.2c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4A3.6 3.6 0 0 0 5.8 9c0 1.6 1.1 3.1 1.3 3.3a12.4 12.4 0 0 0 4.8 4.2c2.4 1 2.4.6 2.8.6a3.2 3.2 0 0 0 2.2-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>',
    "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17h14M3 13l1.6-4.6A3 3 0 0 1 7.4 6h9.2a3 3 0 0 1 2.8 2.4L21 13v4a1 1 0 0 1-1 1h-1a1 1 0 0 1-1-1v-1H6v1a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><circle cx="7.5" cy="13.5" r="1"/><circle cx="16.5" cy="13.5" r="1"/></svg>',
    "battery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2"/><path d="m10 9-2 3h3l-2 3"/></svg>',
    "tyre": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.2"/><path d="M12 3v5.8M12 15.2V21M3 12h5.8M15.2 12H21"/></svg>',
    "fuel": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V5a2 2 0 0 1 2-2h5a2 2 0 0 1 2 2v15"/><path d="M3 20h11"/><path d="M13 9h3a2 2 0 0 1 2 2v6a1.5 1.5 0 0 0 3 0V9l-2.5-2.5"/><path d="M6 8h5"/></svg>',
    "tow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17h11v-5H3z"/><path d="M14 15h3l4-4V8l-6 4"/><circle cx="6.5" cy="18.5" r="1.6"/><circle cx="17" cy="18.5" r="1.6"/></svg>',
    "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8.5 12.2 2.4 2.4 4.6-4.8"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M6 11l6-6 6 6"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m12 2 3 6.6 7.2.8-5.4 4.9 1.5 7.1L12 17.8 5.7 21.4l1.5-7.1L1.8 9.4 9 8.6z"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M16 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 20v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 4 13c0-6 7-10 16-10 0 9-4 16-9 17z"/><path d="M4 21c2-6 6-9 10-11"/></svg>',
}

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("news.html", "News"),
    ("contact.html", "Contact"),
]


def head(title, desc, page):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#070b16">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='24' fill='%23ffb020'/><text y='72' x='50' text-anchor='middle' font-size='62' font-family='sans-serif' font-weight='bold' fill='%231a1204'>R</text></svg>">
<link rel="stylesheet" href="assets/css/style.css">
{'<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">' if page == 'index' else ''}
</head>
<body>
<div class="progress"></div>
"""


def header(active):
    links = "".join(
        f'<a href="{h}" class="{"active" if h == active else ""}">{t}</a>' for h, t in NAV_ITEMS
    )
    return f"""
<div class="topbar">
  <div class="wrap">
    <div class="topbar-left"><span class="dot"></span><strong style="color:var(--teal)">24/7 LIVE</strong><span class="tb-hide">&nbsp;— dispatchers online across the UK right now</span></div>
    <div class="topbar-right">
      <a class="tb-hide" href="#" data-tel>📞 <span data-phone-text></span></a>
      <a href="#" data-wa="Hi RoadRescue 24/7, I need urgent roadside help." target="_blank" rel="noopener">WhatsApp us</a>
      <span class="tb-hide">Avg. arrival 27 min</span>
    </div>
  </div>
</div>

<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html">
      <span class="logo-mark">{ICONS['wrench']}</span>
      <span>RoadRescue<span class="amber">24/7</span><small>UK Emergency Auto</small></span>
    </a>
    <nav class="menu">{links}</nav>
    <div class="nav-cta">
      <a class="btn btn-ghost btn-sm" href="#" data-tel>{ICONS['phone']}<span data-phone-text></span></a>
      <a class="btn btn-primary btn-sm" href="index.html#finder">Find a mechanic</a>
      <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<div class="mobile-menu">
  {"".join(f'<a href="{h}" class="{"active" if h == active else ""}">{t}</a>' for h, t in NAV_ITEMS)}
  <a class="btn btn-primary btn-block" href="index.html#finder">Find nearest mechanic</a>
  <a class="btn btn-wa btn-block" style="margin-top:.6rem" href="#" data-wa="Emergency! I need a mechanic now." target="_blank" rel="noopener">WhatsApp SOS</a>
</div>
"""


def footer(page):
    leaflet = (
        '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>'
        if page == "index"
        else ""
    )
    return f"""
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html">
          <span class="logo-mark">{ICONS['wrench']}</span>
          <span>RoadRescue<span class="amber">24/7</span><small>UK Emergency Auto</small></span>
        </a>
        <p style="margin-top:1.1rem;max-width:34ch">Nationwide emergency mobile mechanics, auto locksmiths and recovery — dispatched to you anywhere in the UK, every hour of every day.</p>
        <div class="socials">
          <a href="#" data-wa="Hello RoadRescue 24/7" target="_blank" rel="noopener" aria-label="WhatsApp">{ICONS['wa']}</a>
          <a href="#" aria-label="Call" data-tel>{ICONS['phone']}</a>
          <a href="contact.html" aria-label="Email">{ICONS['mail']}</a>
          <a href="index.html#finder" aria-label="Find us">{ICONS['pin']}</a>
        </div>
      </div>
      <div>
        <h5>Company</h5>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="news.html">News &amp; announcements</a></li>
          <li><a href="contact.html">Contact &amp; callout</a></li>
          <li><a href="about.html#careers">Join our network</a></li>
          <li><a href="services.html#faq">FAQs</a></li>
        </ul>
      </div>
      <div>
        <h5>Services</h5>
        <ul>
          <li><a href="services.html#mechanic">Mobile mechanic</a></li>
          <li><a href="services.html#keys">Car key making</a></li>
          <li><a href="services.html#lockout">Lockout &amp; unlocking</a></li>
          <li><a href="services.html#battery">Battery &amp; jump start</a></li>
          <li><a href="services.html#recovery">Recovery &amp; towing</a></li>
        </ul>
      </div>
      <div>
        <h5>24/7 Control Room</h5>
        <p style="margin-bottom:.5rem"><a href="#" data-tel><strong class="amber" data-phone-text></strong></a><br>help@roadrescue247.co.uk<br>Unit 12, Orbital Park, Birmingham B6 7AA</p>
        <h5 style="margin-top:1.4rem">Breakdown alerts</h5>
        <form class="newsletter" data-validate>
          <input type="email" name="email" placeholder="you@email.co.uk" required aria-label="Email">
          <button class="btn btn-primary btn-sm" type="submit">Join</button>
          <div class="ok-msg">You're subscribed to UK road &amp; weather alerts.</div>
        </form>
      </div>
    </div>
    <div class="foot-bot">
      <span>&copy; <span data-year></span> RoadRescue 24/7 Ltd. Registered in England &amp; Wales. Demo site.</span>
      <span>Privacy · Terms · Cookies · VAT GB 123 4567 89</span>
    </div>
  </div>
</footer>

<div class="sos-panel">
  <h4>Emergency SOS</h4>
  <p>Tell us what happened — we'll open WhatsApp with it pre-filled.</p>
  <div class="sos-quick">
    <button type="button">Car won't start</button>
    <button type="button">Locked out / lost keys</button>
    <button type="button">Flat tyre or blowout</button>
    <button type="button">Accident / need recovery</button>
  </div>
  <a class="btn btn-wa btn-block" data-sos-go target="_blank" rel="noopener" href="#">{ICONS['wa']} Send on WhatsApp</a>
  <button class="btn btn-ghost btn-block btn-sm" style="margin-top:.5rem" data-sos-close type="button">Close</button>
</div>

<div class="dock">
  <button class="fab fab-top" data-tip="Back to top" aria-label="Back to top">{ICONS['up']}</button>
  <a class="fab fab-call" data-tip="Call the control room" href="#" data-tel aria-label="Call">{ICONS['phone']}</a>
  <a class="fab fab-wa" data-tip="WhatsApp SOS" href="#" data-wa="Emergency! I need help with my car." target="_blank" rel="noopener" aria-label="WhatsApp">{ICONS['wa']}</a>
</div>

<script src="assets/js/data.js"></script>
{leaflet}
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def page(name, title, desc, body, active):
    return head(title, desc, name) + header(active) + body + footer(name)

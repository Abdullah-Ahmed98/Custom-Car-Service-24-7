from layout import ICONS as I

SERVICES = [
    ("mechanic", "Emergency Mobile Mechanic", "wrench", "", 65, "20–40 min",
     "Your car won't start, is overheating, has lost power or lit up the dashboard. A fully-equipped van comes to your driveway, car park or hard shoulder and diagnoses it properly — then fixes it there if it can be fixed there.",
     ["Non-start &amp; crank-no-start faults", "Alternator, starter &amp; belt failures", "Brake, clutch &amp; suspension repairs", "Cooling system &amp; overheating", "Warning light investigation", "Pre-MOT and post-MOT fail repairs"], "assets/img/diag.jpg"),
    ("keys", "Car Key Making &amp; Programming", "key", "teal", 89, "30–60 min",
     "Lost every key, snapped one in the door or need a spare that doesn't cost a dealership fortune? Our auto locksmiths cut and code keys at the roadside with insurance-approved equipment.",
     ["All-keys-lost replacement", "Transponder &amp; chip key cutting", "Remote fob and keyless/proximity coding", "Snapped key extraction", "Lock barrel repair &amp; replacement", "Spare keys cut on your driveway"], "assets/img/keys.jpg"),
    ("lockout", "Vehicle Lockout &amp; Unlocking", "chip", "", 55, "20–35 min",
     "Keys on the seat, boot jammed shut, or a child or pet locked inside. Non-destructive entry techniques get you back in without damaging the door, glass or electronics.",
     ["Non-destructive door opening", "Boot and tailgate release", "Child or pet lock-in emergencies (prioritised)", "Keys locked in a running vehicle", "Vans, campers and light commercials", "No damage guarantee"], None),
    ("battery", "Battery, Jump Start &amp; Electrics", "battery", "teal", 45, "15–30 min",
     "Cold morning, dead battery. We test the battery, alternator and parasitic drain before selling you anything — then fit a replacement on the spot if you actually need one.",
     ["Jump start &amp; safe boost", "Battery health &amp; alternator testing", "Same-visit battery replacement", "3-year battery warranty", "Parasitic drain diagnosis", "Start-stop &amp; AGM batteries coded to the ECU"], None),
    ("tyre", "Puncture &amp; Tyre Replacement", "tyre", "", 49, "25–45 min",
     "Blowout, slow puncture or a wheel you can't shift because the locking nut key is missing. We repair or replace at the roadside and dispose of the old tyre.",
     ["Roadside plug and patch repairs", "Full tyre supply &amp; fitting", "Locking wheel nut removal", "Space-saver and run-flat handling", "Wheel swap to your spare", "Pressure and tread safety check"], None),
    ("diagnostic", "On-Site Fault Diagnostics", "chip", "teal", 59, "25–40 min",
     "Dealer-level OBD scanning with live sensor data, so you find out what's actually wrong before a garage quotes you for guesswork.",
     ["Full multi-system fault code read", "Live data &amp; freeze-frame analysis", "ABS, airbag, engine &amp; gearbox modules", "EV and hybrid high-voltage systems", "Written report with photos", "Fault codes cleared and road tested"], "assets/img/diag.jpg"),
    ("fuel", "Wrong Fuel Drain &amp; Flush", "fuel", "", 129, "35–60 min",
     "Petrol in a diesel is the UK's most common misfuel — around 150,000 a year. Call before you turn the key and it's usually a same-day, no-damage fix.",
     ["Full contaminated fuel drain", "Fuel line and rail flush", "Filter replacement where needed", "Safe disposal of drained fuel", "Injector damage assessment", "Refill with correct fuel to get you going"], None),
    ("recovery", "Breakdown Recovery &amp; Towing", "tow", "teal", 95, "30–60 min",
     "When it genuinely can't be fixed roadside, we move the car — to your home, your chosen garage or anywhere in the UK, including prestige and low-clearance vehicles.",
     ["Flatbed and spec-lift recovery", "Accident and non-runner recovery", "EV recovery with correct wheel lift", "Motorway and hard shoulder collection", "Nationwide long-distance transport", "Storage arranged if needed"], None),
]

FAQS = [
    ("Are you really available 24 hours a day?", "Yes — genuinely. Our Birmingham control room is staffed around the clock, including Christmas Day and bank holidays. Night rates (7pm–7am) carry a 35% loading, which we always tell you before dispatch."),
    ("Do I need a membership or subscription?", "No. RoadRescue is entirely pay-as-you-go. There is no joining fee, no annual renewal and no tiered plan. You pay for the callout you actually use."),
    ("How is the price decided?", "You get a fixed quote in writing on WhatsApp or SMS before the engineer starts. It covers callout, labour and any parts agreed. If the job turns out to be smaller than expected, you pay less."),
    ("Which areas of the UK do you cover?", "All 124 UK postcode areas — England, Scotland, Wales and Northern Ireland, including motorways, service stations, airports and rural roads. Remote Highland and island callouts may carry a longer ETA."),
    ("Can you make a car key if I've lost all of them?", "In most cases yes, at the roadside. We'll need proof of ownership (V5C or insurance documents) plus photo ID. Some premium and very recent models require a dealer-linked security code, which we'll tell you up front."),
    ("What if my car can't be fixed at the roadside?", "About 6% of jobs need recovery. If yours is one of them, your engineer arranges a flatbed there and then and the diagnostic fee is credited against the recovery cost."),
    ("Do you work on electric and hybrid vehicles?", "Yes. Every partner attending an EV holds IMI Level 3 high-voltage certification, and our recovery units use correct wheel-lift or flatbed methods to protect the drivetrain."),
    ("How do I pay?", "Card on the roadside via the engineer's terminal, Apple/Google Pay, or a payment link sent to your phone. We issue a VAT invoice by email immediately after the job."),
]

BODY = f"""
<main>

<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow" style="justify-content:center">Emergency services</span>
    <h1>Every roadside emergency,<br>covered <span class="amber">24/7</span>.</h1>
    <p class="lead">Eight core services, fixed prices, nationwide UK coverage. Most jobs are completed where your car stopped — no tow, no garage queue, no week without a car.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="index.html#finder">{I['pin']} Find nearest unit</a>
      <a class="btn btn-wa btn-lg" href="#" data-wa="Hi, I need help with: " target="_blank" rel="noopener">{I['wa']} WhatsApp SOS</a>
    </div>
    <div class="crumbs"><a href="index.html">Home</a> / <span class="amber">Services</span></div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap grid" style="gap:1.6rem">
    {"".join(f'''
    <article class="card svc-wide rv" id="{key}">
      <div class="img">{f'<img src="{img}" alt="{name}" loading="lazy">' if img else f'<div style="height:100%;min-height:220px;display:grid;place-items:center;background:linear-gradient(150deg,rgba(255,176,32,.12),rgba(46,230,197,.06))"><span class="ico {col}" style="width:78px;height:78px;margin:0;border-radius:24px">{I[ic]}</span></div>'}</div>
      <div class="body">
        <div style="display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;margin-bottom:.9rem">
          <span class="pill hot">From £{price}</span>
          <span class="pill live"><span class="dot"></span> Typical arrival {eta}</span>
          <span class="pill">Available 24/7</span>
        </div>
        <h3 style="font-size:1.5rem">{name}</h3>
        <p style="margin-top:.7rem">{desc}</p>
        <div class="chips">{"".join(f'<span class="tag" style="padding:.32rem .7rem;font-size:.76rem">{b}</span>' for b in bullets)}</div>
        <div class="hero-actions" style="margin:1.5rem 0 0">
          <a class="btn btn-primary btn-sm" href="#" data-tel>{I['phone']} Call now</a>
          <a class="btn btn-wa btn-sm" href="#" data-wa="I need: {name}. My location: " target="_blank" rel="noopener">{I['wa']} Get a quote</a>
        </div>
      </div>
    </article>''' for key, name, ic, col, price, eta, desc, bullets, img in SERVICES)}
  </div>
</section>

<section style="background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)">
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">Transparent pricing</span>
      <h2>What actually goes on the invoice</h2>
      <p>Three things and nothing else: the callout, the labour, and any parts you approved. Here's how the loadings work.</p>
    </div>
    <div class="grid g3">
      {"".join(f'''<article class="card rv" style="{hi}">
        <span class="pill {p}">{tag}</span>
        <h3 style="margin:1rem 0 .4rem">{t}</h3>
        <div style="font-family:var(--font-display);font-size:2.2rem;font-weight:800;color:var(--amber);line-height:1">{price}</div>
        <p style="margin-top:.8rem">{d}</p>
        <ul class="checklist" style="margin-top:1.2rem">{"".join(f'<li>{I["check"]}<span>{x}</span></li>' for x in items)}</ul>
      </article>''' for tag, p, t, price, d, items, hi in [
        ("Standard", "", "Weekday daytime", "from £45", "Monday to Friday, 7am to 7pm. Our base rate with no loading applied.",
         ["No callout surcharge", "First 5 miles included", "Fixed quote before work"], ""),
        ("Most booked", "hot", "Evenings &amp; weekends", "+15%", "Saturday, Sunday and bank holidays, 7am to 7pm. The busiest slot on our network.",
         ["Same engineers, same standards", "Priority for lock-in emergencies", "12-month warranty"], "border-color:rgba(255,176,32,.4)"),
        ("Night cover", "live", "Overnight 7pm–7am", "+35%", "The hours nobody else answers the phone. Fully staffed dispatch every night of the year.",
         ["Guaranteed human dispatcher", "Motorway-trained crews", "Free safety wait with lone drivers"], ""),
      ])}
    </div>
    <p style="text-align:center;font-size:.82rem;color:var(--muted-dim);margin-top:1.6rem">Mileage beyond the first 5 miles is £1.60/mile. Parts quoted separately and always approved by you first. All prices include VAT.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">Extras worth knowing</span>
      <h2>Added-value services</h2>
    </div>
    <div class="grid g4">
      {"".join(f'<article class="card rv"><span class="ico {c}">{I[ic]}</span><h3 style="font-size:1.08rem">{t}</h3><p style="font-size:.9rem">{d}</p></article>'
        for t, d, ic, c in [
          ("Pre-purchase inspection", "Buying used? We'll meet you at the seller and give an honest 120-point verdict before money changes hands.", "check", ""),
          ("Fleet &amp; taxi accounts", "Priority dispatch, monthly invoicing and a named account manager for business fleets of 5+ vehicles.", "car", "teal"),
          ("Winter readiness check", "Battery, coolant, tyres, wipers and lights — a 20-minute check at your home before the cold snap.", "shield", ""),
          ("Safe-wait for lone drivers", "If you're alone at night, your engineer stays until you're moving and safely away. No extra charge.", "users", "teal"),
        ])}
    </div>
  </div>
</section>

<section id="faq" style="background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)">
  <div class="wrap" style="max-width:880px">
    <div class="section-head center rv">
      <span class="eyebrow">Questions</span>
      <h2>Frequently asked</h2>
    </div>
    <div data-acc-group class="rv">
      {"".join(f'<div class="acc"><button class="acc-q" type="button">{q}<i>+</i></button><div class="acc-a"><p>{a}</p></div></div>' for q, a in FAQS)}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta-box rv">
      <h2>Not sure which service you need?</h2>
      <p class="lead" style="max-width:600px;margin:1rem auto 0">Describe the symptoms on WhatsApp — a dispatcher will tell you in plain English what's likely wrong and what it should cost.</p>
      <div class="btns">
        <a class="btn btn-wa btn-lg" href="#" data-wa="Hi, I'm not sure what's wrong. Symptoms: " target="_blank" rel="noopener">{I['wa']} Ask a dispatcher</a>
        <a class="btn btn-primary btn-lg" href="#" data-tel>{I['phone']} Call <span data-phone-text></span></a>
      </div>
    </div>
  </div>
</section>

</main>
"""

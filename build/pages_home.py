from layout import ICONS as I

BODY = f"""
<main>

<!-- HERO -->
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div class="rv in">
        <span class="pill live"><span class="dot"></span> Live dispatch · 214 units on shift</span>
        <h1>Stranded? A UK mechanic is <span class="grad">minutes away.</span></h1>
        <p class="lead">Emergency mobile mechanics, auto locksmiths, car key cutting and recovery — dispatched to your exact location, anywhere in the UK, 24 hours a day, 365 days a year. No membership. No waiting on hold.</p>
        <div class="hero-actions">
          <a class="btn btn-primary btn-lg" href="#finder">{I['pin']} Find nearest mechanic</a>
          <a class="btn btn-wa btn-lg" href="#" data-wa="Emergency! I'm broken down and need a mechanic now. My location: " target="_blank" rel="noopener">{I['wa']} WhatsApp SOS</a>
          <a class="btn btn-ghost btn-lg" href="#" data-tel>{I['phone']} <span data-phone-text></span></a>
        </div>
        <div class="hero-stats">
          <div><div class="n"><span data-count="27">0</span></div><div class="l">Avg. minutes to arrive</div></div>
          <div><div class="n"><span data-count="480" data-suffix="+">0</span></div><div class="l">Vetted UK partners</div></div>
          <div><div class="n"><span data-count="4.9">0</span><span class="amber">★</span></div><div class="l">From 12,400 reviews</div></div>
          <div><div class="n">24/7</div><div class="l">Always on shift</div></div>
        </div>
      </div>

      <div class="hero-visual rv in">
        <div class="shot"><img src="assets/img/hero.jpg" alt="Mobile mechanic attending a broken down car on a UK motorway at night" width="1376" height="768"></div>
        <div class="float-card fc-1">
          <span class="ico teal" style="width:38px;height:38px;margin:0;border-radius:12px">{I['clock']}</span>
          <div><div class="t">Unit 14 dispatched</div><div class="s">ETA 12 min · M6 J8 northbound</div></div>
        </div>
        <div class="float-card fc-2">
          <span class="ico" style="width:38px;height:38px;margin:0;border-radius:12px">{I['shield']}</span>
          <div><div class="t">DBS-checked &amp; insured</div><div class="s">Every engineer, every callout</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TICKER -->
<div class="ticker">
  <div class="ticker-track">
    {"".join(f'<span><i>◆</i> {t}</span>' for t in ["London","Manchester","Birmingham","Leeds","Glasgow","Edinburgh","Cardiff","Belfast","Bristol","Liverpool","Newcastle","Sheffield","Nottingham","Brighton"] * 2)}
  </div>
</div>

<!-- FINDER -->
<section id="finder">
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">Nearest mechanic finder</span>
      <h2>Type a postcode. We'll show who can reach you first.</h2>
      <p>Search our live UK partner network by town or postcode, filter by the service you need, and call or WhatsApp the closest unit directly. Coverage across England, Scotland, Wales and Northern Ireland.</p>
    </div>

    <div class="finder-shell rv">
      <div class="finder-top">
        <div class="finder-form">
          <label class="field">
            {I['pin']}
            <input id="loc-input" type="text" placeholder="UK town or postcode — e.g. M4 5AB" value="London" aria-label="Location">
          </label>
          <label class="field">
            {I['wrench']}
            <select id="svc-select" aria-label="Service">
              <option value="all">All services</option>
              <option value="mechanic">Mobile mechanic</option>
              <option value="keys">Car keys &amp; programming</option>
              <option value="lockout">Lockout / unlocking</option>
              <option value="battery">Battery &amp; jump start</option>
              <option value="tyre">Tyre &amp; puncture</option>
              <option value="diagnostic">Fault diagnostics</option>
              <option value="fuel">Wrong fuel drain</option>
              <option value="recovery">Recovery &amp; towing</option>
            </select>
          </label>
          <button class="btn btn-primary" id="find-btn">Search</button>
          <button class="btn btn-ghost" id="geo-btn">{I['pin']} Use my GPS</button>
        </div>
        <div id="find-status" style="font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:.5rem"></div>
      </div>
      <div class="finder-body">
        <div class="finder-list" id="mech-list"></div>
        <div id="map"></div>
      </div>
    </div>
    <p style="font-size:.78rem;color:var(--muted-dim);margin-top:.9rem;text-align:center">Demo network data for illustration. In production this connects to our live dispatch API and real-time GPS positions.</p>
  </div>
</section>

<!-- SERVICES -->
<section>
  <div class="wrap">
    <div class="section-head rv">
      <span class="eyebrow">What we fix, roadside</span>
      <h2>Eight emergencies. One number. Any hour.</h2>
      <p>Fully-equipped vans carry diagnostics, key-cutting gear, jump packs, tyres and tooling — so most jobs are finished where you stand, not at a garage next week.</p>
    </div>
    <div class="grid g4">
      {"".join(f'''
      <article class="card svc rv">
        <span class="ico {c}">{I[ic]}</span>
        <h3>{t}</h3>
        <p>{d}</p>
        <div class="price"><div><b>from £{p}</b><br><span>{e}</span></div><span class="arrow">{I['arrow']}</span></div>
      </article>''' for t, d, p, e, ic, c in [
        ("Mobile Mechanic", "Engine won't turn over, warning lights, overheating, belts, brakes — diagnosed and fixed at the kerbside.", 65, "20–40 min", "wrench", ""),
        ("Car Key Making", "Lost every key? We cut and program transponder keys and fobs on-site for most makes, no tow needed.", 89, "30–60 min", "key", "teal"),
        ("Lockout Rescue", "Keys locked in, snapped in the barrel or a baby in the back seat — non-destructive entry, fast.", 55, "20–35 min", "chip", ""),
        ("Battery & Jump", "Jump start, alternator testing and same-visit battery replacement with a 3-year warranty.", 45, "15–30 min", "battery", "teal"),
        ("Tyre & Puncture", "Roadside plug, patch or full replacement including locking-nut removal and space-saver fitting.", 49, "25–45 min", "tyre", ""),
        ("Fault Diagnostics", "Dealer-level OBD scanning with live data, so you know the real fault before anyone touches your wallet.", 59, "25–40 min", "chip", "teal"),
        ("Wrong Fuel Drain", "Misfuelled? We drain, flush and refill the system roadside — usually with no lasting engine damage.", 129, "35–60 min", "fuel", ""),
        ("Recovery & Towing", "Flatbed and spec-lift recovery to your home, chosen garage or anywhere in the UK.", 95, "30–60 min", "tow", "teal"),
      ])}
    </div>
    <div style="text-align:center;margin-top:2.6rem" class="rv">
      <a class="btn btn-ghost btn-lg" href="services.html">See all services &amp; transparent pricing {I['arrow']}</a>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section style="background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)">
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">How it works</span>
      <h2>Four steps from stranded to sorted</h2>
    </div>
    <div class="steps">
      {"".join(f'''<div class="step rv"><h3>{t}</h3><p>{d}</p></div>''' for t, d in [
        ("Tell us where", "Share your postcode, drop a pin on WhatsApp or hit “Use my GPS”. Works on the hard shoulder with one bar of signal."),
        ("Get matched", "Our dispatcher assigns the nearest available engineer with the right kit — you see their name, rating and live ETA."),
        ("Fixed price first", "You approve a fixed quote before a spanner is lifted. No hourly creep, no surprise invoice."),
        ("Back on the road", "Most jobs finish roadside. If it can't be fixed there, recovery is arranged in the same call."),
      ])}
    </div>
  </div>
</section>

<!-- SPLIT: keys -->
<section>
  <div class="wrap split">
    <div class="media rv"><img src="assets/img/keys.jpg" alt="Auto locksmith programming a car key" loading="lazy"></div>
    <div class="rv">
      <span class="eyebrow">Auto locksmith division</span>
      <h2>Lost your only car key at 3am?</h2>
      <p class="lead">You don't need a main dealer, a tow truck or a two-week wait. Our mobile locksmiths carry key-cutting machines and dealer-grade programmers in the van.</p>
      <ul class="checklist">
        {"".join(f'<li>{I["check"]}<span>{x}</span></li>' for x in [
          "All-keys-lost service for most UK makes and models",
          "Transponder, remote fob and proximity/keyless key programming",
          "Snapped key extraction and lock barrel repair or replacement",
          "Spare keys cut on the driveway — cheaper than the dealership",
          "Immobiliser and ECU coding with insurance-approved equipment",
        ])}
      </ul>
      <div class="hero-actions" style="margin-bottom:0">
        <a class="btn btn-primary" href="services.html#keys">Car key services</a>
        <a class="btn btn-wa" href="#" data-wa="I've lost my car keys and need a replacement made. Car make/model: " target="_blank" rel="noopener">{I['wa']} Get a key quote</a>
      </div>
    </div>
  </div>
</section>

<!-- BAND -->
<div class="band">
  <div class="wrap" style="padding:3.2rem 0">
    <div class="band-grid">
      {"".join(f'<div class="rv"><div class="n"><span data-count="{n}" data-suffix="{s}">0</span></div><div class="l">{l}</div></div>' for n, s, l in [
        ("128000", "+", "Callouts completed"), ("94", "%", "Fixed at the roadside"),
        ("27", " min", "Average arrival time"), ("12", " mo", "Parts &amp; labour warranty"),
      ])}
    </div>
  </div>
</div>

<!-- ESTIMATOR -->
<section>
  <div class="wrap">
    <div class="section-head rv">
      <span class="eyebrow">No-surprises pricing</span>
      <h2>Instant callout estimator</h2>
      <p>Move the sliders and see roughly what you'll pay before you ring. Night and weekend loadings are shown up front — because hiding them is how the industry got its reputation.</p>
    </div>
    <form class="est rv" id="estimator" onsubmit="return false">
      <div class="est-form">
        <div class="form-row">
          <label for="service">What do you need?</label>
          <select class="input" id="service" name="service">
            <option value="mechanic">Emergency mobile mechanic</option>
            <option value="keys">Car key making &amp; programming</option>
            <option value="lockout">Vehicle lockout / unlocking</option>
            <option value="battery">Battery jump start or replacement</option>
            <option value="tyre">Puncture &amp; tyre replacement</option>
            <option value="diagnostic">On-site fault diagnostics</option>
            <option value="fuel">Wrong fuel drain &amp; flush</option>
            <option value="recovery">Breakdown recovery &amp; towing</option>
          </select>
        </div>
        <div class="form-row">
          <label>When?</label>
          <div class="opt-grid">
            <label class="opt"><input type="radio" name="timeslot" value="day" checked><span>Weekday 7am–7pm</span></label>
            <label class="opt"><input type="radio" name="timeslot" value="weekend"><span>Weekend (+15%)</span></label>
            <label class="opt"><input type="radio" name="timeslot" value="night"><span>Night 7pm–7am (+35%)</span></label>
          </div>
        </div>
        <div class="form-row">
          <label for="distance">Distance from nearest unit — <span id="dist-out" class="amber">8 mi</span></label>
          <input class="input" type="range" id="distance" name="distance" min="1" max="40" value="8" style="padding:.6rem 0;background:none;border:0">
          <span class="form-note">First 5 miles included, then £1.60 per mile.</span>
        </div>
      </div>
      <aside class="est-out">
        <span class="pill hot">Estimated total</span>
        <div class="big" id="est-total">£0</div>
        <div class="est-line"><span>Base callout</span><span id="est-base">£0</span></div>
        <div class="est-line"><span>Time multiplier</span><span id="est-time">×1</span></div>
        <div class="est-line"><span>Mileage</span><span id="est-dist">£0</span></div>
        <div class="est-line"><span>Typical arrival</span><span id="est-eta">—</span></div>
        <a class="btn btn-wa btn-block" style="margin-top:1.3rem" data-est-wa target="_blank" rel="noopener" href="#">{I['wa']} Book this on WhatsApp</a>
        <p class="form-note" style="margin-top:.8rem">Indicative only — your engineer confirms a fixed price on arrival before starting work.</p>
      </aside>
    </form>
  </div>
</section>

<!-- WHY US -->
<section style="background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)">
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">Why drivers choose us</span>
      <h2>Built for the worst night of your week</h2>
    </div>
    <div class="grid g3">
      {"".join(f'''<article class="card rv"><span class="ico {c}">{I[ic]}</span><h3>{t}</h3><p>{d}</p></article>'''
        for t, d, ic, c in [
          ("No membership, ever", "Pay only when you need us. No annual fee, no tiers, no renewal letters that quietly double the price.", "shield", ""),
          ("Vetted &amp; insured engineers", "Every partner is DBS-checked, qualified to IMI standards and carries £2m public liability cover.", "users", "teal"),
          ("Live ETA tracking", "Watch your engineer approach on the map and get WhatsApp updates at dispatch, en-route and arrival.", "pin", ""),
          ("Fixed quote up front", "The price you're told is the price you pay — confirmed in writing on WhatsApp before work starts.", "check", "teal"),
          ("Genuine 24/7 cover", "Christmas Day, 4am, Boxing Day gales — the control room is staffed by humans in the UK, always.", "clock", ""),
          ("Greener callouts", "Route-optimised dispatch and a growing EV van fleet cut wasted miles and roadside idling.", "leaf", "teal"),
        ])}
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section>
  <div class="wrap">
    <div class="section-head rv">
      <span class="eyebrow">Real callouts, real drivers</span>
      <h2>12,400 reviews. 4.9 average.</h2>
    </div>
    <div class="grid g3">
      {"".join(f'''<article class="card quote rv">
        <div class="stars" style="font-size:1rem">★★★★★</div>
        <p>“{q}”</p>
        <div class="who"><div class="avatar">{n[0]}</div><div><div class="n">{n}</div><div class="c">{c}</div></div></div>
      </article>''' for q, n, c in [
        ("Broke down on the M62 at half eleven at night with two kids in the back. Someone answered in four rings and a van was with us in 22 minutes. Alternator belt replaced on the hard shoulder.", "Hannah Whitfield", "Leeds · Mobile mechanic"),
        ("Dropped my only Golf key down a drain in Soho. They cut and coded a new one next to the car in under an hour — the dealer had quoted three days and double the money.", "Marcus Adeyemi", "London · Car key making"),
        ("Put petrol in my diesel Qashqai at a services near Perth. Drained, flushed and back on the road the same afternoon. Honest, calm and fixed price before they started.", "Fiona Sinclair", "Perth · Wrong fuel drain"),
      ])}
    </div>
  </div>
</section>

<!-- CTA -->
<section>
  <div class="wrap">
    <div class="cta-box rv">
      <span class="pill live"><span class="dot"></span> Control room open now</span>
      <h2 style="margin:1.2rem 0 .8rem">Don't wait on hold with your insurer.</h2>
      <p class="lead" style="max-width:620px;margin-inline:auto">One message and the nearest engineer to you is on the way. Nationwide UK coverage, every hour of every day.</p>
      <div class="btns">
        <a class="btn btn-primary btn-lg" href="#" data-tel>{I['phone']} Call <span data-phone-text></span></a>
        <a class="btn btn-wa btn-lg" href="#" data-wa="Emergency! Please send the nearest mechanic. My location: " target="_blank" rel="noopener">{I['wa']} WhatsApp SOS</a>
        <a class="btn btn-ghost btn-lg" href="contact.html">Book a callout</a>
      </div>
    </div>
  </div>
</section>

</main>
"""

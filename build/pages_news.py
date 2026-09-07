from layout import ICONS as I

POSTS = [
    ("service", "Service update", "05 Sep 2026", "Night-shift capacity increased by 40% across the North West",
     "From this week we have 62 additional engineers on the 7pm–7am rota covering Greater Manchester, Merseyside and Lancashire. Average overnight arrival in the region drops to an expected 24 minutes.", True),
    ("alert", "Weather alert", "03 Sep 2026", "Storm Freya: what to do if you break down in high winds",
     "Amber warnings are in place for Scotland and the North East. If you stop on a motorway, exit the vehicle on the passenger side and wait behind the barrier — never in the car on the hard shoulder.", False),
    ("coverage", "Coverage", "28 Aug 2026", "Northern Ireland network doubles to 34 partner engineers",
     "Belfast, Derry/Londonderry, Lisburn and Newry now have dedicated overnight cover, including two dedicated auto locksmith units for all-keys-lost callouts.", False),
    ("service", "Service update", "21 Aug 2026", "Live ETA tracking now sent automatically over WhatsApp",
     "Every callout now triggers three automatic messages: engineer assigned, en route with a live map link, and arriving in five minutes. No app download required.", False),
    ("advice", "Driver advice", "14 Aug 2026", "Five dashboard warning lights you must never drive on",
     "Red oil pressure, red coolant temperature, red brake warning, flashing engine management and the airbag light. We explain what each one means and the damage bill for ignoring it.", False),
    ("coverage", "Coverage", "07 Aug 2026", "EV recovery units added at 12 motorway service areas",
     "Correct wheel-lift and flatbed EV recovery is now stationed at key M1, M6 and M25 services, cutting waits for electric vehicle drivers to under 35 minutes.", False),
    ("advice", "Driver advice", "30 Jul 2026", "Misfuelled? Do this one thing before you touch the ignition",
     "Around 150,000 UK drivers put the wrong fuel in each year. If you don't start the engine, a roadside drain is usually all that's needed — and costs a fraction of injector replacement.", False),
    ("service", "Service update", "18 Jul 2026", "Fixed-price car key programming now covers 41 more models",
     "New dealer-grade programmers across the network add coverage for recent Kia, MG, Cupra and BYD models, including keyless proximity fobs.", False),
    ("alert", "Notice", "02 Jul 2026", "Bank holiday cover: we are open, as always",
     "Every UK bank holiday, including Christmas Day and New Year's Day, our control room and partner network operate a full rota at standard weekend rates.", False),
]

BODY = f"""
<main>

<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow" style="justify-content:center">News &amp; announcements</span>
    <h1>Service updates, road alerts<br>and driver advice.</h1>
    <p class="lead">Live operational notices from the control room, UK weather and roadworks warnings, and practical guidance for when things go wrong.</p>
    <div class="crumbs"><a href="index.html">Home</a> / <span class="amber">News</span></div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="rv">
      <div class="alert-strip">
        <span class="ico">{I['alert']}</span>
        <div>
          <h4>Live: Amber wind warning — Scotland &amp; North East England</h4>
          <p>Storm Freya is bringing 70mph gusts until 22:00 Monday. Expect longer arrival times on exposed routes such as the A1(M), A66 and M74. High-sided vehicle restrictions are in force on the Queensferry Crossing.</p>
        </div>
      </div>
      <div class="alert-strip info">
        <span class="ico">{I['clock']}</span>
        <div>
          <h4>Network status: all regions operating normally</h4>
          <p>214 units on shift right now. Average UK arrival time in the last hour: 26 minutes. Auto locksmith availability: good in all regions except the Highlands (approx. 70 minutes).</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="padding-top:2rem">
  <div class="wrap">
    <div class="filters rv">
      <button class="filter on" data-filter="all">All updates</button>
      <button class="filter" data-filter="service">Service updates</button>
      <button class="filter" data-filter="alert">Road &amp; weather alerts</button>
      <button class="filter" data-filter="coverage">Coverage</button>
      <button class="filter" data-filter="advice">Driver advice</button>
    </div>

    <div class="grid g3">
      {"".join(f'''
      <article class="card post rv" data-cat="{cat}">
        <div class="thumb">
          {'<img src="assets/img/hero.jpg" alt="" loading="lazy">' if featured else f'<div style="height:100%;display:grid;place-items:center"><span class="ico {"teal" if cat in ("coverage","advice") else ""}" style="width:64px;height:64px;margin:0;border-radius:20px">{I[{"service":"wrench","alert":"alert","coverage":"pin","advice":"chip"}[cat]]}</span></div>'}
          <span class="pill {"hot" if cat == "alert" else "live" if cat == "service" else ""}">{label}</span>
        </div>
        <div class="body">
          <span class="date">{date}</span>
          <h3>{title}</h3>
          <p>{body}</p>
          <a class="readmore" href="#">Read the full update {I['arrow']}</a>
        </div>
      </article>''' for cat, label, date, title, body, featured in POSTS)}
    </div>
  </div>
</section>

<section style="background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)">
  <div class="wrap grid g2" style="gap:3rem;align-items:start">
    <div class="rv">
      <span class="eyebrow">Roadside safety</span>
      <h2>If you break down on a motorway</h2>
      <p style="margin-top:1rem">Highways England data shows the hard shoulder is one of the most dangerous places in the UK. Follow this order — every time, even in the rain.</p>
      <div class="timeline" style="margin-top:2rem">
        {"".join(f'<div class="tl-item"><div class="d">Step {i+1}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate([
          ("Pull as far left as possible", "Get onto the hard shoulder or into an emergency refuge area, wheels turned to the left, and switch on your hazard lights immediately."),
          ("Everyone out on the passenger side", "Exit through the left-hand doors, including pets on leads, and climb behind the safety barrier. Never stand between the car and traffic."),
          ("Move up the embankment and back", "Stand behind the barrier and upstream of your vehicle so you are not in the path if it is struck."),
          ("Call for help — 999 first if in a live lane", "If you cannot leave a live running lane, stay belted in with hazards on and call 999. Otherwise call us or use the orange SOS phone."),
          ("Do not attempt repairs yourself", "No changing a wheel, no lifting the bonnet, no warning triangle on a motorway. Wait behind the barrier until your engineer arrives."),
        ]))}
      </div>
    </div>
    <div class="rv">
      <div class="card" style="padding:2.2rem">
        <span class="ico">{I['mail']}</span>
        <h3>Get alerts before you set off</h3>
        <p style="margin-bottom:1.3rem">One short email when severe weather, major roadworks or a service change affects your region. No marketing, unsubscribe in one click.</p>
        <form data-validate class="est-form">
          <div class="form-row">
            <label for="n-name">Name</label>
            <input class="input" id="n-name" name="Name" required placeholder="Alex Morgan">
            <span class="err-txt">Please enter your name.</span>
          </div>
          <div class="form-row">
            <label for="n-email">Email</label>
            <input class="input" id="n-email" name="Email" type="email" required placeholder="you@email.co.uk">
            <span class="err-txt">Please enter a valid email.</span>
          </div>
          <div class="form-row">
            <label for="n-region">Region</label>
            <select class="input" id="n-region" name="Region">
              <option>London &amp; South East</option><option>South West</option><option>Midlands</option>
              <option>North West</option><option>North East &amp; Yorkshire</option>
              <option>Scotland</option><option>Wales</option><option>Northern Ireland</option>
            </select>
          </div>
          <button class="btn btn-primary btn-block" type="submit">Subscribe to alerts</button>
          <div class="ok-msg">Subscribed — you'll get regional alerts from the control room.</div>
        </form>
      </div>
      <div class="card" style="padding:2.2rem;margin-top:1.4rem">
        <span class="ico teal">{I['wa']}</span>
        <h3>Prefer WhatsApp?</h3>
        <p style="margin-bottom:1.2rem">Join the broadcast list for the same alerts straight to your phone — plus one-tap SOS if you ever need us.</p>
        <a class="btn btn-wa btn-block" href="#" data-wa="Please add me to the RoadRescue 24/7 WhatsApp alert list. My region: " target="_blank" rel="noopener">{I['wa']} Join the alert list</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta-box rv">
      <h2>Need help right now, not news?</h2>
      <div class="btns">
        <a class="btn btn-primary btn-lg" href="index.html#finder">{I['pin']} Find nearest mechanic</a>
        <a class="btn btn-wa btn-lg" href="#" data-wa="Emergency! I need help now. Location: " target="_blank" rel="noopener">{I['wa']} WhatsApp SOS</a>
      </div>
    </div>
  </div>
</section>

</main>
"""

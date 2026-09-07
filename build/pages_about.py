from layout import ICONS as I

BODY = f"""
<main>

<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow" style="justify-content:center">About RoadRescue 24/7</span>
    <h1>We built the breakdown service<br>we wished existed.</h1>
    <p class="lead">Founded by two ex-recovery drivers who were tired of watching people wait four hours in the rain for a callout they'd already paid a yearly fee for.</p>
    <div class="crumbs"><a href="index.html">Home</a> / <span class="amber">About</span></div>
  </div>
</section>

<section style="padding-top:1rem">
  <div class="wrap split">
    <div class="media rv"><img src="assets/img/team.jpg" alt="RoadRescue engineers in a UK workshop" loading="lazy"></div>
    <div class="rv">
      <span class="eyebrow">Our story</span>
      <h2>From one van in Birmingham to 480 partners nationwide</h2>
      <p style="margin-top:1rem">In 2016, Dan Okafor and Chris Reilly were subcontracting for a national breakdown brand. They saw the same thing every shift: drivers stuck for hours, quoted one price on the phone and charged another on the kerb, and told "we can't do keys" or "that'll need a tow" when a £70 roadside fix would have done it.</p>
      <p style="margin-top:1rem">So they started RoadRescue with a single kitted van and a rule that still governs everything: <strong style="color:var(--text)">tell the customer the real price before you touch the car, and try to fix it where it stands.</strong></p>
      <p style="margin-top:1rem">Today that rule is enforced across a vetted network of 480+ independent engineers and auto locksmiths covering every UK postcode area, coordinated from a control room in Birmingham that never closes.</p>
      <ul class="checklist">
        {"".join(f'<li>{I["check"]}<span>{x}</span></li>' for x in [
          "No membership fees — 100% pay-as-you-go",
          "94% of callouts resolved without a tow",
          "UK-staffed control room, not an overseas call centre",
        ])}
      </ul>
    </div>
  </div>
</section>

<div class="band">
  <div class="wrap" style="padding:3rem 0">
    <div class="band-grid">
      {"".join(f'<div class="rv"><div class="n"><span data-count="{n}" data-suffix="{s}">0</span></div><div class="l">{l}</div></div>' for n, s, l in [
        ("2016", "", "Founded in Birmingham"), ("480", "+", "Vetted partner engineers"),
        ("124", "", "UK postcode areas covered"), ("128000", "+", "Drivers rescued"),
      ])}
    </div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">What we stand for</span>
      <h2>Four promises we don't bend</h2>
    </div>
    <div class="grid g4">
      {"".join(f'<article class="card rv"><span class="ico {c}">{I[ic]}</span><h3>{t}</h3><p>{d}</p></article>'
        for t, d, ic, c in [
          ("Price honesty", "A fixed quote, in writing, before work begins. If the job turns out smaller, you pay less — that has happened 3,100 times.", "check", ""),
          ("Speed with safety", "Fast matters, but nobody works on a live carriageway without cones, lights and a risk assessment. Ever.", "shield", "teal"),
          ("Fix, don't tow", "Towing is the lazy answer. Our vans carry the diagnostics, keys kit and parts to finish the job where you are.", "wrench", ""),
          ("Human on the phone", "A named UK dispatcher owns your callout from first ring to “you're back on the road”.", "users", "teal"),
        ])}
    </div>
  </div>
</section>

<section style="background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)">
  <div class="wrap">
    <div class="grid g2" style="gap:3rem;align-items:start">
      <div class="rv">
        <span class="eyebrow">Our journey</span>
        <h2 style="margin-bottom:2rem">Milestones</h2>
        <div class="timeline">
          {"".join(f'<div class="tl-item"><div class="d">{d}</div><h4>{t}</h4><p>{x}</p></div>' for d, t, x in [
            ("2016", "One van, one promise", "Dan and Chris launch RoadRescue in Birmingham with a single Transit and a fixed-price pledge."),
            ("2018", "Auto locksmith division", "Key cutting and transponder programming added after 1 in 5 calls turned out to be a key problem."),
            ("2020", "Key-worker support", "Free callouts for NHS staff through the pandemic — 4,200 jobs completed at no charge."),
            ("2022", "National network", "Partner model launched; coverage reaches every UK postcode area and Northern Ireland."),
            ("2024", "Live dispatch platform", "GPS matching and WhatsApp status updates cut average arrival time from 41 to 27 minutes."),
            ("2026", "Electrifying the fleet", "First 40 electric service vans on the road; EV and hybrid high-voltage training rolled out network-wide."),
          ])}
        </div>
      </div>
      <div class="rv">
        <div class="card" style="padding:2.2rem">
          <span class="ico">{I['shield']}</span>
          <h3>Accreditations &amp; cover</h3>
          <p style="margin-bottom:1.2rem">We only onboard engineers who can prove their paperwork — and we re-check it every year.</p>
          <ul class="checklist">
            {"".join(f'<li>{I["check"]}<span>{x}</span></li>' for x in [
              "IMI-qualified technicians (Level 3 minimum)",
              "Master Locksmiths Association affiliated locksmiths",
              "£2,000,000 public liability insurance per partner",
              "Enhanced DBS checks on every engineer",
              "IMI Level 3 EV/hybrid high-voltage certification",
              "12-month parts and labour warranty on all work",
              "GDPR-compliant handling of location and vehicle data",
            ])}
          </ul>
        </div>
        <div class="card" style="padding:2.2rem;margin-top:1.4rem" id="careers">
          <span class="ico teal">{I['users']}</span>
          <h3>Join the network</h3>
          <p>Are you a mobile mechanic, auto locksmith or recovery operator with your own van and the right tickets? We supply the jobs, the app and the payments — you keep 80% of every callout, paid weekly.</p>
          <div class="hero-actions" style="margin:1.4rem 0 0">
            <a class="btn btn-primary" href="#" data-wa="Hi, I'd like to join the RoadRescue partner network. My trade and area: " target="_blank" rel="noopener">Apply on WhatsApp</a>
            <a class="btn btn-ghost" href="contact.html">Contact the team</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">The people behind the pager</span>
      <h2>Control room leadership</h2>
    </div>
    <div class="grid g4">
      {"".join(f'''<article class="card rv" style="text-align:center">
        <div class="avatar" style="width:66px;height:66px;font-size:1.3rem;margin:0 auto 1rem">{i}</div>
        <h3 style="font-size:1.05rem">{n}</h3>
        <div style="font-size:.8rem;color:var(--amber);letter-spacing:.08em;text-transform:uppercase;margin:.3rem 0 .7rem">{r}</div>
        <p style="font-size:.88rem">{b}</p>
      </article>''' for i, n, r, b in [
        ("DO", "Dan Okafor", "Co-founder &amp; CEO", "18 years in recovery. Still takes night shifts on the dispatch desk twice a month."),
        ("CR", "Chris Reilly", "Co-founder &amp; Ops", "IMI master technician. Writes the roadside safety standard every partner signs."),
        ("PK", "Priya Kaur", "Head of Dispatch", "Runs the Birmingham control room and the 27-minute arrival target."),
        ("SM", "Stuart McLeod", "Network Quality", "Audits partner paperwork, ratings and complaints. Nothing gets past him."),
      ])}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta-box rv">
      <h2>Broken down right now?</h2>
      <p class="lead" style="max-width:560px;margin:1rem auto 0">Skip the reading. Tell us where you are and we'll do the rest.</p>
      <div class="btns">
        <a class="btn btn-primary btn-lg" href="index.html#finder">{I['pin']} Find nearest mechanic</a>
        <a class="btn btn-wa btn-lg" href="#" data-wa="I need emergency help. My location: " target="_blank" rel="noopener">{I['wa']} WhatsApp SOS</a>
      </div>
    </div>
  </div>
</section>

</main>
"""

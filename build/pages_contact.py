from layout import ICONS as I

REGIONS = ["London", "Manchester", "Birmingham", "Leeds", "Glasgow", "Edinburgh", "Cardiff", "Belfast",
           "Bristol", "Liverpool", "Newcastle", "Sheffield", "Nottingham", "Leicester", "Coventry",
           "Brighton", "Southampton", "Portsmouth", "Plymouth", "Norwich", "Oxford", "Cambridge",
           "Reading", "Milton Keynes", "Aberdeen", "Swansea", "York", "Hull", "Derby", "Stoke-on-Trent",
           "Wolverhampton", "Luton", "Bradford", "Preston", "Watford", "…and every UK postcode area"]

BODY = f"""
<main>

<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow" style="justify-content:center">Contact &amp; callout</span>
    <h1>One message. Help on the way.</h1>
    <p class="lead">The control room answers 24 hours a day, every day of the year. If it's an emergency, call or WhatsApp — the form is for bookings and general enquiries.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="#" data-tel>{I['phone']} <span data-phone-text></span></a>
      <a class="btn btn-wa btn-lg" href="#" data-wa="Emergency! I need help now. My location: " target="_blank" rel="noopener">{I['wa']} WhatsApp SOS</a>
    </div>
    <div class="crumbs"><a href="index.html">Home</a> / <span class="amber">Contact</span></div>
  </div>
</section>

<section style="padding-top:1rem">
  <div class="wrap contact-grid">

    <div class="card rv" style="padding:2.2rem">
      <span class="pill hot">Non-emergency booking</span>
      <h2 style="font-size:1.8rem;margin:1rem 0 .5rem">Request a callout</h2>
      <p style="margin-bottom:1.6rem">Tell us the vehicle and the symptoms. A dispatcher replies within 15 minutes, day or night, with a fixed price and an arrival window.</p>
      <form data-validate class="est-form">
        <div class="grid g2" style="gap:1.1rem">
          <div class="form-row">
            <label for="c-name">Full name *</label>
            <input class="input" id="c-name" name="Name" required placeholder="Alex Morgan">
            <span class="err-txt">Please enter your name.</span>
          </div>
          <div class="form-row">
            <label for="c-phone">Mobile number *</label>
            <input class="input" id="c-phone" name="Phone" required placeholder="07700 900247">
            <span class="err-txt">Please enter a contact number.</span>
          </div>
        </div>
        <div class="grid g2" style="gap:1.1rem">
          <div class="form-row">
            <label for="c-email">Email *</label>
            <input class="input" id="c-email" name="Email" type="email" required placeholder="you@email.co.uk">
            <span class="err-txt">Please enter a valid email.</span>
          </div>
          <div class="form-row">
            <label for="c-postcode">Postcode / location *</label>
            <input class="input" id="c-postcode" name="Location" required placeholder="M4 5AB or “M6 J8 northbound”">
            <span class="err-txt">We need a location to dispatch.</span>
          </div>
        </div>
        <div class="grid g2" style="gap:1.1rem">
          <div class="form-row">
            <label for="c-reg">Vehicle reg</label>
            <input class="input" id="c-reg" name="Registration" placeholder="LM17 DDX">
          </div>
          <div class="form-row">
            <label for="c-service">Service needed</label>
            <select class="input" id="c-service" name="Service">
              <option>Emergency mobile mechanic</option>
              <option>Car key making &amp; programming</option>
              <option>Vehicle lockout / unlocking</option>
              <option>Battery jump start or replacement</option>
              <option>Puncture &amp; tyre replacement</option>
              <option>On-site fault diagnostics</option>
              <option>Wrong fuel drain &amp; flush</option>
              <option>Breakdown recovery &amp; towing</option>
              <option>Fleet or business account</option>
              <option>Join the partner network</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <label>How urgent is it?</label>
          <div class="opt-grid">
            <label class="opt"><input type="radio" name="Urgency" value="Now" checked><span>Right now</span></label>
            <label class="opt"><input type="radio" name="Urgency" value="Today"><span>Later today</span></label>
            <label class="opt"><input type="radio" name="Urgency" value="Scheduled"><span>Book a slot</span></label>
          </div>
        </div>
        <div class="form-row">
          <label for="c-msg">What's happened? *</label>
          <textarea class="input" id="c-msg" name="Details" required placeholder="e.g. Engine turns over but won't start. Dashboard battery light came on yesterday. Car is in a supermarket car park."></textarea>
          <span class="err-txt">Please describe the problem.</span>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:.7rem;align-items:center">
          <button class="btn btn-primary btn-lg" type="submit">Send request</button>
          <a class="btn btn-wa btn-lg" data-form-wa href="#" target="_blank" rel="noopener">{I['wa']} Send on WhatsApp instead</a>
        </div>
        <p class="form-note">By submitting you agree to us contacting you about this callout. We never sell your data. Demo form — no message is actually transmitted.</p>
        <div class="ok-msg">Request received. A dispatcher will call you back within 15 minutes — keep your phone to hand.</div>
      </form>
    </div>

    <aside class="rv">
      <div class="card" style="padding:2rem">
        <span class="pill live"><span class="dot"></span> Control room open now</span>
        <h3 style="margin:1rem 0 .3rem">Reach us directly</h3>
        <div class="ct-item">
          <span class="ico">{I['phone']}</span>
          <div><h4>24/7 emergency line</h4><a href="#" data-tel><strong class="amber" data-phone-text></strong></a><p style="font-size:.8rem">Freephone from UK landlines and mobiles</p></div>
        </div>
        <div class="ct-item">
          <span class="ico teal">{I['wa']}</span>
          <div><h4>WhatsApp dispatch</h4><a href="#" data-wa="Hi RoadRescue 24/7, I need help." target="_blank" rel="noopener">+44 7700 900247</a><p style="font-size:.8rem">Send a pin drop — fastest way to be found</p></div>
        </div>
        <div class="ct-item">
          <span class="ico">{I['mail']}</span>
          <div><h4>Email</h4><a href="mailto:help@roadrescue247.co.uk">help@roadrescue247.co.uk</a><p style="font-size:.8rem">Accounts: billing@roadrescue247.co.uk</p></div>
        </div>
        <div class="ct-item">
          <span class="ico teal">{I['pin']}</span>
          <div><h4>Head office</h4><p>Unit 12, Orbital Park<br>Aston, Birmingham B6 7AA<br>United Kingdom</p></div>
        </div>
        <div class="ct-item">
          <span class="ico">{I['clock']}</span>
          <div><h4>Opening hours</h4><p><strong style="color:var(--teal)">Open 24 hours — 7 days a week</strong><br>Including all bank holidays and Christmas Day</p></div>
        </div>
      </div>

      <div class="card" style="padding:2rem;margin-top:1.4rem">
        <span class="ico">{I['alert']}</span>
        <h3>In a dangerous position?</h3>
        <p style="margin-bottom:1rem">If you are in a live motorway lane, in a collision or someone is injured, <strong style="color:var(--red)">call 999 first</strong>. Then call us and we'll coordinate with the responding officers.</p>
        <a class="btn btn-ghost btn-block" href="tel:999">Call 999</a>
      </div>
    </aside>
  </div>
</section>

<section style="background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)">
  <div class="wrap">
    <div class="section-head center rv">
      <span class="eyebrow">Nationwide coverage</span>
      <h2>Where we operate</h2>
      <p>Every one of the UK's 124 postcode areas, across England, Scotland, Wales and Northern Ireland — motorways, cities, rural roads and airports.</p>
    </div>
    <div class="coverage rv" style="justify-content:center;max-width:900px;margin-inline:auto">
      {"".join(f'<span>{r}</span>' for r in REGIONS)}
    </div>
    <div style="text-align:center;margin-top:2.4rem" class="rv">
      <a class="btn btn-primary btn-lg" href="index.html#finder">{I['pin']} Check units near your postcode</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap" style="max-width:880px">
    <div class="section-head center rv">
      <span class="eyebrow">Before you call</span>
      <h2>Quick answers</h2>
    </div>
    <div data-acc-group class="rv">
      {"".join(f'<div class="acc"><button class="acc-q" type="button">{q}<i>+</i></button><div class="acc-a"><p>{a}</p></div></div>' for q, a in [
        ("How fast can someone actually get to me?", "Our UK-wide average is 27 minutes. In city centres it is often under 20; in the Highlands, mid-Wales or on islands allow up to 90 minutes. You are given a live ETA before you commit."),
        ("What information should I have ready?", "Your location (postcode, what3words or a WhatsApp pin drop), vehicle make, model and registration, and a short description of the symptoms. That is enough for us to send the right van with the right kit."),
        ("Can you come to a car park, driveway or workplace?", "Yes. We attend homes, workplaces, supermarket car parks, multi-storeys (subject to height), service stations and airports as well as roadside and motorway locations."),
        ("Do you charge a fee if you can't fix it?", "You pay the callout and diagnostic fee only. If recovery is then needed, that diagnostic fee is credited against the recovery cost, so you are never charged twice."),
        ("Can I book for a specific time tomorrow?", "Absolutely. Choose “Book a slot” on the form and we'll confirm a two-hour window. Scheduled non-emergency work is charged at the standard daytime rate."),
      ])}
    </div>
  </div>
</section>

</main>
"""

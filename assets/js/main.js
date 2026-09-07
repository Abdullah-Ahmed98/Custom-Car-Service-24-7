/* =========================================================
   RoadRescue 24/7 — site behaviour
   ========================================================= */
(function () {
  "use strict";

  const WHATSAPP = "447700900247";          // demo UK WhatsApp number
  const PHONE = "+448081234247";            // demo UK freephone
  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.prototype.slice.call((c || document).querySelectorAll(s));

  const waLink = (msg) =>
    "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(msg || "Hi RoadRescue 24/7, I need emergency help with my car.");

  /* ---------- year + phone/whatsapp wiring ---------- */
  function wireContacts() {
    $$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
    $$("[data-tel]").forEach((el) => (el.href = "tel:" + PHONE));
    $$("[data-phone-text]").forEach((el) => (el.textContent = "0808 123 4247"));
    $$("[data-wa]").forEach((el) => (el.href = waLink(el.getAttribute("data-wa"))));
  }

  /* ---------- nav ---------- */
  function nav() {
    const bar = $(".nav");
    const burger = $(".burger");
    const menu = $(".mobile-menu");
    if (burger && menu) {
      burger.addEventListener("click", () => {
        burger.classList.toggle("on");
        menu.classList.toggle("open");
      });
      $$("a", menu).forEach((a) =>
        a.addEventListener("click", () => {
          burger.classList.remove("on");
          menu.classList.remove("open");
        })
      );
    }
    const prog = $(".progress");
    const onScroll = () => {
      if (bar) bar.classList.toggle("shrunk", window.scrollY > 40);
      const top = $(".fab-top");
      if (top) top.classList.toggle("show", window.scrollY > 500);
      if (prog) {
        const h = document.documentElement.scrollHeight - window.innerHeight;
        prog.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + "%";
      }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    const top = $(".fab-top");
    if (top) top.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  /* ---------- reveal on scroll ---------- */
  function reveal() {
    const items = $$(".rv");
    if (!("IntersectionObserver" in window)) return items.forEach((i) => i.classList.add("in"));
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e, i) => {
          if (e.isIntersecting) {
            setTimeout(() => e.target.classList.add("in"), (parseInt(e.target.dataset.delay || 0, 10)) || i * 70);
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px" }
    );
    items.forEach((i) => io.observe(i));
  }

  /* ---------- card spotlight ---------- */
  function spotlight() {
    $$(".card").forEach((c) => {
      c.addEventListener("mousemove", (e) => {
        const r = c.getBoundingClientRect();
        c.style.setProperty("--mx", e.clientX - r.left + "px");
        c.style.setProperty("--my", e.clientY - r.top + "px");
      });
    });
  }

  /* ---------- counters ---------- */
  function counters() {
    const els = $$("[data-count]");
    if (!els.length || !("IntersectionObserver" in window)) return;
    const io = new IntersectionObserver((es) => {
      es.forEach((e) => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const end = parseFloat(el.dataset.count);
        const suffix = el.dataset.suffix || "";
        const dec = (el.dataset.count.split(".")[1] || "").length;
        let t0 = null;
        const step = (ts) => {
          if (!t0) t0 = ts;
          const p = Math.min((ts - t0) / 1600, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = (end * eased).toFixed(dec) + suffix;
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        io.unobserve(el);
      });
    }, { threshold: 0.5 });
    els.forEach((el) => io.observe(el));
  }

  /* ---------- accordion ---------- */
  function accordion() {
    $$(".acc-q").forEach((q) => {
      q.addEventListener("click", () => {
        const acc = q.parentElement;
        const body = $(".acc-a", acc);
        const open = acc.classList.contains("open");
        const group = acc.closest("[data-acc-group]");
        if (group) {
          $$(".acc.open", group).forEach((o) => {
            o.classList.remove("open");
            $(".acc-a", o).style.maxHeight = null;
          });
        }
        if (!open) {
          acc.classList.add("open");
          body.style.maxHeight = body.scrollHeight + "px";
        }
      });
    });
  }

  /* ---------- SOS dock panel ---------- */
  function sos() {
    const btn = $(".fab-wa");
    const panel = $(".sos-panel");
    if (!panel || !btn) return;
    let choice = "";
    btn.addEventListener("click", (e) => {
      if (!panel.classList.contains("open")) {
        e.preventDefault();
        panel.classList.add("open");
      }
    });
    $$(".sos-quick button", panel).forEach((b) => {
      b.addEventListener("click", () => {
        $$(".sos-quick button", panel).forEach((x) => x.classList.remove("on"));
        b.classList.add("on");
        choice = b.textContent.trim();
        const go = $("[data-sos-go]", panel);
        go.href = waLink("Hi RoadRescue 24/7 — EMERGENCY: " + choice + ". My location: ");
      });
    });
    $("[data-sos-close]", panel).addEventListener("click", () => panel.classList.remove("open"));
    document.addEventListener("click", (e) => {
      if (!panel.contains(e.target) && !btn.contains(e.target)) panel.classList.remove("open");
    });
  }

  /* ---------- forms ---------- */
  function forms() {
    $$("form[data-validate]").forEach((form) => {
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        let ok = true;
        $$("[required]", form).forEach((f) => {
          const bad = !f.value.trim() || (f.type === "email" && !/^\S+@\S+\.\S+$/.test(f.value));
          f.classList.toggle("err", bad);
          const msg = f.parentElement.querySelector(".err-txt");
          if (msg) msg.classList.toggle("show", bad);
          if (bad) ok = false;
        });
        if (!ok) return;
        const done = $(".ok-msg", form);
        if (done) {
          done.classList.add("show");
          done.scrollIntoView({ behavior: "smooth", block: "center" });
        }
        // Also offer a WhatsApp handoff with the message pre-filled
        const wa = $("[data-form-wa]", form);
        if (wa) {
          const d = new FormData(form);
          let txt = "New enquiry via website:\n";
          d.forEach((v, k) => { if (v) txt += "• " + k + ": " + v + "\n"; });
          wa.href = waLink(txt);
        }
        form.reset();
      });
      $$("[required]", form).forEach((f) =>
        f.addEventListener("input", () => {
          f.classList.remove("err");
          const m = f.parentElement.querySelector(".err-txt");
          if (m) m.classList.remove("show");
        })
      );
    });
  }

  /* ---------- news filters ---------- */
  function newsFilter() {
    const btns = $$(".filter");
    if (!btns.length) return;
    btns.forEach((b) =>
      b.addEventListener("click", () => {
        btns.forEach((x) => x.classList.remove("on"));
        b.classList.add("on");
        const k = b.dataset.filter;
        $$("[data-cat]").forEach((card) => {
          const show = k === "all" || card.dataset.cat === k;
          card.style.display = show ? "" : "none";
        });
      })
    );
  }

  /* ---------- price estimator ---------- */
  function estimator() {
    const form = $("#estimator");
    if (!form) return;
    const out = {
      total: $("#est-total"),
      base: $("#est-base"),
      time: $("#est-time"),
      dist: $("#est-dist"),
      eta: $("#est-eta")
    };
    const calc = () => {
      const svc = SERVICE_CATALOGUE.find((s) => s.key === form.service.value) || SERVICE_CATALOGUE[0];
      const timeMul = form.timeslot.value === "night" ? 1.35 : form.timeslot.value === "weekend" ? 1.15 : 1;
      const miles = parseInt(form.distance.value, 10) || 0;
      const distFee = Math.max(0, miles - 5) * 1.6;
      const total = svc.from * timeMul + distFee;
      out.base.textContent = "£" + svc.from.toFixed(2);
      out.time.textContent = "×" + timeMul.toFixed(2);
      out.dist.textContent = "£" + distFee.toFixed(2);
      out.eta.textContent = svc.eta;
      out.total.textContent = "£" + total.toFixed(0);
      const wa = $("[data-est-wa]");
      if (wa) wa.href = waLink("Hi, I'd like to book: " + svc.name + " (" + form.timeslot.value + ", ~" + miles + " miles). Estimated £" + total.toFixed(0) + ".");
      const rng = $("#dist-out");
      if (rng) rng.textContent = miles + " mi";
    };
    form.addEventListener("input", calc);
    form.addEventListener("change", calc);
    calc();
  }

  /* ---------- mechanic finder ---------- */
  function finder() {
    const root = $("#finder");
    if (!root || typeof UK_MECHANICS === "undefined") return;

    const listEl = $("#mech-list");
    const input = $("#loc-input");
    const svcSel = $("#svc-select");
    const goBtn = $("#find-btn");
    const geoBtn = $("#geo-btn");
    const statusEl = $("#find-status");

    let map, markers = [], meMarker, origin = [51.5074, -0.1278];

    function haversine(a, b, c, d) {
      const R = 3958.8, dLat = ((c - a) * Math.PI) / 180, dLon = ((d - b) * Math.PI) / 180;
      const x = Math.sin(dLat / 2) ** 2 + Math.cos((a * Math.PI) / 180) * Math.cos((c * Math.PI) / 180) * Math.sin(dLon / 2) ** 2;
      return R * 2 * Math.atan2(Math.sqrt(x), Math.sqrt(1 - x));
    }

    function resolve(q) {
      const t = (q || "").trim().toLowerCase();
      if (!t) return null;
      if (UK_PLACES[t]) return UK_PLACES[t];
      for (const k in UK_PLACES) if (k.indexOf(t) === 0 || t.indexOf(k) === 0) return UK_PLACES[k];
      const pc = t.toUpperCase().replace(/[^A-Z0-9]/g, "");
      const m = pc.match(/^([A-Z]{1,2})\d/);
      if (m && UK_POSTCODE_AREAS[m[1]]) return UK_POSTCODE_AREAS[m[1]];
      return null;
    }

    function initMap() {
      if (map || typeof L === "undefined") return;
      map = L.map("map", { zoomControl: true, scrollWheelZoom: false }).setView(origin, 11);
      L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {
        attribution: '&copy; OpenStreetMap &copy; CARTO',
        maxZoom: 19
      }).addTo(map);
      map.on("click", () => map.scrollWheelZoom.enable());
      map.on("mouseout", () => map.scrollWheelZoom.disable());
    }

    function pin(cls, label) {
      return L.divIcon({
        className: "",
        html: '<div class="map-pin ' + cls + '"><b>' + label + "</b></div>",
        iconSize: [30, 30],
        iconAnchor: [15, 30]
      });
    }

    function render(list) {
      listEl.innerHTML = "";
      if (!list.length) {
        listEl.innerHTML = '<div class="finder-empty">No partners match that filter yet — we still cover you. Tap WhatsApp and our dispatcher will assign the nearest available unit.</div>';
        return;
      }
      list.forEach((m, i) => {
        const el = document.createElement("article");
        el.className = "mech";
        el.innerHTML =
          '<div class="mech-row"><div><h4>' + m.name + "</h4>" +
          '<div class="stars">' + "★".repeat(Math.round(m.rating)) + ' <span style="color:var(--muted-dim)">' + m.rating.toFixed(1) + " (" + m.reviews + ")</span></div>" +
          '</div><div class="dist">' + m.distance.toFixed(1) + " mi</div></div>" +
          '<div class="meta"><span>📍 ' + m.area + ", " + m.city + "</span><span>⏱ ETA " + (m.eta + Math.round(m.distance * 1.4)) + " min</span><span class=\"tealtx\">● Open 24/7</span></div>" +
          '<div class="tags">' + m.tags.map((t) => '<span class="tag">' + t + "</span>").join("") + "</div>" +
          '<div class="mech-actions">' +
          '<a class="btn btn-primary btn-sm" href="tel:' + m.phone + '">Call now</a>' +
          '<a class="btn btn-wa btn-sm" target="_blank" rel="noopener" href="' + waLink("Hi, please dispatch " + m.name + " (" + m.area + ") to me. Issue: ") + '">WhatsApp</a>' +
          "</div>";
        el.addEventListener("click", () => {
          $$(".mech", listEl).forEach((x) => x.classList.remove("sel"));
          el.classList.add("sel");
          if (map && markers[i]) {
            map.setView([m.lat, m.lng], 13, { animate: true });
            markers[i].openPopup();
          }
        });
        listEl.appendChild(el);
      });
    }

    function search(coords, label) {
      origin = coords;
      const svc = svcSel.value;
      let list = UK_MECHANICS.map((m) => Object.assign({}, m, { distance: haversine(coords[0], coords[1], m.lat, m.lng) }));
      if (svc !== "all") {
        const map4 = {
          mechanic: ["Mobile Mechanic", "Engine", "Clutch", "Brakes", "Suspension", "MOT Repairs", "Cooling", "Night Callout"],
          keys: ["Car Keys", "Key Programming", "Spare Keys", "Immobiliser"],
          lockout: ["Lockout", "Car Keys"],
          battery: ["Battery", "Jump Start", "Electrical"],
          tyre: ["Tyres"],
          diagnostic: ["Diagnostics", "ECU", "Electrical"],
          fuel: ["Fuel Drain"],
          recovery: ["Recovery"]
        }[svc] || [];
        list = list.filter((m) => m.tags.some((t) => map4.indexOf(t) > -1));
      }
      list.sort((a, b) => a.distance - b.distance);
      list = list.slice(0, 8);
      render(list);
      statusEl.innerHTML = list.length
        ? '<span class="dot"></span> ' + list.length + " units available near <b>" + label + "</b> · dispatching 24/7"
        : '<span class="dot"></span> Searching wider network near <b>' + label + "</b>";

      initMap();
      if (!map) return;
      markers.forEach((mk) => map.removeLayer(mk));
      markers = [];
      if (meMarker) map.removeLayer(meMarker);
      meMarker = L.marker(coords, { icon: pin("me", "•") }).addTo(map).bindPopup("<b>You</b><br>" + label);
      const bounds = [coords];
      list.forEach((m, i) => {
        const mk = L.marker([m.lat, m.lng], { icon: pin("", i + 1) })
          .addTo(map)
          .bindPopup("<b>" + m.name + "</b><br>" + m.area + ", " + m.city + "<br>" + m.distance.toFixed(1) + " mi · ★ " + m.rating + '<br><a style="color:var(--teal)" href="tel:' + m.phone + '">Call now</a>');
        markers.push(mk);
        bounds.push([m.lat, m.lng]);
      });
      map.fitBounds(bounds, { padding: [45, 45], maxZoom: 13 });
    }

    goBtn.addEventListener("click", () => {
      const c = resolve(input.value);
      if (!c) {
        statusEl.innerHTML = '<span style="color:var(--red)">Enter a UK town or postcode (e.g. Manchester or M4 5AB)</span>';
        input.classList.add("err");
        setTimeout(() => input.classList.remove("err"), 1600);
        return;
      }
      search(c, input.value.trim().toUpperCase());
    });
    input.addEventListener("keydown", (e) => { if (e.key === "Enter") goBtn.click(); });
    svcSel.addEventListener("change", () => search(origin, input.value.trim() || "your area"));

    geoBtn.addEventListener("click", () => {
      if (!navigator.geolocation) return;
      statusEl.innerHTML = '<span class="dot"></span> Locating you…';
      navigator.geolocation.getCurrentPosition(
        (p) => { input.value = "My location"; search([p.coords.latitude, p.coords.longitude], "your GPS location"); },
        () => { statusEl.innerHTML = '<span style="color:var(--red)">Location blocked — type your postcode instead.</span>'; },
        { timeout: 8000 }
      );
    });

    search(origin, "London");
  }

  document.addEventListener("DOMContentLoaded", function () {
    wireContacts(); nav(); reveal(); spotlight(); counters();
    accordion(); sos(); forms(); newsFilter(); estimator(); finder();
  });
})();

/* Clinical Foresight — site behaviour (vanilla JS, no dependencies) */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Sticky header state */
  var header = document.querySelector(".header");
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Mobile navigation */
  var toggle = document.querySelector(".nav__toggle");
  var mobile = document.querySelector(".nav__mobile");
  if (toggle && mobile) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      mobile.classList.toggle("is-open", !open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        toggle.setAttribute("aria-expanded", "false");
        mobile.classList.remove("is-open");
        toggle.focus();
      }
    });
  }

  /* Scroll reveal */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); en.target.classList.remove("reveal--pending"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    var fold = window.innerHeight * 1.1;
    revealEls.forEach(function (el) {
      /* Only elements that start below the fold animate in; everything on screen at load is visible at rest. */
      if (el.getBoundingClientRect().top > fold) { el.classList.add("reveal--pending"); io.observe(el); }
    });
    /* Safety net: never leave content hidden */
    setTimeout(function () { revealEls.forEach(function (el) { el.classList.remove("reveal--pending"); el.classList.add("is-visible"); }); }, 2000);
  }

  /* Hero: constellation of clinical signals, one of which is "the finding" */
  var canvas = document.getElementById("hero-canvas");
  if (canvas && canvas.getContext) {
    var ctx = canvas.getContext("2d");
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W, H, nodes = [], hot = 0, t = 0;
    var seed = 7;
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    function size() {
      var r = canvas.parentElement.getBoundingClientRect();
      W = r.width; H = r.height;
      canvas.width = W * dpr; canvas.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      nodes = [];
      var count = Math.round(Math.min(90, Math.max(36, W / 16)));
      for (var i = 0; i < count; i++) {
        nodes.push({ x: rnd() * W, y: rnd() * H, r: 1 + rnd() * 1.8, vx: (rnd() - 0.5) * 0.08, vy: (rnd() - 0.5) * 0.08, p: rnd() * Math.PI * 2 });
      }
      hot = Math.floor(count * 0.62);
      nodes[hot].x = W * 0.68; nodes[hot].y = H * 0.42; nodes[hot].r = 3;
    }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      /* faint grid */
      ctx.strokeStyle = "rgba(255,255,255,0.035)"; ctx.lineWidth = 1;
      for (var gx = 0; gx < W; gx += 64) { ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, H); ctx.stroke(); }
      for (var gy = 0; gy < H; gy += 64) { ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke(); }
      /* links */
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j]; var dx = a.x - b.x, dy = a.y - b.y; var d = Math.sqrt(dx * dx + dy * dy);
          if (d < 150) {
            var al = (1 - d / 150) * 0.22;
            ctx.strokeStyle = (i === hot || j === hot) ? "rgba(94,209,197," + (al * 2.2) + ")" : "rgba(255,255,255," + al + ")";
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
      }
      /* nodes */
      for (var k = 0; k < nodes.length; k++) {
        var n = nodes[k];
        if (k === hot) {
          var pulse = 10 + Math.sin(t * 0.04) * 6;
          ctx.beginPath(); ctx.arc(n.x, n.y, pulse + 8, 0, Math.PI * 2); ctx.fillStyle = "rgba(94,209,197,0.06)"; ctx.fill();
          ctx.beginPath(); ctx.arc(n.x, n.y, pulse, 0, Math.PI * 2); ctx.strokeStyle = "rgba(94,209,197,0.35)"; ctx.stroke();
          ctx.beginPath(); ctx.arc(n.x, n.y, 3.5, 0, Math.PI * 2); ctx.fillStyle = "#5ED1C5"; ctx.fill();
        } else {
          var tw = 0.35 + 0.25 * Math.sin(t * 0.02 + n.p);
          ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2); ctx.fillStyle = "rgba(255,255,255," + tw + ")"; ctx.fill();
        }
        if (!reduced) { n.x += n.vx; n.y += n.vy; if (n.x < 0 || n.x > W) n.vx *= -1; if (n.y < 0 || n.y > H) n.vy *= -1; }
      }
      t++;
      if (!reduced) requestAnimationFrame(draw);
    }
    size(); draw();
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { size(); if (reduced) draw(); }, 150); });
  }

  /* Contact form: client-side validation and graceful handling */
  var form = document.getElementById("contact-form");
  if (form) {
    var note = document.getElementById("form-status");
    form.addEventListener("submit", function (e) {
      if (!form.checkValidity()) { e.preventDefault(); form.reportValidity(); return; }
      if (form.dataset.endpoint && form.dataset.endpoint.indexOf("YOUR_FORM_ID") === -1) {
        /* Real endpoint configured (e.g. Formspree): let the browser submit normally. */
        return;
      }
      /* No endpoint configured yet: build a pre-filled email as a fallback. */
      e.preventDefault();
      var f = new FormData(form);
      var subject = encodeURIComponent("[" + f.get("interest") + "] " + f.get("organization"));
      var body = encodeURIComponent(
        "Name: " + f.get("name") + "\nTitle: " + f.get("title") + "\nOrganization: " + f.get("organization") +
        "\nEmail: " + f.get("email") + "\nInterest: " + f.get("interest") + "\n\n" + f.get("message"));
      window.location.href = "mailto:DrFrancis@clinicalforesight.ai?subject=" + subject + "&body=" + body;
      if (note) note.textContent = "Opening your email client. If nothing happens, email DrFrancis@clinicalforesight.ai directly.";
    });
  }

  /* Copy email buttons */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy"); var orig = btn.textContent;
      function done() { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = orig; }, 1800); }
      if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(text).then(done).catch(function () { window.prompt("Copy this address:", text); }); }
      else { window.prompt("Copy this address:", text); }
    });
  });

  /* Footer year */
  var y = document.getElementById("year"); if (y) y.textContent = new Date().getFullYear();
})();

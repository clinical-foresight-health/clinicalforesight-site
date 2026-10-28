#!/usr/bin/env python3
"""Assembles the five Clinical Foresight pages from shared header/footer templates.
Run: python3 build.py   (writes *.html next to this file)
Edit the page bodies below or the generated HTML directly — both work."""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://www.clinicalforesight.ai"
EMAIL = "DrFrancis@clinicalforesight.ai"

NAV = [
    ("index.html", "Home"),
    ("ai-hospitalist.html", "AI Hospitalist"),
    ("autonomous-cdi.html", "Autonomous CDI"),
    ("about.html", "Vision"),
    ("contact.html", "Partnerships"),
]

MARK = """<svg class="brand__mark" viewBox="0 0 32 32" aria-hidden="true" fill="none">
  <rect x="1.5" y="1.5" width="29" height="29" rx="8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 19 L12 13 L15.5 17 L19 10 L24 19" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="19" cy="10" r="2.6" fill="#0F9D93"/>
</svg>"""

ARROW = '<svg class="arrow" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h9M8 3.5 12.5 8 8 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHECK = '<svg viewBox="0 0 18 18" aria-hidden="true" fill="none"><path d="M3.5 9.5 7 13l7.5-8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DASH = '<svg viewBox="0 0 18 18" aria-hidden="true" fill="none"><path d="M4 9h10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'


def head(title, desc, path, dark=False):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if path == 'index.html' else path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Clinical Foresight">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{'' if path == 'index.html' else path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1B33">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400;1,8..60,500&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/styles.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Clinical Foresight","url":"{SITE}","email":"{EMAIL}","founder":{{"@type":"Person","name":"Daniel Francis","jobTitle":"Physician-Founder"}},"description":"Physician-founded healthcare AI company developing clinical decision support, patient safety, and Clinical Documentation Integrity (CDI) automation for hospitals."}}
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="header{' header--dark' if dark else ''}">
  <div class="container">
    <nav class="nav" aria-label="Primary">
      <a class="brand" href="index.html" aria-label="Clinical Foresight home">{MARK}<span>Clinical Foresight</span></a>
      <ul class="nav__links">
{''.join(f'        <li><a href="{h}"{' aria-current="page"' if h == path else ''}>{l}</a></li>' + chr(10) for h, l in NAV[1:])}      </ul>
      <a class="btn btn--primary nav__cta" href="contact.html">Explore a Partnership</a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu"><span></span></button>
    </nav>
  </div>
  <div class="nav__mobile" id="mobile-nav">
    <div class="container">
      <ul>
{''.join(f'        <li><a href="{h}"{' aria-current="page"' if h == path else ''}>{l}</a></li>' + chr(10) for h, l in NAV)}      </ul>
      <a class="btn btn--primary" href="contact.html">Explore a Partnership</a>
    </div>
  </div>
</header>
<main id="main">
"""


FOOTER = f"""</main>
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <a class="brand" href="index.html">{MARK}<span>Clinical Foresight</span></a>
        <p class="footer__tag">Better Clinical Decisions. Better Documentation. Better Patient Care.</p>
        <p class="small" style="color:rgba(255,255,255,0.55)">Physician-founded healthcare AI for clinical decision support, patient safety, and Clinical Documentation Integrity.</p>
      </div>
      <div>
        <h4>Platform</h4>
        <ul>
          <li><a href="ai-hospitalist.html">AI Hospitalist + Prospective CDI</a></li>
          <li><a href="autonomous-cdi.html">Autonomous Retrospective CDI</a></li>
          <li><a href="index.html#together">How they work together</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">Our vision</a></li>
          <li><a href="about.html#founder">Physician-founder</a></li>
          <li><a href="contact.html">Partnerships</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="contact.html#demo">Request a demonstration</a></li>
          <li><a href="contact.html#investors">Investor inquiries</a></li>
        </ul>
      </div>
    </div>
    <p class="footer__legal">Clinical Foresight is under active development. Descriptions of planned integrations, automated query transmission, coding, and revenue-cycle workflows are forward-looking and subject to validation, institutional authorization, and regulatory requirements. The platform is not yet deployed in production hospital or EHR environments, and no claim of clinical efficacy or financial outcome is made. All interface examples use synthetic data; no patient information is shown. Clinical judgment, treatment decisions, and final documentation remain the responsibility of the treating physician.</p>
    <div class="footer__bottom">
      <span>&copy; <span id="year">2026</span> Clinical Foresight. All rights reserved.</span>
      <span>clinicalforesight.ai</span>
    </div>
  </div>
</footer>
<script src="assets/main.js" defer></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# HOME
# --------------------------------------------------------------------------
HOME = f"""
<!-- HERO -->
<section class="hero band">
  <div class="hero__canvas" aria-hidden="true"><canvas id="hero-canvas"></canvas></div>
  <div class="hero__fade" aria-hidden="true"></div>
  <div class="container">
    <div class="hero__inner">
      <p class="eyebrow">Physician-founded healthcare AI</p>
      <h1>What if the most important clinical finding was <em>the one no one noticed?</em></h1>
      <p class="lede">Clinical Foresight helps physicians recognize what matters in complex medical records, before the next clinical decision or note is finalized. One platform for clinical safety, prospective Clinical Documentation Integrity, and a path toward autonomous CDI.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Explore a Partnership {ARROW}</a>
        <a class="btn btn--ghost" href="contact.html#demo">Request a Demonstration</a>
      </div>
      <ul class="hero__meta" aria-label="At a glance">
        <li>Built by a practicing hospitalist</li>
        <li>Prospective and retrospective CDI</li>
        <li>Designed for Epic via SMART on FHIR</li>
        <li>Physician remains in control</li>
      </ul>
    </div>
  </div>
</section>

<!-- TAGLINE STRIP -->
<div class="strip">
  <div class="container">
    <p class="strip__inner"><span>Better Clinical Decisions.</span><span>Better Documentation.</span><span>Better Patient Care.</span></p>
  </div>
</div>

<!-- THE PROBLEM -->
<section class="section">
  <div class="container">
    <div class="split">
      <div class="stack stack--lg reveal">
        <p class="eyebrow">The premise</p>
        <h2>Important clinical information is buried in records that keep getting more complex.</h2>
        <p class="lede">Physicians make high-stakes decisions under real time pressure, across admission notes, histories, medication lists, labs, imaging, and specialist recommendations. Traditional CDI arrives afterward and reviews what was written. Clinical Foresight is built to work before the note is signed.</p>
        <ul class="contact-list">
          <li>Reviews longitudinal clinical information, not isolated documentation or code matching.</li>
          <li>Integrates patient safety and prospective CDI in a single physician-facing workflow.</li>
          <li>Built around evidence-supported recommendations, explainable findings, and physician judgment.</li>
        </ul>
      </div>
      <div class="reveal" data-delay="1">
        <!-- Interface mockup: SYNTHETIC data only -->
        <div class="mock" role="img" aria-label="Illustrative pre-rounding review panel with synthetic patient data showing a critical finding, a medication review item, and a documentation specificity opportunity.">
          <div class="mock__bar">
            <div class="mock__title"><span class="dot"></span> Pre-rounding review</div>
            <span class="mono">Synthetic patient · Sandbox</span>
          </div>
          <div class="mock__body">
            <div class="mock__aside">
              <dl>
                <dt>Patient</dt><dd>Test, Synthetic A.</dd>
                <dt>Age</dt><dd>71</dd>
                <dt>Day</dt><dd>Hospital day 3</dd>
                <dt>Admit dx</dt><dd>Community-acquired pneumonia</dd>
                <dt>Sources</dt><dd>H&amp;P, 2 progress notes, 38 lab results, MAR, chest imaging</dd>
              </dl>
            </div>
            <div class="mock__main">
              <div class="finding">
                <span class="finding__sev finding__sev--critical" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Rising creatinine not addressed in plan</strong><span class="chip">Safety</span></div>
                  <p>Creatinine 1.1 → 1.6 → 2.0 mg/dL over 48 h. Progress note plan unchanged. Vancomycin trough pending; last dose given 6 h ago.</p>
                  <p class="finding__q">Ask: urine output trend, contrast exposure, nephrotoxic agents. Consider documenting acute kidney injury if criteria are met.</p>
                </div>
              </div>
              <div class="finding">
                <span class="finding__sev finding__sev--review" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Home anticoagulant not resumed</strong><span class="chip">Medication</span></div>
                  <p>Apixaban listed on home medications; held on admission. No order and no documented rationale since day 1.</p>
                </div>
              </div>
              <div class="finding">
                <span class="finding__sev finding__sev--cdi" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Documented "respiratory failure" lacks acuity and type</strong><span class="chip">CDI</span></div>
                  <p>O₂ 4 L NC, RR 26, pCO₂ normal on day-1 gas. Clinical evidence may support a more specific diagnosis if the physician agrees.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="mock__foot">
            <span>3 findings for physician review · 0 actions taken by the system</span>
            <span class="chip">Physician decides</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TWO PATHWAYS -->
<section class="section section--mist" id="products">
  <div class="container">
    <div class="sec-head sec-head--center reveal">
      <p class="eyebrow">Two products. One clinical foundation.</p>
      <h2>Fix documentation at the point of care, and automate what still needs fixing afterward.</h2>
      <p class="lede">Each product is independently valuable. Together they form a strategy for safer care, fewer preventable documentation gaps, and a progressively automated CDI operation.</p>
    </div>
    <div class="pathway">
      <a class="pathway__card pathway__card--ink reveal" href="ai-hospitalist.html">
        <p class="eyebrow">Product one · Prospective</p>
        <h3>AI Hospitalist + Prospective CDI</h3>
        <p>Clinical intelligence at the point of care. Safety surveillance, decision support, and documentation review that accompany the physician from pre-rounding through note finalization.</p>
        <ul>
          <li>Surfaces overlooked conditions, medication concerns, and unanswered questions</li>
          <li>Suggests high-value questions to investigate at the bedside</li>
          <li>Combined safety and CDI check before every note is signed</li>
        </ul>
        <span class="card__more">Explore the physician workflow {ARROW}</span>
      </a>
      <a class="pathway__card reveal" data-delay="1" href="autonomous-cdi.html">
        <p class="eyebrow">Product two · Retrospective</p>
        <h3>Autonomous Retrospective CDI</h3>
        <p>From manual chart review to intelligent automation. Screens inpatient records against clinical evidence, identifies documentation gaps, and prepares compliant physician queries.</p>
        <ul>
          <li>Deterministic CMS CC/MCC and MS-DRG reference logic</li>
          <li>Three-phase path from reviewer-assisted to autonomous workflows</li>
          <li>Human oversight concentrated on exceptions</li>
        </ul>
        <span class="card__more">See the automation pathway {ARROW}</span>
      </a>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section class="section band">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Built around how hospitalists actually work</p>
      <h2>Three moments in the day. One continuous clinical review.</h2>
      <p class="lede">The review follows the physician through the hospitalization rather than arriving as a query days later.</p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <span class="step__n">01 · BEFORE ROUNDING</span>
        <h3>Review the record, surface what's easy to miss</h3>
        <p>The AI reads available admission documentation, histories, medications, labs, studies, and specialist notes. It flags potentially overlooked safety concerns and proposes high-value questions for the encounter.</p>
      </div>
      <div class="step reveal" data-delay="1">
        <span class="step__n">02 · AFTER ROUNDING</span>
        <h3>Integrate what the physician learned</h3>
        <p>The physician adds updated history, exam findings, and decisions. The system folds that into its assessment and raises further questions or concerns where appropriate.</p>
      </div>
      <div class="step reveal" data-delay="2">
        <span class="step__n">03 · BEFORE THE NOTE IS SIGNED</span>
        <h3>Combined safety and CDI review</h3>
        <p>A final pass identifies issues that warrant attention and opportunities to document supported diagnoses more precisely. The physician reviews, decides, and signs.</p>
      </div>
    </div>
    <div class="status reveal" style="margin-top:48px">
      <strong>Product stage</strong>
      <p>Clinical Foresight is in prototype and integration development. A read-only Epic SMART on FHIR connection has retrieved synthetic sandbox patients; the physician-authored clinical engines are being integrated. The platform is not yet deployed in production hospital environments, and clinical effectiveness has not yet been validated.</p>
    </div>
  </div>
</section>

<!-- TOGETHER -->
<section class="section" id="together">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">How the products work together</p>
      <h2>Get documentation right the first time. Automate the rest.</h2>
    </div>
    <div class="compare">
      <div class="compare__col compare__col--now reveal">
        <p class="eyebrow">Traditional CDI today</p>
        <h3>Review after the fact</h3>
        <ul>
          <li>{DASH}<span>Charts are read by hand, after documentation is complete.</span></li>
          <li>{DASH}<span>Queries reach physicians days later, out of clinical context.</span></li>
          <li>{DASH}<span>Safety and documentation are handled by separate teams and tools.</span></li>
          <li>{DASH}<span>Cost scales with headcount; consistency depends on the reviewer.</span></li>
        </ul>
      </div>
      <div class="compare__col compare__col--next reveal" data-delay="1">
        <p class="eyebrow">With Clinical Foresight</p>
        <h3>Prospective clarity, then intelligent automation</h3>
        <ul>
          <li>{CHECK}<span>The AI Hospitalist resolves documentation gaps while the physician is treating the patient.</span></li>
          <li>{CHECK}<span>Retrospective CDI screens what remains and prepares compliant queries.</span></li>
          <li>{CHECK}<span>One clinical evidence foundation serves both workflows.</span></li>
          <li>{CHECK}<span>Long-term: retrospective correction becomes increasingly unnecessary.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- DIFFERENTIATORS -->
<section class="section section--mist">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Why it's different</p>
      <h2>Technology shaped by the realities of practicing medicine.</h2>
    </div>
    <div class="features">
      <div class="feature reveal"><h4>Developed from real clinical practice</h4><p>Grown from a physician-developed AI Hospitalist workflow refined through daily use, not designed around administrative processes.</p></div>
      <div class="feature reveal" data-delay="1"><h4>Longitudinal, not isolated</h4><p>Reviews the full clinical story across the stay rather than matching codes against single documents.</p></div>
      <div class="feature reveal" data-delay="2"><h4>Safety and CDI in one workflow</h4><p>Medication, diagnostic, and treatment concerns surface alongside documentation opportunities, in a single physician-facing view.</p></div>
      <div class="feature reveal"><h4>Standards-based integration</h4><p>Designed for hospital EHRs, including Epic, through SMART on FHIR interfaces. Read-only by design today.</p></div>
      <div class="feature reveal" data-delay="1"><h4>Explainable findings</h4><p>Every item cites the clinical evidence behind it, so the physician can evaluate and decide quickly.</p></div>
      <div class="feature reveal" data-delay="2"><h4>Progressive autonomy</h4><p>A deliberate path from reviewer-assisted CDI to automated queries, coding support, and downstream revenue-cycle preparation.</p></div>
    </div>
  </div>
</section>

<!-- FOUNDER -->
<section class="section">
  <div class="container">
    <div class="founder">
      <div class="founder__portrait reveal" aria-hidden="true">
        <span class="mono">Dr. Daniel Francis · Physician-Founder</span>
      </div>
      <div class="stack stack--lg reveal" data-delay="1">
        <p class="eyebrow">Built from the bedside outward</p>
        <p class="founder__quote">Clinically consequential details and documentation opportunities get missed, even by experienced clinicians, when the information is dispersed across the record. Bring another layer of clinical intelligence into the moment the physician reviews the patient and finalizes the note.</p>
        <div class="founder__name">
          <strong>Dr. Daniel Francis</strong>
          <span class="small">Physician-Founder · 28 years in medicine, 15 in hospital medicine</span>
        </div>
        <a class="btn btn--ghost" href="about.html">Read the founder story {ARROW}</a>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="section band">
  <div class="container">
    <div class="cta reveal">
      <p class="eyebrow">Health systems · Technology partners · Investors</p>
      <h2>Let's talk about what your organization could do with prospective CDI.</h2>
      <p class="lede center">Initial conversations and demonstrations use synthetic data. Any real-patient pilot requires separate institutional authorization, security review, and clinical evaluation.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Explore a Partnership {ARROW}</a>
        <a class="btn btn--ghost" href="contact.html#demo">Request a Demonstration</a>
      </div>
      <a class="cta__email" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# AI HOSPITALIST
# --------------------------------------------------------------------------
HOSPITALIST = f"""
<section class="page-hero band">
  <div class="container">
    <div class="page-hero__inner">
      <p class="eyebrow">Product one · AI Hospitalist + Prospective CDI</p>
      <h1>Clinical intelligence at the point of care.</h1>
      <p class="lede">Clinical safety surveillance, AI-assisted decision support, and prospective Clinical Documentation Integrity in one physician workflow, from pre-rounding through the signed note.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html#demo">Request a Demonstration {ARROW}</a>
        <a class="btn btn--ghost" href="contact.html">Explore a Partnership</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="stack stack--lg reveal">
        <p class="eyebrow">What it does</p>
        <h2>A second clinical reader that never loses the thread.</h2>
        <p class="lede">The system analyzes available clinical records: admission documentation, medical histories, medications, laboratory results, diagnostic studies, specialist recommendations, and daily clinical changes.</p>
        <p>It identifies potentially overlooked clinical conditions, medication-related concerns, treatment inconsistencies, important unanswered clinical questions, and opportunities to improve diagnostic specificity. Its review accompanies the physician throughout the hospitalization.</p>
      </div>
      <div class="grid grid--2 reveal" data-delay="1">
        <div class="card">
          <div class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 7v5c0 5 3.5 8.5 8 9 4.5-.5 8-4 8-9V7l-8-4Z"/><path d="m9 12 2 2 4-4"/></svg></div>
          <h4>Clinical safety</h4>
          <p class="small">Overlooked chart information, medication discrepancies, potential contraindications, and clinically relevant questions for physician assessment.</p>
        </div>
        <div class="card">
          <div class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l5 5v13H6z"/><path d="M14 3v6h6M9 13h7M9 17h5"/></svg></div>
          <h4>Prospective CDI</h4>
          <p class="small">Clinically supported opportunities for diagnostic specificity, severity documentation, and potential DRG/CC/MCC implications, at the point of care.</p>
        </div>
        <div class="card">
          <div class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div>
          <h4>Decision support</h4>
          <p class="small">Evidence-supported considerations and high-value questions, so the encounter focuses on what changes management.</p>
        </div>
        <div class="card">
          <div class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20c2-5 6-8 8-8s6 3 8 8"/><circle cx="12" cy="7" r="3"/></svg></div>
          <h4>Physician in control</h4>
          <p class="small">The physician evaluates findings, answers clarification questions, and approves documentation. No autonomous treatment, ordering, or EHR write-back.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">The physician workflow</p>
      <h2>Before rounds. After rounds. Before the note is signed.</h2>
    </div>
    <div class="steps">
      <div class="step reveal">
        <span class="step__n">01 · BEFORE ROUNDING</span>
        <h3>Ingest and prioritize</h3>
        <p>The AI reviews available patient information, identifies potentially overlooked safety concerns, and suggests non-routine, high-value questions for the physician to investigate during the encounter.</p>
      </div>
      <div class="step reveal" data-delay="1">
        <span class="step__n">02 · AFTER ROUNDING</span>
        <h3>Reassess with new information</h3>
        <p>The physician contributes updated history, examination findings, and clinical decisions. The system integrates them into its assessment and identifies additional questions or concerns where appropriate.</p>
      </div>
      <div class="step reveal" data-delay="2">
        <span class="step__n">03 · BEFORE FINALIZATION</span>
        <h3>Combined safety and CDI review</h3>
        <p>The AI runs clinical safety and CDI checks together, surfaces actionable findings, and prepares a physician-reviewed note. The physician remains responsible for clinical judgment, treatment decisions, and final documentation.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <!-- SYNTHETIC data only -->
        <div class="mock" role="img" aria-label="Illustrative pre-signature review with synthetic data: a safety item, a documentation specificity item, and the physician's decision controls.">
          <div class="mock__bar">
            <div class="mock__title"><span class="dot"></span> Pre-signature review · Progress note, day 4</div>
            <span class="mono">Synthetic</span>
          </div>
          <div class="mock__body">
            <div class="mock__aside">
              <dl>
                <dt>Patient</dt><dd>Test, Synthetic B.</dd>
                <dt>Age</dt><dd>64</dd>
                <dt>Problem list</dt><dd>Heart failure, CKD stage 3b, type 2 diabetes</dd>
                <dt>Changes 24 h</dt><dd>Weight −2.1 kg, BNP down, K⁺ 3.2</dd>
              </dl>
            </div>
            <div class="mock__main">
              <div class="finding">
                <span class="finding__sev finding__sev--review" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Potassium 3.2 with ongoing loop diuretic; no repletion ordered</strong><span class="chip">Safety</span></div>
                  <p>Magnesium not checked this admission. Consider repletion and a magnesium level if clinically appropriate.</p>
                </div>
              </div>
              <div class="finding">
                <span class="finding__sev finding__sev--cdi" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>"CHF exacerbation" documented without type or acuity</strong><span class="chip">CDI</span></div>
                  <p>Echo 3 months ago: EF 30%. IV diuresis in progress. Evidence may support a more specific heart failure diagnosis if the physician agrees.</p>
                  <p class="finding__q">Specify acuity and type in the assessment if supported by your clinical judgment.</p>
                </div>
              </div>
              <div class="finding">
                <span class="finding__sev finding__sev--cdi" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Malnutrition screen positive; not addressed</strong><span class="chip">CDI</span></div>
                  <p>Dietitian note documents moderate malnutrition criteria. Not reflected in physician assessment.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="mock__foot">
            <span>Accept, edit, or dismiss each item · Note is signed only by the physician</span>
            <span class="chip">Physician decides</span>
          </div>
        </div>
      </div>
      <div class="stack stack--lg reveal" data-delay="1">
        <p class="eyebrow">Intended benefits</p>
        <h2>Fewer misses. Better notes. Less administrative drag.</h2>
        <ul class="contact-list">
          <li>Help physicians recognize clinically significant information that may be missed during routine chart review.</li>
          <li>Improve clinical decision-making and care coordination.</li>
          <li>Identify medication, diagnostic, and treatment concerns.</li>
          <li>Increase the accuracy, specificity, and completeness of physician documentation.</li>
          <li>Reduce avoidable retrospective CDI queries by resolving documentation issues prospectively.</li>
          <li>Reduce administrative burden while maintaining physician oversight.</li>
        </ul>
        <p class="small">Benefits describe design intent. Reductions in query volume, documentation precision, and any financial impact must be measured in deployment studies.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Technical foundation</p>
      <h2>Designed for real clinical workflow, inside an authorized environment.</h2>
      <p class="lede">Patient information stays inside the authorized clinical environment. External medical knowledge is retrieved using focused clinical concepts, never patient identifiers.</p>
    </div>
    <div class="features">
      <div class="feature reveal"><h4>EHR connection</h4><p>Read-only Epic SMART on FHIR integration; normalized encounters, medications, allergies, diagnoses, laboratory results, notes, reports, and orders.</p></div>
      <div class="feature reveal" data-delay="1"><h4>Existing clinical intelligence</h4><p>Preserves the physician-developed AI Hospitalist instructions, standard-of-care review, prospective CDI behavior, and existing CDI logic. No replacement clinical rules invented.</p></div>
      <div class="feature reveal" data-delay="2"><h4>Clinical knowledge</h4><p>Planned or developing connectors for RxNorm, DailyMed, openFDA, PubMed, and society guidelines; configurable institutional pathways for UpToDate and OpenEvidence where supported.</p></div>
      <div class="feature reveal"><h4>Clinician control</h4><p>The physician evaluates findings, answers clarification questions, and approves documentation. No autonomous treatment, ordering, or production EHR write-back is claimed.</p></div>
    </div>
    <div class="status reveal" style="margin-top:40px">
      <strong>Engineering status</strong>
      <p>A working prototype has retrieved and displayed synthetic patients from the Epic developer sandbox through a live, read-only connection, including patient retrieval, normalization, orders, clinical reports, and a clinician interface. The physician-authored clinical engines are being integrated. Production clinical effectiveness has not yet been validated.</p>
    </div>
  </div>
</section>

<section class="section band">
  <div class="container">
    <div class="cta reveal">
      <p class="eyebrow">See it with synthetic patients</p>
      <h2>Walk through the physician workflow with your clinical and CDI leaders.</h2>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html#demo">Request a Demonstration {ARROW}</a>
        <a class="btn btn--ghost" href="autonomous-cdi.html">Explore Autonomous CDI</a>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# AUTONOMOUS CDI
# --------------------------------------------------------------------------
CDI = f"""
<section class="page-hero band">
  <div class="container">
    <div class="page-hero__inner">
      <p class="eyebrow">Product two · Autonomous Retrospective CDI</p>
      <h1>The future of CDI doesn't require reviewing every chart by hand.</h1>
      <p class="lede">Clinical Foresight is building the technology to automate documentation review from clinical evidence through physician clarification and downstream coding, with human oversight concentrated where it matters.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Explore a Partnership {ARROW}</a>
        <a class="btn btn--ghost" href="contact.html#demo">Request a Demonstration</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="stack stack--lg reveal">
        <p class="eyebrow">What it does</p>
        <h2>From manual chart review to intelligent CDI automation.</h2>
        <p class="lede">The retrospective CDI platform is designed to automate the identification, analysis, and resolution of documentation deficiencies within inpatient medical records.</p>
        <p>It examines available clinical evidence, compares it with physician documentation, identifies potential clarification opportunities, and prepares supporting information for compliant, non-leading physician queries. Deterministic coding reference data, including CMS CC/MCC classifications and MS-DRG-related logic, supports the review.</p>
      </div>
      <div class="reveal" data-delay="1">
        <!-- SYNTHETIC data only -->
        <div class="mock" role="img" aria-label="Illustrative CDI worklist with synthetic cases prioritized by documentation opportunity, each with a prepared query for specialist approval.">
          <div class="mock__bar">
            <div class="mock__title"><span class="dot"></span> CDI worklist · Screened overnight</div>
            <span class="mono">Synthetic cases</span>
          </div>
          <div class="mock__body">
            <div class="mock__aside">
              <dl>
                <dt>Screened</dt><dd>212 inpatient encounters</dd>
                <dt>Flagged</dt><dd>31 with clarification opportunity</dd>
                <dt>Prepared</dt><dd>31 draft queries</dd>
                <dt>Awaiting</dt><dd>CDI specialist approval</dd>
              </dl>
            </div>
            <div class="mock__main">
              <div class="finding">
                <span class="finding__sev finding__sev--cdi" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Encounter 00417 · Sepsis documented; organ dysfunction not linked</strong><span class="chip">Draft query</span></div>
                  <p>Lactate 3.4, MAP 62 on admission, vasopressor for 18 h. Evidence organized; query drafted for specialist review.</p>
                </div>
              </div>
              <div class="finding">
                <span class="finding__sev finding__sev--cdi" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Encounter 00392 · "Anemia" without type or acuity</strong><span class="chip">Draft query</span></div>
                  <p>Hgb 12.1 → 7.8 over 36 h; 2 units transfused. Clinical indicators compiled for a compliant query.</p>
                </div>
              </div>
              <div class="finding">
                <span class="finding__sev finding__sev--review" aria-hidden="true"></span>
                <div>
                  <div class="finding__head"><strong>Encounter 00288 · Conflicting diagnoses across notes</strong><span class="chip">Exception</span></div>
                  <p>Attending and consultant document different etiologies. Routed to specialist; not eligible for automated handling.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="mock__foot">
            <span>All queries reviewed by a CDI specialist before sending (Phase One)</span>
            <span class="chip">Human oversight</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Progressive automation strategy</p>
      <h2>Three phases from reviewer-assisted to autonomous.</h2>
      <p class="lede">Each phase expands automation only after validation and institutional authorization. The sequence is the product strategy.</p>
    </div>
    <div class="phases">
      <div class="phase reveal">
        <div class="phase__meta">
          <span class="mono">PHASE ONE</span>
          <h3>AI-Assisted CDI Review</h3>
          <span class="phase__status">In development</span>
        </div>
        <div class="phase__body">
          <p>Clinical Foresight screens charts, organizes clinical evidence, identifies documentation gaps, and prepares proposed physician queries for CDI specialist approval.</p>
          <ul>
            <li>Chart screening and case prioritization</li>
            <li>Evidence organized against physician documentation</li>
            <li>Draft, non-leading queries for specialist sign-off</li>
          </ul>
        </div>
      </div>
      <div class="phase reveal" data-delay="1">
        <div class="phase__meta">
          <span class="mono">PHASE TWO</span>
          <h3>Automated Physician Queries</h3>
          <span class="phase__status phase__status--planned">Planned · subject to validation and institutional approval</span>
        </div>
        <div class="phase__body">
          <p>Following appropriate validation and institutional authorization, qualifying queries can be sent directly to physicians. CDI specialists focus on reviewing responses, documentation updates, and exceptions.</p>
          <ul>
            <li>Eligibility rules define which queries qualify</li>
            <li>Specialists shift to responses and exceptions</li>
            <li>Audit trail for every automated transmission</li>
          </ul>
        </div>
      </div>
      <div class="phase reveal" data-delay="2">
        <div class="phase__meta">
          <span class="mono">PHASE THREE</span>
          <h3>Autonomous CDI and Revenue-Cycle Workflows</h3>
          <span class="phase__status phase__status--future">Long-term architecture</span>
        </div>
        <div class="phase__body">
          <p>The longer-term architecture supports automated routine chart review, query generation, physician-response reconciliation, coding workflows, and downstream billing preparation, with human oversight concentrated on exceptions.</p>
          <ul>
            <li>Routine review and query generation without manual extraction</li>
            <li>Response reconciliation and coding support</li>
            <li>Downstream billing preparation; humans handle exceptions</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Intended benefits</p>
      <h2>Designed for CDI leaders, physician executives, and revenue-cycle leadership.</h2>
    </div>
    <div class="features">
      <div class="feature reveal"><h4>Less manual extraction</h4><p>Eliminate much of the manual chart extraction and review burden.</p></div>
      <div class="feature reveal" data-delay="1"><h4>Consistent identification</h4><p>Improve consistency in identifying documentation opportunities across reviewers and shifts.</p></div>
      <div class="feature reveal" data-delay="2"><h4>Faster queries</h4><p>Accelerate physician-query preparation and resolution.</p></div>
      <div class="feature reveal"><h4>Accurate severity</h4><p>Support accurate representation of patient severity and complexity.</p></div>
      <div class="feature reveal" data-delay="1"><h4>Lower operating cost</h4><p>Reduce the operational costs of traditional CDI processes.</p></div>
      <div class="feature reveal" data-delay="2"><h4>A path to autonomy</h4><p>Enable hospitals to transition toward increasingly autonomous documentation and revenue-cycle operations.</p></div>
    </div>
    <div class="status reveal" style="margin-top:40px">
      <strong>A compelling hospital case, to be proven</strong>
      <p>Improved capture of clinically supported diagnoses and accurate DRG classification are the design goals. Actual reimbursement impact, query-volume reduction, and operating-cost savings require validation in institution-approved pilots before any production rollout.</p>
    </div>
  </div>
</section>

<section class="section band">
  <div class="container">
    <div class="cta reveal">
      <p class="eyebrow">Commercial configuration</p>
      <h2>Prospective AI Hospitalist + CDI, standalone retrospective CDI, or a combined enterprise license.</h2>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Explore a Partnership {ARROW}</a>
        <a class="btn btn--ghost" href="ai-hospitalist.html">Explore the AI Hospitalist</a>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# ABOUT / VISION
# --------------------------------------------------------------------------
ABOUT = f"""
<section class="page-hero band">
  <div class="container">
    <div class="page-hero__inner">
      <p class="eyebrow">Our vision</p>
      <h1>Make retrospective documentation correction increasingly unnecessary.</h1>
      <p class="lede">Our mission is to improve the safety and quality of patient care while fundamentally modernizing clinical documentation and hospital revenue-cycle operations. The way to get there is to get documentation right the first time.</p>
    </div>
  </div>
</section>

<section class="section" id="founder">
  <div class="container">
    <div class="founder">
      <div class="founder__portrait reveal" aria-hidden="true">
        <span class="mono">Dr. Daniel Francis · Physician-Founder</span>
      </div>
      <div class="stack stack--lg reveal" data-delay="1">
        <p class="eyebrow">Physician-founder</p>
        <h2>Built from the bedside outward.</h2>
        <p class="lede">Clinical Foresight was created by Dr. Daniel Francis, a practicing physician with 28 years of clinical experience, including 15 years in hospital medicine.</p>
        <p>The platform grew from a physician-developed AI Hospitalist workflow refined through daily clinical practice. Dr. Francis recognized that increasingly complex electronic medical records often contain clinically important findings that can be overlooked amid the demands of inpatient medicine, and his work demonstrated the practical value of incorporating advanced AI into everyday clinical reasoning, chart review, and documentation.</p>
        <p>Clinical Foresight is the effort to transform that physician-developed approach into an integrated hospital technology platform.</p>
        <p class="founder__quote">This is technology shaped by the realities of practicing medicine, not software designed around hospital administrative processes.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">What we believe</p>
      <h2>Four convictions behind the platform.</h2>
    </div>
    <div class="grid grid--2">
      <div class="card reveal"><h4>The record is the risk</h4><p class="small">Important clinical information is frequently buried within increasingly complex medical records, while physicians must make high-stakes decisions under significant time constraints.</p></div>
      <div class="card reveal" data-delay="1"><h4>Prospective beats retrospective</h4><p class="small">Documentation and safety issues are cheapest and safest to resolve while the physician is still with the patient, not days later through a query.</p></div>
      <div class="card reveal" data-delay="2"><h4>Explainability is non-negotiable</h4><p class="small">Every finding cites its clinical evidence so the physician can evaluate it quickly and remain responsible for the decision.</p></div>
      <div class="card reveal" data-delay="3"><h4>Autonomy is earned in phases</h4><p class="small">Automation expands only after validation and institutional authorization, with human oversight concentrated on exceptions.</p></div>
    </div>
  </div>
</section>

<section class="section band">
  <div class="container">
    <div class="sec-head reveal">
      <p class="eyebrow">Long-term strategy</p>
      <h2>Two commercial opportunities, one clinical foundation.</h2>
      <p class="lede">A prospective physician-facing product and a retrospective CDI-team product share the same clinical data and evidence foundation. Each sells on its own; together they move a hospital toward autonomous documentation operations.</p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <span class="step__n">NOW · PROTOTYPE &amp; INTEGRATION</span>
        <h3>Synthetic-patient workflows</h3>
        <p>Read-only Epic SMART on FHIR connection in the developer sandbox; physician-authored clinical engines being integrated; demonstrations with synthetic data.</p>
      </div>
      <div class="step reveal" data-delay="1">
        <span class="step__n">NEXT · EVALUATION &amp; PILOT</span>
        <h3>Institution-approved measurement</h3>
        <p>Evaluate CDI and clinical safety outputs against physician-approved cases; establish pilot requirements, security review, and metrics for clinical quality, workflow impact, and attributable value.</p>
      </div>
      <div class="step reveal" data-delay="2">
        <span class="step__n">LATER · PROGRESSIVE AUTONOMY</span>
        <h3>Automated queries, coding, revenue cycle</h3>
        <p>Automated physician queries where authorized, then coding workflows and downstream billing preparation, with humans handling exceptions.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta reveal">
      <p class="eyebrow">Join the conversation</p>
      <h2>We welcome CDI leaders, CMOs, CMIOs, informatics teams, revenue-cycle executives, and strategic partners.</h2>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Explore a Partnership {ARROW}</a>
        <a class="btn btn--ghost" href="contact.html#investors">Investor Inquiries</a>
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# CONTACT
# --------------------------------------------------------------------------
CONTACT = f"""
<section class="page-hero band">
  <div class="container">
    <div class="page-hero__inner">
      <p class="eyebrow">Partnerships · Demonstrations · Investment</p>
      <h1>Explore a partnership.</h1>
      <p class="lede">For health systems evaluating prospective CDI and clinical safety workflows, technology partners, and investors interested in a physician-founded platform with two commercial opportunities.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split" style="align-items:start">
      <div class="reveal">
        <form class="form" id="contact-form" method="POST" action="https://formspree.io/f/YOUR_FORM_ID" data-endpoint="https://formspree.io/f/YOUR_FORM_ID" novalidate>
          <div class="form__row">
            <div class="field"><label for="name">Full name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="title">Title</label><input id="title" name="title" type="text" autocomplete="organization-title" placeholder="e.g. Chief Medical Officer"></div>
          </div>
          <div class="form__row">
            <div class="field"><label for="organization">Organization</label><input id="organization" name="organization" type="text" autocomplete="organization" required></div>
            <div class="field"><label for="email">Work email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
          </div>
          <div class="field">
            <label for="interest">I'm interested in</label>
            <select id="interest" name="interest" required>
              <option value="Partnership">Exploring a partnership</option>
              <option value="Demonstration">Requesting a demonstration</option>
              <option value="Pilot">Discussing a pilot</option>
              <option value="Investment">Investment conversation</option>
              <option value="Other">Something else</option>
            </select>
          </div>
          <div class="field"><label for="message">How can we help?</label><textarea id="message" name="message" required placeholder="Tell us about your organization, your current CDI model, and what you'd like to explore."></textarea></div>
          <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
          <div class="btn-row">
            <button class="btn btn--primary" type="submit">Send message {ARROW}</button>
          </div>
          <p class="form__note" id="form-status" aria-live="polite">Or email <a href="mailto:{EMAIL}">{EMAIL}</a> directly.</p>
        </form>
      </div>
      <aside class="contact-aside reveal" data-delay="1">
        <div class="stack">
          <p class="eyebrow">Direct contact</p>
          <h3>Dr. Daniel Francis</h3>
          <p class="small">Physician-Founder</p>
          <p class="email"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <div><button class="btn btn--ghost" type="button" data-copy="{EMAIL}">Copy address</button></div>
        </div>
        <div class="stack" id="demo">
          <p class="eyebrow">Discussion topics</p>
          <ul class="contact-list">
            <li>Hospital workflow fit</li>
            <li>Clinical and CDI evaluation design</li>
            <li>Pilot structure and measurement</li>
            <li>Enterprise licensing</li>
            <li>Strategic partnerships</li>
          </ul>
        </div>
        <div class="status" id="investors">
          <strong>Before any pilot</strong>
          <p>Initial discussions and demonstrations use synthetic data. Any real-patient pilot requires separate institutional authorization, security review, and clinical evaluation.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
"""


PAGES = [
    ("index.html", "Clinical Foresight | Physician-Founded Clinical AI for Safety and CDI",
     "Physician-founded healthcare AI that identifies clinical risks, improves documentation at the point of care, and advances hospitals toward autonomous Clinical Documentation Integrity.", HOME, True),
    ("ai-hospitalist.html", "AI Hospitalist + Prospective CDI | Clinical Foresight",
     "Clinical safety surveillance, decision support, and prospective CDI in one physician workflow: before rounds, after rounds, and before the note is signed.", HOSPITALIST, True),
    ("autonomous-cdi.html", "Autonomous Retrospective CDI | Clinical Foresight",
     "From manual chart review to intelligent CDI automation: a three-phase path from reviewer-assisted review to automated queries, coding support, and revenue-cycle workflows.", CDI, True),
    ("about.html", "Our Vision | Clinical Foresight",
     "The physician-founder story, clinical motivation, company mission, and long-term strategy behind Clinical Foresight.", ABOUT, True),
    ("contact.html", "Partnerships and Contact | Clinical Foresight",
     "Explore a partnership, request a demonstration, or start an investment conversation with Clinical Foresight.", CONTACT, True),
]

for path, title, desc, body, dark in PAGES:
    (ROOT / path).write_text(head(title, desc, path, dark) + body + FOOTER, encoding="utf-8")
    print("wrote", path)

#!/usr/bin/env python3
"""WebFolio static site generator.

Edit the content in this file (or the shared layout), run `python build.py`,
and every HTML page is regenerated with the same header, footer, SEO tags and
schema. The generated .html files are committed, so GitHub Pages needs no build.
"""
import os, json, html

BASE = "https://rajpratham1.github.io/my-portfolio/"
EMAIL = "shrivastavapratham40@gmail.com"
PHONE = "+91-6200892887"
PHONE_TEL = "+916200892887"
WA = "https://wa.me/916200892887"
GA_ID = "G-XXXXXXXXXX"          # replace with your GA4 ID
UPDATED = "2026-10-24"
OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [("index.html", "Home"), ("services.html", "Services"), ("work.html", "Work"),
       ("pricing.html", "Pricing"), ("about.html", "About"), ("faq.html", "FAQ"),
       ("careers.html", "Careers"), ("contact.html", "Contact")]

def head(title, desc, path, schema=None, noindex=False):
    url = BASE + ("" if path == "index.html" else path)
    og = BASE + "assets/img/og-image.png"
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": "WebFolio Studio",
           "url": BASE, "email": EMAIL, "telephone": PHONE,
           "logo": BASE + "assets/logo/webfolio-mark.svg",
           "sameAs": ["https://github.com/rajpratham1"]}]
    if schema: ld.append(schema)
    t = html.escape(title, quote=True); d = html.escape(desc, quote=True)
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="{robots}">
<meta name="author" content="WebFolio Studio">
<meta name="theme-color" content="#070b16">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:locale" content="en_IN">
<meta property="og:site_name" content="WebFolio"><meta property="og:title" content="{t}">
<meta property="og:description" content="{d}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{og}">
<link rel="icon" type="image/svg+xml" href="assets/logo/webfolio-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{GA_ID}");</script>' if GA_ID != "G-XXXXXXXXXX" else ""}
</head>
'''

def header(active):
    links = "".join(
        f'<a href="{h}"{" class=\"active\" aria-current=\"page\"" if h == active else ""}>{l}</a>'
        for h, l in NAV)
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="WebFolio home"><img src="assets/logo/webfolio-mark.svg" alt="" width="34" height="34"><span class="bn">Web<b>Folio</b></span></a>
    <button class="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="navLinks"><span></span></button>
    <nav class="nav-links" id="navLinks" aria-label="Primary">{links}<a class="btn" href="contact.html#start">Start a project</a></nav>
  </div>
</header>
<main id="main">
'''

FOOTER = f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="index.html"><img src="assets/logo/webfolio-mark.svg" alt="" width="34" height="34"><span class="bn">Web<b>Folio</b></span></a>
        <p style="margin-top:1rem;max-width:36ch">We create. We develop. We maintain. Websites, Android apps and long-term support from one dependable team.</p>
      </div>
      <div><h4>Services</h4><ul>
        <li><a href="website-development.html">Website development</a></li>
        <li><a href="android-app-development.html">Android app development</a></li>
        <li><a href="maintenance-support.html">Maintenance &amp; support</a></li>
        <li><a href="pricing.html">Pricing</a></li></ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="about.html">About</a></li><li><a href="work.html">Work</a></li>
        <li><a href="careers.html">Careers</a></li><li><a href="tools.html">Free tools</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
      <div><h4>Talk to us</h4><ul>
        <li><a href="mailto:{EMAIL}">Email</a></li>
        <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li><a href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
        <li><a href="https://github.com/rajpratham1" target="_blank" rel="noopener noreferrer">GitHub</a></li></ul></div>
    </div>
    <div class="foot-bottom">
      <span>© <span data-year>2026</span> WebFolio Studio. All rights reserved.</span>
      <span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></span>
    </div>
  </div>
</footer>
<div class="quickbar" aria-label="Quick contact"><a href="tel:{PHONE_TEL}">Call</a><a href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp</a><a href="contact.html#start">Message</a></div>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

def cta_band(title="Have an idea? Let’s turn it into something people use.",
             text="Tell us what you need — a website, an Android app or ongoing care. You’ll get a clear plan and honest advice within 24 hours.",
             label="Start your project"):
    return f'''<section class="section"><div class="wrap"><div class="cta-band reveal">
  <h2>{title}</h2><p>{text}</p>
  <div class="btn-row"><a class="btn" href="contact.html#start">{label}</a><a class="btn ghost" href="{WA}" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a></div>
</div></div></section>'''

def page_hero(eyebrow, h1, lead, wide=False):
    return f'''<section class="page-hero{' wide' if wide else ''}"><div class="wrap reveal">
  <span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p></div></section>'''

def head_block(eyebrow, h2, lead="", center=False):
    return f'''<div class="section-head{' center' if center else ''} reveal"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{f'<p class="lead">{lead}</p>' if lead else ''}</div>'''

def card(icon, title, text, extra=""):
    return f'<article class="card reveal"><div class="icon" aria-hidden="true">{icon}</div><h3>{title}</h3><p>{text}</p>{extra}</article>'

def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)

PAGES = {}   # filename -> (priority, changefreq)

def build(name, title, desc, body, active=None, schema=None, prio="0.8"):
    PAGES[name] = prio
    write(name, head(title, desc, name, schema) + header(active or name) + body + FOOTER)

# ───────────────────────── HOME ─────────────────────────
marquee_items = ["Business websites", "Android apps", "Landing pages", "Portfolio sites", "Clinic & hospital sites",
                 "School & institute sites", "Dashboards", "Catalog & e-commerce", "Redesign", "Speed optimization",
                 "Monthly maintenance", "SEO-ready builds"]
mq = "".join(f"<span>{m}</span>" for m in marquee_items) * 2

def app_card(name, tag, text, kind):
    if kind == "phone":
        mini = '<div class="phone-s"><i></i><b></b><b></b><b></b></div>'
    else:
        mini = '<div class="desk"><b></b><i></i></div>'
    return f'''<article class="card app-card reveal"><div class="mini" aria-hidden="true">{mini}</div>
<div class="top"><h3>{name}</h3><span class="pill">{tag}</span></div><p>{text}</p></article>'''

home = f'''
<section class="hero"><div class="wrap hero-grid">
  <div class="reveal">
    <span class="eyebrow">Websites · Android apps · Maintenance</span>
    <h1>Digital products that look <span class="grad">premium</span> and work for your business.</h1>
    <p class="lead">Need a website or an Android app? We design, develop, launch and maintain it — fast on every device, clear for your customers, and built to keep growing with you.</p>
    <div class="btn-row"><a class="btn" href="contact.html#start">Start your project</a><a class="btn ghost" href="work.html">See our work</a></div>
    <div class="hero-stats">
      <div><b data-count="7" data-suffix=" days">7 days</b><span>Fastest launch cycle</span></div>
      <div><b data-count="24" data-suffix="h">24h</b><span>First reply target</span></div>
      <div><b data-count="100" data-suffix="%">100%</b><span>Code &amp; assets owned by you</span></div>
    </div>
  </div>
  <div class="stage reveal" aria-hidden="true">
    <div class="browser"><div class="browser-bar"><i></i><i></i><i></i><em></em></div>
      <div class="browser-body"><div class="mk-h"></div><div class="mk-l"></div><div class="mk-l s"></div><div class="mk-row"><div></div><div></div><div></div></div></div></div>
    <div class="phone"><div class="phone-screen"><div class="mk-h"></div><div class="blk on"></div><div class="blk"></div><div class="blk"></div></div></div>
    <div class="chip-float c1"><i></i>Mobile-first</div>
    <div class="chip-float c2"><i></i>SEO-ready</div>
  </div>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{mq}</div></div>

<section class="section"><div class="wrap">
  {head_block("What we do", "Everything you need to launch and grow online", "One partner for the whole journey — from the first sketch to the monthly check-up after launch.")}
  <div class="bento">
    <article class="card feature reveal"><div class="icon" aria-hidden="true">🌐</div><h3>Website development</h3>
      <p>Portfolio, business, clinic, school, catalog or custom platforms. Responsive, fast, accessible and set up for search from day one.</p>
      <div class="tags"><span>Responsive</span><span>SEO-ready</span><span>Conversion-focused</span><span>Fast loading</span></div>
      <p style="margin-top:1.2rem"><a href="website-development.html">Explore website development →</a></p></article>
    {card("📱", "Android apps", "Lightweight, one-hand-friendly APKs for services, sales and operations.", '<p style="margin-top:1rem"><a href="android-app-development.html">Learn more →</a></p>')}
    {card("🛠️", "Maintenance", "Fixes, updates, speed checks and content refreshes after launch.", '<p style="margin-top:1rem"><a href="maintenance-support.html">Learn more →</a></p>')}
    {card("🎨", "Redesign", "Turn an outdated site into a clear, trustworthy and faster one.")}
    {card("💻", "Dashboards &amp; iOS-ready UI", "Desktop workflows and iPhone/iPad interface design with the same brand.")}
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("How we work", "A clear path from idea to launch", "No guesswork. You always know the current stage, the next milestone and the expected delivery date.", True)}
  <div class="steps">
    <div class="step reveal"><h3>Discover</h3><p>We map your audience, goals and page priorities before any design decisions.</p></div>
    <div class="step reveal"><h3>Design</h3><p>Layout and motion are planned together, so the experience feels cohesive.</p></div>
    <div class="step reveal"><h3>Build &amp; test</h3><p>Development with responsive, accessibility and cross-device QA built in.</p></div>
    <div class="step reveal"><h3>Launch &amp; improve</h3><p>We publish, monitor and refine key sections for better results.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Apps &amp; interfaces", "Built for real business use", "A glimpse of the kinds of products we design and develop across web, Android, desktop and iOS-ready interfaces.")}
  <div class="grid g3">
    {app_card("Client Connect", "Service", "Lead capture, booking requests and support tickets in one app.", "phone")}
    {app_card("Sales Tracker", "Business", "Pipeline status, charts and quick mobile updates for your team.", "phone")}
    {app_card("Field Staff", "Operations", "Task assignment, attendance and location-based updates.", "phone")}
    {app_card("Business Website", "Web", "Responsive multi-page sites optimized for speed and conversion.", "desk")}
    {app_card("Desktop Dashboard", "Desktop", "Workflow systems and dashboards built for teams.", "desk")}
    {app_card("Portfolio Lite", "Brand", "A personal-brand app with services, projects and contact actions.", "phone")}
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">Our story</span>
    <h2>From idea to impact — products you’ll be proud to show.</h2>
    <p>WebFolio started with one mission: turn business ideas into premium digital products that look credible and perform in the real world. Today our team of <strong style="color:var(--text)">6+ active developers</strong> covers design, frontend, backend and Android development.</p>
    <p>We focus on delivery quality, clean architecture and smooth user experience — so what we build stays reliable long after launch.</p>
    {ticks(["Clear milestones and honest timelines", "Mobile, tablet and desktop tested", "Support that continues after go-live"])}
    <div class="founder"><img src="https://avatars.githubusercontent.com/rajpratham1?v=4" alt="Pratham Kumar" width="56" height="56" loading="lazy"><div><strong>Pratham Kumar</strong><small>Founder · <a href="https://github.com/rajpratham1" target="_blank" rel="noopener noreferrer">github.com/rajpratham1</a></small></div></div>
    <div class="btn-row"><a class="btn ghost" href="about.html">More about us</a></div>
  </div>
  <div class="panel reveal">
    <h3>Why clients choose us</h3>
    <div class="grid" style="gap:1rem;margin-top:1rem">
      <div><strong>One team, every platform</strong><p>Website, Android and maintenance with a consistent look and one point of contact.</p></div>
      <div><strong>Speed you can feel</strong><p>Optimized assets and lean code so pages load fast even on mid-range phones.</p></div>
      <div><strong>Transparent pricing</strong><p>Scope and budget are agreed upfront — no hidden charges.</p></div>
      <div><strong>You own it</strong><p>Final code and assets are yours when the project is complete.</p></div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Free tools", "Try our products — free to use", "Practical tools we built ourselves, showing how we think about UX and engineering.")}
  <div class="grid g3">
    <article class="card reveal"><div class="icon" aria-hidden="true">⚡</div><h3>Aether Tools</h3><p>Productivity dashboard with weather, AQI, Pomodoro, quick tasks and utility tools.</p><a class="btn ghost" href="https://rajpratham1.github.io/Aether-Tools/" target="_blank" rel="noopener noreferrer">Open Aether Tools</a></article>
    <article class="card reveal"><div class="icon" aria-hidden="true">🔒</div><h3>PrivyChat</h3><p>Zero-trust ephemeral messaging with encryption, stealth mode and panic controls.</p><a class="btn ghost" href="https://privy-chat.onrender.com/" target="_blank" rel="noopener noreferrer">Open PrivyChat</a></article>
    <article class="card reveal"><div class="icon" aria-hidden="true">🧰</div><h3>All free tools</h3><p>See the full feature breakdown and links in one place.</p><a class="btn ghost" href="tools.html">Visit tools page</a></article>
  </div>
</div></section>

<section class="section" id="testimonials" hidden><div class="wrap">
  {head_block("Client voice", "What clients say", "", True)}<div class="grid g3"></div></div></section>

{cta_band()}
'''
build("index.html", "WebFolio — Website & Android App Development Studio",
      "WebFolio designs, develops and maintains fast, premium websites and Android apps for businesses. Clear process, transparent pricing, support after launch.",
      home, prio="1.0")

# ───────────────────────── SERVICES ─────────────────────────
def service_block(icon, title, intro, items, flip=False):
    side = f'''<div class="panel reveal"><div class="icon" aria-hidden="true">{icon}</div><h3>What’s included</h3>{ticks(items)}</div>'''
    copy = f'''<div class="reveal"><h2>{title}</h2><p class="lead">{intro}</p></div>'''
    return f'<div class="split" style="margin-bottom:4rem">{side + copy if flip else copy + side}</div>'

services = page_hero("Services", "From fast landing pages to full business platforms.",
  "Need a website, an Android app, a redesign or ongoing maintenance? Pick one service or combine them — we plan it around your goal.") + f'''
<section class="section"><div class="wrap">
{service_block("🌐", "Website development", "Single-page, multi-page, e-commerce, portfolio and service sites built for your exact requirement — responsive, fast and ready to rank.",
  ["Custom design matched to your brand", "Mobile, tablet and desktop layouts", "SEO setup: titles, metadata, schema, sitemap", "Contact forms and WhatsApp/call actions", "Launch support and handoff"])}
{service_block("📱", "Android app development", "Business apps, utility tools and lightweight APK products with practical, clean interfaces that are easy to use with one hand.",
  ["Service, sales and field-staff apps", "Material-style UI and smooth navigation", "API-ready and push-notification ready", "Stable on mid-range devices", "Matching web identity (optional)"], True)}
{service_block("🛠️", "Maintenance &amp; growth", "Websites need care after launch. We handle fixes, updates and improvements so your brand stays modern, secure and reliable.",
  ["Bug fixes and speed optimization", "Content and section updates", "Monthly health review", "New pages and features in phases", "Priority support for active clients"])}
</div></section>

<section class="section"><div class="wrap">
  {head_block("Process", "How a project runs", "Five clear stages with review checkpoints, so you’re never left guessing.", True)}
  <div class="steps five">
    <div class="step reveal"><h3>Briefing</h3><p>Business objective and audience profile.</p></div>
    <div class="step reveal"><h3>Architecture</h3><p>Page map and conversion flow.</p></div>
    <div class="step reveal"><h3>UI build</h3><p>Components, motion and responsiveness.</p></div>
    <div class="step reveal"><h3>QA</h3><p>Cross-device checks and bug hardening.</p></div>
    <div class="step reveal"><h3>Launch</h3><p>Publish, hand off and monitor.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Support promise", "Service levels you can rely on", "What to expect once your product is live.")}
  <div class="table-wrap reveal"><table>
    <thead><tr><th>Area</th><th>Standard</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>First response</td><td>Within 24 hours</td><td>Business days priority, emergency path available</td></tr>
      <tr><td>Critical bug fix</td><td>24–48 hours</td><td>Depends on hosting/access readiness</td></tr>
      <tr><td>Content update</td><td>1–3 days</td><td>Text and image updates with a QA check</td></tr>
      <tr><td>Monthly maintenance</td><td>Performance + health review</td><td>Speed, responsiveness and broken-link checks</td></tr>
    </tbody></table></div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Dig deeper", "Explore each service", "", True)}
  <div class="grid g3">
    {card("🌐", "Website development", "Scope and outcomes for website builds.", '<p style="margin-top:1rem"><a href="website-development.html">View page →</a></p>')}
    {card("📱", "Android app development", "The APK delivery model and our product approach.", '<p style="margin-top:1rem"><a href="android-app-development.html">View page →</a></p>')}
    {card("🛠️", "Maintenance support", "Post-launch support model and service levels.", '<p style="margin-top:1rem"><a href="maintenance-support.html">View page →</a></p>')}
  </div>
</div></section>
{cta_band()}
'''
build("services.html", "Services — Websites, Android Apps & Maintenance | WebFolio",
      "Website development, Android app development and ongoing maintenance from one team. See what’s included, our process and support levels.",
      services, prio="0.9", schema={"@context":"https://schema.org","@type":"Service","name":"Website and Android app development","provider":{"@type":"Organization","name":"WebFolio Studio"},"areaServed":"Worldwide","serviceType":["Website development","Android app development","Website maintenance"]})

# ───────────────────────── WORK ─────────────────────────
def case(meta, problem, solution, kpis):
    m = "".join(f"<span>{x}</span>" for x in meta)
    k = "".join(f"<div><b>{a}</b><small>{b}</small></div>" for a, b in kpis)
    return f'''<article class="card case reveal"><div class="meta">{m}</div>
<p><strong style="color:var(--text)">Problem:</strong> {problem}</p><p><strong style="color:var(--text)">Solution:</strong> {solution}</p><div class="kpis">{k}</div></article>'''

work = page_hero("Our work", "Work that proves reliability, not just aesthetics.",
  "Every card, section and motion has a reason. Here’s how we approach delivery and the kind of results we aim for.") + f'''
<section class="section"><div class="wrap">
  {head_block("Selected outcomes", "Case studies with measurable results")}
  <div class="grid g2">
    {case(["Healthcare site", "3 weeks", "Next.js + SEO"], "Slow mobile pages and low booking trust.", "Rebuilt the page flow with clear CTA hierarchy, faster image delivery and trust sections.", [("3.8s → 1.7s", "Load time"), ("+42%", "Booking leads"), ("−31%", "Bounce rate")])}
    {case(["Service startup", "4 weeks", "React + Node"], "Good traffic but poor inquiry conversion.", "Structured the landing narrative, simplified forms and introduced intent-based sections.", [("2.9s → 1.5s", "Load time"), ("+58%", "Qualified leads"), ("−26%", "Bounce rate")])}
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Types of products", "What we design and build")}
  <div class="grid g3">
    {card("🩺", "Healthcare UI", "Clear information hierarchy for sensitive decision flows.")}
    {card("🛡️", "Security portal", "Trust-first visual language with a performance-focused build.")}
    {card("📈", "Business landing", "High-impact hero and concise, conversion-driven copy blocks.")}
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Delivery notes", "How we keep quality consistent", "", False)}
  <div class="grid g3">
    {card("🗺️", "Planning", "Each project starts with clear scope, timeline and milestone checkpoints so delivery stays predictable.")}
    {card("⚙️", "Execution", "Design, development and QA run in structured cycles to keep quality consistent on desktop, tablet and mobile.")}
    {card("🤝", "Support", "After launch: bug fixes, performance reviews and iterative improvements based on real user behavior.")}
  </div>
</div></section>

<section class="section" id="testimonials" hidden><div class="wrap">
  {head_block("Client voice", "What clients say")}<div class="grid g3"></div></div></section>
{cta_band("Want results like these for your project?", "Share your goals and we’ll outline what’s realistic — with timelines and measurable targets.", "Discuss your project")}
'''
build("work.html", "Our Work — Case Studies & Delivery Quality | WebFolio",
      "Case studies and delivery notes from WebFolio: faster load times, higher lead quality and reliable launches for websites and apps.",
      work, prio="0.9")

# ───────────────────────── PRICING ─────────────────────────
def plan(name, forwho, time, items, hot=False):
    return f'''<article class="card price{' hot' if hot else ''} reveal">{'<span class="badge">Most popular</span>' if hot else ''}
<h3>{name}</h3><p class="for">{forwho}</p><div class="time">{time}</div><p style="font-size:.85rem">Typical timeline</p>{ticks(items)}
<a class="btn{'' if hot else ' ghost'}" href="contact.html#start">Get a quote</a></article>'''
pricing = page_hero("Pricing", "Fair, consultation-first pricing.",
  "Every project is different, so we recommend a budget after understanding your requirements, features and timeline. No hidden charges, ever.") + f'''
<section class="section"><div class="wrap">
  {head_block("Packages", "Pick a starting point — we’ll tailor it", "", True)}
  <div class="grid g3">
    {plan("Starter", "Local businesses and solo founders", "7–10 days", ["Landing page or compact website", "Responsive layout", "Core SEO setup", "Launch support"])}
    {plan("Growth", "Service brands and startups", "2–4 weeks", ["Multi-page business website", "Conversion flow and trust sections", "Speed optimization", "Analytics-ready"], True)}
    {plan("Pro", "Scaling teams", "Phased delivery", ["Website + app aligned architecture", "Advanced UX and analytics readiness", "Maintenance roadmap", "Priority support"])}
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Project types", "What we build")}
  <div class="grid g3">
    {card("👤", "Portfolio websites", "Personal portfolios, creator profiles and resume sites.")}
    {card("🏥", "Hospital &amp; clinic sites", "Doctor profiles, appointment sections and patient information.")}
    {card("🏢", "Business &amp; startup sites", "Company profiles, lead generation and service funnels.")}
    {card("🎓", "School &amp; institute sites", "Admissions, announcements and faculty sections.")}
    {card("🛒", "E-commerce &amp; catalog", "Product showcases, inquiry forms and room to grow into sales.")}
    {card("📱", "Android + website combo", "Unified web and mobile presence with matching brand and support.")}
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("How pricing works", "Simple, transparent, flexible", "", True)}
  <div class="steps">
    <div class="step reveal"><h3>Consultation first</h3><p>We discuss goals, pages, integrations and timeline before finalizing the amount.</p></div>
    <div class="step reveal"><h3>Budget-friendly phases</h3><p>Start with key pages and scale in phases as your business grows.</p></div>
    <div class="step reveal"><h3>No hidden charges</h3><p>All deliverables are explained clearly before development starts.</p></div>
    <div class="step reveal"><h3>Optional maintenance</h3><p>Post-launch support can be included based on your needs.</p></div>
  </div>
</div></section>
{cta_band("Get a clear quote for your project", "Share your requirement and budget range. We’ll reply with a practical recommendation — not a generic package.", "Request a quote")}
'''
build("pricing.html", "Pricing — Transparent, Consultation-First | WebFolio",
      "Starter, Growth and Pro website and app packages with transparent, consultation-first pricing. No hidden charges.", pricing)

# ───────────────────────── ABOUT ─────────────────────────
about = page_hero("About us", "Engineering mindset with design discipline.",
  "We combine system-level thinking with visual clarity so your product feels premium, stable and easy to maintain over time.") + f'''
<section class="section"><div class="wrap split">
  <div class="reveal"><h2>We treat every site as a long-term product.</h2>
    <p>WebFolio is led by founder Pratham Kumar and a team of 6+ active developers across design, frontend, backend and Android development. We started with a simple belief: businesses deserve digital products that look credible and keep working.</p>
    <p>That’s why we plan before we build, test before we launch, and stay available after go-live.</p>
    <div class="founder"><img src="https://avatars.githubusercontent.com/rajpratham1?v=4" alt="Pratham Kumar" width="56" height="56" loading="lazy"><div><strong>Pratham Kumar</strong><small>Founder · <a href="https://rajpratham1.github.io/my-portfolio/" target="_blank" rel="noopener noreferrer">Portfolio</a> · <a href="https://github.com/rajpratham1" target="_blank" rel="noopener noreferrer">GitHub</a></small></div></div></div>
  <div class="grid" style="gap:1rem">
    {card("🧭", "Product thinking", "We map features to user actions before writing code, reducing rework.")}
    {card("🧩", "System clarity", "Reusable blocks keep the codebase clean and scalable.")}
    {card("💬", "Communication", "Milestone-by-milestone updates keep decisions transparent.")}
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Our values", "What we hold ourselves to", "", True)}
  <div class="grid g3">
    {card("🎯", "Discipline", "Daily quality checks and clear acceptance criteria.")}
    {card("🏗️", "Ownership", "Each client site is a long-term product, not a one-time delivery.")}
    {card("♿", "Respect for users", "Readable content, touch-friendly interactions and reduced-motion support.")}
  </div>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Dedication in practice", "The daily rhythm behind every release")}
  <div class="steps" style="grid-template-columns:repeat(3,1fr)">
    <div class="step reveal"><h3>Morning review</h3><p>Align tasks with business priorities and customer impact.</p></div>
    <div class="step reveal"><h3>Build blocks</h3><p>Ship tested increments with clear changelog entries.</p></div>
    <div class="step reveal"><h3>Evening validation</h3><p>Run responsive and interaction checks before marking work complete.</p></div>
  </div>
</div></section>

<section class="section" id="quality"><div class="wrap">
  {head_block("Quality standards", "Performance is a business metric", "Targets we hold every launch to, so pages feel fast and stable.")}
  <div class="table-wrap reveal"><table>
    <thead><tr><th>Metric</th><th>Target</th><th>Why it matters</th></tr></thead>
    <tbody>
      <tr><td>LCP</td><td>&lt; 2.5s</td><td>Main content appears quickly on mobile</td></tr>
      <tr><td>INP</td><td>&lt; 200ms</td><td>Interactions feel instant</td></tr>
      <tr><td>CLS</td><td>&lt; 0.1</td><td>Layout stays stable and trustworthy</td></tr>
      <tr><td>TTFB</td><td>&lt; 800ms</td><td>Quick server response baseline</td></tr>
    </tbody></table></div>
</div></section>
{cta_band("Let’s build something together", "We’d love to hear about your project — big or small.", "Contact us")}
'''
build("about.html", "About WebFolio — Team, Values & Quality Standards",
      "Meet the WebFolio team: our values, working rhythm and the performance standards we hold every website and app to.", about, prio="0.9")

# ───────────────────────── FAQ ─────────────────────────
faqs = [
 ("How long does delivery take?", "Landing pages take 7–10 days. Most multi-page websites launch in 2–4 weeks depending on final scope and how ready your content is."),
 ("Will it work on all devices?", "Yes. Mobile, tablet and desktop responsiveness are validated during QA before launch."),
 ("Do you build Android apps (APK)?", "Yes. Share your use case and we’ll propose a practical Android development plan with a matching website identity and maintenance support."),
 ("Can we start small and scale later?", "Absolutely. Start with the key pages, then add pages and features in planned phases — the architecture is modular."),
 ("Who owns the code?", "You do. You own the final code and assets once the project is complete."),
 ("Can you maintain my existing website?", "Yes. We offer maintenance for updates, performance improvements and issue fixes, even for sites we didn’t build."),
 ("How are revisions handled?", "Feedback is collected in structured rounds so speed and quality stay balanced. Reasonable revision rounds are included in your plan."),
 ("How does pricing work?", "We recommend a budget after a short consultation, based on scope and timeline. Everything is explained before development starts."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
faq = page_hero("FAQ", "Common questions, answered plainly.", "Timelines, revisions, ownership and support — the things people ask before they start.") + f'''
<section class="section"><div class="wrap"><div class="faq reveal">{faq_html}</div></div></section>
{cta_band("Still have questions?", "We’re happy to help — send a message and we’ll reply within 24 hours.", "Send a message")}
'''
build("faq.html", "FAQ — Timelines, Ownership, Support | WebFolio",
      "Answers about delivery time, Android apps, code ownership, revisions, maintenance and pricing at WebFolio.", faq,
      schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]})

# ───────────────────────── TOOLS ─────────────────────────
tools = page_hero("Free tools", "Useful products for productivity and privacy.",
  "Free to use, and a living example of our focus on practical utility, modern UX and reliable engineering.") + f'''
<section class="section"><div class="wrap grid g2">
  <article class="card reveal"><div class="icon" aria-hidden="true">⚡</div><h2 style="font-size:1.7rem">Aether Tools</h2>
    <p>An all-in-one productivity dashboard with a glassmorphism UI and animated aurora background.</p>
    {ticks(["<strong>Dashboard:</strong> weather, AQI monitor, Pomodoro timer, quick tasks", "<strong>Tools suite:</strong> QR generator, text analytics, color picker, password generator, converter, calculator, stopwatch", "<strong>Sticky notes:</strong> auto-saved in your browser"])}
    <div class="btn-row"><a class="btn" href="https://rajpratham1.github.io/Aether-Tools/" target="_blank" rel="noopener noreferrer">Launch Aether Tools</a></div></article>
  <article class="card reveal"><div class="icon" aria-hidden="true">🔒</div><h2 style="font-size:1.7rem">PrivyChat</h2>
    <p>An open-source, ephemeral messaging platform built on a zero-trust model.</p>
    {ticks(["<strong>Security:</strong> RAM-only architecture, in-browser end-to-end encryption, server relays only ciphertext", "<strong>Stealth suite:</strong> decoy calculator, panic button, ghost mode", "<strong>Messaging:</strong> 1v1 links, private rooms, voice notes, file sharing, WebRTC calls"])}
    <div class="btn-row"><a class="btn" href="https://privy-chat.onrender.com/" target="_blank" rel="noopener noreferrer">Launch PrivyChat</a></div></article>
</div></section>
{cta_band("Need a custom tool for your business?", "We build internal tools, dashboards and utilities tailored to your workflow.", "Discuss tool development")}
'''
build("tools.html", "Free Tools — Aether Tools & PrivyChat | WebFolio",
      "Free productivity and privacy tools built by WebFolio: Aether Tools dashboard and PrivyChat zero-trust messaging.", tools,
      schema={"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"SoftwareApplication","name":"Aether Tools","applicationCategory":"ProductivityApplication","operatingSystem":"Web","url":"https://rajpratham1.github.io/Aether-Tools/"},{"@type":"SoftwareApplication","name":"PrivyChat","applicationCategory":"CommunicationApplication","operatingSystem":"Web","url":"https://privy-chat.onrender.com/"}]})

# ───────────────────────── CONTACT ─────────────────────────
def opts(items):
    return '<option value="">Select…</option>' + "".join(f'<option value="{o}">{o}</option>' for o in items)
contact = page_hero("Contact", "Share your brief and get a clear plan.",
  "Website, Android app, redesign or maintenance — tell us what you need. We’ll reply within 24 hours with practical next steps.") + f'''
<section class="section" id="start"><div class="wrap contact-grid">
  <div class="reveal">
    <a class="channel" href="mailto:{EMAIL}"><span class="icon" aria-hidden="true">✉️</span><span><small>Email</small><strong>{EMAIL}</strong></span></a>
    <a class="channel" href="tel:{PHONE_TEL}"><span class="icon" aria-hidden="true">📞</span><span><small>Call</small><strong>{PHONE}</strong></span></a>
    <a class="channel" href="{WA}" target="_blank" rel="noopener noreferrer"><span class="icon" aria-hidden="true">💬</span><span><small>WhatsApp</small><strong>Chat directly</strong></span></a>
    <div class="panel" style="margin-top:1.4rem"><h3>What happens next</h3>
      <div class="steps" style="grid-template-columns:1fr;gap:.8rem;margin-top:1rem">
        <div class="step" style="padding:1rem"><strong style="color:var(--text)">Send brief</strong><p style="margin:0">Goals, pages needed and launch date.</p></div>
        <div class="step" style="padding:1rem"><strong style="color:var(--text)">Scope call</strong><p style="margin:0">Confirm priorities and timeline.</p></div>
        <div class="step" style="padding:1rem"><strong style="color:var(--text)">Kickoff</strong><p style="margin:0">Milestone-based production begins.</p></div>
      </div></div>
  </div>
  <form id="contactForm" class="panel form reveal" action="https://formsubmit.co/{EMAIL}" method="POST" novalidate>
    <input type="hidden" name="_captcha" value="false"><input type="hidden" name="_subject" value="New WebFolio project enquiry">
    <input type="hidden" name="_template" value="table"><input type="hidden" name="_next" value="{BASE}thank-you.html">
    <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div class="field"><label for="name">Full name</label><input id="name" name="name" type="text" required autocomplete="name" placeholder="Your name"></div>
    <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email" placeholder="you@email.com"></div>
    <div class="field"><label for="phone">Phone (optional)</label><input id="phone" name="phone" type="tel" autocomplete="tel" placeholder="+91 …"></div>
    <div class="field"><label for="bt">Business type</label><select id="bt" name="business_type" required>{opts(["Startup","Local business","Agency","Healthcare","Education","Other"])}</select></div>
    <div class="field"><label for="sv">Service needed</label><select id="sv" name="service" required>{opts(["Landing page","Business website","Portfolio website","Android app","Website + Android app","Redesign","Maintenance","Other"])}</select></div>
    <div class="field"><label for="bg">Budget range</label><select id="bg" name="budget_range" required>{opts(["Under 25k INR","25k – 60k INR","60k – 120k INR","120k+ INR","Not sure yet"])}</select></div>
    <div class="field full"><label for="tl">Preferred timeline</label><select id="tl" name="preferred_timeline" required>{opts(["Urgent (within 1 week)","2–4 weeks","1–2 months","Flexible"])}</select></div>
    <div class="field full"><label for="msg">Project details</label><textarea id="msg" name="message" required placeholder="What does your business do, who is it for, and what should visitors do? Mention pages, integrations, and whether you have content ready."></textarea></div>
    <div class="field full"><button class="btn" type="submit">Send message</button></div>
    <p id="formStatus" class="status" role="status" aria-live="polite"></p>
  </form>
</div></section>

<section class="section"><div class="wrap">
  {head_block("Tips for a faster quote", "What to include in your message", "", True)}
  <div class="grid g3">
    {card("🏷️", "Business context", "What you do, who your audience is, and what action you want visitors to take.")}
    {card("📄", "Scope &amp; content", "Number of pages, style references, integrations — and whether text and images are ready.")}
    {card("💰", "Budget &amp; timeline", "A range helps us prioritize features and give a realistic recommendation.")}
  </div>
</div></section>
'''
build("contact.html", "Contact & Start a Project | WebFolio",
      "Contact WebFolio for website development, Android apps or maintenance. Send a brief and get a clear plan within 24 hours.", contact)

# ───────────────────────── INTENT LANDING PAGES ─────────────────────────
def landing(name, title, desc, eyebrow, h1, lead, why, items, faq_pairs):
    body = page_hero(eyebrow, h1, lead) + f'''
<section class="section"><div class="wrap split">
  <div class="reveal"><h2>Why it matters</h2>{''.join(f"<p>{p}</p>" for p in why)}</div>
  <div class="panel reveal"><h3>What’s included</h3>{ticks(items)}
    <div class="btn-row"><a class="btn" href="contact.html#start">Start a project</a><a class="btn ghost" href="pricing.html">See pricing</a></div></div>
</div></section>
<section class="section"><div class="wrap">{head_block("Quick answers", "Good to know", "", True)}
<div class="faq reveal">{''.join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq_pairs)}</div></div></section>
{cta_band()}'''
    build(name, title, desc, body, active="services.html", prio="0.7")

landing("website-development.html", "Website Development Services | WebFolio",
  "Responsive, fast, conversion-focused website development for businesses that want measurable growth.",
  "Website development", "Websites built with clear business intent.",
  "We build responsive, fast, conversion-focused websites for businesses that want measurable growth — from compact landing pages to multi-page platforms.",
  ["A website is often the first impression customers get. We structure every page around one goal: helping visitors take action.",
   "Fast load times, clean hierarchy and mobile-first layouts keep people engaged — and help you rank."],
  ["Custom, brand-matched design", "Responsive on every device", "SEO metadata, schema and sitemap", "Forms, WhatsApp and call actions", "Performance and accessibility QA", "Handoff and launch support"],
  [("How long does it take?", "Landing pages: 7–10 days. Multi-page sites: 2–4 weeks."), ("Can you redesign my current site?", "Yes — we can restructure content, improve speed and refresh the design.")])
landing("android-app-development.html", "Android App Development (APK) | WebFolio",
  "Reliable, user-friendly Android APK apps — service workflows, dashboards and business tools.",
  "Android app development", "Android apps people actually enjoy using.",
  "From service workflows to operational dashboards, we design Android APK apps that are reliable, lightweight and easy to use.",
  ["App-first access suits teams in the field and customers on the move. We focus on practical features and smooth flow.",
   "We design for one-hand comfort and stable behavior on mid-range devices, with a structure that’s easy to extend."],
  ["Clean Material-style interface", "Lightweight, stable builds", "API and push-notification ready", "Scalable structure for future modules", "Matching website identity (optional)", "Maintenance and update support"],
  [("Do you also build the website?", "Yes — we can deliver a website and Android app together with a consistent brand."), ("Can the app grow later?", "Yes. We structure apps in modules so features can be added in phases.")])
landing("maintenance-support.html", "Website Maintenance & Support | WebFolio",
  "Monthly website and app maintenance: fixes, updates, QA checks and performance monitoring.",
  "Maintenance & support", "Keep your product fast, secure and current.",
  "We provide monthly maintenance with fixes, updates, QA checks and performance monitoring — for sites and apps we built, and for existing ones.",
  ["Websites need regular care. Small issues left alone become broken links, slow pages and outdated content.",
   "A steady maintenance plan keeps your brand modern, reliable and ready for new features."],
  ["Bug fixes and security-minded updates", "Speed and responsiveness checks", "Content and section updates", "Broken-link and health review", "Priority response for active clients", "Roadmap for new features"],
  [("Can you maintain a site you didn’t build?", "Yes. We’ll review it first and then propose a practical plan."), ("How fast do you respond?", "First response within 24 hours; critical fixes in 24–48 hours.")])

# ───────────────────────── CAREERS ─────────────────────────
career_schema = {
    "@context": "https://schema.org", "@type": "WebPage", "name": "Careers at WebFolio",
    "description": "Explore open roles and opportunities to work with WebFolio.",
    "url": BASE + "careers.html"
}
careers = f'''
{page_hero("Careers at WebFolio", "Build useful digital products with a thoughtful team.",
           "We are looking for curious builders who care about craft, clarity and the people who use what we make.", True)}
<section class="section"><div class="wrap">
  {head_block("Open opportunities", "Find your next meaningful challenge", "Our roles are practical, collaborative and focused on shipping work that creates real value.")}
  <div class="career-grid">
    <article class="career-role card reveal">
      <div class="role-top"><span class="pill">Full-time · Remote-friendly</span><span class="role-icon" aria-hidden="true">⌘</span></div>
      <h3>Frontend Developer</h3><p>Turn thoughtful designs into fast, accessible experiences across phones, tablets and desktops.</p>
      <div class="role-meta"><span>HTML · CSS · JavaScript</span><span>1–3 years</span></div>
      <a class="btn ghost" href="#apply">Apply for this role</a>
    </article>
    <article class="career-role card reveal">
      <div class="role-top"><span class="pill">Contract · Project-based</span><span class="role-icon" aria-hidden="true">✦</span></div>
      <h3>UI/UX Designer</h3><p>Shape clear, confident interfaces and systems that help businesses serve their customers better.</p>
      <div class="role-meta"><span>Figma · Design systems</span><span>2+ years</span></div>
      <a class="btn ghost" href="#apply">Apply for this role</a>
    </article>
    <article class="career-role card reveal">
      <div class="role-top"><span class="pill">Freelance · Flexible</span><span class="role-icon" aria-hidden="true">↗</span></div>
      <h3>Android Developer</h3><p>Build reliable mobile workflows and lightweight apps that feel great on everyday devices.</p>
      <div class="role-meta"><span>Kotlin · Android</span><span>2+ years</span></div>
      <a class="btn ghost" href="#apply">Apply for this role</a>
    </article>
  </div>
</div></section>
<section class="section"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">How we hire</span><h2>A clear process, from hello to first commit.</h2>
    <p>We value honest conversations over lengthy tests. Tell us what you have built, what you want to learn and how you like to work.</p>
  </div>
  <div class="steps career-steps">
    <div class="step reveal"><h3>Introduce yourself</h3><p>Send your profile, portfolio or GitHub through our contact portal.</p></div>
    <div class="step reveal"><h3>Meet the team</h3><p>Have a practical conversation about your work and goals.</p></div>
    <div class="step reveal"><h3>Try a small task</h3><p>Only when useful, we share a focused, time-boxed exercise.</p></div>
    <div class="step reveal"><h3>Start well</h3><p>Get a clear brief, a point of contact and room to do your best work.</p></div>
  </div>
</div></section>
<section class="section" id="apply"><div class="wrap">
  {head_block("Student applications", "Start your journey with WebFolio", "Share your details and attach your resume. We review every application and reply through email.")}
  <form id="careerForm" class="panel form career-form reveal" action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
    <input type="hidden" name="_subject" value="New WebFolio career application">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_next" value="{BASE}careers.html?sent=1#apply">
    <div class="field"><label for="careerName">Full name *</label><input id="careerName" name="name" required autocomplete="name" placeholder="Your full name"></div>
    <div class="field"><label for="careerEmail">Email address *</label><input id="careerEmail" type="email" name="email" required autocomplete="email" placeholder="you@example.com"></div>
    <div class="field"><label for="careerPhone">Phone number</label><input id="careerPhone" type="tel" name="phone" autocomplete="tel" placeholder="+91"></div>
    <div class="field"><label for="careerRole">Role you’re interested in *</label><select id="careerRole" name="role" required><option value="">Choose a role</option><option>Frontend Developer</option><option>UI/UX Designer</option><option>Android Developer</option><option>Future opportunity / Internship</option></select></div>
    <div class="field"><label for="careerEducation">Education / current year *</label><input id="careerEducation" name="education" required placeholder="BCA, final year / self-taught"></div>
    <div class="field"><label for="careerPortfolio">Portfolio or GitHub URL</label><input id="careerPortfolio" type="url" name="portfolio" placeholder="https://"></div>
    <div class="field full"><label for="careerResume">Resume / CV * <span class="field-hint">PDF, DOC or DOCX · max 5 MB</span></label><input id="careerResume" type="file" name="attachment" accept=".pdf,.doc,.docx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document" required></div>
    <div class="field full"><label for="careerMessage">Tell us about yourself *</label><textarea id="careerMessage" name="message" required placeholder="What have you built, and what would you like to learn?"></textarea></div>
    <p class="form-note">By submitting, you agree that WebFolio may use these details to review your application and contact you about opportunities.</p>
    <div class="field full"><button class="btn" type="submit">Submit application</button></div>
  </form>
</div></section>
{cta_band("Think you could make WebFolio better?", "Share your portfolio, GitHub or a short note about the kind of work you want to do. We will get back to you through our usual contact portal.", "Send your profile")}
'''
build("careers.html", "Careers at WebFolio | Join Our Team",
      "Explore careers at WebFolio. Join a thoughtful, remote-friendly team building websites, Android apps and digital products.",
      careers, active="careers.html", schema=career_schema, prio="0.7")

# ───────────────────────── LEGAL / UTILITY ─────────────────────────
def prose(eyebrow, h1, sections, note):
    body = f'''<section class="page-hero"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">Last updated: {UPDATED}</p></div></section>
<section class="section"><div class="wrap prose">{''.join(f"<h2>{h}</h2><p>{p}</p>" for h, p in sections)}<p>{note}</p></div></section>'''
    return body
build("privacy.html", "Privacy Policy | WebFolio", "How WebFolio collects, uses and protects the information you share.",
  prose("Privacy", "Your data is handled responsibly.", [
   ("Information we collect", "Name, email, phone, service requirement and project details submitted through our forms."),
   ("How we use it", "To contact you, prepare proposals and provide project or maintenance services."),
   ("Sharing", "We do not sell personal data. Form submissions are processed by FormSubmit solely to deliver them to our inbox."),
   ("Analytics", "We may use Google Analytics to understand aggregate usage and improve the site."),
   ("Your rights", "You can ask us to update or delete your information at any time.")],
   f'Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>'), prio="0.3")
build("terms.html", "Terms of Service | WebFolio", "Project scope, revisions, payments and support terms for WebFolio services.",
  prose("Terms", "Clear terms for transparent collaboration.", [
   ("Scope and deliverables", "Final scope is based on the agreed pages, features and approved requirements."),
   ("Revisions", "Reasonable revision rounds are included per the selected plan."),
   ("Payments", "Milestone-based payments are used. Work starts after initial confirmation."),
   ("Support and maintenance", "Post-launch support terms depend on the selected maintenance package."),
   ("Client responsibilities", "The client provides timely content, approvals and required assets.")],
   f'Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>'), prio="0.3")

# thank-you & 404 (noindex, not in sitemap)
write("thank-you.html", head("Thank you | WebFolio", "Your message has been received.", "thank-you.html", noindex=True) + header("") + f'''
<section class="page-hero"><div class="wrap" style="text-align:center"><span class="eyebrow">Message sent</span>
<h1 style="margin-inline:auto">Thank you — we’ve got your message.</h1>
<p class="lead" style="margin-inline:auto">We’ll review your brief and reply by email or phone, usually within 24 hours.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="{WA}" target="_blank" rel="noopener noreferrer">Message us on WhatsApp</a><a class="btn ghost" href="index.html">Back to home</a></div></div></section>
<section class="section"><div class="wrap"><p style="text-align:center">First time using the form? Check your inbox once for a FormSubmit confirmation email.</p></div></section>''' + FOOTER)
head_404 = head("Page not found | WebFolio", "The page you’re looking for doesn’t exist.", "404.html", noindex=True).replace('<head>\n', '<head>\n<script>var b=(location.pathname.indexOf("/my-portfolio")===0)?"/my-portfolio/":"/";document.write("<base href=\\""+b+"\\">");</script>\n')
write("404.html", head_404 + header("") + '''
<section class="page-hero"><div class="wrap" style="text-align:center"><span class="eyebrow">404</span>
<h1 style="margin-inline:auto">This page took a wrong turn.</h1>
<p class="lead" style="margin-inline:auto">The link may be outdated or the page has moved. Let’s get you back on track.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="index.html">Go home</a><a class="btn ghost" href="contact.html">Contact us</a></div></div></section>''' + FOOTER)

# ───────────────────────── REDIRECT STUBS (keep old URLs alive) ─────────────────────────
REDIRECTS = {"hire.html": "contact.html", "dedication.html": "about.html", "process.html": "services.html",
             "showcase.html": "work.html", "testimonials.html": "work.html", "performance.html": "about.html#quality",
             "release-checklist.html": "about.html", "changelog.html": "index.html"}
for old, new in REDIRECTS.items():
    write(old, f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Redirecting…</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{BASE}{new}">
<meta http-equiv="refresh" content="0; url={new}"><script>location.replace("{new}")</script></head>
<body><p>This page has moved to <a href="{new}">{new}</a>.</p></body></html>
''')

# ───────────────────────── SITEMAP + ROBOTS ─────────────────────────
urls = "".join(f"  <url><loc>{BASE}{'' if n=='index.html' else n}</loc><lastmod>{UPDATED}</lastmod><priority>{p}</priority></url>\n" for n, p in PAGES.items())
write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_internal/\n\nSitemap: {BASE}sitemap.xml\n")
print("Built", len(PAGES), "indexed pages +", len(REDIRECTS), "redirects")

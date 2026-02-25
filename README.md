# WebFolio

WebFolio is a multi-page portfolio and agency-style website focused on:

- business-first presentation
- conversion-oriented section flow
- responsive behavior on mobile/tablet/desktop
- SEO-ready static architecture
- maintainable frontend-only stack (no database required)

---

## 1) Current Scope

This build includes marketing pages, trust pages, operational pages, and intent-based landing pages for service SEO.

### Main Pages

- `index.html` - primary landing and overview
- `about.html` - team and positioning
- `services.html` - service scope, packages, SLA, trust assets
- `work.html` - portfolio delivery narrative + measurable case studies
- `dedication.html`
- `process.html`
- `showcase.html`
- `testimonials.html`
- `pricing.html`
- `faq.html` - interactive FAQ with keyboard support
- `contact.html` - FormSubmit-based lead form and direct contact actions
- `hire.html`

### Support / Utility Pages

- `tools.html` - curated external tools through WebFolio
- `performance.html` - Lighthouse and Core Web Vitals targets
- `release-checklist.html` - monthly QA/release checklist
- `website-development.html` - intent page
- `android-app-development.html` - intent page
- `maintenance-support.html` - intent page
- `changelog.html`
- `thank-you.html`
- `privacy.html`
- `terms.html`
- `404.html`

---

## 2) Tech Stack

- HTML5 (static multipage)
- CSS3 (single design system file)
- Vanilla JavaScript (`assets/js/main.js`)
- FormSubmit for contact form handling
- GA4 placeholder integration (`G-XXXXXXXXXX`)

No backend or database is required.

---

## 3) Core Features

### UX / Motion

- sticky header with responsive navigation
- smooth reveal/counter effects
- scroll progress indicator
- ripple/magnetic CTA effects
- mobile quick contact bar
- desktop quick conversion CTA
- reduced-motion accessibility fallback

### Conversion + Trust

- one primary CTA pattern (`Start Project`)
- productized packages (Starter / Growth / Pro)
- SLA and maintenance scope table
- case studies with before/after KPI examples
- trust logo strip and testimonial support

### Contact Funnel

`contact.html` includes qualification fields:

- business type
- service needed
- budget range
- preferred timeline
- project message

Form destination:

- `https://formsubmit.co/shrivastavapratham40@gmail.com`

### SEO

Every HTML page includes:

- unique `<title>`
- meta description
- canonical URL
- robots
- Open Graph tags
- Twitter Card tags
- `author`, `keywords`, `og:locale`, `twitter:creator`

Additional structured data:

- `Organization` (site-wide)
- `Service` (services page)
- `FAQPage` (faq page)
- `SoftwareApplication` (tools page)

---

## 4) Project Structure

```text
WebFolio/
├─ assets/
│  ├─ css/
│  │  └─ styles.css
│  ├─ data/
│  │  └─ testimonials.json
│  ├─ js/
│  │  └─ main.js
│  └─ logo/
│     └─ webfolio-mark.svg
├─ *.html (23 pages)
├─ sitemap.xml
├─ robots.txt
└─ README.md
```

---

## 5) Local Development

Use a local server (recommended), not direct `file://` browsing.

### Option A: VS Code Live Server

- open project in VS Code
- run Live Server on `WebFolio/`
- open `http://localhost:5500/index.html`

### Option B: Python

```bash
cd WebFolio
python -m http.server 5500
```

Then open:

- `http://localhost:5500/index.html`

---

## 6) Deployment

Static hosting compatible:

- GitHub Pages
- Netlify
- Vercel static
- any Nginx/Apache static host

After deploy, confirm:

- canonical URLs match live domain
- sitemap URL in `robots.txt` is correct
- FormSubmit `_next` URL points to live `thank-you.html`

---

## 7) Configuration Checklist

Before production, update:

1. GA4 ID  
Replace all `G-XXXXXXXXXX` with your measurement ID.

2. Canonical base domain  
Ensure all canonical and OG URLs use your final domain.

3. FormSubmit first-time verification  
Complete confirmation mail once, then submissions go live.

4. Social handles  
Update `@webfolio` to your real profile if needed.

---

## 8) QA Checklist (Recommended per release)

- responsive check: 360px / 768px / 1024px / 1440px
- keyboard navigation and focus visibility
- form validation and success/failure behavior
- page speed and Core Web Vitals sanity check
- footer/nav consistency on all pages
- schema and metadata presence
- broken links (internal + external)

---

## 9) Known Notes

- FormSubmit and some fetch-based interactions can behave differently in `file://` mode. Always test from a local server.
- Image conversion to WebP/AVIF can be added later when tooling is available in the environment.

---

## 10) Ownership / Contact

- Founder: Pratham Kumar
- Portfolio: `https://rajpratham1.github.io/my-portfolio/`
- GitHub: `https://github.com/rajpratham1`
- Email: `shrivastavapratham40@gmail.com`
- Phone: `+91-6200892887`

---

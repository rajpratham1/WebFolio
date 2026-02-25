# WebFolio Multi-Page Portfolio

WebFolio is a responsive multi-page portfolio website focused on premium presentation, smooth motion, conversion-first UX, and long-term maintainability.

## Pages

1. `index.html`
2. `about.html`
3. `services.html`
4. `work.html`
5. `dedication.html`
6. `process.html`
7. `showcase.html`
8. `testimonials.html`
9. `pricing.html`
10. `faq.html`
11. `contact.html`
12. `hire.html`
13. `thank-you.html`
14. `privacy.html`
15. `terms.html`

## Tech Stack

- HTML5
- CSS3 (custom design system and motion system)
- JavaScript (navigation, reveal effects, counters, tracking hooks)
- FormSubmit (direct message handling)

## Visual and UX Improvements

- Unique themed look on each page using page-level color tokens
- Smooth reveal animations with IntersectionObserver
- Animated metric counters and trust/proof blocks
- Scroll progress indicator, ripple clicks, hover depth, and dynamic effects
- Responsive navigation with mobile menu behavior
- Skip link, visible focus states, breadcrumbs, and reduced-motion support
- Unified header/footer with legal page links
- FormSubmit flow redirected to `thank-you.html`
- SEO baseline on each page: canonical, Open Graph, Twitter cards, JSON-LD
- Analytics scaffold (GA4 placeholder + CTA/contact event hooks)

## Project Structure

```text
WebFolio/
|- index.html
|- about.html
|- services.html
|- work.html
|- dedication.html
|- process.html
|- showcase.html
|- testimonials.html
|- pricing.html
|- faq.html
|- contact.html
|- hire.html
|- thank-you.html
|- privacy.html
|- terms.html
|- assets/
|  |- css/
|  |  |- styles.css
|  |- js/
|  |  |- main.js
|  |- logo/
|     |- webfolio-mark.svg
|- sitemap.xml
|- README.md
```

## Setup Notes

- Replace `G-XXXXXXXXXX` in every page with your real GA4 Measurement ID.
- First FormSubmit message may require email verification from FormSubmit.

## Run Locally

Open `index.html` in a browser, or run any static local server.

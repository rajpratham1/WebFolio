/* WebFolio — lightweight interactions (no dependencies) */
(() => {
  const doc = document;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const track = (name, params = {}) => { if (typeof window.gtag === 'function') window.gtag('event', name, params); };
  const EMAIL = 'shrivastavapratham40@gmail.com';

  /* Theme follows the OS until the visitor chooses a preference. */
  const root = doc.documentElement;
  const themeKey = 'webfolio-theme';
  const systemTheme = matchMedia('(prefers-color-scheme: light)');
  const themeButton = doc.createElement('button');
  themeButton.className = 'theme-toggle';
  themeButton.type = 'button';
  themeButton.innerHTML = '<span class="moon" aria-hidden="true">☾</span><span class="sun" aria-hidden="true">☀</span><span class="theme-label">Theme</span>';
  const updateThemeButton = () => {
    const light = root.getAttribute('data-theme') === 'light';
    themeButton.setAttribute('aria-label', `Switch to ${light ? 'dark' : 'light'} theme`);
    themeButton.title = `Switch to ${light ? 'dark' : 'light'} theme`;
  };
  const savedTheme = localStorage.getItem(themeKey);
  const initialTheme = savedTheme === 'light' || savedTheme === 'dark'
    ? savedTheme
    : (systemTheme.matches ? 'light' : 'dark');
  root.setAttribute('data-theme', initialTheme);
  const nav = doc.querySelector('.nav-links');
  const cta = nav && nav.querySelector('.btn');
  if (nav && cta) nav.insertBefore(themeButton, cta);
  themeButton.addEventListener('click', () => {
    const next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    localStorage.setItem(themeKey, next);
    updateThemeButton();
  });
  updateThemeButton();
  systemTheme.addEventListener('change', () => {
    if (!localStorage.getItem(themeKey)) {
      root.setAttribute('data-theme', systemTheme.matches ? 'light' : 'dark');
      updateThemeButton();
    }
  });
  root.classList.remove('no-js');
  doc.body.classList.add('motion-ready');

  /* Header state + scroll progress */
  const header = doc.querySelector('.site-header');
  const bar = doc.createElement('div');
  bar.className = 'progress';
  doc.body.appendChild(bar);
  const onScroll = () => {
    const max = doc.documentElement.scrollHeight - innerHeight;
    bar.style.width = (max > 0 ? Math.min(scrollY / max * 100, 100) : 0) + '%';
    header && header.classList.toggle('scrolled', scrollY > 12);
  };
  onScroll();
  addEventListener('scroll', onScroll, { passive: true });

  /* Keep ambient motion on one animation frame and only enable pointer glow on fine pointers. */
  if (!reduce && matchMedia('(pointer: fine)').matches && innerWidth > 820) {
    const cards = doc.querySelectorAll('.card');
    cards.forEach((card) => {
      card.addEventListener('pointermove', (e) => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--pointer-x', `${e.clientX - rect.left}px`);
        card.style.setProperty('--pointer-y', `${e.clientY - rect.top}px`);
      });
      card.addEventListener('pointerleave', () => {
        card.style.removeProperty('--pointer-x');
        card.style.removeProperty('--pointer-y');
      });
    });
    let frame = 0;
    addEventListener('scroll', () => {
      if (frame) return;
      frame = requestAnimationFrame(() => {
        root.style.setProperty('--scroll-y', `${Math.min(scrollY * .04, 36)}px`);
        root.style.setProperty('--scroll-x', `${Math.sin(scrollY / 900) * 12}px`);
        frame = 0;
      });
    }, { passive: true });
    let pointerFrame = 0;
    let pointerX = 0;
    let pointerY = 0;
    addEventListener('pointermove', (e) => {
      pointerX = e.clientX;
      pointerY = e.clientY;
      if (pointerFrame) return;
      pointerFrame = requestAnimationFrame(() => {
        root.style.setProperty('--spot-x', `${pointerX}px`);
        root.style.setProperty('--spot-y', `${pointerY}px`);
        pointerFrame = 0;
      });
    }, { passive: true });

    /* Small magnetic pull for primary actions; it never changes document layout. */
    const magneticButtons = doc.querySelectorAll('.btn:not(.ghost):not(.theme-toggle)');
    magneticButtons.forEach((button) => {
      button.classList.add('magnetic');
      button.addEventListener('pointermove', (e) => {
        const rect = button.getBoundingClientRect();
        const x = (e.clientX - (rect.left + rect.width / 2)) / rect.width;
        const y = (e.clientY - (rect.top + rect.height / 2)) / rect.height;
        button.style.transform = `translate(${x * 5}px, ${y * 4}px) translateY(-2px)`;
      });
      button.addEventListener('pointerleave', () => {
        button.style.removeProperty('transform');
      });
    });
  }

  /* Mobile navigation */
  const toggle = doc.querySelector('.nav-toggle');
  const links = doc.querySelector('.nav-links');
  if (toggle && links) {
    const set = (open) => { links.classList.toggle('open', open); toggle.setAttribute('aria-expanded', open); };
    toggle.addEventListener('click', () => set(!links.classList.contains('open')));
    links.addEventListener('click', (e) => e.target.closest('a') && set(false));
    addEventListener('keydown', (e) => e.key === 'Escape' && set(false));
  }

  /* Reveal on scroll */
  const items = doc.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    items.forEach((el, index) => el.style.setProperty('--reveal-delay', `${Math.min(index % 5, 4) * 70}ms`));
    const io = new IntersectionObserver((entries) => entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    }), { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach((el) => io.observe(el));
  } else items.forEach((el) => el.classList.add('in'));

  /* Animated counters: <b data-count="7" data-suffix=" days"> */
  const count = (el) => {
    const target = Number(el.dataset.count), suffix = el.dataset.suffix || '', t0 = performance.now();
    if (reduce) { el.textContent = target + suffix; return; }
    const tick = (now) => {
      const p = Math.min((now - t0) / 1100, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + (p === 1 ? suffix : '');
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  const counters = doc.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    const co = new IntersectionObserver((entries) => entries.forEach((en) => {
      if (en.isIntersecting) { count(en.target); co.unobserve(en.target); }
    }), { threshold: 0.6 });
    counters.forEach((el) => co.observe(el));
  } else counters.forEach((el) => { el.textContent = el.dataset.count + (el.dataset.suffix || ''); });

  /* Year */
  doc.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* Event tracking for key conversions */
  doc.addEventListener('click', (e) => {
    const a = e.target.closest('a'); if (!a) return;
    const h = a.getAttribute('href') || '';
    if (h.startsWith('tel:')) track('call_click');
    else if (h.startsWith('mailto:')) track('email_click');
    else if (h.includes('wa.me')) track('whatsapp_click');
    else if (a.classList.contains('btn')) track('cta_click', { label: a.textContent.trim(), href: h });
  });

  /* Testimonials (renders only if assets/data/testimonials.json has entries) */
  const tHost = doc.getElementById('testimonials');
  if (tHost) {
    fetch('assets/data/testimonials.json').then((r) => r.json()).then((list) => {
      if (!Array.isArray(list) || !list.length) return;
      const grid = tHost.querySelector('.grid');
      const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
      grid.innerHTML = list.map((t) => `
        <article class="card quote">
          <div class="stars" aria-label="${Number(t.rating || 5)} out of 5">${'★'.repeat(Number(t.rating || 5))}</div>
          <q>${esc(t.quote)}</q>
          <div class="who"><strong>${esc(t.name)}</strong> · ${esc(t.role)}</div>
        </article>`).join('');
      tHost.hidden = false;
    }).catch(() => {});
  }

  /* Contact form */
  const form = doc.getElementById('contactForm');
  if (form) {
    const status = doc.getElementById('formStatus');
    const btn = form.querySelector('button[type="submit"]');
    const say = (msg, cls) => { status.textContent = msg; status.className = 'status ' + (cls || ''); };
    form.addEventListener('input', (e) => e.target.checkValidity() && e.target.removeAttribute('aria-invalid'));
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const bad = [...form.elements].filter((f) => f.willValidate && !f.checkValidity());
      bad.forEach((f) => f.setAttribute('aria-invalid', 'true'));
      if (bad.length) { bad[0].focus(); say('Please complete the highlighted fields.', 'err'); return; }
      if (location.protocol === 'file:') { say('Open the site through a local server (python -m http.server) to test the form.', 'err'); return; }
      const label = btn.textContent; btn.disabled = true; btn.textContent = 'Sending…'; say('Sending your message…');
      try {
        const res = await fetch('https://formsubmit.co/ajax/' + EMAIL, {
          method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(Object.fromEntries(new FormData(form)))
        });
        const out = await res.json().catch(() => ({}));
        if (res.ok && out.success !== 'false') { track('contact_submit'); location.href = 'thank-you.html'; return; }
        say('Could not send right now. Please use WhatsApp or email instead.', 'err');
      } catch (_) {
        form.submit(); return; /* fall back to normal POST */
      }
      btn.disabled = false; btn.textContent = label;
    });
  }

  /* Career applications use native multipart submission so resume files are preserved. */
  const careerForm = doc.getElementById('careerForm');
  if (careerForm) {
    const showCareerSuccess = () => {
      careerForm.innerHTML = `
        <div class="form-success" role="status" aria-live="polite">
          <div class="success-icon" aria-hidden="true">✓</div>
          <span class="eyebrow">Application received</span>
          <h3>Thank you — we received your response.</h3>
          <p>We'll review your application and resume, then contact you by email if your profile matches an opportunity.</p>
          <a class="btn ghost" href="careers.html">View careers again</a>
        </div>`;
      careerForm.classList.add('submitted');
    };
    if (new URLSearchParams(location.search).get('sent') === '1') showCareerSuccess();
    careerForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const resume = careerForm.querySelector('input[type="file"]');
      if (resume && resume.files[0] && resume.files[0].size > 5 * 1024 * 1024) {
        resume.setCustomValidity('Please choose a resume smaller than 5 MB.');
        resume.reportValidity();
        resume.setCustomValidity('');
        return;
      }
      const btn = careerForm.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = 'Submitting…'; }
      const next = careerForm.querySelector('input[name="_next"]');
      if (next) next.value = `${location.origin}${location.pathname}?sent=1#apply`;
      try {
        const res = await fetch(careerForm.action, {
          method: 'POST',
          headers: { Accept: 'application/json' },
          body: new FormData(careerForm)
        });
        const out = await res.json().catch(() => ({}));
        if (res.ok && out.success !== 'false') {
          track('career_application_submit');
          showCareerSuccess();
          return;
        }
      } catch (_) {
        careerForm.submit();
        return;
      }
      if (btn) { btn.disabled = false; btn.textContent = 'Submit application'; }
    });
    const resumeInput = careerForm.querySelector('input[type="file"]');
    if (resumeInput) resumeInput.addEventListener('change', (e) => {
      e.target.setCustomValidity('');
    });
  }

  /* ═══════════════════════════════════════════════
     ENHANCED ANIMATIONS & INTERACTIONS (new block)
  ═══════════════════════════════════════════════ */
  if (reduce) return; /* respect reduced-motion for all enhancements below */

  /* ── 1. Hero typewriter cursor ── */
  const heroH1 = doc.querySelector('.hero h1');
  if (heroH1) {
    const cursor = doc.createElement('span');
    cursor.className = 'hero-cursor';
    cursor.setAttribute('aria-hidden', 'true');
    heroH1.appendChild(cursor);
  }

  /* ── 2. Scroll-hint indicator below hero CTAs ── */
  const heroBtnRow = doc.querySelector('.hero .btn-row');
  if (heroBtnRow) {
    const hint = doc.createElement('div');
    hint.className = 'scroll-hint';
    hint.setAttribute('aria-hidden', 'true');
    hint.innerHTML = '<div class="wheel"></div><span>Scroll</span>';
    heroBtnRow.parentNode.insertBefore(hint, heroBtnRow.nextSibling);
    /* hide after first scroll */
    const hideHint = () => { hint.style.opacity = '0'; hint.style.transition = 'opacity .5s'; };
    addEventListener('scroll', hideHint, { once: true, passive: true });
  }

  /* ── 3. 3D card tilt on mouse move ── */
  if (matchMedia('(pointer: fine)').matches && innerWidth > 820) {
    doc.querySelectorAll('.card').forEach((card) => {
      card.classList.add('tilt');
      card.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        const nx = (e.clientX - r.left) / r.width  - 0.5;
        const ny = (e.clientY - r.top)  / r.height - 0.5;
        card.style.transform = `translateY(-4px) rotateY(${nx * 8}deg) rotateX(${-ny * 6}deg)`;
      });
      card.addEventListener('pointerleave', () => {
        card.style.transform = '';
      });
    });
  }

  /* ── 4. Stagger-wave reveal for grids ── */
  if ('IntersectionObserver' in window) {
    const grids = doc.querySelectorAll('.grid,.steps,.career-grid');
    const staggerIO = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          en.target.classList.add('stagger-wave');
          staggerIO.unobserve(en.target);
        }
      });
    }, { threshold: 0.08 });
    grids.forEach((g) => staggerIO.observe(g));
  }

  /* ── 5. Hero stats glow when in view ── */
  const heroStats = doc.querySelector('.hero-stats');
  if (heroStats && 'IntersectionObserver' in window) {
    const hsIO = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('in-view'); hsIO.unobserve(en.target); }
      });
    }, { threshold: 0.5 });
    hsIO.observe(heroStats);
  }

  /* ── 6. Stat-strip b glow ── */
  doc.querySelectorAll('.stat-strip b').forEach((b) => {
    if ('IntersectionObserver' in window) {
      const io2 = new IntersectionObserver((entries) => {
        entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in-view'); io2.unobserve(en.target); } });
      }, { threshold: 0.7 });
      io2.observe(b);
    }
  });

  /* ── 7. Cursor trail sparks (fine pointer only) ── */
  if (matchMedia('(pointer: fine)').matches && innerWidth > 820) {
    let trailTime = 0;
    addEventListener('pointermove', (e) => {
      const now = Date.now();
      if (now - trailTime < 55) return;
      trailTime = now;
      const dot = doc.createElement('div');
      dot.className = 'cursor-trail';
      dot.style.left = e.clientX + 'px';
      dot.style.top  = e.clientY + 'px';
      doc.body.appendChild(dot);
      setTimeout(() => dot.remove(), 580);
    }, { passive: true });
  }

  /* ── 8. Sparkle burst on primary CTA clicks ── */
  const SPARKLES = ['✦','✧','⋆','·','★'];
  doc.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn:not(.ghost):not(.theme-toggle)');
    if (!btn) return;
    const rect = btn.getBoundingClientRect();
    const cx = rect.left + rect.width  / 2;
    const cy = rect.top  + rect.height / 2;
    for (let i = 0; i < 7; i++) {
      const s = doc.createElement('span');
      s.className = 'sparkle';
      s.textContent = SPARKLES[Math.floor(Math.random() * SPARKLES.length)];
      const angle = (Math.PI * 2 / 7) * i;
      const dist  = 28 + Math.random() * 22;
      s.style.cssText = `left:${cx}px;top:${cy}px;color:${['var(--a)','var(--b)','var(--c)'][i % 3]};` +
        `transform:translate(${Math.cos(angle)*dist}px,${Math.sin(angle)*dist}px)`;
      doc.body.appendChild(s);
      setTimeout(() => s.remove(), 650);
    }
  });

  /* ── 9. Floating ambient particles ── */
  if (innerWidth > 820) {
    const COUNT = 8;
    const particles = [];
    for (let i = 0; i < COUNT; i++) {
      const p = doc.createElement('div');
      p.className = 'particle';
      const size = 3 + Math.random() * 5;
      p.style.cssText = `width:${size}px;height:${size}px;` +
        `left:${Math.random() * 100}vw;top:${Math.random() * 100}vh;` +
        `opacity:${0.05 + Math.random() * 0.1}`;
      doc.body.appendChild(p);
      particles.push({ el: p, x: Math.random() * innerWidth, y: Math.random() * innerHeight,
        vx: (Math.random() - .5) * .35, vy: (Math.random() - .5) * .35 });
    }
    const animParticles = () => {
      particles.forEach((p) => {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > innerWidth)  p.vx *= -1;
        if (p.y < 0 || p.y > innerHeight) p.vy *= -1;
        p.el.style.transform = `translate(${p.x - parseFloat(p.el.style.width)/2}px,${p.y - parseFloat(p.el.style.height)/2}px)`;
      });
      requestAnimationFrame(animParticles);
    };
    requestAnimationFrame(animParticles);
  }

  /* ── 10. Parallax depth on hero stage ── */
  const stage = doc.querySelector('.stage');
  if (stage && matchMedia('(pointer: fine)').matches) {
    let pf = 0;
    addEventListener('pointermove', (e) => {
      if (pf) return;
      pf = requestAnimationFrame(() => {
        const nx = (e.clientX / innerWidth  - .5) * 2;
        const ny = (e.clientY / innerHeight - .5) * 2;
        stage.style.transform = `perspective(900px) rotateY(${nx * 4}deg) rotateX(${-ny * 3}deg)`;
        pf = 0;
      });
    }, { passive: true });
    stage.addEventListener('mouseleave', () => { stage.style.transform = ''; });
  }

  /* ── 11. Text scramble on eyebrows when revealed ── */
  const CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789·✦';
  const scramble = (el) => {
    const original = el.dataset.text || el.textContent;
    el.dataset.text = original;
    let iter = 0;
    const interval = setInterval(() => {
      el.textContent = original.split('').map((ch, idx) => {
        if (ch === ' ') return ' ';
        if (idx < iter) return original[idx];
        return CHARS[Math.floor(Math.random() * CHARS.length)];
      }).join('');
      iter += .6;
      if (iter >= original.length) { el.textContent = original; clearInterval(interval); }
    }, 28);
  };

  if ('IntersectionObserver' in window) {
    const eyebrows = doc.querySelectorAll('.section-head .eyebrow, .page-hero .eyebrow');
    const eyeIO = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { scramble(en.target); eyeIO.unobserve(en.target); }
      });
    }, { threshold: 0.5 });
    eyebrows.forEach((e) => eyeIO.observe(e));
  }

})();

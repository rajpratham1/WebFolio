document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('page-ready');
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isCoarsePointer = window.matchMedia('(pointer: coarse)').matches;
  const enableHeavyMotion = !prefersReducedMotion && !isCoarsePointer;
  const header = document.querySelector('.site-header');
  let dynamicBg = null;

  const trackEvent = (name, params = {}) => {
    if (typeof window.gtag === 'function') {
      window.gtag('event', name, params);
    }
  };

  const progress = document.createElement('div');
  progress.className = 'scroll-progress';
  document.body.appendChild(progress);

  const transitionLayer = document.createElement('div');
  transitionLayer.className = 'page-transition';
  document.body.appendChild(transitionLayer);

  const bgGrid = document.createElement('div');
  bgGrid.className = 'dynamic-grid';
  document.body.appendChild(bgGrid);

  if (enableHeavyMotion) {
    dynamicBg = document.createElement('div');
    dynamicBg.className = 'dynamic-bg';
    dynamicBg.innerHTML = '<span class="orb one"></span><span class="orb two"></span>';
    document.body.appendChild(dynamicBg);

    const cursorGlow = document.createElement('div');
    cursorGlow.className = 'cursor-glow';
    document.body.appendChild(cursorGlow);

    window.addEventListener('pointermove', (event) => {
      cursorGlow.style.left = `${event.clientX}px`;
      cursorGlow.style.top = `${event.clientY}px`;
    }, { passive: true });
  }

  if (!prefersReducedMotion) {
    document.querySelectorAll('a[href$=".html"], a[href="index.html"]').forEach((link) => {
      link.addEventListener('click', (event) => {
        const href = link.getAttribute('href');
        if (!href || href.startsWith('http') || event.ctrlKey || event.metaKey || event.shiftKey) {
          return;
        }
        event.preventDefault();
        document.body.classList.add('page-exit');
        setTimeout(() => {
          window.location.href = href;
        }, 180);
      });
    });
  }

  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
    navLinks.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => navLinks.classList.remove('open'));
    });
  }

  const currentFile = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('a[data-nav]').forEach((link) => {
    const file = link.getAttribute('href');
    if (file === currentFile) {
      link.classList.add('active');
    }
  });

  const revealItems = document.querySelectorAll('.reveal');
  if (revealItems.length) {
    revealItems.forEach((item, idx) => {
      item.style.transitionDelay = `${Math.min(idx * 70, 280)}ms`;
    });

    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.16 });

    revealItems.forEach((item) => io.observe(item));
  }

  const counters = document.querySelectorAll('[data-count]');
  const animateCounter = (el) => {
    const target = Number(el.dataset.count || '0');
    const duration = 1000;
    const start = performance.now();

    const tick = (now) => {
      const progressTime = Math.min((now - start) / duration, 1);
      const value = Math.floor(progressTime * target);
      el.textContent = value.toString();
      if (progressTime < 1) {
        requestAnimationFrame(tick);
      } else {
        const suffix = el.dataset.suffix || '';
        el.textContent = `${target}${suffix}`;
        const metric = el.closest('.metric');
        if (metric) {
          metric.classList.add('done');
        }
      }
    };
    requestAnimationFrame(tick);
  };

  if (counters.length) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach((counter) => counterObserver.observe(counter));
  }

  const headerEl = document.querySelector('.site-header');
  if (headerEl && !document.querySelector('.global-support-line')) {
    const support = document.createElement('div');
    support.className = 'global-support-line';
    support.innerHTML = '<div class="container"><p>Website Development + Android APK Development + Maintenance Support. We are happy to help you at every stage.</p></div>';
    headerEl.insertAdjacentElement('afterend', support);
  }

  document.querySelectorAll('.hero-art').forEach((art) => {
    if (!art.querySelector('.hero-chip-row')) {
      const chips = document.createElement('div');
      chips.className = 'hero-chip-row';
      chips.innerHTML = '<span>App Development</span><span>UI/UX Polish</span><span>Maintenance</span>';
      art.appendChild(chips);
    }
  });

  const updateProgress = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = max > 0 ? (window.scrollY / max) * 100 : 0;
    progress.style.width = `${Math.min(Math.max(ratio, 0), 100)}%`;
    if (header) {
      header.classList.toggle('scrolled', window.scrollY > 20);
    }
  };
  updateProgress();
  window.addEventListener('scroll', updateProgress, { passive: true });

  if (enableHeavyMotion) {
    const interactiveCards = document.querySelectorAll('.card, .process-card, .apk-card, .gallery figure');
    interactiveCards.forEach((card) => {
      card.addEventListener('mousemove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width;
        const y = (event.clientY - rect.top) / rect.height;
        const rotateY = (x - 0.5) * 8;
        const rotateX = (0.5 - y) * 8;
        card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });

    window.addEventListener('pointermove', (event) => {
      const x = (event.clientX / window.innerWidth) - 0.5;
      const y = (event.clientY / window.innerHeight) - 0.5;
      if (dynamicBg) {
        dynamicBg.style.transform = `translate(${x * 16}px, ${y * 16}px)`;
      }
    }, { passive: true });

    const heroArts = document.querySelectorAll('.hero-art');
    heroArts.forEach((art) => {
      art.addEventListener('mousemove', (event) => {
        const rect = art.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width;
        const y = (event.clientY - rect.top) / rect.height;
        const rotateY = (x - 0.5) * 6;
        const rotateX = (0.5 - y) * 6;
        art.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
      });
      art.addEventListener('mouseleave', () => {
        art.style.transform = '';
      });
    });
  }

  const rippleTargets = document.querySelectorAll('.cta, .contact-btn, .nav-links a');
  rippleTargets.forEach((target) => {
    target.classList.add('ripple-target');
    target.addEventListener('click', (event) => {
      trackEvent('cta_click', { label: target.textContent.trim(), href: target.getAttribute('href') || '' });
      const rect = target.getBoundingClientRect();
      const ripple = document.createElement('span');
      const size = Math.max(rect.width, rect.height);
      ripple.className = 'ripple';
      ripple.style.width = `${size}px`;
      ripple.style.height = `${size}px`;
      ripple.style.left = `${event.clientX - rect.left - (size / 2)}px`;
      ripple.style.top = `${event.clientY - rect.top - (size / 2)}px`;
      target.appendChild(ripple);
      ripple.addEventListener('animationend', () => ripple.remove(), { once: true });
    });
  });

  if (enableHeavyMotion) {
    const magneticTargets = document.querySelectorAll('.cta, .contact-btn');
    magneticTargets.forEach((target) => {
      target.addEventListener('mousemove', (event) => {
        const rect = target.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        target.style.transform = `translate(${x * 7}px, ${y * 7}px)`;
      });
      target.addEventListener('mouseleave', () => {
        target.style.transform = '';
      });
    });
  }

  const year = document.getElementById('year');
  if (year) {
    year.textContent = new Date().getFullYear();
  }

  const footerCol = document.querySelector('.footer-grid > div:first-child');
  if (footerCol && !footerCol.querySelector('.last-updated')) {
    const updated = document.createElement('p');
    updated.className = 'last-updated';
    updated.textContent = 'Last updated: February 20, 2026';
    footerCol.appendChild(updated);
  }

  const currentPath = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  if (currentPath !== 'index.html') {
    const main = document.querySelector('main');
    if (main) {
      const crumbWrap = document.createElement('div');
      crumbWrap.className = 'container breadcrumb-wrap';
      const label = currentPath.replace('.html', '').replace(/-/g, ' ');
      const title = label.charAt(0).toUpperCase() + label.slice(1);
      crumbWrap.innerHTML = `<nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span>${title}</span></nav>`;
      main.prepend(crumbWrap);
    }
  }

  const pageMain = document.querySelector('main');
  if (pageMain && !pageMain.querySelector('.global-conversion-cta')) {
    const cta = document.createElement('section');
    cta.className = 'section container reveal global-conversion-cta';
    cta.innerHTML = `
      <div class="primary-cta-bar">
        <p>Need a high-converting website, app, or maintenance partner? Start one clear project discussion.</p>
        <a class="cta" href="contact.html">Start Your Project</a>
      </div>
    `;
    pageMain.appendChild(cta);
  }

  const params = new URLSearchParams(window.location.search);
  if (params.get('sent') === '1') {
    const form = document.querySelector('.contact-form');
    if (form) {
      const note = document.createElement('p');
      note.className = 'card';
      note.style.marginBottom = '0.8rem';
      note.style.borderColor = 'color-mix(in srgb, var(--accent) 60%, var(--line))';
      note.textContent = 'Message sent successfully. I will contact you shortly.';
      form.prepend(note);
    }
  }

    const form = document.getElementById('contactForm');
  if (form) {
    const validateFormFields = () => {
      const fields = Array.from(form.querySelectorAll('input, select, textarea'));
      let firstInvalid = null;
      fields.forEach((field) => {
        if (!field.checkValidity()) {
          field.setAttribute('aria-invalid', 'true');
          if (!firstInvalid) {
            firstInvalid = field;
          }
        } else {
          field.removeAttribute('aria-invalid');
        }
      });
      if (firstInvalid) {
        firstInvalid.focus();
      }
      return !firstInvalid;
    };

    form.querySelectorAll('input, select, textarea').forEach((field) => {
      field.addEventListener('input', () => {
        if (field.checkValidity()) {
          field.removeAttribute('aria-invalid');
        }
      });
    });
    const fallbackToDirectSubmit = (statusEl, submitBtn) => {
      if (statusEl) {
        statusEl.classList.remove('success', 'error');
        statusEl.textContent = 'Connecting to secure form gateway...';
      }
      if (submitBtn) {
        submitBtn.disabled = false;
      }
      form.action = 'https://formsubmit.co/shrivastavapratham40@gmail.com';
      form.method = 'POST';
      form.submit();
    };

    const showLocalServerMessage = (statusEl, submitBtn) => {
      if (statusEl) {
        statusEl.classList.remove('success');
        statusEl.classList.add('error');
        statusEl.innerHTML = 'FormSubmit does not work in <code>file://</code> mode. Open this site via a local server (for example: <code>python -m http.server 5500</code>) and then submit again.';
      }
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Send Message Now';
      }
    };

    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      trackEvent('contact_submit', { form: 'contact_formsubmit' });

      const statusEl = document.getElementById('formStatus');
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.textContent : '';

      if (!validateFormFields()) {
        if (statusEl) {
          statusEl.classList.remove('success');
          statusEl.classList.add('error');
          statusEl.textContent = 'Please complete all required fields correctly before sending.';
        }
        return;
      }

      if (statusEl) {
        statusEl.classList.remove('success', 'error');
        statusEl.textContent = 'Sending your message...';
      }
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';
      }

      // Local file mode often blocks AJAX CORS. Use direct submit in that case.
      if (window.location.protocol === 'file:') {
        showLocalServerMessage(statusEl, submitBtn);
        return;
      }

      try {
        const formData = new FormData(form);
        const payload = {};
        formData.forEach((value, key) => {
          payload[key] = value;
        });

        const response = await fetch('https://formsubmit.co/ajax/shrivastavapratham40@gmail.com', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
          },
          body: JSON.stringify(payload),
        });

        let result = null;
        try {
          result = await response.json();
        } catch (_err) {
          result = null;
        }

        if (response.ok && (!result || result.success !== 'false')) {
          if (statusEl) {
            statusEl.classList.add('success');
            statusEl.textContent = 'Message sent successfully. Please confirm first FormSubmit email if this is your first submission.';
          }
          form.reset();
        } else {
          if (statusEl) {
            statusEl.classList.add('error');
            statusEl.textContent = 'Failed to send message. Please try again.';
          }
        }
      } catch (_error) {
        // Network blockers may affect AJAX in some browsers. Fallback only on real web server mode.
        if (window.location.protocol === 'http:' || window.location.protocol === 'https:') {
          fallbackToDirectSubmit(statusEl, submitBtn);
          return;
        }
        showLocalServerMessage(statusEl, submitBtn);
        return;
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = originalText || 'Send Message Now';
        }
      }
    });
  }

  document.querySelectorAll('a[href^="https://wa.me/"]').forEach((link) => {
    link.addEventListener('click', () => trackEvent('whatsapp_click', { label: 'whatsapp_contact' }));
  });
  document.querySelectorAll('a[href^="tel:"]').forEach((link) => {
    link.addEventListener('click', () => trackEvent('call_click', { label: 'phone_contact' }));
  });
  document.querySelectorAll('a[href^="mailto:"]').forEach((link) => {
    link.addEventListener('click', () => trackEvent('email_click', { label: 'email_contact' }));
  });

  document.querySelectorAll('img').forEach((img, index) => {
    img.decoding = 'async';
    if (index > 0) {
      img.loading = 'lazy';
    }
  });

  const trustedTarget = document.querySelector('main .hero.container');
  if (trustedTarget && !document.querySelector('.trusted-strip')) {
    const trusted = document.createElement('div');
    trusted.className = 'trusted-strip container reveal';
    trusted.innerHTML = `
      <p>Trusted by founders, clinics, institutes, and service brands.</p>
      <div class="trusted-list">
        <span>Startup Teams</span>
        <span>Healthcare Clinics</span>
        <span>Education Institutes</span>
        <span>Agency Partners</span>
        <span>Local Businesses</span>
      </div>
    `;
    trustedTarget.insertAdjacentElement('afterend', trusted);
  }

  if (!document.querySelector('.mobile-quickbar')) {
    const quickBar = document.createElement('div');
    quickBar.className = 'mobile-quickbar';
    quickBar.innerHTML = `
      <div class="inner">
        <a href="tel:+916200892887">Call</a>
        <a href="https://wa.me/916200892887" target="_blank" rel="noopener noreferrer">WhatsApp</a>
        <a href="contact.html">Message</a>
      </div>
    `;
    document.body.appendChild(quickBar);
  }

  if (!document.querySelector('.desktop-quick-cta')) {
    const desktopCta = document.createElement('a');
    desktopCta.className = 'desktop-quick-cta cta';
    desktopCta.href = 'contact.html';
    desktopCta.textContent = 'Start Project';
    document.body.appendChild(desktopCta);
  }

  const faqWrap = document.getElementById('faqAccordion');
  if (faqWrap) {
    const items = faqWrap.querySelectorAll('.faq-item');
    items.forEach((item) => {
      const btn = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');
      if (!btn || !answer) {
        return;
      }
      const panelId = `faq-panel-${Math.random().toString(36).slice(2, 8)}`;
      answer.id = panelId;
      btn.setAttribute('aria-controls', panelId);
      btn.setAttribute('aria-expanded', 'false');

      const toggle = () => {
        const open = item.classList.toggle('open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      };
      btn.addEventListener('click', toggle);
      btn.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          toggle();
        }
      });
    });
  }

  const sliderRoot = document.getElementById('testimonialsSlider');
  if (sliderRoot) {
    const track = sliderRoot.querySelector('.ts-track');
    const dots = sliderRoot.querySelector('.ts-dots');
    const prevBtn = sliderRoot.querySelector('[data-ts="prev"]');
    const nextBtn = sliderRoot.querySelector('[data-ts="next"]');
    let currentIndex = 0;
    let slides = [];
    let auto = null;

    const render = (data) => {
      if (!track || !dots) {
        return;
      }
      track.innerHTML = '';
      dots.innerHTML = '';
      data.forEach((item, idx) => {
        const stars = '*'.repeat(Number(item.rating || 5));
        const slide = document.createElement('article');
        slide.className = 'ts-slide';
        slide.innerHTML = `
          <div class="ts-card">
            <div class="ts-head">
              <div>
                <div class="ts-name">${item.name}</div>
                <div class="ts-role">${item.role}</div>
              </div>
              <div class="ts-stars">${stars}</div>
            </div>
            <p class="ts-outcome">${item.outcome}</p>
            <p class="ts-quote">"${item.quote}"</p>
          </div>
        `;
        track.appendChild(slide);

        const dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'ts-dot';
        dot.setAttribute('aria-label', `Go to testimonial ${idx + 1}`);
        dot.setAttribute('aria-pressed', 'false');
        dot.addEventListener('click', () => goTo(idx));
        dots.appendChild(dot);
      });
      slides = Array.from(track.children);
      goTo(0);
      startAuto();
    };

    const goTo = (idx) => {
      if (!slides.length || !track || !dots) {
        return;
      }
      currentIndex = (idx + slides.length) % slides.length;
      track.style.transform = `translateX(-${currentIndex * 100}%)`;
      dots.querySelectorAll('.ts-dot').forEach((dot, dotIdx) => {
        dot.classList.toggle('active', dotIdx === currentIndex);
        dot.setAttribute('aria-pressed', dotIdx === currentIndex ? 'true' : 'false');
      });
    };

    const startAuto = () => {
      if (prefersReducedMotion) {
        return;
      }
      if (auto) {
        clearInterval(auto);
      }
      auto = setInterval(() => goTo(currentIndex + 1), 4500);
    };

    prevBtn?.addEventListener('click', () => goTo(currentIndex - 1));
    nextBtn?.addEventListener('click', () => goTo(currentIndex + 1));
    sliderRoot.addEventListener('mouseenter', () => auto && clearInterval(auto));
    sliderRoot.addEventListener('mouseleave', startAuto);

    const fallbackTestimonials = [
      {
        name: 'Aditi Sharma',
        role: 'Clinic Owner',
        rating: 5,
        outcome: 'Bookings increased after redesign launch.',
        quote: 'The team delivered a smooth site and made updates quickly.',
      },
      {
        name: 'Rahul Verma',
        role: 'Startup Founder',
        rating: 5,
        outcome: 'Lead quality improved with clearer landing pages.',
        quote: 'Communication was clear and timelines were realistic.',
      },
    ];

    if (window.location.protocol === 'file:') {
      render(fallbackTestimonials);
      return;
    }

    fetch('assets/data/testimonials.json')
      .then((res) => res.json())
      .then((data) => render(Array.isArray(data) && data.length ? data : fallbackTestimonials))
      .catch(() => render(fallbackTestimonials));
  }
});





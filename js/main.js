/* ═══════════════════════════════════════════════════════
   Main JS — Nav scroll behaviour + scroll reveal
   ═══════════════════════════════════════════════════════ */

(function () {

  /* ── Nav: shrink on scroll ── */
  const navbar  = document.getElementById('navbar');
  const burger  = document.getElementById('navBurger');
  const mobile  = document.getElementById('navMobile');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  /* ── Mobile nav toggle ── */
  if (burger && mobile) {
    burger.addEventListener('click', () => {
      mobile.classList.toggle('open');
    });

    // Close mobile menu when a link is clicked
    mobile.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobile.classList.remove('open');
      });
    });
  }

  /* ── Scroll reveal ── */
  const revealEls = document.querySelectorAll('.reveal');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        // Once revealed, no need to keep observing
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  revealEls.forEach(el => observer.observe(el));

  /* ── Smooth active nav highlight ── */
  const sections  = document.querySelectorAll('section[id], footer[id]');
  const navAnchors = document.querySelectorAll('.nav-links a');

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navAnchors.forEach(a => {
          a.style.color = a.getAttribute('href') === `#${id}`
            ? 'var(--primary)'
            : '';
        });
      }
    });
  }, { rootMargin: '-40% 0px -40% 0px' });

  sections.forEach(s => sectionObserver.observe(s));

})();

/* ═══════════════════════════════════════════════════════
   Projects Showcase Carousel
   ═══════════════════════════════════════════════════════ */
(function () {
  const track    = document.getElementById('showcaseTrack');
  const prevBtn  = document.getElementById('showcasePrev');
  const nextBtn  = document.getElementById('showcaseNext');
  const titleEl  = document.getElementById('showcaseTitle');
  const descEl   = document.getElementById('showcaseDesc');

  if (!track || !prevBtn || !nextBtn) return;

  const projects = [
    {
      title: 'Data Science Platform',
      desc:  'Architected a centralised Data Science platform (Azure Databricks, MLflow, Azure Pipelines) that standardised MLOps workflows across the business, cutting the average deployment cycle from ~3 weeks to under 5 days.'
    },
    {
      title: 'Unified AI Platform',
      desc:  'Defined the technical strategy for a unified AI platform (Azure AI Search, Azure OpenAI) that cut time-to-production for LLM applications by ~60%, enabling multiple product teams to ship independently.'
    },
    {
      title: 'Air-gapped Edge ML Platform',
      desc:  'Pioneered an edge ML deployment pattern using Azure IoT Edge, ACR, and Databricks Apps — enabling model inference on isolated mine sites with zero internet. Adopted as the enterprise-wide standard across all remote operations.'
    },
    {
      title: 'Vision AI Safety System',
      desc:  'Designed and deployed a computer vision safety system using YOLO and Supervision for automated stop-sign monitoring, directly improving operational safety compliance across mining sites.'
    },
    {
      title: 'Predictive Maintenance ML',
      desc:  'Built predictive maintenance models (LightGBM, Random Forest) for a 1,700 km rail network, reducing unplanned downtime through early fault detection. Containerised and deployed via AWS SageMaker.'
    }
  ];

  let current = 0;

  function getCardWidth() {
    const card = track.querySelector('.showcase-card');
    if (!card) return 0;
    const style = getComputedStyle(track);
    const gap = parseFloat(style.gap) || 24;
    return card.offsetWidth + gap;
  }

  function update() {
    track.style.transform = `translateX(-${current * getCardWidth()}px)`;
    titleEl.textContent = projects[current].title;
    descEl.textContent  = projects[current].desc;
    prevBtn.disabled = current === 0;
    nextBtn.disabled = current === projects.length - 1;
  }

  prevBtn.addEventListener('click', () => {
    if (current > 0) { current--; update(); }
  });
  nextBtn.addEventListener('click', () => {
    if (current < projects.length - 1) { current++; update(); }
  });

  update();
})();

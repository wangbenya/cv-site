/* ═══════════════════════════════════════════════════════
   Warm Particle Animation — canvas-based dash particles
   ═══════════════════════════════════════════════════════ */

(function () {
  const canvas = document.getElementById('particleCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  // Warm sunset palette
  const COLORS = [
    '#FF6B35', // coral orange
    '#FFB347', // golden yellow
    '#FF8C69', // salmon
    '#FFD700', // warm gold
    '#E8735A', // terracotta
    '#FF9F43', // amber
    '#FFCA7A', // light gold
    '#F4845F', // peach
  ];

  const PARTICLE_COUNT = 85;
  const DASH_LEN_MIN  = 8;
  const DASH_LEN_MAX  = 28;
  const SPEED_MIN     = 0.25;
  const SPEED_MAX     = 0.75;
  const MOUSE_RADIUS  = 120;
  const MOUSE_FORCE   = 0.06;

  let W, H, dpr, particles = [];
  let mouseX = -9999, mouseY = -9999;
  let raf;

  /* ── Particle class ── */
  class Particle {
    constructor() { this.reset(true); }

    reset(randomY = false) {
      this.x     = Math.random() * W;
      this.y     = randomY ? Math.random() * H : H + 20;
      this.len   = DASH_LEN_MIN + Math.random() * (DASH_LEN_MAX - DASH_LEN_MIN);
      this.angle = (-Math.PI / 2) + (Math.random() - 0.5) * 1.2; // mostly upward
      this.speed = SPEED_MIN + Math.random() * (SPEED_MAX - SPEED_MIN);
      this.vx    = Math.cos(this.angle) * this.speed;
      this.vy    = Math.sin(this.angle) * this.speed;
      this.alpha = 0.2 + Math.random() * 0.65;
      this.color = COLORS[Math.floor(Math.random() * COLORS.length)];
      this.wobble    = Math.random() * Math.PI * 2;
      this.wobbleSpd = 0.01 + Math.random() * 0.02;
      this.width     = 1.5 + Math.random() * 2;
    }

    update() {
      // Gentle sway
      this.wobble += this.wobbleSpd;
      this.vx += Math.sin(this.wobble) * 0.012;

      // Mouse repulsion
      const dx = this.x - mouseX;
      const dy = this.y - mouseY;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < MOUSE_RADIUS && dist > 0) {
        const force = (MOUSE_RADIUS - dist) / MOUSE_RADIUS * MOUSE_FORCE;
        this.vx += (dx / dist) * force;
        this.vy += (dy / dist) * force;
      }

      // Dampen to avoid runaway velocities
      this.vx *= 0.98;
      this.vy *= 0.98;

      // Drift speed floor
      const spd = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
      if (spd < SPEED_MIN * 0.5) {
        this.vx += (0 - this.vx) * 0.05;
        this.vy += (-this.speed - this.vy) * 0.05;
      }

      this.x += this.vx;
      this.y += this.vy;

      // Wrap horizontally, reset when off top
      if (this.x < -40) this.x = W + 20;
      if (this.x > W + 40) this.x = -20;
      if (this.y < -40) this.reset(false);
    }

    draw() {
      const rot = Math.atan2(this.vy, this.vx);
      const ex = this.x + Math.cos(rot) * this.len;
      const ey = this.y + Math.sin(rot) * this.len;

      ctx.save();
      ctx.globalAlpha = this.alpha;
      ctx.strokeStyle = this.color;
      ctx.lineWidth   = this.width;
      ctx.lineCap     = 'round';
      ctx.beginPath();
      ctx.moveTo(this.x, this.y);
      ctx.lineTo(ex, ey);
      ctx.stroke();
      ctx.restore();
    }
  }

  /* ── Setup ── */
  function resize() {
    dpr    = window.devicePixelRatio || 1;
    W      = canvas.offsetWidth;
    H      = canvas.offsetHeight;
    canvas.width  = W * dpr;
    canvas.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function init() {
    resize();
    particles = Array.from({ length: PARTICLE_COUNT }, () => new Particle());
  }

  /* ── Loop ── */
  function loop() {
    ctx.clearRect(0, 0, W, H);
    for (const p of particles) { p.update(); p.draw(); }
    raf = requestAnimationFrame(loop);
  }

  /* ── Events ── */
  window.addEventListener('resize', () => {
    cancelAnimationFrame(raf);
    init();
    loop();
  });

  window.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouseX = e.clientX - rect.left;
    mouseY = e.clientY - rect.top;
  });

  window.addEventListener('mouseleave', () => {
    mouseX = -9999;
    mouseY = -9999;
  });

  /* ── Touch support ── */
  window.addEventListener('touchmove', (e) => {
    const t = e.touches[0];
    const rect = canvas.getBoundingClientRect();
    mouseX = t.clientX - rect.left;
    mouseY = t.clientY - rect.top;
  }, { passive: true });

  /* ── Start ── */
  init();
  loop();
})();

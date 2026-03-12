# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Serve locally
python3 -m http.server 8585
# → http://localhost:8585

# Regenerate cv.pdf after editing generate_cv.py
pip install reportlab
python generate_cv.py
```

No build step — the site is pure HTML/CSS/JS served directly from the root.

## Architecture

Single-page portfolio site with no framework or bundler.

**Rendering pipeline:**
1. `index.html` — all page sections in one file (nav → hero → about → skills → experience → projects → footer/contact)
2. `styles.css` — all styles; CSS custom properties in `:root` define the entire color palette and can be changed in one place
3. `js/particles.js` — self-contained IIFE; draws ~85 dash-shaped particles on a `<canvas>` inside `#hero` using warm colors from `COLORS[]`; responds to mouse position for repulsion; no external library
4. `js/main.js` — self-contained IIFE; handles nav scroll-shrink, mobile burger menu, and `IntersectionObserver`-based scroll reveal (`.reveal` → `.reveal.visible`)

**CV PDF:**
- `generate_cv.py` uses `reportlab` to produce `cv.pdf`; colors match the site's sunset palette
- `cv.pdf` is served as a static file; the "Download CV" button in the nav and hero link directly to it

**Hosting:**
- Designed for GitHub Pages (static, no server needed)
- `CNAME` contains the custom domain — update it before deploying
- DNS setup instructions are in `README.md`

## Customisation map

| Goal | Where to edit |
|---|---|
| Name, bio, headline | `index.html` hero + about sections |
| Skills / experience / projects | `index.html` respective `<section>` blocks |
| Color palette | `styles.css` `:root` variables |
| Particle colors or count | `js/particles.js` `COLORS[]` and `PARTICLE_COUNT` |
| CV content | `generate_cv.py` → run `python generate_cv.py` |
| Custom domain | `CNAME` file |

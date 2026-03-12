# Personal CV Website

A warm, narrative portfolio site for a machine learning engineer, inspired by [antigravity.google](https://antigravity.google/).

## Local development

```bash
# Serve locally on port 8585
python3 -m http.server 8585
# → open http://localhost:8585
```

## Update the CV PDF

Edit `generate_cv.py` with your real details, then:

```bash
pip install reportlab
python generate_cv.py
```

This overwrites `cv.pdf`.

---

## Deploy to GitHub Pages with a custom domain

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
# Create a repo at github.com — name it anything (e.g. cv-site)
git remote add origin https://github.com/YOUR_USERNAME/cv-site.git
git push -u origin main
```

### 2. Enable GitHub Pages

- Go to your repo → **Settings → Pages**
- Source: **Deploy from a branch** → `main` / `(root)`
- Click **Save** → your site will be live at `https://YOUR_USERNAME.github.io/cv-site`

### 3. Add a custom domain (~$10–15/yr)

**Recommended registrar:** [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) (at-cost pricing, free DNS management)

#### DNS records to add (at your registrar):

| Type  | Name | Value                  |
|-------|------|------------------------|
| A     | @    | 185.199.108.153        |
| A     | @    | 185.199.109.153        |
| A     | @    | 185.199.110.153        |
| A     | @    | 185.199.111.153        |
| CNAME | www  | YOUR_USERNAME.github.io |

#### GitHub Pages settings:

- Go to **Settings → Pages → Custom domain**
- Enter `yourname.com` and click **Save**
- Check **Enforce HTTPS** (GitHub provides free SSL via Let's Encrypt)

#### Update `CNAME` file:

Replace `yourname.com` in the `CNAME` file with your actual domain, commit, and push.

DNS propagation takes up to 24 hours — usually much less with Cloudflare.

---

## Customise the site

| What to change | Where |
|---|---|
| Name, headline, bio | `index.html` (hero + about sections) |
| Skills | `index.html` (#skills section) |
| Experience | `index.html` (#experience section) |
| Projects | `index.html` (#projects section) |
| Contact email | `index.html` footer `href="mailto:…"` |
| Colors / fonts | `styles.css` `:root` variables |
| Particle colors/count | `js/particles.js` `COLORS` / `PARTICLE_COUNT` |
| Social links | `index.html` footer `<a href="…">` |
| CV PDF | `generate_cv.py` → run `python generate_cv.py` |
| Custom domain | `CNAME` file |

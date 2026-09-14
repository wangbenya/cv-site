# cv-site

Personal CV site and CV generator for **Dr Benya Wang** — AI & ML Engineer, Perth WA.

Live at **[wangbenya.github.io/cv-site](https://wangbenya.github.io/cv-site)**.

Two artefacts live here and they are meant to agree with each other:

| Artefact | Source | Output |
|---|---|---|
| The website | `index.html`, `styles.css`, `js/` | GitHub Pages, served from `master` |
| The CV PDF | `generate_cv.py` | `Benya_Wang_CV.pdf` |

The PDF is committed to the repo because the site links to it directly — the "Download CV" buttons in the nav, hero and footer all point at `Benya_Wang_CV.pdf`.

## Layout

```
index.html          all page sections in one file (nav, hero, about,
                    skills, projects, experience, contact)
styles.css          all styles; the palette lives in :root variables
js/particles.js     canvas particle field in the hero (no dependencies)
js/main.js          nav scroll-shrink, burger menu, scroll reveal
generate_cv.py      reportlab script that renders Benya_Wang_CV.pdf
CNAME               GitHub Pages custom domain
```

No build step, no framework, no bundler. Edit the files and they are the site.

## Running locally

```bash
python3 -m http.server 8585
# → http://localhost:8585
```

## Regenerating the CV PDF

Edit `generate_cv.py`, then:

```bash
uv run --no-project --with reportlab python generate_cv.py
```

Or with a normal Python install:

```bash
pip install reportlab && python generate_cv.py
```

Either way this overwrites `Benya_Wang_CV.pdf` in place.

**Watch the page count.** The layout is tuned to land on exactly two A4 pages. Adding a few lines silently spills the certifications onto a third page, which looks like a mistake. After regenerating, confirm it is still two pages before committing.

## Tailoring for a job application

Each application gets its own branch, so the tailored CV and the wording that goes with it stay recoverable:

```bash
git worktree add .claude/worktrees/<role> -b <role> master
```

Tailor `generate_cv.py` in that worktree, regenerate, then open a PR to `master` when the wording is settled.

**Keep the site and the CV in step.** The experience bullets exist twice — in `generate_cv.py` and in the `#experience` timeline in `index.html`. They have drifted before: bullets were reordered in the CV and the site kept the old order for two releases. When you change one, change the other, or the site a recruiter opens from your CV will contradict the CV.

**One site, several applications.** There is only one live URL, and every application links to it. If two applications are open at once, the site needs framing that serves both rather than being retargeted at whichever is most recent.

### Per-application PDF copies

Copies named `Benya_Wang_CV_*.pdf` are gitignored, so you can keep one per requisition locally without committing them:

```
Benya_Wang_CV_AIArchitect_Req36794.pdf
Benya_Wang_CV_SeniorAIDataScientist_Req37776.pdf
```

The canonical `Benya_Wang_CV.pdf` stays tracked — the underscore after `CV` is what separates the two cases. Cover letters (`generate_cover_letter.py`, `Benya_Wang_Cover_Letter.pdf`) are gitignored too.

Note that these copies are **snapshots**. Regenerating the CV does not update them; re-copy before uploading.

## Deployment

GitHub Pages serves `master` from the repository root. Merging to `master` publishes.

`.gitattributes` marks `*.pdf` and `*.png` as binary. This matters more than it looks: reportlab PDFs contain no NUL bytes, so git's text/binary heuristic classifies `Benya_Wang_CV.pdf` as text and rewrites LF to CRLF on Windows checkouts, shifting every xref offset in the file. Do not remove that rule.

> **`CNAME` currently contains the placeholder `yourname.com`.** Either replace it with a real domain or delete the file so Pages serves the default `wangbenya.github.io/cv-site` URL cleanly.

### Setting up a custom domain

Point these records at GitHub, then put the domain in `CNAME`:

| Type  | Name | Value                     |
|-------|------|---------------------------|
| A     | @    | 185.199.108.153           |
| A     | @    | 185.199.109.153           |
| A     | @    | 185.199.110.153           |
| A     | @    | 185.199.111.153           |
| CNAME | www  | `wangbenya.github.io`     |

Then **Settings → Pages → Custom domain**, and tick **Enforce HTTPS**.

## Where to change what

| What | Where |
|---|---|
| Name, headline, bio | `index.html` — hero and about sections |
| Skills | `index.html` — `#skills` |
| Experience | `index.html` — `#experience` **and** `generate_cv.py` |
| Projects | `index.html` — `#projects` |
| Contact email, social links | `index.html` footer |
| Colours, fonts | `styles.css` — `:root` variables |
| Particle colours or count | `js/particles.js` — `COLORS`, `PARTICLE_COUNT` |
| CV content | `generate_cv.py`, then regenerate |
| Custom domain | `CNAME` |

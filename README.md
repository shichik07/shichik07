# Personal Website - Julius Kricheldorff

Personal [website](https://julius-kricheldorff.com/), built with Django and exported to static HTML for GitHub Pages.

## Project Structure

- `webapp/` - Django project (source of truth for content and templates)
  - `config/` - Django settings, URLs
  - `pages/` - the single app: views, page copy (`content.py`), management command
  - `templates/` - `base.html` (Liquid Glass UI shell, EEG canvas) + one template per page
  - `static/` - CSS, JS, images, CV PDF
- `docs/` - generated static site, published via GitHub Pages (do not edit by hand)
- `legacy-rmarkdown/` - the previous Distill/R Markdown site, kept for reference

## Build Instructions

```bash
cd webapp
python -m venv ../.venv && source ../.venv/bin/activate  # first time only
pip install django

python manage.py runserver   # preview locally at http://127.0.0.1:8000
python manage.py build_static # regenerate docs/ for deployment
```

`build_static` renders every page with Django's test client and writes the
result into `docs/`, alongside `CNAME` and `.nojekyll`, using the same
filenames the site has always used (`index.html`, `projects.html`, etc.) so
existing links keep working.

## Deployment

The site deploys to GitHub Pages from the `docs/` directory. Run
`python manage.py build_static`, commit the regenerated `docs/`, and push.

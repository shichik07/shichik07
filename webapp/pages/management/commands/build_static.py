import shutil
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse

from pages import content

REPO_ROOT = Path(__file__).resolve().parents[4]
DOCS_DIR = REPO_ROOT / "docs"

# Maps Django URL name (+ kwargs) to the output filename, matching the
# paths the site has always published so existing links/bookmarks keep working.
ROUTES = [
    ("home", {}, "index.html"),
    ("projects", {}, "projects.html"),
    ("personal", {}, "personal.html"),
    ("cv", {}, "CV.html"),
    ("recipes", {}, "recipes.html"),
]
for recipe in content.RECIPES:
    ROUTES.append(
        ("recipe-detail", {"slug": recipe["slug"]}, f"{recipe['slug']}.html")
    )


class Command(BaseCommand):
    help = "Render every page to static HTML into docs/ for GitHub Pages."

    def handle(self, *args, **options):
        if DOCS_DIR.exists():
            shutil.rmtree(DOCS_DIR)
        DOCS_DIR.mkdir(parents=True)

        self.stdout.write("Collecting static assets...")
        call_command("collectstatic", "--noinput", "--clear", verbosity=0)

        shutil.copytree(Path(settings.STATIC_ROOT), DOCS_DIR / "static")

        client = Client()
        for url_name, kwargs, out_name in ROUTES:
            path = reverse(url_name, kwargs=kwargs)
            response = client.get(path)
            if response.status_code != 200:
                self.stderr.write(f"  ! {path} -> {response.status_code}")
                continue
            out_path = DOCS_DIR / out_name
            out_path.write_bytes(response.content)
            self.stdout.write(f"  wrote {out_name}")

        for name in ("CNAME", ".nojekyll"):
            src = REPO_ROOT / name
            if src.exists():
                shutil.copy(src, DOCS_DIR / name)

        self.stdout.write(self.style.SUCCESS(f"Static site built into {DOCS_DIR}"))

from django.http import Http404
from django.shortcuts import render

from . import content


def home(request):
    return render(request, "pages/home.html", {
        "bio_paragraphs": content.HOME_BIO,
        "active": "home",
    })


def projects(request):
    return render(request, "pages/projects.html", {
        "projects": content.PROJECTS,
        "active": "projects",
    })


def personal(request):
    return render(request, "pages/personal.html", {
        "recent_recipes": content.RECIPES[:2],
        "active": "personal",
    })


def cv(request):
    return render(request, "pages/cv.html", {
        "active": "cv",
    })


def recipes(request):
    return render(request, "pages/recipes.html", {
        "recipes": content.RECIPES,
        "active": "personal",
    })


def recipe_detail(request, slug):
    recipe = content.RECIPES_BY_SLUG.get(slug)
    if recipe is None:
        raise Http404("Recipe not found")
    return render(request, "pages/recipe_detail.html", {
        "recipe": recipe,
        "active": "personal",
    })

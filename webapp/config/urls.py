from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects.html", views.projects, name="projects"),
    path("personal.html", views.personal, name="personal"),
    path("CV.html", views.cv, name="cv"),
    path("recipes.html", views.recipes, name="recipes"),
    path("<slug:slug>.html", views.recipe_detail, name="recipe-detail"),
]

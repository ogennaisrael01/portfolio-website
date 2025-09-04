from django.urls import path
from portfolio.views import home, about_view, project_view


urlpatterns = [
    path("", home, name="home"),
    path("about/me/", about_view, name="about"),
    path("projects/",project_view, name="projects")
]
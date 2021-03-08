from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("first/", first, name="first"),
    path("articles/", articles, name="articles"),
    path('archive/', archive, name="archive"),
    path("articles/<int:article_number>/", number),
    path("<int:article_number>/archive/", archive),
    path("<int:article_number>/<slug:slug_text>/", number),
]

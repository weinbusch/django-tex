from django.urls import path
from django_tex.shortcuts import render_to_pdf


def index(request):
    return render_to_pdf(request, "tests/test.tex")


urlpatterns = [
    path("", index, name="index"),
]

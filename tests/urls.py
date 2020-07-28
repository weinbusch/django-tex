from django.conf.urls import url

from django_tex.shortcuts import render_to_pdf


def index(request):
    return render_to_pdf(request, "tests/test.tex")


urlpatterns = [
    url("^$", index, name="index"),
]

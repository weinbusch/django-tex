from django.urls import path

from django_tex.shortcuts import render_to_pdf


def index(request):
    return render_to_pdf(request, "tests/test.tex")


def escape(request):

    names = [
        "& % $  # _ { }",
        "&%$ #_{}"
    ]

    return render_to_pdf(request, "tests/test_escape.tex", {"names": names})


urlpatterns = [
    path("", index, name="index"),
    path("escape", escape, name="escape")
]

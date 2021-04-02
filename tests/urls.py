from django.urls import path
from django_tex.shortcuts import render_to_pdf
from .contants import ESCAPE_CONTEXT


def index(request):
    return render_to_pdf(request, "tests/test.tex")


def escape(request):
    """
    Simple test for escape function, to see the final result of the escaping
    all characters should have the same spacing
    """
    return render_to_pdf(request, "tests/test_escape.tex", ESCAPE_CONTEXT)


urlpatterns = [path("", index, name="index"), path("escape", escape, name="escape")]

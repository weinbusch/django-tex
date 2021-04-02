from django.urls import path
import string
from django_tex.shortcuts import render_to_pdf


def index(request):
    return render_to_pdf(request, "tests/test.tex")


def escape(request):
    """
    Simple test for escape function, to see the final result of the escaping
    all characters should have the same spacing
    """
    names = [
        # With spaces
        r"& % $  # _ { } ~ ^ \ FINAL",
        # Without spaces
        r"&%$#_{}~^\FINAL",
        # With letters separating
        r"&A%A$A#A_A{A}A~A^A\FINAL",
        # With letters and spaces separating
        r"& A % A $ A # A _ A { A } A ~ A ^ A \ FINAL",
        # Test everything that is printable
        string.printable,
    ]
    return render_to_pdf(request, "tests/test_escape.tex", {"names": names})


urlpatterns = [path("", index, name="index"), path("escape", escape, name="escape")]

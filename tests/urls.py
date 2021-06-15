from django.urls import path
import datetime
from django_tex.shortcuts import render_to_pdf


def index(request):
    context = {
        "title": "Die erste Mannschaft des VfL in der Saison 2020/2021",
        "number": 3.14,
        "date": datetime.date.today(),
        "names": [
            "Manuel Riemann",
            "Patrick Drewes",
            "Paul Grave",
            "Cristian Gamboa",
            "Danilo Soares",
            "Saulo Decarli",
            "Herbert Bockhorn",
            "Vasilios Lampropoulos",
            "Maxim Leitsch",
            "Armel Bella Kotchap",
            "Erhan Masovic",
            "Anthony Losilla",
            "Thomas Eisfeld",
            "Raman Chibsah",
            "Robert Tesche",
            "Robert Zulj",
            "Simon Zoller",
            "Tom Weilandt",
            "Soma Novothny",
            "Danny Blum",
            "Tarsis Bonga",
            "Gerrit Holtmann",
            "Milos Pantovic",
            "Baris Ekincier",
            "Silvère Ganvoula",
        ],
        "special_characters": "&$%#_{}",
    }
    return render_to_pdf(request, "tests/index.tex", context)


urlpatterns = [
    path("", index, name="index"),
]

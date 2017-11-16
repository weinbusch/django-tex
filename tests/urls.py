
import datetime
from decimal import Decimal

from django.conf.urls import url

from django_tex.views import render_to_pdf

def pdf_view(request):
    template_name = 'tests/test.tex'
    context = {
        'test': 'a simple test', 
        'number': Decimal('1000.10'), 
        'date': datetime.date(2017, 10, 25),
        'names': ['Arjen', 'Jérôme', 'Robert', 'Mats'], 
    }
    return render_to_pdf(template_name, context, filename='test.pdf')

urlpatterns = [
    url(r'', pdf_view),
]


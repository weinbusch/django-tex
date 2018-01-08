
import datetime
from decimal import Decimal

from django.conf.urls import url
from django.views.generic import ListView
from django.views.generic.dates import YearArchiveView

from django_tex.views import render_to_pdf

from tests.models import Entry

def pdf_view(request):
    template_name = 'tests/test.tex'
    context = {
        'test': 'a simple test', 
        'number': Decimal('1000.10'), 
        'date': datetime.date(2017, 10, 25),
        'names': ['Arjen', 'Jérôme', 'Robert', 'Mats'], 
    }
    return render_to_pdf(template_name, context, filename='test.pdf')

class EntryList(ListView):

    model = Entry

class PdfList(EntryList):

    template_name = 'tests/list.tex'

    def render_to_response(self, context, **kwargs):
        return render_to_pdf(self.template_name, context)

class EntryArchive(YearArchiveView):

    model = Entry
    date_field = 'date'

urlpatterns = [
    url(r'^$', pdf_view),
    url(r'^entry/$', EntryList.as_view(), name='entry_list'),
    url(r'^entry/pdf/$', PdfList.as_view(), name='entry_list_pdf'),
    url(r'^entry/archive/(?P<year>\d{4})/$', EntryArchive.as_view(), name='entry_archive'),
]



from django.http import HttpResponse

from django_tex.core import compile_template_to_pdf

class PDFResponse(HttpResponse):

    def __init__(self, content, filename=None):
        super(PDFResponse, self).__init__(content_type='application/pdf')
        self['Content-Disposition'] = 'filename="{}"'.format(filename)
        self.write(content)


def render_to_pdf(template_name, context, filename=None):
    pdf = compile_template_to_pdf(template_name, context)
    return PDFResponse(pdf, filename=filename)

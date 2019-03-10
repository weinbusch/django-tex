from django.http import HttpResponse

from django_tex.core import compile_template_to_pdf


class PDFResponse(HttpResponse):

    def __init__(self, content, filename=None):
        super(PDFResponse, self).__init__(content_type='application/pdf')
        self['Content-Disposition'] = 'filename="{}"'.format(filename)
        self.write(content)


def render_to_pdf(request, template_name, context=None, filename=None):
    # Request is not needed and only included to make the signature conform to django's render function
    pdf = compile_template_to_pdf(template_name, context)
    return PDFResponse(pdf, filename=filename)

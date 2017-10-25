import os
from subprocess import Popen, PIPE
import tempfile

from django.template import loader

class TexError(Exception):
    pass

def run_tex(source):
    with tempfile.TemporaryDirectory() as tempdir:
        latex_command = ['pdflatex', '-output-directory', tempdir]
        process = Popen(latex_command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        process.communicate(source.encode('utf-8'))
        if process.returncode == 1:
            raise TexError(source)
        filepath = os.path.join(tempdir, 'texput.pdf')
        with open(filepath, 'rb') as pdf_file:
            pdf = pdf_file.read()
    return pdf

def compile_template_to_pdf(template_name, context):
    template = get_template(template_name)
    source = template.render(context)
    return run_tex(source)

def get_template(template_name):
    return loader.get_template(template_name)
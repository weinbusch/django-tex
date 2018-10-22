
import os
from subprocess import Popen, PIPE
import tempfile

from django_tex.engine import engine
from django.conf import settings

DEFAULT_INTERPRETER = 'lualatex'

class TexError(Exception):
    pass

def run_tex(source):
    with tempfile.TemporaryDirectory() as tempdir:
        latex_interpreter = getattr(settings, 'LATEX_INTERPRETER', DEFAULT_INTERPRETER)
        latex_command = [latex_interpreter, '-output-directory', tempdir]
        process = Popen(latex_command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        process.communicate(source.encode('utf-8'))
        if process.returncode == 1:
            with open(os.path.join(tempdir, 'texput.log'), encoding='utf8') as f:
                log = f.read()
            raise TexError(log)
        filepath = os.path.join(tempdir, 'texput.pdf')
        with open(filepath, 'rb') as pdf_file:
            pdf = pdf_file.read()
    return pdf

def compile_template_to_pdf(template_name, context):
    source = render_template_with_context(template_name, context)
    return run_tex(source)

def render_template_with_context(template_name, context):
    template = get_template(template_name)
    return template.render(context)

def get_template(template_name):
    return engine.get_template(template_name)

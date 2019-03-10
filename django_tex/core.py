import os
from subprocess import PIPE, run
import tempfile

from django.template.loader import get_template

from django_tex.exceptions import TexError
from django.conf import settings

DEFAULT_INTERPRETER = 'lualatex'


def run_tex(source):
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, 'texput.tex')
        with open(filename, 'x', encoding='utf-8') as f:
            f.write(source)
        latex_interpreter = getattr(settings, 'LATEX_INTERPRETER', DEFAULT_INTERPRETER)
        latex_interpreter_options = getattr(settings, 'LATEX_INTERPRETER_OPTIONS', '')
        latex_command = f'cd "{tempdir}" && {latex_interpreter} -interaction=batchmode {latex_interpreter_options} {os.path.basename(filename)}'
        process = run(latex_command, shell=True, stdout=PIPE, stderr=PIPE)
        try:
            if process.returncode == 1:
                with open(os.path.join(tempdir, 'texput.log'), encoding='utf8') as f:
                    log = f.read()
                raise TexError(log=log, source=source)
            with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as pdf_file:
                pdf = pdf_file.read()
        except FileNotFoundError:
            if process.stderr:
                raise Exception(process.stderr.decode('utf-8'))
            raise
    return pdf


def compile_template_to_pdf(template_name, context):
    source = render_template_with_context(template_name, context)
    return run_tex(source)


def render_template_with_context(template_name, context):
    template = get_template(template_name, using='tex')
    return template.render(context)

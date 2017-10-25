import os
from subprocess import Popen, PIPE
import tempfile

from tex.engine import engine

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
    source = render_template_with_context(template_name, context)
    return run_tex(source)

def render_template_with_context(template_name, context):
    template = get_template(template_name)
    return template.render(context)

def get_template(template_name):
    return engine.get_template(template_name)
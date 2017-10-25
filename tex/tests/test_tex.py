from unittest import TestCase

from tex.tex import run_tex, compile_template_to_pdf, TexError

CORRECT_SCOURCE = "\
\\documentclass{article}\n\
\\begin{document}\n\
This is a test!\n\
\\end{document}"

WRONG_SOURCE = "\
\\documentclass{article}\n\
\\begin{document}\n\
This is a test!\n\
"

CORRECT_TEMPLATE = "\
\\documentclass{article}\n\
\\begin{document}\n\
This is a {{ test }}!\n\
\\end{document}"

class TexTest(TestCase):

    def test_run_tex(self):
        pdf = run_tex(CORRECT_SCOURCE)
        self.assertIsNotNone(pdf)

    def test_tex_error(self):
        with self.assertRaises(TexError):
            pdf = run_tex(WRONG_SOURCE)

    def test_compile_template_to_pdf(self):
        template_name = ''
        context = {'test': 'simple test'}
        pdf = compile_template_to_pdf(template_name, context)
        self.assertIsNotNone(pdf)
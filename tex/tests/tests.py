from unittest import TestCase

from decimal import Decimal
import datetime

from tex.core import run_tex, compile_template_to_pdf, render_template_with_context
from tex.core import TexError

from tex.engine import engine

class RunningTex(TestCase):

    def test_run_tex(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n\
        \\end{document}"

        pdf = run_tex(source)
        self.assertIsNotNone(pdf)

    def test_tex_error(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n"

        with self.assertRaises(TexError):
            pdf = run_tex(source)

class ComplingTemplates(TestCase):

    def test_compile_template_to_pdf(self):
        template_name = 'tests/test.tex'
        context = {'test': 'a simple test'}
        pdf = compile_template_to_pdf(template_name, context)
        self.assertIsNotNone(pdf)

class RenderingTemplates(TestCase):

    def test_render_template(self):
        template_name = 'tests/test.tex'
        context = {'test': 'a simple test'}
        output = render_template_with_context(template_name, context)
        self.assertIn('a simple test', output)

class Engine(TestCase):

    def render_template(self, template_string, context):
        template = engine.from_string(template_string)
        return template.render(context)

    def test_whitespace_control(self):
        context = {'foo': 'bar'}
        template_string="\\section{ {{- foo -}} }"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '\\section{bar}')

    def test_localize_decimal(self):
        context = {'foo': Decimal('1000.10')}
        template_string="{{ foo|localize }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '1000,10')
    
    def test_localize_date(self):
        context = {'foo': datetime.date(2017, 10, 25)}
        template_string="{{ foo|localize }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '25.10.2017')

    def test_format_long_date(self):
        context = {'foo': datetime.date(2017, 10, 25)}
        template_string="{{ '{:%d. %B %Y}'.format(foo) }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '25. Oktober 2017')

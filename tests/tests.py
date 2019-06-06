import datetime
from decimal import Decimal

from django.test import TestCase
from django.test.utils import override_settings
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.template import engines
from django.conf import settings

from django_tex.core import run_tex, compile_template_to_pdf, render_template_with_context
from django_tex.exceptions import TexError

from django_tex.shortcuts import render_to_pdf

from tests.models import TemplateFile


class RunningTex(TestCase):
    '''
    Tests calling latex compiler
    '''

    def test_run_tex(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n\
        \\end{document}"

        pdf = run_tex(source)
        self.assertIsNotNone(pdf)

    @override_settings(LATEX_INTERPRETER='pdflatex')
    def test_different_latex_interpreter(self):
        '''The default interpreter is lualatex'''
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n\
        \\end{document}"

        pdf = run_tex(source)
        self.assertIsNotNone(pdf)

    @override_settings(LATEX_INTERPRETER='latexmk -pdf')
    def test_latexmk_test(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n\
        \\end{document}"

        pdf = run_tex(source)
        self.assertIsNotNone(pdf)

    @override_settings(LATEX_INTERPRETER='does_not_exist')
    def test_wrong_latex_interpreter(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n\
        \\end{document}"

        with self.assertRaises(Exception):
            pdf = run_tex(source)  # should raise


class Exceptions(TestCase):
    '''
    Tests custom exceptions
    '''

    def test_exception_emergency_stop(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n"

        with self.assertRaises(TexError) as cm:
            pdf = run_tex(source)

        self.assertEqual(source, cm.exception.source)
        self.assertRegex(cm.exception.log, r'^This is LuaTeX')
        self.assertRegex(cm.exception.message, r'^! Emergency stop')
        self.assertRegex(cm.exception.message,
                         r'(End of file on the terminal\!$)|(job aborted, no legal \\end found)')  # First alternative applies
        # if tex source is given to
        # pdflatex via stdin.
        # Second, if tex source is
        # given as filename

    @override_settings(LATEX_INTERPRETER='pdflatex')
    def test_pdflatex_exceptions(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        This is a test!\n"

        with self.assertRaises(TexError) as cm:
            pdf = run_tex(source)

        self.assertRegex(cm.exception.log, r'^This is pdfTeX')
        self.assertRegex(cm.exception.message, r'^! Emergency stop')
        self.assertRegex(cm.exception.message,
                         r'(End of file on the terminal\!$)|(job aborted, no legal \\end found)')  # First alternative applies
        # if tex source is given to
        # pdflatex via stdin.
        # Second, if tex source is
        # given as filename

    def test_exception_unknown_command(self):
        source = "\
        \\documentclass{article}\n\
        \\begin{document}\n\
        \\unkown{command}\n\
        \\end{document}\n"

        with self.assertRaises(TexError) as cm:
            pdf = run_tex(source)

        self.assertEqual(source, cm.exception.source)
        self.assertRegex(cm.exception.log, r'^This is LuaTeX')
        self.assertRegex(cm.exception.message, r'^! Undefined control sequence')


class RenderingTemplates(TestCase):
    '''
    Tests rendering a template file with context to a string

    TODO: Add a test for custom template file locations.
    '''

    def test_render_template(self):
        template_name = 'tests/test.tex'
        context = {
            'test': 'a simple test',
            'number': Decimal('1000.10'),
            'date': datetime.date(2017, 10, 25),
            'names': ['Arjen', 'Robert', 'Mats'],
        }
        output = render_template_with_context(template_name, context)
        self.assertIn('\\section{a simple test}', output)
        self.assertIn('This is a number: 1000,10.', output)
        self.assertIn('And this is a date: 25.10.2017.', output)
        self.assertIn('\\item Arjen', output)

    def test_render_template_from_custom_directory(self):
        template_name = 'custom_directory_test.tex'
        context = {'foo': 'bar'}
        output = render_template_with_context(template_name, context)
        self.assertIn('bar', output)


class CompilingTemplates(TestCase):
    '''
    Tests compiling a template file with a context to a pdf file
    '''

    def test_compile_template_to_pdf(self):
        template_name = 'tests/test.tex'
        context = {
            'test': 'a simple test',
            'number': Decimal('1000.10'),
            'date': datetime.date(2017, 10, 25),
            'names': ['Arjen', 'Robert', 'Mats'],
        }
        pdf = compile_template_to_pdf(template_name, context)
        self.assertIsNotNone(pdf)

    def test_compile_template_with_unicode(self):
        template_name = 'tests/test.tex'
        context = {
            'test': 'a simple test',
            'number': Decimal('1000.10'),
            'date': datetime.date(2017, 10, 25),
            'names': ['äüößéèô'],
        }
        pdf = compile_template_to_pdf(template_name, context)
        self.assertIsNotNone(pdf)

    @override_settings(LATEX_INTERPRETER='pdflatex') 
    def test_compile_template_with_graphics(self):
        # this test fails with lualatex if path to graphics file contains whitespaces
        template_name = 'tests/test_graphics.tex'
        context = {}
        pdf = compile_template_to_pdf(template_name, context)
        self.assertIsNotNone(pdf)


class TemplateLanguage(TestCase):
    '''
    Tests features such as whitespace control and filters
    '''

    def render_template(self, template_string, context={}, using='tex'):
        engine = engines[using]
        template = engine.from_string(template_string)
        return template.render(context)

    def test_whitespace_control(self):
        context = {'foo': 'bar'}
        template_string = "\\section{ {{- foo -}} }"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '\\section{bar}')

    @override_settings(LANGUAGE_CODE='en')
    def test_override_l10n_setting(self):
        context = {'foo': Decimal('1000.10')}
        template_string = "{{ foo|localize }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '1000.10')

    @override_settings(LANGUAGE_CODE='de-de')
    def test_localize_decimal(self):
        context = {'foo': Decimal('1000.10')}
        template_string = "{{ foo|localize }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '1000,10')

    @override_settings(LANGUAGE_CODE='de-de')
    def test_localize_date(self):
        context = {'foo': datetime.date(2017, 10, 25)}
        template_string = "{{ foo|localize }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '25.10.2017')

    @override_settings(LANGUAGE_CODE='de-de')
    def test_format_long_date(self):
        context = {'foo': datetime.date(2017, 10, 25)}
        template_string = "{{ foo | date('d. F Y') }}"
        # template_string="{{ '{:%d. %B %Y}'.format(foo) }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, '25. Oktober 2017')

    def test_rendering_unicode(self):
        context = {'foo': 'äüßéô'}
        template_string = "{{ foo }}"
        output = self.render_template(template_string, context)
        self.assertEqual(output, 'äüßéô')

    def test_linebreaks(self):
        context = {
            'brecht':
                'Ich sitze am Straßenhang.\n' +
                'Der Fahrer wechselt das Rad.'
        }
        template_string = "{{ brecht | linebreaks }}"
        output = self.render_template(template_string, context)
        self.assertEqual(
            output,
            'Ich sitze am Straßenhang.\\\\\n' +
            'Der Fahrer wechselt das Rad.'
        )
        # Render with default django renderer
        output = self.render_template(template_string, context, using='django')
        self.assertHTMLEqual(
            output, 
            '<p>Ich sitze am Straßenhang.<br>'+
            'Der Fahrer wechselt das Rad.</p>'
        )

    @override_settings(TEMPLATES=[
        {
            'NAME': 'tex',
            'BACKEND': 'django_tex.engine.TeXEngine',
            'OPTIONS': {
                'environment': 'tests.environment.test_environment',
            }
        }
    ])
    def test_custom_filters(self):
        context = {
            'duration': datetime.timedelta(minutes=90),
        }
        template_string = '{{ duration | hhmm_format }}'
        output = self.render_template(template_string, context)
        self.assertEqual('1:30', output)

    @override_settings(LATEX_GRAPHICSPATH=['c:\\foo\\bar', 'c:\\bar\\foo'])
    def test_graphicspath(self):
        template_string = '{% graphicspath %}'
        output = self.render_template(template_string)
        self.assertEqual(output, '\graphicspath{ {"c:/foo/bar/"} {"c:/bar/foo/"} }')

class Models(TestCase):
    '''
    TeXTemplateFile contains the relative path to a tex template (e.g. django_tex/test.tex)
    and validates if this template can be loaded.abs

    Since TeXTemplateFile is an abstract base class, it is used here in a subclassed version 'TemplateFile'
    '''

    def test_validation(self):
        TemplateFile(title='valid', name='tests/test.tex').full_clean()

        with self.assertRaises(ValidationError):
            TemplateFile(title='invalid', name='template/doesnt.exist').full_clean()


class Views(TestCase):

    def test_render_to_pdf(self):
        request = None  # request is only needed to make the signature of render_to_pdf similar to the signature of django's render function
        template_name = 'tests/test.tex'
        context = {
            'test': 'a simple test',
            'number': Decimal('1000.10'),
            'date': datetime.date(2017, 10, 25),
            'names': ['Arjen', 'Robert', 'Mats'],
        }
        response = render_to_pdf(request, template_name, context, filename='test.pdf')
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(response['Content-Disposition'], 'filename="test.pdf"')

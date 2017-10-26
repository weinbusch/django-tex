
==========
DJANGO-TEX
==========

Django-tex is a simple Django app to render Latex templates and compile
them into Pdf files.

Django-tex requires a local Latex installation and uses the jinja2 
templating engine for template rendering.

Quick start
-----------

1.  Add "django_tex" to your INSTALLED_APPS setting:

    INSTALLED_APPS = [
        ...
        'django_tex',
    ]

2.  Create a Latex template in your template directory:

    # test.tex
    \documentclass{article}

    \begin{document}

    \section{ {{- foo -}} }

    \end{document}

3.  Use "compile_template_to_pdf" in your code to get the Pdf file 
    as a bytes object:

    from django_tex.core import compile_template_to_pdf

    template_name = 'test.tex'
    context = {'foo': 'Bar'}
    pdf = compile_template_to_pdf(template_name, context)

SOME NOTES ON USAGE
-------------------

Since django-tex uses jinja, you can use jinja's whitespace control in 
Latex templates. For example, "\section{ {{ foo }} }" would be rendered as 
"\section{ Bar }" with the above context; "\section{ {{- foo -}}}", however, 
gets rendered nicely as "\section{Bar}".

Further, django-tex adds the custom filter "localize" to the jinja environment.
This runs its input through "django.utils.formats.localize_input" to
create a localized representation. The output depends on the USE_L10N and LANGUAGE_CODE
settings. Use the filter like this: "{{ foo|localize }}".
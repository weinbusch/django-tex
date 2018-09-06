
# DJANGO-TEX

Django-tex is a simple Django app to render LaTeX templates and compile
them into PDF files.

Django-tex requires a local LaTeX installation and uses the jinja2 
templating engine for template rendering.

## Quick start

1. Add "django_tex" to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'django_tex',
]
```

2. Create a LaTeX template in your template directory:

```tex
# test.tex
\documentclass{article}

\begin{document}

\section{ {{- foo -}} }

\end{document}
```

3. Use "compile_template_to_pdf" in your code to get the PDF file as a bytes object:

```python
from django_tex.core import compile_template_to_pdf

template_name = 'test.tex'
context = {'foo': 'Bar'}
PDF = compile_template_to_pdf(template_name, context)
```

Or use `render_to_pdf` to generate a HTTPResponse containing the PDF file:

```python
from django_tex.views import render_to_pdf

def view(request):
    template_name = 'test.tex'
    context = {'foo': 'Bar'}
    return render_to_pdf(template_name, context, filename='test.pdf')
```

## Some notes on usage

The default LaTeX interpreter is set to `lualatex`. This can be changed by the setting
`LATEX_INTERPRETER`, for instance: `LATEX_INTERPRETER = 'pdflatex'`. Of course, the interpreter needs
to be installed on your system for `django-tex` to work properly.

Since django-tex uses jinja, you can use jinja's whitespace control in 
LaTeX templates. For example, `\section{ {{ foo }} }` would be rendered as 
`\section{ Bar }` with the above context; `\section{ {{- foo -}} }`, however, 
gets rendered nicely as `\section{Bar}`.

Django's built-in filters are available. So you can use `{{ foo|date('d. F Y') }}` 
to get `1. Januar 2018`, for instance.

Further, django-tex adds the custom filter `localize` to the jinja environment.
This runs its input through `django.utils.formats.localize_input` to
create a localized representation. The output depends on the `USE_L10N` and `LANGUAGE_CODE`
settings. Use the filter like this: `{{ foo|localize }}`.

If you want to convert linebreaks into LaTeX linebreaks (`\\`), use the `linebreaks` filter (`{{ foo | linebreaks }}`).
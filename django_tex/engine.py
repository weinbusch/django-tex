import locale

from django.conf import settings
from django.template import engines
from django.template.backends.jinja2 import Jinja2

from jinja2 import Environment

from django_tex.filters import FILTERS

locale.setlocale(locale.LC_ALL, settings.LANGUAGE_CODE)

def environment(**options):
    env = Environment(**options)
    env.filters = FILTERS
    return env

class TeXEngine(Jinja2):
    app_dirname = 'templates'

params = {
    'NAME': 'tex',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'environment': 'django_tex.engine.environment'
    },
}

engine = TeXEngine(params)
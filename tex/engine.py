from django.template import engines
from django.template.backends.jinja2 import Jinja2
from jinja2 import Environment
from django.utils.formats import localize_input

def environment(**options):
    env = Environment(**options)
    env.filters['localize'] = localize_input
    return env

class TeXEngine(Jinja2):
    app_dirname = 'templates'

params = {
    'NAME': 'tex',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'environment': 'tex.engine.environment'
    },
}

engine = TeXEngine(params)
from django.template import engines
from django.template.backends.jinja2 import Jinja2
from jinja2 import Environment

def environment(**options):
    return Environment(**options)

class TeXEngine(Jinja2):
    app_dirname = 'templates'

params = {
    'NAME': 'tex',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        # 'environment': 'tex.engine.environment'
    },
}

engine = TeXEngine(params)
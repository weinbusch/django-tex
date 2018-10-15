
from jinja2 import Environment

from django.template.backends.jinja2 import Jinja2
from django.template.defaultfilters import register
from django.conf import settings
from django_tex.filters import FILTERS as tex_specific_filters

# Django's built-in filters ...
filters = register.filters
# ... updated with tex specific filters
filters.update(tex_specific_filters)

def environment(**options):
    env = Environment(**options)
    env.filters = filters
    return env

class TeXEngine(Jinja2):
    app_dirname = 'templates'

PARAMS = {
    'NAME': 'tex',
    'DIRS': settings.TEMPLATES[0]['DIRS'],
    'APP_DIRS': True,
    'OPTIONS': {
        'environment': 'django_tex.engine.environment'
    },
}

engine = TeXEngine(PARAMS)

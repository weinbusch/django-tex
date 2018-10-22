
from django.template.backends.jinja2 import Jinja2

class TeXEngine(Jinja2):
    app_dirname = 'templates'

PARAMS = {
    'NAME': 'tex',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'environment': 'django_tex.environment.environment'
    },
}

engine = TeXEngine(PARAMS)

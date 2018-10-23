
from django.conf import settings
from django.template.backends.jinja2 import Jinja2

class TeXEngine(Jinja2):
    app_dirname = 'templates'

    def __init__(self, params):
        params = params.copy()
        default_environment = {'environment': 'django_tex.environment.environment'}
        if 'OPTIONS' in params:
            params['OPTIONS'].update(default_environment)
        else:
            params['OPTIONS'] = default_environment
        super().__init__(params)


from django.template.backends.jinja2 import Jinja2

class TeXEngine(Jinja2):
    app_dirname = 'templates'

    def __init__(self, params):
        params = params.copy()
        environment = {'environment': 'django_tex.environment.environment'}
        if 'OPTIONS' in params:
            params['OPTIONS'].update({'environment': 'django_tex.environment.environment'})
        else:
            params['OPTIONS'] = {'environment': 'django_tex.environment.environment'}
        super().__init__(params)

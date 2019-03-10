from django.template.backends.jinja2 import Jinja2


class TeXEngine(Jinja2):
    app_dirname = 'templates'

    def __init__(self, params):
        default_environment = 'django_tex.environment.environment'
        if 'environment' not in params['OPTIONS'] or not params['OPTIONS']['environment']:
            params['OPTIONS']['environment'] = default_environment
        super().__init__(params)

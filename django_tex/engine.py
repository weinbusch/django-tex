from django.template.backends.jinja2 import Jinja2

DEFAULT_ENVIRONMENT = "django_tex.environment.environment"


class TeXEngine(Jinja2):
    app_dirname = "templates"

    def __init__(self, params):
        if (
            "environment" not in params["OPTIONS"]
            or not params["OPTIONS"]["environment"]
        ):
            params["OPTIONS"]["environment"] = DEFAULT_ENVIRONMENT
        super().__init__(params)

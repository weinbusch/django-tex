from jinja2 import Environment

from django.template.defaultfilters import register

from django_tex.filters import FILTERS as tex_specific_filters

# Django's built-in filters ...
filters = register.filters.copy()
# ... updated with tex specific filters
filters.update(tex_specific_filters)


def environment(**options):
    env = Environment(**options)
    env.filters = filters
    return env

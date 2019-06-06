from jinja2 import Environment

from django_tex.filters import FILTERS

def environment(**options):
    options.update(
        {'extensions': ['django_tex.extensions.GraphicspathExtension']}
    )
    env = Environment(**options)
    env.filters = FILTERS
    return env

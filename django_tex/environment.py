from jinja2 import Environment

from django_tex.filters import FILTERS

def environment(**options):
    env = Environment(**options, extensions=['django_tex.extensions.GraphicspathExtension'])
    env.filters = FILTERS
    return env

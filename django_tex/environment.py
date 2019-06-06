from jinja2 import Environment

from django_tex.filters import FILTERS

def environment(**options):
    env = Environment(**options)
    env.filters = FILTERS
    return env

from django.utils.formats import localize_input
from django.template.defaultfilters import register

def do_linebreaks(value):
    return value.replace('\n', '\\\\\n')

tex_specific_filters = {
    'localize': localize_input,
    'linebreaks': do_linebreaks
}

FILTERS = register.filters.copy()
FILTERS.update(tex_specific_filters)

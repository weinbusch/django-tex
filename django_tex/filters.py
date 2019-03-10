from django.utils.formats import localize_input


def do_linebreaks(value):
    return value.replace('\n', '\\\\\n')


FILTERS = {
    'localize': localize_input,
    'linebreaks': do_linebreaks
}

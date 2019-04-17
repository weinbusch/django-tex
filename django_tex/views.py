import warnings

def render_to_pdf(*args, **kwargs):
    from django_tex.shortcuts import render_to_pdf as func
    warnings.warn(
        ('"django_tex.views.render_to_pdf" is deprecated '
        'and will be removed in future releases. Please use '
        '"django_tex.shortcuts.render_to_pdf" instead.'),
        PendingDeprecationWarning
    ) 
    return func(*args, **kwargs)

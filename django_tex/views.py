import warnings

from django_tex.shortcuts import render_to_pdf
warnings.warn(
    ('"from django_tex.views import render_to_pdf" is deprectated '
    'and will be removed in future releases. Please use '
    '"from django_tex.shortcuts import render_to_pdf" instead.'),
    PendingDeprecationWarning
) 
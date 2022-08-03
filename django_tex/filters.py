import re

from django.utils.formats import localize_input
from django.template.defaultfilters import register


def do_linebreaks(value: str) -> str:
    return value.replace("\n", "\\\\\n")


REPLACEMENTS = dict(
    [
        ("&", "\\&"),
        ("%", "\\%"),
        ("$", "\\$"),
        ("#", "\\#"),
        ("_", "\\_"),
        ("{", "\\{"),
        ("}", "\\}"),
        ("\\", "\\textbackslash{}"),
        ("~", "\\textasciitilde{}"),
        ("^", "\\textasciicircum{}"),
    ]
)

ESCAPE_PATTERN = re.compile("[{}]".format("".join(map(re.escape, REPLACEMENTS.keys()))))


def do_latex_escape(value: object) -> str:
    """
    Replace all LaTeX characters that could cause the latex compiler to fail
    and at the same time try to display the character as intended from the user.

    see also https://tex.stackexchange.com/questions/34580/escape-character-in-latex
    """
    value = str(value)
    return ESCAPE_PATTERN.sub(lambda mo: REPLACEMENTS.get(mo.group()), value)


tex_specific_filters = {
    "localize": localize_input,
    "linebreaks": do_linebreaks,
    "latex_escape": do_latex_escape,
}

FILTERS = register.filters.copy()
FILTERS.update(tex_specific_filters)

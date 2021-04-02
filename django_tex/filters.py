from django.utils.formats import localize_input
from django.template.defaultfilters import register

BACKSLASH_REPLACEMENT = "<:-!~#BACKSLASH#~!:->"


def do_linebreaks(value: str) -> str:
    return value.replace("\n", "\\\\\n")


def do_latex_escape(value: str) -> str:
    """
    Replace all LaTeX characters that could cause the latex compiler to fail
    and at the same time try to display the character as intended from the user.

    see also https://tex.stackexchange.com/questions/34580/escape-character-in-latex
    """

    return (
        # Replace Backslashes so we dont' double replace backslashes
        value.replace("\\", BACKSLASH_REPLACEMENT)
        # If there was a space before the character we assume the user wants
        # it also in the displayed LaTeX text
        .replace(BACKSLASH_REPLACEMENT + " ", r"\textbackslash\space ")
        # Otherwise we assume it doesn't matter. Note the space at the end is
        # required that an additional text is not considered as part of the latex
        # command
        .replace(BACKSLASH_REPLACEMENT, r"\textbackslash ")
        # Do the same for ~ and ^
        .replace("~ ", r"\textasciitilde\space ")
        .replace("~", r"\textasciitilde ")
        .replace("^ ", r"\textasciicircum\space ")
        .replace("^", r"\textasciicircum ")
        .replace("&", r"\&")
        .replace("$", r"\$")
        .replace("%", r"\%")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
        # Replace vertical tab as this seems to be the only character from
        # string.printable that can't be consumed from LaTeX
        .replace(chr(11), "")
    )


tex_specific_filters = {
    "localize": localize_input,
    "linebreaks": do_linebreaks,
    "latex_escape": do_latex_escape,
}

FILTERS = register.filters.copy()
FILTERS.update(tex_specific_filters)

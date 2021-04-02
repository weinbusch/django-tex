import string

UNICODE_TEST_DEFAULT = "äüößéèô"
UNICODE_TEST_SPECIAL = "♞Ⅷ😉"


# This works only with luatex, pdflatex has troubles even with unputenc
UNICODE_TEST = UNICODE_TEST_DEFAULT + UNICODE_TEST_SPECIAL

# A list with different lines that are good to test escpaing
ESCAPE_LINES = [
    # With spaces
    r"& % $  # _ { } ~ ^ \ FINAL",
    # Without spaces
    r"&%$#_{}~^\FINAL",
    # With letters separating
    r"&A%A$A#A_A{A}A~A^A\FINAL",
    # With letters and spaces separating
    r"& A % A $ A # A _ A { A } A ~ A ^ A \ FINAL",
    # Test everything that is printable
    string.printable,
    r"&%$#_{}~^\FINAL " + UNICODE_TEST_DEFAULT,
]
ESCAPE_CONTEXT = {"names": ESCAPE_LINES}
ESCAPE_CONTEXT_SPECIAL_UNICODE = {"names": ESCAPE_LINES + [UNICODE_TEST_SPECIAL]}

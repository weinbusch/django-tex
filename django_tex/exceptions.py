import re


error_patterns = [
    r"^\!.*?l\.(?P<lineno>\d+).*?$",
    r"^\! Emergency stop.*?\*{3}.*?$",
    r"^\!.*?$",
]


ERROR = re.compile(r"|".join(error_patterns), re.DOTALL + re.MULTILINE)


class TexError(Exception):
    def __init__(self, log, source):
        self.log = log
        self.source = source

        mo = ERROR.search(self.log)

        self.message = mo.group() or "No error message found."

        if mo.group("lineno"):
            lineno = int(mo.group("lineno")) - 1
            source_lines = source.splitlines()
            total = len(source_lines)
            top = max(0, lineno - 5)
            bottom = min(lineno + 5, total)

            self.template_debug = {
                "name": "template",
                "message": mo.group(),
                "source_lines": list(enumerate(source_lines[top:bottom], top + 1)),
                "line": lineno + 1,
                "before": "",
                "during": source_lines[lineno],
                "after": "",
                "total": total,
                "top": top,
                "bottom": bottom,
            }

            width = len(str(bottom + 1))

            template_context = "\n".join(
                "{lineno:>{width}} {line}".format(lineno=lineno, width=width, line=line)
                for lineno, line in source_lines
            )

            self.message += "\n\n" + template_context

    def __str__(self):
        return self.message

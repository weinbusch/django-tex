import re


error_patterns = [
    r"^\!.*?l\.(?P<lineno>\d+).*?$",
    r"^\! Emergency stop.*?\*{3}.*?$",
    r"^\!.*?$",
]


ERROR = re.compile(r"|".join(error_patterns), re.DOTALL + re.MULTILINE)


class TexError(Exception):
    def __init__(self, log, source, template_name=None):
        self.log = log
        self.source = source.splitlines()
        self.mo = ERROR.search(self.log)
        
    @property
    def message(self):
        m = mo.group() or "No error message found."
        if ctx := self.template_context:
            m += "\n\n" + ctx
        return m
    
    @property
    def template_debug(self):
        if self.mo.group("lineno"):
            lineno = int(mo.group("lineno")) - 1
            total = len(self.source)
            top = max(0, lineno - 5)
            bottom = min(lineno + 5, total)
            source_lines = list(enumerate(self.source[top:bottom], top + 1))
            line, during = source_lines[lineno - top]

            return {
                "name": template_name,
                "message": self.message,
                "source_lines": source_lines,
                "line": line,
                "before": "",
                "during": during,
                "after": "",
                "total": total,
                "top": top,
                "bottom": bottom,
            }

    @property
    def template_context(self):
        if debug := self.template_debug:
            width = len(str(debug["bottom"] + 1))

            return "\n".join(
                "{lineno:>{width}} {line}".format(lineno=lineno, width=width, line=line)
                for lineno, line in debug["source_lines"]
            )

    def __str__(self):
        return self.message

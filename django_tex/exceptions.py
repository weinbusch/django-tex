import re


error_pattern = r"|".join([
    r"^\!.*?l\.(?P<lineno>\d+).*?$",
    r"^\! Emergency stop.*?\*{3}.*?$",
    r"^\!.*?$",
])


ERROR = re.compile(error_pattern, re.DOTALL + re.MULTILINE)


class TexError(Exception):
    def __init__(self, log):
        self.log = log
        self.message = self.get_message()

    def get_message(self):
        mo = ERROR.search(self.log)
        if mo:
            message = mo.group()
        else:
            message = "No error message found."
        return message

    def __str__(self):
        return self.message

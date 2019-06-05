import re


def prettify_message(message):
    '''
    Helper methods that removes consecutive whitespaces and newline characters
    '''
    # Replace consecutive whitespaces with a single whitespace
    message = re.sub(r'[ ]{2,}', ' ', message)
    # Replace consecutive newline characters, optionally separated by whitespace, with a single newline
    message = re.sub(r'([\r\n][ \t]*)+', '\n', message)
    return message


def tokenizer(code):
    token_specification = [
        ('ERROR', r'\! (.+[\r\n])+[\r\n]*'),
        ('WARNING', r'latex warning.*'),
        ('NOFILE', r'no file.*')
    ]
    token_regex = '|'.join('(?P<{}>{})'.format(label, regex) for label, regex in token_specification)
    for m in re.finditer(token_regex, code, re.IGNORECASE):
        token_dict = dict(type=m.lastgroup, message=prettify_message(m.group()))
        yield token_dict


class TexError(Exception):

    def __init__(self, log, source):
        self.log = log
        self.source = source
        self.tokens = list(tokenizer(self.log))
        self.message = self.get_message()

    def get_message(self):
        for token in self.tokens:
            if token['type'] == 'ERROR':
                return token['message']
        return 'No error message found in log'

    def __str__(self):
        return self.message

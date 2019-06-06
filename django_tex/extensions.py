import os.path
from django.conf import settings
from jinja2.ext import Extension
from jinja2 import nodes

def format_path_for_latex(path):
    path = path.replace('\\', '/')
    if not path.endswith('/'):
        path += '/'
    path = '{"' + path + '"}'
    return path

class GraphicspathExtension(Extension):
    """Adds a `graphicspath` tag to Jinja2 that 
    prints out a \graphicspath{ {<path>} } command, where
    <path> is derived from the LATEX_GRAPHICSPATH setting or 
    the BASE_DIR setting by default. 
    """
    tags = set(['graphicspath'])

    def parse(self, parser):
        list_of_paths = getattr(settings, 'LATEX_GRAPHICSPATH', [settings.BASE_DIR])
        value = '\graphicspath{ ' + ' '.join(map(format_path_for_latex, list_of_paths)) + ' }'
        node = nodes.Output(lineno=next(parser.stream).lineno)
        node.nodes = [nodes.MarkSafe(nodes.Const(value))]
        return node

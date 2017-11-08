import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

    from django.core.management import execute_from_command_line

    argv = sys.argv[:1] + ['test'] + sys.argv[1:]

    execute_from_command_line(argv)
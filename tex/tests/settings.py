
"""
Django settings for running tests
"""

SECRET_KEY = 'secret'

INSTALLED_APPS = [
    'tex',
    'tex.tests',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
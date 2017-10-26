
"""
Django settings for running tests
"""

SECRET_KEY = 'secret'

INSTALLED_APPS = [
    'django_tex',
    'django_tex.tests',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

LANGUAGE_CODE = 'de'

USE_L10N = True


"""
Django settings for running tests
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'secret'

INSTALLED_APPS = [
    'django_tex',
    'tests',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROOT_URLCONF = 'tests.urls'

DEBUG = True
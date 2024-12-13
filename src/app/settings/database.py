import sys

import environ

from .environment import BASE_DIR
# from app.settings.apps import APP

env = environ.Env()

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

IS_TEST = 'test' in sys.argv or 'test_coverage' in sys.argv
if IS_TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
elif env.str('DB_NAME', default='PLACEHOLDER') != 'PLACEHOLDER':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.str('DB_NAME'),
            'USER': env.str('DB_USER'),
            'PASSWORD': env.str('DB_PASSWORD'),
            'HOST': env.str('DB_HOST'),
            'PORT': env.str('DB_PORT'),
        }
    }

DATABASES_ROUTERS = ['app.utils.db.DBRouter']
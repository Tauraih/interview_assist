"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from .environment import env, IS_TEST, BASE_DIR
from .logging import LOGGING, logger
from django.core.management.commands import runserver
from .apps import INSTALLED_APPS
from .database import DATABASES, DATABASES_ROUTERS
from .mail import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = ['*']

MIDDLEWARE = [
    'app.utils.csp.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.utils.logging.RequestLoggingMiddleware',
    'app.utils.db.DBMiddleware',

    # # Add the account middleware:
    # "allauth.account.middleware.AccountMiddleware",

    # # Plotly
    # 'django_plotly_dash.middleware.BaseMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'
ASGI_APPLICATION = "app.asgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'app.settings.backends.EmailBackend',  # Custom email authentication backend
    'django.contrib.auth.backends.ModelBackend',  # Optional fallback for username authentication
]


AUTH_USER_MODEL = 'user.User'

SITE_ID = 1

shel_plus_imports = []

X_FRAME_OPTIONS = 'SAMEORIGIN'

runserver.Command.default_port = 8101

# Content Security Policy
CSP_FRAME_ANCESTORS = (
    'https://localhost:5173'
)

sources = (
    "'self'",
    "'unsafe-inline'",
    'data:',
    "https://unpkg.com",
    'https://cdn.jsdeliv.net',
    'https://fonts.googleapis.com',
    'https://fonts.gstatic.com',
)

CSP_IMG_SRC = sources
CSP_STYLE_SRC = sources
CSP_SCRIPT_SRC = sources
CSP_FONT_SRC = sources

CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "data:", "https://cdn.jsdelivr.net")

import os
from os import path

from .environment import BASE_DIR

django_apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

third_app_apps = [
    "django_bootstrap5",
    # Health Check
    'health_check',
    'health_check.db',
    'health_check.contrib.migrations',
]

# auth_apps = [
#     'rest_framework.authtoken',
#     'dj_rest_auth',
#     'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'dj_rest_auth.registration',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.facebook',
#     'django_rest_passwordreset',
# ]

project_apps = []
for item in os.listdir(BASE_DIR):
    if path.isdir(item) and path.isfile(path.join(item, 'apps.py')):
        project_apps.append(item)
print(f"Project apps: {project_apps}")

INSTALLED_APPS = django_apps + third_app_apps + project_apps  # + auth_apps
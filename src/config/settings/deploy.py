from config.settings.base import *  # flake8: noqa

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '*',
]

STATIC_ROOT = "/var/www/{{ project_name }}/static/"
MEDIA_ROOT = "/var/www/{{ project_name }}/media/"

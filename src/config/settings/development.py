from config.settings.base import *  # flake:8 noq

DEBUG = TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    # Here you can place apps used only in development,
    # for example:
    # 'debug_toolbar.apps.DebugToolbarConfig',
    'template_debug',
)

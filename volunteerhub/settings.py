"""
Django settings for our volunteerhub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys

from configurations import Configuration, values


class Common(Configuration):

    ADMINS = (
        ('Admin', 'info@example.com'),
    )

    # You'll likely want to add your own auth model.
    AUTH_USER_MODEL = 'custom_user.EmailUser'

    MANAGERS = ADMINS

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(BASE_DIR, 'volunteerhub/apps'))

    USE_SOUTH = True

    SOUTH_MIGRATION_MODULES = {
        'taggit': 'taggit.south_migrations',
    }

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.comments",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.redirects",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",
        'django.contrib.gis',

        'custom_user',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.github',
        'allauth.socialaccount.providers.google',
        "django_extensions",
        'foundation',
        'floppyforms',
        'taggit',
        'south',
        'braces',
        'localflavor',

        'volunteers',

    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + \
        ("django.core.context_processors.request",
         "django.core.context_processors.tz",
         "allauth.account.context_processors.account",
         "allauth.socialaccount.context_processors.socialaccount",
         "volunteers.context_processors.organization_loader")

    MIDDLEWARE_CLASSES = (
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_USERNAME_REQUIRED = False

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",)

    ROOT_URLCONF = 'volunteerhub.urls'

    WSGI_APPLICATION = 'volunteerhub.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(BASE_DIR, 'db.sqlite3'),
        environ=True))

    NEVERCACHE_KEY = values.Value('klladsf-wefkjlwef-wekjlwef--wefjlkjfslkxvl')

    #CACHES = values.CacheURLValue('memcached://127.0.0.1:11211')

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'America/New_York'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    SITE_ID = 1

    ALLOWED_HOSTS = values.Value('*')

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    PROJECT_DIRNAME = BASE_DIR.split(os.sep)[-1]

    CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

    MEDIA_URL = "/media/"

    MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')

    TEMPLATE_DIRS = (os.path.join(BASE_DIR, "volunteerhub/templates"),)

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "volunteerhub/static"),
    )

    #DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.Value()
    AWS_SECRET_ACCESS_KEY = values.Value()
    AWS_STORAGE_BUCKET_NAME = 'example.com'
    AWS_HEADERS = {'ExpiresDefault': 'access plus 30 days',
                   'Cache-Control': 'max-age=86400', }

    # Account activations automatically expire after this period
    ACCOUNT_ACTIVATION_DAYS = 14

    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/dashboard/'
    LOGOUT_URL = '/accounts/logout/'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }


class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = TEMPLATE_DEBUG = True

    DATABASES = values.DatabaseURLValue(
        'postgis://localhost/vhub')

    SECRET_KEY = 'notasecretatall'

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)

    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + (
        'debug_toolbar.middleware.DebugToolbarMiddleware',)


class Stage(Common):
    pass


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = TEMPLATE_DEBUG = False

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(True)

    DSN_VALUE = values.Value()

    # If we're on production, connect to Sentry
    RAVEN_CONFIG = {
        'dsn': DSN_VALUE,
    }

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',)

"""
Django settings for battlecat project.

By convention we pull values from the user's environment. For local
development it will be best to set these in your project's
virtualenv's postactive hook.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import getpass
import dj_database_url
from django.core.exceptions import ImproperlyConfigured
from path import Path

BASE_DIR = Path(__file__).parent.dirname()

ENVIRONMENT = os.environ.get('ENVIRONMENT')
if not ENVIRONMENT:
    raise ImproperlyConfigured('No "ENVIRONMENT" environment variable set')
if ENVIRONMENT not in ('development', 'staging', 'production', 'test'):
    raise ImproperlyConfigured('"ENVIRONMENT" setting must be one of development, staging, production, test')


SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ImproperlyConfigured('No "SECRET_KEY" environment variable set')

DEBUG = bool(os.environ.get('DEBUG', ENVIRONMENT in ('development', )))

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']


INSTALLED_APPS = [
    'django_adminlte',
    'django_adminlte_theme',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'django.contrib.humanize',

    'django_extensions',
    'django_celery_results',
    'django_celery_beat',
    'bootstrap3',

    'battlecat.core',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'battlecat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'battlecat.wsgi.application'


# Database

DATABASES = {
    # Configure by setting the DATABASE_URL environment variable.
    # The default settings may work well for local development.
    'default': dj_database_url.config() or {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'battlecat',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': getpass.getuser(),
        'PASSWORD': '',
    }
}


# Password validation

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


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': (os.environ.get('REDIS_URL') or 'redis://localhost') + '/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Sessions

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Internationalization

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '.static'

# Celery
CELERY_RESULT_BACKEND = 'django_celery_results.backends.DatabaseBackend'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_BROKER_URL = (os.environ.get('BROKER_URL') or os.environ.get('REDIS_URL') or 'redis://localhost') + '/0'
CELERY_WORKER_CONCURRENCY = 4

# Sites
SITE_ID = 1

# Email
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '25')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS', False))
EMAIL_USE_SSL = bool(os.environ.get('EMAIL_USE_SSL', False))
EMAIL_TIMEOUT = os.environ.get('EMAIL_TIMEOUT', 20)
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'webmaster@localhost')


# Debug toolbar
if 'ENABLE_DEBUG_TOOLBAR' in os.environ:
    ENABLE_DEBUG_TOOLBAR =bool(os.environ.get('ENABLE_DEBUG_TOOLBAR'))
else:
    try:
        import debug_toolbar
    except ImportError:
        ENABLE_DEBUG_TOOLBAR = False
    else:
        ENABLE_DEBUG_TOOLBAR = True

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')



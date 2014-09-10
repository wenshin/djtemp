#!/usr/bin/env python
# encoding: utf-8

"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{{ project_name }}.apps.main',
    '{{ project_name }}.utils',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static_prod/')

# Custom static path
STATICFILES_DIRS = (
    # >=v2.0.0 of djtemp have move this folder to `utils/`
    # os.path.join(BASE_DIR, 'static/'),
)

# It is default, just to known it
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Custom templates settings
TEMPLATE_DIRS = (
    # >=v2.0.0 of djtemp have move this folder to `apps/main/`
    # os.path.join(BASE_DIR, 'templates/'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# Set your log file path and name
LOG_FILE = '/var/data/log/{{ project_name }}.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': ('[%(asctime)s] %(levelname)-8s '
                       '%(name)s %(pathname)s %(funcName)s '
                       '%(lineno)d %(process)d %(thread)d '
                       '%(threadName)s: %(message)s')
        },
        'brief': {
            'format': ('[%(name)s] [%(funcName)s] [%(lineno)d] '
                       '%(process)d %(thread)d %(threadName)s: %(message)s')
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # Actived when DEBUG=True
            'filters': ['require_debug_true'],
            'formatter': 'brief',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            # Actived when DEBUG=False
            'filters': ['require_debug_false'],
            'formatter': 'verbose',
            'filename': LOG_FILE,
            'maxBytes': 10485760,
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        '{{ project_name }}': {
            # If the __name__ attribute in your project file is {{ project_name }}.module
            # you can use logging.getLogger(__name__) to get this logger instance
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    }
}

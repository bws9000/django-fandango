import os
from os.path import dirname
from django.utils.translation import ugettext_lazy as _

import dj_database_url
import django_heroku
import sys

#from urllib2 import Request, urlopen
from urllib.request import Request, urlopen
import json

BASE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir, ''))

CONTENT_DIR = os.path.join(BASE_DIR, 'content')


SECRET_KEY = '3d305kajG5Jy8KBafCMpHwDIsNi0SqVaW'

#DEBUG = (sys.argv[1] == 'runserver')
DEBUG = 1

ALLOWED_HOSTS = [
    'hidden-wave-51986.herokuapp.com',
    '127.0.0.1'
]

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Vendor apps
    'bootstrap4',

    # Application apps
    'main',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CONTENT_DIR, 'templates'),
        ],
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
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

request = Request(
    "https://mailtrap.io/api/v1/inboxes.json?api_token=<MAILTRAP_API_TOKEN>")
response_body = urlopen(request).read()
credentials = json.loads(response_body)[0]

EMAIL_HOST = credentials['domain']
EMAIL_HOST_USER = credentials['username']
EMAIL_HOST_PASSWORD = credentials['password']
EMAIL_PORT = credentials['smtp_ports'][0]
EMAIL_USE_TLS = True

#EMAIL_HOST = os.environ.get('EMAIL_HOST')
#EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
#EMAIL_PORT = os.environ.get('EMAIL_PORT')

#SMTP_SERVER = os.environ.get('SMTP_SERVER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

#EMAIL_HOST = SMTP_SERVER
#EMAIL_HOST_USER = ''
#DEFAULT_FROM_EMAIL = ''
#EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
#EMAIL_PORT = 465
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = True

if not DEBUG:
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=False)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'blackjack001',
            'USER': 'eddy',
            'PASSWORD': 'vanhalen',
            'HOST': 'localhost',
            'PORT': '5432',
        }

    }

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

ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = False
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = False

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
EMAIL_ACTIVATION_AFTER_CHANGING = True

SIGN_UP_FIELDS = ['username', 'first_name',
                  'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name',
                      'email', 'password1', 'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('zh-Hans', _('Simplified Chinese')),
]

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_ROOT = os.path.join(CONTENT_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets'),
]

LOCALE_PATHS = [
    os.path.join(CONTENT_DIR, 'locale')
]

# Activate Django-Heroku.
django_heroku.settings(locals())

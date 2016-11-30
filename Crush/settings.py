"""
Django settings for Crush project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'whcv7dp@qyg3l=unto%yvlsx^tbkp!i@jh)ikcf5er7blcc#fn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['crushbook.net','www.crushbook.net']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Crush.urls'

WSGI_APPLICATION = 'Crush.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'ENGINE': 'django.db.backends.sqlite3',

        'NAME': 'django',                      # Or path to database file if using sqlite3.
        'USER': 'django',
        'PASSWORD': 'LEx5IbL7ju',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/erfan/PycharmProjects/CB/Main/static/',
)

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'Crush.email_backend.DKIMBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'Whatever <no-reply@crushbook.net>'
DKIM_SELECTOR = 'dkim'
DKIM_DOMAIN = 'crushbook.net'
DKIM_PRIVATE_KEY='''-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCi+O0cPG24sEdWbsbSp7kBgq5kAcAGmZ6tZ0c68PoQXqGxl7U2
hYPzDuXpyx0d6aq/RNeOftqpUAv00yqqSGBQz6Bvz2mEROqEIW3tUF9A2Z365Jv8
7vAvzs+64rOK29JcNZO68Pt8auZ6zVUGrRyhSsbKui70Q4j5RzipHHiwJwIDAQAB
AoGAGIBuPYmEQXkXMJJ1B+S5dtWr3FM7CIL+DTnyxpTGM8HWc3nIf8rw/JDn1g94
cC/aQOlbswu1WjEzqvo4duNsv1wTQ1jF/m0iIDZRr22u9M7bebSWarJOhUxgZrFU
0H9oNdvZzkKROdMjKg2SMlOhqF0Pcj/SMZk6ENsgRh0Ja/kCQQDTgke/CqsnRTjF
TpE5llRDKlItsbCV1URheR3D4vMiyQkBRDxSYOlzIFpPvNiPbExYYlOCN7F5pxhd
8upCpDRjAkEAxUD2GYiEl+BXo0OB1MffQ4k8Q6f8JiYgy/JFDG6yenrBVxVEJodW
V7MTxC5OcSSnL97icGnAm7H3OYb63HC2bQJAGOlkV+0CwapWiG67jiPVot+ONFGU
ceFfn3dreRH2/ybch6iozi8Z7/RkjrW4cBQaXeKe4Vx7688xgIdG7jh27wJBAJ4g
UmjrmKeLz5Vw045439DrHeV6r9cBL79uqs2pm+g1qfIeeTCNw7iwNQNKv9VRtbjZ
axsEm8P0aaSzQT0gGg0CQQDORIQoIENF3lwHYEYwzELyMoaTsYh692cOFXPXRBgj
SBprRgQaCVrjOG99rdk8fiho+4Gwf81CxG0h3Ho3nmmk
-----END RSA PRIVATE KEY-----'''

STATIC_ROOT = ''
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

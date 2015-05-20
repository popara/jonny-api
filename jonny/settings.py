import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'nu04u00k0wm0^qsswa0paf4kyn1xofq6h@vd=l#d#(5l=$iys('
GOOGLE_PLACES_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY', '')
STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', '')

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'matching',
    'plan',
    'storages',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {

}

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'herokuapp.com',
    'localhost:8000',
    'localhost:3333',
    'localhost:3000',
    'jonnyibiza.com',
    '127.0.0.1:8000',
    'jonnyinc.divshot.io',
    'burning-torch-1428.firebaseapp.com',
)
CORS_URL_REGEX = r'^/api/.*$'
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'cache-control'
)

ROOT_URLCONF = 'jonny.urls'
WSGI_APPLICATION = 'jonny.wsgi.application'


DATABASES = {
    'default': dj_database_url.config(default="postgres://jonny:jonny@localhost:5432/jonnyinc")
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


import os
import dj_database_url

def env(key):
    return os.environ.get(key, '')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

JONNY_PLAN_PRICE_IN_CENTS = 5000
JONNY_PLAN_CURRENCY = "eur"

SECRET_KEY = 'nu04u00k0wm0^qsswa0paf4kyn1xofq6h@vd=l#d#(5l=$iys('

GOOGLE_PLACES_API_KEY = env('GOOGLE_PLACES_API_KEY')
STRIPE_API_KEY = env('STRIPE_API_KEY')

EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_USER = env('SG_USER')
SENDGRID_PASSWORD = env('SG_PASSWORD')

TWILIO_SID = env('TWILIO_ACCOUNT_SID')
TWILIO_TOKEN = env('TWILIO_AUTH_TOKEN')
TWILIO_DEFAULT_SENDER = "+34931071527"

MR_WOLF_DEST_NO = "+34654715245"
MR_WOLF_EMAIL = "mrwolf@jonnyibiza.com"
MR_WOLF_EMAIL_DEST = "support@jonnyibiza.com"

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
    'sslserver',
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



CORS_ORIGIN_WHITELIST = (
    'herokuapp.com',
    'localhost:8000',
    'localhost:3333',
    'localhost:3000',
    '127.0.0.1:3000',
    'jonnyibiza.com',
    'www.jonnyibiza.com',
    'experts.jonnyibiza.com',
    'mrwolf.jonnyibiza.com',
    '127.0.0.1:8000',
    'development.jonnyinc.divshot.io',
    'staging.jonnyinc.divshot.io',
    'jonnyinc.divshot.io',
    'burning-torch-1428.firebaseapp.com',
    'jonnyibiza.firebaseapp.com',
    'development.jonny-experts.divshot.io',
    'staging.jonny-experts.divshot.io',
    'jonny-experts.divshot.io',
)

CORS_ORIGIN_ALLOW_ALL = False
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
CORS_ALLOW_CREDENTIALS = True



ROOT_URLCONF = 'jonny.urls'
WSGI_APPLICATION = 'jonny.wsgi.application'


AWS_ACCESS_KEY_ID = "AKIAJSRYIQNUCNW3VDZA"
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = 'jonnyinc'
AWS_STORAGE_BUCKET = 'jonnyinc'


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

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'notifications': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

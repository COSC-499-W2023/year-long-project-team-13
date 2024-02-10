"""
Django settings for video_app project.

Generated by 'django-admin startproject' using Django 2.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from pathlib import Path
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fpfd*qb+!is4hf@l6c(0n*1v4syzidbwzfsm-^%c30x*&772wc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False


# STATIC_LOCATION = "static"
# STATIC_URL = f'{CLOUDFRONT_DOMAIN}/static/'
# # Add your path in the STATICFILES_STORAGE
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ['ebdjango-env-1.eba-uzn2yvai.ca-central-1.elasticbeanstalk.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stream.apps.StreamConfig',
    # 'streamers.apps.StreamersConfig',
    'bootstrap5',
    'storages',
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

ROOT_URLCONF = 'video_app.urls'

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

WSGI_APPLICATION = 'video_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'djangodatabase',
    'USER': 'masteruser',
    'PASSWORD': 'masteruser',
    'HOST': 'database-django.cqtxhhmhjnhu.ca-central-1.rds.amazonaws.com',
    'PORT': '5432',
  }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

#Add this in your settings.py file:
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'

# # AWS_ACCESS_KEY_ID = 'ASIA4HU6ILMRHALXJ5UV'
# # AWS_SECRET_ACCESS_KEY = 'Qukq6847BUBvzckLohMB9sIUEhzb4swWl74O/HWE'
AWS_STORAGE_BUCKET_NAME = 'elasticbeanstalk-ca-central-1-841071745826'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_REGION_NAME = "ca-central-1"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_QUERYSTRING_EXPIRE = 604800
CLOUDFRONT_DOMAIN = 'd18u3jaflgrcvn.cloudfront.net'
AWS_CLOUDFRONT_DOMAIN = 'd18u3jaflgrcvn.cloudfront.net'

AWS_S3_REGION_NAME = 'ca-central-1'
AWS_S3_ENDPOINT_URL = 'https://s3.amazonaws.com'

S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        'key': 'uploads/',
        'allowed': ['image/jpg', 'image/jpeg', 'image/png', 'video/mp4'],
    },
}

# MEDIAFILES_LOCATION = 'media'
# MEDIA_ROOT = '/%s/' % MEDIAFILES_LOCATION
# MEDIA_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'app.custom_storages.MediaStorage'

# STATICFILES_LOCATION = 'static'
# STATIC_ROOT = '/%s/' % STATICFILES_LOCATION
# STATIC_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
# STATICFILES_STORAGE = 'app.custom_storages.StaticStorage'

# STATIC_LOCATION = "static"
# STATIC_URL = f'{CLOUDFRONT_DOMAIN}/static/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = f'{CLOUDFRONT_DOMAIN}/media/'
# MEDIA_URL = "https://%s/%s/" % (CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#solves vidstream auto-created primary key error
DEFAULT_AUTO_FIELD='django.db.models.AutoField'


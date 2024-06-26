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
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fpfd*qb+!is4hf@l6c(0n*1v4syzidbwzfsm-^%c30x*&772wc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = ['vnonymous-env.eba-ai3bsdyf.us-west-2.elasticbeanstalk.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stream.apps.StreamConfig',
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
                'stream.context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'video_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Local SQLite3 database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# AWS RDS database
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'djangodatabase',
    'USER': 'masteruser',
    'PASSWORD': 'masteruser',
    'HOST': 'django-database.c6pxc7oyiyq1.us-west-2.rds.amazonaws.com',
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

# Local (AWS access) [Manually update] Copy it from AWS access portal
# AWS_ACCESS_KEY_ID=""
# AWS_SECRET_ACCESS_KEY=""
# AWS_SESSION_TOKEN=""

# Elasic Beanstalk server (AWS access)
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN')

AWS_STORAGE_BUCKET_NAME = 'rekognitionvideofaceblurr-outputimagebucket1311836-qbibfhivlghz'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_REGION_NAME = "us-west-2"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_QUERYSTRING_EXPIRE = 604800
CLOUDFRONT_DOMAIN = 'dns1ziq7g5vyv.cloudfront.net'
AWS_CLOUDFRONT_DOMAIN = 'dns1ziq7g5vyv.cloudfront.net'
AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_ENDPOINT_URL = f'https://s3.{AWS_S3_REGION_NAME}.amazonaws.com'

AWS_S3_INPUT_BUCKET_NAME = 'rekognitionvideofaceblurr-inputimagebucket20b2ba6b-c4zs9410qluo'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    # Local media store folder
MEDIA_URL = '/media/'

MEDIAFILES_LOCATION = ''
# MEDIA_URL = f'{CLOUDFRONT_DOMAIN}/'   # S3 media store location

PROFILE_PICTURE_FILES_LOCATION = 'profile-pics'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#solves vidstream auto-created primary key error
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100  # X is the size in megabytes - 50mb (1 min record video = 5.5mb)
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100  # X is the size in megabytes - 50mb

STATIC_ROOT=os.path.join(BASE_DIR,'productionfiles')
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')

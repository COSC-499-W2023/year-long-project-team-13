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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# AWS RDS database
# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'djangodatabase',
#     'USER': 'masteruser',
#     'PASSWORD': 'masteruser',
#     'HOST': 'django-database.c6pxc7oyiyq1.us-west-2.rds.amazonaws.com',
#     'PORT': '5432',
#   }
# }


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

# Local (AWS access) [Manually update]
AWS_ACCESS_KEY_ID="ASIA4HU6ILMRLXD7ZR3A"
AWS_SECRET_ACCESS_KEY="lTOcv5p4y+KQp5bYVt23PVEozqg/7CfrOZiIZXzP"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEPv//////////wEaDGNhLWNlbnRyYWwtMSJHMEUCIQDLttHepknAJIvQ4ZGhRMUzcn6IckpesEJd1oGyFw2uyAIgXUoKGzf4qAiTtimTrNQtIP8sCWALhT8jDnMk0DNJNhUqjgMIJRAAGgw4NDEwNzE3NDU4MjYiDHluA6jjkwty71hCrSrrAifRY1s5dimQld29iEUhpHjMrN6qPQWfbSSHDXeXP852mm3T3ExpsiD2vxn9a1eABu4rAhF79PX+8YlUl2MxczUUJPSo/aiLr57PQ1c8dCM2yjGhQWA2EkqX3DsdJqXT74dwQXLmLq5ocsOInaKjNbLKSwdlINAaT7wXVu0FMfXfoiBn3ZnjNc8Yd/hqlOVshEUuGltP9ocQec8uUF9oOB2qWxZNyP6J0UWxJCOIjznucFz2Gr7QrATvWE0a3m2eSpF5QMHlk+fRGb7FRPcYFOyc8Vz71eCbZarL4z6XKCZD9B/sAzBM21SISaZ73C23/fsANzP8GxhD6WlXFyW/mjWec9RDNlvYhw4r2UZinJVsPIwlFX5apSvSYn5ud29+o3RrWslcMmV/w9DQa8DZDG9LhJSUqBPa5aQW02jCsoEhkD1jdTCEopzGs5wpXG1IpDx0mWv6nHQ/BBtyUEPR6hO5dBy9pnA7wIHxuTDesaOwBjqmAcsdihW38krm+zNXrow7e8IQqDxQNidppVyZlmx80EGuy4yaZo7hp4ixhlTrbbuHhnczRNfCwVgMoLerkbh27OKL3cAO5dbS0W/s/+22uPiwBGA5lui1P/koYYSwz/4RETS10gxr9kB7N6Rx17BIxkfMkaP8HlCX+FBJwk5MjQrlJCfJtexOnNfQTX7CY+KcI6PQNkF12x13KgBEvyCeY5h+9HCCAuU="

# Elasic Beanstalk server (AWS access)
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN')

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

DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100  # X is the size in megabytes - 100mb (1 min record video = 5.5mb)
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100  # X is the size in megabytes - 100mb

STATIC_ROOT=os.path.join(BASE_DIR,'productionfiles')
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')

# ffmpeg_path to ffmpeg folder  (put ffmpeg folder files in app folder repository)
# ffmpeg_path = os.path.join(BASE_DIR, 'ffmpeg/bin')  # Example path, adjust as per your installation

# Set elastic beanstalk ffmpeg environment to ffmpeg_path
# os.environ['FFMPEG_PATH'] = ffmpeg_path

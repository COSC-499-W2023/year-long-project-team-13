from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'
    custom_domain = settings.CLOUDFRONT_DOMAIN

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    custom_domain = settings.CLOUDFRONT_DOMAIN

class ProfilePictureStorage(S3Boto3Storage):
    location = settings.PROFILE_PICTURE_FILES_LOCATION
    custom_domain = settings.CLOUDFRONT_DOMAIN

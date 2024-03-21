from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'
    custom_domain = settings.CLOUDFRONT_DOMAIN

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    custom_domain = settings.CLOUDFRONT_DOMAIN

    # def _save(self, name, content):
    #     # Get the username from the content object
    #     username = content.user.username

    #     # Create a new name for the file which includes the username
    #     name = f'{username}/{name}'

    #     # Call the parent class's _save method with the new name
    #     return super()._save(name, content)


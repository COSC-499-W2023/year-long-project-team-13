from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
import os

class StaticStorage(S3Boto3Storage):
    location = 'static'
    custom_domain = settings.CLOUDFRONT_DOMAIN


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    custom_domain = settings.CLOUDFRONT_DOMAIN

    def _save(self, name, content):
        print(dir(content))

        # Check if the content object has a user attribute
        if hasattr(content, 'user'):
            # Get the username from the content object
            username = content.user.username

            # Create a new name for the file which includes the username
            name = f'{name}'

        # Call the parent class's _save method with the new name
        return super()._save(name, content)

    def get_available_name(self, name, max_length=None):
        """This method will return a filename that is available in the storage system, and
        will be called from the _save method."""
        if self.exists(name):
            # If the filename already exists, add an integer suffix to the filename.
            # The suffix will start with 1 and increment with each new version.
            basename, extension = os.path.splitext(name)
            counter = 1
            while self.exists(name):
                # Append the counter to the basename.
                name = f"{basename}_{counter}{extension}"
                counter += 1
        return name


class ProfilePictureStorage(S3Boto3Storage):
    location = settings.PROFILE_PICTURE_FILES_LOCATION
    custom_domain = settings.CLOUDFRONT_DOMAIN

    def _save(self, name, content):
        # Print the attributes of the content object
        print(dir(content))

        # Check if the content object has a user attribute
        if hasattr(content, 'user'):
            # Get the username from the content object
            username = content.user.username

            # Create a new name for the file which includes the username
            name = f'{name}'

        # Call the parent class's _save method with the new name
        return super()._save(name, content)

    def get_available_name(self, name, max_length=None):
        """This method will return a filename that is available in the storage system, and
        will be called from the _save method."""
        if self.exists(name):
            # If the filename already exists, add an integer suffix to the filename.
            # The suffix will start with 1 and increment with each new version.
            basename, extension = os.path.splitext(name)
            counter = 1
            while self.exists(name):
                # Append the counter to the basename.
                name = f"{basename}_{counter}{extension}"
                counter += 1
        return name

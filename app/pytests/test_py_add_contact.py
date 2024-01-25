from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')

    def test_add_existing_user(self):
        try:
            user_to_add = User.objects.get(username='user2')
            self.user1.profile.contacts.add(user_to_add.profile)  # Add user_to_add to user1's contacts
            self.assertIn(user_to_add.profile, self.user1.profile.contacts.all())  # Check if user_to_add is in user1's contacts
        except ObjectDoesNotExist:
            self.fail("User does not exist")

    def test_add_nonexistent_user(self):
        try:
            user_to_add = User.objects.get(username='nonexistent_user')
            self.user1.profile.contacts.add(user_to_add.profile)  # Try to add nonexistent_user to user1's contacts
            self.fail("User should not exist")  # If the above line does not raise an exception, the test fails
        except ObjectDoesNotExist:
            self.assertTrue(True)  # If the above line raises an exception, the test passes
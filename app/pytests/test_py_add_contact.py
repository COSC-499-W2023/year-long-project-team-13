from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from stream.models import FriendRequest

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')

    def test_send_friend_request(self):
        try:
            receiver = User.objects.get(username='user2')
            FriendRequest.objects.create(sender=self.user1, receiver=receiver)  # Send a add contact request from user1 to user2
            self.assertTrue(FriendRequest.objects.filter(sender=self.user1, receiver=receiver).exists())  # Check if request exists
        except ObjectDoesNotExist:
            self.fail("User does not exist")

    def test_send_friend_request_to_nonexistent_user(self):
        try:
            receiver = User.objects.get(username='nonexistent_user')
            FriendRequest.objects.create(sender=self.user1, receiver=receiver)  # Sending request to nonexistent_user
            self.fail("User should not exist")  
        except ObjectDoesNotExist:
            self.assertTrue(True)  # If the above line raises an exception, the test passes
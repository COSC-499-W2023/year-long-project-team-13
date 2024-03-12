from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from stream.models import FriendRequest, Notification, Contact

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

            recentFriendRequest = FriendRequest.objects.filter(sender=self.user1).last()
            Notification.objects.create(user=self.user1, message=f'You have sent a friend request to '+ str(receiver) +'.', type=1, friendRequest_id=recentFriendRequest)   # create notification for sender
            Notification.objects.create(user=receiver, message=f'You have received a friend request from '+ str(self.user1) +'.', type=2,friendRequest_id=recentFriendRequest)  # create notificaiton for receiver

            self.assertTrue(FriendRequest.objects.filter(sender=self.user1, receiver=receiver).exists() and Notification.objects.filter(user=self.user1, type=1, friendRequest_id=recentFriendRequest) and Notification.objects.filter(user=receiver, type=2, friendRequest_id=recentFriendRequest))  # Check if friend request, notification for both sender/receiver exists

        except ObjectDoesNotExist:
            self.fail("User does not exist")

    def test_send_friend_request_to_nonexistent_user(self):
        try:
            receiver = User.objects.get(username='nonexistent_user')
            FriendRequest.objects.create(sender=self.user1, receiver=receiver)  # Sending request to nonexistent_user
            self.fail("User should not exist")
        except ObjectDoesNotExist:
            self.assertTrue(True)  # If the above line raises an exception, the test passes

    def test_remove_friend_request(self):
        try:
            sender = User.objects.get(username='user1')
            receiver = User.objects.get(username='user2')
            FriendRequest.objects.create(sender=sender, receiver=receiver)  # Send a add contact request from user1 to user2

            recentFriendRequest = FriendRequest.objects.filter(sender=sender).last()
            Notification.objects.create(user=sender, message=f'You have sent a friend request to '+ str(receiver) +'.', type=1, friendRequest_id=recentFriendRequest)

            notificationIDsender = Notification.objects.filter(user=sender, type=1, friendRequest_id=recentFriendRequest).last()

            Notification.objects.create(user=receiver, message=f'You have received a friend request from '+ str(sender) +'.', type=2,friendRequest_id=recentFriendRequest)

            notificationid = notificationIDsender.id
            friendRequestid = Notification.objects.get(id=notificationid).friendRequest_id.id
            receiver = FriendRequest.objects.get(id=friendRequestid).receiver

            sender = User.objects.get(username='user1')

            FriendRequest.objects.filter(id=friendRequestid).delete()   # delete friend request
            Notification.objects.create(user=sender, message=f'You have successfully deleted a friend request to '+ str(receiver) +'.', type=8) # create notification message for sender
            notificationMessage = Notification.objects.filter(user=sender, type=8).last()

            self.assertFalse(FriendRequest.objects.filter(sender=sender, receiver=receiver).exists())  # Check if friend request not exists (deleted)

            self.assertTrue(Notification.objects.filter(id=notificationMessage.id))   # Check if remove friend request notification is created

        except ObjectDoesNotExist:
            self.fail("Friend Request does not exist")

    def test_accept_friend_request(self):
        try:
            sender = User.objects.get(username='user1')
            receiver = User.objects.get(username='user2')
            FriendRequest.objects.create(sender=sender, receiver=receiver)  # Send a add contact request from user1 to user2

            recentFriendRequest = FriendRequest.objects.filter(sender=sender).last()
            Notification.objects.create(user=sender, message=f'You have sent a friend request to '+ str(receiver) +'.', type=1, friendRequest_id=recentFriendRequest)

            Notification.objects.create(user=receiver, message=f'You have received a friend request from '+ str(sender) +'.', type=2,friendRequest_id=recentFriendRequest)
            notificationIDreceiver = Notification.objects.filter(user=receiver, type=2, friendRequest_id=recentFriendRequest).last()

            notificationid = notificationIDreceiver.id
            friendRequestid = Notification.objects.get(id=notificationid).friendRequest_id.id
            sender = FriendRequest.objects.get(id=friendRequestid).sender

            Contact.objects.create(sender=sender, receiver=receiver)    # create friend list with both sender/receiver in contact
            FriendRequest.objects.filter(id=friendRequestid).delete()   # delete friend request
            Notification.objects.create(user=sender, message=f'You and '+ str(receiver) +' had become friends.', type=8)
            notificationMessageSender = Notification.objects.filter(user=sender, type=8).first()    # create notification message for sender
            Notification.objects.create(user=receiver, message=f'You and '+ str(sender) +' had become friends.', type=8)
            notificationMessageReceiver = Notification.objects.filter(user=receiver, type=8).last()    # create notification message for receiver

            self.assertFalse(FriendRequest.objects.filter(sender=sender, receiver=receiver).exists())  # Check if friend request not exists (deleted)

            self.assertTrue(Contact.objects.filter(sender=sender, receiver=receiver) and Notification.objects.filter(id=notificationMessageSender.id) and Notification.objects.filter(id=notificationMessageReceiver.id))   # Check if friendlist contact and accept friend request notification is created

        except ObjectDoesNotExist:
            self.fail("Friend Request does not exist")

    def test_reject_friend_request(self):
        try:
            sender = User.objects.get(username='user1')
            receiver = User.objects.get(username='user2')
            FriendRequest.objects.create(sender=sender, receiver=receiver)  # Send a add contact request from user1 to user2

            recentFriendRequest = FriendRequest.objects.filter(sender=sender).last()
            Notification.objects.create(user=sender, message=f'You have sent a friend request to '+ str(receiver) +'.', type=1, friendRequest_id=recentFriendRequest)

            Notification.objects.create(user=receiver, message=f'You have received a friend request from '+ str(sender) +'.', type=2,friendRequest_id=recentFriendRequest)
            notificationIDreceiver = Notification.objects.filter(user=receiver, type=2, friendRequest_id=recentFriendRequest).last()

            notificationid = notificationIDreceiver.id
            friendRequestid = Notification.objects.get(id=notificationid).friendRequest_id.id
            sender = FriendRequest.objects.get(id=friendRequestid).sender

            FriendRequest.objects.filter(id=friendRequestid).delete()   # delete friend request
            Notification.objects.create(user=receiver, message=f'You have rejected a friend request from '+ str(sender) +'.', type=8)
            notificationMessageReceiver = Notification.objects.filter(user=receiver, type=8).last()    # create notification message for receiver

            self.assertFalse(FriendRequest.objects.filter(sender=sender, receiver=receiver).exists())  # Check if friend request not exists (deleted)

            self.assertTrue(Notification.objects.filter(id=notificationMessageReceiver.id))   # Check if reject friend request notification is created

        except ObjectDoesNotExist:
            self.fail("Friend Request does not exist")

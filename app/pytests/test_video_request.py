from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from stream.models import VidRequest, Notification, Contact

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')
        Contact.objects.create(sender=User.objects.get(username='user1'), receiver=User.objects.get(username='user2'))    # Create friend list of user1 & user2

    def test_send_video_request(self):
        try:
            sender = User.objects.get(username='user1') # set user1 as sender
            receiver = User.objects.get(username='user2')   # set user2 as receiver
            VidRequest.objects.create(sender=sender, receiver=receiver, description="Testing", due_date="2024-02-28 15:32:19")  # Create video request from user1 to user2
            recentVideoRequest = VidRequest.objects.filter(sender=sender).last()

            Notification.objects.create(user=sender, message=f'You have sent a video request to '+ str(receiver) + '.' + '\n\n&nbsp;&nbsp; Video Request ID: ' + str(recentVideoRequest) + '.' + '\n&nbsp;&nbsp; Description: ' + 'Testing' + '\n&nbsp;&nbsp; Due DateTime: ' + '2024-02-28 15:32:19', type=3, videoRequest_id=recentVideoRequest)  # create notification for sender
            Notification.objects.create(user=receiver, message=f'You have received a video request from '+ str(sender) + '.' + '\n&nbsp;&nbsp; Description: ' + 'Testing' + '\n&nbsp;&nbsp; Due DateTime: ' + '2024-02-28 15:32:19', type=4,videoRequest_id=recentVideoRequest) # create notificaiton for receiver

            self.assertTrue(VidRequest.objects.filter(sender=sender, receiver=receiver, description="Testing", due_date="2024-02-28 15:32:19").exists() and Notification.objects.filter(user=sender, type=3, videoRequest_id=recentVideoRequest) and Notification.objects.filter(user=receiver, type=4, videoRequest_id=recentVideoRequest))  # Check if video request, notification for both sender/receiver exists

        except ObjectDoesNotExist:
            self.fail("User does not exist")

    def test_send_video_request_to_nonexistent_user(self):
        try:
            receiver = User.objects.get(username='nonexistent_user')
            VidRequest.objects.create(sender=self.user1, receiver=receiver)  # Sending video request to nonexistent_user
            self.fail("User should not exist")
        except ObjectDoesNotExist:
            self.assertTrue(True)  # If the above line raises an exception, the test passes

    def test_remove_video_request(self):
        try:
            sender = User.objects.get(username='user1') # set user1 as sender
            receiver = User.objects.get(username='user2')   # set user2 as receiver
            VidRequest.objects.create(sender=sender, receiver=receiver, description="Testing", due_date="2024-02-28 15:32:19")  # Create video request from user1 to user2
            recentVideoRequest = VidRequest.objects.filter(sender=sender).last()
            Notification.objects.create(user=sender, message=f'You have sent a video request to '+ str(receiver) + '.' + '\n\n&nbsp;&nbsp; Video Request ID: ' + str(recentVideoRequest) + '.' + '\n&nbsp;&nbsp; Description: ' + 'Testing' + '\n&nbsp;&nbsp; Due DateTime: ' + '2024-02-28 15:32:19', type=3, videoRequest_id=recentVideoRequest)  # create notification for sender

            notificationIDsender = Notification.objects.filter(user=sender, type=3, videoRequest_id=recentVideoRequest).last()

            Notification.objects.create(user=receiver, message=f'You have received a video request from '+ str(sender) + '.' + '\n&nbsp;&nbsp; Description: ' + 'Testing' + '\n&nbsp;&nbsp; Due DateTime: ' + '2024-02-28 15:32:19', type=4,videoRequest_id=recentVideoRequest) # create notificaiton for receiver

            notificationid = notificationIDsender.id
            videoRequestid = Notification.objects.get(id=notificationid).videoRequest_id.id
            VidRequest.objects.filter(id=videoRequestid).delete()
            Notification.objects.create(user=sender, message=f'You have successfully deleted a video request to '+ str(receiver) +'.', type=8)
            notificationMessage = Notification.objects.filter(user=sender, type=8).last()

            self.assertFalse(VidRequest.objects.filter(sender=sender, receiver=receiver, description="Testing", due_date="2024-02-28 15:32:19").exists())  # Check if video request not exists (deleted)

            self.assertTrue(Notification.objects.filter(id=notificationMessage.id))   # Check if remove video request notification is created

        except ObjectDoesNotExist:
            self.fail("User does not exist")

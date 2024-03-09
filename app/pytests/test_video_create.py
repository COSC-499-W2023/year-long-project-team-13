from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from stream.models import VidRequest, Notification, Contact, Post
import os

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')
        Contact.objects.create(sender=User.objects.get(username='user1'), receiver=User.objects.get(username='user2'))    # Create friend list of user1 & user2
        VidRequest.objects.create(sender=User.objects.get(username='user1'), receiver=User.objects.get(username='user2'), description="Testing", due_date="2024-02-28 15:32:19")  # Create video request from user1 to user2

    def test_send_video_post(self):
        try:
            sender = User.objects.get(username='user1') # set user1 as sender
            receiver = User.objects.get(username='user2')   # set user2 as receiver
            recentVideoRequest = VidRequest.objects.filter(sender=sender).last()    # get recently sent video request

            Post.objects.create(sender=sender, receiver=receiver, title="Testing", description="Testing", timelimit="2024-02-28 15:32:19", video=os.path.abspath('../../app/media/Beautiful_City_SEA_VIEW___Creative_Commons_Videos___Free_HD_Videos_-_no_copyright.mp4'), request_id=recentVideoRequest)  # Create video post from user1 to user2

            recentVideoUpload = Post.objects.filter(sender=sender).last()   # get recently uploaded video post
            Notification.objects.create(user=sender, message=f'You have post a video to '+ str(receiver) +'.', type=5, post_id=recentVideoUpload)   # create notification for sender
            Notification.objects.create(user=receiver, message=f'You have received a video post from '+ str(sender) +'.', type=8, post_id=recentVideoUpload)    # create notification for receiver

            self.assertTrue(Post.objects.filter(sender=sender, receiver=receiver, title="Testing", description="Testing", timelimit="2024-02-28 15:32:19", video=os.path.abspath('../../app/media/Beautiful_City_SEA_VIEW___Creative_Commons_Videos___Free_HD_Videos_-_no_copyright.mp4'), request_id=recentVideoRequest).exists() and Notification.objects.filter(user=sender, type=5, post_id=recentVideoUpload) and Notification.objects.filter(user=receiver, type=8, post_id=recentVideoUpload))  # Check if video post, notification for both sender/receiver exists

        except ObjectDoesNotExist:
            self.fail("User does not exist")

    def test_send_video_post_to_nonexistent_user(self):
        try:
            receiver = User.objects.get(username='nonexistent_user')
            Post.objects.create(sender=self.user1, receiver=receiver)  # Sending video post to nonexistent_user
            self.fail("User should not exist")
        except ObjectDoesNotExist:
            self.assertTrue(True)  # If the above line raises an exception, the test passes

    def test_remove_video_post(self):
        try:
            sender = User.objects.get(username='user1') # set user1 as sender
            receiver = User.objects.get(username='user2')   # set user2 as receiver
            recentVideoRequest = VidRequest.objects.filter(sender=sender).last()    # get recently sent video request

            Post.objects.create(sender=sender, receiver=receiver, title="Testing", description="Testing", timelimit="2024-02-28 15:32:19", video=os.path.abspath('../../app/media/Beautiful_City_SEA_VIEW___Creative_Commons_Videos___Free_HD_Videos_-_no_copyright.mp4'), request_id=recentVideoRequest)  # Create video post from user1 to user2

            recentVideoUpload = Post.objects.filter(sender=sender).last()   # get recently uploaded video post
            Notification.objects.create(user=sender, message=f'You have post a video to '+ str(receiver) +'.', type=5, post_id=recentVideoUpload)   # create notification for sender
            Notification.objects.create(user=receiver, message=f'You have received a video post from '+ str(sender) +'.', type=8, post_id=recentVideoUpload)    # create notification for receiver

            notificationIDsender = Notification.objects.filter(user=sender, type=5, post_id=recentVideoUpload).last()

            postid = notificationIDsender.post_id.id
            Post.objects.filter(id=postid).delete()
            Notification.objects.create(user=sender, message=f'You have successfully deleted a video post to '+ str(receiver) +'.', type=8)
            notificationMessage = Notification.objects.filter(user=sender, type=8).last()

            self.assertFalse(Post.objects.filter(sender=sender, receiver=receiver, title="Testing", description="Testing", timelimit="2024-02-28 15:32:19", video=os.path.abspath('../../app/media/Beautiful_City_SEA_VIEW___Creative_Commons_Videos___Free_HD_Videos_-_no_copyright.mp4'), request_id=recentVideoRequest).exists())  # Check if video post not exists (deleted)

            self.assertTrue(Notification.objects.filter(id=notificationMessage.id))   # Check if remove video post notification is created

        except ObjectDoesNotExist:
            self.fail("User does not exist")

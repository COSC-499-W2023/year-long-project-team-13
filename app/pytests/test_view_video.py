from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from stream.models import Post

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.upload_url = reverse('stream:video-upload-alt')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.video = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")

    def test_video_upload_POST(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.post(self.upload_url, {
            'title': 'Test Video',
            'description': 'Test Description',
            'video': self.video,
        })

        self.assertEqual(response.status_code, 302)  # check if redirect happened
        self.assertEqual(Post.objects.last().title, 'Test Video')  # check if video was uploaded

    def test_video_list_GET(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.get(reverse('stream:video-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stream/video-list.html')
from django.test import TestCase
from django.contrib.auth.models import User
from stream.forms import ValidatingPasswordChangeForm

class SettingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='old_password')
  
    def test_valid_password(self):
        form = ValidatingPasswordChangeForm(data={
            'password': 'ValidP@ssw0rd',
            'password2': 'ValidP@ssw0rd',
        }, user=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_password(self):
        form = ValidatingPasswordChangeForm(data={
            'password': 'invalidP@ssword1111',
            'password2': 'invalidP@ssword1111',
        }, user=self.user)
        self.assertFalse(form.is_valid())
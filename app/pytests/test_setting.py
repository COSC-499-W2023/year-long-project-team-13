from django.test import TestCase
from django.contrib.auth.models import User
from stream.forms import ValidatingPasswordChangeForm, SettingForm

class SettingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='ValidP@ssw0rd')

    def test_valid_password(self):
        form = ValidatingPasswordChangeForm(instance=self.user, data={
            'oldpassword': 'ValidP@ssw0rd',
            'password': 'NewValidP@ssw0rd',
            'password2': 'NewValidP@ssw0rd'
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_password(self):
        form = ValidatingPasswordChangeForm(instance=self.user, data={
            'oldpassword': 'wrong_old_password',
            'password': 'user1',
            'password2': 'user1',
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_valid_setting_form(self):
        form = SettingForm(data={
            'darkmode': 'Yes',
            'emailnotification': 'No',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_setting_form(self):
        form = SettingForm(data={
        'darkmode': '',
        'emailnotification': '',
    })
        self.assertFalse(form.is_valid(), form.errors)
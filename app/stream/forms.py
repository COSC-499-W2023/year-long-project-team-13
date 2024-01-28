from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from . models import VidStream, VidRequest, Profile, UserInfo, Setting, FriendRequest, Notification
# , Contact
from django.contrib.auth import password_validation
from django.contrib import auth
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
import difflib
# from django.utils.translation import gettext_lazy as _
import re

class VidUploadForm(forms.ModelForm):

    class Meta:
        model = VidStream
        fields = ["title","description", "video"]

class VidRequestForm(forms.ModelForm):
    # reciever =
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'style': 'boarder: 2px groove lightgreen;','required': True}))
    due_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder' :'Select a due date',
                                                              'style': '',
                                                              'class': 'form-control', 'type': 'date','required': True}))

    class Meta:
        model = VidRequest
        fields = ["receiver","description", "due_date"]

# From Streamers
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Username',
                                                             'style':'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email',
                                                            'style': 'width: 400px; height: 45px;margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                            'class': 'form-control', 'required': True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Confirm Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 27px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Username',
    #                                                          'style':'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
    #                                                          'class': 'form-control', 'required': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'First Name',
                                                             'style':'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Last Name',
                                                             'style':'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}), max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email',
                                                            'style': 'width: 400px; height: 45px;margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                            'class': 'form-control', 'required': True}))

    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class UserInfoUpdateForm(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.TextInput(attrs={'placeholder' :'Select a date',
                                                              'style': 'width: 400px; height: 45px;margin-left: auto; margin-right: auto; margin-bottom: 25px;border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'type': 'date','required': True}))
    class Meta:
        model = UserInfo
        fields = ['birthdate']

class UserProfileUpdateForm(forms.ModelForm):

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['image']

# Send friend request form to database
class AddContactForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.none()
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver'].queryset = User.objects.exclude(username=user.username)
        self.fields['receiver'].queryset = self.fields['receiver'].queryset.exclude(contact_receiver__sender__username=user.username).exclude(contact_sender__receiver__username=user.username).exclude(requests_receiver__sender__username=user.username).exclude(requests_sender__receiver__username=user.username)

    class Meta:
        model = FriendRequest
        fields = ['receiver']

class SettingForm(forms.ModelForm):
    YES_NO = (('Yes', 'True'),('No', 'False'),)
    darkmode = forms.BooleanField(widget=forms.RadioSelect(choices=YES_NO, attrs={'placeholder' :'On/Off',
                                                        'class': 'form-control','required': True}))
    emailnotification = forms.BooleanField(widget=forms.RadioSelect(choices=YES_NO, attrs={'placeholder' :'On/Off',
                                                        'class': 'form-control','required': True}))
    class Meta:
        model = Setting
        fields = ['darkmode', 'emailnotification']

# class SetPasswordForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password',
#                                                                   'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
#                                                                   'class': 'form-control', 'required': True}))

#     class Meta:
#         model = User
#         fields = ['password']


# class SetPasswordForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password',
#                                                                   'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
#                                                                   'class': 'form-control', 'required': True}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Confirm Password',
#                                                                   'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 27px; border: 2px groove lightgreen;',
#                                                                   'class': 'form-control', 'required': True}))

#     class Meta:
#         model = User
#         fields = ['password']

# class SetPasswordFormWithConfirm(SetPasswordForm):
#     new_password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Confirm Password',
#             'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
#             'class': 'form-control',
#             'required': True,
#         }),
#     )

# Change Password
class ValidatingPasswordChangeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}),validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Confirm Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 27px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}))
    MIN_LENGTH = 8

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super(ValidatingPasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.instance.username
        email = self.instance.email
        email = re.sub(r'@[A-Za-z]*\.?[A-Za-z0-9]*',"", email)

        # At least MIN_LENGTH long
        if len(password) < self.MIN_LENGTH:
            raise forms.ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)

        # At least one letter and one non-letter
        first_isalpha = password[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password):
            raise forms.ValidationError("The new password must contain at least one letter and at least one digit or" \
                                        " punctuation character.")

        # ... any other validation you want ...
        # Check Password not similar to username and email information
        username_similarity = difflib.SequenceMatcher(None, password.lower(), username.lower()).ratio()
        email_similarity = difflib.SequenceMatcher(None, password.lower(), email.lower()).ratio()

        similarity_threshold = 0.6  # Adjust this threshold as needed

        if username_similarity > similarity_threshold or email_similarity > similarity_threshold:
            raise forms.ValidationError("The new password cannot be too similar to your username or email.")

        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(('The two password fields must match.'))

        return password2

    class Meta:
        model = User
        fields = ['password']

     #Validation for repeated characters in password. Cannot have 4 of the same characters in a row.
        # if re.search(r'(.{2,}).*\1', password):
        #     raise forms.ValidationError("The new password cannot have 4 of the same characters in a row.")
        # raise forms.ValidationError(email)

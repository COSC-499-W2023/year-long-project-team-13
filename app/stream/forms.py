from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
from django.db.models import Q
import difflib, re
from . models import VidRequest, VidStream, Contact, FriendRequest, Post, Profile, UserInfo, Notification, Setting

class VidUploadForm(forms.ModelForm):
    # receiver = forms.ModelChoiceField(
    #     queryset=User.objects.none(),
    #     widget=forms.Select(attrs={'style': 'width: 207px; border: 2px groove lightgreen;',
    #                                 'required': True})
    # )
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Title',
                                                             'style':'width: 215px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":23,
                                                               'style': 'border: 2px groove lightgreen;',
                                                               'required': True}))
    timelimit = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder' :'Select a time limit date',
                                                              'style': 'width: 210px; margin-left: auto; margin-right: auto; border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'type': 'datetime-local','required': True}))
    # video = forms.FileField()
    request_id = forms.ModelChoiceField(
        queryset=User.objects.none(),
        widget=forms.Select(attrs={'style': 'width: 210px; border: 2px groove lightgreen;',
                                    'required': True})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['receiver'].queryset = User.objects.exclude(username=user.username)
        # self.fields['receiver'].queryset = self.fields['receiver'].queryset.filter(video_sender__receiver__username=user.username)
        self.fields['request_id'].queryset = VidRequest.objects.filter(receiver__username=user.username)

    class Meta:
        model = Post
        fields = ['title','description','timelimit','request_id']
        # ,'receiver', 'video',

class VidCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Title',
                                                             'style':'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":23,
                                                               'style': 'border: 2px groove lightgreen;',
                                                               'required': True}))
    timelimit = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder' :'Select a time limit date',
                                                              'style': 'width: 210px; margin-left: auto; margin-right: auto; border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'type': 'datetime-local','required': True}))
    request_id = forms.ModelChoiceField(
        queryset=User.objects.none(),
        widget=forms.Select(attrs={'style': 'width: 207px; border: 2px groove lightgreen;',
                                    'required': True})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['request_id'].queryset = VidRequest.objects.filter(receiver__username=user.username)

    class Meta:
        model = Post
        fields = ['title','description','timelimit','request_id']

class VidUpFilledForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Title',
                                                             'style':'width: 215px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":23,
                                                               'style': 'border: 2px groove lightgreen;',
                                                               'required': True}))
    timelimit = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder' :'Select a time limit date',
                                                              'style': 'width: 210px; margin-left: auto; margin-right: auto; border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'type': 'datetime-local','required': True}))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title','description','timelimit']

class VidRecFilledForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Title',
                                                             'style':'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":23,
                                                               'style': 'border: 2px groove lightgreen;',
                                                               'required': True}))
    timelimit = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder' :'Select a time limit date',
                                                              'style': 'width: 210px; margin-left: auto; margin-right: auto; border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'type': 'datetime-local','required': True}))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title','description','timelimit']

class VidRequestForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.none(),
        widget=forms.Select(attrs={'style': 'width: 207px; border: 2px groove lightgreen;',
                                    'required': True})
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":23,
                                                               'style': 'border: 2px groove lightgreen;',
                                                               'required': True}))
    due_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder' :'Select a due date',
                                                              'style': 'width: 210px; margin-left: auto; margin-right: auto; border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'type': 'datetime-local','required': True}))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver'].queryset = User.objects.exclude(username=user.username)
        self.fields['receiver'].queryset = self.fields['receiver'].queryset.filter(Q(contact_receiver__sender__username=user.username) | Q(contact_sender__receiver__username=user.username))

    class Meta:
        model = VidRequest
        fields = ['receiver','description','due_date']

# Register new user account
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

class UserPermissionForm(forms.ModelForm):
    STATUS_CHOICES = (
      (1, 'Sender'),
      (2, 'Reciever'),
     )
    QUESTIONS_CHOICES = (
      (1, 'What was the name of your first pet?'),
      (2, 'In which city were you born?'),
      (3, 'What is the middle name of your oldest sibling?'),
      (4, 'What is the name of your favorite sports team?'),
      (5, 'What was the make and model of your first car?'),
     )

    permission = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'style': 'width: 400px; height: 45px;margin-left: auto; margin-right: auto; margin-bottom: 25px;border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'required': True}))

    security_question = forms.ChoiceField(choices=QUESTIONS_CHOICES, widget=forms.Select(attrs={'style': 'width: 400px; height: 45px;margin-left: auto; margin-right: auto; margin-bottom: 25px;border: 2px groove lightgreen;',
                                                              'class': 'form-control', 'required': True}))

    security_answer = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Your Answer',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 27px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}))

    class Meta:
        model = UserInfo
        fields = ['permission', 'security_question', 'security_answer']

class SecurityQuestionForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Username',
                                                             'style':'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                             'class': 'form-control', 'required': True}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email',
                                                            'style': 'width: 400px; height: 45px;margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                            'class': 'form-control', 'required': True}))

    class Meta:
        model = UserInfo
        fields = ['username', 'email']

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

    def clean_darkmode(self):
        darkmode = self.cleaned_data.get('darkmode')
        if darkmode not in [True, False]:
            raise ValidationError("Invalid value for darkmode")
        return darkmode

    def clean_emailnotification(self):
        emailnotification = self.cleaned_data.get('emailnotification')
        if emailnotification not in [True, False]:
            raise ValidationError("Invalid value for emailnotification")
        return emailnotification

# Change Password
class ValidatingPasswordChangeForm(forms.ModelForm):
    oldpassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Old Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}))
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

    def clean_oldpassword(self):
        old_password = self.cleaned_data.get("oldpassword")
        password1 = self.cleaned_data.get('password')
        user = self.instance
        if not authenticate(username=user.username, password=old_password):
            raise forms.ValidationError("Your old password was entered incorrectly. Please enter it again.")
        if old_password and password1 and old_password == password1:
            raise forms.ValidationError(("You cannot use your old password as the new password. Please try a different password."))
        return old_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        old_password = self.cleaned_data.get('oldpassword')  # Fetch the old password
        username = self.instance.username
        email = self.instance.email
        email = re.sub(r'@[A-Za-z]*\.?[A-Za-z0-9]*',"", email)

        # Ensure oldpassword field is added to cleaned_data
        if password == old_password:
            raise forms.ValidationError("You cannot use your old password as the new password.")

        # At least MIN_LENGTH long
        if len(password) < self.MIN_LENGTH:
            raise forms.ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)

        # At least one letter and one non-letter
        first_isalpha = password[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password):
            raise forms.ValidationError("The new password must contain at least one letter and at least one digit or" \
                                        " punctuation character.")

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


class ResetPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}),validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Confirm Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 27px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}))

    MIN_LENGTH = 8

    def clean_resetpassword(self):
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

        # Check Password not similar to username and email information
        username_similarity = difflib.SequenceMatcher(None, password.lower(), username.lower()).ratio()
        email_similarity = difflib.SequenceMatcher(None, password.lower(), email.lower()).ratio()

        similarity_threshold = 0.6  # Adjust this threshold as needed

        if username_similarity > similarity_threshold or email_similarity > similarity_threshold:
            raise forms.ValidationError("The new password cannot be too similar to your username or email.")

        return password

    def clean_resetpassword2(self):
        resetpassword = self.cleaned_data.get('password')
        resetpassword2 = self.cleaned_data.get('password2')

        if resetpassword and resetpassword2 and resetpassword != resetpassword2:
            raise forms.ValidationError(('The two password fields must match.'))

        return resetpassword2

    class Meta:
        model = User
        fields = ['password']


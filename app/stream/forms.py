from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from . models import VidStream, VidRequest, Profile, UserInfo, Setting, FriendRequset
# , Contact

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
        fields = ["reciever","description", "due_date"]

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
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     super(AddContactForm, self).__init__(*args, **kwargs)
    #     self.fields['reciever'].queryset = User.objects.exclude(user=self.request.user)

    def clean_sender(self):
        return User.objects.get(username=self.cleaned_data.get('sender'))


    def clean_receiver(self):
        return User.objects.get(username=self.cleaned_data.get('reciever'))

    class Meta:
        model = FriendRequset
        fields = ['sender','reciever']

    sender = forms.CharField(widget=forms.HiddenInput)
    reciever = forms.ModelChoiceField(
        queryset=User.objects.all(),
        # widget=forms.CheckboxSelectMultiple
    )

class SettingForm(forms.ModelForm):
    YES_NO = (('Yes', 'True'),('No', 'False'),)
    darkmode = forms.BooleanField(widget=forms.RadioSelect(choices=YES_NO, attrs={'placeholder' :'On/Off',
                                                        'class': 'form-control','required': True}))
    emailnotification = forms.BooleanField(widget=forms.RadioSelect(choices=YES_NO, attrs={'placeholder' :'On/Off',
                                                        'class': 'form-control','required': True}))
    class Meta:
        model = Setting
        fields = ['darkmode', 'emailnotification']

class SetPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password',
                                                                  'style': 'width: 400px; height: 45px; margin-left: auto; margin-right: auto; margin-bottom: 25px; border: 2px groove lightgreen;',
                                                                  'class': 'form-control', 'required': True}))

    class Meta:
        model = User
        fields = ['password']

from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile 
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


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
        widgets = {
        }

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']
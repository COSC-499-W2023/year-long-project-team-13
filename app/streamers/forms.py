from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile 
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Username', 
                                                             'style':'width: 300px; color: green;', 
                                                             'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 
                                                            'style': 'width: 300px; color: red;', 
                                                            'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password', 
                                                                  'style': 'width: 300px; color: blue;', 
                                                                  'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Confirm Password', 
                                                                  'style': 'width: 300px; color: purple;', 
                                                                  'class': 'form-control'}))

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
            'username': TextInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px; color:red;',
                'placeholder': 'Username'
            }),
            'email': EmailInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px; color:blue;',
                'placeholder': 'Email'
            })
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']
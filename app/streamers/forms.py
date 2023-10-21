from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile 
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': TextInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),
            'email': TextInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Email'
            }),
            'password1': TextInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px; color:green;',
                'placeholder': 'Password'
            }),
            'password2': TextInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px; color:yellow;',
                'placeholder': 'Confirm Password'
            })
        }


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']
        # widgets = {
        #     'username': TextInput(attrs = {
        #         'class': "form-control",
        #         'style': 'max-width: 300px; color:red;',
        #         'placeholder': 'Username'
        #     }),
        #     'email': EmailInput(attrs = {
        #         'class': "form-control",
        #         'style': 'max-width: 300px; color:blue;',
        #         'placeholder': 'Email'
        #     })
        # }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']
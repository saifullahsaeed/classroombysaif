from django.core import validators
from django import forms
from .models import User_data
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.core.validators import re
from django.contrib.auth.models import User


class UserRegistration(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': '*************'}))
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': '*************'}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Email address...'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password1','password2']
        labels = {'fist_name':'Firstname','last_name':'Last Name','email':'Email'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username...'})}



class UserLoginForm(AuthenticationForm):
    username = UsernameField( widget=forms.TextInput(attrs={'autofocus': True,'class': 'input100'}))
    password =  forms.CharField(label=("Password"),strip=False,widget=forms.PasswordInput(attrs={'class': 'input100'}))
    
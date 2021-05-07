from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       UsernameField)
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import re
from django_clamd.validators import validate_file_infection


class CreateClassForm(forms.Form):
    class_name= forms.CharField(error_messages = {'required': 'Give A Classroom name'},widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class Lable', 'id': 'text-input'}))
    class_limit =forms.IntegerField(error_messages = {'required': 'Give A student Limit'},widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Student Limit', 'id': 'text-input'}))    
    class_Discription = forms.CharField(error_messages = {'required': 'Give A Class Discription'},widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Class Discription', 'id': 'text-input'}))
    image = forms.FileField(required=False ,error_messages = {'required': 'Upload a Class banner'},widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'file-input'}))

class assignment(forms.Form):
    pass
class assignment_upload(forms.Form):
    assignment_id = forms.CharField(widget=forms.HiddenInput(),initial=0)
    assignment_file = forms.FileField(allow_empty_file=False,validators=[validate_file_infection])

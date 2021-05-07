from django import forms
from django.core import validators
import re

class messageForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Name','data-rule':'minlen:4','data-msg':'Please enter at least 4 chars'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Your Email','data-rule':'email','data-msg':'Please enter a valid email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Subject','data-rule':'minlen:4','data-msg':'Please enter at least 8 chars of subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':'5','class': 'form-control','placeholder':'Message','data-rule':'required','data-msg':'Please write something for us'}))
    def clean(self):
        cleaned_data = super().clean()
        name =self.cleaned_data['name']
        email =self.cleaned_data['email']
        subject =self.cleaned_data['subject']
        message =self.cleaned_data['message']    
        if len(name) < 4:
            raise forms.ValidationError("Please enter at least 4 chars")
        if len(subject) < 8:
            raise forms.ValidationError("Please enter at least 8 chars")
        if len(message) < 1:
            raise forms.ValidationError("Please write something for us")
        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email) != None:
            raise forms.ValidationError("Invalid Email")
    

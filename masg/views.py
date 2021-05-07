from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import messageForm
from .models import massages
# Create your views here.
def content_get(request):
    form = messageForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name =form.cleaned_data['name']
            email =form.cleaned_data['email']
            subject =form.cleaned_data['subject']
            message =form.cleaned_data['message']
            send =  massages(msg_name=name,msg_email=email,msg_subject=subject,msg_message=message)
            send.save()
            print(name,email,subject,message)
        else:
            form = messageForm()
    else:
        form = messageForm()
    return redirect("/")
    
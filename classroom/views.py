from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from masg.forms import messageForm

# Create your views here.
def index(request):
    auths = False
    if  request.user.is_authenticated:
        auths =True
    carasole_header = "The Virtual ClassRoom"
    carasole_punch = "An online plateform for teachers and student to make hair life easy and safe"
    now = datetime.now()
    slides_data= {'first':1,"second":2}
    value = 1
    print(auths)
    slides = {1:"1",2:"",3:"",4:""}
    time = now.strftime("%H:%M:%S")
    form = messageForm(auto_id=True)
    data = {"form":form, "title": "ClassRoom ~ Improve","time": time, "slides": slides,"carasole_header":carasole_header ,"carasole_punch":carasole_punch,"auth": auths}
    return render(request,'index.html',data)


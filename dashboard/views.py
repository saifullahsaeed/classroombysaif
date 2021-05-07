from django.shortcuts import redirect, render
from django.contrib.auth import logout
from auths.models import User_data
from auths.urls import urlpatterns
from classes.urls import urlpatterns
import classroom.urls
from dashboard.models import class_db
from django.http import HttpResponse
from classes.models import Students, class_lacture
from django.contrib.sites.shortcuts import get_current_site
import base64
from django.core.mail import message
from django.contrib import messages
from base64 import b64decode
from classes.urls import urlpatterns
from django.contrib.auth.models import User
# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        base64username = base64.b64encode(
            username.encode("ascii")).decode("ascii")
        db = User_data.objects.get(usr_username=username)
        is_teacher = False
        classes = None
        stu = None
        current_site = get_current_site(request)
        domain = current_site.domain
        empty = 0
        in_classes=[]
        is_student = False
        if db.usr_account_type == 2:
            is_teacher = True
        if is_teacher:
            try:
                if class_db.objects.filter(class_createdby=username).exists():
                    classes = class_db.objects.filter(class_createdby=username)
                    empty = 1
                else:
                    empty = 0
            except:
                empty = 0
        else:
            if Students.objects.filter(username=user).exists():
                empty = 1
                is_student = True
                stu = Students.objects.filter(username=user)
                for clases_stu in stu:
                    key = clases_stu.class_key.class_secretkey
                    classes = class_db.objects.filter(
                        class_secretkey=key)
                    #for u in classes:
                        #print(u.class_createdby,u.class_name)
                    in_classes.append(classes)
                print(in_classes)
                for a in in_classes:
                    for i in a:
                     print(i.class_name)
        usrname = db.usr_name
        usrmail = db.usr_email
        data = {"usr_name": usrname, "usr_email": usrmail,
                "db": db, "classes": classes, "in_classes": in_classes, "empty": empty, "stu": stu, "domain": domain, "base64_username": base64username}
        try:
            check = User_data.objects.filter(
                usr_account_type=0, usr_username=username).exists()
        except:
            check = False
        if check:
            return redirect('/dashboard/choseaccount')
        else:
            return render(request, 'dashboard/index.html', data)
    else:
        return redirect('/auth/login')


def logoutUser(request):
    logout(request)
    return redirect('/auth/login')


def select_account(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            check = User_data.objects.filter(
                usr_account_type=0, usr_username=username).exists()
        except:
            check = False
        print(check)
        if not check:
            return redirect('/dashboard')
        else:
            return render(request, 'auth/chooseaccount.html')
    else:
        return redirect('/auth/login')


def shift(request):
    if request.user.is_authenticated:
        username = request.user.username
        db = User_data.objects.get(usr_username=username)
        try:
            check = User_data.objects.filter(
                usr_account_type=0, usr_username=username).exists()
        except:
            check = False
        if check:
            return redirect('auth/choseaccount/')
        else:
            if db.usr_account_type == 1:
                enter = User_data.objects.filter(
                    usr_username=username).update(usr_account_type=2)
                return redirect('/dashboard')
            elif db.usr_account_type == 2:
                enter = User_data.objects.filter(
                    usr_username=username).update(usr_account_type=1)
                return redirect('/dashboard')
            else:
                return HttpResponse("<h1>Error</h1>")
    else:
        return redirect('/auth/login')


def join_student(request, key, usern, accept=0):
    if request.user.is_authenticated:
        username = request.user.username
        classis = class_db.objects.get(class_secretkey=key)
        db = User_data.objects.filter(usr_username=username)
        user = User.objects.get(username=username)
        clas = class_db.objects.filter(class_secretkey=key).exists()
        if clas is True:
            stud = Students.objects.filter(
                username=user, class_key=classis).exists()
            if stud is False:
                if accept == 0:
                    usr = usern.encode("ascii")
                    usr = b64decode(usr).decode("ascii")
                    dta = User_data.objects.get(usr_username=usr)
                    print(dta.usr_name)
                    return render(request, 'dashboard/joinmesg.html', {"user_name": dta.usr_name, "class": classis, "usern": usern, "key": key})
                else:
                    pass
            else:
                messages.info(request,"You are alrady in class "+classis.class_name)
                return redirect('/dashboard/')
        else:
            return HttpResponse('Invalid url')

    else:
        messages.error(
            request, 'You are not logind')
        return redirect('/auth/login')

def join_students(request, key, usern, accept):
    if request.user.is_authenticated:
        classis = class_db.objects.get(class_secretkey=key)
        username = request.user.username
        user = User.objects.get(username=username)
        db = User_data.objects.filter(usr_username=username)
        clas = class_db.objects.filter(class_secretkey=key).exists()
        if clas is True:
            stud = Students.objects.filter(
                username=user, class_key=classis).exists()
            if stud is False:
                if accept == 1:
                    classis = class_db.objects.get(class_secretkey=key)
                    Students(username=user,class_key=classis,class_name=classis.class_name).save()
                    messages.success(request,"Secussfullay joined the class "+classis.class_name)
                    return redirect('/dashboard/')
                else:
                    messages.Info(request,"You are alrady in class "+classis.class_name)
                    return redirect('/dashboard/')

            else:
                return HttpResponse('Alrady in class')
        else:
            return HttpResponse('Invalid url')

    else:
        messages.error(
            request, 'You are not logind')
        return redirect('/auth/login')
       

def account(request):
    db = User_data.objects.get(usr_username= request.user.username)
    data ={'db':db}
    return render(request,'dashboard/account.html',data)
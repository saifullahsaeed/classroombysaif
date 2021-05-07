from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, response
from dashboard.models import class_db
from django.utils import timezone
from auths.models import User_data
import uuid
from .models import *
from key_generator.key_generator import generate
from .forms import CreateClassForm,assignment_upload
from django.contrib import messages
from classes.models import Students, assignments
from asgiref.sync import sync_to_async
# Create your views here.

def viewed(lacture_id,user):
    if not views.objects.filter(for_lacture=lacture_id).exists():
        views(view_id=uuid4(),for_lacture=lacture_id,viewed_by=user).save()

def is_student(user):
    try:
        db= User_data.objects.filter(usr_username=user,usr_account_type=1).exists()
    except:
        return response(404)
    return db
def inclass(user,key):
    db= Students.objects.filter(username=user,class_key=key).exists()
    return db
def is_teacher(user,key):
    try:
        db= class_db.objects.filter(class_createdby=user,class_secretkey=key).exists()
    except:
        return response(404)
    return db

def add(request):
    if request.user.is_authenticated:
        db = User_data.objects.get(usr_username=request.user)

        if db.usr_account_type == 0 | db.usr_account_type == 1:
            return redirect('/dashboard/choseaccount')
        else:
            form = CreateClassForm()
            if request.method == 'POST':
                form = CreateClassForm(request.POST,request.FILES)
                if form.is_valid():
                    name_class = form.cleaned_data['class_name']
                    name_students = form.cleaned_data['class_limit']
                    name_disc = form.cleaned_data['class_Discription']
                    try:
                        image = request.FILES['image']
                    except:
                        image = "class_banners/default.png"
                    key =uuid.uuid4()
                    class_db(class_createdby=request.user,class_secretkey=key,class_name=name_class,class_limit=name_students,class_Discription=name_disc,class_image=image).save()
                    print (image,name_class,name_students,name_disc)
                    return redirect("/dashboard/")
                else:
                    form = CreateClassForm(request.POST)
            else:
                form = CreateClassForm()
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            data = {"title": "Classes ~ Improve", "time": time, "db": db,"form" : form}
            return render(request, 'classes/create.html', data)
    else:
        return redirect('/auth/login')

def classroom(request,**key):
    if request.user.is_authenticated:
        user = request.user
        db = User_data.objects.get(usr_username=request.user)
        user_obj = User.objects.get(username= user)
        for uid in key.values():
            print(uid)
        if class_db.objects.filter(class_secretkey=uid).exists() is False:
            return HttpResponse(status=404)
        classroom = class_db.objects.get(class_secretkey=uid)
        if is_student(db) is True:
            pass
        else:
            enter = User_data.objects.filter(
                    usr_username=user).update(usr_account_type=1) 
        if inclass(user,classroom) is True:
            student = Students.objects.filter(username=user,class_key=classroom)
            for stu in student:
                print(stu.date_of_join)
           # print(student.date_of_join)
            print("user is Student and in class") 
            data = {"title": "Classes ~ Improve", "db": db,"class":classroom,"student":stu}
            return render(request,"classes/classroom.html",data)
        else:
            messages.error(request,"You are not In This class")
            return redirect('/dashboard/')
    else:
        messages.error(request,"User Un-authanticated")
        return redirect('/auth/login')
    
def class_admin(request,**key):
    if request.user.is_authenticated:
        user = request.user
        db = User_data.objects.get(usr_username=request.user)
        user_obj = User.objects.get(username= user)
        for uid in key.values():
            print(uid)
        if class_db.objects.filter(class_secretkey=uid).exists() is False:
            return HttpResponse(status=404)
        classroom = class_db.objects.get(class_secretkey=uid)
        if is_student(db) is False:
            pass
        else:
            enter = User_data.objects.filter(
                    usr_username=user).update(usr_account_type=2) 
        if is_teacher(user,uid) is True:
            print("user is Teacher and in class") 
            data = {"title": "Classes ~ Improve", "db": db,"class":classroom}
            return render(request,"classes/class_admin.html",data)
        else:
            messages.error(request,"You are not Teacher of This class")
            return redirect('/dashboard/')
    else:
        messages.error(request,"User Un-authanticated")
        return redirect('/auth/login')

def lactures(request,**key):
    if request.user.is_authenticated:
        user = request.user
        db = User_data.objects.get(usr_username=request.user)
        user_obj = User.objects.get(username= user)
        for uid in key.values():
            print(uid)
        if class_db.objects.filter(class_secretkey=uid).exists() is False:
            return HttpResponse(status=404)
        classroom = class_db.objects.get(class_secretkey=uid)
        if is_student(db) is True:
            pass
        else:
            enter = User_data.objects.filter(
                    usr_username=user).update(usr_account_type=1) 
        if inclass(user,classroom) is True:
            student = Students.objects.filter(username=user,class_key=classroom)
            for stu in student:
                pass
            lactures = class_lacture.objects.filter(for_class=classroom)
            lacture_views = views.objects.filter(viewed_by=user_obj)
            data = { "db": db,"class":classroom,"lactures":lactures,"views":lacture_views,"classroom":classroom}
            return render(request,"classes/lactures.html",data)
        else:
            messages.error(request,"You are not In This class")
            return redirect('/dashboard/')
    else:
        messages.error(request,"User Un-authanticated")
        return redirect('/auth/login')

def lacture(request,id,key):
    if request.user.is_authenticated:
        if not class_db.objects.filter(class_secretkey=key).exists():
            return HttpResponse(status=404)
        if not class_lacture.objects.filter(lacture_id=id).exists():
            return HttpResponse(status=504)
        user = request.user
        user_obj = User.objects.get(username= user)
        classroom = class_db.objects.get(class_secretkey=key)
        db = User_data.objects.get(usr_username=request.user)
        if is_student(db) is True:
            pass
        else:
            enter = User_data.objects.filter(
                    usr_username=user).update(usr_account_type=1) 
        if inclass(user,classroom) is True:
            student = Students.objects.filter(username=user,class_key=classroom)
            for stu in student:
                pass
            lacture = class_lacture.objects.get(lacture_id=id)
            sync_to_async(viewed(lacture,user_obj))
            comments = comment.objects.filter(lacture_id=lacture)
            data = { "db": db,"class":classroom,"lacture":lacture,"comments":comments,"classroom":classroom}
            return render(request,"classes/lacture.html",data)
        else:
            messages.error(request,"You are not In This class")
            return redirect('/dashboard/')
    else:
        messages.error(request,"User Un-authanticated")
        return redirect('/auth/login')

def comments(reqest):
    return JsonResponse({'message' : "done"})

def assignment(request,**key):
        user = request.user
        db = User_data.objects.get(usr_username=request.user)
        for uid in key.values():
            print(uid)
        classroom = class_db.objects.get(class_secretkey=uid)
        if is_student(db) is True:
            pass
        else:
            enter = User_data.objects.filter(
                    usr_username=user).update(usr_account_type=1) 
        if inclass(user,classroom) is True:
            student = Students.objects.filter(username=user,class_key=classroom)
            for stu in student:
               pass
            Assignments = assignments.objects.filter(for_class=classroom)
            assignment_upload_form = assignment_upload()
            data = {"title": "Classes ~ Improve", "db": db,"class":classroom,"student":stu,'assignment_upload':assignment_upload_form,'assignments':Assignments}
            return render(request,"classes/assignment.html",data)
        else:
            messages.error(request,"You are not In This class")
            return redirect('/dashboard/')

def upload_assignment(request):
    if request.method == 'POST':
        form = assignment_upload(request.POST,request.FILES)
        
        if form.is_valid():
             print(form.cleaned_data['assignment_id'])
        try:
            if form.is_valid():
                print(form.cleaned_data['assignment_id'])
        except:
             return JsonResponse({"Uploaded": False})
        return JsonResponse({"Uploaded": True})


def quizz(request,**key):
    user = request.user
    db = User_data.objects.get(usr_username=request.user)
    for uid in key.values():
        print(uid)
    classroom = class_db.objects.get(class_secretkey=uid)
    if is_student(db) is True:
        pass
    else:
        enter = User_data.objects.filter(
                usr_username=user).update(usr_account_type=1) 
    if inclass(user,classroom) is True:
        student = Students.objects.filter(username=user,class_key=classroom)
        for stu in student:
            pass
        data = {"title": "Classes ~ Improve", "db": db,"class":classroom,"student":stu}
        return render(request,"classes/assignment.html",data)
    else:
        messages.error(request,"You are not In This class")
        return redirect('/dashboard/')

def announcements(request,**key):
    user = request.user
    db = User_data.objects.get(usr_username=request.user)
    for uid in key.values():
        print(uid)
    classroom = class_db.objects.get(class_secretkey=uid)
    if is_student(db) is True:
        pass
    else:
        enter = User_data.objects.filter(
                usr_username=user).update(usr_account_type=1) 
    if inclass(user,classroom) is True:
        student = Students.objects.filter(username=user,class_key=classroom)
        for stu in student:
            pass
        announements = announcement.objects.filter(for_class=classroom)
        data = {"title": "Classes ~ Improve", "db": db,"class":classroom,"student":stu,'announcements':announements}
        return render(request,"classes/announcements.html",data)
    else:
        messages.error(request,"You are not In This class")
        return redirect('/dashboard/')
def quizz(request,**key):
    return HttpResponse("Quiz page")
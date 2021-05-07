from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .forms import UserRegistration
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as set_login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from auths.models import User_data
from .forms import UserLoginForm
from django.http import request
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your views here.


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            formf = UserLoginForm(request=request, data=request.POST)
            # if formf.is_valid():
            username = formf.data.get('username')
            password = formf.data.get('password')
            user = authenticate(username=username, password=password)
            print(username)
            try:
                check = User_data.objects.filter(
                    usr_account_type=0, usr_username=username).exists()
            except:
                check = False
            if user is not None:
                set_login(request, user)
                if check:
                    return redirect('/dashboard/choseaccount')
                else:
                    return redirect('/dashboard')

            else:
                messages.error(request, "Invalid Credentials")
        else:
            formf = UserLoginForm()
        data = {"form": formf}
        return render(request, 'auth/login.html', data)
    else:
        return redirect('/dashboard')


def register(request):
    if not request.user.is_authenticated:
        data = UserRegistration(request.POST)
        if request.method == 'POST':
            if data.is_valid():
                user = data.save(commit=False)
                user.is_active = False
                data.save()
                current_site = get_current_site(request)
                message = render_to_string('auth/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                mail_subject = 'Activate your account.'
                name = data.cleaned_data['first_name']
                name_last = data.cleaned_data['last_name']
                email_is = data.cleaned_data['email']
                email = EmailMessage(
                    mail_subject, message, to=[email_is]
                )
                email.send()
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                username = data.cleaned_data['username']
                user_name = name + " " + name_last
                password = make_password(data.cleaned_data['password1'])
                enter = User_data(usr_username=username, usr_name=user_name,
                                  usr_email=email_is, usr_ip=ip, usr_password=password)
                res = enter.save()
                messages.success(
                    request, 'Varification Email Sent Check inbox Check Spam')
        else:
            data = UserRegistration()
        data = {"form": data}
        return render(request, 'auth/register.html', data)
    else:
        return redirect('/dashboard')


def choose_account(request, type):
    username = request.user.username
    if type == "student":
        enter = User_data.objects.filter(
            usr_username=username).update(usr_account_type=1)
        return redirect("/dashboard/")
    elif type == "teacher":
        enter = User_data.objects.filter(
            usr_username=username).update(usr_account_type=2)
        return redirect("/dashboard/")
    else:
        return HttpResponse(type)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token) and user.is_active is False:
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

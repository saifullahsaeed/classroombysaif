from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from auths.models import User_data
from django.utils.datetime_safe import datetime
from django.shortcuts import redirect


@receiver(user_logged_in)
def logedin_signal(sender, user, request, **kwargs):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        data = User_data.objects.get(usr_username = user)
    except:
        return redirect('')
    if data:
        data.usr_ip = ip
        data.usr_lastlogin = datetime.now().strftime("%b %d %Y %H:%M:%S")
        data.save() 
        
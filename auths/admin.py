from django.contrib import admin
from .models import User_data
# Register your models here.
@admin.register(User_data)
class User_dataAdmin(admin.ModelAdmin):
    list_display=('id','usr_name','usr_email','usr_ip','usr_password')

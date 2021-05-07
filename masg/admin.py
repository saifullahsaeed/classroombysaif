from django.contrib import admin
from masg.models import massages
# Register your models here.

@admin.register(massages)
class massageAdmin(admin.ModelAdmin):
    list_display=('id','msg_name','msg_email','msg_subject','msg_message')

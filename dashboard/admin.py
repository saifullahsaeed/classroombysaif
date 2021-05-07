from django.contrib import admin
from .models import class_db
# Register your models here.
@admin.register(class_db)
class class_dataAdmin(admin.ModelAdmin):
    list_display=('class_name','class_createdby','class_createdate','class_noofstudents')
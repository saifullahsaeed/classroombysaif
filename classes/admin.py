from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Students)
class Students(admin.ModelAdmin):
    list_display=('username','class_name','date_of_join','is_cr')

@admin.register(assignments)
class Assignments(admin.ModelAdmin):
    list_display=('title','Expires_Date','Upload_date')

@admin.register(assignment_submit)
class Submited_Assignments(admin.ModelAdmin):
    list_display=('submited_by','assignment_file','Upload_date')

@admin.register(quiz)
class quiz(admin.ModelAdmin):
    list_display=('title','Start_Date','Expires_Date')

@admin.register(class_lacture)
class Lactures(admin.ModelAdmin):
    list_display=('lacture_video','meterial','Upload_date')

@admin.register(views)
class Views(admin.ModelAdmin):
    list_display=('for_lacture','date')
    
@admin.register(comment)
class comments(admin.ModelAdmin):
    list_display=('lacture_id','comment','date')

@admin.register(announcement)
class comments(admin.ModelAdmin):
    list_display=('username','title','date','for_class')
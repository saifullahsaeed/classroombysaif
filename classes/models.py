from django.db import models
from dashboard.models import class_db
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.utils import timezone
from uuid import uuid3, uuid4
from django.urls import reverse

# Create your models here.
class Students(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100,default="Class Name")
    class_key = models.ForeignKey(class_db, on_delete=models.CASCADE,related_name='%(class)s_class_secretkey')
    date_of_join = models.DateTimeField(('date joined'), default=timezone.now)
    rollno =models.CharField(default="Rool No",max_length=100)
    is_cr=models.BooleanField(default=False)

class assignments(models.Model):
    for_class = models.ForeignKey(class_db, on_delete=models.CASCADE,related_name='%(class)s_class_secretkey')
    Start_Date = models.DateTimeField(('Start date'), default=timezone.now)
    Expires_Date = models.DateTimeField(('Due date'), default=timezone.now)
    Upload_date = models.DateTimeField(('date uploaded'), default=timezone.now)
    title = models.CharField(max_length=100,default="Assignment Title")
    uid = models.CharField(max_length=100,default="Uid")
    assignment_file=models.FileField(upload_to="assignments",blank=True)
class assignment_submit(models.Model):
    for_class = models.ForeignKey(class_db, on_delete=models.CASCADE,related_name='%(class)s_class_secretkey')
    assignment_id = models.CharField(max_length=100,default="Uid")
    submited_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assignment_file=models.FileField(upload_to="assignments",blank=True)
    Upload_date = models.DateTimeField(('date uploaded'), default=timezone.now)
class quiz(models.Model):
    for_class = models.ForeignKey(class_db, on_delete=models.CASCADE,related_name='%(class)s_class_secretkey')
    title = models.CharField(max_length=100,default="quiz Title")
    quiz_id = models.UUIDField()
    Start_Date = models.DateTimeField(('Start date'), default=timezone.now)
    Expires_Date = models.DateTimeField(('Due date'), default=timezone.now)
class class_lacture(models.Model):
    lacture_id = models.CharField(("lacture ID"), max_length=50)
    title = models.CharField(max_length=100,default="Lacture Title")
    Discription = models.CharField(max_length=100,default="There Is No Discription About This Lacture")
    for_class = models.ForeignKey(class_db, on_delete=models.CASCADE,related_name='%(class)s_class_secretkey')
    lacture_video = models.URLField(max_length=100)
    Related = models.CharField(max_length=100,default="There Is No Related Links for This Lacture Till Now")
    meterial = models.URLField(max_length=100)
    Upload_date = models.DateTimeField(('date uploaded'), default=timezone.now)

class comment(models.Model):
    comment_id = models.UUIDField(primary_key=True)
    lacture_id = models.ForeignKey(class_lacture, on_delete=models.CASCADE,related_name='%(class)s_class_secretkey')
    comment = models.CharField(max_length = 100,)
    comment_by =  models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(("Post Date"), default=timezone.now)

    class Meta:
        verbose_name = ("comment")
        verbose_name_plural = ("comments")

class views(models.Model):
    view_id = models.UUIDField(primary_key=True)
    for_lacture = models.ForeignKey(class_lacture, on_delete=models.CASCADE)
    viewed_by= models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(('view uploaded'), default=timezone.now)

class announcement(models.Model):
    for_class = models.ForeignKey(class_db, on_delete=models.CASCADE,related_name='%(class)s_class_secretkey')
    title = models.CharField(max_length=100,default="quiz Title")
    Discription = models.CharField(max_length=100,default="There Is No Discription About This Lacture")
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(('view uploaded'), default=timezone.now)
    class Meta:
        verbose_name = ("announcement")
        verbose_name_plural = ("announcements")


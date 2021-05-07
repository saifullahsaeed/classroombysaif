from django.db import models
from auths.models import User_data
from django.contrib.auth.models import User
from key_generator.key_generator import generate



# Create your models here.
class class_db(models.Model):
    class_name = models.CharField(max_length=50,)
    class_createdby = models.CharField(max_length=50,)
    class_createdate = models.DateTimeField(auto_now_add=True, blank=True)
    class_Discription = models.TextField(null=True)
    class_noofstudents = models.IntegerField(default=0,)
    class_limit = models.IntegerField(default=10)
    class_secretkey = models.CharField(max_length=50,unique=True,default=generate(seed = 101).get_key())
    class_cr = models.CharField(max_length=50,default="Select One")
    class_no_of_subjects = models.IntegerField(blank=False,default=1)
    class_image=models.ImageField(upload_to="class_banners",default="class_banners/default.png")
    class Meta:
        db_table="Class_db"
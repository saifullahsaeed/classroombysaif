from django.db import models
from django.utils.datetime_safe import datetime
from django.contrib.postgres.fields.array import ArrayField
# Create your models here.
class User_data(models.Model):
    id = models.AutoField(primary_key = True,editable=False)
    usr_name = models.CharField(max_length=100)
    usr_username = models.CharField(max_length=20)
    usr_email = models.EmailField(max_length=160)
    usr_password = models.CharField(max_length=200)
    usr_inclasses= ArrayField(models.CharField(max_length=200,null=True), null=True)
    usr_account_type = models.IntegerField(default=0)
    usr_ip = models.GenericIPAddressField(max_length=20,default="127.0.0.1")
    usr_phone=models.CharField(max_length=15,default="")
    usr_profilepic = models.ImageField(upload_to="profile_pic",default="profile_pic/user-demo.png")
    class Meta:
        db_table="users"
    
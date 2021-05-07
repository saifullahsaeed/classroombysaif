from django.db import models

# Create your models here.
class massages(models.Model):
    msg_name = models.CharField(max_length=70)
    msg_email = models.EmailField(max_length=70)
    msg_subject = models.CharField(max_length=70)
    msg_message = models.CharField(max_length=70)
    

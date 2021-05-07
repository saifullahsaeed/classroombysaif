from django.db.models.signals import post_save 
from django.dispatch import receiver

@receiver(post_save)

def database_add(sender,created,raw,**kwargs):
    print(sender,"a",created,"a<",raw)
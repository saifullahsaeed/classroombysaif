from django.urls import re_path
from channels import consumer
from . import consumer

websoket_urlpattrens=[
    re_path('ws/comment',consumer.studentComment.as_asgi()),
]
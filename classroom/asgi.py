"""
ASGI config for classroom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from classes.channels import websoket_urlpattrens

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classroom.settings')

application = ProtocolTypeRouter({
 'http' : get_asgi_application(),
 'websocket' : AuthMiddlewareStack(URLRouter(websoket_urlpattrens)),
})

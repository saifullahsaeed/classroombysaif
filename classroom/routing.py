from channels.auth import AuthMiddlewareStack 
from channels.routing import ProtocolTypeRouter, URLRouter
import classes.channels

application = ProtocolTypeRouter({
    'websoket' : AuthMiddlewareStack(
        URLRouter(
            classes.channels.websoket_urlpattrens
        )
    )
})
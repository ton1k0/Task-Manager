from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/general-chat/(?P<chat_id>\d+)/$', consumers.GeneralChatConsumer.as_asgi()),
    re_path(r'ws/personal-chat/(?P<chat_id>\d+)/$', consumers.PersonalChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})



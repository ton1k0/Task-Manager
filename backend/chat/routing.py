from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/general-chat/(?P<chat_id>\d+)/$', consumers.GeneralChatConsumer.as_asgi()),
    re_path(r'ws/personal-chat/(?P<chat_id>\d+)/$', consumers.PersonalChatConsumer.as_asgi()),
]



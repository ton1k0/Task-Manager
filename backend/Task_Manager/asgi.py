import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Task_Manager.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack  # Добавьте импорт
from chat.routing import websocket_urlpatterns



application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(  # Добавьте AuthMiddlewareStack
            URLRouter(websocket_urlpatterns)
        ),
    }
)
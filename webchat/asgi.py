import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from webchat.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<int:chat_id>/', ChatConsumer.as_asgi()),
        ])
    ),
})

print("ASGI application is being used.")
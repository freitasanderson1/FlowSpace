import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from webchat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat.settings')

# Carregar a aplicação Django
django_asgi_app = get_asgi_application()

# Verificar se o middleware foi inserido corretamente
application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": AuthMiddlewareStack(
      URLRouter(
        websocket_urlpatterns  # Seu arquivo de roteamento para WebSockets
      )
  ),
})

print("ASGI application is being used.")
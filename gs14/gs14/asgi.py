import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from App import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs14.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": URLRouter(
            routing.websocket_urlpatterns
    )
    
})

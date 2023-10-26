from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/wsc/<str:groupName>/", consumers.MyWebsocketConsumer.as_asgi()),
    path("ws/awsc/<str:groupName>/", consumers.MyAsyncWebsocketConsumer.as_asgi()),
]

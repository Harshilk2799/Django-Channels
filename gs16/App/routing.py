from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/jwsc/", consumers.MyJsonWebsocketConsumer.as_asgi()),
    path("ws/ajwsc/", consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]

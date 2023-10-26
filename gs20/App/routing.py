from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/jwsc/<str:groupname>/", consumers.MyJsonWebsocketConsumer.as_asgi()),
    path("ws/ajwsc/<str:groupname>/", consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]

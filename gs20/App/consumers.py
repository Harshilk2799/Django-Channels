from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Chat, Group

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    # This handler is called when client initially opens a connection and is about 
    # to finish the Websocket handshake.
    def connect(self):
        print("Websocket Connected...")
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        self.group_name = self.scope["url_route"]["kwargs"]["groupname"]
        print("Group Name: ", self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()  # To accept the connection

    # This handler is called when data received from client with decoded JSON content
    def receive_json(self, content, **kwargs):
        print("Message receive from Client: ", content)

        # Find group object
        group = Group.objects.get(name = self.group_name)
        if self.scope["user"].is_authenticated:
            chat = Chat(
                content = content["msg"],
                group = group
            )
            chat.save()
            
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type":"chat.message",
                    "message": content["msg"]
                }
            )
        else:
            self.send_json({
                "message":"Login Required..."
            })

    def chat_message(self, event):
        print("Event: ", event)
        self.send_json({"message": event["message"]})

    # This handler is called when either connection to the client is lost, either from the client 
    # closing the connection, the server closing the connection, or loss of the socket.
    def disconnect(self, close_code):
        print("Websocket Disconnect..", close_code)
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()
    


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    # This handler is called when client initially opens a connection and is about 
    # to finish the Websocket handshake.
    async def connect(self):
        print("Websocket Connected...")
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        self.group_name = self.scope["url_route"]["kwargs"]["groupname"]
        print("Group Name: ", self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()  # To accept the connection


    # This handler is called when data received from client with decoded JSON content
    async def receive_json(self, content, **kwargs):
        print("Message receive from Client: ", content)

        # Find group object
        group = await database_sync_to_async(Group.objects.get)(name = self.group_name)
        if self.scope["user"].is_authenticated:
            chat = Chat(
                content = content["msg"],
                group = group
            )
            await database_sync_to_async(chat.save)()

            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type":"chat.message",
                    "message": content["msg"]
                }
            )
        else:
            await self.send_json({
                "message":"Login Required..."
            })

    async def chat_message(self, event):
        print("Event: ", event)
        await self.send_json({"message": event["message"]})

    # This handler is called when either connection to the client is lost, either from the client 
    # closing the connection, the server closing the connection, or loss of the socket.
    async def disconnect(self, close_code):
        print("Websocket Disconnect..", close_code)
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
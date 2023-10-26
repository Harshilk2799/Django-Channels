from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Group, Chat
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connect....", event)
        print("Channel Layer...", self.channel_layer) # Get Default Channel layer from a project
        print("Channel Name: ", self.channel_name) # Get Channel Name
        print("Group Name: ",self.scope["url_route"]["kwargs"]["groupname"])
        self.group_name = self.scope["url_route"]["kwargs"]["groupname"]
        print("Group Name: ", self.group_name)
        # Add a channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.send({"type":"websocket.accept"})

    def websocket_receive(self, event):
        print("Message received from Client: ", event["text"])
        print("type of Message received from Client: ", type(event["text"]))
        data = json.loads(event["text"])
        print("Data: ", data)
        print("Type of Data: ", type(data))
        print("Chat Message: ", data["msg"])

        # Find Group Object 
        group = Group.objects.get(name = self.group_name)

        # Create New Chat Object 
        chat = Chat(
            content = data["msg"],
            group = group
        )
        chat.save()

        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            "type":"chat.message",
            "message":event["text"]
        })

    def chat_message(self, event):
        print("Event: ", event)
        print("Actual Data: ", event["message"])
        print("Type of Actual Data: ", type(event["message"]))
        self.send({
            "type":"websocket.send",
            "text": event["message"]
        })

    def websocket_disconnect(self, event):
        print("Websocket Disconnect...", event)
        print("Channel Layer...", self.channel_layer) # Get Default Channel layer from a project
        print("Channel Name: ", self.channel_name) # Get Channel Name
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        raise StopConsumer()




class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connect....", event)
        print("Channel Layer...", self.channel_layer) # Get Default Channel layer from a project
        print("Channel Name: ", self.channel_name) # Get Channel Name
        print("Group Name: ",self.scope["url_route"]["kwargs"]["groupname"])
        self.group_name = self.scope["url_route"]["kwargs"]["groupname"]
        print("Group Name: ", self.group_name)
        # Add a channel to a new or existing group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.send({"type":"websocket.accept"})

    async def websocket_receive(self, event):
        print("Message received from Client: ", event["text"])
        print("type of Message received from Client: ", type(event["text"]))
        
        data = json.loads(event["text"])
        print("Data: ", data)
        print("Type of Data: ", type(data))
        print("Chat Message: ", data["msg"])

        # Find Group Object 
        group = await database_sync_to_async(Group.objects.get)(name = self.group_name)

        # Create New Chat Object 
        chat = Chat(
            content = data["msg"],
            group = group
        )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(self.group_name, {
            "type":"chat.message",
            "message":event["text"]
        })

    async def chat_message(self, event):
        print("Event: ", event)
        print("Actual Data: ", event["message"])
        print("Type of Actual Data: ", type(event["message"]))
        await self.send({
            "type":"websocket.send",
            "text": event["message"]
        })

    async def websocket_disconnect(self, event):
        print("Websocket Disconnect...", event)
        print("Channel Layer...", self.channel_layer) # Get Default Channel layer from a project
        print("Channel Name: ", self.channel_name) # Get Channel Name
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()

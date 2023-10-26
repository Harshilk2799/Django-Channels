from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json

# WebsocketConsumer
class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connect...")
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        self.group_name = self.scope["url_route"]["kwargs"]["groupName"]
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        print("Group Name: ", self.group_name)
        # self.channel_layer
        self.accept()  # To Accept the connection
    
    def receive(self, text_data=None, bytes_data=None):
        print("Message Received from client...", text_data)
        data = json.loads(text_data)
        print("Data: ", data)
        message = data["msg"]
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat.message",
                "message": message
            }
        )

    def chat_message(self, event):
        print("Event: ", event)
        self.send(text_data=json.dumps({"msg":event["message"]}))

    def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
        raise StopConsumer()
    

# AsyncWebsocketConsumer
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket Connect...")
        print("Channel Layer: ", self.channel_layer)
        print("Channel Name: ", self.channel_name)
        self.group_name = await self.scope["url_route"]["kwargs"]["groupName"]
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        print("Group Name: ", self.group_name)
        # self.channel_layer
        await self.accept()  # To Accept the connection
    
    async def receive(self, text_data=None, bytes_data=None):
        print("Message Received from client...", text_data)
        data = json.loads(text_data)
        print("Data: ", data)
        message = data["msg"]
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat.message",
                "message": message
            }
        )

    async def chat_message(self, event):
        print("Event: ", event)
        await self.send(text_data=json.dumps({"msg":event["message"]}))

    async def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
        raise StopConsumer()
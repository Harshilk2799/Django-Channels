from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

# WebsocketConsumer
class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connect...")
        self.accept()  # To Accept the connection
    
    def receive(self, text_data=None, bytes_data=None):
        print("Message Received from client...", text_data)
        for i in range(6):
            self.send(text_data=str(i)) # To send data to client
            sleep(1)

    def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
        raise StopConsumer()
    

# AsyncWebsocketConsumer
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket Connect...")
        await self.accept()  # To Accept the connection
    
    async def receive(self, text_data=None, bytes_data=None):
        print("Message Received from client...", text_data)
        for i in range(6):
            await self.send(text_data=str(i)) # To send data to client
            await asyncio.sleep(1)

    async def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
        raise StopConsumer()
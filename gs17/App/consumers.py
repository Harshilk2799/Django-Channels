from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    # This handler is called when client initially opens a connection and is about 
    # to finish the Websocket handshake.
    def connect(self):
        print("Websocket Connected...")
        self.accept()  # To accept the connection

    # This handler is called when data received from client with decoded JSON content
    def receive_json(self, content, **kwargs):
        print("Message receive from Client: ", content)
        print("Type of Message receive from Client: ", type(content))
        
        # Encode the given content as JSON and send it to the client.
        for i in range(1,16):
            self.send_json({"msg":str(i)})
            sleep(1)

    # This handler is called when either connection to the client is lost, either from the client 
    # closing the connection, the server closing the connection, or loss of the socket.
    def disconnect(self, close_code):
        print("Websocket Disconnect..", close_code)
        raise StopConsumer()
    


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    # This handler is called when client initially opens a connection and is about 
    # to finish the Websocket handshake.
    async def connect(self):
        print("Websocket Connected...")
        await self.accept()  # To accept the connection

    # This handler is called when data received from client with decoded JSON content
    async def receive_json(self, content, **kwargs):
        print("Message receive from Client: ", content)
        print("Type of Message receive from Client: ", type(content))

        # Encode the given content as JSON and send it to the client.
        for i in range(1,16):   
            await self.send_json({"msg":str(i)})
            await asyncio.sleep(1)

    # This handler is called when either connection to the client is lost, either from the client 
    # closing the connection, the server closing the connection, or loss of the socket.
    async def disconnect(self, close_code):
        print("Websocket Disconnect..", close_code)
        raise StopConsumer()
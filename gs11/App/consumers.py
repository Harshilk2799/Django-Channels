from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer

# WebsocketConsumer
class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when client initially opens a connection and is about to finish the websocket handshake.
    def connect(self):
        print("Websocket Connect...")
        self.accept()  # To Accept the connection
        # self.close()  # To Reject the connection
    
    # This handler is called when data received from client.
    def receive(self, text_data=None, bytes_data=None):
        print("Message Received from client...", text_data)
        self.send(text_data="Hi, Message from Server...")

        # self.send(bytes_data=data)  # To send Binary frame to client
        # self.close()  # To force-close the connection
        # self.close(code=4123)  # To add a custom websocket error code

    # This handler is called when either connection to the client is lost, either from the client closing the connection, then 
    # server closing the connection, or loss of the socket.
    def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
        raise StopConsumer()
    

# AsyncWebsocketConsumer
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when client initially opens a connection and is about to finish the websocket handshake.
    async def connect(self):
        print("Websocket Connect...")
        await self.accept()  # To Accept the connection
        # await self.close()  # To Reject the connection
    
    # This handler is called when data received from client.
    async def receive(self, text_data=None, bytes_data=None):
        print("Message Received from client...", text_data)
        await self.send(text_data="Hi, Message from Server...")

        # await self.send(bytes_data=data)  # To send Binary frame to client
        # await self.close()  # To force-close the connection
        # await self.close(code=4123)  # To add a custom websocket error code

    # This handler is called when either connection to the client is lost, either from the client closing the connection, then 
    # server closing the connection, or loss of the socket.
    async def disconnect(self, close_code):
        print("Websocket Disconnected...", close_code)
        raise StopConsumer()
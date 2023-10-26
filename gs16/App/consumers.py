from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    # This handler is called when client initially opens a connection and is about 
    # to finish the Websocket handshake.
    def connect(self):
        print("Websocket Connected...")
        self.accept()  # To accept the connection
        # self.close()  # To reject the connection

    # This handler is called when data received from client with decoded JSON content
    def receive_json(self, content, **kwargs):
        print("Message receive from Client: ", content)
        print("Type of Message receive from Client: ", type(content))

        # Encode the given content as JSON and send it to the client.
        self.send_json({"msg":"Message from server to client."})

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
        # await self.close()  # To reject the connection

    # This handler is called when data received from client with decoded JSON content
    async def receive_json(self, content, **kwargs):
        print("Message receive from Client: ", content)
        print("Type of Message receive from Client: ", type(content))

        # Encode the given content as JSON and send it to the client.
        await self.send_json({"msg":"Message from server to client."})

    # This handler is called when either connection to the client is lost, either from the client 
    # closing the connection, the server closing the connection, or loss of the socket.
    async def disconnect(self, close_code):
        print("Websocket Disconnect..", close_code)
        raise StopConsumer()
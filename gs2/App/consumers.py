from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    # This handler is called when client initially opens a connection and 
    # is about to finish the websocket handshake.
    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        self.send({"type":"websocket.accept"})

    # This handler is called when data received from client.
    def websocket_receive(self, event):
        print("Messaged Received...", event)
        print("Message: ", event["text"])

    # This handler is called when either connection to the client is lost, either 
    # from the client closing the connection, the server closing the connection,
    # or loss of the socket.
    def websocket_disconnect(self, event):
        print("Websocket Disconnect...", event)
        raise StopConsumer()



class MyAsyncConsumer(AsyncConsumer):
    # This handler is called when client initially opens a connection and 
    # is about to finish the websocket handshake.
    async def websocket_connect(self, event):
        print("Websocket Connected...", event)
        await self.send({"type":"websocket.accept"})

    # This handler is called when data received from client.
    async def websocket_receive(self, event):
        print("Messaged Received...", event)
        print("Message: ", event["text"])

    # This handler is called when either connection to the client is lost, either 
    # from the client closing the connection, the server closing the connection,
    # or loss of the socket.
    async def websocket_disconnect(self, event):
        print("Websocket Disconnect...", event)
        raise StopConsumer()


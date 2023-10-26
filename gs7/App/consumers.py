from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connect....", event)
        print("Channel Layer...", self.channel_layer) # Get Default Channel layer from a project
        print("Channel Name: ", self.channel_name) # Get Channel Name
        # Add a channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)("Programmers", self.channel_name)
        self.send({"type":"websocket.accept"})

    def websocket_receive(self, event):
        print("Message received from Client: ", event["text"])
        print("type of Message received from Client: ", type(event["text"]))
        async_to_sync(self.channel_layer.group_send)("Programmers", {
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
        async_to_sync(self.channel_layer.group_discard)("Programmers", self.channel_name)
        raise StopConsumer()




class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connect....", event)
        print("Channel Layer...", self.channel_layer) # Get Default Channel layer from a project
        print("Channel Name: ", self.channel_name) # Get Channel Name
        # Add a channel to a new or existing group
        await self.channel_layer.group_add("Programmers", self.channel_name)
        await self.send({"type":"websocket.accept"})

    async def websocket_receive(self, event):
        print("Message received from Client: ", event["text"])
        print("type of Message received from Client: ", type(event["text"]))
        await self.channel_layer.group_send("Programmers", {
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
        await self.channel_layer.group_discard("Programmers", self.channel_name)
        raise StopConsumer()

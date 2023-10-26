from time import sleep
import asyncio
import json
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connect....", event)
        self.send({"type":"websocket.accept"})

    def websocket_receive(self, event):
        print("Message received from Client: ", event["text"])
        for i in range(1,16):
            # self.send({"type":"websocket.send", "text":str(i)})
            self.send({"type":"websocket.send", "text":json.dumps({"count":i})})
            sleep(1)


    def websocket_disconnect(self, event):
        print("Websocket Disconnect...", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connect....", event)
        await self.send({"type":"websocket.accept"})

    async def websocket_receive(self, event):
        print("Message received from Client: ", event["text"])
        for i in range(1,16):
            await self.send({"type":"websocket.send", "text":str(i)})
            # await self.send({"type":"websocket.send", "text":json.dumps({"count":i})})
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print("Websocket Disconnect...", event)
        raise StopConsumer()
        
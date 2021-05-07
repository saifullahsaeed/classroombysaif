from channels.generic.websocket import AsyncWebsocketConsumer
import json

class studentComment(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in range(1000):
            self.send(json.dumps({'comment' : "Hello"}))
        return super().connect()
    
# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer,AsyncConsumer
from asgiref.sync import async_to_sync
from .models import Post
from django.utils import timezone
from django.core import serializers
from dashboard.views import update
# from asgiref.sync import sync_to_async
import asyncio
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        
        self.send(text_data=update())

class ChatConsumer_A(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })

        while True:
            await asyncio.sleep(1)

            obj = await update() #(Ex: constantly query DB...)

            await self.send({
                'type': 'websocket.send',
                'text': obj,
            })

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
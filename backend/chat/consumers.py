import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import GeneralMessage, GeneralChat, PersonalChat, PersonalMessage
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from asgiref.sync import sync_to_async
import httpx
from django.utils.encoding import smart_str


class GeneralChatConsumer(AsyncWebsocketConsumer):
    async def get_user(self, token):
        jwt_auth = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(token)
        user = await sync_to_async(jwt_auth.get_user)(validated_token)
        return user

    async def get_chat(self, token, chat_id):
        user = await self.get_user(token)
        chat = await sync_to_async(GeneralChat.objects.get)(id=chat_id, members=user)
        return chat

    async def connect(self):
        user_id = self.scope["session"]["_auth_user_id"]
        self.group_name = "{}".format(user_id)
        # Join room group

        headers = self.scope.get('headers', [])
        token_header = [header for header in headers if header[0].decode('utf-8').lower() == 'authorization']
        if token_header:
            token = token_header[0][1].decode('utf-8').split()[0]
        else:
            await self.close()
            return

        try:
            user = await self.get_user(token)

            chat = await self.get_chat(token, self.chat_id)
            if not chat:
                await self.close()
                return

            await self.channel_layer.group_add(
                self.chat_group_name,
                self.channel_name
            )

            await self.accept()

            # Fetch chat history using API
            url = f"http://localhost:8000/chat/general-chat/{self.chat_id}/history/"
            headers = {'Authorization': f'Bearer {token}'}
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers)
                if response.status_code == 200:
                    chat_history = response.json()['results']
                    messages = []
                    for message in chat_history:
                        message['text'] = smart_str(message['text'])
                        messages.append(message)

                    await self.send(text_data=json.dumps(messages, ensure_ascii=False))

        except (User.DoesNotExist, IndexError):
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_text = text_data_json['message']

        headers = self.scope.get('headers', [])
        token_header = [header for header in headers if header[0].decode('utf-8').lower() == 'authorization']
        if token_header:
            token = token_header[0][1].decode('utf-8').split()[0]
        else:
            await self.close()
            return

        try:
            user = await self.get_user(token)
            chat = await sync_to_async(GeneralChat.objects.get)(id=self.chat_id)
            message = await sync_to_async(GeneralMessage.objects.create)(text=message_text, chat=chat, author=user)
        except (User.DoesNotExist, ObjectDoesNotExist):
            await self.close()
            return

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message_text,
                'author_id': user.id,
                'created_at': message.created_at.isoformat()
            }
        )

    async def chat_message(self, event):
        message = event['message']
        author_id = event['author_id']
        created_at = event['created_at']

        await self.send(text_data=json.dumps({
            'message': message,
            'author_id': author_id,
            'created_at': created_at
        }, ensure_ascii=False, separators=(',', ':')))


class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def get_user(self, token):
        jwt_auth = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(token)
        user = await sync_to_async(jwt_auth.get_user)(validated_token)
        return user

    async def get_chat(self, token, chat_id):
        user = await self.get_user(token)
        chat = await sync_to_async(PersonalChat.objects.get)(id=chat_id, participants=user)
        return chat

    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f'personal_chat_{self.chat_id}'

        headers = self.scope.get('headers', [])
        token_header = [header for header in headers if header[0].decode('utf-8').lower() == 'authorization']
        if token_header:
            token = token_header[0][1].decode('utf-8').split()[0]
        else:
            await self.close()
            return

        try:
            user = await self.get_user(token)

            chat = await self.get_chat(token, self.chat_id)
            if not chat:
                await self.close()
                return

            await self.channel_layer.group_add(
                self.chat_group_name,
                self.channel_name
            )

            await self.accept()

            # Fetch chat history using API
            url = f"http://localhost:8000/chat/personal-chat/{self.chat_id}/history/"
            headers = {'Authorization': f'Bearer {token}'}
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers)
                if response.status_code == 200:
                    chat_history = response.json()['results']
                    messages = []
                    for message in chat_history:
                        message['text'] = smart_str(message['text'])
                        messages.append(message)

                    await self.send(text_data=json.dumps(messages, ensure_ascii=False))

        except (User.DoesNotExist, IndexError):
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_text = text_data_json['message']

        headers = self.scope.get('headers', [])
        token_header = [header for header in headers if header[0].decode('utf-8').lower() == 'authorization']
        if token_header:
            token = token_header[0][1].decode('utf-8').split()[0]
        else:
            await self.close()
            return

        try:
            user = await self.get_user(token)
            chat = await sync_to_async(PersonalChat.objects.get)(id=self.chat_id)
            message = await sync_to_async(PersonalMessage.objects.create)(text=message_text, chat=chat, author=user)
        except (User.DoesNotExist, ObjectDoesNotExist):
            await self.close()
            return

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'personal_chat_message',
                'message': message_text,
                'author_id': user.id,
                'created_at': message.created_at.isoformat()
            }
        )

    async def personal_chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
            'author_id': author_id,
            'created_at': created_at
        }, ensure_ascii=False, separators=(',', ':')))

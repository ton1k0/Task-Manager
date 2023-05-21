from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Message, Chat
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f'chat_{self.chat_id}'

        # Проверяем, принадлежит ли пользователь к данному чату
        token_key = self.scope['query_string'].decode().split('=')[1]
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            chat = Chat.objects.filter(id=self.chat_id, members=user).first()
            if not chat:
                # Если пользователь не принадлежит к чату, закрываем соединение
                await self.close()
                return
        except ObjectDoesNotExist:
            # Обработка неверного токена или неидентифицированного пользователя
            await self.close()
            return

        # Присоединяем клиента к группе чата
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Отсоединяем клиента от группы чата
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Обрабатываем полученное сообщение
        text_data_json = json.loads(text_data)
        message_text = text_data_json['message']

        # Сохраняем сообщение в базе данных
        token_key = self.scope['query_string'].decode().split('=')[1]
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            chat = Chat.objects.get(id=self.chat_id)
            message = Message.objects.create(text=message_text, chat=chat, author=user)
        except ObjectDoesNotExist:
            # Обработка неверного токена или неидентифицированного пользователя
            await self.close()
            return

        # Отправляем сообщение всем клиентам в группе чата
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
        # Отправляем полученное сообщение клиенту
        message = event['message']
        author_id = event['author_id']
        created_at = event['created_at']

        await self.send(text_data=json.dumps({
            'message': message,
            'author_id': author_id,
            'created_at': created_at
        }))

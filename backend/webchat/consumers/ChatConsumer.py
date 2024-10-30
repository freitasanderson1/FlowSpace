import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = parse_qs(self.scope['query_string'].decode('utf8')).get('username')[-1]
        # print(f"USERNAME: {self.username}")

        self.room_group_name = f'chat_{self.username}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        from webchat.models import Chat, ChatMessages, Usuario
        # print(f"Chat: {text_data_json.get('chat')}")
        chat = await Chat.objects.aget(id=text_data_json.get('chat'))
        user = await Usuario.objects.aget(username=self.username)
        message = text_data_json.get('message')

        # print(f'Mensagem: {message} de {self.username} para o CHAT ID:{chat.id}')

        novaMensagem = ChatMessages(
            chat=chat,
            quemEnviou=user,
            conteudo=message
        )
        await sync_to_async(novaMensagem.save)()  

        
        for usuario in await sync_to_async(list)(chat.usuarios.all()):  
            await self.channel_layer.group_send(
                f'chat_{usuario.username}',
                {
                    'type': 'chat_message',
                    'message': message,
                    'time': novaMensagem.dataEnvio.strftime("%Y-%m-%d %H:%M:%S") ,
                    'sender_username': self.username,  
                }
            )
            if usuario != user:
                await sync_to_async(novaMensagem.quemRecebeu.add)(usuario)

    async def chat_message(self, event):
        message = event['message']
        sender_username = event['sender_username']  
        time = event['time']  
        # print(f'Teste Sender: {event}')
        await self.send(text_data=json.dumps({
            'message': message,
            'sender_username': sender_username,
            'time': time,  
        }))
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
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
        from webchat.models import ChatMessages
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        recipient_username = text_data_json.get('recipient_username')  # Username do usuário de destino
        
        print(f'Mensagem: {message} de {self.username} para {recipient_username}')
        
        # Envia a mensagem para o grupo do usuário de destino
        room_group_name = f'chat_{recipient_username}'

        ChatMessages.objects.create(
            quemEnviou__username=self.username, 
            quemRecebeu=recipient_username, 
            conteudo=message)

        await self.channel_layer.group_send(
            room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_username': self.username,  # Inclui o username do remetente
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_username = event['sender_username']  # Username do remetente

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_username': sender_username,  # Inclui o username do remetente na resposta
        }))
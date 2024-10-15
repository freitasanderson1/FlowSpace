from rest_framework import serializers

from webchat.models import Chat
from webchat.serializers import ChatMessagesSerializer

class ChatSerializer(serializers.ModelSerializer):
  mensagens = ChatMessagesSerializer(source='chatmessages_set', many=True)

  class Meta:
    model = Chat
    fields = '__all__'
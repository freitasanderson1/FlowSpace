from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from webchat.models import Chat
from webchat.serializers import ChatSerializer

class GetUserChatMessages(viewsets.ModelViewSet, APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        responseData = ChatSerializer(Chat.objects.filter(usuarios=request.user), many=True).data[0]
        return Response(responseData)
    
    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        data = ChatSerializer(Chat.objects.filter(id=id), many=True).data[0]
        return Response(data)
    
    def create(self, request, *args, **kwargs):
        responseData = {'mensagem':'Não permitido!'}
        return Response(responseData)
    
    def destroy(self, request, *args, **kwargs):
        responseData = {'mensagem':'Não permitido!'}
        return Response(responseData)
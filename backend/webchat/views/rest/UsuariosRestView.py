from rest_framework import viewsets

from webchat.serializers import UserSerializer
from webchat.models import Usuario
class UsuariosRestView(viewsets.ModelViewSet):

    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from webchat.serializers import UserSerializer

class UsuariosRestView(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
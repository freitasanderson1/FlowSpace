from rest_framework import serializers

from webchat.models import Usuario

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = Usuario
    fields = ('url', 'id', 'first_name', 'last_name', 'username', 'password', 'email', 'imagemPerfil', 'imagemCapa', 'seguindo', 'seguidores', 'qtdSeguindo', 'qtdSeguidores', 'last_login', 'date_joined')
    extra_kwargs = {
        'password': {'write_only':True}
    }
        
  def create(self, validated_data):
    user = Usuario(
      username = validated_data['username'],
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      email = validated_data['email'],
      dataAniversario = validated_data['dataAniversario'],
    )

    user.set_password(validated_data['password'])
    user.save()

    return user
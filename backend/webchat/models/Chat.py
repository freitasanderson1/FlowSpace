from django.db import models
import uuid

from webchat.models import Usuario

class Chat(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  usuarios = models.ManyToManyField(Usuario, verbose_name="Usuários no Chat")
  dataCriacao = models.DateTimeField('Data de Criação', auto_now_add=True, null=True)

  class Meta:
    verbose_name = 'Chat'
    verbose_name_plural = 'Chats'
    ordering = ['dataCriacao']

  def __str__(self):
    return f'Conversa entre: {"-".join(list(self.usuarios.all().values_list("username", flat=True)))}'
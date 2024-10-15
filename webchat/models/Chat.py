from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
  usuarios = models.ManyToManyField(User, verbose_name="Usuários no Chat")
  dataCriacao = models.DateTimeField('Data de Criação', auto_now_add=True, null=True)

  class Meta:
    verbose_name = 'Chat'
    verbose_name_plural = 'Chats'
    ordering = ['dataCriacao']

  def __str__(self):
    return f'Conversa entre: {"-".join(list(self.usuarios.all().values_list("username", flat=True)))}'
from django.db import models
import uuid

from webchat.models import Usuario, Chat

class ChatRequest(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  usuario = models.ForeignKey(Usuario, related_name='usuario_solicitante', verbose_name="Usuário que solicitou o Chat", on_delete=models.PROTECT)
  usuarioDestino = models.ForeignKey(Usuario, related_name='usuario_alvo', verbose_name="Usuário alvo do Chat", on_delete=models.PROTECT)

  chat = models.ForeignKey(Chat, verbose_name="Chat", on_delete=models.SET_NULL, null=True, blank=True)
  mensagem = models.TextField(u'Conteúdo da Mensagem de solicitação', max_length=300, null=False, blank=False, default=' ')
  
  aceito = models.BooleanField(verbose_name='Aceitou a solicitação?', default=False)

  dataCriacao = models.DateTimeField('Data de Criação', auto_now_add=True, null=True)

  class Meta:
    verbose_name = 'Solicitação de Chat'
    verbose_name_plural = 'Solicitações de Chats'
    ordering = ['dataCriacao']

  def save(self, *args, **kwargs):
    if self.aceito and not self.chat:
      novoChat = Chat()
      novoChat.id=uuid.uuid4()
      novoChat.save()

      novoChat.usuarios.add(self.usuario)
      novoChat.usuarios.add(self.usuarioDestino)

      self.chat = novoChat.id
      
    super(ChatRequest, self).save()
    
  def __str__(self):
    return f'Solicitação de conversa entre {self.usuario.username} e {self.usuarioDestino.username}'
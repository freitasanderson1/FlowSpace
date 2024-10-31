from django.db import models

from webchat.models import Usuario, Chat

class ChatMessages(models.Model):
  chat = models.ForeignKey(Chat, verbose_name="Chat", on_delete=models.CASCADE)

  conteudo = models.TextField(u'Conteúdo da Mensagem', max_length=2800, null=False, blank=False, default=' ')

  quemEnviou = models.ForeignKey(Usuario, verbose_name="Quem enviou", related_name='quemEnviou', on_delete=models.CASCADE)
  quemRecebeu = models.ManyToManyField(Usuario, verbose_name="Usuários que receberam", related_name='quemRecebeu')
  quemLeu = models.ManyToManyField(Usuario, verbose_name="Usuários que leram", related_name='quemLeu')

  dataEnvio = models.DateTimeField('Data de Envio', auto_now_add=True, null=True)

  class Meta:
    verbose_name = 'Message'
    verbose_name_plural = 'Messages'
    ordering = ['chat','dataEnvio']

  def __str__(self):
    return f'Mensagem no Chat {self.chat} enviada por {self.quemEnviou}'
  
  def save(self, *args, **kwargs):
    self.conteudo = self.conteudo.strip()
    
    return super(ChatMessages, self).save()
from django.db import models

from webchat.models import Usuario

INTERACAO_CHOICES = (
  (1,'Post'),
  (2,'Resposta'),
  (3,'Repostagem'), 
)

class Post(models.Model):

  conteudo = models.TextField(u'Conteúdo da Mensagem', max_length=300, null=False, blank=False, default=' ')
  quemPostou = models.ForeignKey(Usuario, verbose_name="Quem enviou", related_name='quemPostou', on_delete=models.CASCADE)

  interacao = models.ForeignKey('self', verbose_name="Repostagem", null=True, blank=True, on_delete=models.SET_NULL)
  tipoInteracao = models.IntegerField(u'Tipo de Interação', choices=INTERACAO_CHOICES, default=1)

  curtidas = models.ManyToManyField(Usuario, verbose_name="Usuários que curtiram", related_name='curtidas')
  salvo = models.ManyToManyField(Usuario, verbose_name="Usuários que salvaram", related_name='salvo')

  qtCurtidas = models.IntegerField(verbose_name='Quantidade de Curtidas', default=0)
  qtRepostagens = models.IntegerField(verbose_name='Quantidade de Repostagens', default=0)
  qtSalvo = models.IntegerField(verbose_name='Quantidade de Salvamentos', default=0)

  dataEnvio = models.DateTimeField('Data de Envio', auto_now_add=True, null=True)

  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'
    ordering = ['dataEnvio']

  def __str__(self):
    return f'Post de {self.quemPostou} -Tipo: {self.get_tipoInteracao_display()} Curtidas: {self.qtCurtidas} Repostagens: {self.qtRepostagens} Salvo: {self.qtSalvo}'
  
  def save(self, *args, **kwargs):
    self.conteudo = self.conteudo.strip()
    
    return super(Post, self).save()
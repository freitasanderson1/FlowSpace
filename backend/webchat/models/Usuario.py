from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
  dataAniversario = models.DateField(verbose_name="Data de Aniversário", null=True)

  imagemPerfil = models.ImageField(blank=True,upload_to='Perfil')
  imagemCapa = models.ImageField(blank=True,upload_to='Capa')

  seguindo = models.ManyToManyField('Usuario',related_name='Seguindo', blank=True)
  seguidores = models.ManyToManyField('Usuario', related_name='Seguidores', blank=True)
  
  qtdSeguindo = models.IntegerField(verbose_name='Quantidade Seguindo', default=0)
  qtdSeguidores = models.IntegerField(verbose_name='Quantidade Seguidores', default=0)

  groups = models.ManyToManyField(Group, verbose_name='Grupos de Permissões', blank=True, help_text='Os grupos aos quais este usuário pertence.', related_name='usuario_set', related_query_name='usuario')
  user_permissions = models.ManyToManyField(Permission, verbose_name='Permissões de Usuários', blank=True, help_text='Permissões específicas para este usuário.', related_name='usuario_permissions', related_query_name='usuario')

  def __str__(self):
    return f'{self.get_full_name()} ({self.username})'
  
  class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'
from django.db import models

from webchat.models import Post

class PostMedia(models.Model):
  post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
  template_file = models.FileField(upload_to=f'post', verbose_name='File')
  
  class Meta:
    verbose_name = 'Post Media'
    verbose_name_plural = 'Post Medias'

  def __str__(self):
    return f'Media {self.id} do Post {self.post.id} de {self.post.quemPostou}'
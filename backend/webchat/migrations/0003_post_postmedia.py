# Generated by Django 5.1.2 on 2024-10-31 01:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webchat', '0002_alter_chatmessages_options_chatrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField(default=' ', max_length=300, verbose_name='Conteúdo da Mensagem')),
                ('tipoInteracao', models.IntegerField(choices=[(1, 'Post'), (2, 'Resposta'), (3, 'Repostagem')], default=1, verbose_name='Tipo de Interação')),
                ('qtCurtidas', models.IntegerField(default=0, verbose_name='Quantidade de Curtidas')),
                ('qtRepostagens', models.IntegerField(default=0, verbose_name='Quantidade de Repostagens')),
                ('qtSalvo', models.IntegerField(default=0, verbose_name='Quantidade de Salvamentos')),
                ('dataEnvio', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Envio')),
                ('curtidas', models.ManyToManyField(related_name='curtidas', to=settings.AUTH_USER_MODEL, verbose_name='Usuários que curtiram')),
                ('interacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webchat.post', verbose_name='Repostagem')),
                ('quemPostou', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quemPostou', to=settings.AUTH_USER_MODEL, verbose_name='Quem enviou')),
                ('salvo', models.ManyToManyField(related_name='salvo', to=settings.AUTH_USER_MODEL, verbose_name='Usuários que salvaram')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['dataEnvio'],
            },
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_file', models.FileField(upload_to='post', verbose_name='File')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webchat.post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Post Media',
                'verbose_name_plural': 'Post Medias',
            },
        ),
    ]

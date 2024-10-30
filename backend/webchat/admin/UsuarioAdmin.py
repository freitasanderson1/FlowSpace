from django.contrib import admin

from webchat.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','username','qtdSeguindo','qtdSeguidores','date_joined')
    search_fields = ('id','username','qtdSeguindo','qtdSeguidores','date_joined')
    readonly_fields = ('qtdSeguindo','qtdSeguidores',)
    autocomplete_fields = ['seguindo','seguidores']
    icon_name = 'person'

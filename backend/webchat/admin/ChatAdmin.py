from django.contrib import admin

from webchat.models import Chat, ChatMessages

class MessagesInline(admin.TabularInline):
    model = ChatMessages
    extra = 0

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','dataCriacao')
    search_fields = ('id','dataCriacao')
    readonly_fields = ('dataCriacao',)
    autocomplete_fields = ['usuarios']
    icon_name = 'forum'
    inlines = [
        MessagesInline    
    ]

@admin.register(ChatMessages)
class ChatMessagesAdmin(admin.ModelAdmin):
    list_display = ('chat','quemEnviou','dataEnvio')
    search_fields = ('chat','quemEnviou','dataEnvio')
    exclude = ('id',)
    readonly_fields = ('dataEnvio',)
    autocomplete_fields = ['chat','quemEnviou','quemLeu','quemRecebeu']
    icon_name = 'message'
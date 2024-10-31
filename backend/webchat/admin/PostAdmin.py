from django.contrib import admin

from webchat.models import Post, PostMedia

class MediaInline(admin.TabularInline):
    model = PostMedia
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','dataEnvio')
    search_fields = ('id','dataEnvio')
    readonly_fields = ('dataEnvio',)
    autocomplete_fields = ['quemPostou','interacao','curtidas','salvos']
    icon_name = 'forum'
    inlines = [
        MediaInline    
    ]
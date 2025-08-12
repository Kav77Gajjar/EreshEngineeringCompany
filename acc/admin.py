from django.contrib import admin
from .models import *

admin.site.site_header = "Aatmabhav's Admin"
admin.site.site_title = "Aatmabhav's Admin Portal"
admin.site.index_title = "Welcome to Aatmabhav's Admin Dashboard"

admin.site.register(AboutMe)
admin.site.register(SocialLinks)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'slug')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'image_url', 'content')

    class Media:
        css = {
            'all': ('admin/css/widgets.css',)
        }




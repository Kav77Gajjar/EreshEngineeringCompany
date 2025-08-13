from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from .models import *


admin.site.site_header = "Aatmabhav's Admin"
admin.site.site_title = "Aatmabhav's Admin Portal"
admin.site.index_title = "Welcome to Aatmabhav's Admin Dashboard"

admin.site.register(AboutMe)
admin.site.register(SocialLinks)
admin.site.register(Services)

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



User = get_user_model()

LOCKED_SUPERUSER = ["gajjarkav@gmail.com", "bhavansijethva@gmail.com"]

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_superuser", "is_staff")


    def get_readonly_fields(self, request, obj=None):
        if obj and obj.email in LOCKED_SUPERUSER:
            return [ f.name for f in self.model._meta.fields ]
        return super().get_readonly_fields(request, obj)

    def has_delete_permission(self, request, obj = None):
        if obj and obj.email in LOCKED_SUPERUSER:
            return False
        return super().has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if obj.email in LOCKED_SUPERUSER:
            original = User.objects.get(pk=obj.pk)
            obj.username = original.username
            obj.email = original.email
            obj.password = original.password
            obj.is_superuser = original.is_superuser
            obj.is_staff = original.is_staff
            obj.is_active = original.is_active
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.email in LOCKED_SUPERUSER:
            raise PermissionDenied("You cannot delete this user.")
        super().delete_model(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


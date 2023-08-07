from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'created_at', 'updated_at')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)
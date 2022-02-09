from django.contrib import admin
from .models import CustomUser, Expense, Tag, Goal
from django.contrib.auth.admin import UserAdmin

class CustomUserAdminConfig(UserAdmin):
    search_fields = ('email',)
    ordering = ('id',)
    list_display = ('email', 'id',)
    fieldsets = (
        (None, {
            'fields':('email',)
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )

admin.site.register(CustomUser, CustomUserAdminConfig)
admin.site.register(Expense)
admin.site.register(Tag)
admin.site.register(Goal)
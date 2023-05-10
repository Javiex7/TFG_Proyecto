from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from profiles.models import Profile


# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Perfil"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'email')}),
        ('Permissions', {
         'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    ]
    readonly_fields = ['last_login', 'date_joined']


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

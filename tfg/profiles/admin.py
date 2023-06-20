from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from profiles.models import Profile


# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Perfil"
    filter_horizontal = ['purchased_packs']


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff']
    inlines = [ProfileInline]

    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'email')}),
        ('Permissions', {
         'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Fechas relevantes', {'fields': ('last_login', 'date_joined')}),
    ]
    readonly_fields = ['last_login', 'date_joined']

    def save_model(self, request, obj, form, change):
        try:
            obj.email = obj.username
            super().save_model(request, obj, form, change)

        except:
            super().save_model(request, obj, form, change)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

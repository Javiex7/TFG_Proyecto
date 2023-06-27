from django.contrib import admin
from categories.models import PointPackModel, CustomImageModel


class PointPackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'price']
    search_fields = ['name', 'code']
    filter_horizontal = ['images']


admin.site.register(PointPackModel, PointPackAdmin)


class CustomImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']
    search_fields = ['name', 'code']


admin.site.register(CustomImageModel, CustomImageAdmin)

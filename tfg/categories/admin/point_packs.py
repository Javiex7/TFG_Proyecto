from django.contrib import admin
from categories.models import PointPackModel, CustomImageModel


class PointPackAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'price']
    filter_horizontal = ['images']


admin.site.register(PointPackModel, PointPackAdmin)


class CustomImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


admin.site.register(CustomImageModel, CustomImageAdmin)

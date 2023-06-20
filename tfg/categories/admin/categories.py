from django.contrib import admin
from categories.models import CategoryModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
    filter_horizontal = ['files', 'packs']


admin.site.register(CategoryModel, CategoryAdmin)

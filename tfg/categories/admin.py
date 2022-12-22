from django.contrib import admin
from categories.models import CategoryModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')


admin.site.register(CategoryModel, CategoryAdmin)

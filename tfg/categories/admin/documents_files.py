from django.contrib import admin
from categories.models.documents_files import DocumentFileModel


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(DocumentFileModel, DocumentAdmin)

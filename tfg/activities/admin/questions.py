from django.contrib import admin
from activities.models.questions import QuestionModel


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'code']


admin.site.register(QuestionModel, QuestionAdmin)

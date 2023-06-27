from django.contrib import admin
from activities.models.quizzes import QuizModel


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']
    search_fields = ['name']
    filter_horizontal = ['questions',]


admin.site.register(QuizModel, QuizAdmin)

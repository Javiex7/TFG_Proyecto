from django.contrib import admin
from activities.models.user_quizzes import UserQuizModel


class UserQuizAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz']


admin.site.register(UserQuizModel, UserQuizAdmin)

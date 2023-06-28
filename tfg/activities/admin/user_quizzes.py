import time

from django.contrib import admin
from activities.models.user_quizzes import UserQuizModel


class UserQuizAdmin(admin.ModelAdmin):
    def customTime(self, instance):
        hours, remainder = divmod(instance.best_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = instance.best_time.microseconds // 1000
        return "{}m {}s {}ms".format(minutes, seconds, milliseconds) + " ---- Mejor tiempo consiguiendo la máxima puntuación"

    customTime.short_description = 'Mejor tiempo'

    list_display = ['id', 'user', 'quiz']
    search_fields = ['user__email', 'quiz__name', 'quiz__code']
    readonly_fields = ('customTime',)

    fieldsets = [
        (None, {'fields': ('quiz', 'user')}),
        ('Estadísticas', {
         'fields': ('tries', 'correct_answers', 'customTime')}),
    ]


admin.site.register(UserQuizModel, UserQuizAdmin)

from django.db import models


class Options(models.TextChoices):
    OPTION_A = "Opción A"
    OPTION_B = "Opción B"
    OPTION_C = "Opción C"
    OPTION_D = "Opción D"


class QuestionModel(models.Model):
    class Meta:
        app_label = "activities"
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    question = models.CharField(
        max_length=256,
        verbose_name="Pregunta",
        help_text="Texto de la pregunta"
    )
    code = models.CharField(
        max_length=256,
        verbose_name="Código",
        help_text="Código para identificar rápidamente preguntas/quiz",
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='data/questions/questions_images/',
        verbose_name="Imagen",
        null=True,
        blank=True
    )
    option_a = models.CharField(
        max_length=256,
        verbose_name="Opción A",
    )
    option_b = models.CharField(
        max_length=256,
        verbose_name="Opción B",
    )
    option_c = models.CharField(
        max_length=256,
        verbose_name="Opción C",
    )
    option_d = models.CharField(
        max_length=256,
        verbose_name="Opción D",
    )
    correct_option = models.CharField(
        max_length=256,
        choices=Options.choices,
        default=Options.OPTION_A,
    )

    def __str__(self):
        if (self.code):
            return '%s - %s' % (self.code, self.question)
        return self.question

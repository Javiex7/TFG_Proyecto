# Generated by Django 4.1.4 on 2023-05-10 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question",
                    models.CharField(
                        help_text="Texto de la pregunta",
                        max_length=256,
                        verbose_name="Pregunta",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True,
                        help_text="Código para identificar rápidamente preguntas/quiz",
                        max_length=256,
                        null=True,
                        verbose_name="Código",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="data/questions/questions_images/",
                        verbose_name="Imagen",
                    ),
                ),
                ("option_a", models.CharField(max_length=256, verbose_name="Opción A")),
                ("option_b", models.CharField(max_length=256, verbose_name="Opción B")),
                ("option_c", models.CharField(max_length=256, verbose_name="Opción C")),
                ("option_d", models.CharField(max_length=256, verbose_name="Opción D")),
                (
                    "correct_option",
                    models.CharField(
                        choices=[
                            ("Opción A", "Option A"),
                            ("Opción B", "Option B"),
                            ("Opción C", "Option C"),
                            ("Opción D", "Option D"),
                        ],
                        default="Opción A",
                        max_length=256,
                    ),
                ),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "Questions",
            },
        ),
        migrations.CreateModel(
            name="QuizModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Nombre del quiz",
                        max_length=256,
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Pequeña descripción del quiz",
                        max_length=256,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "max_tries",
                    models.PositiveIntegerField(
                        default=3,
                        help_text="Número máximo de intentos para realizar el cuestionario",
                        verbose_name="Intentos",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True,
                        help_text="Código para identificar rápidamente preguntas/quiz",
                        max_length=256,
                        null=True,
                        verbose_name="Código",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Categoría del quiz",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="quizzes",
                        to="categories.categorymodel",
                        verbose_name="Categoría",
                    ),
                ),
                (
                    "questions",
                    models.ManyToManyField(
                        related_name="quizzes", to="activities.questionmodel"
                    ),
                ),
            ],
            options={
                "verbose_name": "Quiz",
                "verbose_name_plural": "Quizzes",
            },
        ),
        migrations.CreateModel(
            name="UserQuizModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quiz",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_quizzes",
                        to="activities.quizmodel",
                        verbose_name="Quiz",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_quizzes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "User quiz",
                "verbose_name_plural": "User quizzes",
            },
        ),
    ]

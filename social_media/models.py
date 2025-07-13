from django.core.exceptions import ValidationError
from django.db import models

from social_media.validators import AgeValidator, TitleValidator
from users.models import User


class Post(models.Model):
    """Модель поста"""

    title = models.CharField(verbose_name="Заголовок", max_length=255)
    text = models.TextField(verbose_name="Текст", max_length=10000)
    image = models.ImageField(
        verbose_name="Изображение (необязательно)",
        upload_to="posts/",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        related_name="author_posts",
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата редактирования"
    )

    def clean(self):
        super().clean()
        # Проверка возраста автора
        if self.author and self.author.date_of_birth:
            AgeValidator(field="author")(self.author.date_of_birth)
        else:
            raise ValidationError("У автора должна быть указана дата рождения.")

        # Проверка заголовка
        TitleValidator(field="title")(self.title)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Модель комментария"""

    post = models.ForeignKey(
        Post,
        verbose_name="Пост",
        related_name="post_comments",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        related_name="author_comments",
        on_delete=models.CASCADE,
    )
    text = models.TextField(verbose_name="Текст", max_length=10000)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата редактирования"
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

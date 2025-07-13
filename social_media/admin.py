from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from social_media.models import Comment, Post


class CommentInline(admin.TabularInline):
    """Создаем Inline для отображения в админке у поста только связанные комментарии"""

    model = Comment
    extra = 0
    # Отображаем в Inline только автора и дату создания комментария
    fields = ("author", "text", "date_created")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Регистрируем в админке модель поста"""

    inlines = [CommentInline]
    list_display = ("id", "title", "author_link", "date_created", "date_updated")
    # Фильтр по дате создания
    list_filter = ("date_created",)

    def author_link(self, obj):
        # Создаем ссылку на автора в админке при помощи reverse
        url = reverse("admin:users_user_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', url, obj.author.username)

    author_link.short_description = "Автор"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Регистрируем в админке модель комментария"""

    list_display = ("post", "author", "text", "date_created")
    search_fields = ("text",)
    list_filter = ("date_created",)

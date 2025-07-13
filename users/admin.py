from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрируем в админке модель пользователя"""

    list_display = ("id", "username", "email", "date_of_birth")

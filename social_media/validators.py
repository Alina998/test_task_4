from datetime import date

from django.core.exceptions import ValidationError


class AgeValidator:
    """Проверка возраста"""

    def __init__(self, field):
        self.field = field

    def __call__(self, date_of_birth):
        today = date.today()
        age = (
            today.year
            - date_of_birth.year
            - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        )
        if age < 18:
            raise ValidationError("Автор поста должен быть не младше 18 лет.")


forbidden_words = ["ерунда", "глупость", "чепуха"]


class TitleValidator:
    """Проверка на наличие запрещенных слов в заголовке"""

    def __init__(self, field):
        self.field = field

    def __call__(self, title):
        title_lower = title.lower()
        for word in forbidden_words:
            if word in title_lower:
                raise ValidationError(
                    f"В заголовке поста запрещено использовать слово: {word}."
                )

from django.core.exceptions import ValidationError


def validate_password(value):
    """Валидатор для пароля (должен быть не менее 8 символов, должен включать цифры)."""
    if len(value) < 8:
        raise ValidationError("Пароль должен быть не менее 8 символов.")
    if not any(symb.isdigit() for symb in value):
        raise ValidationError("Пароль должен включать цифры.")


def validate_email(value):
    """Валидатор для почты (разрешены домены: mail.ru, yandex.ru)."""
    allowed_domains = ["mail.ru", "yandex.ru"]
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError(f'Разрешенные домены: {", ".join(allowed_domains)}.')

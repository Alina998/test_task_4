from rest_framework import serializers

from users.models import User
from users.validators import validate_email, validate_password


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""

    password = serializers.CharField(
        write_only=True, validators=[validate_password]
    )  # Валидатор пароля
    email = serializers.EmailField(
        validators=[validate_email]
    )  # Валидатор электронной почты

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "phone_number",
            "date_of_birth",
            "date_created",
            "date_updated",
        ]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            phone_number=validated_data.get("phone_number"),
            date_of_birth=validated_data.get("date_of_birth"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

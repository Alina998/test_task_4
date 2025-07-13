from rest_framework import permissions, viewsets

from users.models import User
from users.permissions import IsOwnerOrAdmin
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Представление пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # Регистрация: доступна всем
        if self.action == "create":
            return [permissions.AllowAny()]
        # Чтение: доступно администраторам или авторизованным пользователям
        elif self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticated()]
        # Обновление: доступно администратору или владельцу аккаунта
        elif self.action in ["update", "partial_update"]:
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
        # Удаление пользователя: доступно только администраторам
        elif self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return [permissions.IsAuthenticated()]

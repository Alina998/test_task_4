from rest_framework import permissions, viewsets

from social_media.models import Comment, Post
from social_media.serializers import CommentSerializer, PostSerializer
from users.permissions import IsOwnerOrAdmin


class PostViewSet(viewsets.ModelViewSet):
    """Представление для поста"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        # Создание: авторизованные пользователи
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        # Чтение: все пользователи
        elif self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticatedOrReadOnly()]
        # Обновление: администраторы или владельцы
        elif self.action in ["update", "partial_update"]:
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
        # Удаление: администраторы или владельцы
        elif self.action == "destroy":
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
        else:
            return [permissions.IsAuthenticated()]


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для комментариев"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        # Создание: авторизованные пользователи
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        # Чтение: все пользователи
        elif self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticatedOrReadOnly()]
        # Обновление: администраторы или владельцы
        elif self.action in ["update", "partial_update"]:
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
        # Удаление: администраторы или владельцы
        elif self.action == "destroy":
            return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
        else:
            return [permissions.IsAuthenticated()]

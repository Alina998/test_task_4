from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """Проверка разрешения: только для владельцев или администратора"""

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user

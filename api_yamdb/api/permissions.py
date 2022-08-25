from rest_framework import permissions

from reviews.models import UserRole


class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_staff
                )

    def has_object_permission(self, request, view, obj):
        return (request.user.is_staff
                or request.method in permissions.SAFE_METHODS)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            is_admin = request.user.role == UserRole.value
            return is_admin or request.user.is_superuser
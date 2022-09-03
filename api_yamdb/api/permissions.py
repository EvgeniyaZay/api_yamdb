from rest_framework import permissions

from user.models import UserRole


class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                        request.user.role == UserRole.ADMIN.value
                        or request.user.is_superuser)))


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
                request.user.role == UserRole.ADMIN.value
                or request.user.is_superuser)


class IsAdminOrIsModeratorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.role == UserRole.MODERATOR.value
                or request.user.role == UserRole.ADMIN.value)

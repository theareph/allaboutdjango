import typing as t
from rest_framework import permissions

class IsAdminOrReadonly(permissions.BasePermission):
    @t.override
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_admin)
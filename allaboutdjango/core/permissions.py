import typing as t
from rest_framework import permissions

class IsAdminOrReadonly(permissions.BasePermission):
    @t.override
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not getattr(request, "user", None,) or not getattr(request.user, "is_admin", None):
            return False
        return bool(request.user.is_admin)
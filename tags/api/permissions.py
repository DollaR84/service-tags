from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (obj.user == request.user) or request.user.profile.is_company_admin:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.profile.is_company_admin


class IsAdminUserOrReadOnly(IsAdmin):
    def has_object_permission(self, request, view, obj):
        is_admin = super().has_object_permission(request, view, obj)
        return request.method in SAFE_METHODS or is_admin

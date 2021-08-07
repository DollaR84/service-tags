from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.profile.is_company_admin


class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (obj.user == request.user) or request.user.profile.is_company_admin:
            return True
        return False

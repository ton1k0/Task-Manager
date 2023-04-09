from rest_framework import permissions

class IsCompanyOwner(permissions.BasePermission):
    message = 'Вы должны быть владельцем компании, чтобы выполнить это действие'

    def has_object_permission(self, request, view, obj):
        return request.user in obj.owners.all()
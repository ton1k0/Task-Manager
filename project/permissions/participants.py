from rest_framework import permissions


class IsParticipant(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
        return request.user in view.get_object().participants.all()
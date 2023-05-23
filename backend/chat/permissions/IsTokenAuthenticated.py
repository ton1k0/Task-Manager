from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication


class IsTokenAuthenticated(BasePermission):
    def has_permission(self, request, view):
        jwt_auth = JWTAuthentication()
        try:
            user, token = jwt_auth.authenticate(request)
            return bool(user)
        except:
            return False

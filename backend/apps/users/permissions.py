from rest_framework.permissions import BasePermission

from .models import User


class ModeratorOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.ROLES.MODERATOR

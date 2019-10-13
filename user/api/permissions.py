from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, views, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj == request.user or request.user.is_superuser

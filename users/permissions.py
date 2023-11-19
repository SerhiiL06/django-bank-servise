from rest_framework.permissions import BasePermission


class OwnerOrSuperser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id or request.user.is_staff:
            return True

        return False

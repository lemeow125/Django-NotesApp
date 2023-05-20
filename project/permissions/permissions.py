from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow the creator of an object to view and manipulate it.
    """
    def has_object_permission(self, request, view, obj):
        # Only allow the creator of the object to view and manipulate it.
        return obj.creator == request.user
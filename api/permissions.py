from rest_framework.permissions import BasePermission
from .models import Bucketlist


class IsOwner(BasePermission):
    """Custom permission class to allow only Bucketlist owners to edit them."""

    def has_objects_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, Bucketlist):
            return obj.owner == request.user
        return obj.owner == request.user

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the request method is in the list of safe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # For non-safe methods, check if the user is authenticated and is an admin
        return bool(request.user and request.user.is_staff)

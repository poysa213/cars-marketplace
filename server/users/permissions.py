from rest_framework import permissions

class IsOwnerOrAdminOrReadOnlyProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return  bool((obj.user == request.user) or  (request.user and request.user.is_staff))
    
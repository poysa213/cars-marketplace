from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return bool(request.user and request.user.is_staff)
    
class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool((obj.seller == request.user) or  (request.user and request.user.is_staff))
    
class IsOwnerOrAdminOrReadOnlySeller(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool((obj.seller == request.user) or  (request.user and request.user.is_staff))
    
class IsOwnerOrAdminOrReadOnlyImageOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return  bool((obj.car.seller == request.user) or  (request.user and request.user.is_staff))
    
class IsOwnerOrAdminOrReadOnlyProviderOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return  bool((obj.user == request.user) or  (request.user and request.user.is_staff))
    
    



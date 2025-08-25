from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsMoverOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'move':
            return request.user and (request.user.is_staff or request.user.groups.filter(name='Смотритель').exists())
        if request.method in SAFE_METHODS:
            return True
        return False

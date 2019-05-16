from rest_framework.permissions import BasePermission

from photos.models import Photo


class PhotoPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action == ['list', 'retrieve'] or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return obj.visibility == Photo.PUBLIC or obj.owner == request.user or request.user.is_superuser

        return obj.owner == request.user or request.user.is_superuser

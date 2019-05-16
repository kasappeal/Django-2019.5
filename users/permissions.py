from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        from users.api import UserDetailAPI
        # Endpoint de listado (GET): solo admin
        # Edpoint de creacion (POST): cualquier usuario
        # Endpoint de detalle (GET): usuario autenticado sólo a sus datos o admin a todos
        # Endpoint de actualizacion (PUT): usuario autenticado sólo a sus datos o admin a todos
        # Endpoint de borrado (DELETE): usuario autenticado sólo a sus datos o admin a todos
        if request.method == 'POST' or request.user.is_superuser:
            return True

        return request.user.is_authenticated and isinstance(view, UserDetailAPI)

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj

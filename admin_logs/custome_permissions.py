from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class SuperAdminPermission(BasePermission):
    def has_permission(self, request, view):
        admin = request.session.get('admin')
        try:
            admin = User.objects.get(username=admin)
        except User.DoesNotExist:
            return False
        if admin.is_superuser():
            return True
        else:
            return False
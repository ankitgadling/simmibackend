from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User


class AdminIsInTheSession(BaseAuthentication):
    def authenticate(self, request):
        username = request.session.get('admin',None)
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('User Not athenticated..!')
        return (user , None)
    
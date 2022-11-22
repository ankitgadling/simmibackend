from django.urls import path
from admin_logs.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('login',admin_login.as_view()),
    path('logout',admin_logout.as_view()),
    path('change_password',ChangePassword.as_view()),
    path('get_token_by_user/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),
    path('token_delete/', TokenBlacklistView.as_view()), 
]

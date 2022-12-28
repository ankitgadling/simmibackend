from django.urls import path
from admin_logs.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('login',admin_login.as_view()),
    #path('logout',admin_logout.as_view()),
    path('change_password',ChangePassword.as_view()),
    path('update',ProfileUpdate.as_view()),
    path('get_token_by_user/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout', TokenBlacklistView.as_view()), 
]

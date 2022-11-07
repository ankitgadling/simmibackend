from django.urls import path
from admin_logs.views import *
urlpatterns = [
    path('login',admin_login.as_view()),
    path('logout',admin_logout.as_view()),
]

from .views import register_api, Login_api
from knox.views import LogoutView
from django.urls import path

urlpatterns = [
    path('register', register_api.as_view(), name='register'),
    path('login', Login_api.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

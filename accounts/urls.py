from .views import register_api, Login_api, user
#from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('register/', register_api.as_view(), name='register'),
    path('login/', Login_api.as_view(), name='login'),
    #path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('user/', user, name='user'),
]

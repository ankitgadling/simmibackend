from .views import register_api, Login_api , userdetailsupdateview,userprofileupdateview,ChangePassword,LogoutUser
from django.urls import path

urlpatterns = [
    path('register', register_api.as_view(), name='register'),
    path('login', Login_api.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    path('user_details_update/<pk>',userdetailsupdateview.as_view()),
    path('user_profile_update/<pk>',userprofileupdateview.as_view()),
    path('changepass',ChangePassword.as_view()),
    ]

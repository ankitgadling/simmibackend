from .views import List_users_pisc, profileDetail
from django.urls import path

urlpatterns = [
    path('user/', List_users_pisc.as_view(), name='users'),
    path('user/<int:pk>/', profileDetail.as_view(), name='user')
]

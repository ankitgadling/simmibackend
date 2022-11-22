from django.urls import path
from .views import *
urlpatterns = [
    path('',contact),
    path('response/',responseapi.as_view()),
    path('admin_response/',adminresponseapi.as_view()),
    path('admin_response/<pk>',admineditresponseapi.as_view()),
    ]

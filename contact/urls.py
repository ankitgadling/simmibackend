from django.urls import path
from .views import *
urlpatterns = [
    path('',contact),
    path('response/',responseapi.as_view()),
    ]

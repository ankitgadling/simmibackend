from django.urls import path
from .views import *
urlpatterns = [
    path('',navbarAPI.as_view()),
    path("<pk>",navbarupdateAPI.as_view()),
    ]

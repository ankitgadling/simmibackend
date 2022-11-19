from django.urls import path
from .views import *
urlpatterns = [
    path('',admintenderapi.as_view()),
    path('<pk>',tendermodificationapi.as_view()),
    ]


from django.urls import path
from .views import *

urlpatterns = [
    path("getallevents/",AllEvents.as_view()),
    path('eventcreate/',EventCreateView.as_view()),
    path('eventmodify/<pk>',EventModifyView.as_view()),
]

from django.urls import path
from .views import *

urlpatterns = [
    path("getallevents/",AllEvents.as_view()),
    path('eventcreate',EventCreateView.as_view()),
    path('eventmodify/<pk>',EventModifyView.as_view()),
    path('speakers/', AllSpeakers.as_view()),
    path('post-speaker/', PostSpeaker.as_view()),
    path('CRUD-speaker/<pk>', CRUDSpeaker.as_view()),
]
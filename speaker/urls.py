from django.urls import path
from .views import *


urlpatterns = [
    path('speakers/', AllSpeakers.as_view()),
    path('post-speaker/', PostSpeaker.as_view()),
    path('CRUD-speaker/<pk>', CRUDSpeaker.as_view()),
]

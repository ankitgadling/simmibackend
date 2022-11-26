
from django.urls import path
from .views import *
urlpatterns = [
    path('researches',Researches.as_view()),
    path('researches/<pk>',ResearchesDetail.as_view())
]
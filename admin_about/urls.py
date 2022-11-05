from django.urls import path
from django.contrib import admin
from admin_about.views import *
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('about/',Aboutapi.as_view()),
    path("about/<pk>",Aboutapidetail.as_view()),
    path('founder/',Foundersapi.as_view()),
    path("founder/<pk>",Foundersapidetail.as_view()),
    path('advisor/',Advisorapi.as_view()),
    path("advisor/<pk>",Advisorysapidetail.as_view()),
    path('seniormanager/',Seniormanagerapi.as_view()),
    path("seniormanager/<pk>",Seniormanagerapidetail.as_view()),
    path('senior_tech/',Seniortechapi.as_view()),
    path("senior_tech/<pk>",Seniortechapidetail.as_view()),
    path('team/',Teamapi.as_view()),
    path("team/<pk>",Teamapidetail.as_view()),
    path('initiatives/',Intiativeapi.as_view()),
    path("initiatives/<pk>",Initiativesapidetail.as_view()),
    path('campaign/',Campaignapi.as_view()),
    path("campaign/<pk>",Campaignapidetail.as_view()),  
]

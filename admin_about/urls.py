from django.urls import path
from django.contrib import admin
from admin_about.views import *
from about.views import Createaboutapi,Updateaboutapi,Viewaboutapi
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('initiatives/',Intiativeapi.as_view()),
    path("initiatives/<pk>",Initiativesapidetail.as_view()),
    path('campaign/',Campaignapi.as_view()),
    path("campaign/<pk>",Campaignapidetail.as_view()), 
    path('create/',Createaboutapi.as_view()),
    path("view/",Viewaboutapi.as_view()),
    path('view/<pk>',Updateaboutapi.as_view()), 
]

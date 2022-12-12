from django.urls import path
from about.views import *
urlpatterns = [
    # path('',Aboutapi.as_view()),
    # path('founder/',Foundersapi.as_view()),
    # path('founder/<pk>/',Founderupdatedetail.as_view()),
    # path('advisor/',Advisorapi.as_view()),
    # path('advisor/<pk>/',Advisoryupdatedetail.as_view()),
    # path('senior_manager/',Seniormanagerapi.as_view()),
    # path('senior_manager/<pk>/',Seniormanupdatedetail.as_view()),
    # path('senior_tech/',Seniortechapi.as_view()),
    # path('senior_tech/<pk>/',Seniortechupdatedetail.as_view()),
    # path('team/',Teamapi.as_view()),
    # path('team/<pk>/',Teamupdatedetail.as_view()),
    path('intiatives/',Intiativeapi.as_view()),
    path('campaign/',Campaignapi.as_view()),
    path('create/',Createviewaboutapi.as_view()),
    path('create/<pk>',Updateaboutapi.as_view()),

    ]

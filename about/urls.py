from django.urls import path
from about.views import *
urlpatterns = [
    # path('',Aboutapi.as_view()),
    # path('founder/',Foundersapi.as_view()),
    # path('advisor/',Advisorapi.as_view()),
    # path('senior_manager/',Seniormanagerapi.as_view()),
    # path('senior_tech/',Seniortechapi.as_view()),
    # path('team/',Teamapi.as_view()),
    path('intiatives/',Intiativeapi.as_view()),
    path('campaign/',Campaignapi.as_view()),
    path('view/',Viewaboutapi.as_view()),
    ]

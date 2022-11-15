from django.urls import path
from institutional_aliance.views import *
urlpatterns = [
    path('coparate/',Copatnerapi.as_view()),
    path('',Alliance.as_view()),
    path('<pk>',DetailedAlliance.as_view()),

    ]

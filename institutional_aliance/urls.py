from django.urls import path
from institutional_aliance.views import *
urlpatterns = [
    # path('coparate/',Copatnerapi.as_view()),
    # path('',Alliance.as_view()),
    # path('<pk>',DetailedAlliance.as_view()),
    # path('adminco/',AdminCopatnerapi.as_view()),
    # path('adminco/<pk>',AdmineditCopatnerapi.as_view()),
    path('adminalliance/',AdminAlliance.as_view()),
    path('adminalliance/<pk>',AdmineditAlliance.as_view()),
    ]
